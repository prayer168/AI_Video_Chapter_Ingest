# CH01 V2 整合前差異與保護報告

- 建立時間：2026-10-18 13:24 +08:00
- 備份目錄：`backups/CH01-V2-integration-20261018-132434/`
- 整合狀態：本報告在 canonical CH01、術語、引用、提示詞或圖片登錄修改前建立。

## 輸入位置盤點

| 位置 | 實測結果 | 處理方式 |
|---|---|---|
| `staging/CH01-V2/` | 存在但遞迴檔案數為 0；唯讀屬性 | 沒有可讀的章稿素材包；以 repo 內既有 V2 雙語稿及工作計畫比對 |
| `staging/Homage-V1/` | 存在但遞迴檔案數為 0；唯讀屬性 | 使用 repo 內原始 ZIP `chapters/AI-Video-Bible-Homage-V1-CH01-Supplement-DRAFT.zip`，不解壓覆寫來源 |
| `chapters/source-packs/AI-Filmmaking-Bible-CH01-Codex.zip` | ZIP 存在；含 CH01 原始稿、README、CODEX-INSTRUCTIONS、shot JSON、提示詞 | 僅作 V1 來源比對，原 ZIP 保持不變 |

## 修改前保護清單

備份目錄保存 canonical 雙語稿、CH01 figure manifest、全域術語／引用／提示詞／資產 registry、章節 registry／工作計畫、V2 validator、V2 bibliography／figure registry、建置驗收報告和 `history.md`。每個檔案及兩個來源 ZIP 的 SHA-256 和長度記於 `MANIFEST.json`。

V1 原稿、原始 source-pack ZIP 和其他章節均保持原位，不會被此整合流程覆蓋或移動。

## 整合前預期差異

1. CH01 繁中／英文 V2 稿是骨架，`CH01-S01` 至 `CH01-S12` 錨點已存在；正文仍標記草稿／待翻譯。
2. Homage V1 ZIP 含雙語 CH01 插入稿、五張原創圖 briefs、圖說／alt 草案、32 部候選片單及品質清單。
3. 僅把五個 CH01 案例及其術語、可追溯來源、圖像 brief metadata 納入現有 V2 結構；32 部片單仍是候選索引，不分派到其餘章節。
4. 原創插圖尚未生成或通過人工權利／技術／編輯審查，因此只建立待審圖像 briefs，不登記為可出版圖片、不嵌入章稿。
5. 來源包要求 `CH01-HOMAGE-FIG-*` namespace；V2 validator 現行 regex 不接受該格式。修 validator 前會先備份並增加專用允許格式。

## 修改後差異

整合完成於 2026-10-18。原始 V1 稿、來源 ZIP、現有第一／二章原稿均未覆蓋、移動或刪除。修改前快照保存在上述 backup 目錄，`MANIFEST.json` 記錄來源與基線 SHA-256；本報告保留為修改前後比較索引。

### 已整合內容

- 繁中與英文 CH01-S09 各納入 5 個對應案例，穩定段落 ID 為 `CH01-P001` 至 `CH01-P005`：*Citizen Kane*、*Rashomon*、*A City of Sadness*、*In the Mood for Love*、*Yi Yi*。
- 每組案例均保留來源可支持的事實、評論／理論解讀、實務轉譯及讀者練習之區別；原文中的法定觀看版次及場景 timecode 留待後續補查，理論性主張也需增加學術來源。
- 加入 6 個雙語術語草案及 9 筆 CH01 參考來源（R013–R021），登錄於章稿、全域 glossary、V2 terminology registry 和 bibliography。
- 建立 5 份中英圖說／alt 與原創插圖 briefs，登錄於 CH01 figure manifest、figure registry 和 prompts；沒有生成或嵌入正式圖片，權利、技術及編輯狀態均為 pending。
- 更新 `scripts/v2_validate.py`，使 `CH01-HOMAGE-FIG-###` namespace 僅適用 CH01；增加 4 個 namespace 測試。
- 更新 Pandoc 書籍參考錨點格式，支援 HTML 網站及 PDF/EPUB 輸出；章稿中的 brief 路徑只作紀錄，不連到靜態網站不存在的資產 URL。
- 將雙語術語表由寬表格改為逐詞條排版，修正 PDF 欄位重疊；`build_books.py` 的中英文 PDF 命令都指定 CJK 字型，並增加回歸測試。
- 將本機草稿 smoke-test 輸出目錄加入 `.gitignore`；本機預覽檔仍保留，但不會被誤認為正式出版資產。

### 實測結果（2026-10-18）

- `python scripts/v2_validate.py`：PASS。
- `python scripts/validate_project.py`：PASS，12 篇／60 章、2 份 canonical CH01 稿、52 個術語、21 筆參考資料。
- `python scripts/validate/check_links.py`：PASS，0 個失敗；3 個外部 URL 未能確認，不代表已證實可用。
- `python -m unittest discover -s tests -v`：PASS，22/22。
- `npm --prefix apps/web run check`：0 errors/warnings/hints。Starlight content loader 另外在 CH01 中英文頁面各輸出一則 duplicate ID 訊息，須查明其來源。
- `npm --prefix apps/web run build`：PASS，123 個靜態頁面。建置成功不代表 duplicate ID 警告已解除。
- Pandoc 3.12.1 + MiKTeX XeLaTeX：中英文 CH01 草稿 PDF 及 EPUB 均產出於 `tmp/CH01-V2-draft-preview/`，不屬正式出版物。PDF `pdffonts` strict check 顯示 Microsoft JhengHei（繁中）及 Times New Roman（英）均有嵌入；`pdftotext` 中英抽取及首頁 PNG 渲染通過。中英文 PDF 均指定 Microsoft JhengHei CJK fallback 與 Times New Roman Latin，XeLaTeX 缺字警告數皆為 0；英文雙語術語頁重排後視覺抽查無欄位重疊。
- 兩份 EPUB 的 ZIP CRC、未壓縮首項 `mimetype`、container／OPF、語言標記和案例文字結構檢查通過；未安裝 EPUBCheck，尚無正式 EPUB conformance 驗證。
- `scripts/image_policy.py --target zh-TW-book` 與 `--target en-book`：BLOCKED，原因為既有 V1 `ASSET-CH01-FIG-01` 權利與核准欄位仍 pending/unresolved。CH01 V2 本身目前沒有圖片嵌入；新 5 個 planned figures 也尚未生成或核准。
- 正式書籍 builder 對中英文分別 BLOCKED，因 CH01 editorial/translation status 未 approved；符合本次不得宣稱完成的要求。

網站沒有部署；沒有 commit 或 push GitHub。
