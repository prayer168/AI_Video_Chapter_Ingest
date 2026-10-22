# CH05 Final Acceptance｜類型、再現與影視倫理

- 日期：2026-10-21（Asia/Taipei）
- 版本：2.1.1-draft
- 狀態：draft / review-needed；不是 publication-ready
- Pipeline run：`production/runs/CH05/20261021T063754+0800-75e973e5/`
- 備份：原始章節起始快照 `backups/CH05-start-20261020-225446`；本輪各修改檔 pre-edit 快照與 SHA-256 見 `production/runs/CH05/20261021T063754+0800-75e973e5/backup/pre-edit/MANIFEST.json`。
- 工作區基準：main branch；本輪開始前存在未提交 CH04 變更，均予保留，沒有 commit/push/deploy。

## 本輪交付

- 中英文 canonical 草稿，各 13 個共用 section IDs；2026-10-21 更新來源定位、案例來源、版次限制與雙語引用清單；英文稿未人工校譯。
- 8 個雙語章節術語、R039–R045 來源紀錄與 translation alignment。
- 2 張可編輯 SVG、雙語標題／圖說／alt、figure manifest、全域 figure/asset 登錄；權利狀態 pending。
- 雙語網站建置與 DOCX/PDF/EPUB 本機草稿，最新輸出位於 `tmp/CH05-draft-20261021-r3/`。
- 章節測試、備份 hash、history/run 日誌。

## 全項目稽核

