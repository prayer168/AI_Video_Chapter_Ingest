#!/usr/bin/env python3
"""Register CH01 homage references, terms, prompts, and ungenerated figure briefs."""
from __future__ import annotations

from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
STAMP = "2026-10-18"

REFERENCES = [
    ("R013", "institutional-film-record", "Citizen Kane (1941)", "British Film Institute", "https://www.bfi.org.uk/film/f4c92833-af39-5cd6-a41e-8df5933d0dc1/citizen-kane", "Film metadata; deep focus, camera angles, non-chronological narration, overlapping dialogue, and Gregg Toland collaboration."),
    ("R014", "institutional-film-analysis", "Where to Begin with Akira Kurosawa", "British Film Institute", "https://www.bfi.org.uk/features/where-begin-with-akira-kurosawa", "Rashomon section; differing testimonies and viewpoints. Article author/date and shot locator remain to be checked."),
    ("R015", "institutional-film-record", "A City of Sadness (1989)", "British Film Institute", "https://www.bfi.org.uk/film/989a6349-4d1c-54da-8ea1-0abd2a558d8a/a-city-of-sadness", "Film year, director, and historical setting."),
    ("R016", "film-criticism", "Flowers of Shanghai: Inside the Dream", "Criterion Collection", "https://www.criterion.com/current/posts/7395-flowers-of-shanghai-inside-the-dream", "Secondary analysis of a specific A City of Sadness restaurant scene, offscreen singing, window, and historical context."),
    ("R017", "film-criticism", "A City of Sadness", "The New Yorker", "https://www.newyorker.com/goings-on-about-town/movies/city-sadness", "Secondary discussion of long takes and doorway framing; exact viewed edition/timecode pending."),
    ("R018", "institutional-film-record", "In the Mood for Love (2000)", "Criterion Collection", "https://www.criterion.com/films/198-in-the-mood-for-love", "Film metadata; visual style, soundtrack, linked critical essays; scene locator pending."),
    ("R019", "film-criticism", "Yi Yi: Time and Space", "Kent Jones", "https://www.criterion.com/current/posts/429-yi-yi-time-and-space", "Secondary interpretation of foreground/background overlap, reflected cityscape, and urban space."),
]

TERMS = [
    ("DEEP-FOCUS", "深焦攝影", "Deep focus", "同一鏡頭中，前景與背景等不同距離的元素可同時保持可辨識的清晰度；效果受光學、光圈、照明、感光材料及觀看條件影響。", "A shot in which elements at different distances, including foreground and background, remain legibly sharp; results depend on optics, aperture, lighting, capture medium, and viewing conditions.", "film-form analysis", ["R013"]),
    ("MULTIPLE-PERSPECTIVE", "多重觀點敘事", "Multiple perspectives", "透過不同人物或資訊範圍呈現同一事件的不同觀點；觀點不同本身不能證明敘述者說謊。", "Different characters or information ranges present an event from distinct viewpoints; difference alone does not prove that a narrator is lying.", "narrative analysis", ["R014"]),
    ("OFFSCREEN-SPACE", "畫外空間", "Offscreen space", "畫框之外但可由聲音、視線、動作或剪輯關係被觀眾推知的空間。", "Space beyond the frame that viewers may infer through sound, eyelines, movement, or editing relations.", "film space", ["R016", "R017"]),
    ("LONG-TAKE", "長鏡頭", "Long take", "持續時間較長且內部未剪接的單一鏡頭；本詞沒有跨作品通用的秒數門檻。", "A single uncut shot of comparatively extended duration; there is no universal duration threshold across films.", "editing and cinematography", ["R017"]),
    ("FRAME-WITHIN-FRAME", "框中框構圖", "Frame within a frame", "利用門、窗或其他畫面內邊界形成次級框景，改變可見範圍、遮擋或空間層次。", "A doorway, window, or other in-frame boundary creates a secondary frame that changes visibility, occlusion, or spatial layering.", "composition", ["R017", "R019"]),
    ("LAYERED-COMPOSITION", "層次構圖", "Layered composition", "透過景深、前後景、反射或遮擋同時安排多組可見資訊；不等同固定鏡頭類型或必然心理效果。", "Depth, foreground/background, reflections, or occlusion arrange multiple visible information layers; this is neither a fixed shot type nor a guaranteed psychological effect.", "composition", ["R013", "R019"]),
]

