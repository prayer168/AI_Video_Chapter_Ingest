"""Build one locale from V2 Markdown using Pandoc; never publish or overwrite source."""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
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
                asset = figure.get("asset_approved")
                if not asset or (ROOT / asset).resolve() != requested:
                    continue
                approved = all(figure.get(key) == "approved" for key in ("rights_review", "technical_review", "editorial_review"))
                approved = approved and bool(figure.get("captions", {}).get(locale)) and bool(figure.get("alt", {}).get(locale))
                approved = approved and bool(figure.get("figure_id")) and bool(figure.get("teaching_goal"))
                generation = figure.get("generation") or {}
                approved = approved and all(key in generation for key in ("tool", "version", "date", "prompt_file"))
                break
            if not approved:
                raise ValueError(f"Image is not registered and approved for {locale}: {ref}")


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
    command = ["pandoc", *map(str, sources), "--standalone", "--toc", "--metadata", f"lang={args.locale}", "--metadata", f"language={args.locale}", "--output", str(target)]
    figure_filter = ROOT / "scripts" / "publishing" / "figure-captions.lua"
    if figure_filter.is_file():
        command += ["--lua-filter", str(figure_filter)]
    if args.format == "pdf":
        command += pdf_font_args(args.latin_font, args.font)
    result = subprocess.run(command, cwd=ROOT)
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
