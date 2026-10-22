# CH16 最終驗收報告｜Final Acceptance

- 章名：曝光、感光元件與影像形成 / Exposure, Image Sensors, and Image Formation
- 版本：2.1.0-draft
- 驗收日期：2026-10-23（Asia/Taipei）
- 範圍：僅 CH16；原有 CH04–CH15 與未提交變更保留。
- 起始備份：`backups/CH16-start-20261023-062121/`（含起始稿、登錄表、網站投影、Git 狀態及 `SHA256SUMS.txt`）
- 主要 run：`production/runs/CH16/20261023T061952+0800-95526c49/`
- 出版狀態：**研究草稿與本機出版預覽完成；尚未達正式出版標準。**
- 發布邊界：本地建置；本次未發布網站，未 commit、未 push。

## 驗收摘要

| 檢查項目 | 狀態 | 實測證據／限制 |
|---|---|---|
| 起始盤點、Git 狀態與備份 | PASS | 依章節登錄確認 CH16 原為 scaffold；保存起始稿與空圖 manifest 的 hash。備份位於上述資料夾；V1、其他章節、素材與既有工作樹變更均保留。 |
| 中英文正文 | PASS（研究草稿） | `content/zh-TW/chapters/CH16-chapter-16.md` 與 `content/en-US/chapters/CH16-chapter-16.md` 含 S01–S12；目標、先備知識、術語、歷史原理、傳統方法、AI 限制、流程、提示詞／JSON、技術案例、QA、練習與參考資料均有正文。機器驗證不代表專業核稿。 |
| 雙語節次與翻譯對照 | PASS（結構）／NEEDS HUMAN REVIEW（語言） | `metadata/translations/CH16-alignment.yaml` 登錄 12 節；`tests.test_ch16_content` 驗證 S01–S12 對齊。英文仍待雙語編輯校譯。 |
| 來源與主張定位 | PASS（登錄）／NEEDS HUMAN REVIEW（專業複核） | R112–R119 登錄於來源資料與 BibTeX；`assets/chapters/CH16/CH16-SOURCE-AND-CASE-NOTES.md` 註明 locator 與限制。R119 已將 Log C 與底片負片掃描的類比主張連回 ARRI 官方 FAQ；ARRI／Kodak／Sony 廠商來源有範圍限制。頁碼及各主張支持範圍仍須研究編輯覆核。 |
| 術語登錄 | PASS（草稿資料）／NEEDS HUMAN REVIEW（定義核定） | 12 個雙語詞條登錄於 `metadata/terminology.yaml`、`data/terms.yaml`；來源和 draft 狀態可查。 |
| 電影片例及時間碼 | NEEDS HUMAN REVIEW | 本章採 Kodak／ARRI 技術案例，未假稱已觀看片段；作者／研究編輯仍須提供合法影片版本、觀看來源、場景及時間碼，或核定本章不採電影場景分析。 |
| 圖稿、圖說、alt 與權利 | PASS（資產登錄）／NEEDS HUMAN REVIEW（刊用） | 2 張原創手繪可編輯 SVG：`CH16-FIG-001`、`CH16-FIG-002`；SHA-256、尺寸、製作方法、來源、雙語圖說與 alt 登錄在 manifest／asset registry。權利、技術、可及性、署名、相似性及出版核准均 pending；沒有下載第三方圖片。 |
| CH16 自動測試 | PASS | `python -m unittest tests.test_ch16_content -v`：5/5 通過。 |
| 專案資料驗證 | PASS | `python scripts/v2_validate.py` 與 `python scripts/validate_project.py` 通過；後者顯示 12 篇／60 章、90 個詞條、114 筆參考資料。 |
| 雙語網站投影與同步 | PASS | 僅更新 CH16 兩個 Astro 投影及該章圖片；`sync_site_content.py --check` 通過。產生 `/zh-tw/ch16-chapter-16/`、`/en/ch16-chapter-16/`。兩頁各 42 個唯一 HTML IDs、2 張具 alt 的 CH16 圖片。 |
| Astro 檢查 | PASS（診斷）／警告已記錄 | 實測 check 為 0 errors、0 warnings、0 hints；啟動載入階段曾出現 CH16 重複內容 ID loader notices。輸出 HTML 實查無重複 ID，後續 Astro build 未重現 notices；建置仍成功。此 loader 提示保留為追蹤警告。 |
| 網站建置 | PASS（本機） | `npm --prefix apps/web run build` 成功，產生 123 個靜態頁面，含中英文 CH16 路由；未部署。 |
| DOCX | PASS（草稿） | 中英 DOCX 產生於 `tmp/CH16-draft-20261023-r3/`。 |
| PDF、字型與渲染 | PASS（草稿抽驗）／NEEDS HUMAN REVIEW（全頁校樣） | 中 PDF 10 頁、英 PDF 14 頁。`pdffonts`：中 23 項、英 22 項，均 `emb=yes`；`pdftotext` 可擷取標題與圖號 16-1／16-2。已渲染抽查中文第 1、5 頁，繁中字形可讀、圖文未截斷；圖內小字仍待設計／作者檢視。未作全頁校樣。 |
| EPUB | PASS（草稿） | 中英文 EPUBCheck 5.4.0 均為 0 fatal errors、0 errors、0 warnings、0 informational；解壓檢查可見正文文字與 2 個圖號。 |
| 全套測試 | FAIL（既有 CH01 失敗） | `python -m unittest discover -s tests -v`：103 tests，102 通過、1 error。錯誤在 `tests/test_ch01_content.py`，`KeyError: 'status'`；本次未改 CH01，詳見 `tmp/CH16-draft-20261023-r3/full-tests.log`。 |
| 作者／專業／權利核准 | NEEDS HUMAN REVIEW | `assets/chapters/CH16/CH16-HUMAN-REVIEW-CHECKLIST.md` 列出攝影／DIT／影像科學、英文編輯、來源定位、片例、SVG 可及性／權利及作者簽核待辦。 |
| run、history 與進度表 | PASS | 主要 run、`history.md`、`reports/CHAPTER-PROGRESS-TRACKER.md` 已更新；本報告記錄剩餘風險與證據。 |

