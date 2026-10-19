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
    "noto serif tc": ("Noto Serif TC", "Noto Serif CJK TC"),
    "noto sans cjk tc": ("Noto Sans CJK TC", "Noto Sans TC"),
    "noto sans tc": ("Noto Sans TC", "Noto Sans CJK TC"),
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


def check_pdf_fonts(path: Path, requested_font: str, strict: bool = False) -> int:
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
        return 1 if strict else 0
    malformed = [row[0] for row in rows if len(row) < 7]
    if strict and malformed:
        print("ERROR: could not parse font embedding status for: " + ", ".join(malformed), file=sys.stderr)
        return 1
    # The PDF font ``type`` and ``encoding`` columns can contain spaces, so
    # fixed token positions are unreliable. The five trailing tokens are
    # consistently: emb, sub, uni, object number, generation number.
    missing = [row[0] for row in rows if len(row) >= 7 and row[-5].casefold() != "yes"]
    if missing:
        print("ERROR: fonts are not embedded: " + ", ".join(missing), file=sys.stderr)
        return 1
    if strict:
        normalize = lambda value: "".join(char for char in value.casefold() if char.isalnum())
        expected = normalize(requested_font)
        aliases = {normalize(alias) for alias in FONT_ALIASES.get(requested_font.casefold(), (requested_font,))}
        embedded = {normalize(row[0].split("+")[-1]) for row in rows if row}
        if not any(any(alias in name or name in alias for alias in aliases) for name in embedded):
            print(f"ERROR: requested font family not found among embedded PDF fonts: {requested_font}", file=sys.stderr)
            return 1
    print(f"PDF font embedding confirmed for {len(rows)} font entries.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--font", default="Noto Serif TC")
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--require-pdffonts", action="store_true", help="Fail if pdffonts is unavailable; use for formal publication gates")
    args = parser.parse_args()

    if font_is_installed(args.font):
        print(f"Font family appears installed: {args.font}")
    else:
        print(f"WARNING: font not confirmed: {args.font}")

    if args.pdf:
        if args.require_pdffonts and not shutil.which("pdffonts"):
            print("ERROR: pdffonts is required to verify embedded PDF fonts, but was not found.", file=sys.stderr)
            return 2
        return check_pdf_fonts(args.pdf, args.font, args.require_pdffonts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
