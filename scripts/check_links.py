#!/usr/bin/env python3
"""Check URLs in Markdown and the reference registry; online checks are best-effort."""
from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--online", action="store_true", help="Send HEAD requests to discovered HTTP(S) URLs")
args = parser.parse_args()

urls: dict[str, set[str]] = {}
errors: list[str] = []
markdown_files = [ROOT / "README.md", *ROOT.glob("docs/*.md"), *ROOT.glob("chapters/*.md")]
for path in markdown_files:
    text = path.read_text(encoding="utf-8-sig")
    for url in re.findall(r"https?://[^\s<>\])}\"']+", text):
        cleaned = url.rstrip(".,;:")
        urls.setdefault(cleaned, set()).add(str(path.relative_to(ROOT)))

references_path = ROOT / "data" / "references.yaml"
references = yaml.safe_load(references_path.read_text(encoding="utf-8-sig")) or []
for record in references:
    if isinstance(record, dict) and record.get("url"):
        url = str(record["url"]).strip()
        urls.setdefault(url, set()).add(f"data/references.yaml:{record.get('id', 'unknown')}")

for url, locations in sorted(urls.items()):
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        errors.append(f"Malformed URL {url} ({', '.join(locations)})")
        continue
    if not args.online:
        continue
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "AI-Filmmaking-Bible-Link-Check/0.1"},
        method="HEAD",
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            if response.status >= 400:
                errors.append(f"HTTP {response.status}: {url}")
    except urllib.error.HTTPError as exc:
        if exc.code not in {401, 403, 405, 429}:
            errors.append(f"HTTP {exc.code}: {url}")
        else:
            print(f"REVIEW HTTP {exc.code}: {url} ({', '.join(locations)})")
    except Exception as exc:
        print(f"REVIEW network issue: {url} ({exc})")

if errors:
    print("LINK CHECK FAILED")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

mode = "online best-effort" if args.online else "syntax only"
print(f"Link check passed: {len(urls)} unique URLs ({mode})")
