import hashlib, json, re, subprocess, zipfile
from html.parser import HTMLParser
from pathlib import Path
import fitz

root=Path(__file__).resolve().parents[4]
out=root/'tmp/CH06-draft-20261021-r2'
class Page(HTMLParser):
    def __init__(self): super().__init__(); self.ids=[]; self.images=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag=='img': self.images.append(a.get('alt',''))
result={'packages':{},'pdf':{},'website':{},'citation_parity':{}}
for locale in ('zh-TW','en-US'):
    for ext in ('docx','epub'):
        path=out/f'CH06-{locale}.{ext}'
        with zipfile.ZipFile(path) as z:
            bad=z.testzip()
            if bad: raise SystemExit(f'ZIP CRC failed: {path}: {bad}')
            result['packages'][path.name]={'crc':'PASS','members':len(z.namelist())}
    pdf=out/f'CH06-{locale}.pdf'
    doc=fitz.open(pdf)
    text='\n'.join(p.get_text() for p in doc)
    if '\ufffd' in text: raise SystemExit(f'Replacement glyph in {pdf}')
    result['pdf'][pdf.name]={'pages':len(doc),'replacement_chars':text.count('\ufffd'),'text_chars':len(text)}
    for page_idx in sorted(set([0,len(doc)-1])):
        pix=doc[page_idx].get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False)
        pix.save(out/f'{locale}-page-{page_idx+1}-proof.png')
    src=(root/'content'/locale/'chapters'/'CH06-chapter-06.md').read_text(encoding='utf-8')
    citations=sorted(set(re.findall(r'\bR\d{3}\b',src)))
    result['citation_parity'][locale]=citations
for locale,route in [('zh-TW','zh-tw'),('en-US','en')]:
    p=root/'apps/web/dist'/route/'ch06-chapter-06/index.html'
    parser=Page(); parser.feed(p.read_text(encoding='utf-8'))
    if len(parser.ids)!=len(set(parser.ids)): raise SystemExit(f'Duplicate IDs: {p}')
    if any(not x.strip() for x in parser.images): raise SystemExit(f'Empty image alt: {p}')
    result['website'][locale]={'path':p.relative_to(root).as_posix(),'unique_ids':len(parser.ids),'images':len(parser.images),'alt':'PASS'}
if result['citation_parity']['zh-TW'] != result['citation_parity']['en-US']:
    raise SystemExit('Bilingual citation ID mismatch')
(root/'production/runs/CH06/20261021T065143+0800-f153e02e/verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
