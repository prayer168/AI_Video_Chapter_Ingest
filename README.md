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
- [出版工具鏈](docs/PUBLISHING.md)
- `data/`：術語、來源、提示詞與資產資料
- `scripts/`：驗證、建置、連結與字型檢查

## 快速開始

需要 Python 3.10 或更新版本及 `pip install -r requirements.txt`。HTML 由 Python Markdown 建置；DOCX 需 Pandoc 或 `python-docx`；PDF 需 Pandoc 和 XeLaTeX。

```powershell
python scripts/validate_project.py
python scripts/build.py --format html
python scripts/build.py --format docx
python scripts/build.py --format pdf
```

輸出位於 `dist/`。DOCX/PDF 可用 `--font "Noto Serif CJK TC"` 指定字型。請安裝中文字型，並以 `python scripts/check_fonts.py --pdf dist/AI-Filmmaking-Bible.pdf` 檢查嵌入及人工抽查字形。

## 撰寫與來源原則

每章一個 Markdown 檔，位於 `chapters/`，檔名採 `NN-NN-slug.md`。依模板加入 YAML metadata，並更新目錄。狀態為 `planned`、`draft`、`review` 或 `verified`。

不得捏造史料、論文、官方文件、頁碼、URL 或工具功能。可查證主張須有可追溯來源；時效資訊記錄來源、日期和版本。區分已查證事實、電影理論、實務建議、AI 生成假設與示範內容。理論優先採專業研究，AI 技術優先採官方文件並記錄實測。

## 授權

原創文字採 CC BY-SA 4.0（`LICENSE-CONTENT`），程式碼採 MIT（`LICENSE-CODE`）。第三方作品及素材依其個別授權。
