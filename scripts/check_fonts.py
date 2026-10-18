#!/usr/bin/env python3
"""Check requested font availability and embedded fonts in a generated PDF."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

FONT_ALIASES = {
    "noto serif cjk tc": ("Noto Serif CJK TC", "Noto Serif TC"),
    "noto sans cjk tc": ("Noto Sans CJK TC", "Noto Sans TC"),
}


def installed_font_names() -> set[str]:
    names: set[str] = set()
    if sys.platform == "win32":
        try:
            import winreg

            for root in (winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER):
                for key_path in (
                    r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts",
                    r"SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Fonts",
                ):
                    try:
                        with winreg.OpenKey(root, key_path) as key:
                            for index in range(winreg.QueryInfoKey(key)[1]):
                                name, _, _ = winreg.EnumValue(key, index)
                                names.add(name.casefold())
                    except OSError:
                        continue
        except OSError:
            pass
    elif shutil.which("fc-list"):
        result = subprocess.run(
            ["fc-list", "-f", "%{family}\n"],
            capture_output=True,
            text=True,
            check=False,
        )
        names.update(line.strip().casefold() for line in result.stdout.splitlines())
    return names


def font_is_installed(requested: str) -> bool:
    names = installed_font_names()
    accepted = FONT_ALIASES.get(requested.casefold(), (requested,))
    return any(
        alias.casefold() in registered
        for alias in accepted
        for registered in names
    )


def check_pdf_fonts(path: Path) -> int:
    if not path.exists():
        print(f"PDF does not exist: {path}", file=sys.stderr)
        return 2
    pdffonts = shutil.which("pdffonts")
    if not pdffonts:
        print("pdffonts unavailable; inspect File > Properties > Fonts in a PDF reader.")
        return 0
    result = subprocess.run(
        [pdffonts, str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    print(result.stdout)
    if result.returncode:
        print(result.stderr, file=sys.stderr)
        return result.returncode
    rows = [
        line.split()
        for line in result.stdout.splitlines()[2:]
        if line.strip() and not line.startswith("-")
    ]
    if not rows:
        print("WARNING: no PDF fonts were listed; inspect the document manually.")
        return 0
    # The PDF font ``type`` and ``encoding`` columns can contain spaces, so
    # fixed token positions are unreliable. The five trailing tokens are
    # consistently: emb, sub, uni, object number, generation number.
    missing = [row[0] for row in rows if len(row) >= 7 and row[-5].casefold() != "yes"]
    if missing:
        print("ERROR: fonts are not embedded: " + ", ".join(missing), file=sys.stderr)
        return 1
    print(f"PDF font embedding confirmed for {len(rows)} font entries.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--font", default="Noto Serif TC")
    parser.add_argument("--pdf", type=Path)
    args = parser.parse_args()

    if font_is_installed(args.font):
        print(f"Font family appears installed: {args.font}")
    else:
        print(f"WARNING: font not confirmed: {args.font}")

    if args.pdf:
        return check_pdf_fonts(args.pdf)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
