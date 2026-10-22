from pathlib import Path
import argparse, hashlib, json, zipfile

parser = argparse.ArgumentParser()
parser.add_argument("--revision", default="r1")
revision = parser.parse_args().revision

root = Path(__file__).resolve().parents[4]
out = root / "tmp/CH08-draft-20261021-r1"
run = Path(__file__).resolve().parent
zip_path = out / f"CH08-Codex-Materials-DRAFT-{revision}.zip"
if zip_path.exists():
    raise SystemExit(f"Refusing to overwrite existing package: {zip_path}")

include = [
    root / "content/zh-TW/chapters/CH08-chapter-08.md",
    root / "content/en-US/chapters/CH08-chapter-08.md",
    root / "metadata/translations/CH08-alignment.yaml",
    root / "assets/chapters/CH08/figure-manifest.yaml",
    root / "assets/chapters/CH08/figure-captions.md",
    root / "assets/chapters/CH08/CH08-FIGURE-RIGHTS-AND-SOURCES.md",
    root / "assets/chapters/CH08/CH08-SOURCE-AND-CASE-NOTES.md",
    root / "assets/chapters/CH08/CH08-HUMAN-REVIEW-CHECKLIST.md",
    root / "reports/CH08-FINAL-ACCEPTANCE.md",
    root / "reports/CHAPTER-PROGRESS-TRACKER.md",
    root / "tests/test_ch08_content.py",
    root / "metadata/terminology.yaml",
    root / "data/references.yaml",
    root / "metadata/references.bib",
    root / "history.md",
    root / "CHAPTER_INTEGRATION_MATRIX.md",
]
include += sorted((root / "assets/chapters/CH08/figures/originals").glob("*.svg"))
include += sorted(out.glob("CH08-*-draft.*"))
include += sorted((out / "logs").glob("*"))
include += sorted((out / "proofs").glob("*.png"))
include += sorted((run / "backup/pre-edit").rglob("*"))
include += [run / "build_ch08_draft-r1.py", run / "inspect_ch08_outputs.py"]
files = [p for p in include if p.is_file()]
members = []
for path in files:
    try:
        rel = path.relative_to(root).as_posix()
    except ValueError:
        rel = "draft-output/" + path.relative_to(out).as_posix()
    content = path.read_bytes()
    members.append({"path": rel, "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest()})
manifest_path = out / f"OUTPUT-MANIFEST-{revision}.json"
manifest_path.write_text(json.dumps({"chapter": "CH08", "status": "draft-not-approved-for-publication", "files": members}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
with zipfile.ZipFile(zip_path, "x", compression=zipfile.ZIP_DEFLATED) as archive:
    for item, path in zip(members, files):
        archive.write(path, item["path"])
    archive.write(manifest_path, f"draft-output/{manifest_path.name}")
with zipfile.ZipFile(zip_path) as archive:
    bad = archive.testzip()
    if bad:
        raise SystemExit(f"CRC verification failed: {bad}")
    names = archive.namelist()
    if len(names) != len(set(names)):
        raise SystemExit("Duplicate archive paths detected")
digest = hashlib.sha256(zip_path.read_bytes()).hexdigest()
(out / f"PACKAGE-CHECKSUM-{revision}.json").write_text(json.dumps({"file": zip_path.name, "sha256": digest, "members": len(members) + 1, "crc": "PASS"}, indent=2) + "\n", encoding="utf-8")
print(f"PACKAGE PASS {zip_path} members={len(members)+1} sha256={digest}")
