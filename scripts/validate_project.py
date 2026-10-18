#!/usr/bin/env python3
"""Validate chapter metadata, registries, JSON examples, and local Markdown links."""
from __future__ import annotations

import json
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def load_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        ERRORS.append(f"{path.relative_to(ROOT)}: invalid YAML: {exc}")
        return None


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        ERRORS.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return None


registries = {}
for name in ("terms", "references", "assets", "prompts"):
    registries[name] = load_yaml(ROOT / "data" / f"{name}.yaml")
    if not isinstance(registries[name], list):
        ERRORS.append(f"data/{name}.yaml must contain a YAML list")
        registries[name] = []


def registry_ids(name: str) -> set[str]:
    rows = registries[name]
    ids = [row.get("id") for row in rows if isinstance(row, dict)]
    if len(ids) != len(set(ids)):
        ERRORS.append(f"data/{name}.yaml contains duplicate IDs")
    return {value for value in ids if isinstance(value, str)}


term_ids = registry_ids("terms")
reference_ids = registry_ids("references")
registry_ids("assets")
registry_ids("prompts")

for row in [*registries["terms"], *registries["assets"], *registries["prompts"]]:
    if isinstance(row, dict):
        for source_id in row.get("source_ids", []):
            if source_id not in reference_ids:
                ERRORS.append(f"Registry item {row.get('id')}: unknown source ID {source_id}")

chapter_schema = load_json(ROOT / "schemas" / "chapter.schema.json")
shot_schema = load_json(ROOT / "schemas" / "shot.schema.json")
try:
    from jsonschema import validate as validate_schema
except ImportError:
    validate_schema = None

chapters = sorted((ROOT / "chapters").glob("*.md"))
chapter_ids: set[str] = set()
for path in chapters:
    text = path.read_text(encoding="utf-8-sig")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        ERRORS.append(f"{path.name}: malformed or missing YAML front matter")
        continue
    try:
        metadata = yaml.safe_load(match.group(1)) or {}
    except Exception as exc:
        ERRORS.append(f"{path.name}: invalid front matter: {exc}")
        continue
    if not isinstance(metadata, dict):
        ERRORS.append(f"{path.name}: front matter must be a mapping")
        continue
    if validate_schema and chapter_schema:
        try:
            validate_schema(metadata, chapter_schema)
        except Exception as exc:
            ERRORS.append(f"{path.name}: chapter schema error: {getattr(exc, 'message', str(exc))}")
    else:
        for key in ("id", "part", "chapter", "title", "slug", "status", "updated", "sources", "terms", "related_chapters"):
            if key not in metadata:
                ERRORS.append(f"{path.name}: missing metadata field {key}")
    chapter_id = metadata.get("id")
    if chapter_id in chapter_ids:
        ERRORS.append(f"duplicate chapter ID {chapter_id}")
    if isinstance(chapter_id, str):
        chapter_ids.add(chapter_id)
    if metadata.get("status") not in {"planned", "draft", "review", "verified"}:
        ERRORS.append(f"{path.name}: unsupported chapter status {metadata.get('status')}")
    for source_id in metadata.get("sources", []):
        if source_id not in reference_ids:
            ERRORS.append(f"{path.name}: unknown source ID {source_id}")
    for term_id in metadata.get("terms", []):
        if term_id not in term_ids:
            ERRORS.append(f"{path.name}: unknown term ID {term_id}")
    for link in re.findall(r"\]\(([^)]+)\)", text):
        target = link.strip().split()[0].strip("<>")
        parsed = urlparse(target)
        if parsed.scheme or target.startswith("#") or not target:
            continue
        local_target = (path.parent / target.split("#", 1)[0]).resolve()
        if not local_target.exists():
            ERRORS.append(f"{path.name}: broken local link {target}")

for path in sorted((ROOT / "chapters").glob("**/*.json")):
    data = load_json(path)
    if path.name.startswith("shot-") and validate_schema and shot_schema and data is not None:
        try:
            validate_schema(data, shot_schema)
        except Exception as exc:
            ERRORS.append(f"{path.relative_to(ROOT)}: shot schema error: {getattr(exc, 'message', str(exc))}")

toc_path = ROOT / "docs" / "TOC.md"
toc = toc_path.read_text(encoding="utf-8-sig")
chapter_count = len(re.findall(r"^\d+\.\s+.+$", toc, re.M))
part_count = len(re.findall(r"^## 第.+篇", toc, re.M))
if chapter_count != 60:
    ERRORS.append(f"TOC has {chapter_count} chapters; expected 60")
if part_count != 12:
    ERRORS.append(f"TOC has {part_count} parts; expected 12")

for archive in (ROOT / "chapters" / "source-packs").glob("*.zip"):
    try:
        with zipfile.ZipFile(archive) as source:
            for member in source.namelist():
                member_path = Path(member)
                if member_path.is_absolute() or ".." in member_path.parts:
                    ERRORS.append(f"{archive.name}: unsafe archive member {member}")
    except zipfile.BadZipFile:
        ERRORS.append(f"{archive.name}: invalid ZIP archive")

if ERRORS:
    print("VALIDATION FAILED")
    for error in ERRORS:
        print(f"- {error}")
    raise SystemExit(1)

print(f"VALIDATION PASSED: {part_count} parts, {chapter_count} planned chapters, {len(chapters)} canonical chapter files, {len(term_ids)} terms, {len(reference_ids)} references")
