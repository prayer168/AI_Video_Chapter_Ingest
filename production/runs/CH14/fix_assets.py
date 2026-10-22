from pathlib import Path
import yaml
p=Path('data/assets.yaml'); d=yaml.safe_load(p.read_text(encoding='utf-8'))
for a in d:
 if a.get('id','').startswith('ASSET-CH14-FIG-'):
  for src in a.get('research_sources',[]):src['purpose']='Conceptual context only; the SVG is an original schematic, not copied artwork.'
p.write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=120),encoding='utf-8')
