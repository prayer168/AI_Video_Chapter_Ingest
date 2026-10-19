# Chapter Pipeline V4 — Test Report

- Test date: 2026-10-18 (Asia/Taipei)
- Scope: V4 checkpoint workflow and CH01 end-to-end verification against existing CH01 V2.1.0 sources.
- Result: **automation and technical checks pass; CH01 publication readiness remains blocked by human approvals and provenance gaps.**
- No canonical manuscript, legacy V1 file, or existing image was overwritten. No image generation API was called. No website was deployed and no GitHub push was performed.

## Environment and preservation

- Pre-change backup: `backups/V4-pipeline-20261018-211633/`; manifest records the saved pre-change `history.md` and CH01 acceptance report.
- Existing CH01 Chinese and English canonical manuscripts, manifest, and translation alignment were inventoried with SHA-256 in `production/runs/CH01/20261018T211950+0800-6ddc17e8/run.json`.
- Five pre-existing original-illustration PNGs were retained and were not regenerated.
- Skill installed at `.codex/skills/ai-video-bible-chapter-pipeline/` and mirrored to the user's Codex skills directory. The skill validator reported `Skill is valid!` with UTF-8 mode enabled.

## Results

| Check | Status | Evidence |
|---|---|---|
| V4 pipeline and image-adapter unit tests | PASS | `python -m unittest tests.test_chapter_pipeline tests.test_image_generation_adapter -v`: 6 tests passed. |
| Full project test suite | PASS | `python -m unittest discover -s tests -v`: 35 tests passed. Expected error messages in font-validator negative tests are assertions; the suite exit code was 0. |
| V2 architecture validation | PASS | `python scripts/v2_validate.py`: 12 parts, 60 chapter registry and image-policy gates pass. |
| Project validation | PASS | `python scripts/validate_project.py`: 12 parts, 60 planned chapters, 2 canonical chapter files, 52 terms, 24 references. |
| Site content projection | PASS | `python scripts/publishing/sync_site_content.py --check`: canonical bilingual Markdown and local images current. |
| Astro diagnostics | PASS | `npm run check`: 0 errors, 0 warnings, 0 hints. |
| Static bilingual site build | PASS | `npm run build`: 123 HTML pages generated; no deploy performed. |
| CH01 bilingual content/assets regression | PASS | Full suite includes required substantive bilingual sections, citation registry, terms, stable translation anchors, figure manifest/caption/alt synchronization, local image presence and pending-review state. |
| Existing CH01 PDF and font proof | PASS (previously verified) | Latest CH01 finalproof evidence is recorded in `reports/CH01-FINAL-ACCEPTANCE.md`: 14-page zh-TW and 20-page en-US PDFs; embedded font streams and figure/caption layout were inspected. This V4 run did not modify canonical chapter sources, so the existing proof was reused, not represented as a new V4 PDF build. |
| Existing CH01 EPUB validation | PASS (previously verified) | Same acceptance report records EPUBCheck 5.4.0 results: 0 errors, warnings, informational messages, or references for each language. |
| Image generation service | BLOCKED | Native image generation capability is available in this environment, but commercial terms, exact per-run cost, and an explicit user budget authorization are not established. No provider/API was called. Local ComfyUI/Ollama was not found in the prior machine audit. |
| Editable SVG chapter figure | NEEDS HUMAN REVIEW | No existing CH01 editable SVG was found in its image inventory. The pipeline does not invent a new canonical figure or figure number without an editorial placement decision. |
| Research, film-case and translation approval | NEEDS HUMAN REVIEW | Existing references/cases are present; source locators, film-version/timecode verification, theoretical interpretation and professional bilingual edit remain editorial gates. |
| Illustration provenance and rights | NEEDS HUMAN REVIEW | Five files exist and stay pending review. The source ZIP did not provide verified generator/model/version, date, complete prompt or operator/edit log. Similarity, rights and subject/mark review remain human approvals. |
| Publication approval | BLOCKED | Author approval and professional editorial/rights sign-off are outstanding. No status is upgraded to publication-ready. |

## CH01 pipeline checkpoint

The run started in inspection/checkpoint mode. Steps that can be evidenced mechanically are recorded as PASS; author-dependent work remains NEEDS HUMAN REVIEW or BLOCKED in `run.json` and `CHECKLIST.md`. The run ends as `partial`, never `complete`.

## Remaining actions

1. Author and film researcher verify the five homage cases, exact editions, source locators and timecodes.
2. Complete professional Traditional Chinese and English editorial review and verify all citations against source editions.
3. Review original-image provenance, composition/similarity, likeness/trademark risks, accessibility text and each publication target; record an explicit author decision.
4. Decide whether CH01 needs an additional editable SVG diagram and approve its scope/location before assigning a new stable figure ID.
5. After approvals, rebuild the chapter deliverables from canonical sources and perform final visual proofing; do not treat draft builds as publication approval.
