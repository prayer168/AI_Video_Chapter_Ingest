# Project layout

- `chapters/` Markdown source chapters. Canonical manuscripts live at the root as `NN-NN-short-title.md`; chapter-specific media and JSON live beside them in `NN-NN-short-title-assets/`; immutable imported originals live in `chapters/source-packs/`. See `docs/CHAPTER-INGEST.md`.
- `docs/` editorial, quality, source, asset and publishing rules
- `templates/` editable authoring templates
- `data/` YAML terminology, reference, prompt and asset records
- `schemas/` reserved for formal schemas
- `assets/` images, audio, video and diagrams
- `scripts/` validation, publication and link/font checks
- `site/` website source and future theme
- `dist/` generated outputs; excluded from Git
