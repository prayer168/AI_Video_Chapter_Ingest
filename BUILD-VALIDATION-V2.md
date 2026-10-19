# AI Video Bible V2.0 驗證報告

**日期：** 2026-10-18（Asia/Taipei）  
**驗證範圍：** Codex Skill frontmatter、V2 雙語資料模型、術語與翻譯狀態、圖片權利、網站投影、書籍建置和繁中字型 gate。  
**限制：** 僅安全修改專案內 V2 validator、出版 gate、字型檢查、metadata、測試與文件；沒有覆寫／刪除 V1 章稿或素材，未使用第三方網路圖片，未發布網站或推送 GitHub。

## 1. Codex Skill 檢查

使用者指定的 `C:\Users\user.codex\...` 路徑中，使用者名稱與 `.codex` 間疑似少了反斜線。本次檢查到的實際檔案為：

`C:\Users\user\.codex\skills\verify-content\SKILL.md`

- YAML frontmatter 有正確起始／結束 `---` 分隔線，並且是合法 mapping。
- `name: verify-content` 與 Skill 資料夾名稱一致；`description` 是非空字串，長度符合基本 metadata 範圍。
- Python `yaml.safe_load` 解析通過；正文 309 行，檔案及 `examples/`、`references/` 目錄均存在。
- 本次工作開始時，Codex Skill 清單已列出 `verify-content`，表示可被索引發現。
- **未修改 Skill，故未建立新備份。** 目錄中原已有 `SKILL.md.backup-20261018-114006`，保持不變。沒有發現可證實的 frontmatter 格式錯誤；因此不做無必要格式改寫。
- Skill 是否在目前已開啟的 Codex 工作階段立即重新載入，不能由檔案解析單獨保證；若警告仍顯示，重新載入／重啟 Codex 後再從 Skill 清單確認。

## 2. 架構與流程驗證

已重新閱讀：

- `BUILD-REPORT-V2.md`
- `planning-v2/ARCHITECTURE-V2.md`
- `planning-v2/CODEX-BOOTSTRAP.md`

| 項目 | 驗證結果 | 說明 |
|---|---|---|
| 雙語章節架構 | 通過 | `metadata/chapters.yaml` 與 `content/zh-TW`、`content/en-US` 各有 CH01–CH60；同章 ID 配對，節錨點一致。 |
| 翻譯狀態 | 通過並補強 | 每章兩語狀態存在且與檔案 frontmatter 相同；狀態 enum 納入 planned、draft-migration-pending 等實際值；英文草稿不得標為 approved。 |
| 術語管理 | 通過並補強 | `metadata/terminology.yaml` 是合法雙語詞條清單；新增 `schemas/term-v2.schema.json`，validator 核對 term ID、雙語首選詞／定義、參考 ID；核准詞條須有審校人和日期。目前詞條庫為空，屬待編輯資料，並非已完成術語內容。 |
| 原創插圖規範 | 通過 | 規範禁止網路圖直接出版；既有圖片政策測試涵蓋外部圖、未登錄圖與 pending 審核。V2 正式書籍 gate 另檢查本機檔案、alt、雙語 caption 及權利／技術／編輯核准；未建立圖或替任何缺圖找網圖。 |
| 中英文網站 | 部分通過 | canonical Markdown 對 Astro 120 頁的同步與一致性檢查通過。實際 `npm --prefix apps/web run build` 在同步後失敗，錯誤為 `astro` 未安裝／不在 PATH；未宣稱網站 build 成功。 |
| PDF／EPUB 出版 | EPUB smoke 通過；正式產物被 gate 阻擋 | 先前同日建置紀錄記載 Pandoc 3.12.1，CH01 暫存 EPUB 建立成功；本次重新驗證暫存檔 ZIP 完整（10 entries）。目前 shell 的 `where.exe pandoc` 無結果，無法重現建置器版本；正式中英文建置因章稿未 approved 而正確拒絕。 |
| 繁中 PDF 字型 | 嚴格 gate 已測；實際 V2 PDF 未驗 | Windows 有 Noto Serif TC 等繁中字型；先前紀錄提到 MiKTeX 初始化寫入權限問題。本次 shell 的 `xelatex`、`pdffonts` 均未能由 PATH 解析；沒有 V2 PDF 可供實測，不能宣稱字型嵌入成功。 |
| 參考連結 | 部分通過 | 本地 Markdown 連結 0 個失效；3 個外部 URL 未做連網查證，不能視為已確認有效。 |

