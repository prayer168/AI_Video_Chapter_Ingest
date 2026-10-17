#!/usr/bin/env python3
"""Create lightweight HTML, DOCX or PDF outputs from Markdown sources."""
import argparse, html, re, shutil, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"dist"
def files():
 paths=[ROOT/"README.md",ROOT/"docs/TOC.md"]+sorted((ROOT/"chapters").glob("*.md"))
 return [(p,p.read_text(encoding="utf-8-sig")) for p in paths if p.exists()]
def body(text):
 text=re.sub(r"\A---\s*\n.*?\n---\s*\n","",text,flags=re.S); out=[]; para=[]
 def flush():
  if para: out.append("<p>"+html.escape(" ".join(para))+"</p>"); para.clear()
 for line in text.splitlines():
  s=line.strip()
  if not s: flush()
  elif s.startswith("#"):
   flush(); n=min(len(s)-len(s.lstrip("#")),6); out.append(f"<h{n}>{html.escape(s.lstrip('# ').strip())}</h{n}>")
  elif s.startswith("- "):
   flush(); out.append("<p>• "+html.escape(s[2:])+"</p>")
  else: para.append(s)
 flush(); return "\n".join(out)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--format",required=True,choices=["html","docx","pdf","all"]); ap.add_argument("--font",default="Noto Serif CJK TC"); a=ap.parse_args(); data=files(); fmts=["html","docx","pdf"] if a.format=="all" else [a.format]; OUT.mkdir(exist_ok=True)
 for fmt in fmts:
  if fmt=="html":
   dest=OUT/"html"; dest.mkdir(exist_ok=True); links=[]
   for p,t in data:
    name="index.html" if p.name=="README.md" else ("toc.html" if p.name=="TOC.md" else p.stem+".html"); title=p.stem
    doc="<!doctype html><html lang='zh-Hant'><meta charset='utf-8'><meta name='viewport' content='width=device-width'><title>"+html.escape(title)+"</title><style>body{max-width:52rem;margin:3rem auto;padding:0 1rem;font:1.1rem/1.8 system-ui,sans-serif}</style><body>"+body(t)+"</body></html>"
    (dest/name).write_text(doc,encoding="utf-8"); links.append(f'<li><a href="{name}">{html.escape(title)}</a></li>')
   (dest/"contents.html").write_text("<!doctype html><meta charset=utf-8><h1>AI 電影製作聖經</h1><ul>"+"".join(links)+"</ul>",encoding="utf-8"); print("Built HTML output")
  elif fmt=="docx":
   try: from docx import Document
   except ImportError: print("DOCX requires python-docx: pip install python-docx",file=sys.stderr); return 2
   d=Document(); d.styles["Normal"].font.name=a.font
   for p,t in data:
    for line in re.sub(r"\A---\s*\n.*?\n---\s*\n","",t,flags=re.S).splitlines():
     s=line.strip()
     if not s: continue
     if s.startswith("#"): d.add_heading(s.lstrip("# "),min(len(s)-len(s.lstrip("#")),3))
     elif s.startswith("- "): d.add_paragraph(s[2:],style="List Bullet")
     else: d.add_paragraph(s)
   d.save(OUT/"AI-Filmmaking-Bible.docx"); print("Built DOCX")
  else:
   pandoc=shutil.which("pandoc"); xelatex=shutil.which("xelatex")
   if not pandoc or not xelatex: print("PDF requires Pandoc and XeLaTeX on PATH",file=sys.stderr); return 2
   md=OUT/"book-source.md"; md.write_text("\n\n\\newpage\n\n".join(t for _,t in data),encoding="utf-8")
   r=subprocess.run([pandoc,str(md),"-o",str(OUT/"AI-Filmmaking-Bible.pdf"),"--pdf-engine=xelatex",f"-V mainfont={a.font}"],cwd=ROOT)
   if r.returncode:return r.returncode
   print("Built PDF")
 return 0
if __name__=="__main__":sys.exit(main())
