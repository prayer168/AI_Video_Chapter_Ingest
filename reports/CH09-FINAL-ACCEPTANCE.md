# CH09 驗收報告｜類型劇作、系列敘事與非線性結構

- 日期：2026-10-21（Asia/Taipei）
- 版本：2.1.0-draft
- 狀態：雙語研究草稿與出版工程草稿完成；**未達正式出版標準**。
- 工作目錄：`production/runs/CH09/20261021T204249+0800-1ab5afed/`
- 編輯前備份：`production/runs/CH09/20261021T204249+0800-1ab5afed/backup/pre-edit/MANIFEST.json`；已保存既有章節、metadata、登錄與全書追蹤檔案的 SHA-256。
- 出版草稿：`tmp/CH09-draft-20261021-r7/`；本機生成，未發布、未 commit、未 push。

## 驗收總表

| 項目 | 狀態 | 證據／限制 |
|---|---|---|
| CH09 原始中英文檔備份 | PASS | 編輯前 manifest 有兩語原稿及相關既有專案檔的 SHA-256；原始版本可從 run backup 還原。 |
| 繁中章稿 | PASS（研究草稿） | `content/zh-TW/chapters/CH09-chapter-09.md` 含 S01–S12、實質正文、案例、工作流程、提示詞／資料格式、練習及參考資料；仍待作者及專業審稿。 |
| 英文譯稿 | PASS（工作譯稿） | `content/en-US/chapters/CH09-chapter-09.md` 對應 S00–S12；英文校譯、文化語感和術語一致性仍 NEEDS HUMAN REVIEW。 |
| 雙語段落對照 | PASS（結構） | `metadata/translations/CH09-alignment.yaml`；自動測試確認 S01–S12 一致。 |
| 專業術語 | PASS（草案登錄） | 新增 9 筆 `TERM-CH09-*` 雙語草案；定義、首選譯名及跨章一致性待編輯核准。 |
| 參考來源 | PASS（來源入口） | R066–R069 登錄至 `data/references.yaml` 和 `metadata/references.bib`；連同既有 R051、R062 使用。書籍完整頁碼定位、期刊全文與理論詮釋待專業審查。 |
| 電影案例 | PARTIAL | 以《Memento》《Dunkirk》《The Wire》作研究討論入口並提供可追溯來源。未聲稱本專案觀看片源、版次或時間碼；需作者觀片補記。 |
| 原創圖稿 | PASS（草稿檔存在） | 三張手工編寫可編輯 SVG，具中英文圖說、alt text、圖號、尺寸、SHA-256、製作方法與權利欄位；未使用第三方圖像或電影劇照。 |
| 圖片權利與作者署名 | NEEDS HUMAN REVIEW | `asset_approved: null`、`approval_status: pending`、出版狀態 pending；需確認個人署名、授權、可及性與出版核准。 |
| V2 專案驗證 | PASS | `python scripts/v2_validate.py`；60 章登錄、雙語 scaffold、舊版雜湊與圖像政策檢查通過。 |
| 專案 validator | PASS | `python scripts/validate_project.py`；12 篇、60 章、雙語 canonical 檔、術語與參考登錄格式通過。 |
| CH09 單元測試 | PASS | `python -m unittest tests.test_ch09_content -v`：4/4 通過，驗證雙語錨點、術語／來源、圖稿 XML／SHA-256／狀態與非佔位內容。 |
| 全套單元測試 | PARTIAL | 70 個測試中 69 通過、1 個既有 CH01 測試錯誤：`tests/test_ch01_content.py` 讀取某 CH01 術語列時遇 `KeyError: 'status'`。錯誤與 CH09 無關，原始章節和術語未在本工作修改。 |
| 網站內容同步 | PASS | `python scripts/publishing/sync_site_content.py --check` 通過；期間發現既有同步器不會覆寫已存在但雜湊不同的生成圖片，已修正使非 check 同步會複製更新檔。 |
| Astro 網站建置 | PASS | `npm --prefix apps/web run build` 成功產生 123 頁；最後建置日誌未見 Duplicate ID 或 WARN。雙語 CH09 頁各含 3 張圖、3 個 alt，DOM id 無重複。 |
| DOCX 草稿 | PASS | zh-TW、en-US 各成功生成。 |
| PDF 草稿與字型 | PASS | 繁中 12 頁、英文 16 頁；`check_fonts.py --require-pdffonts` 均確認 Microsoft JhengHei 字型有嵌入；另已抽查圖頁，發現並修正 SVG 填色瑕疵後重建。 |
| EPUB 草稿 | PASS | zh-TW、en-US 均通過 EPUBCheck 5.4.0；檢查摘要 0 致命錯誤、0 錯誤、0 警告；ZIP CRC 完整。 |
| 作者與專業簽核 | NEEDS HUMAN REVIEW | 依作者先前安排保留至全書完成後集中簽核；所有 publication-ready 欄位仍 pending。 |

## 本次來源清單與使用範圍

- R066 Rick Altman, *Film/Genre*：出版社書目頁和目錄支持出版資訊及語義／句法／語用框架的範圍；非完整專書核讀。
- R067 Jason Mittell, *Complex TV*：NYU Press 書目頁支持專書範圍及列出的研究主題；詳細章節定位待核。
- R068 Artur Borowiecki (2024)：期刊頁、摘要及 DOI 可查；文章提出 plotline 術語需重新討論；不可當作全業界共識。
- R069 James Mottram, “Non-linear Nolan,” BFI, 2020-08-28：支持對《Memento》《Dunkirk》時間結構的概述；不代替本專案觀片和 timecode。
- R051 David Bordwell 與 R062 既有登錄來源沿用，採用範圍受既有 locator 限制。

## 必須保留的人工審查

詳見 `assets/chapters/CH09/CH09-HUMAN-REVIEW-CHECKLIST.md`。至少包含理論頁碼／完整文本定位、案例片源版次與時間碼、雙語校譯及術語、圖稿署名／權利／可及性、出版校樣與作者最終核准。未完成前不得改為 publication-ready。

## 已知非阻擋與限制

1. 本機網站為出版草稿工程驗證，不是公開部署。
2. DOCX/PDF/EPUB 均為 draft；字型嵌入及 EPUB 格式通過不代表人工視覺校樣完成。
3. 全套測試的唯一錯誤是 CH01 舊資料缺少術語 `status` 欄位；留給 CH01 後續修正，不在本章擅改。
4. 這些章稿不可宣稱出版完成；作者指示全部章節完成後才進行人工簽核。

## 草稿檔案 SHA-256

- `CH09-zh-TW-draft.docx` — `c28a65c05ed18b36b95ed9e33810dd18f34ec647ddb02f6b011cd24d5240faf7`
- `CH09-zh-TW-draft.pdf` — `ff94ffecf5967a9b7364eeca6fa92f1c115fd8a8830c92c266acb210c8fc4653`
- `CH09-zh-TW-draft.epub` — `3c51ec66faa61323ac8720273c64b738db09b21380f479fe1344de58dc0498a6`
- `CH09-en-US-draft.docx` — `1e7009c5021f39dd3d48a7b290981232491f1875e189e343fd12fa5f12d4cfee`
- `CH09-en-US-draft.pdf` — `2e4098e37e7093cbcb2307d911ec6005555e6f98db81fcabe23967ef92c6f2c1`
- `CH09-en-US-draft.epub` — `938e578d27997b2c600f42694053a86b4180fb93e648d3a8e5d0f4ebf7533c5d`