## 3. 本次安全修復

1. 強化 `scripts/v2_validate.py`：實際解析 YAML，核對 12 篇、60 個永久章 ID、雙語稿件、翻譯狀態、段落錨點、術語引用及禁止遠端／inline 圖片。
2. 強化 `scripts/publishing/build_books.py`：正式輸出前檢查 60 章完整性、每章兩層的核准狀態、語言、占位文字；圖像需是本機已存在、登錄且經權利／技術／編輯核准，包含正確語言 caption/alt 和生成紀錄。正式 PDF 建成後會呼叫嚴格字型檢查。
3. 強化 `scripts/check_fonts.py`：新增 `--require-pdffonts`；正式 gate 遇檢查工具缺失、字型未嵌入、字型表不可解析或未找到要求的字型時均失敗，不會將「未能檢查」當成通過。
4. 新增術語資料 JSON Schema 和 [CH01 V2 工作清單／驗收規範](planning-v2/CH01-V2-WORKPLAN.md)。該文件只有編輯任務與驗收條件，不含大量章節正文或插圖。
5. 將建置過程、測試命令、失敗原因及後續工作寫入 `history.md`；更新建置報告測試數與已知限制。

## 4. 實際測試

| 命令／檢查 | 結果 |
|---|---|
| Skill frontmatter YAML parser | PASS；欄位／名稱／長度檢查通過，無修補需要 |
| `python scripts/v2_validate.py` | PASS |
| `python scripts/publishing/sync_site_content.py --check` | PASS；120 個網站章節投影與 canonical source 相同 |
| `python scripts/validate/check_links.py` | PASS；本地連結無錯，3 個外部 URL 未查 |
| `python -m unittest discover -s tests -v` | PASS；17 項測試，包括圖片政策、雙語 ID、遷移 hash、書籍 preflight、字型嵌入 gate |
| Python `py_compile` | PASS；變更的 validator、書籍建置器與字型檢查腳本 |
| `python scripts/publishing/build_books.py --locale en-US --format epub` | 預期拒絕，exit code 2；CH01 未核准，未產生正式 EPUB |
| Pandoc CH01 草稿 EPUB smoke | PASS；暫存 EPUB ZIP 完整，共 10 entries，不是正式出版物 |
| `npm --prefix apps/web run build` | FAIL（環境相依缺失）；120 頁同步成功，`astro` command not found |
| `python scripts/check_fonts.py --font "Noto Serif TC"` | Noto Serif TC 字型家族在 Windows 登錄可辨識；不代表已嵌入 PDF |
| MiKTeX／Poppler 探測 | FAIL（環境相依未確定）；先前紀錄有 MiKTeX 初始化權限錯誤，本次 shell 無法解析 `xelatex`／`pdffonts`；未驗證 V2 PDF |

## 5. 未解決事項與下一步

- 安裝／修復 Astro 專案依賴後執行網站 production build，再人工檢查 `/zh-tw/`、`/en/`、搜尋、語言切換、響應式和鍵盤操作。
- Pandoc 已可用；需初始化可寫且可重現的 MiKTeX，或改採 TeX Live／獨立 Poppler，再用真正完成的雙語樣章產生 DOCX/PDF/EPUB。PDF 必須由 strict gate 證實繁中字型嵌入，並人工抽查字形和排版。
- 補查外部參考連結與 V1 CH01 理論來源；建立 glossary 詞條並核實來源後才標為 approved。
- 依 [CH01 工作計畫](planning-v2/CH01-V2-WORKPLAN.md) 由編輯室完成繁中主稿、英文人工翻譯和 figure plan。Codex 目前只負責架構、收錄、檢查和出版；本次未撰寫章節正文或產圖。
- Skill frontmatter 沒有發現錯誤，故未修改該專案外檔案。若 Codex UI 的警告在重新載入後仍存在，需提供警告原文／畫面再定位其來源。

本次沒有覆蓋或移動 V1 章稿／素材、沒有發布網站，也沒有 commit 或 push。

## 6. 最新建置環境複驗（2026-10-18）

以下結果為目前環境的最新狀態，**取代前文第 2、4、5 節中仍稱 Astro、Pandoc、XeLaTeX、pdffonts 未安裝或尚無 PDF 實測的舊環境敘述**。測試稿與產物只在 `tmp/publishing-smoke/`，不是正式章稿或出版品。

