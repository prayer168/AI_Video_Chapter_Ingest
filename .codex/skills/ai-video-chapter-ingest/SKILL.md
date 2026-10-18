---
name: ai-video-chapter-ingest
description: Ingest and editorially integrate new manuscript drafts or source packs into the AI-Filmmaking-Bible chapter repository. Use when the user asks to process files placed under chapters/ or provides a chapter source pack.
metadata:
  short-description: Process book chapter source packs
  display-name: AI_Video_Chapter_Ingest
---

# AI Video Chapter Ingest workflow

Use this skill for the AI-Filmmaking-Bible repository. The user's writing workflow is: ChatGPT researches and finalizes chapter drafts; Codex preserves originals, integrates, checks, formats, and manages versions.

## Workflow

1. Inspect repository status and list files under `chapters/`. Identify the intended chapter from explicit IDs, manuscript metadata, title, and `docs/TOC.md`. If chapter identity is ambiguous, report the candidates and process only unambiguous independent material.
2. Preserve every supplied original unchanged under `chapters/source-packs/` (or leave it in place if moving it would be confusing). Never overwrite the raw manuscript. For archives, inspect member names and reject path traversal before extraction.
3. Extract useful files into a canonical chapter Markdown file named `NN-NN-slug.md` and companion assets folder `NN-NN-slug-assets/`. Adapt front matter to `schemas/chapter.schema.json`; retain substantive manuscript sections and mark unresolved claims `待查證`.
4. Validate JSON and local paths. Link prompts and examples from the chapter. Do not claim that an example prompt was executed, that generated media exists, or that an asset is licensed unless the supplied evidence establishes it.
5. Verify time-sensitive or factual source claims against professional/primary sources. Record source IDs, exact URLs, editions/versions, access dates, and known limitations in `data/references.yaml`. Keep bibliographic leads separate from verified citations.
6. Register canonical bilingual terms in `data/terms.yaml`, prompt examples in `data/prompts.yaml`, and assets with provenance and rights status in `data/assets.yaml`. Use stable IDs and the project conventions.
7. Add or update schemas only when needed; keep chapter metadata and cross-chapter links consistent with the whole-book structure. Add figure placeholders or original diagrams where appropriate, with asset and rights metadata.
8. Run `python scripts/validate_project.py`, `python scripts/check_links.py`, relevant JSON/schema validation, and `python scripts/build.py --format html`. Review generated output and `git diff`; fix issues that can be resolved without inventing facts.
9. Summarize integrated files, preserved originals, verified vs pending claims, validation results, and remaining editorial work. Commit when the user asks or the established project workflow calls for versioning. Push only when explicitly requested.

## Trigger limitation

A skill is not a filesystem watcher and cannot start when files arrive while no Codex turn is active. When the user says they have dropped new material, inspect `chapters/` and run this workflow. True event-triggered processing requires a separate watcher or scheduled automation and must be configured separately.
