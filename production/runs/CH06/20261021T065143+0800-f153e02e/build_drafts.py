import os, subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[4]
out = root / 'tmp' / 'CH06-draft-20261021-r2'
out.mkdir(parents=True, exist_ok=False)
pandoc = r'C:\Users\user\AppData\Local\Pandoc\pandoc.exe'
miktex_bin = r'C:\Users\user\AppData\Local\Programs\MiKTeX\miktex\bin\x64'
for locale, lang in [('zh-TW','zh-TW'),('en-US','en-US')]:
    source = root / 'content' / locale / 'chapters' / 'CH06-chapter-06.md'
    for fmt in ('docx','epub','pdf'):
        target = out / f'CH06-{locale}.{fmt}'
        cmd = [pandoc, str(source), '--data-dir', str(root/'scripts/publishing/pandoc-data'), '--standalone','--toc','--metadata',f'lang={lang}','-o',str(target)]
        if fmt == 'pdf':
            cmd += ['--pdf-engine=xelatex','-V','mainfont=Times New Roman','-V','CJKmainfont=Microsoft JhengHei']
        env = {**os.environ,'LANG':'C.UTF-8','LC_ALL':'C.UTF-8','PATH':miktex_bin+os.pathsep+os.environ.get('PATH','')}
        run = subprocess.run(cmd, cwd=Path.home()/'Documents', text=True, encoding='utf-8', errors='replace', capture_output=True, env=env)
        (out/f'build-{locale}-{fmt}.log').write_text(run.stdout+'\n'+run.stderr, encoding='utf-8')
        print(locale, fmt, 'exit=',run.returncode,'exists=',target.exists())
        if run.returncode:
            raise SystemExit(run.returncode)
print(out)
