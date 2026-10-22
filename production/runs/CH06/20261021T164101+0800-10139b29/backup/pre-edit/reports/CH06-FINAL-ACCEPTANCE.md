# CH06 Final Acceptance｜故事、情節與因果結構

- 日期：2026-10-21（Asia/Taipei）
- 版本：2.1.0-draft
- 狀態：draft / review-needed；不是 publication-ready
- Run：`production/runs/CH06/20261021T065143+0800-f153e02e/`
- 前置備份：run 目錄內 `backup/pre-edit/`；SHA-256 見 `backup/MANIFEST.json`。
- 範圍：從空白雙語 scaffold 製作研究草稿；未修改 V1、CH01–CH05 原稿；無 commit、push 或網站發布。

## 逐項驗收

| 檢查項目 | 狀態 | 證據／後續行動 |
|---|---|---|
| 學習目標與先備知識 | PASS | CH06-S01/S02 以可觀察能力和章節前置條件描述。 |
| 中英文節次與穩定 ID | PASS | CH06-S01–S12 兩語一致；alignment YAML 對照。 |
| 專業術語雙語登錄 | PASS | 8 個 TERM-CH06 IDs 已登錄；均為 draft，等待術語編輯。 |
| 歷史／理論事實 | NEEDS HUMAN REVIEW | Aristotle 僅按《詩學》悲劇理論歸屬；R046 web chapters cited，採用版次與中譯詞及印刷頁碼待專業核對。 |
| 電影敘事研究來源 | NEEDS HUMAN REVIEW | R047 出版者書目與研究範圍已核；未讀全文，具體主張需按採用版次定位。 |
| 傳統製作方法 | PASS | 場景目標、因果節點、故事時間／呈現順序工作方法已列為實務流程。 |
| AI 技術能力與限制 | PASS | 僅列可測工作假設、失誤風險與資料紀錄要求；不宣稱工具已實測或保證能力。 |
| 詳細工作流程 | PASS | CH06-S07 10 步驟，包含作者決策和版本記錄。 |
| 提示詞與參數 | PASS | CH06-S08 提供模型中立模板及 JSON 示例；清楚標示未實測，不虛構供應商參數。 |
| 電影案例與來源 | NEEDS HUMAN REVIEW | *Rashomon* R048–R050 使用可查片目與具名影評；作者觀看版本、字幕及時間碼尚未登錄。 |
| 圖片及權利 | NEEDS HUMAN REVIEW | 本輪未使用影像或第三方圖片，沒有將缺圖冒充完成；原創因果／多視點 SVG、圖說、alt 與 figure manifest 尚待製作及審查。觀看版次欄位模板見 `assets/chapters/CH06/CH06-RASHOMON-VIEWING-LOG.md`。 |
| 常見錯誤與品質驗證 | PASS | CH06-S10 列出 7 類錯誤及機器可測／須人工判斷分界。 |
| 練習、評量與研究 | PASS | 3 項練習、0–4 課堂 rubric 和延伸研究方向。 |
| 引用登錄／雙語引用同步 | PASS | R046–R050 已同步 YAML/BibTeX 及雙語正文；locator 限制明列。 |
| 英文翻譯與術語品質 | NEEDS HUMAN REVIEW | 英文工作譯稿已按繁中對齊，未由雙語電影編輯校譯。 |
| 網站建置與路由 | PASS | `npm --prefix apps/web run check` 0 errors/warnings/hints；Astro build 123 pages；雙語 CH06 頁各 32 個唯一 ID。首次同步後曾見短暫 loader duplicate-ID console 訊息，重跑與最終 build 無警告且實際路由 IDs 唯一。 |
| DOCX/PDF/EPUB 草稿 | PASS | `tmp/CH06-draft-20261021-r2/` 產生中英 DOCX/PDF/EPUB 六檔；DOCX CRC PASS 各 16 members，EPUB CRC PASS 各 9 members。 |
| PDF 字型嵌入／繁中渲染 | PASS | strict `scripts/check_fonts.py --require-pdffonts --font "Microsoft JhengHei"` 中英各 7 個字型列全部 emb/sub/uni=yes；PyMuPDF 抽字無 U+FFFD；中英首頁及末頁 proof 已目視，未見截切。 |
| EPUBCheck | PASS | EPUBCheck 5.4.0 中英各 0 errors、0 warnings、0 informationals、0 references；UTF-8／書目與雙語文字檢查通過。 |
| 自動測試及專案 validator | PASS | V2 validator PASS；project validator PASS（12 parts/60 chapters/52 terms/45 references）；完整 unit tests 51/51 PASS；CH06 專項 3/3 PASS；site sync check PASS；`git diff --check` exit 0（有既有 LF/CRLF 提示）。 |
| 作者／專業簽核 | NEEDS HUMAN REVIEW | 依作者指示留待全書章節完成後集中審查；不得標為 approved。 |

## 人工待辦

1. 電影敘事專業審稿：按作者指定版次核對 Aristotle 與 Bordwell 的具體主張及 locator。
2. 作者合法觀看《羅生門》所選版本，補記版本、字幕、片長和可重現 timecode，或把鏡頭級分析維持排除。
3. 雙語編輯校譯；術語編輯核准八組詞條。
4. 製作原創可編輯 SVG 因果圖／資訊揭露矩陣，記錄繪製方法、hash、作者歸屬、雙語 caption/alt，並完成權利、相似性、無障礙及出版審查。
5. 作者及相關電影研究／編劇專業審查（全書完成後集中）。

人工簽核欄位清單：`assets/chapters/CH06/CH06-HUMAN-REVIEW-CHECKLIST.md`。

## 草稿建置與測試

草稿輸出：`tmp/CH06-draft-20261021-r2/`。工具：Pandoc 3.12.1、MiKTeX XeLaTeX（本機 MiKTeX bin）、EPUBCheck 5.4.0、Astro 專案鎖定依賴。自動檢查與頁面／字型／EPUB 證據見 `production/runs/CH06/20261021T065143+0800-f153e02e/verification.json` 及 build logs。一次性初始 build script 在本 PowerShell PATH 找不到 Pandoc 而失敗；修正為實際安裝路徑後六個出版草稿全數建置成功。完整測試 51/51 pass。

## 草稿素材包

雙語章稿、metadata 快照、研究備忘、驗收報告、觀看紀錄模板、單元測試、build logs、DOCX/PDF/EPUB、頁面 proof、run scripts 與備份證據封裝於 `tmp/CH06-draft-20261021-r2/CH06-Codex-Materials-DRAFT-r1.zip`。`OUTPUT-MANIFEST.json` 列出封包成員、CRC 及 SHA-256；該包仍是未核准草稿。

## 判定

CH06 已由空白 scaffold 形成雙語研究草稿，並完成本機網站與 DOCX/PDF/EPUB 技術草稿、strict PDF 字型和 EPUBCheck 驗證；來源全文定位、電影觀看片段、原創插圖及人工校譯待辦未結。**CH06 尚未達正式出版標準。**
