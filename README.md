# AI 電影製作聖經

**《AI 電影製作聖經：從電影語言到 AI Agent 自動化製片》** 是長期開源的繁體中文電影製作百科與 AI 影視技術教科書計畫，並維護專業術語、提示詞資料庫和自動出版系統。

> 第一階段工程骨架與第一章草稿 v0.2.0。目錄和模板已建立；其餘 59 章正文尚未撰寫。

## 專案文件

- [全書目錄](docs/TOC.md)
- [章節素材匯入流程](docs/CHAPTER-INGEST.md)
- [Codex 章稿匯入技能：AI_Video_Chapter_Ingest](.codex/skills/ai-video-chapter-ingest/SKILL.md)
- [章節模板](templates/chapter-template.md)
- [術語資料模型](docs/TERMINOLOGY.md)
- [引用與證據規範](docs/REFERENCES.md)
- [品質審查規則](docs/QUALITY.md)
- [資產管理規範](docs/ASSETS.md)
- [插圖原創與著作權規範](docs/IMAGE-RIGHTS-POLICY.md)
- [出版工具鏈](docs/PUBLISHING.md)
- [建置與編輯歷史](history.md)
- `data/`：術語、來源、提示詞與資產資料
- `scripts/`：驗證、建置、連結與字型檢查

## 快速開始

需要 Python 3.10 或更新版本及 `pip install -r requirements.txt`。HTML 由 Python Markdown 建置；DOCX 需 Pandoc 或 `python-docx`；PDF 需 Pandoc 和 XeLaTeX。

正式建置會先檢查圖片來源、資產登錄及權利／品質核准；尚有待審圖片時，正式輸出會停止。編輯預覽以 `--preview` 產生，並省略未核准圖片；詳細規則見[插圖原創與著作權規範](docs/IMAGE-RIGHTS-POLICY.md)。

```powershell
python scripts/validate_project.py
python scripts/build.py --format html --preview
python scripts/build.py --format docx --preview
python scripts/build.py --format pdf --preview
python scripts/build.py --format epub --preview
```

輸出位於 `dist/`。DOCX/PDF 可用 `--font "Noto Serif CJK TC"` 指定字型。請安裝中文字型，並以 `python scripts/check_fonts.py --pdf dist/AI-Filmmaking-Bible.pdf` 檢查嵌入及人工抽查字形。

## 撰寫與來源原則

每章一個 Markdown 檔，位於 `chapters/`，檔名採 `NN-NN-slug.md`。依模板加入 YAML metadata，並更新目錄。狀態為 `planned`、`draft`、`review` 或 `verified`。

ChatGPT Work 完成一章後，在 Codex 說「第二章完成了，請整理」即可啟動[章節收錄流程](docs/CHAPTER-INGEST.md)。流程沿用 `chapters/` 既有章稿、`-assets/` 素材夾及 `source-packs/` 原稿位置；Codex 不會在背景自動監看檔案。

不得捏造史料、論文、官方文件、頁碼、URL 或工具功能。可查證主張須有可追溯來源；時效資訊記錄來源、日期和版本。區分已查證事實、電影理論、實務建議、AI 生成假設與示範內容。理論優先採專業研究，AI 技術優先採官方文件並記錄實測。

## 授權

原創文字採 CC BY-SA 4.0（`LICENSE-CONTENT`），程式碼採 MIT（`LICENSE-CODE`）。第三方作品及素材依其個別授權。

## V2.0 雙語出版架構

V2 採用 zh-TW 創作主稿與 en-US 人工審校譯稿，詳見 [V2 建置報告](BUILD-REPORT-V2.md)、[V2 章節登錄](metadata/chapters.yaml)、[翻譯規範](docs/TRANSLATION-V2.md) 與 [圖像權利規範](docs/IMAGE-RIGHTS-V2.md)。V1 原稿與素材已複製到 `legacy/2026-v1/`，附 SHA-256 遷移清單；V2 樣板不是已完成章稿。

```powershell
python scripts/v2_validate.py
python -m unittest discover -s tests -p 'test_v2_architecture.py'
```

網站起始架構位於 `apps/web/`（Astro + Starlight 候選）；本地建置需先執行 `npm --prefix apps/web install`。不包含自動部署。

## V2 電影知識整合

- [專案現況盤點（2026-10-19）](reports/PROJECT-STATUS-V2-20261019.md)
- [十二大電影核心元素](FILM_ELEMENTS.md)
- [八大 AI 電影製作系統與工具整合狀態](AI_PRODUCTION_SYSTEMS.md)
- [60 章整合矩陣](CHAPTER_INTEGRATION_MATRIX.md)
- [電影品質 Rubric 與驗收閘門](FILM_QUALITY_RUBRIC.md)
- [V2 章節模板入口](CHAPTER_TEMPLATE_V2.md)（canonical 模板：`templates/chapter-v2.md`）
- [V2 增量整合與遷移計畫](MIGRATION_PLAN_V2.md)

電影核心分類和 AI 系統文件是規劃／編輯參考，不能代替逐章查證和章末驗收。Remotion、Manim、Blender、ComfyUI 尚未整合；**Cinetic 與 TTS 依作者指示排除**。未經核准不安裝付費服務、不發布網站、不推送 GitHub。
