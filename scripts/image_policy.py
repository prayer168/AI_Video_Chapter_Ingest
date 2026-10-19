#!/usr/bin/env python3
"""Fail-closed checks for images included in publication outputs."""
from __future__ import annotations

import argparse
import html
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml

IMAGE_SUFFIXES = {".avif", ".bmp", ".emf", ".eps", ".gif", ".heic", ".jpeg", ".jpg", ".pdf", ".png", ".psd", ".svg", ".tif", ".tiff", ".webp", ".wmf"}
TARGETS = ("zh-TW-book", "en-book", "zh-TW-site", "en-site")
STATUS_KEYS = ("technical", "quality", "rights", "final")


class _ImageHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.sources: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        values = dict(attrs)
        if tag.casefold() == "img" and values.get("src"):
            self.sources.append((values["src"], values.get("alt", "")))
        if tag.casefold() == "source":
            if values.get("src"):
                self.sources.append((values["src"], values.get("alt", "HTML source image")))
            if values.get("srcset"):
                for candidate in values["srcset"].split(","):
                    src = candidate.strip().split()[0] if candidate.strip() else ""
                    if src:
                        self.sources.append((src, values.get("alt", "HTML source image")))
        if tag.casefold() == "video" and values.get("poster"):
            self.sources.append((values["poster"], "video poster image"))
        if tag.casefold() == "object" and values.get("data"):
            self.sources.append((values["data"], values.get("alt", "HTML object image")))
        if tag.casefold() == "embed" and values.get("src"):
            self.sources.append((values["src"], values.get("alt", "HTML embed image")))
        for key, value in attrs:
            if key and key.casefold() == "style" and value:
                for url in re.findall(r"url\(\s*['\"]?([^)'\"]+)", value, re.I):
                    self.sources.append((url.strip(), "CSS background image"))

    def handle_startendtag(self, tag: str, attrs) -> None:
        self.handle_starttag(tag, attrs)


def _md_reference_definitions(text: str) -> dict[str, str]:
    return {
        label.strip().casefold(): target.strip("<>")
        for label, target in re.findall(r"^\s*\[([^\]]+)\]:\s*(\S+)", text, re.M)
    }


def markdown_image_refs(text: str) -> list[tuple[str, str]]:
    """Return inline/reference Markdown and HTML image sources plus alt text."""
    found: list[tuple[str, str]] = []
    definitions = _md_reference_definitions(text)
    inline_pattern = re.compile(r"!\[([^\]]*)\]\((?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)")
    consumed: list[tuple[int, int]] = []
    for match in inline_pattern.finditer(text):
        found.append((match.group(2) or match.group(3), match.group(1)))
        consumed.append(match.span())
    ref_pattern = re.compile(r"!\[([^\]]*)\](?:\[([^\]]*)\])?(?!\()")
    for match in ref_pattern.finditer(text):
        if any(a <= match.start() < b for a, b in consumed):
            continue
        key = (match.group(2) or match.group(1)).strip().casefold()
        target = definitions.get(key)
        if target:
            found.append((target, match.group(1) or key))
    parser = _ImageHTMLParser()
    try:
        parser.feed(text)
    except Exception:
        pass
    found.extend(parser.sources)
    if re.search(r"<\s*svg\b", text, re.I):
        found.append(("inline-svg:unsupported", "inline SVG illustration"))
    for url in re.findall(r"url\(\s*['\"]?([^)'\"]+)", text, re.I):
        found.append((url.strip(), "CSS image URL"))
    return found


def _local_path(root: Path, markdown_path: Path, target: str) -> Path | None:
    parsed = urlparse(target)
    if parsed.scheme or parsed.netloc:
        return None
    path_text = unquote(parsed.path)
    if not path_text:
        return None
    candidate = (markdown_path.parent / path_text).resolve()
    if not candidate.is_relative_to(root.resolve()):
        return None
    return candidate


def image_registry(root: Path) -> list[dict]:
    rows = yaml.safe_load((root / "data" / "assets.yaml").read_text(encoding="utf-8-sig")) or []
    return [row for row in rows if isinstance(row, dict) and (row.get("media_kind") == "image" or Path(str(row.get("path", ""))).suffix.casefold() in IMAGE_SUFFIXES)]


