# V2 出版工具鏈

內容源：雙語 Markdown + YAML/BibTeX；校驗由 Python 腳本執行。Web 候選 Astro + Starlight，採自訂 editorial theme，正式採用前需以 CH01 雙語樣章做可行性驗收。書籍以 Pandoc 轉 DOCX/EPUB，以 XeLaTeX 輸出 PDF；HTML 網站與書籍共用章節源稿。

本階段建立可重現設定與 smoke tests，不宣稱已完成版面／字型驗收。正式 PDF 要檢查字型嵌入及繁中文字形、圖說跨頁、解析度與印刷校樣；工具缺席時清楚報告 skipped。預設輸出 `dist/`，不自動發布。

## 本機可重現驗證（2026-10-18）

- 網站依賴以 `apps/web/package-lock.json` 固定版本；乾淨安裝：`npm ci --prefix apps/web --ignore-scripts --no-audit --no-fund`。驗證：`npm --prefix apps/web run build` 與 `npm --prefix apps/web run check`。
- Astro/Starlight 章稿投影採純 Markdown，canonical 章稿的 `locale`、`slug` 留在原稿，網站路由由語系資料夾與成對檔名生成。`apps/web/src/content.config.ts` 明確使用 Starlight `docsLoader`/`docsSchema`。
- Pandoc 3.12.1：`C:\Users\user\AppData\Local\Pandoc\pandoc.exe`；MiKTeX XeLaTeX 26.5：`C:\Users\user\AppData\Local\Programs\MiKTeX\miktex\bin\x64`。MiKTeX 路徑已加入使用者 PATH；新 PowerShell 驗證可呼叫 `pandoc`、`xelatex`、`pdffonts`。
- 使用 `python scripts/publishing/smoke_test_formats.py` 建立純測試文字的 zh-TW / en-US PDF 與 EPUB，所有產物只寫入 `tmp/publishing-smoke/`，不代表正式章節。
- PDF 使用 XeLaTeX；西文預設 Times New Roman，繁中預設 Microsoft JhengHei。`pdffonts` 必須實測 `emb=yes`，並檢查文字擷取及 PNG 渲染。2026-10-18 兩語 smoke PDF 均通過嵌入、文字擷取和頁面渲染檢查。
- `Noto Serif TC` 雖已安裝，MiKTeX/dvipdfmx 實際輸出 `Invalid font: -1 (0)`，且英文字稿只使用該字型時也會失敗；此字型／目前引擎組合不得作正式 PDF 字型。字型檔對應 `NotoSerifTC-VF.ttf`，變動式字型支援是待進一步隔離的原因假設。
- EPUB smoke 逐項檢查 ZIP CRC、首個未壓縮 `mimetype`、`container.xml`、OPF 中 `dc:language`、XHTML 文字。Pandoc 3.12.1 對 `zh-TW` 會顯示 UI 翻譯警告，但 EPUB 語言 metadata 與繁中文字元均通過；正式樣章需再檢查閱讀器顯示與 EPUBCheck。
- EPUBCheck 官方發行版：W3C／DAISY EPUBCheck 5.4.0，需 Java。Windows 安裝後可設定 `EPUBCHECK_JAR`，或置於 `%LOCALAPPDATA%\Programs\EPUBCheck\5.4.0\epubcheck-5.4.0\epubcheck.jar`；以 `./scripts/publishing/check_epub.ps1` 檢查預設雙語 CH01 EPUB，也可傳入 `-Epub` 與 `-Jar` 指定目標。官方來源：[W3C EPUBCheck](https://www.w3.org/publishing/epubcheck/)、[5.4.0 發行頁](https://github.com/w3c/epubcheck/releases/tag/v5.4.0)。版本與查證日期須隨更新記錄。
- 2026-10-18 安裝 EPUBCheck 5.4.0 與 Java 18 後，`tmp/CH01-V2-draft-preview/CH01-zh-TW-draft.epub` 和 `CH01-en-US-draft.epub` 均通過，0 errors、0 warnings、0 informational messages、0 references。
- 2026-10-18 重跑 Astro build：123 頁成功，`/zh-tw/ch01-cinematic-language/` 與 `/en/ch01-cinematic-language/` 均存在，建置輸出沒有 `Duplicate id` 訊息。舊驗收報告中的 duplicate 訊息已由新一輪乾淨建置覆蓋；不把草稿網站視為已發布網站。
- 目前章稿仍未核准；正式書籍 gate 仍會拒絕輸出。Smoke test 不繞過正式審核，不會覆寫 `dist/books/`。
