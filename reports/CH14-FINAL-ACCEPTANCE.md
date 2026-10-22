# CH14 Final Acceptance / 最終驗收報告

- Chapter: **CH14 — 分鏡、預視覺化與鏡頭清單 / Storyboards, Previsualization, and Shot Lists**
- Run: `production/runs/CH14/20261022T224558+0800-f4a29f11/`
- Backup: `backups/CH14-start-20261022-224652/`
- Overall: **PARTIAL — bilingual research draft and local publication previews are ready for human review; not publication-ready.**
- Scope: CH14 only. CH15 was not started. No site was deployed, no Git commit/push was performed.

## Protection and inventory

| Check | Status | Evidence |
|---|---|---|
| Existing V1/V2 and CH14 scaffold protected | PASS | Original CH14 manuscript and manifest copies plus pre-edit `git status --short` are in the backup folder. V1 is retained under `legacy/2026-v1`. |
| Existing worktree changes preserved | PASS | Existing unrelated dirty files were not reset, cleaned, or overwritten. |
| CH14 material inventory | PASS | Initial canonical files were blank S01–S12 scaffolds and an empty figure manifest; no source pack or existing figure files were found. |

## Editorial deliverables

| Item | Status | Evidence / remaining work |
|---|---|---|
| Traditional Chinese chapter S00–S12 | PASS as draft | `content/zh-TW/chapters/CH14-chapter-14.md`; substantive draft, not an approved manuscript. |
| English counterpart S00–S12 | NEEDS HUMAN REVIEW | `content/en-US/chapters/CH14-chapter-14.md`; aligned working translation, requires bilingual copyedit. |
| Section alignment | PASS | `metadata/translations/CH14-alignment.yaml`; 13 stable IDs agree in both files. |
| Five bilingual terms | PASS as draft | `metadata/terminology.yaml` and `data/terms.yaml`; definitions and linked source IDs registered, terminology review pending. |
| Sources R101–R106 | PASS, scope-limited | `data/references.yaml`, `metadata/references.bib`, and chapter bibliography. Publisher pages, ASC practitioner interviews, Epic/Blender official documentation used. R101 publisher page only; full text and page locators were not consulted. External link checker left 27 URLs inconclusive across the existing project; no confirmed failures. |
| Film cases | NEEDS HUMAN REVIEW | ASC interview sources for *Three Billboards Outside Ebbing, Missouri* and *Indiana Jones and the Temple of Doom* support attributed production statements. Lawful viewing editions, scene observations, and timecodes remain unlogged. |
| Two original diagrams | PASS as draft assets | Editable SVGs in `assets/chapters/CH14/figures/originals/`; hashes, dimensions, bilingual captions and alt text in `assets/chapters/CH14/figure-manifest.yaml`, global figure and asset registries. No third-party film stills used. Rights/attribution/accessibility approval is pending. |
| Rights checklist | NEEDS HUMAN REVIEW | `assets/chapters/CH14/CH14-FIGURE-RIGHTS-AND-SOURCES.md` and `CH14-HUMAN-REVIEW-CHECKLIST.md`; no figure is approved for publication. |

## Technical validation

| Check | Status | Evidence |
|---|---|---|
| Project schema validation | PASS | `python scripts/validate_project.py` passed: 12 parts, 60 chapter records, 72 terms, 101 references. |
| V2 architecture validation | PASS | `python scripts/v2_validate.py` passed. |
| CH14 targeted tests | PASS | `python -m unittest discover -s tests -p 'test_ch14_content.py' -v`: 4/4. |
| Full unit suite | FAIL (pre-existing CH01 issue) | `python -m unittest discover -s tests -v`: 93 tests, 92 pass, 1 error in `test_ch01_content.py::test_chapter_terms_are_bilingual_and_registered`; `KeyError: 'status'` for a CH01 term. CH14 tests pass. CH01 was not changed. |
| Website source sync | PASS | `python scripts/publishing/sync_site_content.py --check` passed; both CH14 language pages and figure assets are current. |
| Astro type/content check | PASS | `npm --prefix apps/web run check`: 0 errors, 0 warnings, 0 hints on final run. An earlier transient duplicate-ID warning did not recur on the final check/build. |
| Local static website build | PASS | `npm --prefix apps/web run build`: 123 static pages built, including `/en/ch14-chapter-14/` and `/zh-tw/ch14-chapter-14/`. This is a local build only; not deployed. |
| DOCX / EPUB / PDF drafts | PASS | `tmp/CH14-draft-20261022-r1/` contains Chinese and English draft outputs for all three formats. |
| PDF font embedding | PASS | `scripts/check_fonts.py --require-pdffonts` was invoked by the build; Chinese PDF contains embedded Microsoft JhengHei and English PDF contains embedded Times New Roman plus embedded CJK fallback. Both checks passed. Rendered first pages are in `tmp/CH14-draft-20261022-r1/rendered/`. |
| EPUBCheck | PASS | EPUBCheck 5.4.0: both EPUBs reported zero errors, warnings, and informational messages. |
| Reference link reachability | PARTIAL | `python scripts/validate/check_links.py`: 0 confirmed failures; 27 links were not conclusively checked and require manual/internet follow-up. |

## Run-stage record

The machine-readable run checkpoint is `production/runs/CH14/20261022T224558+0800-f4a29f11/run.json`; unfinished human review gates are explicitly recorded. Full test suite remains FAIL because of the pre-existing CH01 test error, so the run is partial rather than complete.

## Remaining work before publication

1. Bilingual editor reviews the English translation, headings, term choices, captions, and cross-language equivalence.
2. Film/production specialist verifies definitions, workflow suitability, and source-scope limitations.
3. Author views lawful copies of both films, logs edition and exact timecodes, and confirms whether the case analysis is sufficiently evidenced.
4. Rights holder confirms figure attribution, authorship, similarity risk, accessibility, and target-specific publication permission.
5. Author completes proof review and publication approval.
6. Repair the unrelated CH01 `status` registry/test mismatch, then rerun the full project suite.
7. Recheck the 27 inconclusive project links; do not treat unchecked as broken or verified.

**Publication decision: NOT APPROVED.** Technical draft builds are evidence of format generation only; human review and author approval remain open.
