# CH02 Verification Log — 2026-10-19

## PASS
- `python scripts/v2_validate.py`
- `python scripts/validate_project.py`
- `python scripts/publishing/sync_site_content.py --check`
- `python -m unittest discover -s tests -v` — 40/40
- `python scripts/validate/check_links.py` — 0 failures; 0 network checked; 5 inconclusive (not proof of link health)
- `npm --prefix apps/web run check` — 0 errors/warnings/hints
- `npm --prefix apps/web run build` — 123 static pages, local only
- CH02 bilingual route audit — 5 figures and nonempty alt per route
- Pandoc CH02 DOCX/EPUB/PDF previews — both locales
- `pdffonts` strict checks — fonts embedded; 20-page zh-TW and 16-page en-US; extracted labels/no U+FFFD
- EPUBCheck 5.4.0 — both locales exit 0
- Source/assets custom audit — 15 citation IDs resolve, 5/5 figures per locale, 10 unique global figure IDs; V1/ZIP hashes unchanged
- `git diff --check` — exit 0 (pre-existing LF/CRLF notices only)

## BLOCKED / NEEDS HUMAN REVIEW
- Full 60-chapter formal book build: approval gate requires every chapter approved.
- CH02 publication: bilingual edit, film-edition/timecode verification, terminology and theory/source locators, SVG authorship/accessibility/rights, and author approval remain pending.
- Site deployment was not run.

## Resolved test/build issues
- Synced stale site projection before rerunning Astro check; duplicate-ID warnings cleared.
- Removed duplicated canonical figure insertion by rebuilding from unchanged staging manuscripts and fixing only paths/figure captions. Updated the old scaffold-immutability test to verify the authorized migration while protecting V1 and source ZIP.
- MiKTeX `dvipdfmx: Invalid font: -1` with Noto Serif TC resolved for preview by using Microsoft JhengHei; strict embedded-font verification passed.
- Fixed duplicate English PDF figure labels in `figure-captions.lua`.
- Captured tool logs as UTF-8 after Windows cp950 decode interrupted one first preview attempt.

Pipeline run: `production/runs/CH02/20261019T225451+0800-a105b6d9`
Acceptance: `reports/CH02-FINAL-ACCEPTANCE.md`
Draft outputs and SHA manifest: `tmp/CH02-draft-integration-20261019-r1/`
