# AI Video Bible V2.0 架構建置報告

**日期：** 2026-10-18（Asia/Taipei）  
**範圍：** 雙語書籍、雙語網站與出版工程骨架  
**狀態：** 架構建置完成；內容、網站相依安裝及正式出版驗收仍在進行

## 遷移計畫與安全邊界

1. 以 `planning-v2/ARCHITECTURE-V2.md` 和 `planning-v2/CODEX-BOOTSTRAP.md` 作為架構依據。
2. 唯讀盤點 V1 CH01/CH02、章節素材及 source-packs，先複製到 `legacy/2026-v1/chapters/`，逐檔比對 SHA-256；保留 V1 原路徑。
3. 新建 V2 `content/zh-TW`、`content/en-US` 及永久 ID metadata，不批次遷移或覆寫舊稿。
4. 建立圖片、翻譯、引用、品質、網站及書籍工具鏈規則；先用架構檢查與測試驗收。
5. 不提交、不推送、不部署；不刪除舊素材，不以網路圖片作正式插圖。

## 完成項目

- **V1 備份：** 第一章、第二章 Markdown、兩章素材目錄及 source-packs 已複製；[遷移清單](legacy/2026-v1/migration-manifest.csv) 共 20 個檔案，SHA-256 全數相符。V1 來源仍在原位置。額外歸檔了整個 `source-packs/` 目錄，以保留其他既有原始包。
- **雙語內容模型：** 建立 12 篇、60 章永久 ID 登錄及繁中／英文各 60 個章節 scaffold；各語言使用同一 `chapter_id`。CH01、CH02 繁中狀態標為待遷移審校；英文均標為 translation-needed。無完整章節正文被宣稱完成。
- **出版 metadata：** 章節與篇章登錄、翻譯狀態、術語空登錄、BibTeX 參考庫、圖像登錄及每章 figure manifest 已建立。
- **模板和規範：** 新增章節模板、中英翻譯配對契約、圖像權利規範、引用與證據規範、品質 gate、Cinematic Editorial 設計系統與編輯代理規則。
- **影像治理：** 圖片須有永久 ID、來源／生成紀錄、雙語 caption/alt、權利／技術／編輯審查；未核准不得進正式輸出。圖像文字採可編輯 SVG overlay；未建立或下載正式插圖。
- **網站起始碼：** `apps/web/` 已有 Astro + Starlight 候選設定、繁中與英文樣章占位頁、自訂 editorial CSS。新增 `scripts/publishing/sync_site_content.py`，將 `content/` 的 canonical Markdown 投影至 Astro 文件集合；建置前自動同步，不把網站投影副本當編輯源。未設定部署流程。
- **書籍工具鏈：** 新增 `scripts/publishing/build_books.py`，支援指定語系以 Pandoc 輸出 DOCX、EPUB 或 XeLaTeX PDF；會拒絕含 scaffold/placeholder 的正式書籍輸出。正式 PDF 字型驗收尚未完成。
- **自動檢查：** 新增 V2 Python validator、雙語內容同步、正式書籍 fail-closed gate、嚴格 PDF 字型檢查、術語 JSON Schema、17 項測試與 GitHub Actions workflow；根 README、CHANGELOG、`.gitignore` 加上 V2 使用入口。

## 驗證結果

| 驗證 | 結果 |
|---|---|
| `python scripts/v2_validate.py` | 通過：12 篇、60 章、60 組雙語 scaffold、遷移雜湊、圖像 gate |
| `python scripts/publishing/sync_site_content.py` + `--check` | 通過：120 個雙語章節頁面同步與來源一致檢查 |
| `python -m unittest discover -s tests -v` | 通過：17 項測試（V1 圖片政策、V2 架構／書籍 gate、PDF 字型 gate） |
| `python scripts/validate/check_links.py` | 通過：本地連結 0 個失效；3 個外部連結未做網路檢查 |
| `python -m py_compile ...` | 通過：V2 bootstrap、validator、出版器、連結檢查器語法 |
| `git diff --check` | 通過；僅顯示既有 Git autocrlf 換行提示 |
| V1 檔案備份雜湊 | 通過：20/20 |
| Astro dependency install / web build | 未完成：`npm --prefix apps/web install` 長時間沒有輸出，為避免背景安裝而中止；尚未證明 build 可用 |
| Astro build 實際呼叫 | 未通過環境相依檢查：同步 120 頁成功，接著 `astro` 未安裝／不在 PATH，命令無法執行 |
| 雙語正式 DOCX/PDF/EPUB | 未執行：正式書籍 gate 對 CH01 的 `translation-needed` 狀態正確拒絕；Pandoc 不在 PATH |
| PDF 字型嵌入及渲染校樣 | 未驗收：Windows 登錄可找到 Noto Serif TC，但 XeLaTeX／pdffonts 均不存在，不能確認實際 PDF 嵌入 |
| 參考文獻外連與內容審稿 | 未執行；須依實際研究章稿逐筆查證 |

## 尚未完成

- Astro 相依安裝和網站 production build；canonical 內容同步通過，但目前只有 source scaffold，不能宣稱網站 build／視覺驗收通過。
- CH01 V2 繁中逐節審校／遷移、英文人工翻譯與編輯審校。
- CH01 figure plan、原創插圖、SVG 標註、雙語圖說與權利／技術／編輯核准。
- Pandoc/DOCX/EPUB/PDF 全鏈路實測、PDF 字型嵌入、字形抽查和版面校樣。
- 術語逐筆定義、參考資料核實、外部 URL 檢查及無障礙人工檢查。
- 其餘 59 章內容撰寫；本次僅建立 scaffold，未撰寫完整章稿。

CH01 僅有工作清單與驗收條件，見 [CH01 V2 工作計畫](planning-v2/CH01-V2-WORKPLAN.md)；本次沒有撰寫章節正文或生成插圖。

## CH01 雙語圖文樣章下一步

1. 審查 V1 CH01，將核准內容遷入 `content/zh-TW/chapters/CH01-*.md`；補足理論原件、頁碼與來源追溯。
2. 保持永久段落錨點，完成人工英文翻譯與專業術語校對；記錄來源 revision、譯者／審校者和日期。
3. 編寫逐段 figure plan：figure ID、插入點、教學目的、雙語 caption/alt、原創 prompt、圖像製作與審查欄位。
4. 依內容需要製作原創電影式透明插圖和可編輯 SVG 技術圖；逐圖完成權利、技術和編輯審核。
5. 解決 npm 安裝後建置網站樣章，檢查 `/zh-tw/`、`/en/` 路徑、搜尋、行動版、鍵盤操作與圖片呈現。
6. 用同一雙語 Markdown 內容建置 HTML、DOCX、PDF、EPUB；驗證繁中字型嵌入、字形、圖說、頁面與 EPUB 結構。
7. 校對樣章後產出 CH01 release pack（雙語章稿、圖片原件／SVG、figure manifest、鏡頭資料、術語、參考及測試報告）。

## Git 狀態

本次未 commit、未 push、未發布網站。開始建置前工作樹已存在使用者先前的 tracked 修改與 untracked 第二章、source packs、權利規範及測試；所有內容均予保留。請先人工檢視 `git status` 及變更，再決定後續提交範圍。
