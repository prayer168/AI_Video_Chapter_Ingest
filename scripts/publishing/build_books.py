"""Build one locale from V2 Markdown using Pandoc; never publish or overwrite source."""
from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.image_policy import _local_path, markdown_image_refs

FORMATS = {"docx": ".docx", "epub": ".epub", "pdf": ".pdf"}


def pdf_font_args(latin_font: str, cjk_font: str) -> list[str]:
    """Set both script families because bilingual glossaries occur in either locale."""
    return ["--pdf-engine=xelatex", "-V", f"mainfont={latin_font}", "-V", f"CJKmainfont={cjk_font}"]


def pandoc_data_dir_args() -> list[str]:
    """Use project-local Traditional Chinese labels for Pandoc's zh-TW fallback."""
    return ["--data-dir", str(ROOT / "scripts" / "publishing" / "pandoc-data")]


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"Missing YAML frontmatter: {path.relative_to(ROOT)}")
    _, raw, _ = text.split("---", 2)
    if yaml is None:
        raise RuntimeError("PyYAML is required for publication metadata checks; install requirements-v2.txt")
    data = yaml.safe_load(raw)
    if not isinstance(data, dict):
        raise ValueError(f"Invalid YAML frontmatter: {path.relative_to(ROOT)}")
    return data


def validate_manuscripts(locale: str, sources: list[Path]) -> None:
    expected_ids = [f"CH{i:02d}" for i in range(1, 61)]
    actual_ids, image_refs = [], []
    if yaml is None:
        raise RuntimeError("PyYAML is required for publication metadata checks; install requirements-v2.txt")
    state_file = ROOT / "metadata" / "translation-status.yaml"
    states = yaml.safe_load(state_file.read_text(encoding="utf-8")) or {}
    states = states.get("chapters", {})
    for source in sources:
        metadata = read_frontmatter(source)
        chapter_id = metadata.get("chapter_id")
        actual_ids.append(chapter_id)
        if metadata.get("locale") != locale:
            raise ValueError(f"Locale mismatch in {source.relative_to(ROOT)}")
        if metadata.get("translation_status") != "approved":
            raise ValueError(f"Chapter is not editorially approved: {chapter_id} ({metadata.get('translation_status')})")
        if (states.get(chapter_id, {}) or {}).get(locale) != "approved":
            raise ValueError(f"Translation registry is not approved: {chapter_id}/{locale}")
        body = source.read_text(encoding="utf-8").lower()
        if "scaffold" in body or "placeholder" in body:
            raise ValueError(f"Chapter contains scaffold/placeholder content: {chapter_id}")
        image_refs.extend((source, ref, alt) for ref, alt in markdown_image_refs(source.read_text(encoding="utf-8")))
    if actual_ids != expected_ids:
        raise ValueError("Formal book requires exactly 60 chapters in CH01–CH60 order")

    if image_refs:
        if yaml is None:
            raise RuntimeError("PyYAML is required to validate figure rights")
        for source, ref, alt in image_refs:
            ref = ref.strip().split()[0].strip("<>")
            if not alt.strip():
                raise ValueError(f"Image must have descriptive alt text: {ref}")
            requested = _local_path(ROOT, source, ref)
            if requested is None:
                raise ValueError(f"Remote, inline or unsafe image prohibited in formal book: {ref}")
            if not requested.is_file():
                raise ValueError(f"Referenced image file does not exist: {ref}")
            chapter_id = read_frontmatter(source).get("chapter_id")
            manifest_path = ROOT / "assets" / "chapters" / str(chapter_id) / "figure-manifest.yaml"
            manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
            approved = False
            for figure in (manifest or {}).get("figures", []):
                if figure.get("figure_id") and figure_is_approved(figure, locale, requested):
                    approved = True
                    break
            if not approved:
                raise ValueError(f"Image is not registered and approved for {locale}: {ref}")


