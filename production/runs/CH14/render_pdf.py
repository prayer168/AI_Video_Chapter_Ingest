import fitz
from pathlib import Path
out=Path('tmp/CH14-draft-20261022-r1/rendered'); out.mkdir(parents=True,exist_ok=True)
for lang in ('zh-TW','en-US'):
 p=Path(f'tmp/CH14-draft-20261022-r1/CH14-{lang}-draft.pdf'); d=fitz.open(p); page=d[0]; pix=page.get_pixmap(matrix=fitz.Matrix(1.2,1.2),alpha=False); pix.save(out/f'{lang}-p1.png'); print(lang,'pages',len(d),'first_page_image',out/f'{lang}-p1.png')
