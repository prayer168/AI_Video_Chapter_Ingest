# CH02 最終整合與章末驗收報告

- 章節：CH02《鏡頭、場面與剪接：電影語言的基本單位》
- 本次工作：staging V4 草稿逐項審稿、非破壞式整合、雙語網站及單章出版格式草稿測試
- 日期：2026-10-19（Asia/Taipei）
- Pipeline run：`production/runs/CH02/20261019T225451+0800-a105b6d9/`
- 本次整合備份：`backups/CH02-safe-integration-20261019-225715/`（含逐檔 SHA-256 manifest）
- 狀態：**草稿整合及可自動驗證部分完成；CH02 尚未達正式出版標準。**

## 變更摘要

- 將原 staging 繁中與英文草稿整合至 `content/zh-TW/chapters/CH02-camera-language.md` 與 `content/en-US/chapters/CH02-camera-language.md`。前置 metadata 明確維持 `draft-migration-pending`／`draft-for-human-review`，全書登錄狀態為 `review-needed`。
- V1 章稿、原來源 ZIP、staging 原稿、staging SVG、第一章、第三章均保留；整合前 canonical scaffold、metadata、圖稿索引、網站投影和 `history.md` 已備份。中途試排版的重複圖稿版本也另存於備份，不覆蓋原始稿。
- 26 個雙語術語及 R025–R029 來源紀錄合併至 V2 全域 metadata。另建立 `metadata/translations/CH02-alignment.yaml`，保留 13 個章節節點、26 個術語及 5 個 staging-to-canonical 圖號對照；語意對等仍待雙語編輯審查。
- 五張原創可編輯 SVG 逐位元複製到 `assets/chapters/CH02/figures/originals/`，永久圖號為 CH02-FIG-001–005（顯示為 2-1A–2-1E）。每張圖的 SHA-256 與 staging 原圖一致；原始 staging ID 以 `source_staging_figure_id` 保留。
- 五張圖的權利、技術、編輯與出版狀態皆為 pending；沒有將圖稿標為 approved。網站與排版 PNG 僅由 SVG 產生於建置投影／gitignored `tmp/` 預覽目錄。
- 修正 `scripts/publishing/figure-captions.lua` 支援 CH02 圖號，並避免 PDF 自動圖號與英文手動圖號重複。
- 更新 CH02 測試，使其驗證來源 ZIP 與 V1 原稿不變，以及 canonical 草稿已安全遷移；原本「canonical scaffold 必須不變」的舊測試不再適用本次明確整合任務。

## 章末逐項稽核