def stage_sources_for_pandoc(locale: str, sources: list[Path], output_format: str, work_dir: Path) -> tuple[list[Path], Path]:
    """Stage source media; keep SVG for EPUB, use raster DOCX fallback, and vector PDF for XeLaTeX."""
    staged_dir = work_dir / locale
    media_dir = work_dir / "media"
    staged_dir.mkdir(parents=True, exist_ok=True)
    media_dir.mkdir(parents=True, exist_ok=True)
    inkscape = shutil.which("inkscape")
    if not inkscape:
        for candidate in (Path(r"C:\Program Files\Inkscape\bin\inkscape.com"), Path(r"C:\Program Files\Inkscape\bin\inkscape.exe")):
            if candidate.is_file():
                inkscape = str(candidate)
                break
    staged_sources: list[Path] = []
    for source in sources:
        text = source.read_text(encoding="utf-8")
        for reference, _alt in markdown_image_refs(text):
            if reference.startswith(("http://", "https://", "data:")):
                continue
            image = _local_path(ROOT, source, reference)
            if image is None or not image.is_file():
                raise ValueError(f"Cannot stage publication image: {reference} ({source.name})")
            is_svg = image.suffix.casefold() == ".svg"
            vector_pdf = output_format == "pdf" and is_svg
            raster_docx = output_format == "docx" and is_svg
            suffix = ".pdf" if vector_pdf else ".png" if raster_docx else image.suffix.casefold()
            digest = hashlib.sha256(image.read_bytes()).hexdigest()
            staged_media = media_dir / f"{digest}{suffix}"
            if not staged_media.exists():
                if vector_pdf or raster_docx:
                    if not inkscape:
                        raise RuntimeError("SVG publication output needs Inkscape; install it or add inkscape to PATH.")
                    export_type = "pdf" if vector_pdf else "png"
                    command = [inkscape, str(image), f"--export-type={export_type}", f"--export-filename={staged_media}"]
                    if raster_docx:
                        command.append("--export-width=1800")
                    # Inkscape may emit UTF-8 diagnostics even when Windows' active
                    # console code page is legacy CP950. Decode explicitly so staging
                    # SVG assets from non-ASCII paths cannot break the build process.
                    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")
                    if result.returncode:
                        raise RuntimeError(f"Inkscape SVG-to-PDF conversion failed for {image}: {result.stderr}")
                else:
                    shutil.copy2(image, staged_media)
            staged_reference = f"../media/{staged_media.name}"
            pattern = re.compile(r"(!\[[^\]]*\]\()" + re.escape(reference) + r"(?=[\s)])")
            text = pattern.sub(lambda match: match.group(1) + staged_reference, text)
        staged_source = staged_dir / source.name
        staged_source.write_text(text, encoding="utf-8", newline="\n")
        staged_sources.append(staged_source)
    return staged_sources, staged_dir


def figure_is_approved(figure: dict, locale: str, requested: Path) -> bool:
    """Validate publication approval and provenance appropriate to the asset type."""
    approved_asset = figure.get("asset_approved")
    if not approved_asset or (ROOT / approved_asset).resolve() != requested.resolve():
        return False
    approved = all(figure.get(key) == "approved" for key in ("rights_review", "technical_review", "editorial_review"))
    captions = figure.get("captions") or {"zh-TW": figure.get("caption_zh"), "en-US": figure.get("caption_en")}
    alts = figure.get("alt") or {"zh-TW": figure.get("alt_zh"), "en-US": figure.get("alt_en")}
    approved = approved and bool(captions.get(locale)) and bool(alts.get(locale))
    approved = approved and bool(figure.get("figure_id")) and bool(figure.get("teaching_goal"))
    if requested.suffix.casefold() == ".svg":
        log = figure.get("production_log") or []
        provenance = bool(figure.get("method")) and any(item.get("date") and item.get("change") for item in log)
    else:
        generation = figure.get("generation") or {}
        provenance = all(key in generation for key in ("tool", "version", "date", "prompt_file"))
    return approved and provenance


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", choices=("zh-TW", "en-US"), required=True)
    parser.add_argument("--format", choices=tuple(FORMATS), required=True)
    parser.add_argument("--font", default="Microsoft JhengHei", help="Installed font used for Traditional Chinese PDF text")
    parser.add_argument("--latin-font", default="Times New Roman", help="Installed font used for Latin text in PDFs")
    args = parser.parse_args()
    source_dir = ROOT / "content" / args.locale / "chapters"
    sources = sorted(source_dir.glob("CH*.md"))
    if not sources:
        print(f"ERROR: no chapter sources found for {args.locale}", file=sys.stderr)
        return 2
    try:
        validate_manuscripts(args.locale, sources)
    except (ValueError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if not shutil.which("pandoc"):
        print("ERROR: Pandoc is not installed or not on PATH.", file=sys.stderr)
        return 2
    out_dir = ROOT / "dist" / "books" / args.locale
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"AI-Video-Bible-{args.locale}{FORMATS[args.format]}"
    with tempfile.TemporaryDirectory(prefix="book-build-", dir=ROOT / "tmp") as temporary:
        staged_sources, staged_dir = stage_sources_for_pandoc(args.locale, sources, args.format, Path(temporary))
        command = ["pandoc", *map(str, staged_sources), *pandoc_data_dir_args(), "--standalone", "--toc", "--metadata", f"lang={args.locale}", "--metadata", f"language={args.locale}", "--output", str(target)]
        figure_filter = ROOT / "scripts" / "publishing" / "figure-captions.lua"
        if figure_filter.is_file():
            command += ["--lua-filter", str(figure_filter)]
        if args.format == "pdf":
            command += pdf_font_args(args.latin_font, args.font)
        result = subprocess.run(command, cwd=staged_dir)
    if result.returncode == 0:
        if args.format == "pdf":
            checker = ROOT / "scripts" / "check_fonts.py"
            expected_font = args.font if args.locale == "zh-TW" else args.latin_font
            check = subprocess.run([sys.executable, str(checker), "--pdf", str(target), "--font", expected_font, "--require-pdffonts"], cwd=ROOT)
            if check.returncode:
                print("ERROR: PDF was generated, but embedded-font verification did not pass.", file=sys.stderr)
                return check.returncode
        print(f"Built draft book: {target.relative_to(ROOT)}")
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
