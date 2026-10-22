from pathlib import Path
import os, subprocess, sys
root=Path.cwd(); sys.path.insert(0,str(root/'scripts/publishing')); import build_books as b
out=root/'tmp/CH09-draft-20261021-r4'
if out.exists(): raise SystemExit(f'Output exists; refusing overwrite: {out}')
out.mkdir(parents=True); logs=out/'logs'; logs.mkdir()
results=[]
for locale in ('zh-TW','en-US'):
 source=root/'content'/locale/'chapters'/'CH09-chapter-09.md'
 for fmt in ('docx','pdf','epub'):
  work=out/f'work-{locale}-{fmt}'; work.mkdir(); staged,stage=b.stage_sources_for_pandoc(locale,[source],fmt,work)
  target=out/f'CH09-{locale}-draft.{fmt}'
  cmd=['pandoc',str(staged[0]),*b.pandoc_data_dir_args(),'--standalone','--toc','--metadata',f'lang={locale}','--metadata',f'language={locale}','--lua-filter',str(root/'scripts/publishing/figure-captions.lua'),'--output',str(target)]
  if fmt=='pdf': cmd+=b.pdf_font_args('Times New Roman','Microsoft JhengHei')
  p=subprocess.run(cmd,cwd=stage,text=True,capture_output=True,encoding="utf-8",errors="replace")
  (logs/f'{locale}-{fmt}.log').write_text('COMMAND: '+subprocess.list2cmdline(cmd)+'\nEXIT: '+str(p.returncode)+'\nSTDOUT:\n'+p.stdout+'\nSTDERR:\n'+p.stderr,encoding='utf-8')
  print(locale,fmt,'build',p.returncode,target.exists())
  results.append((locale,fmt,p.returncode))
  if p.returncode: print(p.stderr[-3000:]); continue
  if fmt=='pdf':
   chk=subprocess.run([sys.executable,str(root/'scripts/check_fonts.py'),'--pdf',str(target),'--font','Microsoft JhengHei','--require-pdffonts'],text=True,capture_output=True,encoding="utf-8",errors="replace")
   (logs/f'{locale}-pdf-fonts.log').write_text(chk.stdout+'\n'+chk.stderr,encoding='utf-8'); print(locale,'fonts',chk.returncode,chk.stdout[-800:]); results.append((locale,'fonts',chk.returncode))
  if fmt=='epub':
   jar=Path(os.environ['LOCALAPPDATA'])/'Programs/EPUBCheck/5.4.0/epubcheck-5.4.0/epubcheck.jar'
   chk=subprocess.run(['java','-jar',str(jar),str(target)],text=True,capture_output=True,encoding="utf-8",errors="replace")
   (logs/f'{locale}-epubcheck.log').write_text(chk.stdout+'\n'+chk.stderr,encoding='utf-8'); print(locale,'EPUBCheck',chk.returncode); results.append((locale,'epubcheck',chk.returncode))
print('RESULTS',results,'OUT',out)