FILMS = [
    ("001", "Citizen Kane", "《公民凱恩》", "deep focus", "虛構的當代教室，前景教師、中景學生、遠處門邊人物；多層景深均可辨識。不得用原片劇照、角色、場景或可識別構圖。", "A fictional contemporary classroom with a teacher in foreground, students in middle ground, and a distant figure; keep depth planes legible. Do not use film stills, characters, sets, or recognizable compositions.", "R013"),
    ("002", "Rashomon", "《羅生門》", "multiple perspectives", "虛構教室器材意外的三視角分格；人物、道具及事件事實一致，只改變觀察位置與可見資訊。不得重現原片場景、人物或鏡頭。", "A triptych of a fictional classroom equipment accident. Keep characters, props, and event facts consistent; vary camera position and visible information only. Do not reproduce the film’s setting, characters, or shots.", "R014"),
    ("003", "A City of Sadness", "《悲情城市》", "offscreen space", "原創當代家庭餐廳，以門窗、固定視點和畫外聲音表現延伸空間。不得仿造片中年代服裝、人物或特定場景。", "An original contemporary family dining room. Use doors, windows, a fixed viewpoint, and offscreen sound to suggest extended space. Do not imitate period costumes, characters, or specific scenes.", "R015"),
    ("004", "In the Mood for Love", "《花樣年華》", "framing and repeated rhythm", "原創現代圖書館走道，虛構人物以三個節點呈現重複動作與框中框；避免原片走廊、服裝、人物、色彩組合及可辨識構圖。", "An original modern library corridor with fictional characters at three beats of a repeated action within nested framing. Avoid the film’s corridors, costumes, characters, color combinations, and recognizable compositions.", "R018"),
    ("005", "Yi Yi", "《一一》", "layered composition and reflection", "原創當代校園玻璃走廊，呈現畫內人物與窗外活動，反射幾何合理；不得重現電影人物、場景或攝影構圖。", "An original contemporary school corridor with reflective glass, showing people inside and activity beyond the window with plausible reflection geometry. Do not reproduce film characters, settings, or cinematography.", "R019"),
]


def load_list(path: Path) -> list[dict]:
    rows = yaml.safe_load(path.read_text(encoding="utf-8-sig")) or []
    if not isinstance(rows, list):
        raise ValueError(f"Expected YAML list: {path.relative_to(ROOT)}")
    return rows


def append_list(path: Path, entries: list[dict]) -> int:
    rows = load_list(path)
    by_id = {row.get("id"): row for row in rows if isinstance(row, dict)}
    fresh = []
    for row in entries:
        if row["id"] in by_id:
            if by_id[row["id"]] != row:
                raise ValueError(f"Conflicting ID {row['id']} in {path.relative_to(ROOT)}")
            continue
        fresh.append(row)
    if fresh:
        with path.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write("\n\n" + yaml.safe_dump(fresh, allow_unicode=True, sort_keys=False, width=120))
    return len(fresh)


