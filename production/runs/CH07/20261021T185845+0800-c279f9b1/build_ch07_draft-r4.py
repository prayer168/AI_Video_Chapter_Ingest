from pathlib import Path
import os, subprocess, sys
root=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(root/'scripts/publishing'))
import build_books as b
os.environ['PATH']=r'C:\Program Files\Inkscape\bin;'+os.environ['PATH']
out=root/'tmp/CH07-draft-20261021-r4'; out.mkdir(parents=True,exist_ok=False)
logs=out/'logs'; logs.mkdir()
for locale in ('zh-TW','en-US'):
    source=root/'content'/locale/'chapters'/'CH07-chapter-07.md'
    for fmt in ('docx','pdf','epub'):
        work=out/f'work-{locale}-{fmt}'; work.mkdir()
        staged, staged_dir=b.stage_sources_for_pandoc(locale,[source],fmt,work)
        target=out/f'CH07-{locale}-draft.{fmt}'
        cmd=['pandoc',str(staged[0]),*b.pandoc_data_dir_args(),'--standalone','--toc','--metadata',f'lang={locale}','--metadata',f'language={locale}','--lua-filter',str(root/'scripts/publishing/figure-captions.lua'),'--output',str(target)]
        if fmt=='pdf': cmd += b.pdf_font_args('Times New Roman','Microsoft JhengHei')
        p=subprocess.run(cmd,cwd=staged_dir,text=True,capture_output=True)
        (logs/f'{locale}-{fmt}.log').write_text('COMMAND: '+subprocess.list2cmdline(cmd)+'\nEXIT: '+str(p.returncode)+'\nSTDOUT:\n'+p.stdout+'\nSTDERR:\n'+p.stderr,encoding='utf-8')
        print(locale,fmt,'exit',p.returncode,'exists',target.exists())
        if p.returncode: print(p.stderr[-3000:]); raise SystemExit(p.returncode)
        if fmt=='pdf':
            checker=subprocess.run([sys.executable,str(root/'scripts/check_fonts.py'),'--pdf',str(target),'--font',('Microsoft JhengHei' if locale=='zh-TW' else 'Times New Roman'),'--require-pdffonts'],text=True,capture_output=True)
            (logs/f'{locale}-pdf-fonts.log').write_text(checker.stdout+'\n'+checker.stderr,encoding='utf-8')
            print('font check',locale,checker.returncode)
            if checker.returncode: raise SystemExit(checker.returncode)
        if fmt=='epub':
            jar=Path(os.environ['LOCALAPPDATA'])/'Programs/EPUBCheck/5.4.0/epubcheck-5.4.0/epubcheck.jar'
            epubcheck=subprocess.run(['java','-jar',str(jar),str(target)],text=True,capture_output=True)
            (logs/f'{locale}-epubcheck.log').write_text(epubcheck.stdout+'\n'+epubcheck.stderr,encoding='utf-8')
            print('epubcheck',locale,epubcheck.returncode,epubcheck.stdout[-500:])
            if epubcheck.returncode: raise SystemExit(epubcheck.returncode)
print('OUTPUT_DIR',out)


