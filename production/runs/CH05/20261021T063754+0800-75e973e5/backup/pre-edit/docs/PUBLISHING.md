# 出版工具鏈

## 1. 安裝專案 Python 套件

```powershell
python -m pip install -r requirements.txt
```

## 2. 安裝出版程式

建議用 Pandoc 同時產生 DOCX 和 PDF。Windows 可從 [Pandoc 官方安裝頁](https://pandoc.org/installing.html) 下載安裝程式，也可依官方指示使用 winget：

```powershell
winget install --source winget --exact --id JohnMacFarlane.Pandoc
```

PDF 另需 XeLaTeX 和 Inkscape（章節插圖含 SVG 時）。Windows 可由 [MiKTeX 官方下載頁](https://miktex.org/download) 安裝 XeLaTeX，並從 [Inkscape 官方網站](https://inkscape.org/) 安裝圖形轉換器；重開終端後確認 `pandoc --version`、`xelatex --version` 和 `inkscape --version` 可執行。

## 3. 建置

```powershell
python scripts/build.py --format html
python scripts/build.py --format docx --font "Noto Serif TC"
python scripts/build.py --format pdf --font "Noto Serif TC"
```

HTML 輸出在 `dist/html/`，包含專案文件與章節頁面。DOCX/PDF 只收錄 `chapters/` 根目錄下的編號章稿，避免把 README、出版規範等內部文件放進讀者版。DOCX 用 Pandoc 保留標題、表格與程式碼，再由 `python-docx` 設定中英文字型樣式。PDF 同時指定 `mainfont` 與 `CJKmainfont`，由 XeLaTeX 排版繁體中文字元；章稿含 SVG 時，建置器會呼叫 Inkscape 分別轉成 DOCX 用 PNG 與 PDF 用 PDF 圖檔，並把資源路徑改寫成 repo 根目錄相對路徑。

若 PowerShell 找不到 Inkscape，但已安裝在預設位置，先保存目前 Python 路徑，再將 Inkscape 目錄加到目前工作階段 PATH 尾端。不要放到 PATH 最前面，否則可能優先執行 Inkscape 隨附的 Python：

```powershell
$pythonExe = (Get-Command python).Source
$env:Path += ';C:\Program Files\Inkscape\bin'
Get-Command python, pandoc, xelatex, inkscape
& $pythonExe scripts/build.py --format docx --font "Noto Serif TC"
& $pythonExe scripts/build.py --format pdf --font "Noto Serif TC"
```

## 4. 驗證字型

本機登錄目前可找到 `Noto Serif TC` 和 `Noto Sans TC`；此前檢查失敗是因舊檢查器只比對 `Noto Serif CJK TC` 名稱。現在可以執行：

```powershell
python scripts/check_fonts.py --font "Noto Serif TC"
python scripts/check_fonts.py --font "Noto Serif TC" --pdf dist/AI-Filmmaking-Bible.pdf
```

第二個命令若系統安裝 `pdffonts`，會檢查 PDF 每個字型的 embedded 欄位是否為 yes。沒有 `pdffonts` 時，請在 Acrobat 或其他 PDF 閱讀器的文件屬性檢視 Fonts。最後需抽查繁體中文、標點、箭頭、插圖和表格換頁；字型已安裝不等於 PDF 已嵌入，也不等於所有字形正確。MiKTeX 若提示尚未檢查更新，建議發布前開啟 MiKTeX Console 執行更新，再重新建置。

## 5. 引用連結

```powershell
python scripts/check_links.py
python scripts/check_links.py --online
```

線上檢查遇到 403、逾時或限流時列為待人工確認，不直接判定來源失效。術語定義的頁碼必須對應到本書採用的確切版次；建議在術語資料補上版次、ISBN、頁碼或章節定位。若不同版次頁碼不同，記錄可追溯的章節/節標題，並把頁碼標為待核。出版輸出是生成物，預設不納入 Git；發布時記錄專案版本、Git commit、建置工具版本、字型名稱和日期。


## 插圖核准與正式出版閘門

正式 HTML、DOCX、PDF、EPUB 建置會先依輸出目標檢查章稿使用的所有圖片；任何外部圖像、缺少 `data/assets.yaml` 登錄或尚未完成權利／技術／品質核准的圖片，都會使建置中止。HTML 網站輸出也檢查 README 與 `docs/` 內容。檢查單一目標：

```powershell
python scripts/image_policy.py --target zh-TW-site --include-docs
python scripts/image_policy.py --target zh-TW-book
python scripts/image_policy.py --target en-site --include-docs
python scripts/image_policy.py --target en-book
```

英文檢查只代表核准資料狀態；目前書籍建置輸入仍取自現有繁中章稿，並不會自動翻譯或產出英文版本。

編輯中的草稿預覽會省略尚未核准的圖像，並以待審文字替代：

```powershell
python scripts/build.py --format html --preview
python scripts/build.py --format docx --preview
python scripts/build.py --format pdf --preview --font "PMingLiU"
python scripts/build.py --format epub --preview
```

預覽輸出位於 `dist/preview/`，不可直接作正式出版物。完整欄位和狀態定義見 [插圖原創與著作權管理規範](IMAGE-RIGHTS-POLICY.md)。
