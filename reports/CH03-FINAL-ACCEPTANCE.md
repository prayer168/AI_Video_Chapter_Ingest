# CH03 章節草稿驗收報告

- 章節：CH03《景別、視點與觀看位置》
- 英文暫定標題：*Shot Scale, Point of View, and the Spectator’s Position*
- 日期：2026-10-20（Asia/Taipei）
- revision：2.1.0-draft
- Pipeline run：`production/runs/CH03/20261020T060229+0800-cc9a6553/`
- 備份：`backups/CH03-start-20261020-060306/`；另有圖說轉換器備份 `backups/CH03-caption-filter-20261020-061102/`
- 狀態：**CH03 雙語草稿、原創技術圖及草稿格式測試完成；全書集中人工審核尚未進行。本章不是正式出版稿。**

## 變更摘要

- 將原本只有空白欄位的中英文 scaffold 擴寫為研究草稿，保留穩定錨點 CH03-S00–S14；含學習目標、先備知識、8 組雙語術語、基本原理、傳統方法、AI 使用限制、逐步流程、模型中立 Shot Specification、兩個來源案例、品質檢核及練習評量。
- 新增 `R030` Columbia Film Language Glossary 的 POV 詞條，與 `R022` Oklahoma State University 開放教材章節 locator 一起寫入雙份引用 registry。未引用未查明的精確電影版次、timecode、教材頁碼或 AI 模型功能。
- 新增 8 個雙語術語 ID `TERM-CH03-*`，全數維持 `draft`；新增 `metadata/translations/CH03-alignment.yaml`。
- 新增兩張自行編寫、可編輯的 SVG 教學圖 `CH03-FIG-001–002`。各自 SHA-256、雙語標題／圖說／alt、繪製方式及待審權利欄位記錄於章節與全域 manifest；沒有使用網路圖片或呼叫付費生圖 API。
- 章節 registry、translation-status 及 `CHAPTER_INTEGRATION_MATRIX.md` 更新為 review-needed／PARTIAL；未修改 CH01、CH02 正文或其圖稿，也沒有將任何章節標為 approved。
- 備份 manifest 記錄 10 個修改前檔案的 hash；未刪除或搬移舊章稿、素材或來源包。

## 研究與內容證據

| 來源 | 本章用途 | 查證範圍／限制 |
|---|---|---|
| R022，Uhlin, *Introduction to Film & TV* (2024)，Oklahoma State University Libraries | framing、景別距離分類與彈性、角度／高度區別、移動畫框、畫外空間、POV 與人物敘事對齊 | 2026-10-20 直接讀取公開教材的 Cinematography「Framing」「Types of Framing」及 Narrative「Point of View」頁面。教材概述不當作唯一電影史解釋；最終仍須按編輯選定版次核查。 |
| R030，Columbia Film Language Glossary, “Point of View” | POV 與 eyeline match 的關係；列出機構所編片段 metadata | 2026-10-20 直接讀取詞條。只引用詞條定義及索引範圍；本章撰稿者沒有因此宣稱看過索引所列版本，也沒有使用其 timecode。 |

電影史案例採 R022 的教材敘述並明確標示其論述範圍；電影案例版次、合法觀看來源、逐鏡筆記及 timecode 仍待全書集中審查時補查。章內旅人／燈煙及教室告示均明標為虛構教學示範。

## 章末全項目稽核

