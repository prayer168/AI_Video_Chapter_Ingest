#!/usr/bin/env python3
import argparse,re,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; ap=argparse.ArgumentParser(); ap.add_argument("--online",action="store_true"); a=ap.parse_args(); links=[]
for p in [ROOT/"README.md",*ROOT.glob("docs/*.md"),*ROOT.glob("chapters/*.md")]:
 for u in re.findall(r"\[[^\]]*\]\((https?://[^)]+)\)",p.read_text(encoding="utf-8-sig")):links.append((p,u))
errors=[]
for p,u in links:
 if not a.online:
  if not re.match(r"https?://[^\s]+$",u):errors.append((p,u,"malformed"))
 else:
  try:
   q=urllib.request.Request(u,headers={"User-Agent":"AI-Filmmaking-Bible"},method="HEAD")
   with urllib.request.urlopen(q,timeout=10) as r:
    if r.status>=400:errors.append((p,u,str(r.status)))
  except Exception as e: print(f"REVIEW {p.name} {u}: {e}")
if errors:
 for p,u,e in errors:print(f"ERROR {p.name} {u}: {e}")
 raise SystemExit(1)
print(f"Link check passed: {len(links)} links"+(" (online best effort)" if a.online else " (syntax only)"))
