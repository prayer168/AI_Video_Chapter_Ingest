# CH06 Final Acceptance｜故事、情節與因果結構

- 日期：2026-10-21（Asia/Taipei）
- 版本：2.1.0-draft
- 狀態：draft / review-needed；不是 publication-ready
- Run：`production/runs/CH06/20261021T164101+0800-10139b29/` (continuation; original baseline run retained)
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

## 2026-10-21 CH06 continuation audit — latest status

本節為最新證據，取代上方前次 run 對「尚無原創圖」與未更新出版輸出的描述。版本仍為 `2.1.0-draft`；本章尚未獲人工核准，不能視為正式出版完成。

| 本輪項目 | 狀態 | 實測證據 |
|---|---|---|
| 可定位的電影敘事理論來源 | PASS | 新增 R051 David Bordwell, “Three Dimensions of Film Narrative,” 作者公開 *Poetics of Cinema* 第 3 章；“Narration and story” 印刷 pp. 14–15（PDF pp. 13–14）。中英文正文、data/references、BibTeX 與 alignment 同步。R047 保留書目參考，不將未讀專書內容當成已查證主張。 |
| CH06-FIG-001 原創因果圖 | PASS（檔案與資料）／NEEDS HUMAN REVIEW（權利與出版） | 可編輯透明 SVG、1200×480、SHA-256 及雙語標題／圖說／alt 已登錄；置於 S07 後；未用劇照、第三方圖或生圖服務。rights、個人作者歸屬、可及性和出版核准仍 pending。 |
| CH06-FIG-002 故事時間／呈現順序圖 | PASS（檔案與資料）／NEEDS HUMAN REVIEW（權利與出版） | 可編輯透明 SVG、1200×560、SHA-256 及雙語標題／圖說／alt 已登錄；置於 S09 後；只用 A/B/C 抽象符號，非特定電影場景。rights、作者歸屬、可及性和出版核准仍 pending。 |
| 中英文圖文同步 | PASS | 兩語均使用永久 ID CH06-FIG-001/002 與圖號 6-1/6-2；`assets/chapters/CH06/figure-manifest.yaml`、`metadata/figure-registry.yaml`、`data/assets.yaml`、`figure-captions.md`、`CH06-FIGURE-RIGHTS-AND-SOURCES.md`、translation alignment 及 Lua caption map 已同步。 |
| 網站 | PASS（本機草稿） | Astro check 0 errors/warnings/hints；build 123 pages；中英文 CH06 route 各顯示本章兩張圖、具 alt、無重複 HTML IDs；site sync check PASS。未發布。 |
| DOCX | PASS（草稿） | 中英文各一份；各含 2 個 `word/media` 媒體項；檔案位於 `tmp/CH06-draft-20261021-r4/`。 |
| PDF | PASS（草稿技術檢查） | XeLaTeX 以 Inkscape 將原 SVG 轉成暫存向量 PDF 後排版；原 SVG 未變更。繁中及英文 PDF 嚴格字型檢查各 14 個字型項目，`emb/sub/uni=yes`；PyMuPDF 抽字 0 replacement character；圖頁 proof 已渲染。 |
| EPUB | PASS（格式草稿） | EPUBCheck 5.4.0 中英文各 0 errors、0 warnings、0 informationals、0 references；每本含 2 張 SVG 與 alt。 |
| 出版建置器 SVG 支援 | PASS | `scripts/publishing/build_books.py` 加入原始素材雜湊命名暫存與 Inkscape SVG→vector-PDF staging；新增回歸測試。首次失敗輸出/log 留存於 r3，成功輸出與 logs 在 r4。 |
| 專案結構／測試 | PASS | `scripts/v2_validate.py` PASS；`scripts/validate_project.py` PASS（12 parts、60 planned chapters、2 canonical chapter files、52 terms、46 references）；全套 unittest 55/55 PASS，CH06 專項 7/7。 |
| 公開出版權利閘門 | BLOCKED（預期） | 兩圖 `rights_review`、`editorial_review`、`asset_approved`、`approval_status` 均 pending。`image_policy.py` 目標出版檢查必須拒絕；本機草稿網站／檔案建置不是授權發布。 |
| 《羅生門》版本與鏡頭定位 | NEEDS HUMAN REVIEW | 仍需作者選合法版本實看，填 `assets/chapters/CH06/CH06-RASHOMON-VIEWING-LOG.md` 的版次、字幕、片長及 timecodes；稿件沒有宣稱未親看的鏡頭事實。 |
| 雙語編輯、術語與理論審校 | NEEDS HUMAN REVIEW | 英文仍為工作譯稿；R046 中譯術語、R047 專書全文主張、電影案例詮釋及 8 個術語均保留人工校核。依作者決策，人工簽核留至全書完成後集中辦理。 |
| 作者／專業核准 | NEEDS HUMAN REVIEW | 尚無作者出版核准；不得標示 `publication-ready`。 |

### 輸出與證據位置

- 最新雙語出版草稿：`tmp/CH06-draft-20261021-r4/`；r2 舊包與 r3 首次錯誤試作均保留。
- 本輪圖片權利紀錄：`assets/chapters/CH06/CH06-FIGURE-RIGHTS-AND-SOURCES.md`。
- 重現建置命令：`production/runs/CH06/20261021T164101+0800-10139b29/build_ch06_draft_outputs.py`；各格式 log 在 r4。
- 前編輯備份與 SHA-256：`production/runs/CH06/20261021T164101+0800-10139b29/backup/pre-edit/`。

**判定：** CH06 可由 Codex 執行的原創圖、來源定位、雙語素材同步、網站、DOCX/PDF/EPUB 草稿及自動檢查缺口已完成；仍是可供審閱的草稿，未達正式出版標準。全書集中人工審核前，不簽核 CH06，也不進入 CH07。


### Package and publication gate

- Final non-overwriting package: `tmp/CH06-draft-20261021-r4/CH06-Codex-Materials-DRAFT-r5.zip` (60 members; CRC PASS; SHA-256 recorded in `PACKAGE-CHECKSUM-r5.json`). The earlier r2 package is retained.
- `image_policy.py` publication gate was executed for zh-TW-book, en-book, zh-TW-site and en-site. All remain BLOCKED by unresolved project image approvals/rights/attribution, including CH06's pending status; this is expected and prevents publication. These failures are retained in the continuation run logs. Local draft generation does not bypass this gate.


### SVG publication-gate correction

書籍建置器依素材類型檢查 provenance：有作者核准的手繪 SVG 以繪製方法及製作紀錄驗證；AI 點陣圖仍要求 tool/version/date/prompt file。新增回歸測試確認此差異；CH06 兩圖的實際 rights 欄位維持 pending，出版閘門依然 BLOCKED。該規則不會自動核准任何圖片。
