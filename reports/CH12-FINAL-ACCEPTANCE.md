# CH12 Final Acceptance Report

- **Chapter:** CH12 — 演員調度、走位與表演連續性 / *Actor Blocking, Movement, and Performance Continuity* (working English title)
- **Run:** `production/runs/CH12/20261022T202702+0800-a0742107/`
- **Status:** **Research draft and local technical preview complete; not publication-ready.** Author, bilingual editor, film/performance/safety specialist, rights reviewer, and publisher approvals are not recorded.
- **Scope:** CH12 only. CH13 was not started. No deployment, Git commit, or push was performed.

## Protection and inventory

- The workspace was already extensively dirty across CH04–CH11, project registries, site content, and publication files. No unrelated changes were reset, deleted, or overwritten.
- Before editing, the CH12 run checkpoint preserved 18 target files under `production/runs/CH12/20261022T202702+0800-a0742107/backup/pre-edit/`; SHA-256 inventory: `backup/pre-edit/MANIFEST.json`; initial git status: `backup/pre-edit/git-status-before.txt`.
- CH12 had registry metadata and canonical scaffold files but no substantive manuscripts, source pack, or figure assets. Existing CH01–CH11 and V1 assets were retained.

## Chapter audit

| Item | Result | Evidence |
|---|---|---|
| Traditional Chinese manuscript | PASS — substantive research draft, stable sections CH12-S00–S13 | `content/zh-TW/chapters/CH12-chapter-12.md` |
| English manuscript | PASS — complete working translation aligned to S00–S13; still needs line editing | `content/en-US/chapters/CH12-chapter-12.md` |
| Chapter registry and translation map | PASS — working English title, source-draft/review-needed states, 14 paired section IDs | `metadata/chapters.yaml`, `metadata/translation-status.yaml`, `metadata/translations/CH12-alignment.yaml` |
| Terms | PASS — nine bilingual draft terms, all explicitly unapproved | `metadata/terminology.yaml`, `data/terms.yaml`, `assets/chapters/CH12/CH12-terms.yaml` |
| Sources | PASS — R087–R093 in YAML/BibTeX and chapter source notes; claims scoped to evidence | `data/references.yaml`, `metadata/references.bib`, `assets/chapters/CH12/CH12-SOURCE-AND-CASE-NOTES.md` |
| Research locator completeness | NEEDS HUMAN REVIEW — R087 full chapter unavailable; page-specific claims unverified; source scope/jurisdiction and film edition/timecodes require review | Source notes and citations in S04, S09, S12 |
| Film case accuracy | PARTIAL — *The Graduate*, *Lola Montès*, and *A Clockwork Orange* examples have traceable published sources; no lawful viewing edition or first-hand timecode is claimed | CH12-S09; `CH12-SOURCE-AND-CASE-NOTES.md` |
| Traditional production workflow | PASS as draft — eight production steps, responsibility handoffs, safety/consent checks, continuity record fields | CH12-S05–S07 |
| AI process and prompt | PASS as draft — explicitly untested hypothesis, model-neutral prompt, privacy and human-review limits | CH12-S06–S08 |
| Exercises and rubric | PASS as draft — original chair/two-objectives exercise and 0–2 rubric | CH12-S11 |
| Original figures | PASS as draft assets — two hand-authored editable bilingual SVGs; no third-party images or generated film stills used | `assets/chapters/CH12/figures/originals/`, `figure-manifest.yaml`, `figure-captions.md` |
| Figure IDs, hashes, XML, captions and alt | PASS — both figures are registered, both hashes match, SVG parses, bilingual captions state they are not film stills, alt text exists | `tests/test_ch12_content.py`; `figure-manifest.yaml`; `metadata/figure-registry.yaml`; `data/assets.yaml` |
| Figure rights/approval | NEEDS HUMAN REVIEW — attribution, similarity, accessibility, creator identity, rights, and publication approval remain pending; `asset_approved` is null | `figure-manifest.yaml`, `CH12-HUMAN-REVIEW-CHECKLIST.md` |
| Site projections | PASS — canonical sync check clean; zh-TW/en routes each built with 41 unique IDs, both figure IDs and nonempty alt text | `apps/web/dist/zh-tw/ch12-chapter-12/index.html`, `apps/web/dist/en/ch12-chapter-12/index.html` |
| Astro check/build | PASS — second check: 0 errors/warnings/hints; static site build completed for 120 routes. Initial check emitted a duplicate-ID loader notice that did not recur on rerun; route HTML was checked for duplicate IDs (none). | `npm --prefix apps/web run check`; `npm --prefix apps/web run build` |
| Chapter material pack | PASS — final draft-only ZIP with 19 manuscript, registry, original-figure, review, and format files; CRC verified; SHA-256 in `tmp/CH12-draft-20261022-r1/OUTPUT-MANIFEST-r2.json`. The canonical acceptance report is external to avoid a circular package hash. Earlier r1 is retained as an intermediate snapshot. | `tmp/CH12-draft-20261022-r1/CH12-Codex-Materials-DRAFT-r2.zip` |
| DOCX drafts | PASS — zh-TW and en-US generated locally | `tmp/CH12-draft-20261022-r1/CH12-zh-TW-draft.docx`, `CH12-en-US-draft.docx` |
| PDF drafts and text extraction | PASS — zh-TW 8 pages, en-US 12 pages; no U+FFFD replacement characters; both figure numbers appear once | `tmp/CH12-draft-20261022-r1/*.pdf` |
| PDF fonts | PASS for embedding — build’s `pdffonts` evidence lists 12 font entries per PDF, each embedded; Microsoft JhengHei and Times New Roman included. Visual spot-check of pages 4–5 (zh-TW) and 6, 8 (en-US) showed legible diagrams and captions. This is a draft proof, not final typography approval. | Build output; rendered previews under `tmp/CH12-draft-20261022-r1/` |
| EPUB drafts | PASS — both archives pass CRC checks, contain two chapter figure references, and no replacement characters | `tmp/CH12-draft-20261022-r1/CH12-zh-TW-draft.epub`, `CH12-en-US-draft.epub` |
| EPUBCheck | PASS — EPUBCheck 5.4.0: 0 fatal errors, 0 errors, 0 warnings, 0 informational references for both locales | `scripts/publishing/check_epub.ps1 -Epub @(...)` |
| CH12 unit tests | PASS — 5/5 | `python -m unittest tests.test_ch12_content -v` |
| V2 / project validators | PASS — V2 registry/image-policy validation and project schema validation (12 parts, 60 chapters, 61 terms, 88 references) | `python scripts/v2_validate.py`; `python scripts/validate_project.py` |
| Site sync and link checks | PASS / PARTIAL — site projection current; link checker reports 0 failures, 27 URLs not conclusively checked | `python scripts/publishing/sync_site_content.py --check`; `python scripts/validate/check_links.py` |
| Full test suite | FAIL — 83/84 tests pass; one pre-existing CH01 failure: `KeyError: 'status'` in `tests/test_ch01_content.py::test_chapter_terms_are_bilingual_and_registered`. CH01 was not modified. | `python -m unittest discover -s tests -v` |
| Image publication policy | BLOCKED by design — images remain pending human review; the global site policy also finds pending CH01 figures, so it cannot authorize publication | `python scripts/image_policy.py --target zh-TW-site` |
| Final editorial and legal review | NEEDS HUMAN REVIEW — required before any publication-ready designation | `assets/chapters/CH12/CH12-HUMAN-REVIEW-CHECKLIST.md` |
| Git/deployment guard | PASS — no deploy, commit, or push performed | current session actions; workspace changes remain local |

## Remaining work

1. Bilingual editor to review terminology, meaning, captions, and the provisional English title.
2. Film/performance specialist to review blocking vocabulary, theory, safety framing, source locators, and the case interpretations.
3. Record lawful viewing editions and timecodes if the author wishes to include shot-level analyses; none are invented here.
4. Rights reviewer and author to confirm SVG attribution, similarity, license/permission, accessibility, and publication status.
5. Author/publisher to conduct final proof and approval; no chapter approval is recorded.
6. Resolve the unrelated CH01 unit-test error and review 27 unchecked external URLs when appropriate.
7. Re-run the full project suite after required reviews and before publication.

**Conclusion:** CH12 has a complete, testable bilingual research draft and local publication previews. It is **not at formal publication standard** while professional, source-location, translation, rights, and author-review gates remain open. Stop after CH12; do not start CH13 until separately requested.
