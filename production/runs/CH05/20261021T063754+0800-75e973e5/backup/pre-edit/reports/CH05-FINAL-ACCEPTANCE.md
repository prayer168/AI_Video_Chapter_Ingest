# CH05 Final Acceptance｜類型、再現與影視倫理

- 日期：2026-10-20（Asia/Taipei）
- 版本：2.1.0-draft
- 狀態：draft / review-needed；不是 publication-ready
- Pipeline run：`production/runs/CH05/20261020T225328+0800-59388910/`
- 備份：`backups/CH05-start-20261020-225446`；SHA-256 清單見 run 目錄 `backup-sha256.txt`。
- 工作區基準：main branch；本輪開始前存在未提交 CH04 變更，均予保留，沒有 commit/push/deploy。

## 本輪交付

- 中英文 canonical 草稿，各 13 個共用 section IDs；英文稿未人工校譯。
- 8 個雙語章節術語、R039–R044 來源紀錄與 translation alignment。
- 2 張可編輯 SVG、雙語標題／圖說／alt、figure manifest、全域 figure/asset 登錄；權利狀態 pending。
- 雙語網站建置與 DOCX/PDF/EPUB 本機草稿，位於 `tmp/CH05-draft-20261020-r1/`。
- 章節測試、備份 hash、history/run 日誌。

## 全項目稽核

| 必要項目 | 狀態 | 證據 | 待辦／責任角色 |
|---|---|---|---|
| 學習目標 | PASS | Both locale files contain observable outcomes; CH05-S01. |  |
| 先備知識 | PASS | Both locale files identify CH01–CH04 prerequisite; CH05-S02. |  |
| 專業名詞中英文對照與定義 | PASS | 8 bilingual TERM-CH05 records; `metadata/terminology.yaml`; CH05-S03. |  |
| 電影製作歷史與基本原理 | NEEDS HUMAN REVIEW | CH05-S04 cites R039/R040; Altman full text and Hall adopted chapter/page locator not verified. | Film scholar checks theory and edition/page locators. |
| 傳統電影製作方法 | NEEDS HUMAN REVIEW | Draft workflow in CH05-S05; professional production/editor review pending. | Production editor validates consent and safeguarding recommendations by jurisdiction. |
| AI 時代技術轉換、能力與限制 | NEEDS HUMAN REVIEW | CH05-S06 cites UNESCO R042 as high-level guidance; no model-specific claims; specialist review pending. | AI production/privacy/rights review. |
| 詳細工作流程 | PASS | Eight explicit steps in both language drafts; CH05-S07; alignment IDs in CH05-alignment.yaml. |  |
| 提示詞與技術參數（含版本／未實測聲明） | NEEDS HUMAN REVIEW | Model-neutral demonstration and explicit no-parameter fabrication statement; CH05-S08. No model/version run. | Choose a model and reproduce prompt only if later authorized. |
| 實際鏡頭／影片案例與來源 | NEEDS HUMAN REVIEW | Get Out identity/year verified against BFI R044; no edition, viewing log, shot claim, or timecode. BFI framework R043 is cited as an institutional teaching example. | Author selects lawful edition and views; film scholar checks analysis. |
| 常見錯誤與品質驗證 | PASS | Six named failure patterns plus audit record checklist in CH05-S10. |  |
| 練習與評量 | PASS | Two exercises and 0–10 rubric in CH05-S11. |  |
| 延伸研究 | PASS | Three bounded research directions in CH05-S11. |  |
| 主張分類及引用可追溯性 | NEEDS HUMAN REVIEW | R039–R044 exist in `data/references.yaml` and `metadata/references.bib`; selected sources are catalogue/abstract/framework only. | Verify each substantive claim against full sources. |
| 中英文節次、穩定 ID、術語、案例和圖號逐項對齊 | PASS | 13 matching anchors; 8 stable terms; 2 figures; `metadata/translations/CH05-alignment.yaml`; automated test. |  |
| 中英文語意、單位、引用位置及專業用語編輯狀態 | NEEDS HUMAN REVIEW | English translation follows zh-TW sections and source IDs; not proofread or approved. | Bilingual film editor reviews. |
| 來源存在、版本／日期／頁碼或 locator 已核對 | NEEDS HUMAN REVIEW | R039–R044 recorded with URLs/date/status; R039 abstract only; R040 publisher metadata only; page locators incomplete. | Source editor checks adopted editions and locators. |
| 電影案例版次、合法觀看來源與 timecode | NEEDS HUMAN REVIEW | No selected streaming/disc edition or timecode claimed. | Author/film researcher supplies viewing record. |
| 原稿及素材備份、差異與保留情形 | PASS | CH05 start backup: `backups/CH05-start-20261020-225446`; hashes in run `backup-sha256.txt`; V1 and CH01–CH04 unchanged by scope. |  |
| 圖片／SVG 原檔、hash、生成或繪製紀錄 | PASS | 2 editable hand-authored SVGs with recorded SHA-256, method, date, and production log in chapter/global manifests. |  |
| 圖號、雙語標題／圖說／alt 與正文位置 | PASS | CH05-FIG-001/002 mapped to 5-1/5-2; bilingual caption file, manifest, alt and manuscript references. |  |
| 圖片權利、相似性、肖像及標誌人工審查 | NEEDS HUMAN REVIEW | Original schematic contains no third-party imagery; creator attribution, accessibility and publication-rights review pending. | Author confirms creator/rights; visual editor approves. |
| SVG 技術正確性、可編輯性、可及性及印刷檢視 | NEEDS HUMAN REVIEW | SVGs render into PDF previews via Inkscape; no third-party raster images. Human contrast/accessibility/print proof pending. | Visual/accessibility editor inspects source and print proof. |
| 中英文網站路由、內容、ID、圖檔及 alt | PASS | Astro build 123 pages; `/en/ch05-chapter-05/` and `/zh-tw/ch05-chapter-05/`; local assets synced; route spot-check pending below. |  |
| DOCX 草稿建置與內嵌素材 | PASS | Pandoc 3.12.1 built both DOCX files; Python ZIP CRC passed and each contains 2 embedded figure media files (see verification.json). |  |
| PDF 建置、字型嵌入及繁中實際渲染 | PASS | XeLaTeX/MiKTeX PDF built both locales; PyMuPDF extracted nonempty font streams including Microsoft JhengHei/Times New Roman; 0 U+FFFD; figure page rendered and visually inspected. `pdffonts` CLI unavailable, so repo strict checker remains BLOCKED. | Do final page-by-page proof; install/use pdffonts for independent strict gate. |
| 中英文 EPUB 結構、雙語顯示及 EPUBCheck | PASS | EPUBCheck 5.4.0 both locales: 0 errors/warnings/informationals/references; package/media spot-check recorded. |  |
| 連結檢查及網路不確定項目 | NEEDS HUMAN REVIEW | Local references registered; web link checker result recorded in run log; time-sensitive BFI event and full text access limitations remain. | Recheck source URLs and access/edition before publication. |
| 單元、整合、專案結構與出版品質測試 | PASS | CH05 tests 3/3; full unittest suite 47/47 passed; V2/project validators and Astro check/build recorded. |  |
| registry、翻譯狀態及章節 metadata 同步 | PASS | Chapter, translation, terms, references, figures, assets and site projection synced; V1 approval unchanged. |  |
| run log、history、備份 manifest 與重現指令 | PASS | Run directory has checkpoint, backup hash list, build scripts, logs; history appended before handoff. |  |
| 作者／專業審稿人／權利核准狀態 | NEEDS HUMAN REVIEW | No author, bilingual, film studies, community, legal, or visual sign-off recorded; both locale statuses review-needed. | Consolidated review after all chapters per author instruction. |
| 未發布網站、未推送等授權邊界（如適用） | PASS | Local static build only; no deployment, commit, or push performed. |  |

