"""Build one bilingual chapter's local-only draft formats, bypassing book approval gates visibly."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.publishing.build_books import FORMATS, pandoc_data_dir_args, pdf_font_args, stage_sources_for_pandoc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chapter", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--font", default="Noto Serif TC")
    parser.add_argument("--latin-font", default="Times New Roman")
    args = parser.parse_args()
    ch = f"CH{args.chapter:02d}"
    args.out_dir = args.out_dir.resolve()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise RuntimeError("Pandoc is not installed or not on PATH")
    for locale in ("zh-TW", "en-US"):
        source = ROOT / "content" / locale / "chapters" / f"{ch}-chapter-{args.chapter}.md"
        if not source.is_file():
            raise FileNotFoundError(source)
        for fmt, suffix in FORMATS.items():
            stage = args.out_dir / "stage" / fmt
            staged, cwd = stage_sources_for_pandoc(locale, [source], fmt, stage)
            # Prevent long indented prompt-template paragraphs from running past PDF margins.
            if fmt == "pdf":
                text = staged[0].read_text(encoding="utf-8")
                text = re.sub(
                    r"(?m)^( {4,})(.{85,})$",
                    lambda m: "\n".join(m.group(1) + m.group(2)[i:i+72] for i in range(0, len(m.group(2)), 72)),
                    text,
                )
                staged[0].write_text(text, encoding="utf-8")
            target = args.out_dir / f"{ch}-{locale}-draft{suffix}"
            command = [pandoc, *map(str, staged), *pandoc_data_dir_args(), "--standalone", "--toc", "--metadata", f"lang={locale}", "--metadata", f"language={locale}", "--output", str(target)]
            lua = ROOT / "scripts/publishing/figure-captions.lua"
            if lua.is_file():
                command += ["--lua-filter", str(lua)]
            if fmt == "pdf":
                command += pdf_font_args(args.latin_font, args.font)
            subprocess.run(command, cwd=cwd, check=True)
            print(f"DRAFT {locale} {fmt}: {target}")
            if fmt == "pdf":
                font = args.font if locale == "zh-TW" else args.latin_font
                subprocess.run([sys.executable, str(ROOT / "scripts/check_fonts.py"), "--pdf", str(target), "--font", font, "--require-pdffonts"], cwd=ROOT, check=True)
    print("Local chapter drafts only. This command does not approve or publish chapter content.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

