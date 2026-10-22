import hashlib, json, zipfile
from pathlib import Path
import yaml

root=Path(__file__).resolve().parents[4]
out=root/'tmp/CH06-draft-20261021-r2'
refs=yaml.safe_load((root/'data/references.yaml').read_text(encoding='utf-8'))
terms=yaml.safe_load((root/'metadata/terminology.yaml').read_text(encoding='utf-8'))
(out/'CH06-sources.yaml').write_text(yaml.safe_dump({'chapter_id':'CH06','sources':[r for r in refs if r['id'] in {'R046','R047','R048','R049','R050'}]},allow_unicode=True,sort_keys=False),encoding='utf-8')
term_ids={'TERM-CH06-STORY','TERM-CH06-PLOT','TERM-CH06-CAUSALITY','TERM-CH06-MOTIVATION','TERM-CH06-INCITING-INCIDENT','TERM-CH06-REVERSAL','TERM-CH06-RECOGNITION','TERM-CH06-FORESHADOWING'}
(out/'CH06-terms.yaml').write_text(yaml.safe_dump({'chapter_id':'CH06','terms':[t for t in terms['terms'] if t['term_id'] in term_ids]},allow_unicode=True,sort_keys=False),encoding='utf-8')
package=out/'CH06-Codex-Materials-DRAFT-r1.zip'
files=[
 root/'content/zh-TW/chapters/CH06-chapter-06.md',root/'content/en-US/chapters/CH06-chapter-06.md',
 root/'metadata/translations/CH06-alignment.yaml',root/'metadata/chapters.yaml',root/'metadata/translation-status.yaml',
 root/'metadata/terminology.yaml',root/'metadata/references.bib',root/'data/references.yaml',
 root/'CHAPTER_INTEGRATION_MATRIX.md',root/'reports/CH06-FINAL-ACCEPTANCE.md',
 root/'assets/chapters/CH06/CH06-RASHOMON-VIEWING-LOG.md',root/'assets/chapters/CH06/CH06-HUMAN-REVIEW-CHECKLIST.md',
 root/'production/runs/CH06/20261021T065143+0800-f153e02e/RESEARCH-SOURCE-CHECK.md',
 root/'production/runs/CH06/20261021T065143+0800-f153e02e/verification.json',
 root/'production/runs/CH06/20261021T065143+0800-f153e02e/backup/MANIFEST.json',
 root/'production/runs/CH06/20261021T065143+0800-f153e02e/build_drafts.py',
 root/'production/runs/CH06/20261021T065143+0800-f153e02e/verify_outputs.py',
 root/'tests/test_ch06_content.py']
files += [p for p in out.iterdir() if p.is_file() and p.suffix.lower() in {'.docx','.pdf','.epub','.png','.md','.log','.yaml'}]
files += list((root/'production/runs/CH06/20261021T065143+0800-f153e02e/backup/pre-edit').rglob('*'))
uniq=[]; seen=set()
for p in files:
 if p.is_file() and p.resolve() not in seen: uniq.append(p); seen.add(p.resolve())
rows=[]
with zipfile.ZipFile(package,'x',zipfile.ZIP_DEFLATED) as z:
 for p in uniq:
  rel=p.relative_to(root).as_posix()
  arc=rel if rel.startswith('tmp/CH06-') else 'project/'+rel
  z.write(p,arc); data=p.read_bytes()
  rows.append({'path':arc,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
with zipfile.ZipFile(package) as z:
 if z.testzip(): raise SystemExit('ZIP CRC failed')
 for row in rows:
  if hashlib.sha256(z.read(row['path'])).hexdigest()!=row['sha256']: raise SystemExit('ZIP hash mismatch: '+row['path'])
manifest={'chapter_id':'CH06','status':'draft','package':package.name,'package_sha256':hashlib.sha256(package.read_bytes()).hexdigest(),'zip_crc':'PASS','member_count':len(rows),'members':rows}
(out/'OUTPUT-MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'package':str(package),'sha256':manifest['package_sha256'],'members':len(rows),'crc':'PASS'},ensure_ascii=False))