| 項目 | 狀態 | 實測證據 |
|---|---|---|
| Astro / Starlight 安裝 | PASS | `npm ci --prefix apps/web --ignore-scripts --no-audit --no-fund` 依 lockfile 安裝 445 個套件。新增 `@astrojs/check` 供 `astro check` 使用。 |
| 繁中／英文網站建置 | PASS | `npm --prefix apps/web run build` exit 0，Starlight 回報 123 pages built；`dist/zh-tw` 與 `dist/en` 各有 61 個 `index.html`（各含首頁與 60 章）。建置無錯誤／警告。 |
| Astro 診斷及網站同步 | PASS | `npm --prefix apps/web run check`：0 errors、0 warnings、0 hints；`python scripts/publishing/sync_site_content.py --check`：120 個雙語頁面投影一致。 |
| Pandoc / 新 PowerShell PATH | PASS | `C:\Users\user\AppData\Local\Pandoc\pandoc.exe`，Pandoc 3.12.1。從使用者與系統 PATH 建立新 PowerShell 行程，成功解析 `pandoc`、`xelatex`、`pdffonts`，並讀到 Pandoc 3.12.1、MiKTeX-XeTeX 4.18（MiKTeX 26.5）。MiKTeX bin 路徑已寫入使用者 PATH。 |
| 可用 PDF 引擎／渲染器 | PASS | MiKTeX 26.5 提供 `xelatex`；`pdffonts` 24.04.0、`pdftotext`、`pdftoppm` 均可呼叫。 |
| 繁中與英文 PDF smoke | PASS | `python scripts/publishing/smoke_test_formats.py` 完成兩份合成 PDF。繁中 PDF `pdffonts` 顯示 Microsoft JhengHei Regular/Bold 與 Times New Roman 均 `emb=yes`、`sub=yes`、`uni=yes`；英文 PDF 的 Times New Roman Regular/Bold 同樣為 `yes`。兩份 PDF 的文字擷取與 PNG 渲染均成功，兩張頁面已人工檢視。 |
| Noto Serif TC 實際嵌入 | FAIL | 雖可在 Windows 字型登錄找到 `Noto Serif TC`（對應 `NotoSerifTC-VF.ttf`），MiKTeX/dvipdfmx 輸出 `Invalid font: -1 (0)`，PDF 只有 15 bytes。英語測試只設 `mainfont=Noto Serif TC` 仍同樣失敗，故故障點是該字型交給目前 XeLaTeX/dvipdfmx 時的字型輸出／嵌入，不是繁中 glyph 選擇。根因可能與 variable font 支援有關，但尚未用靜態字型做對照，故不把推測寫成已證實原因。正式 smoke 預設改用實測可嵌入的 Microsoft JhengHei。 |
| zh-TW / en-US EPUB smoke | PASS | 兩個 EPUB 均通過 ZIP CRC、首個未壓縮 `mimetype`、`container.xml`、OPF `dc:language`、XHTML 文字內容檢查。繁中與英文樣本文字在封裝內可正確解碼。 |
| Pandoc 繁中 EPUB UI 翻譯 | WARN | Pandoc 3.12.1 顯示 `Could not load translations for zh-TW` 與 `Abstract` 無翻譯；上述 EPUB metadata 與本文字仍通過。正式樣章需另檢視 title page／導覽等模板字串。 |
| EPUBCheck | BLOCKED | 本機未安裝 EPUBCheck；目前 smoke 使用 Python ZIP/XML 結構斷言，沒有宣稱通過官方 EPUBCheck。可在正式出版前加入一次性 EPUBCheck 驗收。 |
| 正式整書輸出 | BLOCKED（預期） | `build_books.py --locale zh-TW --format pdf` exit 2，原因 CH01 `draft-migration-pending`；英文 EPUB 同樣 exit 2，原因 `translation-needed`。正式出版 gate 正確阻止未核准草稿；沒有寫入正式整書。 |
| 專案單元測試 | PASS | `python -m unittest discover -s tests -v`：17/17。 |
| V2 架構與圖片規則 | PASS | `python scripts/v2_validate.py` exit 0；12 篇、60 章、雙語稿、舊稿雜湊及圖片政策 gate 均通過。 |
| Python 語法 | PASS | `py_compile` 覆蓋 smoke script、書籍建置器、網站同步器、V2 validator 與字型檢查器，exit 0。 |
| 外部參考連結 | BLOCKED / 待查 | 本地 Markdown 連結無失敗；仍有 3 個 URL 未做連網查證，`unchecked` 不代表有效。 |
| GitHub Actions / 部署 | 未執行 | 本次只做本機建置；未發布網站、未推送 GitHub，也未提交變更。 |