| 必要項目 | 狀態 | 證據／剩餘工作 |
|---|---|---|
| 學習目標與先備知識 | PASS | 中英文 CH03-S01、S02 已有可評量目標及先備說明。 |
| 專業術語中英文對照與定義 | PASS（資料結構）／NEEDS HUMAN REVIEW（定義核定） | 8 個雙語 ID 同步見兩語章稿、`metadata/terminology.yaml`、對照檔；詞條均為 draft，攝影專家及雙語編輯需核定用語和定義。 |
| 電影史與基本原理 | PASS（有來源草稿）／NEEDS HUMAN REVIEW（學理審查） | CH03-S04 引用 R022；教材 locator 已記錄。論述範圍、概念歸屬與採用教材版本需研究編輯確認。 |
| 傳統電影製作方法 | PASS（草稿） | CH03-S05 包含資訊任務、空間基準、景別試演、主觀關係和剪輯測試；實務流程需攝影／剪輯專家終審。 |
| AI 時代技術轉換、能力與限制 | PASS（保守界定） | CH03-S06 不宣稱自然語言能精確控制鏡頭；沒有特定工具版本實測，該段維持一般性限制。 |
| 詳細工作流程 | PASS | CH03-S07 列出輸入、操作和驗收條件。 |
| 提示詞、參數及版本紀錄 | PASS（示範）／NEEDS HUMAN REVIEW（實測） | CH03-S08 有模型中立 YAML 規格，明確標 `fictional-teaching-demo`；沒有模型生成實測或付費 API 呼叫。 |
| 電影案例及可追溯來源 | PASS（來源可追）／NEEDS HUMAN REVIEW（片段核看） | R022 案例與 R030 glossary 案例入口已說明來源限制；未提供合法發行版、觀看記錄或 timecode。 |
| 常見錯誤與品質驗證 | PASS（草稿） | CH03-S11 有症狀、修正、驗收方式；現場和觀眾測試尚未執行。 |
| 練習、評量及延伸研究 | PASS（草稿） | CH03-S12–S13 有 6–8 格作業、10 分評量錨點和延伸題；需教學編輯審查適切性。 |
| 主張分類與引用可追溯 | PASS（機器結構）／NEEDS HUMAN REVIEW（證據充分性） | Frontmatter 有 claim types；引用 R022/R030 均存在於 bibliography。頁碼不猜；來源對每個細項主張的充分性需人工查核。 |
| 中英節次、anchor、術語、案例、圖號對照 | PASS（結構） | 兩語 CH03-S00–S14 anchor 相同；8 個 TERM IDs、2 個 FIG IDs；`metadata/translations/CH03-alignment.yaml`。語意等值未人工簽核。 |
| 中英文稿件完整性與校譯 | NEEDS HUMAN REVIEW | 英文為雙語對照譯稿，尚未由人工雙語編輯校閱；標題目前為編輯暫定名。 |
| 來源版本、出版定位與連結 | NEEDS HUMAN REVIEW | R022/R030 公開頁已存取；教材採用版／紙本頁碼未核。全專案 link check：0 failures、0 network checked、5 inconclusive；不能視為外鏈全部有效。 |
| 原稿及素材備份、差異與保留 | PASS | `CH03-start` 備份 manifest 記 10 項修改前 hash；V1/V2 其他章稿與 staging 均保留。 |
| SVG 原檔、hash、繪製紀錄 | PASS（檔案）／NEEDS HUMAN REVIEW（作者歸屬／技術） | 原檔存在且 hash 見兩份 manifest；SVG 為專案手寫，個別繪製者姓名尚未登記，圖面可及性與印刷品質待人工檢視。 |
| 圖號、雙語圖說、alt、位置 | PASS（機器檢核） | 雙語各有 2 圖，穩定 ID CH03-FIG-001–002，網站 HTML 各 2 個 image/figure，alt 非空；PDF 抽文圖號無重複。 |
| 圖像原創性、權利、相似性及出版核准 | NEEDS HUMAN REVIEW | 沒有採用第三方圖片；兩 SVG 記錄為專案原創但個人作者歸屬未確認。rights／technical／editorial 均 pending、未核准出版。 |
| 網站投影、兩語 route、ID 與資產 | PASS（本機預覽） | `sync_site_content.py --check` 通過；Astro check 0 errors/warnings/hints；build 123 頁。CH03 中英路由均存在，各含 2 圖、2 figure IDs、非空 alt。未發布。 |
| DOCX 草稿及內嵌圖 | PASS（非正式） | Pandoc 3.12.1；兩語 DOCX 建置 exit 0，ZIP CRC 通過，各含 2 個 `word/media/` 資產。 |
| PDF 字型嵌入與繁中渲染 | PASS（草稿） | XeLaTeX/MiKTeX 26.5；strict `check_fonts.py --require-pdffonts` 中英均 exit 0，各 4 個字型項目全部 `emb=yes`，包含 Microsoft JhengHei。`pdftotext` 可擷取中英字元；第 1 頁及含兩張圖的第 7 頁已渲染抽查；修正圖說重複後圖號各只出現一次。全書印刷校樣未做。 |
| EPUB 結構、雙語文字及 EPUBCheck | PASS（草稿） | 中英 EPUB ZIP CRC 通過、各有 2 張 media，XHTML 文字含 2 個 CH03 figure IDs，未見 U+FFFD；EPUBCheck 5.4.0 各 0 errors／warnings／informationals／references。Pandoc 繁中模板仍警告缺 `zh-TW` 翻譯及 Abstract/Table/Figure 標籤本地化。 |
| 單元、整合與專案品質測試 | PASS | `python scripts/v2_validate.py` PASS；`python scripts/validate_project.py` PASS；`python -m unittest discover -s tests -v` 40/40；`git diff --check` exit 0（僅既有 LF/CRLF 工作副本提醒）。 |
| CH03 專項完整性核對 | PASS | 本輪附加檢查確認 anchor/TERM/FIG ID 成對一致、引用 ID 存在、兩圖檔 hash 與 manifest 一致、權利狀態仍 pending、網站和 EPUB 對應圖數為 2。 |
| 作者／專業審稿人／權利核准 | NEEDS HUMAN REVIEW（依作者決策延後） | 使用者決定全書完成後集中審核。本章不等待簽核才繼續後續製作，但在簽核前不得標 `approved` 或 `publication-ready`。 |
| 正式全書出版、發布及 GitHub | BLOCKED／NOT RUN | 全書 60 章尚未核准；正式全書 builder 閘門保持封鎖。沒有部署、commit 或 push。 |

