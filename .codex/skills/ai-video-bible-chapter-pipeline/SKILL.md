---
name: ai-video-bible-chapter-pipeline
description: Produce, integrate, verify, and prepare one AI Video Bible chapter from the existing project registry when the user asks to make a chapter, such as “製作第 3 章”. Preserve legacy and reviewed content; never spend on image generation, approve rights, publish, or push without explicit authorization.
metadata:
  short-description: AI Video Bible 章節研究、製作與出版流程
---

# AI Video Bible Chapter Pipeline

Use this skill for a request such as `製作第 3 章` or `製作 CH03`. The project root is the repository containing this skill. Read `CHAPTER-PIPELINE-README.md` and `AI-VIDEO-BIBLE-SOP-V4.md` at the root before acting; load the chapter template and prompt references as needed.

## Operating rules

- Check `git status`, the chapter registry, canonical zh-TW/en-US files, prior reports, references, terms, source packs, assets, and run history before making changes. Determine the chapter ID from `metadata/chapters.yaml`, not from a guessed filename.
- Preserve V1, V2, existing canonical text, raw sources, and media. Create a timestamped backup and a run record before editing. Integrate only the requested chapter; do not scaffold or rewrite all 60 chapters.
- Research with attributable professional/primary sources. Keep source IDs, stable URLs/DOIs, edition/version, access date, claim support, and limitations. Mark claims as verified fact, theory, practice, AI hypothesis, or demonstration. Never invent page numbers, film timecodes, citations, or tool capabilities.
- Draft Traditional Chinese first. Create or revise the English pair against the approved source text, but keep both languages `review-needed` until a human editor approves them. Preserve stable chapter, section, term, reference, and figure IDs.
- Film homage means analysis and original transformation of formal ideas. Do not reproduce identifiable shots, costumes, sets, actors, characters, logos, or official stills. Add film facts only with sources and mark similarity review pending.
- Do not fetch third-party images for publication. Use an original SVG/programmable diagram or an image-generation service only when that service is actually available and its terms, account authorization, and budget are confirmed. The repository adapter defaults to BLOCKED and its test double produces no image. Never call a paid API without explicit approval and an approved spend cap.
- Preserve figure originals, hash every asset, and record prompt/tool/model/version/date/source/edits, bilingual captions and alt text, rights/technical/editorial review, and publication status. Missing provenance or review stays `pending`; never mark a figure publication-ready by inference.
- Build locally only. Never deploy, publish, commit, or push unless the user explicitly asks for that specific action.

## Chapter run

1. Start a checkpoint with `python scripts/chapter_pipeline.py --chapter N`. Save its run directory in the working notes. This inspects progress and creates a run log/checklist; it does not generate content or touch manuscripts.
2. Follow the full SOP sections for research, bilingual drafting, homage analysis, assets, and QA. Record each completed or blocked stage with `--run-dir <path> --step <stage>=<status> --note "..."`.
3. Back up each existing target file before any edit. Never replace an approved or legacy file silently; use a diff and preserve the previous version.
4. Run project validators and chapter tests. Build both web locales and draft formats only if their dependencies and chapter-level gates permit. A whole-book formal build may correctly block while chapters remain unapproved; report that separately from a draft build.
5. Inspect actual HTML routes and assets, PDF embedded fonts and Traditional Chinese rendering, EPUBCheck, figure/caption/alt parity, IDs, links, source IDs, and hashes. A command exit code alone does not prove visual or editorial quality.
6. Create `reports/CHNN-FINAL-ACCEPTANCE.md` from the report template. List PASS, FAIL, BLOCKED, and NEEDS HUMAN REVIEW separately and cite concrete evidence.
7. Before finishing, complete the report template's **mandatory chapter completion audit**. Check every content requirement and every applicable production/publishing requirement individually; each row must have exactly one status and concrete evidence or a named human action. Do not infer a pass from a neighboring test.
8. Resolve all automated FAILs that are safe and authorized. Keep unresolved human decisions, missing authorization, and unrun checks explicitly open; do not call those items complete. If an automated requirement is blocked, state what input or environment change would unblock it.
9. Only after the audit is filled and the acceptance report is saved may this chapter's run be finished and reported. Do not start the next chapter in the same run; wait for the user to choose/ask for it after seeing the chapter report. A chapter may be reported as a completed draft package while remaining not publication-ready.
10. Finish the run log with `python scripts/chapter_pipeline.py --chapter N --run-dir <path> --finish <complete|partial|blocked>`. Only use `complete` if all authorized automated work is done; human-review or image-generation blockers may leave the run `partial`.
11. Append the request, decisions, changes, backups, versions, commands, test results, errors, audit outcome, and next actions to `history.md`.

## Quality gates

Use existing project tools where applicable: `scripts/v2_validate.py`, `scripts/validate_project.py`, `scripts/publishing/sync_site_content.py --check`, `scripts/validate/check_links.py`, `scripts/image_policy.py`, `scripts/publishing/check_epub.ps1`, `scripts/publishing/build_books.py`, and the test suite. Read current project documentation because formats and commands may evolve.

No chapter reaches `publication-ready` unless every blocking gate in `AI-VIDEO-BIBLE-SOP-V4.md` passes and the author and required professional editors have recorded approval. Research, writing, generated media, formatting, and publishing are distinct review states.
