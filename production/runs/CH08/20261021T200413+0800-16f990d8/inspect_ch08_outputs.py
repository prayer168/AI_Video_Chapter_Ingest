from pathlib import Path
import re
import fitz

root = Path(__file__).resolve().parents[4]
out = root / "tmp/CH08-draft-20261021-r1"
for locale, route in (("zh-TW", "zh-tw"), ("en-US", "en")):
    pdf = fitz.open(out / f"CH08-{locale}-draft.pdf")
    page_text = [page.get_text() for page in pdf]
    proofs = []
    for i, page in enumerate(pdf):
        txt = page_text[i]
        if i == 0 or "8-1" in txt or "8-2" in txt:
            proof = out / "proofs" / f"{locale}-page-{i+1}.png"
            proof.parent.mkdir(exist_ok=True)
            page.get_pixmap(matrix=fitz.Matrix(1.25, 1.25), alpha=False).save(proof)
            proofs.append(proof.name)
    pdf_text = "\n".join(page_text)
    replacement = pdf_text.count("\ufffd")
    print(f"PDF {locale}: pages={len(pdf)}, replacement_chars={replacement}, figure_8_1={pdf_text.count('8-1')}, figure_8_2={pdf_text.count('8-2')}, proofs={proofs}")
    html_path = root / "apps/web/dist" / route / "ch08-chapter-08" / "index.html"
    html = html_path.read_text(encoding="utf-8")
    ids = re.findall(r'\sid="([^"]+)"', html)
    images = re.findall(r'<img\b[^>]*>', html)
    image_alt = [re.search(r'\balt="([^"]*)"', tag).group(1) if re.search(r'\balt="([^"]*)"', tag) else "" for tag in images]
    figure_refs = sum(html.count(f"CH08-FIG-00{i}") for i in (1, 2))
    print(f"WEB {locale}: route_exists={html_path.exists()}, unique_ids={len(ids)==len(set(ids))} ({len(ids)} ids), images={len(images)}, descriptive_alt={all(bool(x.strip()) for x in image_alt)}, figure_id_refs={figure_refs}")