### 本次修正

- `npm ci` 依 `apps/web/package-lock.json` 建立可重現的依賴安裝，並加入 Starlight 建議的 `docsLoader`/`docsSchema` 設定。
- 網站投影改成 `.md`，並在生成副本中省略僅供編輯資料使用的 `locale`、`slug` 欄位；canonical Markdown 不變。這修正 MDX 無法解析 HTML 編輯註解，以及雙語頁面被相同 `slug` 合併的問題。
- 新增 `scripts/publishing/smoke_test_formats.py`，僅生成明確標示 SMOKE 的合成測試文字；對 EPUB 驗證封裝與雙語文字，對 PDF 驗證字型嵌入、抽取文字和 PNG 渲染。
- 更新 `scripts/publishing/build_books.py`：所有 EPUB 明列 `lang`/`language` metadata；中英文 PDF 都使用 XeLaTeX 和字型參數，正式 PDF 以 `pdffonts` strict gate 驗證預期字型。
- Pandoc 原本已安裝於使用者目錄且版本為 3.12.1；為確認固定版本，本次亦從官方 3.12.1 release 取得一份使用者本機副本。使用者 PATH 目前保留兩個同版 Pandoc 目錄，既有 `AppData\\Local\\Pandoc` 排在前面；MiKTeX 路徑加入 PATH。新 PowerShell 測試按 PATH 順序解析到既有 Pandoc。多出的副本可日後整理，未影響本次驗證。

本次未改動 `content/` 內 V1 原稿，未寫正式章節、未下載或建立出版插圖、未發布或推送。

## 7. CH01 出版問題最新複驗（2026-10-18）

本節是網站重複 ID、PDF 字型與 EPUBCheck 的最新狀態，取代本檔前文對這三項仍為警告／未安裝／未實測的舊紀錄。測試使用現有 CH01 草稿，未發布網站。

| 項目 | 最新狀態 | 實測證據 |
|---|---|---|
| Astro 重複 ID | PASS | 重新執行 `npm --prefix apps/web run build`，123 頁完成；log 無 `Duplicate id`；兩語 CH01 HTML 路由存在。 |
| PDF 字型嵌入與文字擷取 | PASS（draft） | 兩份既有 CH01 PDF 重新通過 `scripts/check_fonts.py --require-pdffonts`：各 7 個字型項目 `emb/sub/uni=yes`；中文 PDF 嵌入 Microsoft JhengHei。PDF 文字可抽取中英字元。XeLaTeX 缺字數 0 依對應建置 log／前次實測紀錄。 |
| EPUBCheck 安裝與 EPUB 結構符合性 | PASS（draft） | W3C／DAISY EPUBCheck 5.4.0 已安裝於使用者本機；兩語 CH01 draft EPUB 均 0 errors、0 warnings、0 informational messages、0 references。可由 `scripts/publishing/check_epub.ps1` 重跑。 |
| CH01 編輯審稿 | REVIEW NEEDED | Codex 結構與編輯初審已完成，九個主要區塊仍空白、英文稿未完成專業翻譯審校、案例缺版本／timecode 和學術理論來源。需完成退修，不可標 `approved`。詳見 `reports/CH01-EDITORIAL-AND-RIGHTS-REVIEW.md`。 |
| 插圖權利 | PENDING | 五項仍是 brief，尚無圖檔可做權利／技術／編輯核准；CH01 正文沒有嵌入第三方圖片。舊 V1 插圖權利資料仍待核實或排除。 |
| 正式出版 | BLOCKED（預期） | CH01 稿件不完整且中英文狀態未核准；V1 圖片授權未決。正式書籍 builder 保持 fail-closed。 |

本輪修改／重測檔案：`apps/web/astro.config.mjs`（移除過期、錯誤的手寫 sidebar link；Duplicate ID 舊警告在目前乾淨建置未重現，故不宣稱已定位歷史根因）、`scripts/publishing/check_epub.ps1`、`docs/PUBLISHING-V2.md`。完整編輯和權利判定見 CH01 專項審查紀錄；未 commit、未 push、未部署。
