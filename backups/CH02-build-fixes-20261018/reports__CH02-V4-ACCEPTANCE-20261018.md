# CH02 V4 Draft Acceptance Report

- Chapter: CH02 — 鏡頭、場面與剪接：電影語言的基本單位
- Run: `production/runs/CH02/20261018T215615+0800-55868375/`
- Draft revision: `2.1.0-draft`
- Report date: 2026-10-18 (Asia/Taipei)
- Decision: **PARTIAL — editorially reviewable draft; not publication-ready**

## Scope and preservation

The substantive legacy chapter and its source pack were read and cross-referenced. The source ZIP passed its CRC test and its recorded SHA-256 is `d448defde21abe8802ad87684928eaade0f7c39101b423159073391457a519a5`. A pre-change snapshot is retained at `backups/CH02-pipeline-20261018-215634/`; a finalization snapshot is at `backups/CH02-finalization-20261018/`. The original V1 manuscript, canonical V2 Chinese and English scaffolds, global chapter registry, and source archive were not overwritten. The V4 deliverables remain additive under `staging/CH02-V4/`.

## Acceptance results

| Check | Result | Evidence / remaining work |
|---|---|---|
| Inventory and source preservation | PASS | Source archive CRC passed; original source and canonical scaffold hashes are recorded in `staging/CH02-V4/SOURCE-AND-ASSET-RECORD.json`; backup manifests are present. |
| Traditional Chinese draft | PASS — draft only | Substantive 13-section draft with stable anchors CH02-S00–S12 at `staging/CH02-V4/zh-TW/CH02-camera-language.md`. |
| English translation | NEEDS HUMAN REVIEW | Substantive English editorial translation exists at `staging/CH02-V4/en-US/CH02-camera-language.md`; it is not an approved translation. |
| Section alignment | PASS — draft alignment | 13 stable section pairs in `staging/CH02-V4/CH02-alignment.yaml`; automated test confirms IDs match. An editor must verify meaning and omissions. |
| Bilingual terminology | PASS — draft terminology | 26 stable term IDs, Chinese and English labels/definitions in `staging/CH02-V4/glossary-CH02.yaml`; professional terminology review remains open. |
| Reference traceability | PASS — staged records; factual review open | Staged bibliography `staging/CH02-V4/references.bib`; source crosswalk at `staging/CH02-V4/source-records/CH02-source-crosswalk.md`. Added R025–R029 to the Chinese reference list. Textbook edition/page locators and exact film sequence/timecode still need verification. |
| Film example | NEEDS HUMAN REVIEW | A *Jaws* dolly-zoom example is sourced to the American Cinematographer article. Confirm lawful viewing edition, exact sequence/timecode, and shot description before publication. |
| Original editable diagrams | PASS — files/hash checked; editorial review open | Five authored SVGs parse as XML, have matching recorded SHA-256, and are referenced in both drafts and the manifest. They are project-authored diagrams, not third-party images; visual accuracy, accessibility, language layout, and final rights/editorial review remain pending. |
| Prompts and production parameters | NEEDS HUMAN REVIEW | Demonstration prompts are explicitly not-run. No AI generation service or paid API was invoked; no generated raster image is claimed. Record actual model/version/settings only after an authorized test. |
| Automated tests | PASS | `python -m unittest discover -s tests -v`: 40/40 passed. Expected negative font-validation cases emit error text while the test suite confirms rejection behavior. `python scripts/v2_validate.py`, `python scripts/validate_project.py`, `python scripts/publishing/sync_site_content.py --check`, `python -m compileall -q scripts tests`, and `git diff --check` passed. |
| Website toolchain | PASS — project baseline only | `npm run check`: 0 errors, warnings, hints. `npm run build`: 123 pages. These commands built the canonical site; canonical CH02 is still a scaffold, so they do not validate or publish this staged CH02 content. No deployment occurred. |
| CH02 website route | BLOCKED pending editorial integration | The staged draft is intentionally not copied into canonical content or the site projection. After editor review and approval, integrate additively, then check both locale routes and figure rendering. |
| DOCX / PDF / EPUB | BLOCKED by local tools | Current PowerShell PATH has no `pandoc`, `xelatex`, `pdffonts`, or `epubcheck`. No CH02 book artifact was built. Install/locate the documented tools, then build into a fresh draft output directory. |
| Embedded Traditional Chinese font and rendered pages | BLOCKED | No PDF exists for this CH02 draft. Font installation alone would not pass this gate; inspect embedded font entries and render pages for visual review after a PDF build. |
| EPUB structure | BLOCKED | No EPUB exists and EPUBCheck is unavailable on PATH. Validate the generated package with EPUBCheck after tooling setup. |
| Chapter title / registry consistency | NEEDS HUMAN REVIEW | The source subtitle and registry title differ. Confirm final Chinese and English chapter titles before canonical integration; do not change the TOC implicitly. |
| Publication approval | NOT APPROVED | Author approval, bilingual editorial review, source locators, film fact/timecode checks, diagram review, and successful book-format gates are outstanding. Do not label publication-ready. |

## Sources used for scoped verification

The Columbia glossary describes the 180-degree convention and camera movement terminology; the American Cinematographer article supports the cited *Jaws* dolly-zoom production example. ZEISS and Canon technical education pages support the bounded lens/perspective and depth-of-field discussions. Runway's Gen-4 guide is treated as current, model-specific vendor documentation, not general film theory or a guarantee of physical camera control. All web pages were accessed 2026-10-18; re-check time-sensitive vendor guidance before release.

## Remaining work

1. A film-studies/editorial reviewer should verify every historical and technical claim against the cited edition and add page/chapter locators where needed.
2. A bilingual editor should review all 13 section pairs, the 26 terms, figure captions/alt text, and the English adaptation.
3. Verify the *Jaws* viewing edition and exact sequence/timecode; review the film discussion for accuracy and scope.
4. Confirm the chapter title against the TOC and resolve the English registry title.
5. Review SVG diagram pedagogy, accessibility, contrast, localization, print scaling, and rights status.
6. Install/locate Pandoc, XeLaTeX, PDF font inspection, and EPUBCheck; then produce draft DOCX/PDF/EPUB in a new output folder and perform rendered-page and package checks.
7. Integrate the reviewed draft into canonical bilingual content only after editorial acceptance; then rebuild and inspect the two CH02 routes.
8. Obtain author approval before any `publication-ready` status.

No V1 source was overwritten; no source archive or image was deleted; no site was deployed; no GitHub push or commit was made.
