# Repository editing rules

- Preserve V1 under `chapters/`; V2 canonical content lives under `content/`. Never overwrite/delete legacy manuscripts or source assets.
- Never use web-sourced images as formal illustrations. Missing figures become briefs, not downloaded substitutes.
- Do not fabricate citations, page numbers, history, research or tool features. Mark evidence type and verification status.
- English is an editorially reviewed translation, never auto-approved.
- Run `python scripts/v2_validate.py` and `python -m unittest discover -s tests` after V2 structural changes.
- Update `history.md` for every substantial integration/build: capture the request context, decisions, changed files, commands, test evidence, failures/limitations, and next steps. Treat it as a future teaching/demo/presentation/video production source; update before handing work back or compressing context.
- Build locally only; never publish or push unless explicitly requested.
