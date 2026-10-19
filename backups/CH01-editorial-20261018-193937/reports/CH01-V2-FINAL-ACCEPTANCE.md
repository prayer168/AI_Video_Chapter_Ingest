# CH01 V2 整合與最終驗收報告

- 驗收日期：2026-10-18（Asia/Taipei）
- 狀態：**未正式完成；目前為可編輯的雙語整合草稿**
- 整合差異及來源盤點：[CH01-V2-INTEGRATION-DIFF.md](CH01-V2-INTEGRATION-DIFF.md)
- 修改前備份：`backups/CH01-V2-integration-20261018-132434/`（含 `MANIFEST.json` 與基線 SHA-256）
- 草稿格式預覽：`tmp/CH01-V2-draft-preview/`（PDF、EPUB、抽取文字、首頁 PNG 與建置輸出；不得當作正式出版物）

## 摘要

V2 雙語 CH01 中已整合五組經典電影案例、六個雙語術語草案、九筆新增來源，以及五份原創插圖需求 briefs。V1 原稿和來源素材未覆蓋、移動或刪除。章稿仍有大量空白模板段落，英文題名及兩語編輯審查未完成；五張插圖尚未生成。故本報告記錄的是整合驗收與技術 smoke test，不是內容定稿或正式出版核准。

## 驗收矩陣

| 項目 | 狀態 | 實測證據與限制 |
|---|---|---|
| 來源包與指令盤點 | PASS | `staging/CH01-V2/`、`staging/Homage-V1/` 遞迴檔案數均為 0；改讀專案內兩個 CH01 ZIP，依其 README／整合指令作業。ZIP 原件未解壓覆蓋。 |
| 原稿保護與修改前備份 | PASS | `backups/CH01-V2-integration-20261018-132434/MANIFEST.json` 保存 canonical 稿、registry、validator、報告、history 與來源 ZIP 的基線雜湊；V1 原稿未改動。 |
| 中英文案例配對 | PASS（結構） | 兩語各有 5 個對應案例，`CH01-P001`–`CH01-P005` 穩定 ID 一致。案例文字仍為草稿，版次／場景 timecode 待人工核實。 |
| 中英文術語與資料庫 | PASS（草案） | 六個 CH01 術語已進雙語章稿及 `metadata/terminology.yaml`；全專案驗證為 52 個術語。定義仍待編輯審閱。 |
| 參考資料與交叉引用 | PASS（部分） | R013–R021 有來源、存取日期及中英章稿條目；引用錨點已改為 Pandoc 支援的 span。外部連結檢查 0 failures、3 unchecked；電影理論的學術來源與場景定位需補強。 |
| 新增插圖的原創／權利管理 | BLOCKED | 五份原創 briefs 和雙語圖說／alt 已登錄；沒有生成圖片，也沒有任何項目獲權利、技術或編輯核准。CH01 V2 章稿目前未嵌入圖片，未使用網路第三方圖片。正式全書 image-policy gate 另被 V1 的 `ASSET-CH01-FIG-01` 權利狀態阻擋。 |
| 雙語網站型別檢查 | PASS | `npm --prefix apps/web run check`：0 errors／warnings／hints。 |
| 雙語網站建置 | PASS | 2026-10-18 重跑 `npm --prefix apps/web run build`：123 頁完成；輸出無 `Duplicate id`，中英文 CH01 路由存在；未部署。 |
| 中文 PDF 生成、字型嵌入與渲染 | PASS for draft technical gate | 中英文 PDF 均指定 Microsoft JhengHei CJK fallback 與 Times New Roman Latin。strict `pdffonts` 驗出字型嵌入，中文可抽取，首頁 PNG 視覺抽查正常；XeLaTeX 缺字警告數為 0。章節尚未核准，非正式出版版面。 |
| 英文 PDF 生成、字型嵌入與渲染 | PASS for draft technical gate | Times New Roman 及雙語術語所需的 Microsoft JhengHei 均通過 strict `pdffonts`；文字可抽取，缺字警告數為 0。寬表格已改為逐條詞條排版，抽查無重疊；正式全文仍需版面檢查。 |
| 中英文 EPUB 結構與 EPUBCheck | PASS for draft conformance | W3C／DAISY EPUBCheck 5.4.0 對兩語 draft EPUB 檢出 0 errors、0 warnings、0 informational messages、0 references；尚未做閱讀器相容性驗證。 |
| 章節編輯審查 | REVIEW NEEDED | Codex 初審已完成，發現 9 個必要章節區塊空白、英文稿未完成專業審校，案例仍缺觀看版次／timecode 及理論來源；退修清單見 [CH01 編輯與權利審查紀錄](CH01-EDITORIAL-AND-RIGHTS-REVIEW.md)。 |
| 插圖權利審查 | PENDING | 五項僅有 brief、沒有成品；正文沒有嵌入第三方圖片。V1 舊圖 `ASSET-CH01-FIG-01` 仍須查明權利或排除。 |
| 正式出版審批 | BLOCKED | 中文 CH01 `draft-migration-pending`，英文 `translation-needed`。正式 builder 因未核准狀態拒絕建置；此為預期保護 gate。 |
| 網站發布／GitHub 推送 | NOT PERFORMED | 本次未部署、未 commit、未 push。 |

