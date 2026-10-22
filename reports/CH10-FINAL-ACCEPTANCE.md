# CH10 驗收報告｜劇本格式、改編與版本管理

- 日期：2026-10-22（Asia/Taipei）
- 版本：2.1.0-draft
- 狀態：**雙語研究草稿與本機出版工程草稿完成；未達正式出版標準。**
- Run：`production/runs/CH10/20261022T062041+0800-d6ab6deb/`
- 編輯前備份：`production/runs/CH10/20261022T062041+0800-d6ab6deb/backup/pre-edit/MANIFEST.json`（13 個檔案；備份 SHA-256 逐檔比對 13/13 通過）
- 本機草稿：`tmp/CH10-draft-20261022-r3/`。未發布網站、未 commit、未 push，未開始 CH11。

## 驗收總表

| 項目 | 狀態 | 證據／限制 |
|---|---|---|
| 既有工作區與未提交內容 | PASS | 執行前 `git status` 保存在 run 目錄；所有既有 CH01–CH09 修改及未追蹤素材均保留。只製作 CH10。 |
| 編輯前備份 | PASS | Manifest 記錄 13 個原始稿、章節／翻譯／術語／來源／圖片登錄、歷史、矩陣及進度表；備份雜湊比對 13/13 相符。 |
| 繁中稿 | PASS（研究草稿） | `content/zh-TW/chapters/CH10-chapter-10.md`；S01–S12 有實質文字，含目標、先備知識、原理、傳統流程、AI 限制、工作流、提示詞、案例、驗證、練習與來源。 |
| 英文稿 | PASS（工作譯稿） | `content/en-US/chapters/CH10-chapter-10.md`；S01–S12 與中文錨點相同。英文正式章名及語言校譯仍待核准。 |
| 翻譯逐節對照 | PASS（結構） | `metadata/translations/CH10-alignment.yaml`；12 個節次、術語與圖號已登錄，狀態 `review-needed`。 |
| 術語 | PASS（草案登錄） | `metadata/terminology.yaml` 新增 8 個雙語草案；定義、首選譯名和跨章用語待術語編輯審核。 |
| 正式來源 | PASS（來源頁核對） | R070–R076 已登錄 `data/references.yaml` 與 `metadata/references.bib`；來源和主張範圍記於 `assets/chapters/CH10/CH10-SOURCE-AND-CASE-NOTES.md`。外部連結格式檢查 73 個 URL 通過；正式出版前仍需再確認可達性及法域。 |
| 電影案例 | PARTIAL / NEEDS HUMAN REVIEW | AFI Catalog 支持《The Wizard of Oz》（1939）與 1900 年小說的關聯及其片目／製作史資料。尚無專案觀看片源、底本版次、頁碼、鏡頭時間碼或逐場景比較。 |
| 原創圖稿 | PASS（檔案及結構） | 3 張手工編寫、可編輯 SVG，圖號 CH10-FIG-001–003；manifest、雙語圖說／alt、尺寸、SHA-256 與權利欄位已同步。未使用第三方圖片、電影劇照或圖像生成服務。 |
| 圖稿權利與署名 | NEEDS HUMAN REVIEW | 三圖 `asset_approved: null`、`approval_status: pending`，出版目標均 pending。作者署名、相似性、可及性、技術品質及出版授權未簽核。 |
| 圖片與章節狀態登錄 | PASS | `metadata/figure-registry.yaml`、`data/assets.yaml`、`assets/chapters/CH10/figure-manifest.yaml`、雙語正文圖號及圖說一致；SHA-256 自動比對通過。 |
| V2 驗證 | PASS | `python scripts/v2_validate.py`：12 篇、60 章 registry、舊版雜湊及圖像政策通過。 |
| 專案驗證 | PASS | `python scripts/validate_project.py`：60 章登錄、52 個術語、71 筆來源及雙語 canonical 檔格式通過。 |
| CH10 測試 | PASS | `python -m unittest tests.test_ch10_content -v`：4/4 通過，涵蓋 S01–S12 對齊、8 詞條、來源、3 張 SVG/hash/權利狀態與非佔位正文。 |
| 全套測試 | PARTIAL | `python -m unittest discover -s tests -v`：74 項中 73 通過，1 項既有 CH01 錯誤：`tests/test_ch01_content.py` 因 CH01 一筆術語資料缺少 `status` 欄位而出現 `KeyError: 'status'`。本章未修改 CH01。 |
| 網站內容同步 | PASS | `python scripts/publishing/sync_site_content.py --check` 通過；雙語章稿與本機圖資同步。 |
| Astro 型別檢查 | PASS | `npm --prefix apps/web run check`：0 errors、0 warnings、0 hints。最終檢查未出現重複 ID 警告。 |
| Astro 建置 | PASS | `npm --prefix apps/web run build`：123 頁建置完成。未部署。 |
| 網站頁面／錨點／圖片 | PASS | 建置後中英文 CH10 route 各有 38 個唯一 HTML id、3 張本機圖片，所有圖片均有非空 alt。 |
| DOCX 草稿 | PASS | 中文及英文各成功輸出至 r3。 |
| PDF 草稿及字型 | PASS（嵌入檢查） | 中文 8 頁、英文 10 頁；Microsoft JhengHei 與 Times New Roman 的 pdffonts 嵌入檢查均通過（各 16 個字型項目）。已抽看圖頁並修正 SVG 標題對比。視覺校樣仍待人工確認。 |
| PDF 字型問題紀錄 | PARTIAL / RESOLVED FOR THIS BUILD | r1 使用 Noto Serif TC 時，MiKTeX/dvipdfmx 回報 `Invalid font: -1 (0)`，MiKTeX log 記錄 `fwrite` invalid argument，且字型有缺字警告。改用已安裝且已嵌入的 Microsoft JhengHei 後 r3 中英文 PDF 成功。Noto Serif TC 根本原因仍待另行排查；本章出版草稿使用替代字型。 |
| EPUB 草稿 | PASS（格式檢查） | 中文及英文 EPUB 均成功輸出；EPUBCheck 3.4 各報 0 fatal errors、0 errors、0 warnings；ZIP CRC 及雙語內容抽查通過。 |
| 編輯／法律／作者簽核 | NEEDS HUMAN REVIEW | 依作者安排，雙語校譯、電影專業審稿、權利法律確認與作者簽核留待全書完成後集中處理。章節和圖稿不是 publication-ready。 |

