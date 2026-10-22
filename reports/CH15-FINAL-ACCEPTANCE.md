# CH15 最終驗收報告｜Final Acceptance

- 章名：現場導演：排演、覆蓋與臨場修正 / On-Set Directing: Rehearsal, Coverage, and Real-Time Adjustment（英文工作章名）
- 版本：2.1.0-draft
- 日期：2026-10-23（Asia/Taipei）
- 狀態：**研究草稿完成；未達正式出版標準**
- 範圍：只處理 CH15。未開始 CH16；未發布網站；未 commit、未 push。

## 驗收表

| 檢查項目 | 狀態 | 實測證據／限制 |
|---|---|---|
| 起始盤點與備份 | PASS | `backups/CH15-start-20261023-060700/` 保存 19 個檔案；run checkpoint 記錄原稿與空 manifest SHA-256。舊 V1／其他章節未覆寫。 |
| 雙語正文 | PASS（草稿） | 中英文各 S01–S12，12 個穩定 section ID 完全對齊；含目標、先備知識、術語、歷史原理、傳統流程、AI 限制、操作流程、提示詞、案例、錯誤檢查、練習與來源。 |
| 翻譯對照 | PASS（草稿） | `metadata/translations/CH15-alignment.yaml` 登錄 12 節；英文仍需專業校譯。 |
| 來源與案例 | PARTIAL | R107–R111 已列入資料庫與 BibTeX，頁面於 2026-10-23 開啟核對；ScreenSkills 為英國職務資料，ASC 為實務訪談，DGA 為 2003 專業組織宣言。精確段落 locator、作者／出版資訊及具合法觀看版本和時間碼的電影案例仍待查；正文沒有假稱已觀片。 |
| 術語 | PASS（草稿） | 6 個中英詞條在 `metadata/terminology.yaml` 與 `data/terms.yaml` 登錄；定義待導演與雙語編輯審定。 |
| 圖稿檔案與權利 | PASS（檔案）／NEEDS HUMAN REVIEW（刊用） | 2 張手繪可編輯 SVG，XML 可解析，尺寸 1200×620，SHA-256 與容量列於 manifest。原創製作紀錄已寫；署名、相似性、可及性與刊用許可均 pending。 |
| 雙語圖說／alt | PASS（草稿） | `figure-captions.md`、manifest、兩語正文及網站均含兩張圖與非空 alt；圖號 15-1、15-2。 |
| 網站 | PASS（本機建置） | Astro check：0 errors/warnings/hints；前置內容同步曾印出 duplicate-id loader notices，實際輸出 HTML 各 43 個 ID、無重複，包含兩個穩定 figure IDs、2 張有 alt 圖片；Astro build 成功產生 123 頁。未發布。 |
| DOCX | PASS（草稿） | 中英文 DOCX 均存在於 `tmp/CH15-draft-20261023-r4/`，含圖像素材。 |
| PDF 與字型 | PASS（草稿） | 中英文 PDF 分別 8／10 頁；`pdffonts` 對各 13 個字型項目均顯示 embedded=yes。繁中採 Microsoft JhengHei，英文字體 Times New Roman；`pdftotext` 抽查圖號 15-1／15-2，未見替代字元。**Noto Serif TC 曾失敗**（MiKTeX `dvipdfmx: Invalid font: -1` 並有缺字），該失敗輸出未列為通過。 |
| EPUB | PASS（草稿） | EPUBCheck 5.4.0 對繁中與英文均回報 0 fatal／0 errors／0 warnings／0 informational；輸出於同一 r4 目錄。 |
| CH15 專項測試 | PASS | `python -m unittest tests.test_ch15_content -v`：5/5 通過。 |
| 專案驗證 | PASS | `scripts/v2_validate.py`、`scripts/validate_project.py`、`scripts/publishing/sync_site_content.py --check` 均通過。 |
| 全套測試 | PARTIAL | `python -m unittest discover -s tests -v`：97/98 通過。唯一既有錯誤為 `test_ch01_content.Chapter01ContentTests.test_chapter_terms_are_bilingual_and_registered` 的 `KeyError: status`；未修改 CH01。 |
| 作者／專業／權利簽核 | NEEDS HUMAN REVIEW | 清單見 `assets/chapters/CH15/CH15-HUMAN-REVIEW-CHECKLIST.md`。未簽核，禁止標示 publication-ready。 |

## 已完成

- 完成 CH15 中英文 S01–S12 研究草稿，保留作為可修訂原稿。
- 登錄 R107–R111、六個雙語術語、章節翻譯對照、兩張 SVG、圖說／alt、來源及權利紀錄。
- 更新 CH15 章節與翻譯狀態、整合矩陣、進度表、`history.md` 和 run log。
- 本機網站、DOCX、PDF、EPUB 草稿與自動檢查已執行；未發布。

## 未完成／人工審查

1. 為 R107–R111 補精確段落 locator，並逐筆核實作者、日期、版本或來源機構欄位。
2. 作者選定一至兩部電影，記錄可合法觀看版次、地區／發行資訊、場景及時間碼，再完成具體鏡頭分析。
3. 導演、演員／片場製作專業審查流程、職責及安全／同意內容；必要時按法域修訂。
4. 中英文編輯完成專業校譯與術語定稿；核對英文工作章名。
5. 作者／權利審查者核准 SVG 署名、原創性、可及性及刊用狀態。
6. 修復既有 CH01 全套測試 `KeyError: status`，再重跑全套測試。
7. 出版前另行做頁面視覺校樣、PDF 字型／字元逐頁抽查和作者簽核。

## 結論

**CH15 已完成可驗證的研究草稿與本機出版預覽，但沒有達到正式出版標準。** 來源定位、指定電影觀看片例、雙語／電影專業審校、插圖權利及作者核准仍是阻擋項。此報告不授權發布、刊用或對外宣稱定稿。