## 建置問題與修復記錄

1. Pandoc 以專案 Unicode 工作目錄輸出診斷時曾遇 Windows console encoding error；改從 ASCII 工作目錄執行並設 `LANG=C.UTF-8`／`LC_ALL=C.UTF-8` 後，六種雙語草稿格式均可產出。
2. Pandoc 缺少 `rsvg-convert`，首次把 SVG 轉換至 DOCX／PDF 時缺圖。使用 Inkscape 1.4.4 從原始 SVG 產生 `tmp/CH03-draft-20261020/` 下的 1600px PNG 排版衍生檔，重建後驗證 DOCX/PDF/EPUB 各含兩圖；canonical SVG 未改動。
3. PDF 首次抽查發現手動「圖 3-1／圖 3-2」與 Pandoc 自動圖號重複。備份 `figure-captions.lua` 後增加 CH03 永久圖號映射，重建 PDF 並抽文／抽頁確認修復。
4. 第一輪全套測試在網站尚未同步時有一項投影測試失敗；同步後再跑，40 項全數通過。
5. Pandoc 仍有繁中模板字串翻譯警告；正文、字型、圖和 EPUBCheck 均通過，但書籍模板字串應在後續出版樣式工作中處理。

## 草稿成品與重現

成品與衍生 PNG 位於 `tmp/CH03-draft-20261020/`（gitignored，僅為本機校稿預覽）。格式包含 zh-TW/en-US 的 DOCX、PDF、EPUB；`OUTPUT-MANIFEST.json` 列出輸出 hash。最新素材包為 `CH03-Codex-Materials-DRAFT-r2.zip`，內含雙語原稿、章節對照、圖稿母檔、manifest、驗收報告及六份草稿格式，並附未核准出版聲明；較早的 `CH03-Codex-Materials-DRAFT.zip` 原樣保留。圖稿正式母檔在 `assets/chapters/CH03/figures/originals/`。

## 結論

**CH03 是否達到正式出版標準？否。** 本章的可安全自動完成工作、雙語草稿、圖稿登錄及本機出版預覽已完成；英文校譯、研究／攝影專業審稿、電影合法版本與片段核看、圖稿作者歸屬與權利／可及性終審、全書集中作者簽核仍待處理。以上為全書完稿後的集中審核清單，不阻擋目前轉入下一章製作。

本章工作報告交付後停止；下一章依使用者「每章完成後再進下一章」指示，等待使用者提出下一章製作要求。
