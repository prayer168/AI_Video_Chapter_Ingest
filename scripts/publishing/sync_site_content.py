"""Stage canonical bilingual Markdown into Astro's content collection."""
from __future__ import annotations

import argparse
import hashlib
import html
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANGS = {"zh-TW": "zh-tw", "en-US": "en"}
IMAGE_RE = re.compile(r"!\[([^]]*)\]\(([^)]+)\)")
FIGURE_BLOCK_RE = re.compile(r"!\[([^]]*)\]\(([^)]+)\)\{#([A-Za-z0-9_-]+)([^}]*)\}\s*\n\n\*\*(.+?)\*\*", re.S)


def chapter_images(source: Path):
    """Return safe local image mappings for the generated site projection."""
    text = source.read_text(encoding="utf-8")
    root = ROOT.resolve()
    seen = set()
    for alt, raw_ref in IMAGE_RE.findall(text):
        ref = raw_ref.strip().split()[0].strip("<>")
        if ref.startswith(("http://", "https://", "data:")):
            continue
        original = (source.parent / ref).resolve()
        try:
            original.relative_to(root)
        except ValueError as exc:
            raise ValueError(f"Image path escapes project root: {ref} ({source.name})") from exc
        if not original.is_file():
            raise FileNotFoundError(f"Referenced image file does not exist: {ref} ({source.name})")
        chapter_id = re.search(r"(?m)^chapter_id:\s*([A-Z0-9-]+)\s*$", text.split("---", 2)[1]).group(1)
        destination = ROOT / "apps" / "web" / "public" / "images" / "chapters" / chapter_id / original.name
        url = "/images/chapters/" + chapter_id + "/" + original.name
        key = (ref, original, destination, url)
        if key not in seen:
            seen.add(key)
            yield key


def sync_site_images(source: Path, check: bool) -> list[Path]:
    stale = []
    for ref, original, destination, _ in chapter_images(source):
        source_hash = hashlib.sha256(original.read_bytes()).digest()
        if destination.exists():
            if hashlib.sha256(destination.read_bytes()).digest() != source_hash:
                stale.append(destination)
                if not check:
                    shutil.copy2(original, destination)
        elif check:
            stale.append(destination)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(original, destination)
    return stale


def rendered_markdown(source: Path, locale: str) -> str:
    text = source.read_text(encoding="utf-8")
    expected = f"locale: {locale}"
    if expected not in text.split("---", 2)[1]:
        raise ValueError(f"locale mismatch in {source.relative_to(ROOT)}")
    # Canonical chapter paths are relative to content/<locale>/chapters. The static
    # site uses stable /images URLs and keeps generated copies under apps/web/public.
    for ref, _, _, url in chapter_images(source):
        text = text.replace(f"]({ref})", f"]({url})")
    # Render a canonical image + caption pair as semantic HTML. Pandoc's Lua
    # filter performs the corresponding conversion for PDF/EPUB builds.
    def render_figure(match):
        alt, url, figure_id, attributes, caption = match.groups()
        explicit_alt = re.search(r'fig-alt="([^"]*)"', attributes)
        if explicit_alt:
            alt = explicit_alt.group(1)
        return (f'<figure id="{figure_id}">'
                f'<img src="{url}" alt="{html.escape(alt, quote=True)}" />'
                f'<figcaption>{caption}</figcaption></figure>')
    text = FIGURE_BLOCK_RE.sub(render_figure, text)
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
    image_stale = []
    for locale, web_locale in LANGS.items():
        sources = sorted((ROOT / "content" / locale / "chapters").glob("CH*.md"))
        for source in sources:
            # These pages are plain Markdown. Keeping the .md extension lets the
            # Astro Markdown pipeline accept editorial HTML comments from the
            # canonical chapter template; MDX rejects those comments.
            target = ROOT / "apps/web/src/content/docs" / web_locale / source.with_suffix(".md").name
            image_stale.extend(sync_site_images(source, check=args.check))
            expected = rendered_markdown(source, locale)
            if not target.exists() or target.read_text(encoding="utf-8") != expected:
                stale.append((source, target, expected))
    if args.check:
        if stale or image_stale:
            print(f"Site projection is stale: {len(stale)} chapter pages and {len(image_stale)} image assets need sync.")
            return 1
        print("Site content sync check PASS: canonical bilingual Markdown and local image assets are current.")
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
    print(f"Synced {sum(len(list((ROOT / 'content' / lang / 'chapters').glob('CH*.md'))) for lang in LANGS)} canonical chapter files; updated {len(stale)} generated Astro pages; removed {removed} obsolete generated MDX projections; checked/copied local image assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