def approved_image_paths(root: Path, target: str) -> set[Path]:
    approved: set[Path] = set()
    for row in image_registry(root):
        if asset_approval_errors(row, target):
            continue
        approved.add((root / row["path"]).resolve())
    return approved


def asset_approval_errors(row: dict, target: str) -> list[str]:
    errors: list[str] = []
    asset_id = row.get("id", "unknown asset")
    review = row.get("review_status", {})
    if row.get("approval_status") != "approved":
        errors.append(f"{asset_id}: approval_status is {row.get('approval_status', 'missing')}")
    for key in STATUS_KEYS:
        if review.get(key) != "approved":
            errors.append(f"{asset_id}: {key} review is {review.get(key, 'missing')}")
    risk = row.get("rights_risk_review", {})
    if risk.get("status") != "approved":
        errors.append(f"{asset_id}: rights-risk review is {risk.get('status', 'missing')}")
    target_status = row.get("publication_targets", {}).get(target)
    if target_status != "approved":
        errors.append(f"{asset_id}: {target} approval is {target_status or 'missing'}")
    for field in ("figure_id", "paragraph_reference", "description", "creator", "attribution", "permission"):
        if not row.get(field):
            errors.append(f"{asset_id}: {field} is required")
    for field in ("tool_name", "tool_version"):
        if field not in row:
            errors.append(f"{asset_id}: record {field}; use null when unavailable")
    unresolved = ("pending", "unconfirmed", "待確認", "待查", "not approved")
    for field in ("creator", "attribution", "permission"):
        value = str(row.get(field, "")).casefold()
        if any(token in value for token in unresolved):
            errors.append(f"{asset_id}: {field} is unresolved")
    if not row.get("caption_zh_tw") or not row.get("caption_en"):
        errors.append(f"{asset_id}: Traditional Chinese and English captions are required")
    if not row.get("teaching_purpose"):
        errors.append(f"{asset_id}: teaching_purpose is required")
    if not row.get("original_prompt_or_method"):
        errors.append(f"{asset_id}: original prompt or drawing method is required")
    if not row.get("production_log"):
        errors.append(f"{asset_id}: production/modification log is required")
    else:
        for item in row.get("production_log", []):
            if not item.get("change") or "date" not in item:
                errors.append(f"{asset_id}: every production log entry needs a change and date (null if unknown)")
    if not row.get("research_sources"):
        errors.append(f"{asset_id}: research sources and checked dates are required")
    else:
        for item in row.get("research_sources", []):
            if not item.get("source_id") or not item.get("accessed") or not item.get("purpose"):
                errors.append(f"{asset_id}: every research source needs an ID, checked date, and purpose")
    if not row.get("creator") or not row.get("attribution"):
        errors.append(f"{asset_id}: creator and attribution records are required")
    if not row.get("permission"):
        errors.append(f"{asset_id}: permission record is required")
    if not row.get("tool_name") and not row.get("original_prompt_or_method"):
        errors.append(f"{asset_id}: record the original prompt or drawing method")
    if str(row.get("license", "")).casefold() in {"unconfirmed", "unknown", "", "none"}:
        errors.append(f"{asset_id}: publication license/permission is unconfirmed")
    return errors


