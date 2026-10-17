#!/usr/bin/env python3
import argparse,shutil,subprocess,sys
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument("--font",default="Noto Serif CJK TC");ap.add_argument("--pdf",type=Path);a=ap.parse_args();found=False
if sys.platform=="win32":
 try:
  import winreg
  for root in (winreg.HKEY_LOCAL_MACHINE,winreg.HKEY_CURRENT_USER):
   try:
    with winreg.OpenKey(root,r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts") as k:
     for i in range(winreg.QueryInfoKey(k)[1]):
      n,_,_=winreg.EnumValue(k,i)
      if a.font.casefold() in n.casefold():found=True
   except OSError:pass
 except Exception:pass
elif shutil.which("fc-match"):
 r=subprocess.run(["fc-match","-f","%{family}",a.font],capture_output=True,text=True);found=bool(r.stdout.strip())
print(("Font appears installed: " if found else "WARNING: font not confirmed: ")+a.font)
if a.pdf:
 if not a.pdf.exists():print("PDF does not exist:",a.pdf);raise SystemExit(2)
 if shutil.which("pdffonts"):
  r=subprocess.run(["pdffonts",str(a.pdf)],capture_output=True,text=True);print(r.stdout)
  if r.returncode:raise SystemExit(r.returncode)
 else:print("pdffonts unavailable; inspect PDF embedding with a PDF reader")