def main() -> int:
    ref_rows = []
    for rid, kind, title, org, url, notes in REFERENCES:
        ref_rows.append({"id": rid, "type": kind, "title": title, "authors": [org], "publisher": org, "edition": None,
                         "publication_date": "2011-03-15" if rid == "R019" else None, "version": f"Web page accessed {STAMP}",
                         "doi": None, "url": url, "accessed": STAMP, "locator": None, "language": "en",
                         "status": "verified-current-page" if rid in {"R013", "R014", "R015", "R018"} else "reviewed-secondary", "notes": notes})
    references_added = append_list(ROOT / "data/references.yaml", ref_rows)

    legacy_terms, canonical_terms = [], []
    for code, zh, en, zhdef, endef, domain, refs in TERMS:
        tid = f"TERM-CH01-{code}"
        legacy_terms.append({"id": tid, "zh_TW": zh, "en": en, "variants": [], "definition": zhdef, "domain": domain,
                             "status": "draft", "source_ids": refs, "related_terms": [],
                             "notes": "CH01 V2 homage integration; bilingual definition and source locator need editorial review.", "updated": STAMP})
        canonical_terms.append({"term_id": tid, "preferred": {"zh-TW": zh, "en-US": en}, "definitions": {"zh-TW": zhdef, "en-US": endef},
                                "domain": domain, "context": "CH01 film-homage case studies; draft definition, not approved.",
                                "synonyms": {"zh-TW": [], "en-US": []}, "see_also": [], "references": refs,
                                "status": "draft", "reviewed_by": None, "reviewed_on": None})
    terms_added = append_list(ROOT / "data/terms.yaml", legacy_terms)
    canonical_path = ROOT / "metadata/terminology.yaml"
    canonical = yaml.safe_load(canonical_path.read_text(encoding="utf-8-sig")) or {"terms": []}
    canonical.setdefault("terms", [])
    ids = {row.get("term_id") for row in canonical["terms"]}
    for row in canonical_terms:
        if row["term_id"] not in ids:
            canonical["terms"].append(row)
    canonical_path.write_text(yaml.safe_dump(canonical, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")

    bib_path = ROOT / "metadata/references.bib"
    bib_entries = {
        "R013": "@misc{R013, author = {{British Film Institute}}, title = {Citizen Kane (1941)}, howpublished = {BFI film record}, url = {https://www.bfi.org.uk/film/f4c92833-af39-5cd6-a41e-8df5933d0dc1/citizen-kane}, note = {Accessed 2026-10-18}}",
        "R014": "@misc{R014, author = {{British Film Institute}}, title = {Where to Begin with Akira Kurosawa}, howpublished = {BFI feature}, url = {https://www.bfi.org.uk/features/where-begin-with-akira-kurosawa}, note = {Accessed 2026-10-18}}",
        "R015": "@misc{R015, author = {{British Film Institute}}, title = {A City of Sadness (1989)}, howpublished = {BFI film record}, url = {https://www.bfi.org.uk/film/989a6349-4d1c-54da-8ea1-0abd2a558d8a/a-city-of-sadness}, note = {Accessed 2026-10-18}}",
        "R016": "@misc{R016, author = {{Criterion Collection}}, title = {Flowers of Shanghai: Inside the Dream}, howpublished = {Criterion Current}, url = {https://www.criterion.com/current/posts/7395-flowers-of-shanghai-inside-the-dream}, note = {Accessed 2026-10-18; secondary film analysis}}",
        "R017": "@misc{R017, author = {{The New Yorker}}, title = {A City of Sadness}, howpublished = {Goings On About Town}, url = {https://www.newyorker.com/goings-on-about-town/movies/city-sadness}, note = {Accessed 2026-10-18; secondary film analysis}}",
        "R018": "@misc{R018, author = {{Criterion Collection}}, title = {In the Mood for Love (2000)}, howpublished = {Criterion film record}, url = {https://www.criterion.com/films/198-in-the-mood-for-love}, note = {Accessed 2026-10-18}}",
        "R019": "@article{R019, author = {Kent Jones}, title = {Yi Yi: Time and Space}, journal = {Criterion Current}, date = {2011-03-15}, url = {https://www.criterion.com/current/posts/429-yi-yi-time-and-space}, note = {Accessed 2026-10-18; secondary film analysis}}",
    }
    bib = bib_path.read_text(encoding="utf-8-sig")
    for key, entry in bib_entries.items():
        if not __import__("re").search(r"@\w+\s*\{\s*" + key + r"\s*,", bib):
            bib += "\n\n" + entry
    bib_path.write_text(bib.rstrip() + "\n", encoding="utf-8")

    figures = []
    prompts = []
    for num, film, zhfilm, concept, zhprompt, enprompt, ref in FILMS:
        fid = f"CH01-HOMAGE-FIG-{num}"
        prompt_path = f"assets/chapters/CH01/homage/briefs/{fid}.md"
        section_num = int(num)
        captions = {"zh-TW": f"規劃中的原創教學圖以新人物及場景說明「{concept}」；尚未生成，非《{zhfilm[1:-1]}》劇照。",
                    "en-US": f"Planned original teaching illustration using new characters and a new setting to explain {concept}; not generated and not a still from *{film}*."}
        alt = {"zh-TW": f"規劃以原創人物與場景呈現「{concept}」的教學示意圖；圖片尚未生成。",
               "en-US": f"Planned instructional illustration of {concept} using original characters and a new setting; image not generated."}
        figures.append({"figure_id": fid, "chapter_id": "CH01", "section_id": "CH01-S09", "placement_after": f"CH01-P{section_num:03d}",
                        "kind": "original-ai-teaching-illustration", "teaching_goal": concept, "asset_original": None, "asset_approved": None,
                        "overlay_zh": None, "overlay_en": None, "captions": captions, "alt": alt,
                        "generation": {"tool": None, "version": None, "date": None, "prompt_file": prompt_path},
                        "rights_review": "pending", "technical_review": "pending", "editorial_review": "pending"})
        prompts.append({"id": f"PROMPT-{fid}", "chapter_id": "CH01", "path": prompt_path,
                        "purpose": f"Bilingual original illustration brief for {film} technique example", "modality": "image-generation",
                        "tool": None, "model_version": None, "status": "draft-not-run", "input_assets": [],
                        "parameters": {"output": "text-free image; bilingual labels on editable overlay only",
                                       "rights_constraint": "new characters and setting; do not reproduce film stills, characters, costumes, posters, or recognizable compositions"},
                        "source_ids": [ref], "verification": "Brief only; no image generation or output inspection has been performed.", "updated": STAMP})

    manifest_path = ROOT / "assets/chapters/CH01/figure-manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8-sig")) or {"chapter_id": "CH01", "figures": []}
    known = {row.get("figure_id") for row in manifest.get("figures", [])}
    manifest["figures"].extend(row for row in figures if row["figure_id"] not in known)
    manifest_path.write_text(yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")

    registry_path = ROOT / "metadata/figure-registry.yaml"
    registry = yaml.safe_load(registry_path.read_text(encoding="utf-8-sig")) or {"schema_version": 1, "figures": []}
    known = {row.get("figure_id") for row in registry.get("figures", [])}
    for figure, (_, _, _, _, _, _, ref) in zip(figures, FILMS):
        if figure["figure_id"] not in known:
            registry["figures"].append({"figure_id": figure["figure_id"], "chapter_id": "CH01", "section_id": "CH01-S09",
                                         "placement_after": figure["placement_after"], "source_film_ref": f"FILM-{figure['figure_id'][-3:]}",
                                         "source_ids": [ref], "brief_file": figure["generation"]["prompt_file"],
                                         "asset_original": None, "asset_approved": None, "rights_review": "pending",
                                         "technical_review": "pending", "editorial_review": "pending", "publication_status": "not-generated"})
    registry_path.write_text(yaml.safe_dump(registry, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
    prompts_added = append_list(ROOT / "data/prompts.yaml", prompts)

    print(f"References added: {references_added}; terms added: {terms_added}; prompts added: {prompts_added}; planned figures: {len(figures)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
