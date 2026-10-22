from pathlib import Path
import hashlib
import yaml
R=Path(__file__).resolve().parents[1]
manifest=R/'assets/chapters/CH10/figure-manifest.yaml'
data=yaml.safe_load(manifest.read_text(encoding='utf-8'))
for figure in data['figures']:
 p=R/figure['asset_original']; s=p.read_text(encoding='utf-8')
 s=s.replace('class="zh" fill="#24344a"','class="zh title"')
 s=s.replace('class="en" fill="#526274"','class="en subtitle"')
 s=s.replace('.foot{font:14px Arial,sans-serif;fill:#657080}', '.title{fill:#24344a}.subtitle{fill:#526274}.foot{font:14px Arial,sans-serif;fill:#657080}')
 p.write_text(s,encoding='utf-8')
 raw=p.read_bytes(); figure['sha256']=hashlib.sha256(raw).hexdigest(); figure['bytes']=len(raw)
manifest.write_text(yaml.safe_dump(data,allow_unicode=True,sort_keys=False),encoding='utf-8')
p=R/'metadata/figure-registry.yaml'; d=yaml.safe_load(p.read_text(encoding='utf-8'))
byid={f['figure_id']:f for f in data['figures']}
for row in d['figures']:
 if row.get('figure_id') in byid: row['sha256']=byid[row['figure_id']]['sha256']; row['bytes']=byid[row['figure_id']]['bytes']
p.write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False),encoding='utf-8')
p=R/'data/assets.yaml'; d=yaml.safe_load(p.read_text(encoding='utf-8'))
for row in d:
 fid=row.get('figure_id')
 if fid in byid: row['sha256']=byid[fid]['sha256']
p.write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False),encoding='utf-8')
print('Updated CH10 SVG title contrast and synchronized hashes.')