## 已執行命令與測試

| 命令 | 結果 |
|---|---|
| `python scripts/v2_validate.py` | PASS |
| `python scripts/validate_project.py` | PASS；12 篇、60 個章節 ID、52 個術語、21 筆參考資料 |
| `python scripts/validate/check_links.py` | PASS；0 failures，3 外部 URL unchecked |
| `python -m unittest discover -s tests -v` | PASS；22/22 tests |
| `python scripts/publishing/sync_site_content.py --check` | PASS |
| `npm --prefix apps/web run check` | 0 errors/warnings/hints |
| `npm --prefix apps/web run build` | PASS；123 pages |
| `scripts/check_fonts.py --pdf <draft.pdf> --font <font> --require-pdffonts` | 中 PDF Microsoft JhengHei PASS；英 PDF Times New Roman PASS |
| EPUB ZIP／OPF／語文及正文自訂 smoke checks | 中英文均 PASS |
| `python scripts/image_policy.py --target zh-TW-book` / `--target en-book` | BLOCKED；V1 圖片未核准／授權未確認 |
| `python scripts/publishing/build_books.py --locale zh-TW --format pdf` | BLOCKED；CH01 未經編輯核准 |
| `python scripts/publishing/build_books.py --locale en-US --format epub` | BLOCKED；CH01 未完成翻譯審核 |
| `git diff --check` | PASS；僅回報工作樹既有 LF/CRLF 提醒 |

## 尚未通過與解決方式

1. **內容完成度**：依章節模板補齊學習目標、先備知識、歷史／理論、傳統方法、AI 技術轉換、詳細流程、提示詞與參數、常見錯誤、評量及延伸研究。保持中英段落 ID 成對，完成後由編輯審稿。
2. **電影案例核查**：記錄實際合法觀看版本、片段時間碼、鏡頭／場景描述與來源頁碼；增加正式電影研究來源支持概念性主張。不可僅憑二手評論替代鏡頭觀察。
3. **翻譯及術語審查**：決定英文正式章名，校對兩語案例語義，審閱術語定義及引用對應，更新 translation/editorial 狀態至 approved 前不可正式出版。
4. **原創圖像審查**：依 briefs 製作五張原創示意圖或可編輯 SVG；保存生成工具／版本／日期／提示詞和修改紀錄，完成權利風險、技術、編輯及中英文 caption／alt 核准，再納入正式章稿。
5. **網站 duplicate ID 訊息**：本輪重建 123 頁，無 Duplicate ID 訊息，兩語 CH01 路由均存在。建置未部署。
6. **完整書籍排版**：目前只測過 CH01 草稿。正文完整後仍需多頁視覺檢查目錄、長標題、註腳、參考資料、跨頁段落及字重；每次輸出需維持 0 缺字警告、strict `pdffonts` 嵌入及 `pdftotext` 字元完整。
7. **EPUB 正式符合性**：EPUBCheck 5.4.0 已安裝並通過雙語 CH01 draft；仍需待完整稿以閱讀器檢查 TOC、語言標籤、連結與中英字形。
8. **影像政策範圍**：確認 V1 圖片的權利資料與是否仍納入正式出版範圍；在任何正式 build 前清楚決定是否核准、替換或排除該 V1 資產，不能默認沿用。

## 下一步建議

先由 ChatGPT／編輯室依 `planning-v2/CH01-V2-WORKPLAN.md` 補齊 CH01 必要正文與英文專業審校，並逐項補電影版本、場景 timecode 及學術來源。Codex 已完成本輪初審，退修項目與插圖權利限制見 `reports/CH01-EDITORIAL-AND-RIGHTS-REVIEW.md`；正文與實際插圖審核完成後再跑完整出版 gate。只有所有編輯、權利及技術項目通過後，才把狀態升為正式完成。
