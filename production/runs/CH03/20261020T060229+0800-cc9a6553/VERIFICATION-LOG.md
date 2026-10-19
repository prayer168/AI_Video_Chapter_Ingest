# CH03 Run Verification Log

- Run: `20261020T060229+0800-cc9a6553`
- Date: 2026-10-20 Asia/Taipei
- Final run state: `partial` — authorized draft work is complete; human review and publication approval are deferred.
- Report: `reports/CH03-FINAL-ACCEPTANCE.md`
- Backup manifest: `backups/CH03-start-20261020-060306/BACKUP-MANIFEST.json`
- Output manifest: `tmp/CH03-draft-20261020/OUTPUT-MANIFEST.json`
- Material pack: `tmp/CH03-draft-20261020/CH03-Codex-Materials-DRAFT-r2.zip` (the earlier draft archive is preserved)

## Source and content checks

- Checked official open university textbook pages for R022 and Columbia University Film Language Glossary page R030 on 2026-10-20; records updated in `data/references.yaml` and `metadata/references.bib`.
- Bilingual anchors: 15 per locale, identical set (`CH03-S00`–`CH03-S14`).
- Draft glossary terms: 8 paired IDs, all `draft`.
- Figures: 2 paired IDs; originals are editable SVG and both SHA-256 values match `assets/chapters/CH03/figure-manifest.yaml` and `metadata/figure-registry.yaml`.
- Figure status: rights, technical, editorial, and publication approval remain pending.

## Commands and results

| Check | Result |
|---|---|
| `python scripts/v2_validate.py` | PASS |
| `python scripts/validate_project.py` | PASS; registry reports 12 parts / 60 planned chapters |
| `python scripts/publishing/sync_site_content.py --check` | PASS |
| `python -m unittest discover -s tests -v` | PASS; 40/40 |
| `python scripts/validate/check_links.py` | 0 failures; 0 network checked; 5 inconclusive |
| `npm --prefix apps/web run check` | PASS; 0 errors / warnings / hints |
| `npm --prefix apps/web run build` | PASS; 123 local pages, no deployment |
| Chapter-only Pandoc DOCX/PDF/EPUB, both locales | PASS after replacing the layout-only SVG references with Inkscape-derived PNGs; canonical manuscripts retain SVG references |
| DOCX ZIP CRC and media check | PASS; 2 images in each locale |
| PDF strict font check | PASS; Microsoft JhengHei plus Consolas entries embedded in both locales |
| PDF text extraction / rendered-page inspection | PASS for text extraction; cover/TOC page and page 7 with figures visually inspected; no duplicated figure numbering after filter mapping fix |
| EPUBCheck 5.4.0 | PASS; both locales: 0 errors, warnings, informational messages, or references |
| EPUB package check | PASS; ZIP CRC valid, 2 media files per locale, bilingual body text and figure IDs present |
| Chapter-specific ID/hash/alt/status checks | PASS; 15 anchor pairs, 8 term pairs, 2 figure pairs, local website routes each show 2 figures with nonempty alt |
| `git diff --check` | PASS; only existing LF/CRLF working-copy notices |

## Environment issues and repairs

1. Pandoc inherited a Windows console encoding that could not print a Unicode path from the Google Drive working directory. Running from the ASCII working directory `C:\Users\user\Documents` with `LANG=C.UTF-8` and `LC_ALL=C.UTF-8` resolved it.
2. `rsvg-convert` is not installed, so Pandoc could not rasterize the new SVGs for DOCX/PDF. Inkscape 1.4.4 exported 1600-pixel PNG layout derivatives under the ignored `tmp/` directory; the editable SVG masters were not altered.
3. PDF preview initially duplicated the manual and automatic figure labels. The previous Lua filter was backed up; CH03 figure-number mappings were added and both PDFs were rebuilt and rechecked.
4. Pandoc still warns that its `zh-TW` translation file and some template labels (`Abstract`, `Table`, `Figure`) are unavailable. This affects template localization warnings, not the successful EPUBCheck package validation; keep this warning visible for later publication-template work.

## Approval boundaries

- English translation, film theory/terminology, source edition and locator, lawful film editions/timecodes, illustration creator attribution, rights/similarity/accessibility review, and author approval are not signed off.
- These reviews are intentionally deferred until all chapters are drafted, per the user’s editorial workflow.
- No paid image service was called. No website was deployed. No commit or GitHub push was made.
