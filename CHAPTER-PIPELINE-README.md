# AI Video Bible V4 Chapter Pipeline

本專案以 Codex Skill 作為章節工作流入口，以現有 V2 registry、Markdown、assets、Astro、Pandoc 與 validators 作為內容及出版管線。V4 是增量自動化層，不取代 V1/V2 原稿。

## 最簡單的用法

在此專案的 Codex 對話輸入：

```text
製作第 3 章
```

也可明確指定：

```text
$ai-video-bible-chapter-pipeline 製作 CH03
```

Codex 會先按 `metadata/chapters.yaml` 確認章節，建立備份及 run log，再依 SOP 完成可安全執行的工作。需要付費 API、帳戶登入、生成影像預算或作者／專業核准時，流程保留 BLOCKED/NEEDS HUMAN REVIEW，繼續不依賴該項目的其他工作。

若只要建立檢查點，不啟動撰稿：

```powershell
python scripts/chapter_pipeline.py --chapter 3
```

此命令只讀取 registry、現有檔案及狀態，建立 `production/runs/CH03/` 下的新 run 資料夾與 checklist，不撰稿、不建圖、不改章稿。完成後，Codex Skill 會把研究與編輯工作記錄在該 run。

## 已有工具鏈

- 內容：`content/zh-TW/chapters/`、`content/en-US/chapters/`
- Registry：`metadata/chapters.yaml`、`metadata/translation-status.yaml`
- 術語、引用、圖：`metadata/terminology.yaml`、`metadata/references.yaml`、`assets/chapters/CHNN/figure-manifest.yaml`
- 網站：Astro + Starlight，`apps/web/`
- 出版：Pandoc + XeLaTeX/MiKTeX；EPUBCheck；字型與圖像政策腳本
- 新 Skill：`.codex/skills/ai-video-bible-chapter-pipeline/SKILL.md`
- 完整 SOP：`AI-VIDEO-BIBLE-SOP-V4.md`
- 生圖 adapter：`production/image_generation/adapter.py`（預設 BLOCKED；測試替身不會產生圖片）

## 安全閘門

- 先看 Git 狀態、既有內容、章節 registry 和過往報告；每次章節修改前備份並 hash。
- 保留 V1、V2、來源包與原始圖。不以另一份重複稿取代 canonical 稿。
- 不下載網路第三方圖片；不把 AI 生成當成自動有權利。沒有圖像服務授權或預算時只建立 brief／SVG 技術圖。
- API 呼叫預設不可用。需另行確認服務條款、帳戶計費、單章預算、每圖上限後，才可由作者明確啟用。
- 人工譯校、電影史／法律審查、圖像權利和出版核准均不能以 CI 或成功建置取代。
- 不部署、不推送 GitHub、不 commit；除非使用者明確要求。

## 初次驗證

```powershell
python -m unittest discover -s tests -v
python scripts/chapter_pipeline.py --chapter 1
python scripts/v2_validate.py
python scripts/validate_project.py
python scripts/publishing/sync_site_content.py --check
npm --prefix apps/web run check
```

`CHAPTER-PIPELINE-TEST-REPORT.md` 記錄本次驗證實測結果。單元測試只驗證結構與安全邏輯；它不聲稱完成一章研究、圖像生成或作者核准。

## 出版工具的限制

`scripts/publishing/build_books.py` 執行正式書籍全量 gate，要求 60 章和人工核准狀態。它可能因目前只有少量內容而 BLOCKED；章節預覽應使用本 SOP 明列的臨時 draft 命令，輸出至 `tmp/`，不得把 draft 標成出版品。PDF 嵌入字型需由 `pdffonts` 或等效 PDF 解析器查驗，繁體字形及版面仍需渲染後人工抽頁。

## 新章完成後

更新翻譯／章節／圖稿 registry、章節 acceptance report、`history.md` 和該 run 的最終狀態。報告的每個 PASS 都附命令或審核人證據；沒測到就寫 NOT RUN 或 BLOCKED。