| 必要項目 | 狀態 | 證據 | 待辦／責任角色 |
|---|---|---|---|
| 學習目標 | PASS | Both locale files contain observable outcomes; CH05-S01. |  |
| 先備知識 | PASS | Both locale files identify CH01–CH04 prerequisite; CH05-S02. |  |
| 專業名詞中英文對照與定義 | PASS | 8 bilingual TERM-CH05 records; `metadata/terminology.yaml`; CH05-S03. |  |
| 電影製作歷史與基本原理 | NEEDS HUMAN REVIEW | R039：JSTOR 書目、摘要與 pp. 6–18 篇幅於 2026-10-21 複核；摘要支持語義／句法取徑。R040：Google Books 目錄定位 Hall 章自 p. 13 起、下一章 p. 75 起；正文已標明西部片例為本章示範，並把 Hall 問句標成實務提問。逐主張的全文頁碼定位仍待核。 | 電影理論審稿者按採用版次核對全文主張／頁碼。 |
| 傳統電影製作方法 | NEEDS HUMAN REVIEW | Draft workflow in CH05-S05; professional production/editor review pending. | Production editor validates consent and safeguarding recommendations by jurisdiction. |
| AI 時代技術轉換、能力與限制 | NEEDS HUMAN REVIEW | CH05-S06 cites UNESCO R042 as high-level guidance; no model-specific claims; specialist review pending. | AI production/privacy/rights review. |
| 詳細工作流程 | PASS | Eight explicit steps in both language drafts; CH05-S07; alignment IDs in CH05-alignment.yaml. |  |
| 提示詞與技術參數（含版本／未實測聲明） | PASS | CH05-S08 明確標示模型中立教學示範、未驗證工具命令；未宣稱實測模型功能或參數，並要求未測欄位記為未測。此列驗收的是範例標示完整，不宣稱有模型實測。 |  |
| 實際鏡頭／影片案例與來源 | NEEDS HUMAN REVIEW | 新增 R045：BFI《Sight and Sound》Trevor Johnston 具名影評，支持其二手類型／主題解讀；R044 仍只支持片目 metadata。章內未假稱本書作者看片，已建立 `assets/chapters/CH05/CH05-GET-OUT-VIEWING-LOG.md`。 | 作者／研究者選合法版次、看片並填可重現 locator；電影研究者審核分析。 |
| 常見錯誤與品質驗證 | PASS | Six named failure patterns plus audit record checklist in CH05-S10. |  |
| 練習與評量 | PASS | Two exercises and 0–10 rubric in CH05-S11. |  |
| 延伸研究 | PASS | Three bounded research directions in CH05-S11. |  |
| 主張分類及引用可追溯性 | NEEDS HUMAN REVIEW | R039–R045 均在 references YAML/BibTeX；英文／繁中 frontmatter 與正文來源 ID 已同步。R045 為二手影評；R039 主文未取得，R040 僅定位章節起訖；不能以書目登錄代替逐主張審閱。 | 來源編輯／電影理論審稿者核實每項實質主張。 |
| 中英文節次、穩定 ID、術語、案例和圖號逐項對齊 | PASS | 13 matching anchors; 8 stable terms; 2 figures; `metadata/translations/CH05-alignment.yaml`; automated test. |  |
| 中英文語意、單位、引用位置及專業用語編輯狀態 | NEEDS HUMAN REVIEW | English translation follows zh-TW sections and source IDs; not proofread or approved. | Bilingual film editor reviews. |
| 來源存在、版本／日期／頁碼或 locator 已核對 | NEEDS HUMAN REVIEW | 2026-10-21 直接查核 JSTOR R039 書目／摘要、Google Books R040 目錄、BFI R043 活動頁（標示 2026-11-27）、BFI R044 片目及新增 R045 影評；存取日期及限制已寫入 sources registry。R039 全文、R040 精確主張頁碼仍缺。 | 來源編輯核對指定採用版本與逐主張 locator。 |
| 電影案例版次、合法觀看來源與 timecode | NEEDS HUMAN REVIEW | No selected streaming/disc edition or timecode claimed. | Author/film researcher supplies viewing record. |
| 原稿及素材備份、差異與保留情形 | PASS | CH05 start backup: `backups/CH05-start-20261020-225446`; hashes in run `backup-sha256.txt`; V1 and CH01–CH04 unchanged by scope. |  |
| 圖片／SVG 原檔、hash、生成或繪製紀錄 | PASS | 2 editable SVG hashes unchanged; manifest/data.assets now accurately records Codex-assisted source authoring, date, no raster generation/third-party image, and that the original model/build/session and individual contributor identity were not captured. See `assets/chapters/CH05/figure-manifest.yaml`. |  |
| 圖號、雙語標題／圖說／alt 與正文位置 | PASS | CH05-FIG-001/002 mapped to 5-1/5-2; bilingual caption file, manifest, alt and manuscript references. |  |
| 圖片權利、相似性、肖像及標誌人工審查 | NEEDS HUMAN REVIEW | Original schematic contains no third-party imagery; creator attribution, accessibility and publication-rights review pending. | Author confirms creator/rights; visual editor approves. |
| SVG 技術正確性、可編輯性、可及性及印刷檢視 | NEEDS HUMAN REVIEW | SVGs render into PDF previews via Inkscape; no third-party raster images. Human contrast/accessibility/print proof pending. | Visual/accessibility editor inspects source and print proof. |
| 中英文網站路由、內容、ID、圖檔及 alt | PASS | Astro build 123 pages; `/en/ch05-chapter-05/` and `/zh-tw/ch05-chapter-05/`; generated routes each have 40 unique IDs and 2 local images with nonempty alt. An immediate post-sync check once logged transient duplicate-ID console warnings; an independent rerun returned 0 errors/warnings/hints, and built route IDs are unique. |  |
| DOCX 草稿建置與內嵌素材 | PASS | Pandoc 3.12.1 rebuilt both locales in `tmp/CH05-draft-20261021-r3/`; DOCX ZIP CRC PASS, each contains two embedded figure media files. Project-local Traditional Chinese labels loaded with no Pandoc locale warnings. |  |
| PDF 建置、字型嵌入及繁中實際渲染 | PASS | 新建 zh/en PDF 均由 `scripts/check_fonts.py --require-pdffonts` 實測通過；七列字型皆 `emb/sub/uni=yes`，繁中 Microsoft JhengHei 正常嵌入，抽字 0 U+FFFD。中文字型頁 3、5 與英文圖頁 5、7 已渲染並視覺抽查。`pdffonts.exe` 位於 MiKTeX bin；嚴格 gate 已不再 BLOCKED。 | 作者仍須全頁最終校樣。 |
| 中英文 EPUB 結構、雙語顯示及 EPUBCheck | PASS | 新建雙語 EPUB 均通過 EPUBCheck 5.4.0：各 0 errors/warnings/informationals/references；ZIP CRC PASS、雙語欄位及 figure media 均驗證。 |  |
| 連結檢查及網路不確定項目 | NEEDS HUMAN REVIEW | Repository checker：0 failures、0 network-tested、5 inconclusive。另 2026-10-21 以網頁工具直接讀取 BFI R043/R044/R045 與 Google Books R040；JSTOR R039 讀到書目／摘要，未取全文。外部連結整體可達性不能由本地掃描證明。 | 出版前重驗來源可達性、版本與存取權。 |
| 單元、整合、專案結構與出版品質測試 | PASS | CH05 tests 3/3；完整 unittest 48/48；V2 validator、project validator、網站 sync check PASS；Astro check 0 errors/warnings/hints、build 123 pages；雙語 EPUBCheck PASS；出版 smoke test zh/en EPUB+PDF PASS。 |  |
| registry、翻譯狀態及章節 metadata 同步 | PASS | Chapter, translation, terms, references, figures, assets and site projection synced; V1 approval unchanged. |  |
| run log、history、備份 manifest 與重現指令 | PASS | Run directory has checkpoint, backup hash list, build scripts, logs; history appended before handoff. |  |
| 作者／專業審稿人／權利核准狀態 | NEEDS HUMAN REVIEW | No author, bilingual, film studies, community, legal, or visual sign-off recorded; both locale statuses review-needed. | Consolidated review after all chapters per author instruction. |
| 未發布網站、未推送等授權邊界（如適用） | PASS | Local static build only; no deployment, commit, or push performed. |  |

