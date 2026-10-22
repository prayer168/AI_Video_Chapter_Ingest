from pathlib import Path
import shutil, subprocess, sys
sys.path.insert(0, str(Path.cwd()))
from scripts.publishing.build_books import ROOT, stage_sources_for_pandoc, pandoc_data_dir_args, pdf_font_args
out=ROOT/'tmp/CH06-draft-20261021-r4'; pandoc=shutil.which('pandoc')
if not pandoc: raise SystemExit('Pandoc missing from PATH')
for locale in ('zh-TW','en-US'):
    src=[ROOT/'content'/locale/'chapters'/'CH06-chapter-06.md']
    for fmt in ('docx','epub','pdf'):
        work=out/f'staging-{locale}-{fmt}'
        staged,cwd=stage_sources_for_pandoc(locale,src,fmt,work)
        target=out/f'CH06-{locale}.{fmt}'
        cmd=[pandoc,*map(str,staged),*pandoc_data_dir_args(),'--standalone','--toc','--metadata',f'lang={locale}','--metadata',f'language={locale}','--lua-filter',str(ROOT/'scripts/publishing/figure-captions.lua'),'--output',str(target)]
        if fmt=='pdf': cmd+=pdf_font_args('Times New Roman','Microsoft JhengHei')
        with (out/f'build-{locale}-{fmt}.log').open('w',encoding='utf-8') as log:
            result=subprocess.run(cmd,cwd=cwd,stdout=log,stderr=subprocess.STDOUT,text=True)
        if result.returncode: raise SystemExit(f'{locale} {fmt} failed; see {out/f"build-{locale}-{fmt}.log"}')
        print(locale,fmt,'PASS',target.stat().st_size)


