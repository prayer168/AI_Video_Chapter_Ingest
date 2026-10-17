#!/usr/bin/env python3
"""Validate book source metadata, IDs, and planned outline."""
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
try:
 import yaml
except ImportError:
 print("Install PyYAML for project validation: pip install pyyaml",file=sys.stderr); raise SystemExit(2)
errors=[]
def load(path):
 try: return yaml.safe_load(path.read_text(encoding="utf-8-sig"))
 except Exception as e: errors.append(f"{path.relative_to(ROOT)}: {e}"); return None
for name in ("terms.yaml","references.yaml","assets.yaml","prompts.yaml"):
 if not (ROOT/"data"/name).exists(): errors.append(f"Missing data/{name}")
terms=load(ROOT/"data/terms.yaml") or []
refs=load(ROOT/"data/references.yaml") or []
for name in ("assets.yaml","prompts.yaml"): load(ROOT/"data"/name)
for label,rows in (("term",terms),("reference",refs)):
 ids=[r.get("id") for r in rows if isinstance(r,dict)]
 if len(ids)!=len(set(ids)): errors.append(f"Duplicate {label} IDs")
term_ids={r.get("id") for r in terms if isinstance(r,dict)}
ref_ids={r.get("id") for r in refs if isinstance(r,dict)}
chapters=list((ROOT/"chapters").glob("*.md"))
for p in chapters:
 txt=p.read_text(encoding="utf-8-sig")
 m=re.match(r"\A---\s*\n(.*?)\n---\s*\n",txt,re.S)
 if not m: errors.append(f"{p.name}: malformed YAML front matter"); continue
 meta=yaml.safe_load(m.group(1)) or {}
 for k in ("id","part","title","status","updated","sources","terms"):
  if k not in meta: errors.append(f"{p.name}: missing metadata field {k}")
 for sid in meta.get("sources",[]):
  if sid not in ref_ids: errors.append(f"{p.name}: unknown source ID {sid}")
 for tid in meta.get("terms",[]):
  if tid not in term_ids: errors.append(f"{p.name}: unknown term ID {tid}")
toc=(ROOT/"docs/TOC.md").read_text(encoding="utf-8-sig")
count=len(re.findall(r"^\d+\.\s+.+$",toc,re.M)); parts=len(re.findall(r"^## 第.+篇",toc,re.M))
if count!=60: errors.append(f"TOC has {count} chapters; expected 60")
if parts!=12: errors.append(f"TOC has {parts} parts; expected 12")
if errors:
 print("VALIDATION FAILED")
 for e in errors: print("- "+e)
 raise SystemExit(1)
print(f"VALIDATION PASSED: {parts} parts, {count} chapters, {len(chapters)} chapter files, {len(terms)} terms, {len(refs)} reference records")
