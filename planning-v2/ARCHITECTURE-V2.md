# AI Video Bible — V2.0 出版與專案架構規格

狀態：Proposed／待 Codex 實作。正式語言：zh-TW 與 en-US。規劃日期：2026-10-18。

## 1. 原則

1. 一套內容模型、兩份語言原稿、書籍與網站兩種輸出。
2. `content/zh-TW` 是創作主稿；`content/en-US` 是經人工審校的專業譯稿，不以即時機器翻譯代替。
3. 所有章節使用永久 ID（如 `CH01`），所有圖使用永久 ID（如 `CH01-FIG-001`）；檔名及網頁路由可變，ID 不變。
4. 原始 AI 圖片不寫死大量文字；中文與英文圖號、標籤、說明保留可編輯分層，必要時由 SVG 疊加。
5. 繪圖以段落意圖為單位，電影感插圖為主；技術精度重要時採 SVG／向量繪製。
6. 書籍 PDF/EPUB 與網站皆從相同 Markdown/MDX 資料建立，版型可不同，不複製內容。
7. 不覆蓋舊版章節；先備份且建立遷移清單。
8. 影像生成記錄模型、生成日期、prompt、審校狀態、使用權與來源標記。

## 2. 建議儲存庫結構

```text
AI_Video_Bible/
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── package.json
├── content/
│   ├── zh-TW/
│   │   ├── frontmatter/
│   │   ├── chapters/
│   │   │   ├── CH01-cinematic-language.md
│   │   │   ├── CH02-camera-language.md
│   │   │   └── ...
│   │   └── backmatter/
│   └── en-US/
│       ├── frontmatter/
│       ├── chapters/
│       │   ├── CH01-cinematic-language.md
│       │   └── ...
│       └── backmatter/
├── assets/
│   ├── chapters/
│   │   ├── CH01/
│   │   │   ├── figures/
│   │   │   │   ├── originals/          # 原始生成圖
│   │   │   │   ├── approved/           # 出版核准無文字底圖
│   │   │   │   ├── overlays/           # SVG 雙語可編輯標註
│   │   │   │   └── exports/            # 依版面/語言輸出
│   │   │   ├── storyboards/
│   │   │   ├── reference-images/
│   │   │   └── figure-manifest.yaml
│   │   └── CH02/
│   └── shared/
├── metadata/
│   ├── chapters.yaml
│   ├── terminology.yaml
│   ├── references.bib
│   ├── translation-status.yaml
│   └── figure-registry.yaml
├── production/
│   ├── shot-lists/
│   ├── prompts/
│   ├── agent-instructions/
│   └── rubrics/
├── design/
│   ├── design-system.md
│   ├── book/                   # 紙本排版規範、樣式
│   └── web/                    # 響應式排版、元件樣式
├── apps/
│   └── web/                    # Astro + Starlight（自訂 editorial theme）
├── scripts/
│   ├── validate/               # Markdown、翻譯、圖片連結、參考文獻、無障礙
│   ├── figures/                # 轉換輸出、疊字、尺寸檢查
│   └── publishing/             # PDF／EPUB／HTML
├── legacy/
│   └── 2026-v1/               # 既有 chapters 與 source packs 原封保存
├── dist/
│   ├── books/zh-TW/
│   ├── books/en-US/
│   └── website/
└── release-packs/
    ├── CH01-Codex-V2.zip
    └── ...
```

## 3. 章節中英檔案契約

同一章兩個語言檔案使用相同 `chapter_id` 與段落錨點；每張圖的 `figure_id` 相同，`alt` 和 `caption` 各語系不同。示例：

```yaml
---
chapter_id: CH01
volume_id: V01
locale: zh-TW
slug: cinematic-language
title: 電影視聽語言：從單一鏡頭到完整敘事
translation_status: source-reviewed
revision: 2.0.0
---
```

英文為 `locale: en-US`，翻譯狀態必須標註 `draft / review-needed / approved / out-of-sync`。段落錨點不依賴中英文標題自動生成。

## 4. 圖片與圖說資料契約

```yaml
figure_id: CH01-FIG-003
chapter_id: CH01
section_id: CH01-S1.2
placement_after: CH01-P014
kind: cinematic-still
teaching_goal: 比較相同角色在遠景和特寫中的敘事資訊
asset_original: assets/chapters/CH01/figures/originals/CH01-FIG-003.png
asset_approved: assets/chapters/CH01/figures/approved/CH01-FIG-003.webp
overlay_zh: null
overlay_en: null
captions:
  zh-TW: 同一角色在不同景別中，觀眾注意的資訊會改變。
  en-US: Framing the same character differently changes what the viewer notices.
alt:
  zh-TW: 遠景呈現人物與教室空間，特寫突顯人物表情。
  en-US: A wide view establishes the classroom; a close-up emphasizes facial expression.
generation:
  tool: ChatGPT Images
  version: record-at-generation
  date: null
  prompt_file: production/prompts/CH01-FIG-003.md
rights_review: pending
technical_review: pending
editorial_review: pending
```

正式出版不得將 `pending` 圖示為已驗收；技術圖必須檢查幾何及術語；具實拍感的合成影像不得冒充真實紀錄。

## 5. 書籍與網站

- 書籍：繁體中文、英文各自生成 PDF 與 EPUB；PDF 必須嵌入中文字型，對頁排版、孤行寡行、跨頁圖說、圖片解析度需驗證。正式印刷由樣章校樣決定出血、安全邊界與色彩流程。
- 網站：同站 ` /zh-tw/ ` 與 ` /en/ `，以 locale 切換。每章同 ID 對應，缺譯標記，不悄悄展示錯語言內容。響應式圖文排版、圖像燈箱、搜尋、目錄、術語詞條可逐階段擴充。
- 網站可考慮 Astro + Starlight，必須自訂為電影編輯式版面，而非預設方框文件站。出版工具鏈以小規模雙語樣章驗收後定案。

## 6. V2.0 第一章最低交付

1. CH01 完整繁體中文 Markdown V2.0（不直接沿用舊稿而未審校）。
2. CH01 英文 Markdown 譯稿（逐節技術審校）。
3. 逐段 `figure plan`，包括圖號、插入點、教學意圖、圖說與提示詞。
4. 6–12 張依內容需要製作的內文圖（非硬性 KPI）；保留原圖、可編輯標註、雙語替代文字。
5. 雙語書籍樣章及雙語網站樣章。
6. Codex 完整素材包 ZIP，含 README、章節、圖、圖說、鏡頭 JSON、術語、參考與檢查報告。

## 7. 遷移安全

- 原有 `chapters/` 與 `source-packs/` 先保留，產生 `migration-manifest.csv` 逐一記錄來源和新位置；不得未經比對刪除或覆蓋。
- 若 Google Drive 同步與 Git 同時修改，應採單一權威工作副本，先檢查雲端／本機衝突。
- 第一次改造只提交架構、樣式和 CH01 樣章，驗收後才批次遷移其餘章節。
