#!/usr/bin/env python3
"""Build accessible HTML and print-ready DOCX/PDF outputs from Markdown."""
from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

import markdown
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist"
HTML = OUT / "html"


def source_files() -> list[Path]:
    paths = [ROOT / "README.md", ROOT / "docs" / "TOC.md"]
    paths += sorted((ROOT / "docs").glob("*.md"))
    paths += sorted((ROOT / "chapters").glob("*.md"))
    return [path for path in paths if path.exists()]


def book_chapters() -> list[Path]:
    """Return only canonical chapter manuscripts for reader-edition exports."""
    return sorted(
        path
        for path in (ROOT / "chapters").glob("*.md")
        if path.name[:2].isdigit()
    )


def split_front_matter(text: str) -> tuple[dict, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        return {}, text
    try:
        metadata = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        metadata = {}
    return metadata, text[match.end():]


def output_path(source: Path) -> Path:
    if source == ROOT / "README.md":
        return HTML / "index.html"
    if source == ROOT / "docs" / "TOC.md":
        return HTML / "toc.html"
    if source.parent == ROOT / "docs":
        return HTML / "docs" / f"{source.stem}.html"
    return HTML / f"{source.stem}.html"


def rewrite_links(text: str, source: Path, target: Path, known_sources: set[Path]) -> str:
    pattern = re.compile(r"(!?\[[^\]]*\]\()([^)]*)(\))")

    def replace(match: re.Match) -> str:
        label, raw_target, close = match.groups()
        target_text = raw_target.strip()
        if not target_text or target_text.startswith("#"):
            return match.group(0)
        parsed = urlparse(target_text)
        if parsed.scheme or parsed.netloc:
            return match.group(0)
        file_part, separator, fragment = target_text.partition("#")
        resolved = (source.parent / file_part).resolve()
        if resolved in known_sources:
            destination = output_path(resolved)
        elif resolved.is_relative_to(ROOT / "assets"):
            destination = HTML / "assets" / resolved.relative_to(ROOT / "assets")
        elif resolved.is_relative_to(ROOT / "chapters"):
            relative = resolved.relative_to(ROOT / "chapters")
            if relative.parts and relative.parts[0].endswith("-assets"):
                destination = HTML / relative
            else:
                return match.group(0)
        else:
            return match.group(0)
        relative_url = Path(os.path.relpath(destination, target.parent)).as_posix()
        if separator:
            relative_url += "#" + fragment
        return f"{label}{relative_url}{close}"

    return pattern.sub(replace, text)


def markdown_body(text: str, source: Path, target: Path, known_sources: set[Path]) -> str:
    _, body = split_front_matter(text)
    body = rewrite_links(body, source, target, known_sources)
    return markdown.markdown(
        body,
        extensions=["tables", "fenced_code", "toc", "sane_lists"],
        output_format="html5",
    )


def page_title(source: Path, text: str) -> str:
    metadata, body = split_front_matter(text)
    if metadata.get("title"):
        return str(metadata["title"])
    heading = re.search(r"^#\s+(.+)$", body, re.M)
    if heading:
        return heading.group(1).strip()
    if source.name == "README.md":
        return "AI 電影製作聖經"
    return source.stem.replace("-", " ").title()


def build_html(sources: list[Path]) -> None:
    HTML.mkdir(parents=True, exist_ok=True)
    known = {path.resolve() for path in sources}
    for source in sources:
        target = output_path(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        text = source.read_text(encoding="utf-8-sig")
        title = page_title(source, text)
        content = markdown_body(text, source, target, known)
        page = f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="AI 電影製作聖經章節與出版資料">
<title>{html.escape(title)}</title>
<style>
:root{{color-scheme:light;--ink:#183247;--muted:#526777;--line:#dce5eb;--accent:#176b87}}
*{{box-sizing:border-box}}body{{margin:0;color:var(--ink);font:18px/1.8 system-ui,"Noto Sans CJK TC","Microsoft JhengHei",sans-serif}}
main{{max-width:900px;margin:0 auto;padding:2rem clamp(1rem,4vw,3rem) 5rem}}
h1,h2,h3{{line-height:1.35;margin-top:2.2em}}h1{{font-size:2.2rem;margin-top:1em}}h2{{border-bottom:1px solid var(--line);padding-bottom:.3em}}
a{{color:var(--accent);overflow-wrap:anywhere}}img,svg{{max-width:100%;height:auto}}figure{{margin:2rem 0}}figcaption,blockquote{{color:var(--muted)}}
blockquote{{border-left:4px solid var(--accent);margin:1.5rem 0;padding:.2rem 1rem}}table{{border-collapse:collapse;display:block;max-width:100%;overflow-x:auto;font-size:.95rem}}th,td{{border:1px solid var(--line);padding:.45rem .65rem;text-align:left;vertical-align:top}}th{{background:#edf4f7}}
pre{{overflow:auto;padding:1rem;background:#f2f5f7;border-radius:8px}}code{{font-family:ui-monospace,Consolas,monospace;font-size:.9em}}hr{{border:0;border-top:1px solid var(--line);margin:2rem 0}}
@media(max-width:600px){{body{{font-size:16px}}main{{padding:1rem 1rem 3rem}}h1{{font-size:1.8rem}}}}
@media print{{body{{font-size:11pt}}main{{max-width:none;padding:0}}a{{color:inherit;text-decoration:none}}}}
</style>
</head>
<body><main class="markdown-body">{content}</main></body>
</html>"""
        target.write_text(page, encoding="utf-8")
    assets = ROOT / "assets"
    if assets.exists():
        shutil.copytree(assets, HTML / "assets", dirs_exist_ok=True)
    for folder in (ROOT / "chapters").glob("*-assets"):
        shutil.copytree(folder, HTML / folder.name, dirs_exist_ok=True)
    links = []
    for source in sources:
        destination = output_path(source).relative_to(HTML).as_posix()
        links.append(f'<li><a href="{html.escape(destination)}">{html.escape(page_title(source, source.read_text(encoding="utf-8-sig")))}</a></li>')
    index = "<!doctype html><html lang='zh-Hant'><meta charset='utf-8'><meta name='viewport' content='width=device-width'><title>書籍內容</title><h1>AI 電影製作聖經</h1><nav><ul>" + "".join(links) + "</ul></nav></html>"
    (HTML / "contents.html").write_text(index, encoding="utf-8")
    print(f"Built HTML: {HTML}")


def combined_markdown(sources: list[Path]) -> Path:
    sections = []
    for source in sources:
        text = source.read_text(encoding="utf-8-sig")
        metadata, body = split_front_matter(text)
        title = metadata.get("title") or page_title(source, text)
        # Chapter manuscripts already carry their own H1. Avoid adding a
        # duplicate title that would create two chapter headings in exports.
        if not re.search(r"^#\s+", body, re.M):
            body = f"# {title}\n\n{body}"
        sections.append(body.strip())
    target = OUT / "book-source.md"
    target.write_text("\n\n\\newpage\n\n".join(sections), encoding="utf-8")
    return target


def build_docx(sources: list[Path], font: str) -> int:
    pandoc = shutil.which("pandoc")
    source = combined_markdown(book_chapters())
    target = OUT / "AI-Filmmaking-Bible.docx"
    if pandoc:
        result = subprocess.run(
            [pandoc, str(source), "-o", str(target), "-V", f"mainfont={font}"],
            cwd=ROOT,
        )
        if result.returncode:
            return result.returncode
        try:
            from docx import Document
            from docx.oxml.ns import qn
        except ImportError:
            print("DOCX created; install python-docx to apply the requested CJK font to Word styles.", file=sys.stderr)
        else:
            document = Document(target)
            for style_name in ("Normal", "Heading 1", "Heading 2", "Heading 3"):
                style = document.styles[style_name]
                style.font.name = font
                properties = style._element.get_or_add_rPr()
                fonts = properties.rFonts
                if fonts is None:
                    from docx.oxml import OxmlElement
                    fonts = OxmlElement("w:rFonts")
                    properties.append(fonts)
                for key in ("ascii", "hAnsi", "eastAsia", "cs"):
                    fonts.set(qn(f"w:{key}"), font)
            document.save(target)
        print(f"Built DOCX: {target}")
        return 0
    try:
        from docx import Document
    except ImportError:
        print("DOCX requires Pandoc or python-docx: pip install python-docx", file=sys.stderr)
        return 2
    document = Document()
    document.styles["Normal"].font.name = font
    for source_path in sources:
        text = source_path.read_text(encoding="utf-8-sig")
        _, body = split_front_matter(text)
        for line in body.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("#"):
                level = min(len(stripped) - len(stripped.lstrip("#")), 3)
                document.add_heading(stripped.lstrip("# ").strip(), level)
            elif stripped.startswith("- "):
                document.add_paragraph(stripped[2:], style="List Bullet")
            else:
                document.add_paragraph(stripped)
    document.save(target)
    print(f"Built DOCX: {target}")
    return 0


def build_pdf(sources: list[Path], font: str) -> int:
    pandoc, xelatex = shutil.which("pandoc"), shutil.which("xelatex")
    if not pandoc or not xelatex:
        print("PDF requires Pandoc and XeLaTeX on PATH", file=sys.stderr)
        return 2
    source = combined_markdown(book_chapters())
    svg_converter = shutil.which("inkscape")
    image_pattern = re.compile(r"(!\[[^\]]*\]\()([^\s)]+\.svg)([^)]*\))", re.I)

    def convert_svg(match: re.Match) -> str:
        image_path = (source.parent / match.group(2)).resolve()
        if not image_path.exists():
            raise FileNotFoundError(f"SVG image not found: {image_path}")
        if not svg_converter:
            raise RuntimeError("PDF includes SVG figures. Install Inkscape and ensure 'inkscape' is on PATH.")
        media_dir = OUT / "pdf-media"
        media_dir.mkdir(parents=True, exist_ok=True)
        relative_name = "--".join(image_path.relative_to(ROOT).parts).removesuffix(".svg") + ".pdf"
        converted = media_dir / relative_name
        result = subprocess.run(
            [svg_converter, str(image_path), f"--export-filename={converted}"],
            cwd=ROOT,
        )
        if result.returncode:
            raise RuntimeError(f"Inkscape failed to convert {image_path.name} to PDF")
        replacement = Path(os.path.relpath(converted, source.parent)).as_posix()
        return f"{match.group(1)}{replacement}{match.group(3)}"

    try:
        source_text = source.read_text(encoding="utf-8")
        source_text = image_pattern.sub(convert_svg, source_text)
        source.write_text(source_text, encoding="utf-8")
    except (FileNotFoundError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    target = OUT / "AI-Filmmaking-Bible.pdf"
    result = subprocess.run(
        [pandoc, str(source), "-o", str(target), "--pdf-engine=xelatex", "-V", f"mainfont={font}"],
        cwd=ROOT,
    )
    if result.returncode == 0:
        print(f"Built PDF: {target}")
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", required=True, choices=["html", "docx", "pdf", "all"])
    parser.add_argument("--font", default="Noto Serif CJK TC")
    args = parser.parse_args()
    sources = source_files()
    OUT.mkdir(parents=True, exist_ok=True)
    formats = ["html", "docx", "pdf"] if args.format == "all" else [args.format]
    for output_format in formats:
        if output_format == "html":
            build_html(sources)
        elif output_format == "docx":
            result = build_docx(sources, args.font)
            if result:
                return result
        else:
            result = build_pdf(sources, args.font)
            if result:
                return result
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
