# CH13 Final Acceptance Report

- **Chapter:** CH13 — 場面調度：空間、動線與視線 / *Mise-en-scène: Space, Blocking, and Eyelines* (working English title)
- **Run:** `production/runs/CH13/20261022T205359+0800-185a8aa8/`
- **Status:** **Complete as a bilingual research draft and local technical preview; not publication-ready.** Human editorial, source-location, film-viewing, rights, and author approval gates remain open.
- **Scope:** CH13 only. CH14 was not started. No website deployment, Git commit, or push was performed.

## Protection and inventory

- Before edits, CH13 contained only bilingual scaffold manuscripts, a figure manifest with no figures, empty asset folders, and a progress row marked not started. Existing V1 remains under `legacy/2026-v1`; no source pack or usable CH13 assets were present.
- The workspace already had extensive uncommitted changes for earlier chapters. They were preserved. Pre-edit copies of 18 target files and SHA-256 values are in `production/runs/CH13/20261022T205359+0800-185a8aa8/backup/pre-edit/MANIFEST.json`; initial Git status is in `backup/pre-edit/git-status-before.txt`.

## Chapter audit

| Item | Result | Evidence |
|---|---|---|
| Traditional Chinese draft | PASS — substantive sections CH13-S00–S12 | `content/zh-TW/chapters/CH13-chapter-13.md` |
| English draft | PASS as working translation — aligned S00–S12; human line editing remains | `content/en-US/chapters/CH13-chapter-13.md`; `metadata/translations/CH13-alignment.yaml` |
| Chapter metadata | PASS — working English title recorded; both locales remain review-needed | `metadata/chapters.yaml`; `metadata/translation-status.yaml` |
| Terms | PASS — six bilingual draft terms registered; none approved | `metadata/terminology.yaml`; `data/terms.yaml` |
| Sources | PASS — R094–R100 registered in YAML/BibTeX and cited in chapter | `data/references.yaml`; `metadata/references.bib`; `assets/chapters/CH13/CH13-SOURCE-AND-CASE-NOTES.md` |
| Source locator completeness | NEEDS HUMAN REVIEW — publisher summaries and role profiles support only limited claims; detailed book locators, BFI article metadata, and current successor for the historical UK standard need confirmation | Source notes; chapter S04/S05/S09/S12 |
| Film case facts and interpretation | PARTIAL — *Parasite* and Akerman examples are attributed to published criticism; no lawful viewing edition, first-hand viewing, or timecodes are claimed | Chapter S09; R098–R099 |
| Production workflow / AI limits | PASS as draft — planning, rehearsal, feasibility, continuity, safety, data, and human decision handoffs described | Chapter S05–S08 |
| Prompt / schema | PASS as illustrative draft — model-neutral prompt and proposed JSON fields; not an implemented standard or tested tool feature | Chapter S08 |
| Original figures | PASS as draft assets — two hand-authored editable SVGs; no third-party stills or image-generation service used | `assets/chapters/CH13/figures/originals/`; figure manifest |
| Figure IDs, hashes, XML, captions, alt | PASS — CH13-FIG-001/002 registered across manifest, metadata and both manuscripts; SVG XML parses; SHA-256 matches; bilingual captions explicitly say original illustration and not an official film still | `assets/chapters/CH13/figure-manifest.yaml`; `data/assets.yaml`; `metadata/figure-registry.yaml`; `tests/test_ch13_content.py` |
| Figure rights / approval | NEEDS HUMAN REVIEW — attribution, similarity, accessibility, rights, and publication approval remain pending; `asset_approved` is null | `CH13-FIGURE-RIGHTS-AND-SOURCES.md`; `CH13-HUMAN-REVIEW-CHECKLIST.md` |
| Site content sync | PASS — generated projections match canonical chapter manuscripts | `python scripts/publishing/sync_site_content.py --check` |
| Astro check/build | PASS — check has 0 errors, warnings, or hints; local static build completed for 123 routes. An initial loader duplicate-ID warning did not recur after sync; both CH13 route pages have 38 unique IDs and both figure anchors. | `npm --prefix apps/web run check`; `npm --prefix apps/web run build`; `apps/web/dist/zh-tw/ch13-chapter-13/index.html`; `apps/web/dist/en/ch13-chapter-13/index.html` |
| DOCX drafts | PASS — zh-TW and en-US local draft files generated | `tmp/CH13-draft-20261022-r2/` |
| PDF drafts / embedded fonts | PASS for build evidence — both PDFs generated; `pdffonts` reports 10 and 11 entries respectively with all listed entries embedded, including Microsoft JhengHei and Times New Roman. Spot-check of diagram pages showed legible Traditional Chinese and correctly numbered captions after Lua mapping update; this is not final typography approval. | Build output; PDF previews in `tmp/CH13-draft-20261022-r2/` |
| EPUB drafts / EPUBCheck | PASS — both archives pass EPUBCheck 5.4.0 with 0 fatal errors, 0 errors, 0 warnings, 0 informational references; ZIP CRC checks succeed | `tmp/CH13-draft-20261022-r2/*.epub`; `scripts/publishing/check_epub.ps1` |
| CH13 unit tests | PASS — 5/5 | `python -m unittest discover -s tests -p test_ch13_content.py -v` |
| V2 / project validators | PASS — V2 checks and project schema validation; 12 parts, 60 planned chapters, 67 terms, 95 references | `python scripts/v2_validate.py`; `python scripts/validate_project.py` |
| Link check | PARTIAL — 0 confirmed failures; 27 URLs not conclusively checked | `python scripts/validate/check_links.py` |
| Full test suite | FAIL — 88/89 pass; one unrelated pre-existing CH01 error: `KeyError: status` in `test_chapter_terms_are_bilingual_and_registered`; CH01 was not changed | `python -m unittest discover -s tests -v` |
| Publication gate | BLOCKED / NEEDS HUMAN REVIEW — all figure publication targets remain pending; author and required professional reviews are not recorded | Figure registries and human-review checklist |
| Image policy execution | BLOCKED — project-wide zh-TW site policy fails on the pre-existing CH01 figure (creator, attribution, permission and approvals unresolved); CH13 figures independently remain pending | `python scripts/image_policy.py --target zh-TW-site` (exit 2; output identifies CH01) |

## Remaining work

1. Bilingual editor: verify meaning, natural English, preferred Traditional Chinese terms, titles, captions, and alt text.
2. Film-theory/professional editor: check the definition boundaries, production practice, interpretation, safety and role descriptions.
3. Researcher: consult accessible full texts for precise page locators; verify the BFI article metadata and successor status for R097.
4. Film reviewer: view lawful editions of the cited films and record edition-specific timecodes only if useful.
5. Rights/accessibility reviewer and author: confirm originality/similarity, creator credit, accessibility, license, permission, and publication targets for both SVGs.
6. Author/publisher: proof the full chapter and approve before any publication-ready designation.
7. Resolve the existing CH01 test error separately; review the 27 unchecked external URLs.

**Conclusion:** CH13 has a substantive bilingual research draft and successful local draft builds. It is **not at formal publication standard** because source locators, human translation/professional review, film viewing checks, figure rights, and author approval remain open. All files remain local and uncommitted.