## 來源與範圍

- R070 Academy Nicholl：格式指引及美國專業寫作者格式存在差異的說明。
- R071 WGAW Registry：其登記服務紀錄作者主張，並說明不取代美國著作權局登記；此內容不構成法律意見。
- R072 U.S. Copyright Office Title 17：只用於美國法條的衍生作品範圍概述；不可外推至其他法域。
- R073–R074 Final Draft 官方文件：修訂模式及鎖頁工具；產品文件不代表所有劇組的做法。
- R075 Fountain 語法規格：只驗證規格頁所述文字語法；本專案未做不同編劇軟體的互轉實測。
- R076 AFI Catalog：影片／小說關聯及製作史線索；不能替代觀片、劇本全文或權利審查。

以上來源頁於 2026-10-22 查閱。專書頁碼、作者採用的本地法律、電影版本與時間碼、實際轉檔工具與版本，均保留人工核對。

## 人工審查清單

詳見 `assets/chapters/CH10/CH10-HUMAN-REVIEW-CHECKLIST.md`。至少需要作者核定章名及範圍、英文校譯、電影格式專業審稿、合法底本與影片版本的觀片記錄、法律專業權利確認、圖稿署名與權利核准、網站／PDF／EPUB 視覺校樣及作者簽核。

## 待辦與出版判定

1. 依 CH10 待人工審查清單完成全書階段安排的作者、雙語、電影專業及權利簽核。
2. 若需保留 Noto Serif TC，另以最小 XeLaTeX 文件重現 MiKTeX `fwrite`／`dvipdfmx Invalid font` 錯誤並查明根因；本次改用 Microsoft JhengHei 不等於修復原字型環境。
3. 後續統一修復既有 CH01 術語缺少 `status` 的全套測試錯誤。
4. 測試 Fountain／FDX 或實際採用的編劇軟體格式互轉，並登錄軟體版本和差異。

**CH10 是否達正式出版標準：否。** 目前完成的是中英文研究草稿、素材登錄和本機格式技術檢查；來源定位、觀片、雙語校譯、法律／權利、圖稿核准與作者校樣仍有明確待辦。