| 檢查項目 | 狀態 | 實際證據／限制 |
|---|---|---|
| V1 原稿、來源包及 staging 原始素材完整性 | PASS | V1 SHA-256 `a669651d795bba3e02933f1771a1ee5b53855daebb11fa2452850c38363138af`；來源 ZIP SHA-256 `d448defde21abe8802ad87684928eaade0f7c39101b423159073391457a519a5`，ZIP CRC 通過。staging 兩語原稿未改；五張 SVG hash 與來源紀錄一致。 |
| 整合前備份及回復能力 | PASS | `backups/CH02-safe-integration-20261019-225715/BACKUP-MANIFEST.json` 列出整合前 11 個既有檔案雜湊；試排版重複插入版本另留於 `.../files/content/`；測試檔與 caption filter 編輯前副本亦備份。 |
| 繁中正文內容結構 | PASS（編輯草稿） | canonical 稿含摘要、目標、先備知識、術語、原理、傳統流程、AI 轉換、工作流程、提示詞、案例、品質、練習及來源；13 個章節節點。內容與論述仍需專業審稿。 |
| 英文對譯稿 | NEEDS HUMAN REVIEW | 英文完整草稿已 canonical 化；仍是繁中來源對譯稿，未經人工雙語編輯簽核。正式英文章名仍留空於 registry；章稿內暫用標題不等於已核准標題。 |
| 中英文節點、圖號及術語對照 | PASS（結構） | 自動比對中英 14 個 anchor（含章根 ID）集合一致；兩語各有 26 個 TERM-CH02 ID、5 個 CH02-FIG ID。`metadata/translations/CH02-alignment.yaml` 保存原始 section/term/figure 對照。語意等值需人工校譯。 |
| 術語定義與中文用語 | NEEDS HUMAN REVIEW | 26 個雙語詞條合併至 `metadata/terminology.yaml`，全部仍是 draft；攝影、鏡頭、構圖及運鏡術語需電影攝影／教育編輯確認。 |
| 電影理論、光學與歷史主張 | NEEDS HUMAN REVIEW | 引用 R001、R009–R012、R025–R028；未補猜教科書頁碼。出版前研究編輯需逐項核對採用版次、章節 locator、主張範圍及理論脈絡。 |
| 電影案例及片段核實 | NEEDS HUMAN REVIEW | 《大白鯊》dolly-zoom 實務案例以 R026 支持一般製作描述；尚無已記錄的合法觀看版本、精確 timecode 及逐鏡核看紀錄。 |
| AI 工具與模型能力敘述 | NEEDS HUMAN REVIEW | Runway R006/R029 限定於官方特定版本提示指南；沒有把文字提示描述成精確物理控制保證。出版前需重查版本、工具可用性並提供授權實測紀錄。 |
| 提示詞與技術規格 | NEEDS HUMAN REVIEW | 章稿有 Shot Spec、JSON 與提示詞範例；未執行付費生成，也未有指定模型的實測 take／版本／參數紀錄。 |
| 原創插圖檔案及 hash | PASS（檔案層） | CH02-FIG-001–005 五個 SVG 均存在，分別 1,829／1,493／1,145／1,538／1,626 bytes；canonical SHA-256 全部與 staging manifest 相符。SVG 原檔可編輯且未替換。 |
| 雙語圖說、alt、圖號及正文位置 | PASS（機器檢查） | 每語 5 張圖、對應圖號 2-1A–2-1E、非空 alt、雙語圖說同步；網站 HTML、EPUB、DOCX 檢查到 5 個嵌入圖。PDF 圖號重複問題已修正，校樣抽查通過。 |
| 插圖原創性、作者歸屬、權利及可及性終審 | NEEDS HUMAN REVIEW | SVG 為專案手寫原創示意圖，未嵌入第三方圖片；individual creator 欄未記名。Manifest 仍標示 rights/technical/editorial `pending`、`pending-publication-approval`。需確認實際繪製者、視覺技術、對比、縮放、閱讀順序和出版核准。 |
| 全域術語、來源、圖稿 ID 唯一性 | PASS | `python scripts/v2_validate.py` 通過；26 個新增 term IDs、R025–R029 和 CH02-FIG-001–005 無重複；全域 figure registry 已同步納入 5 筆 pending 草稿。 |
| 連結檢查 | NEEDS HUMAN REVIEW | `python scripts/validate/check_links.py`：0 failures、0 network checked、5 not conclusively checked。無本地檢查失敗不代表 5 個外部連結已即時可達或能支持相應主張。 |
| 網站 canonical-to-Astro 投影 | PASS | `python scripts/publishing/sync_site_content.py` 與 `--check` 通過；已更新中英文 CH02 投影及 5 個靜態 SVG 複本，來源在 `content/` 與 `assets/`。 |
| Astro 型別與內容檢查 | PASS | `npm --prefix apps/web run check`：0 errors、0 warnings、0 hints。第一次在 sync 前執行時出現兩個舊投影重複 ID 警告；同步後重跑無警告。 |
| Astro 本機網站建置 | PASS（預覽） | `npm --prefix apps/web run build` 成功，123 個 HTML 頁面；中英 CH02 路由均存在。僅本機靜態建置，沒有部署或發布。 |
| 網頁圖稿、ID、替代文字檢查 | PASS | 解析 `apps/web/dist/zh-tw/ch02-camera-language/index.html` 與 `apps/web/dist/en/ch02-camera-language/index.html`：各有 5 個 CH02-FIG figure、每圖 1 個圖檔、非空 alt。 |
| 雙語 DOCX 草稿 | PASS（非正式） | Pandoc 3.12.1；`tmp/CH02-draft-integration-20261019-r1/` 中英 DOCX ZIP CRC 通過，各含 5 張內嵌圖。 |
| 雙語 PDF 草稿及字型嵌入 | PASS（非正式） | XeLaTeX/Pandoc 建出繁中 20 頁、英文 16 頁。`scripts/check_fonts.py --require-pdffonts` 確認繁中 Microsoft JhengHei、英文 Times New Roman 及 PDF 所列字型全數嵌入；PyMuPDF 抽取沒有 U+FFFD，五個圖號均可抽取。抽看含圖頁，圖文未見明顯截切。 |
| PDF 字型失敗與修復記錄 | PASS（已修復，仍留校樣限制） | 首次用 Noto Serif TC 出現 MiKTeX `dvipdfmx:fatal: Invalid font: -1 (1)`，並有缺字訊息；改用可解析並實際嵌入的 Microsoft JhengHei 後成功。最終校樣輸出為 `CH02-zh-TW-captionfix.pdf` 和 `CH02-en-US-captionfix.pdf`。 |
| 雙語 EPUB 與 EPUBCheck | PASS（非正式） | 兩語 EPUB ZIP CRC 通過，各含 5 張 EPUB media；EPUBCheck 5.4.0 兩語退出碼 0，完整輸出記錄在 `tmp/CH02-draft-integration-20261019-r1/epubcheck-*.log`。 |
| 全書 60 章正式出版建置 | BLOCKED（符合防護門檻） | `build_books.py` 要求 60 章兩語均 approved；目前僅 CH02 為 review-needed，未嘗試繞過正式出版門檻。此項與單章草稿輸出分開計算。 |
| CH02／全站正式出版圖像權利閘門 | BLOCKED | 本章 5 張圖尚未通過權利與人工審查，不能發布；全站圖片政策檢查亦指出 CH01 圖稿尚有 pending 狀態。此為預期防護結果，沒有將任何素材自動批准。 |
| 單元、整合與 V2 結構測試 | PASS | `python -m unittest discover -s tests -v`：40/40 PASS；`python scripts/v2_validate.py` PASS；`python scripts/validate_project.py` PASS（12 篇、60 章、2 份完整 canonical 章稿；其 52 術語／24 來源統計來自 legacy 資料集，不等於新增 V2 全域 bibliography 數）。 |
| 歷史記錄、差異與版本管理 | PASS | 本報告、`history.md` 及 run checkpoint 記載修改理由、失敗／修復、工具版本、備份位置、hash 與測試結果。未 commit、未 push。 |
| 作者、雙語編輯、研究／攝影專家簽核 | NEEDS HUMAN REVIEW | 尚無作者或專業審稿人簽名／日期；全書 metadata 未設 approved。 |
| 網站發布／GitHub 推送 | NOT RUN | 本輪只做本機 build；未部署網站、未 commit、未 push GitHub。 |

