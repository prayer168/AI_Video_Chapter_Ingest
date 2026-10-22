from pathlib import Path
import hashlib, json, subprocess

root = Path(__file__).resolve().parents[4]
run = Path(__file__).resolve().parent
paths = [
    "content/zh-TW/chapters/CH09-chapter-09.md",
    "content/en-US/chapters/CH09-chapter-09.md",
    "apps/web/src/content/docs/zh-tw/CH09-chapter-09.md",
    "apps/web/src/content/docs/en/CH09-chapter-09.md",
    "assets/chapters/CH09/figure-manifest.yaml",
    "metadata/chapters.yaml", "metadata/translation-status.yaml",
    "metadata/terminology.yaml", "data/references.yaml", "metadata/references.bib",
    "data/assets.yaml", "metadata/figure-registry.yaml",
    "scripts/publishing/figure-captions.lua", "CHAPTER_INTEGRATION_MATRIX.md",
    "history.md", "reports/CHAPTER-PROGRESS-TRACKER.md",
    "scripts/update_chapter_progress_tracker.py",
    "metadata/translations/CH09-alignment.yaml",
    "assets/chapters/CH09/figure-captions.md",
    "assets/chapters/CH09/CH09-FIGURE-RIGHTS-AND-SOURCES.md",
    "assets/chapters/CH09/CH09-SOURCE-AND-CASE-NOTES.md",
    "assets/chapters/CH09/CH09-HUMAN-REVIEW-CHECKLIST.md",
    "tests/test_ch09_content.py", "reports/CH09-FINAL-ACCEPTANCE.md",
]
base = run / "backup/pre-edit"
entries = []
for relative in paths:
    source = root / relative
    exists = source.is_file()
    entry = {"path": relative, "existed": exists}
    if exists:
        content = source.read_bytes()
        target = base / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        entry.update({"backup_path": target.relative_to(run).as_posix(), "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest()})
    entries.append(entry)
status = subprocess.run(["git", "status", "--short"], cwd=root, capture_output=True, text=True, check=True).stdout
(run / "git-status-before.txt").write_text(status, encoding="utf-8")
(run / "backup/pre-edit/MANIFEST.json").write_text(json.dumps({"chapter": "CH09", "run_id": run.name, "created_at": "2026-10-21T20:43:00+08:00", "files": entries}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Backed up {sum(x['existed'] for x in entries)} files; recorded {sum(not x['existed'] for x in entries)} absent targets; preserved git status.")
