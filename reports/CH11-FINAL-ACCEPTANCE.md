# CH11 Final Acceptance Report

- **Chapter:** CH11 — 導演工作：意圖、溝通與決策 / *Directing: Intention, Communication, and Decision-Making* (working English title)
- **Run:** `production/runs/CH11/20261022T181247+0800-46c00c02/`
- **Status:** **Research draft complete; not publication-ready.** No author, bilingual-editor, film-professional, or rights approval is recorded.
- **Scope:** CH11 only. No CH12 work, website deployment, Git commit, or push was performed.

## Protection and inventory

- The repository already had substantial uncommitted CH04–CH10 work when CH11 began. That work was retained; see the run checkpoint and the recorded pre-edit backup.
- Before editing, 17 target files were copied under `production/runs/CH11/20261022T181247+0800-46c00c02/backup/pre-edit/`, with SHA-256 values in `backup/pre-edit/MANIFEST.json`. The backup represents the prior scaffold and repository state; CH11 target files and registries were intentionally updated in this run.
- Existing V1 and CH01–CH10 materials were not deleted or replaced.

## Work completed

| Check | Result | Evidence |
|---|---|---|
| Traditional Chinese manuscript | PASS — substantive S00–S12 research draft | `content/zh-TW/chapters/CH11-chapter-11.md` |
| English manuscript | PASS — substantive working translation, not line-edited | `content/en-US/chapters/CH11-chapter-11.md` |
| Chapter registry and bilingual alignment | PASS — CH11 title, state, 13 stable section IDs and eight term IDs registered | `metadata/chapters.yaml`, `metadata/translation-status.yaml`, `metadata/translations/CH11-alignment.yaml` |
| Sources | PASS — R077–R086 registered in YAML/BibTeX; research notes state scope and limits | `data/references.yaml`, `metadata/references.bib`, `assets/chapters/CH11/CH11-SOURCE-AND-CASE-NOTES.md` |
| Terminology | PASS — eight bilingual draft terms registered; not approved glossary definitions | `metadata/terminology.yaml`, `metadata/translations/CH11-alignment.yaml` |
| Film case | PARTIAL — *The Godfather* credits and published descriptions trace to AFI/ASC; no first-hand viewing version/timecode claimed | CH11 manuscript S09; source notes |
| Original figures | PASS as draft assets — two editable SVGs, bilingual captions and alt text; no third-party stills or image generation used | `assets/chapters/CH11/figure-manifest.yaml`, `figure-captions.md`, `metadata/figure-registry.yaml`, `data/assets.yaml` |
| Figure file integrity | PASS — SHA-256/bytes/dimensions match all three manifests/registries; XML parses | `tests/test_ch11_content.py`; hashes in figure manifest |
| SVG proof review | PASS for current draft layout — feedback arrow separation and department labels adjusted after proof inspection | `tmp/CH11-draft-20261022-r3/proof/zh-TW-p4.png`, `zh-TW-p6.png`, `en-US-p5.png`, `en-US-p7.png` |
| Website projection | PASS — canonical content sync check clean; two built CH11 routes each have 39 unique IDs, two figures and nonempty alt text | `apps/web/dist/en/ch11-chapter-11/index.html`, `apps/web/dist/zh-tw/ch11-chapter-11/index.html` |
| Astro check/build | PASS — `npm --prefix apps/web run check` reports 0 errors/warnings/hints; local build produced 123 pages | local build output in `apps/web/dist/`; not deployed |
| PDF drafts | PASS — zh-TW 9 pages, en-US 11 pages; extracted text has no U+FFFD; figure numbers present once each | `tmp/CH11-draft-20261022-r3/CH11-zh-TW-draft.pdf`, `CH11-en-US-draft.pdf` |
| PDF font embedding | PASS — `pdffonts` confirms embedded/subset fonts for Microsoft JhengHei and Times New Roman, including bilingual scripts | build log; both PDFs in r3 |
| EPUB drafts | PASS — ZIP CRC valid; four XHTML documents per EPUB; no replacement characters; both figure labels present | `tmp/CH11-draft-20261022-r3/CH11-zh-TW-draft.epub`, `CH11-en-US-draft.epub` |
| EPUBCheck | PASS — both language files report 0 fatal errors, 0 errors, 0 warnings and 0 informational references | EPUBCheck 5.4.0 output, run on both r3 EPUBs |
| Project validators | PASS — `python scripts/v2_validate.py`; `python scripts/validate_project.py` (12 parts, 60 planned chapters, 52 terms, 81 references) | command output, 2026-10-22 |
| CH11 tests | PASS — 5/5 | `python -m unittest tests.test_ch11_content -v` |
| Full test suite | FAIL (unrelated existing CH01 issue) — 78/79 pass; CH01 test raises `KeyError: 'status'` in `tests/test_ch01_content.py`; CH01 was not changed in response | `python -m unittest discover -s tests -v` |
| External reference link check | PARTIAL — 0 failures, 27 links not conclusively checked; checker reached 0 network URLs in this run | `python scripts/validate/check_links.py`; unchecked does not mean broken |

## Human review still required

All items below remain **NEEDS HUMAN REVIEW** in `assets/chapters/CH11/CH11-HUMAN-REVIEW-CHECKLIST.md`:

1. Film-directing theory/history, edition-specific page locators and claims about collaboration/auteurism.
2. Traditional workflow scope and role descriptions for the intended production context.
3. DGA handbook/agreement wording and any jurisdiction-specific legal interpretation.
4. Full English line edit and bilingual terminology choices.
5. Lawful *The Godfather* viewing edition, restoration/release information, observer notes and timecodes; no shot-level claim should be added without that evidence.
6. Tool/privacy policy review only if a concrete AI service is selected; no tool-specific capability is asserted as verified here.
7. SVG creator attribution, rights, visual similarity, accessibility, design and publication approval.
8. Author approval tied to a specific manuscript/asset revision.

The figure records remain `draft-original-svg`, with rights, technical/editorial and publication approvals pending. This draft is **not publication-ready**.

## Commands executed

```text
python -m unittest tests.test_ch11_content -v
python -m unittest discover -s tests -v
python scripts/v2_validate.py
python scripts/validate_project.py
python scripts/validate/check_links.py
python scripts/publishing/sync_site_content.py --check
npm --prefix apps/web run check
npm --prefix apps/web run build
python scripts/publishing/build_chapter_drafts.py --chapter 11 --out-dir tmp/CH11-draft-20261022-r3 --font "Microsoft JhengHei" --latin-font "Times New Roman"
java -jar <EPUBCheck 5.4.0 jar> <each CH11 r3 EPUB>
```

## Final decision

**CH11 is complete as an evidence-tracked research draft and local publication preview. It has not met formal publication standards.** The unresolved human reviews above, unverified external links, missing lawful viewing log/timecodes, and the unrelated CH01 full-suite error remain visible. Do not label the chapter `publication-ready` until the relevant reviews and final proof are recorded.