def publication_blockers(root: Path, target: str, include_docs: bool = False) -> list[str]:
    root = root.resolve()
    rows = image_registry(root)
    by_path = {(root / str(row.get("path", ""))).resolve(): row for row in rows if row.get("path")}
    sources = sorted((root / "chapters").glob("*.md"))
    if include_docs:
        sources += [root / "README.md", *sorted((root / "docs").glob("*.md"))]
    blockers: list[str] = []
    seen: set[tuple[Path, str]] = set()
    try:
        reference_ids = {
            row.get("id") for row in yaml.safe_load((root / "data" / "references.yaml").read_text(encoding="utf-8-sig")) or []
            if isinstance(row, dict)
        }
    except Exception as exc:
        blockers.append(f"data/references.yaml cannot be read: {exc}")
        reference_ids = set()
    for row in rows:
        for research_source in row.get("research_sources", []):
            if research_source.get("source_id") not in reference_ids:
                blockers.append(f"{row.get('id')}: unknown research source {research_source.get('source_id')}")
    for source in sources:
        text = source.read_text(encoding="utf-8-sig")
        for raw_target, alt in markdown_image_refs(text):
            image_path = _local_path(root, source, raw_target)
            if not alt.strip():
                blockers.append(f"{source.relative_to(root)}: image needs descriptive alt text: {raw_target}")
            key = (source, raw_target)
            if key in seen:
                continue
            seen.add(key)
            if image_path is None:
                blockers.append(f"{source.relative_to(root)}: external/unsupported image source is not permitted: {raw_target}")
                continue
            row = by_path.get(image_path)
            if row is None:
                blockers.append(f"{source.relative_to(root)}: image is missing from data/assets.yaml: {raw_target} (alt: {alt})")
                continue
            if not image_path.is_file():
                blockers.append(f"{row.get('id')}: image file does not exist: {row.get('path')}")
                continue
            blockers.extend(f"{source.relative_to(root)}: {item}" for item in asset_approval_errors(row, target))
    return list(dict.fromkeys(blockers))


def _is_approved(root: Path, markdown_path: Path, source: str, target: str) -> bool:
    path = _local_path(root, markdown_path, source)
    if path is None:
        return False
    for row in image_registry(root):
        if (root / str(row.get("path", ""))).resolve() == path:
            return not asset_approval_errors(row, target)
    return False


def redact_unapproved_images(text: str, root: Path, markdown_path: Path, target: str) -> str:
    """Replace non-approved draft-preview images with explicit editorial notices."""
    inline_pattern = re.compile(r"!\[([^\]]*)\]\((?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)")
    text = inline_pattern.sub(
        lambda m: m.group(0) if _is_approved(root, markdown_path, m.group(2) or m.group(3), target)
        else f"**[插圖待審核：{html.escape(m.group(1) or '未命名插圖')}]**",
        text,
    )
    definitions = _md_reference_definitions(text)
    ref_pattern = re.compile(r"!\[([^\]]*)\](?:\[([^\]]*)\])?(?!\()")
    def replace_ref(match):
        key = (match.group(2) or match.group(1)).strip().casefold()
        src = definitions.get(key)
        if src and _is_approved(root, markdown_path, src, target):
            return match.group(0)
        return f"**[插圖待審核：{html.escape(match.group(1) or '未命名插圖')}]**"
    text = ref_pattern.sub(replace_ref, text)
    img_tag = re.compile(r"<img\b[^>]*>", re.I)
    def replace_img(match):
        tag = match.group(0)
        src_match = re.search(r"\bsrc\s*=\s*(['\"])(.*?)\1", tag, re.I)
        alt_match = re.search(r"\balt\s*=\s*(['\"])(.*?)\1", tag, re.I)
        if src_match and _is_approved(root, markdown_path, src_match.group(2), target):
            return tag
        return f"<span class=\"image-pending\">[插圖待審核：{html.escape(alt_match.group(2) if alt_match else '未命名插圖')}]</span>"
    text = img_tag.sub(replace_img, text)
    text = re.sub(r"<(?:object|embed)\b[^>]*>(?:[\s\S]*?</object\s*>)?", "<span class=\"image-pending\">[嵌入式插圖待登錄及審查]</span>", text, flags=re.I)
    text = re.sub(r"<svg\b[\s\S]*?</svg\s*>", "<span class=\"image-pending\">[內嵌 SVG 插圖待登錄及審查]</span>", text, flags=re.I)
    text = re.sub(r"url\(\s*(['\"]?)[^)'\"]+\1\s*\)", "none", text, flags=re.I)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description="Check whether chapter images are approved for a publication target.")
    parser.add_argument("--target", choices=TARGETS, required=True)
    parser.add_argument("--include-docs", action="store_true", help="Also check README and docs included in the website build")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    blockers = publication_blockers(root, args.target, include_docs=args.include_docs)
    if blockers:
        print(f"PUBLICATION BLOCKED for {args.target}")
        for item in blockers:
            print(f"- {item}")
        return 2
    print(f"PUBLICATION READY for {args.target}: all included images are registered and approved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
