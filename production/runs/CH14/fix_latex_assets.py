from pathlib import Path
import yaml
p=Path('scripts/publishing/figure-captions.lua'); s=p.read_text(encoding='utf-8'); s=s.replace('"\\usepackage{caption}"','"\\\\usepackage{caption}"'); p.write_text(s,encoding='utf-8')
p=Path('data/assets.yaml'); d=yaml.safe_load(p.read_text(encoding='utf-8'))
for a in d:
 if a.get('id','').startswith('ASSET-CH14-FIG-'):a['rights_risk_review']['checked_at']='2026-10-22'
p.write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=120),encoding='utf-8')
