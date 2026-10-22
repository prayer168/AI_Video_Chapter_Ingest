import hashlib, json, zipfile
from pathlib import Path

root = Path(__file__).resolve().parents[4]
out = root / 'tmp/CH05-draft-20261021-r3'
package = out / 'CH05-Codex-Materials-DRAFT-r6.zip'
files = [
    root/'content/zh-TW/chapters/CH05-chapter-05.md',
    root/'content/en-US/chapters/CH05-chapter-05.md',
    root/'metadata/translations/CH05-alignment.yaml',
    root/'assets/chapters/CH05/figure-manifest.yaml',
    root/'assets/chapters/CH05/figure-captions.md',
    root/'assets/chapters/CH05/CH05-GET-OUT-VIEWING-LOG.md',
    root/'assets/chapters/CH05/CH05-HUMAN-REVIEW-CHECKLIST.md',
    root/'reports/CH05-FINAL-ACCEPTANCE.md',
    root/'tmp/CH05-draft-20261021-r2/CH05-sources.yaml',
    root/'tmp/CH05-draft-20261021-r2/CH05-terms.yaml',
    root/'production/runs/CH05/20261021T063754+0800-75e973e5/verification-editorial.json',
]
files += list((root/'assets/chapters/CH05/figures/originals').glob('*.svg'))
files += [p for p in out.iterdir() if p.is_file() and p.name != package.name and p.name != 'OUTPUT-MANIFEST.json' and p.suffix.lower() in {'.docx','.pdf','.epub','.png','.md'}]
unique=[]
seen=set()
for p in files:
    if p.is_file() and p.resolve() not in seen:
        unique.append(p); seen.add(p.resolve())
members=[]
with zipfile.ZipFile(package, 'x', compression=zipfile.ZIP_DEFLATED) as z:
    for p in unique:
        rel = p.relative_to(root).as_posix()
        arc = rel if rel.startswith('tmp/CH05-draft-') else 'project/'+rel
        z.write(p, arc)
        data=p.read_bytes()
        members.append({'path':arc,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
with zipfile.ZipFile(package) as z:
    bad=z.testzip()
    if bad: raise SystemExit('ZIP CRC failed: '+bad)
    names=z.namelist()
    for row in members:
        if hashlib.sha256(z.read(row['path'])).hexdigest()!=row['sha256']:
            raise SystemExit('Archive checksum mismatch: '+row['path'])
manifest={'chapter_id':'CH05','status':'draft','package':package.name,'package_sha256':hashlib.sha256(package.read_bytes()).hexdigest(),'zip_crc':'PASS','member_count':len(members),'members':members}
(out/'OUTPUT-MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'package':str(package),'sha256':manifest['package_sha256'],'members':len(members),'crc':'PASS'},ensure_ascii=False))
