from pathlib import Path
import subprocess,sys
root=Path.cwd(); sys.path.insert(0,str(root/'scripts/publishing')); import build_books as b
out=root/'tmp/CH09-draft-20261021-r7'; out.mkdir(parents=True,exist_ok=False); (out/'logs').mkdir()
for locale in ('zh-TW','en-US'):
 source=root/'content'/locale/'chapters'/'CH09-chapter-09.md'
 for fmt in ('docx','pdf','epub'):
  work=out/f'work-{locale}-{fmt}'; work.mkdir(); staged,stage=b.stage_sources_for_pandoc(locale,[source],fmt,work); target=out/f'CH09-{locale}-draft.{fmt}'
  cmd=['pandoc',str(staged[0]),*b.pandoc_data_dir_args(),'--standalone','--toc','--metadata',f'lang={locale}','--metadata',f'language={locale}','--lua-filter',str(root/'scripts/publishing/figure-captions.lua'),'--output',str(target)]
  if fmt=='pdf': cmd+=b.pdf_font_args('Times New Roman','Microsoft JhengHei')
  p=subprocess.run(cmd,cwd=stage,text=True,capture_output=True,encoding='utf-8',errors='replace')
  (out/'logs'/f'{locale}-{fmt}.log').write_text('COMMAND: '+subprocess.list2cmdline(cmd)+'\nEXIT: '+str(p.returncode)+'\nSTDOUT:\n'+p.stdout+'\nSTDERR:\n'+p.stderr,encoding='utf-8')
  print(locale,fmt,'PASS' if p.returncode==0 and target.exists() else f'FAIL ({p.returncode})')
  if p.returncode: raise SystemExit(p.returncode)
print('OUTPUT',out)

