"""Stage canonical bilingual Markdown into Astro's content collection."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANGS = {"zh-TW": "zh-tw", "en-US": "en"}


def rendered_markdown(source: Path, locale: str) -> str:
    text = source.read_text(encoding="utf-8")
    expected = f"locale: {locale}"
    if expected not in text.split("---", 2)[1]:
        raise ValueError(f"locale mismatch in {source.relative_to(ROOT)}")
    # Pandoc-style explicit heading IDs are converted to portable HTML anchors.
    text = re.sub(r"(?m)^(#{1,6} .+?) \{#([A-Za-z0-9_-]+)\}\s*$", r'<a id="\2"></a>\n\1', text)
    # Locale and slug are publication registry metadata. Starlight derives the
    # localized route and translation pairing from the language directory and
    # shared filename, so do not let these canonical fields override its IDs.
    head, separator, body = text.partition("---\n")
    if separator:
        frontmatter, end_separator, remainder = body.partition("---\n")
        if end_separator:
            frontmatter = re.sub(r"(?m)^(?:locale|slug):.*\n", "", frontmatter)
            text = f"---\n{frontmatter}---\n{remainder}"
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if generated Astro docs are missing or stale; do not write")
    args = parser.parse_args()
    stale = []
    for locale, web_locale in LANGS.items():
        sources = sorted((ROOT / "content" / locale / "chapters").glob("CH*.md"))
        for source in sources:
            # These pages are plain Markdown. Keeping the .md extension lets the
            # Astro Markdown pipeline accept editorial HTML comments from the
            # canonical chapter template; MDX rejects those comments.
            target = ROOT / "apps/web/src/content/docs" / web_locale / source.with_suffix(".md").name
            expected = rendered_markdown(source, locale)
            if not target.exists() or target.read_text(encoding="utf-8") != expected:
                stale.append((source, target, expected))
    if args.check:
        if stale:
            print(f"Site content is stale: {len(stale)} generated chapter pages need sync.")
            return 1
        print("Site content sync check PASS: canonical bilingual Markdown is current.")
        return 0
    for _, target, expected in stale:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(expected, encoding="utf-8")
    # Remove only old generated CHxx MDX projections created by the previous
    # sync rule. Canonical editable sources remain under content/.
    removed = 0
    for web_locale in LANGS.values():
        for old_projection in (ROOT / "apps/web/src/content/docs" / web_locale).glob("CH*.mdx"):
            old_projection.unlink()
            removed += 1
    print(f"Synced {sum(len(list((ROOT / 'content' / lang / 'chapters').glob('CH*.md'))) for lang in LANGS)} canonical chapter files; updated {len(stale)} generated Astro pages; removed {removed} obsolete generated MDX projections.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
