from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAMP = date.today().isoformat()
LEGACY = ROOT / "legacy" / "2026-v1"


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def safe_copy(src: Path, dst: Path) -> None:
    if dst.exists():
        if src.is_file() and digest(src) == digest(dst):
            return
        raise FileExistsError(f"Refusing to overwrite legacy backup: {dst}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)


def parse_toc() -> tuple[list[dict], list[dict]]:
    text = (ROOT / "docs" / "TOC.md").read_text(encoding="utf-8")
    parts, chapters = [], []
    part_no = 0
    for line in text.splitlines():
        match = re.match(r"^## 第([一二三四五六七八九十]+)篇｜(.+)$", line.strip())
        if match:
            part_no += 1
            parts.append({"part_id": f"P{part_no:02d}", "part_number": part_no, "title_zh": match.group(2).strip()})
        match = re.match(r"^\s*(\d+)\.\s+(.+?)(?:\s+[（(]([^)）]+)[)）])?\s*$", line)
        if match:
            number, title, status = int(match.group(1)), match.group(2).strip(), match.group(3) or "planned"
            slug = {1: "cinematic-language", 2: "camera-language"}.get(number) or f"chapter-{number:02d}"
            chapters.append({"chapter_id": f"CH{number:02d}", "part_id": f"P{(number-1)//5+1:02d}", "number": number, "title_zh": title, "slug": slug, "legacy_status": status})
    if len(chapters) != 60 or len(parts) != 12:
        raise ValueError(f"TOC parse expected 12 parts and 60 chapters; got {len(parts)} and {len(chapters)}")
    return parts, chapters


def put(path: str, content: str) -> None:
    target = ROOT / path
    if target.exists():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    # Preserve all current V1 materials, including user-provided, untracked files.
    targets = [ROOT / "chapters" / "01-01-cinematic-language.md", ROOT / "chapters" / "01-01-cinematic-language-assets",
               ROOT / "chapters" / "01-02-camera-language.md", ROOT / "chapters" / "01-02-camera-language-assets",
               ROOT / "chapters" / "source-packs"]
    for src in targets:
        if src.exists():
            safe_copy(src, LEGACY / "chapters" / src.relative_to(ROOT / "chapters"))
    manifest_path = LEGACY / "migration-manifest.csv"
    if not manifest_path.exists():
        rows = []
        for src in targets:
            if src.is_file():
                pairs = [(src, LEGACY / "chapters" / src.relative_to(ROOT / "chapters"))]
            elif src.is_dir():
                pairs = [(item, LEGACY / "chapters" / item.relative_to(ROOT / "chapters")) for item in src.rglob("*") if item.is_file()]
            else:
                continue
            for original, backup in pairs:
                rows.append({"source": original.relative_to(ROOT).as_posix(), "legacy_copy": backup.relative_to(ROOT).as_posix(), "sha256_source": digest(original), "sha256_backup": digest(backup), "status": "verified" if digest(original) == digest(backup) else "mismatch"})
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        with manifest_path.open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=["source", "legacy_copy", "sha256_source", "sha256_backup", "status"])
            writer.writeheader(); writer.writerows(rows)

    parts, chapters = parse_toc()
    for lang in ("zh-TW", "en-US"):
        (ROOT / "content" / lang / "chapters").mkdir(parents=True, exist_ok=True)
        (ROOT / "content" / lang / "frontmatter").mkdir(parents=True, exist_ok=True)
        (ROOT / "content" / lang / "backmatter").mkdir(parents=True, exist_ok=True)
        for ch in chapters:
            path = ROOT / "content" / lang / "chapters" / f"{ch['chapter_id']}-{ch['slug']}.md"
            if path.exists():
                continue
            title = ch["title_zh"] if lang == "zh-TW" else f"Chapter {ch['number']:02d}: English title pending editorial translation"
            status = "draft-migration-pending" if lang == "zh-TW" and ch["number"] <= 2 else ("translation-needed" if lang == "en-US" else "planned")
            template = f'''---
chapter_id: {ch['chapter_id']}
part_id: {ch['part_id']}
locale: {lang}
slug: {ch['slug']}
title: "{title}"
translation_status: {status}
revision: 2.0.0
source_chapter: {f"legacy/2026-v1/chapters/{'01-01-cinematic-language.md' if ch['number']==1 else '01-02-camera-language.md'}" if ch['number'] <= 2 and lang == 'zh-TW' else 'null'}
---

<!-- V2 working copy. V1 source remains immutable under legacy/2026-v1. -->

# {title}

> Editorial state: {status}. This scaffold is not a completed chapter.

## Learning objectives {{#{ch['chapter_id']}-S01}}
<!-- Add observable outcomes and prerequisites. -->

## Prerequisites {{#{ch['chapter_id']}-S02}}

## Key terms {{#{ch['chapter_id']}-S03}}
<!-- Link term IDs from metadata/terminology.yaml. -->

## History and principles {{#{ch['chapter_id']}-S04}}

## Traditional production practice {{#{ch['chapter_id']}-S05}}

## AI-era workflow and limits {{#{ch['chapter_id']}-S06}}

## Step-by-step workflow {{#{ch['chapter_id']}-S07}}

## Prompt and technical parameters {{#{ch['chapter_id']}-S08}}

## Shot / film case study {{#{ch['chapter_id']}-S09}}

## Common errors and quality checks {{#{ch['chapter_id']}-S10}}

## Exercises, assessment, and research {{#{ch['chapter_id']}-S11}}

## References {{#{ch['chapter_id']}-S12}}
<!-- Use stable reference IDs and the citation policy; never invent metadata. -->
'''
            path.write_text(template, encoding="utf-8")

    put("metadata/parts.yaml", "# V2 part registry\n" + "\n".join(f"- part_id: {p['part_id']}\n  number: {p['part_number']}\n  title_zh: {json.dumps(p['title_zh'], ensure_ascii=False)}\n  title_en: \"\" # editorial translation pending" for p in parts))
    put("metadata/chapters.yaml", "# Stable chapter registry; IDs persist across locales and URL changes.\n" + "\n".join(f"- chapter_id: {c['chapter_id']}\n  part_id: {c['part_id']}\n  number: {c['number']}\n  slug: {c['slug']}\n  title_zh: {json.dumps(c['title_zh'], ensure_ascii=False)}\n  title_en: \"\" # editorial translation pending\n  legacy_status: {c['legacy_status']}\n  zh_status: {'draft-migration-pending' if c['number'] <= 2 else 'planned'}\n  en_status: translation-needed" for c in chapters))
    put("metadata/translation-status.yaml", "schema_version: 1\npolicy: Human-reviewed translation; machine translation may assist but cannot be approved automatically.\nstatuses: [source-draft, review-needed, approved, out-of-sync, translation-needed]\nchapters:\n" + "".join(f"  {c['chapter_id']}:\n    zh-TW: {'draft-migration-pending' if c['number'] <= 2 else 'planned'}\n    en-US: translation-needed\n    sync_revision: null\n" for c in chapters))
    put("metadata/terminology.yaml", "schema_version: 1\nterms: []\n# See docs/TERMINOLOGY-V2.md for the data contract and validation rules.\n")
    put("metadata/references.bib", "% Bibliography registry. Add only sources whose metadata has been verified.\n")
    put("metadata/figure-registry.yaml", "schema_version: 1\nfigures: []\n# Formal-use gate: rights_review, technical_review, editorial_review must all be approved.\n")
    put("metadata/migration-manifest.csv", "source,legacy_copy,sha256_source,sha256_backup,status\n")
    for ch in chapters:
        base = ROOT / "assets" / "chapters" / ch["chapter_id"]
        for sub in ("figures/originals", "figures/approved", "figures/overlays", "figures/exports", "storyboards", "reference-images"):
            (base / sub).mkdir(parents=True, exist_ok=True)
        put(f"assets/chapters/{ch['chapter_id']}/figure-manifest.yaml", f"chapter_id: {ch['chapter_id']}\nfigures: []\n")
    for folder in ("assets/shared", "production/shot-lists", "production/prompts", "production/agent-instructions", "production/rubrics", "design/book", "design/web", "scripts/validate", "scripts/figures", "scripts/publishing", "reports", "release-packs", "apps/web/src/content/docs/zh-tw", "apps/web/src/content/docs/en", "apps/web/src/styles", "apps/web/public/images", "tests"):
        (ROOT / folder).mkdir(parents=True, exist_ok=True)

    put("templates/chapter-v2.md", '''---\nchapter_id: CHXX\npart_id: PXX\nlocale: zh-TW\nslug: stable-ascii-slug\ntitle: "章名"\ntranslation_status: source-draft\nrevision: 2.0.0\n---\n\n# 章名\n\n## 學習目標 {#CHXX-S01}\n## 先備知識 {#CHXX-S02}\n## 核心術語 {#CHXX-S03}\n## 歷史與基本原理 {#CHXX-S04}\n## 傳統製作方法 {#CHXX-S05}\n## AI 時代的技術轉換 {#CHXX-S06}\n## 詳細工作流程 {#CHXX-S07}\n## 提示詞與技術參數 {#CHXX-S08}\n## 鏡頭／影片案例 {#CHXX-S09}\n## 常見錯誤與品質驗證 {#CHXX-S10}\n## 練習、評量與延伸研究 {#CHXX-S11}\n## 參考文獻 {#CHXX-S12}\n''')
    put("templates/figure-manifest-entry.yaml", '''figure_id: CHXX-FIG-001\nchapter_id: CHXX\nsection_id: CHXX-S01\nplacement_after: CHXX-P001\nkind: cinematic-still # cinematic-still | technical-vector | workflow\nteaching_goal: ""\nasset_original: assets/chapters/CHXX/figures/originals/CHXX-FIG-001.png\nasset_approved: null\noverlay_zh: null\noverlay_en: null\ncaptions: {zh-TW: "", en-US: ""}\nalt: {zh-TW: "", en-US: ""}\ngeneration: {tool: "", version: null, date: null, prompt_file: null}\nrights_review: pending\ntechnical_review: pending\neditorial_review: pending\n''')
    put("templates/translation-pair.md", '''# Translation pair contract\n\n- Preserve `chapter_id`, section anchor IDs, paragraph IDs, figure IDs and reference IDs across locales.\n- English text is an editorial translation; machine output must remain `review-needed`.\n- Record source revision, translator/editor, review date, terminology decisions and unresolved queries in translation metadata.\n- Mark a translation `out-of-sync` whenever its source revision changes after approval.\n''')
    put("docs/IMAGE-RIGHTS-V2.md", '''# V2 圖片原創、來源與權利規範\n\n正式出版圖片必須為本專案原創，或有文件化授權。網路搜尋圖片僅供研究參考，禁止直接下載或嵌入正式出版物。不得描摹或高度仿作第三方作品。\n\n每個永久 `figure_id` 必須記錄教學目的、段落位置、研究來源與查證日期、原創 prompt／繪圖方法、生成工具與版本、製作修改紀錄、權利／技術／編輯審查、繁中與英文圖說及 alt。AI 生成不代表已取得排他著作權；肖像、商標、受保護作品另行審查。\n\n原圖放 `originals/`，核准底圖放 `approved/`，文字標註保存在可編輯 `overlays/*.svg`，輸出版放 `exports/`。原始生成圖避免烘焙大量文字，雙語標籤應可編輯。缺圖只建立 figure brief／待辦，不以網圖填補。正式發佈需三項審查全數 approved；未核准圖不得輸出。\n''')
    put("docs/TRANSLATION-V2.md", '''# 中英翻譯管理\n\n`content/zh-TW` 為創作主稿；`content/en-US` 為人工審校譯稿。兩語共用永久章節、段落、術語、引用及圖號 ID。章名、slug 可各語系呈現，但 ID 不變。\n\n狀態：`source-draft`、`review-needed`、`approved`、`out-of-sync`、`translation-needed`。源稿變更時使已核准譯文失效並標記 out-of-sync。逐節核對技術術語、引文頁碼、單位和提示詞參數；記錄譯者、編輯、來源 revision、審查日期及疑義。不得以即時機器翻譯當成正式英文稿。網站缺譯顯示明確缺譯標記，不回退顯示錯語言內容。\n''')
    put("docs/CITATION-V2.md", '''# 引用與證據規範\n\n優先使用電影理論／史料的學術出版社、期刊、檔案館及原始文獻；AI 工具功能優先官方文件、版本紀錄及可重現實測。每筆來源使用永久 `R###`，記錄作者／機構、年份、標題、出版資訊、DOI／穩定 URL、存取日、版本、支持的主張與查證狀態。引用頁碼僅在核對原件後填寫。\n\n主張標籤：`verified-fact`（可追溯事實）、`theory`（標明理論脈絡）、`practice`（實務建議）、`ai-hypothesis`（待驗證 AI 推論）、`demo`（示範內容）。不可捏造引文、史料、論文、頁碼、URL 或工具能力。時效資訊記錄查證日期及文件／產品版本；失效連結保留記錄並更新替代來源。\n''')
    put("docs/QUALITY-GATES-V2.md", '''# V2 品質審查規則\n\n## 阻擋條件\n- 章節 ID、locale、永久錨點重複或缺漏；zh/en 配對不一致。\n- 參考 ID 未登錄、必要來源欄位缺漏、外部連結失效（網路檢查可選，離線標示未檢）。\n- 正式輸出含無核准圖片、外部圖片 URL、缺雙語 alt/caption、未記錄權利／版本。\n- PDF 字型未嵌入或繁中文字形渲染未人工抽查；未經人工校樣不得宣稱出版就緒。\n- 英文稿非人工審校卻標記 approved；源稿變更後仍維持譯文 approved。\n\n## 審查分類\n1. 結構：metadata、錨點、交叉引用、雙語狀態。\n2. 證據：來源可追溯、主張類型清楚、版本及日期充分。\n3. 專業：電影概念、技術參數、工作流程由專業審查者複核。\n4. 圖像：權利、技術、編輯核准；向量圖可編輯且術語正確。\n5. 出版：HTML/DOCX/PDF/EPUB 產物檢查、字型嵌入、溢版、孤行寡行及連結。\n\n任何未實測功能、待查主張、生成假設均須明確標示，不能以 CI 通過取代編輯與專業審讀。\n''')
    put("design/design-system.md", '''# Cinematic Editorial 設計系統\n\n採電影式節奏與圖文敘事：寬幅影像、留白、克制的字級層次、編輯式欄寬、全幅章節開場和圖說／旁註，不用滿版硬式矩形卡片。圖片可透明背景並與文字排版交疊；技術概念以可編輯 SVG 或程式化向量圖表呈現。\n\n保留鍵盤操作、足夠對比、縮放與行動裝置閱讀。每張圖有雙語 alt/caption。避免以裝飾犧牲可讀性。印刷色彩與出血需依實際印刷廠規格另定。\n''')
    put("docs/PUBLISHING-V2.md", '''# V2 出版工具鏈\n\n內容源：雙語 Markdown + YAML/BibTeX；校驗由 Python 腳本執行。Web 候選 Astro + Starlight，採自訂 editorial theme，正式採用前需以 CH01 雙語樣章做可行性驗收。書籍以 Pandoc 轉 DOCX/EPUB，以 XeLaTeX 輸出 PDF；HTML 網站與書籍共用章節源稿。\n\n本階段建立可重現設定與 smoke tests，不宣稱已完成版面／字型驗收。正式 PDF 要檢查字型嵌入及繁中文字形、圖說跨頁、解析度與印刷校樣；工具缺席時清楚報告 skipped。預設輸出 `dist/`，不自動發布。\n''')
    put("AGENTS.md", '''# Repository editing rules\n\n- Preserve V1 under `chapters/`; V2 canonical content lives under `content/`. Never overwrite/delete legacy manuscripts or source assets.\n- Never use web-sourced images as formal illustrations. Missing figures become briefs, not downloaded substitutes.\n- Do not fabricate citations, page numbers, history, research or tool features. Mark evidence type and verification status.\n- English is an editorially reviewed translation, never auto-approved.\n- Run `python scripts/v2_validate.py` and `python -m unittest discover -s tests` after V2 structural changes.\n- Build locally only; never publish or push unless explicitly requested.\n''')
    put("CHANGELOG.md", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8") + "\n## V2.0 architecture bootstrap — " + STAMP + "\n- Added bilingual content model and scaffold; legacy chapter sources copied with SHA-256 migration manifest.\n- Added translation, rights, citation, design and quality contracts plus local web/book build skeleton.\n")

    # Create a web starter without remote images or automatic deploy configuration.
    put("apps/web/package.json", json.dumps({"name": "ai-video-bible-web", "private": True, "type": "module", "scripts": {"dev": "astro dev", "build": "astro build", "check": "astro check"}, "dependencies": {"@astrojs/starlight": "^0.37.0", "astro": "^5.14.0"}, "devDependencies": {"typescript": "^5.9.0"}}, ensure_ascii=False, indent=2))
    put("apps/web/astro.config.mjs", '''import { defineConfig } from 'astro/config';\nimport starlight from '@astrojs/starlight';\n\nexport default defineConfig({\n  site: 'https://example.invalid',\n  base: '/',\n  integrations: [starlight({\n    title: 'AI Video Bible',\n    defaultLocale: 'root',\n    locales: { root: { label: '繁體中文', lang: 'zh-TW' }, en: { label: 'English', lang: 'en-US' } },\n    sidebar: [{ label: '樣章', translations: { en: 'Sample' }, items: [{ label: 'CH01 — Cinematic Language', link: '/zh-tw/ch01/' }] }],\n    customCss: ['./src/styles/editorial.css'],\n  })],\n});\n''')
    put("apps/web/src/styles/editorial.css", ''':root { --sl-content-width: 58rem; --sl-sidebar-width: 17rem; --sl-color-accent-low: #e8ded0; --sl-color-accent: #8b4b32; --sl-color-accent-high: #4f261a; }\n.sl-markdown-content { line-height: 1.82; }\n.sl-markdown-content h1 { font-family: Georgia, 'Noto Serif TC', serif; letter-spacing: .015em; }\n.sl-markdown-content img { background: transparent; border-radius: 0; box-shadow: none; }\n.sl-markdown-content figure { margin-inline: 0; }\n.sl-markdown-content figcaption { color: var(--sl-color-gray-3); font-size: .88rem; max-width: 48rem; }\n/* Editorial rhythm: avoid card grids and hard boxed callouts as the default layout. */\n''')
    put("apps/web/src/content/docs/zh-tw/index.mdx", "---\ntitle: AI 電影製作聖經\ndescription: 電影語言、製作實務與 AI 工作流程的雙語知識庫\n---\n\n# AI 電影製作聖經\n\nV2.0 雙語出版架構樣站。內容仍在編輯中，未核准的章節和插圖不代表正式出版。\n")
    put("apps/web/src/content/docs/en/index.mdx", "---\ntitle: AI Video Bible\ndescription: A bilingual knowledge base for film language, production practice, and AI workflows\n---\n\n# AI Video Bible\n\nV2.0 bilingual publishing scaffold. Content remains under editorial development.\n")
    put("apps/web/src/content/docs/zh-tw/ch01.mdx", "---\ntitle: CH01｜電影視聽語言\ndescription: 雙語圖文樣章待編輯\n---\n\n# CH01｜電影視聽語言\n\n本頁是網站樣章占位稿；完成雙語編修及圖片審核前，不是正式章節。\n")
    put("apps/web/src/content/docs/en/ch01.mdx", "---\ntitle: CH01 | Cinematic Language\ndescription: Bilingual editorial sample pending\n---\n\n# CH01 | Cinematic Language\n\nThis is a site sample placeholder, not a completed translation or chapter.\n")
    put("apps/web/README.md", "# V2 website starter\n\nAstro + Starlight candidate with a custom Cinematic Editorial stylesheet. Local preview/build only; no deployment workflow is configured. Replace placeholder docs from reviewed bilingual Markdown before publication.\n")
    put("package.json", json.dumps({"name": "ai-video-bible-v2", "private": True, "scripts": {"web:install": "npm --prefix apps/web install", "web:dev": "npm --prefix apps/web run dev", "web:build": "npm --prefix apps/web run build", "validate:v2": "python scripts/v2_validate.py"}}, ensure_ascii=False, indent=2))
    put("requirements-v2.txt", "PyYAML>=6.0,<7\nMarkdown>=3.5,<4\n")

    put("scripts/v2_validate.py", '''from __future__ import annotations\nimport re, sys\nfrom pathlib import Path\ntry:\n    import yaml\nexcept ImportError:\n    yaml = None\nROOT = Path(__file__).resolve().parents[1]\nerrors, warnings = [], []\n\ndef check_registry():\n    chapters_file = ROOT / 'metadata/chapters.yaml'\n    text = chapters_file.read_text(encoding='utf-8')\n    ids = re.findall(r'^- chapter_id: (CH\\d{2})$', text, re.M)\n    if len(ids) != 60 or len(set(ids)) != 60: errors.append(f'chapter registry expected 60 unique IDs, got {len(ids)}')\n    for locale in ('zh-TW', 'en-US'):\n        files = list((ROOT / 'content' / locale / 'chapters').glob('CH*.md'))\n        if len(files) != 60: errors.append(f'{locale}: expected 60 scaffolds, got {len(files)}')\n        for path in files:\n            body = path.read_text(encoding='utf-8')\n            if not body.startswith('---\\n') or 'chapter_id:' not in body or 'locale:' not in body: errors.append(f'missing frontmatter: {path.relative_to(ROOT)}')\n            if locale == 'en-US' and 'translation_status: approved' in body: errors.append(f'unreviewed English scaffold marked approved: {path.name}')\ndef check_manifest():\n    path = ROOT/'legacy/2026-v1/migration-manifest.csv'\n    if not path.exists(): errors.append('migration manifest missing'); return\n    import csv\n    with path.open(encoding='utf-8-sig', newline='') as f: rows=list(csv.DictReader(f))\n    if not rows: errors.append('migration manifest has no file entries')\n    for row in rows:\n        if row['status'] != 'verified' or row['sha256_source'] != row['sha256_backup']: errors.append(f"migration checksum mismatch: {row['source']}")\ndef check_figures():\n    for path in (ROOT/'assets/chapters').glob('CH*/figure-manifest.yaml'):\n        text=path.read_text(encoding='utf-8')\n        if 'figures: []' not in text and yaml:\n            data=yaml.safe_load(text) or {}\n            for fig in data.get('figures', []):\n                if any(fig.get(k) != 'approved' for k in ('rights_review','technical_review','editorial_review')):\n                    errors.append(f'non-approved figure in formal manifest: {path}')\ndef check_links():\n    for path in list((ROOT/'apps/web/src/content/docs').rglob('*.mdx')):\n        text=path.read_text(encoding='utf-8')\n        for url in re.findall(r'!\\[[^]]*\\]\\((https?://[^)]+)\\)', text): errors.append(f'external image prohibited: {url} ({path.name})')\n\nif __name__ == '__main__':\n    check_registry(); check_manifest(); check_figures(); check_links()\n    if errors:\n        print('V2 validation FAILED')\n        for error in errors: print(f'ERROR: {error}')\n        sys.exit(1)\n    print('V2 validation PASS: 12-part/60-chapter registries, bilingual scaffolds, legacy checksums, and image policy gates.')\n    print('NOTE: editorial review, external reference checks, visual layout, PDF font embedding, and web build are separate gates.')\n''')
    put("tests/test_v2_architecture.py", '''import csv, hashlib, subprocess, sys, unittest\nfrom pathlib import Path\nROOT=Path(__file__).resolve().parents[1]\nclass ArchitectureTests(unittest.TestCase):\n    def test_v2_validator(self):\n        result=subprocess.run([sys.executable, str(ROOT/'scripts/v2_validate.py')], cwd=ROOT, capture_output=True, text=True)\n        self.assertEqual(result.returncode, 0, result.stdout+result.stderr)\n    def test_registry_has_60_ids(self):\n        import re\n        ids=re.findall(r'^- chapter_id: (CH\\d{2})$', (ROOT/'metadata/chapters.yaml').read_text(encoding='utf-8'), re.M)\n        self.assertEqual(len(ids), 60); self.assertEqual(len(set(ids)), 60)\n    def test_language_pairs_have_stable_ids(self):\n        for i in range(1,61):\n            zh=list((ROOT/'content/zh-TW/chapters').glob(f'CH{i:02d}-*.md'))\n            en=list((ROOT/'content/en-US/chapters').glob(f'CH{i:02d}-*.md'))\n            self.assertEqual(len(zh),1); self.assertEqual(len(en),1)\n            self.assertIn(f'chapter_id: CH{i:02d}', zh[0].read_text(encoding='utf-8'))\n            self.assertIn(f'chapter_id: CH{i:02d}', en[0].read_text(encoding='utf-8'))\n    def test_legacy_manifest_hashes(self):\n        path=ROOT/'legacy/2026-v1/migration-manifest.csv'\n        with path.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))\n        self.assertTrue(rows)\n        for row in rows:\n            self.assertEqual(row['status'],'verified',row['source'])\n            self.assertEqual(row['sha256_source'],row['sha256_backup'],row['source'])\n    def test_no_auto_deploy_workflow(self):\n        workflows=ROOT/'.github/workflows'\n        for path in workflows.glob('*.yml') if workflows.exists() else []:\n            text=path.read_text(encoding='utf-8').lower()\n            self.assertNotIn('deploy-pages',text); self.assertNotIn('gh-pages',text)\nif __name__=='__main__': unittest.main()\n''')
    put(".github/workflows/v2-validate.yml", '''name: V2 architecture validation\non:\n  push:\n    paths: ['content/**', 'metadata/**', 'assets/chapters/**', 'scripts/v2_validate.py', 'tests/test_v2_architecture.py']\n  pull_request:\n    paths: ['content/**', 'metadata/**', 'assets/chapters/**', 'scripts/v2_validate.py', 'tests/test_v2_architecture.py']\njobs:\n  validate:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-python@v5\n        with: {python-version: '3.11'}\n      - run: python scripts/v2_validate.py\n      - run: python -m unittest discover -s tests -p 'test_v2_architecture.py'\n''')
    put("README.md", (ROOT / "README.md").read_text(encoding="utf-8") + "\n## V2.0 雙語出版架構\n\nV2 採用 zh-TW 創作主稿與 en-US 人工審校譯稿，詳見 [V2 建置報告](BUILD-REPORT-V2.md)、[V2 章節登錄](metadata/chapters.yaml)、[翻譯規範](docs/TRANSLATION-V2.md) 與 [圖像權利規範](docs/IMAGE-RIGHTS-V2.md)。V1 原稿與素材已複製到 `legacy/2026-v1/`，附 SHA-256 遷移清單；V2 樣板不是已完成章稿。\n\n```powershell\npython scripts/v2_validate.py\npython -m unittest discover -s tests -p 'test_v2_architecture.py'\n```\n\n網站起始架構位於 `apps/web/`（Astro + Starlight 候選）；本地建置需先執行 `npm --prefix apps/web install`。不包含自動部署。\n")
    # Migration report lists all V1 files, including untracked source packs.
    (ROOT / "metadata").mkdir(exist_ok=True)
    shutil.copy2(manifest_path, ROOT / "metadata" / "migration-manifest.csv")
    print(f"Backed up and verified {sum(1 for _ in csv.DictReader(manifest_path.open(encoding='utf-8-sig')))} V1 files.")

if __name__ == "__main__":
    main()
