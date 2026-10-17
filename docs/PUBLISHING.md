# 出版工具鏈

## 建置

```powershell
python scripts/build.py --format html
python scripts/build.py --format docx
python scripts/build.py --format pdf
python scripts/build.py --format all
```

HTML 由標準函式庫產生至 `dist/html/`。DOCX 使用 `python-docx`（`pip install python-docx`）。PDF 使用 Pandoc + XeLaTeX，若不可用則可用 WeasyPrint（`pip install weasyprint`）。工具缺少時腳本會以非零狀態結束並提示安裝方式。

## 繁體中文與字型

可透過 `--font "Noto Serif CJK TC"` 指定 DOCX/PDF 字型。系統需安裝該字型。執行：

```powershell
python scripts/check_fonts.py --pdf dist/book.pdf
```

腳本檢查系統字型登錄，並在有 `pdffonts` 時檢查 PDF 字型嵌入旗標；缺少檢查工具時會提示人工驗證。PDF 對中文字元是否有字形覆蓋仍應用目標閱讀器抽樣檢查。

## 來源連結

```powershell
python scripts/check_links.py
python scripts/check_links.py --online
```

離線模式檢查格式；線上模式查 URL 可達性，網路阻擋或限流會被標成待確認。引用有效性仍需人工審閱。

## 可重現性

出版輸出是生成物，預設不納入 Git；每次發布記錄專案版本、Git commit、建置工具版本、字型名稱和日期。保留 Markdown、YAML、Python、CSS 等原始檔。
