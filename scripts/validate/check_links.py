"""Check local Markdown links; network checks are explicit and rate-limited."""
from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
URL_RE = re.compile(r"https?://[^\s)>]+")


def collect_files() -> list[Path]:
    return [* (ROOT / "content").rglob("*.md"), * (ROOT / "docs").glob("*.md"), ROOT / "README.md"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--network", action="store_true", help="Check external links over HTTPS; sends requests to cited hosts")
    parser.add_argument("--delay", type=float, default=0.5, help="Seconds between network requests (default: 0.5)")
    args = parser.parse_args()
    failures, unchecked, checked = [], [], 0
    for path in collect_files():
        if not path.exists():
            continue
        for target in LINK_RE.findall(path.read_text(encoding="utf-8")):
            target = target.strip().split()[0].strip("<>")
            if target.startswith(("https://", "http://")):
                if not args.network:
                    unchecked.append((path, target)); continue
                request = urllib.request.Request(target, method="HEAD", headers={"User-Agent": "AI-Video-Bible-Link-Checker/1.0"})
                try:
                    with urllib.request.urlopen(request, timeout=15) as response:
                        if response.status >= 400:
                            failures.append((path, target, f"HTTP {response.status}"))
                except urllib.error.HTTPError as exc:
                    if exc.code not in (403, 405):
                        failures.append((path, target, f"HTTP {exc.code}"))
                    else:
                        unchecked.append((path, target))
                except Exception as exc:  # Report network failure without treating transient blocks as certain dead links.
                    unchecked.append((path, target))
                checked += 1
                time.sleep(max(0, args.delay))
                continue
            if target.startswith(("#", "mailto:", "tel:")):
                continue
            local = (path.parent / target.split("#", 1)[0]).resolve()
            if target.split("#", 1)[0] and not local.exists():
                failures.append((path, target, "local target missing"))
    for path, target, reason in failures:
        print(f"ERROR: {path.relative_to(ROOT)} -> {target}: {reason}")
    print(f"Links: {checked} network checked; {len(unchecked)} not conclusively checked; {len(failures)} failures.")
    if unchecked:
        print("NOTE: blocked/transient or offline URLs require manual review; unchecked is not equivalent to broken.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
