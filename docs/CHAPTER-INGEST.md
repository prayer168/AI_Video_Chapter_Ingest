# Chapter material intake workflow

Identify new source material under `chapters/` using explicit chapter IDs, title, and `docs/TOC.md`. Preserve original files unchanged in `chapters/source-packs/`. Check archive member paths before extraction. Create the canonical `NN-NN-slug.md` and companion folder `chapters/NN-NN-slug-assets/`. Update reference, term, prompt, and asset registries as needed.

Validate metadata against `schemas/chapter.schema.json`; validate structured shot examples against `schemas/shot.schema.json`. Verify claims against appropriate professional or primary sources, record dates and editions, and mark unsupported claims `待查證`. Never claim a prompt was executed or an included asset is licensed without evidence. Run project validation, link checks, JSON/schema checks, and HTML build. Review the diff before commit. Push only when explicitly requested.

A Codex skill does not monitor the filesystem by itself. This workflow starts when the user asks Codex to process new files; event-triggered processing needs a separate watcher or scheduled automation.