## 已完成的自動修復及測試錯誤處理

1. 依第一次 `sync_site_content.py` 失敗訊息，將原 staging 既有圖稿路徑改指向 canonical 資產目錄，沒有重複插入第二份圖稿。
2. 將舊單元測試從「canonical scaffold 永遠不變」改為「來源 ZIP 與 V1 不變、canonical 內容已遷移且保持 draft」，對應本次使用者授權的整合目標。
3. 首輪全套測試因此有 2 個預期不相容檢查失敗；修正測試及投影後，第二輪 40/40 PASS。
4. 首次 Noto Serif TC PDF 編譯失敗；改用 Microsoft JhengHei 並檢查實際嵌入及文字抽取。英文圖說的自動／手動圖號重複亦已修復，最終中英文 PDF captionfix 版測試通過。

## 剩餘工作及責任角色

- **雙語編輯**：逐節校譯，審核 26 個術語、學習目標、技術參數、圖說／alt 對應，正式核定英文章名。
- **研究編輯／攝影專業審稿人**：逐主張檢查理論與來源；確認教科書採用版次與頁碼；選定合法電影版本並記錄《大白鯊》案例 timecode；重查 Runway 版本功能。
- **插圖作者／權利及可及性審查者**：補記 SVG 實際創作者與修訂歷史；檢視技術正確性、文字縮放、色彩對比及讀序；逐張簽署 rights/editorial/publication 狀態。
- **作者**：核定中英正式章名、正文、圖稿及出版版本。上述簽核完成以前，CH02 不得標示 `publication-ready`。
- **出版工程**：人審完成後再跑正式圖像閘門、完整網站審查及正式章稿輸出；目前單章 tmp 草稿不能當成正式出版成品。

## 出版結論

**CH02 是否達到正式出版標準？否。** 本輪完成了安全整合與可自動驗證的出版草稿檢核，但雙語校譯、來源定位、電影 timecode、SVG 創作者／權利終審與作者核准仍未完成；正式全書建置及發布權利閘門維持封鎖。完成以上人工作業並取得簽核後，才進入正式定稿驗收。