## 草稿素材包

- 最新雙語 DOCX/PDF/EPUB 草稿位於 `tmp/CH05-draft-20261021-r3/`；PDF 嚴格字型檢查與 Pandoc zh-TW 本地化警告均已處理。
- 最新草稿章稿、DOCX/PDF/EPUB、頁面 proof、來源 R039–R045、看片記錄表、人工審查表、SVG 原稿及驗收證據封裝於 `tmp/CH05-draft-20261021-r3/CH05-Codex-Materials-DRAFT-r6.zip`；先前 ZIP 均保留。`OUTPUT-MANIFEST.json` 記錄 ZIP SHA-256 及 31 個成員雜湊。

## 測試摘要

- 狀態統計：PASS 20；FAIL 0；BLOCKED 0；NEEDS HUMAN REVIEW 12；NOT RUN 0。
- 完整測試輸出、網站路由 DOM/ID/alt 核對、DOCX media CRC、EPUBCheck、PDF pdffonts/font extraction/render、檔案 SHA-256、研究查證備忘與 tool versions 另存新 run logs／素材包 manifest。
- `python scripts/v2_validate.py` PASS；`python scripts/validate_project.py` PASS（40 references）；網站投影 check PASS；unit tests 48/48 PASS；Astro check 0 errors/warnings/hints；Astro static build 123 pages PASS；EPUBCheck zh/en 各 0 errors/warnings/informationals/references；PDF strict `pdffonts` 全字型 embed/subset/ToUnicode PASS；`git diff --check` exit 0（只有既有 CH04及文件 LF/CRLF 訊息）。Link scan 0 failures、0 network-tested、5 inconclusive。
- 正式全書 build gate 未執行：全書 60 章未核准；本輪只做單章草稿。

## 最終判定

CH05 雙語草稿與本輪可自動執行的章末檢查已完成；**尚未達正式出版標準**。剩餘集中人工審查包括英文校譯、Altman 全文與 Hall 採用版次逐主張頁碼定位、合法電影版本及看片紀錄、倫理／法律／社群專業審查、兩張 SVG 個別貢獻者與權利／相似性／可及性及印刷核准、全頁校樣和作者簽核。依作者指示留至全書集中審查；本次使用者另行要求先完成 CH05 再接續 CH06，故此報告只記錄 CH05 未核准草稿狀態，不代表出版核准。

