"""Create and verify synthetic bilingual EPUB/PDF samples in tmp only."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
SAMPLES = {
    "zh-TW": ("出版流程測試（非正式章節）", "繁體中文測試：電影語言、鏡頭運動、景深與色彩。"),
    "en-US": ("Publishing Workflow Smoke Test (Not Book Content)", "English rendering test: film language, camera movement, depth of field, and color."),
}


def run(command: list[str]) -> None:
    print("+", subprocess.list2cmdline(command))
    subprocess.run(command, cwd=ROOT, check=True)


def verify_epub(path: Path, locale: str, text: str) -> None:
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise RuntimeError(f"EPUB ZIP CRC failure: {path}")
        names = archive.namelist()
        if not names or names[0] != "mimetype" or archive.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            raise RuntimeError(f"Invalid EPUB mimetype entry: {path}")
        if archive.read("mimetype") != b"application/epub+zip":
            raise RuntimeError(f"Invalid EPUB mimetype value: {path}")
        ns = "{urn:oasis:names:tc:opendocument:xmlns:container}"
        rootfile = ET.fromstring(archive.read("META-INF/container.xml")).find(f"{ns}rootfiles/{ns}rootfile")
        if rootfile is None:
            raise RuntimeError(f"EPUB container has no OPF rootfile: {path}")
        opf = ET.fromstring(archive.read(rootfile.attrib["full-path"]))
        metadata = opf.find("{http://www.idpf.org/2007/opf}metadata")
        lang = metadata.find("{http://purl.org/dc/elements/1.1/}language") if metadata is not None else None
        if lang is None or lang.text != locale:
            raise RuntimeError(f"EPUB language metadata mismatch: {path}")
        xhtml = "\n".join(archive.read(n).decode("utf-8", "replace") for n in names if n.lower().endswith((".xhtml", ".html")))
        if text not in xhtml:
            raise RuntimeError(f"EPUB text missing/garbled: {path}")
    print(f"EPUB PASS {locale}: ZIP, mimetype, container, OPF language and text verified.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--font", default="Microsoft JhengHei", help="Traditional Chinese font to verify")
    parser.add_argument("--latin-font", default="Times New Roman", help="Latin font to verify")
    parser.add_argument("--out-dir", type=Path, default=ROOT / "tmp" / "publishing-smoke")
    parser.add_argument("--skip-pdf", action="store_true")
    parser.add_argument("--skip-epub", action="store_true")
    args = parser.parse_args()
    pandoc, xelatex = shutil.which("pandoc"), shutil.which("xelatex")
    if not pandoc:
        raise RuntimeError("Pandoc is not on PATH.")
    if not args.skip_pdf and not xelatex:
        raise RuntimeError("XeLaTeX is not on PATH.")
    args.out_dir.mkdir(parents=True, exist_ok=True)
    print("Pandoc:", subprocess.check_output([pandoc, "--version"], text=True).splitlines()[0])
    for locale, (title, text) in SAMPLES.items():
        source = args.out_dir / f"SMOKE-{locale}.md"
        source.write_text(f"---\ntitle: {title}\nlang: {locale}\nlanguage: {locale}\n---\n\n# {title}\n\n{text}\n", encoding="utf-8")
        if not args.skip_epub:
            epub = args.out_dir / f"SMOKE-{locale}.epub"
            run([pandoc, str(source), "--from=markdown", "--to=epub3", "--standalone", "--metadata", f"lang={locale}", "--metadata", f"language={locale}", "--output", str(epub)])
            verify_epub(epub, locale, text)
        if not args.skip_pdf:
            pdf = args.out_dir / f"SMOKE-{locale}.pdf"
            pdf_command = [pandoc, str(source), "--from=markdown", "--standalone", "--pdf-engine=xelatex", "--metadata", f"lang={locale}", "-V", f"mainfont={args.latin_font}"]
            expected_font = args.latin_font
            if locale == "zh-TW":
                pdf_command += ["-V", f"CJKmainfont={args.font}"]
                expected_font = args.font
            pdf_command += ["--output", str(pdf)]
            run(pdf_command)
            run([sys.executable, str(ROOT / "scripts/check_fonts.py"), "--pdf", str(pdf), "--font", expected_font, "--require-pdffonts"])
            text_extractor = shutil.which("pdftotext")
            if text_extractor:
                extracted = pdf.with_suffix(".txt")
                run([text_extractor, str(pdf), str(extracted)])
                normalize = lambda value: "".join(value.split())
                if normalize(text) not in normalize(extracted.read_text(encoding="utf-8", errors="replace")):
                    raise RuntimeError(f"PDF extracted text missing/garbled: {locale}")
            renderer = shutil.which("pdftoppm")
            if renderer:
                run([renderer, "-f", "1", "-singlefile", "-png", "-r", "120", str(pdf), str(pdf.with_suffix(""))])
                print(f"PDF render PASS {locale}: {pdf.with_suffix('.png')}")
            else:
                print("PDF visual render BLOCKED: pdftoppm is not on PATH.")
            print(f"PDF PASS {locale}: file created and requested font embedding verified.")
    print("Synthetic publishing smoke test completed. No chapter manuscript was generated.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"SMOKE TEST FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