## 草稿素材包

- `tmp/CH05-draft-20261020-r1/CH05-Codex-Materials-DRAFT-r3.zip`：包含雙語稿、來源／術語、原創 SVG、驗收報告和 DOCX/PDF/EPUB 草稿。
- r2 的 `CH05-sources.yaml` 曾因來源 ID 篩選格式錯誤而為空；r3 已修正為 R039–R044 六筆來源紀錄。此修正僅修復交付包索引，不改變 canonical references registry 或正文。
- `tmp/CH05-draft-20261020-r1/OUTPUT-MANIFEST.json` 記錄 r3 package SHA-256、輸出檔案雜湊和 CRC 結果；r1、r2 原始 ZIP 均保留。

## 測試摘要

- 狀態統計：PASS 19；FAIL 0；BLOCKED 0；NEEDS HUMAN REVIEW 13；NOT RUN 0。
- 完整測試輸出、網站路由 DOM/ID/alt 核對、DOCX media CRC、EPUBCheck、PDF font extraction/render、檔案 SHA-256 與 tool versions 另存 run logs/OUTPUT-MANIFEST。
- `python scripts/v2_validate.py` PASS；`python scripts/validate_project.py` PASS；網站投影 check PASS；unit tests 47/47 PASS；Astro check 0 errors/warnings/hints；Astro static build 123 pages PASS；`git diff --check` exit 0 (pre-existing CH04 LF/CRLF notices). Link scan 0 failures, 0 network-tested, 5 inconclusive.
- 正式全書 build gate 未執行：全書 60 章未核准；本輪只做單章草稿。

## 最終判定

CH05 雙語草稿與可自動執行的章末檢查已完成；**尚未達正式出版標準**。主要缺口是英文編輯校譯、理論全文與精確 locator、合法電影版本及看片紀錄、社群／法律／倫理專業審查、圖片作者及權利/可及性核准、最終逐頁校樣和作者簽核。依作者指示，集中人工審核留至全書完成後。此後停止；不自動開始 CH06。