## 本次完成

- 完成 CH16 中英 S01–S12 研究草稿及逐節翻譯對照，維持 `review-needed`。
- 登錄 R112–R119、12 個雙語術語、2 個原創 SVG 圖稿及雙語圖說／alt／權利欄位。
- 將英文稿中 Log C 類比誤引由 R113 更正為 ARRI 官方 FAQ R119，避免用動態範圍白皮書支持未涵蓋的主張。
- 本機建置中英文網站及 DOCX／PDF／EPUB 草稿；完成 CH16 專項、自動結構、PDF 字型、頁面渲染和 EPUBCheck 檢查。
- 更新章節矩陣、章末人工審查清單、進度表與 `history.md`。

## 尚未完成／待辦

1. 攝影指導、DIT 或影像科學專家核對底片與數位感光、EI、動態範圍、SNR、剪裁及影像鏈敘述。
2. 編輯逐項覆核 R112–R119 的版本、頁碼／段落 locator、及各主張實際支持範圍。
3. 雙語編輯完成英文校譯及術語定稿。
4. 作者／研究編輯選定合法取得的電影版本，完成觀片紀錄與時間碼；或明確核准維持技術案例而不增電影場景案例。
5. SVG 審查者檢視技術準確性、縮印可讀性、語意與可及性；作者／權利審查者核准署名、相似性與出版權利。
6. 修復 CH01 全套測試中的 `status` 欄位錯誤，重跑全套測試；本章未擅改 CH01。
7. 完成中英文 PDF 全頁校樣、EPUB 閱讀器人工抽查與作者最終簽核。

## 最終判定

**CH16 尚未達到正式出版標準。** 可交付的是來源可追溯、已通過章節專項測試並完成雙語本機出版預覽的研究草稿。英文編輯、攝影／影像科學審查、來源定位複核、電影案例決策、插圖技術／權利核准和作者簽核尚未完成；全套測試亦有一項既有 CH01 錯誤。不得標記 `publication-ready`。
