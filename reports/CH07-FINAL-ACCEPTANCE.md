# CH07 最終驗收｜人物、欲望、衝突與角色弧線

- 日期：2026-10-21（Asia/Taipei）
- 版本：2.1.0-draft
- 狀態：`draft / review-needed`；未達正式出版標準
- Run：`production/runs/CH07/20261021T185845+0800-c279f9b1/`
- 草稿輸出：`tmp/CH07-draft-20261021-r5/`
- 基線備份與 SHA-256：run 目錄 `backup/pre-edit/MANIFEST.json`
- 範圍：由既有空白 scaffold 建立 CH07 中英文研究草稿、術語、兩張原創 SVG、網站投影及出版格式草稿。未修改 CH01–CH06 正文，不發布網站、不 commit、不 push。

## 逐項驗收

| 檢查項目 | 狀態 | 實測證據／待辦 |
|---|---|---|
| 學習目標、先備知識、歷史／理論、傳統方法、AI 轉換、工作流程、提示詞、案例、錯誤檢查、練習與來源 | PASS（草稿內容存在） | 中英文稿含 CH07-S00–S13 穩定節次；技術及理論主張附來源或明列為實務建議／未實測假設。專業內容仍須審稿。 |
| 雙語章節及節次對照 | PASS（結構）／NEEDS HUMAN REVIEW（語言） | `metadata/translations/CH07-alignment.yaml` 對照穩定錨點；英文為工作譯稿，需雙語編輯校譯。 |
| 術語管理 | PASS（登錄）／NEEDS HUMAN REVIEW（核定） | 8 個 `TERM-CH07-*` 已登錄並在兩語稿使用；詞義、譯名及全書一致性待術語編輯核定。 |
| 理論來源、版本與頁碼定位 | NEEDS HUMAN REVIEW | 可追溯來源已加入 YAML/BibTeX，定位限制記在 `assets/chapters/CH07/CH07-SOURCE-AND-CASE-NOTES.md`；需按編輯選定版次核對。 |
| 電影案例與觀看片段 | NEEDS HUMAN REVIEW | 案例分析有具名二手來源，不宣稱已親看特定版次；作者／編輯需核電影版本、字幕及需要的時間碼。 |
| 原創圖 7-1、7-2 及 SVG | PASS（檔案／技術）／NEEDS HUMAN REVIEW（權利） | 兩張原創可編輯 SVG、檔案雜湊、雙語 caption/alt 已登錄。圖說明示非電影劇照。製作者署名、相似性、無障礙及出版權利核准仍 pending。 |
| 圖片檔案與權利狀態 | PASS（待審標示） | `figure-manifest.yaml` 和全域登錄維持 pending；不得視為正式出版核准。 |
| 中英文網站投影 | PASS（本機建置） | `npm --prefix apps/web run check`：0 errors/warnings/hints；build 成功 123 pages。中英文 CH07 routes 各有 43 個唯一 ID、2 張本章圖片且 alt 非空。未發布網站。 |
| DOCX 草稿 | PASS（建置） | `tmp/CH07-draft-20261021-r5/CH07-zh-TW-draft.docx`、`CH07-en-US-draft.docx`；build log 無錯誤；DOCX SVG 暫存點陣化回歸測試通過，原 SVG 保留。圖號顯示方式仍須編輯確認。 |
| PDF 草稿及字型嵌入 | PASS（技術） | 中英文 PDF 均有嵌入 `Microsoft JhengHei`，嚴格 `pdffonts` 檢查全部 emb/sub/uni=yes；PyMuPDF 抽字 replacement-char 數為 0；中文 9 頁、英文 12 頁；圖號 7-1、7-2 各出現一次。proof 已目視確認圖文可讀、無黑色背景。 |
| EPUB 草稿 | PASS（格式） | 中英文 EPUBCheck logs 均記錄以 EPUB 3.4 規則驗證：0 致命錯誤、0 errors、0 warnings、0 references。此 log 未記錄 EPUBCheck 工具版本。 |
| 兩張圖的版面顯示 | PASS（草稿目視） | `tmp/CH07-draft-20261021-r5/proofs/zh-TW-figpage-5.png`、`zh-TW-figpage-7.png`、`en-US-figpage-8.png` 及白底 SVG proof 已檢視；圖說和圖面可辨。 |
| CH07 專項自動測試 | PASS | `python -m unittest tests.test_ch07_content -v`：6/6 PASS，涵蓋雙語節次、術語、來源、SVG 雜湊／權利狀態、DOCX 圖片 staging。 |
| 專案 validators | PASS | `python scripts/v2_validate.py` PASS；`python scripts/validate_project.py` PASS（12 parts、60 planned chapters、52 terms、52 references）。 |
| 全專案單元測試 | FAIL（既有 CH01 缺欄位） | `python -m unittest discover -s tests -v`：61 tests 中 1 error；`tests/test_ch01_content.py::test_chapter_terms_are_bilingual_and_registered` 因既有 CH01 詞條缺 `status` 欄位而 KeyError。CH01 基線備份證明此問題在本輪前已存在；本次不修改 CH01。 |
| 外部連結檢查 | NEEDS HUMAN REVIEW | 0 failures；7 個連結未能確定可達（網路未驗證／暫時不可判定，不等同於失效）。需在來源審查時人工複查。 |
| 全書發布權利閘門 | BLOCKED（正確阻擋） | CH07 插圖仍待核准；專案其他章節亦有 pending 圖片。出版發布不得通過。 |
| 作者與專業簽核 | NEEDS HUMAN REVIEW | 依作者安排，集中於全書章節完成後辦理。不得標示 `publication-ready`。 |

## 待全書集中審查

1. 電影研究／編劇專業審稿，核對理論歸屬、各採用版本的頁碼與案例解讀。
2. 雙語編輯校譯，核定 8 個 CH07 術語及英文標題。
3. 作者／編輯決定電影案例的觀看版本、字幕及時間碼需求；沒有核實的鏡頭級主張不得補寫。
4. 審查兩張原創 SVG 的作者署名、視覺相似性、無障礙和正式出版授權狀態。
5. 修復或確認 CH01 詞條缺 `status` 的既有測試錯誤，再重跑全套測試。
6. 複查 7 個未確定外部連結。
7. 編輯確認 DOCX/PDF 圖號與全書排版慣例。

## 判定

CH07 的雙語研究草稿、可編輯原創示意圖、網站本機建置及 DOCX/PDF/EPUB 草稿已完成；本章專項測試及兩項專案 validator 通過。全套測試仍受既有 CH01 資料錯誤影響，且英文校譯、理論與案例審稿、插圖權利核准和作者簽核尚未完成。**CH07 尚未達正式出版標準。** 本輪只完成 CH07，不自動開始 CH08。
