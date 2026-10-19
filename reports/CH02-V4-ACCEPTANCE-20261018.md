# CH02 V4 章節整合與技術驗收報告

- 章節：CH02《鏡頭、場面與剪接：電影語言的基本單位》
- Run：`production/runs/CH02/20261018T215615+0800-55868375/`
- Draft revision：`2.1.0-draft`
- 日期：2026-10-18（Asia/Taipei）
- 總結：**章稿整理及草稿出版測試完成；尚未達正式出版標準。**

## 安全與來源盤點

- V1 實質章稿：`chapters/01-02-camera-language.md`；素材包：`chapters/01-02-camera-language-assets/`。
- 來源 ZIP CRC 檢查通過，SHA-256：`d448defde21abe8802ad87684928eaade0f7c39101b423159073391457a519a5`。
- 修改前備份：`backups/CH02-pipeline-20261018-215634/`；建置問題修正前備份：`backups/CH02-build-fixes-20261018/`；收尾備份：`backups/CH02-finalization-20261018/`。各資料夾含備份 manifest。
- V1 原稿、V2 canonical 中英文 scaffold、來源 ZIP 和全書 TOC 均未覆蓋或刪除。新章稿僅新增在 `staging/CH02-V4/`。

## 驗收清單

| 項目 | 狀態 | 證據及限制 |
|---|---|---|
| 素材盤點與備份 | PASS | ZIP CRC 及 SHA-256 已記錄；來源與 canonical 檔案雜湊在 `staging/CH02-V4/SOURCE-AND-ASSET-RECORD.json`。 |
| 繁體中文章稿 | PASS（草稿） | `staging/CH02-V4/zh-TW/CH02-camera-language.md`，13 個穩定節點 CH02-S00–S12；有學習目標、術語、原理與歷史、傳統流程、AI 轉換、提示詞示例、鏡頭案例、錯誤排查、評量與參考資料。 |
| 英文譯稿 | NEEDS HUMAN REVIEW | `staging/CH02-V4/en-US/CH02-camera-language.md` 為完整編譯草稿；尚未由專業雙語編輯核准。 |
| 中英逐節對照 | PASS（草稿對齊） | `staging/CH02-V4/CH02-alignment.yaml` 具 13 組穩定節點；自動測試確認雙語 ID 完整一致，語意等值仍待編輯審校。 |
| 雙語術語 | PASS（草稿） | `staging/CH02-V4/glossary-CH02.yaml` 有 26 個穩定 TERM-CH02 ID、中英詞條與工作定義；需專業術語審查。 |
| 參考來源 | PASS（可追溯；審查未完） | `staging/CH02-V4/references.bib`、`source-records/CH02-source-crosswalk.md`；繁中稿已補 R025–R029。Columbia 詞彙表用於攝影機運動和 180 度規則術語；American Cinematographer 文章支持《大白鯊》dolly zoom 實務案例；ZEISS、Canon 為製造商技術教育資料；Runway 指南僅用於特定版本產品操作，不當作普遍電影理論。教材版本／頁碼、電影版本和精確 timecode 待人工核實。 |
| 原創技術圖 | PASS（檔案；審核待辦） | 5 張專案撰寫的可編輯 SVG，XML 解析、SHA-256、雙語引用、圖說和 alt 欄位自動檢查通過。Manifest 將其標示為 draft、非實拍或工具實測；視覺、技術、可及性及權利終審 pending。 |
| 示範提示詞及 AI 實測 | NEEDS HUMAN REVIEW | 提示詞保持 not-run；未呼叫付費 API，未生成或冒稱存在點陣插圖。需在服務／費用／授權確認後實測並記錄模型版本與參數。 |
| 單元與架構測試 | PASS | `python -m unittest discover -s tests -v`：40/40；`v2_validate.py`、`validate_project.py`、`sync_site_content.py --check`、Python compile、`git diff --check` 通過。 |
| 雙語網站工具鏈 | PASS（現有網站基線） | Astro check：0 errors/warnings/hints；Astro build：123 頁。建置內容來自既有 canonical 檔案。CH02 V4 草稿尚未投影入站，因此 CH02 章節路由檢查 **BLOCKED（待編輯整合）**，不可把舊 scaffold 頁面當作本章驗收。沒有部署網站。 |
| DOCX 草稿 | PASS | Pandoc 3.12.1 建置中英各一份；DOCX ZIP CRC 通過，每份含 5 張內嵌圖像。輸出在 gitignored `dist/drafts/CH02-V4-20261018/`。 |
| PDF 草稿與字型 | PASS（技術檢查） | MiKTeX XeTeX 4.18 編譯中英 PDF。繁中 20 頁、英文 16 頁；繁中嵌入 Microsoft JhengHei，英文嵌入 Times New Roman，兩份皆含所需字型子集。PyMuPDF 文字擷取無 U+FFFD；五張插圖均與圖說同頁；繁中標籤為「圖」，英文為 “Figure”。抽查了含圖頁的渲染校樣。圈號 ①–⑥ 在草稿正文改為 (1)–(6)，避免 Times New Roman 缺字。 |
| EPUB 草稿與 EPUBCheck | PASS（技術檢查） | Pandoc 建置中英 EPUB；ZIP CRC、XHTML XML 解析、5 個 media 圖檔通過。官方 EPUBCheck 5.4.0 中英文均為 0 errors / 0 warnings / 0 informational / 0 references。繁中稿中的素材包 JSON 改以隨章素材包附檔文字說明呈現，避免 EPUB 指向封裝外路徑。 |
| 建置工具警告 | WARN | Pandoc 對 zh-TW 顯示缺少 `translations/zh.yaml` 及 Abstract/Table/Figure 詞彙翻譯的警告；專用 filter 已使 PDF 圖說標籤正確顯示「圖」，但其餘通用文件詞彙需在整書樣式審查時檢查。 |
| 章名及目錄 | NEEDS HUMAN REVIEW | Registry 的中文正式標題與來源副標題略有不同；registry 英文 title 尚空白。未擅改全書目錄。 |
| 作者出版核准 | NOT APPROVED | 章稿、英文譯稿及插圖均未取得作者／專業審查核准；不得標為 publication-ready。 |

## 草稿輸出

以下僅供編輯檢閱，不是正式出版物，並存於 gitignored 臨時目錄：

- `dist/drafts/CH02-V4-20261018/CH02-zh-TW.docx` / `.pdf` / `.epub`
- `dist/drafts/CH02-V4-20261018/CH02-en-US.docx` / `.pdf` / `.epub`
- 含圖頁聯校：`dist/drafts/CH02-V4-20261018/CH02-zh-TW-figure-pages.jpg`、`CH02-en-US-figure-pages.jpg`
- PDF 字型檢查由 `scripts/check_fonts.py --require-pdffonts` 完成。EPUBCheck 5.4.0 官方發行包僅下載至 gitignored `tmp/epubcheck-5.4.0/`；ZIP SHA-256 `33350c61038e71dfb3d45a76aed04bf5481e6d5500cb780f6e98db8bbd15a28c`。

## 尚待完成

1. 專業審閱 13 組中英節次與 26 個術語，確認英文不是逐字硬譯。
2. 查核教科書採用版次與章節／頁碼定位；不填入未核實頁碼。
3. 依合法可觀看版本確認《大白鯊》鏡頭案例的片段及 timecode，逐項核對文字描述。
4. 確認第二章中英文正式章名，並與全書 TOC/registry 同步。
5. 審閱 5 張 SVG 的技術正確、閱讀性、色彩對比、雙語字體與印刷縮放，再核准權利狀態。
6. 作者核准後，才將 staging 內容整合到 canonical 雙語稿；接著建置及檢查 CH02 的中英文網站路由和圖稿呈現。
7. Pandoc zh-TW 翻譯警告需由出版樣式負責人決定是否建立自訂翻譯字串，再做整書樣章校樣。

## 章末全項目稽核（2026-10-18）

此稽核逐項檢查本章 staging 稿、alignment、術語、source crosswalk、SVG、run log 及本報告所記錄的草稿輸出。狀態只反映具體證據；技術建置通過不等於內容或權利核准。

### 內容完整性

| 必要項目 | 狀態 | 證據 | 待辦／責任角色 |
|---|---|---|---|
| 學習目標 | PASS | 繁中 staging 稿 13 節中含可觀察學習目標；英文稿有相應內容。 | 英文與教學措辭仍納入雙語編輯審校。 |
| 先備知識 | PASS | 中英章稿均有先備知識區塊。 | 無結構缺漏。 |
| 專業名詞中英文對照與定義 | NEEDS HUMAN REVIEW | `staging/CH02-V4/glossary-CH02.yaml` 有 26 個 TERM-CH02 雙語詞條；自動 ID 對齊通過。 | 電影攝影／剪輯專業編輯確認定義、慣用譯名及易混淆詞。 |
| 電影製作歷史與基本原理 | NEEDS HUMAN REVIEW | 中英稿含歷史與原理說明，參考來源列於 `references.bib`、source crosswalk。 | 研究編輯逐項確認歷史主張、理論脈絡及來源支持範圍。 |
| 傳統電影製作方法 | PASS | 中英稿說明傳統攝影機、鏡頭、場面與剪接流程，並列出實務步驟。 | 專業準確性仍待整體編輯審讀。 |
| AI 時代技術轉換、能力與限制 | NEEDS HUMAN REVIEW | 章稿含 AI 影像／影片工具與傳統流程比較；Runway 指南只支撐特定供應商版本。 | 技術編輯確認時效性、工具版本及一般原理與廠商功能的界線。 |
| 詳細工作流程 | PASS | 中英稿含 13 組穩定節點，含輸入、運鏡／剪接決策與檢查步驟。 | 英文語意對照仍需人工校讀。 |
| 提示詞與技術參數（含版本／未實測聲明） | PASS | 兩語稿含提示詞示範及參數說明；run log 明記提示詞 not-run、未呼叫付費服務。 | 如需主張工具效果，須另作授權實測並保存模型版本與輸出。 |
| 實際鏡頭／影片案例與來源 | NEEDS HUMAN REVIEW | 《大白鯊》dolly zoom 案例引用 American Cinematographer；目前未記錄已核實的合法版次及精確 timecode。 | 作者／研究編輯選定可合法觀看版本並核對片段與描述。 |
| 常見錯誤與品質驗證 | PASS | 中英章稿含運鏡／軸線／鏡頭選擇錯誤及檢查方式。 | 編輯確認 QA 建議與本書術語一致。 |
| 練習與評量 | PASS | 中英稿含練習交付與評量內容。 | 教學編輯可進一步確認評分規準與讀者程度。 |
| 延伸研究 | PASS | 章稿設有延伸研究問題。 | 無自動出版阻擋；可由研究編輯審閱。 |
| 主張分類及引用可追溯性 | NEEDS HUMAN REVIEW | R025–R029、source crosswalk 與段落來源已建立；Columbia、ASC、ZEISS、Canon、Runway 各自限制已說明。 | 研究編輯核對教材版次／頁碼及每項主張實際支持範圍；不得補猜頁碼。 |

### 雙語、素材與出版完整性

| 必要項目 | 狀態 | 證據 | 待辦／責任角色 |
|---|---|---|---|
| 中英文節次、穩定 ID、術語、案例和圖號逐項對齊 | PASS | `CH02-alignment.yaml` 及自動測試確認 13 組節點 ID 一致；圖稿及術語 ID 成對。此項只判結構對齊。 | 語意等值獨立列於下一項審校。 |
| 中英文語意、單位、引用位置及專業用語編輯狀態 | NEEDS HUMAN REVIEW | 兩語 staging 稿均存在，英文為可讀編譯草稿。 | 專業雙語編輯逐節對照、修訂並留下姓名／日期／稿版。 |
| 來源存在、版本／日期／頁碼或 locator 已核對 | NEEDS HUMAN REVIEW | 5 筆來源及 2026-10-18 查閱日期記錄於 source crosswalk；未填未核實頁碼。 | 編輯確認原始頁面、適用版本和精確 locator。 |
| 電影案例版次、合法觀看來源與 timecode | NEEDS HUMAN REVIEW | 報告及 run log 均明確記錄尚未選定合法版次／timecode。 | 作者／研究編輯提供版次、合法來源及核看片段記錄。 |
| 原稿及素材備份、差異與保留情形 | PASS | `backups/CH02-pipeline-20261018-215634/`、`CH02-build-fixes-20261018/`、`CH02-finalization-20261018/` 含備份 manifest；V1 與 canonical V2 未覆蓋。 | 保留 staging 作草稿；canonical 整合待人工核稿。 |
| 圖片／SVG 原檔、hash、生成或繪製紀錄 | PASS | 5 張專案撰寫 SVG 及 SHA-256 記錄於 `staging/CH02-V4/` manifest／source record；非 AI 圖片生成或外部下載。 | 設計者／編輯確認完整繪製履歷及版本記錄是否滿足正式檔案標準。 |
| 圖號、雙語標題／圖說／alt 與正文位置 | PASS | 5 張 SVG 已插入兩語 staging 稿，圖說／alt 欄位及 ID 檢查通過。 | 文字與閱讀順序需配合人工圖面審校。 |
| 圖片權利、相似性、肖像及標誌人工審查 | NEEDS HUMAN REVIEW | 資產標記為 project-authored SVG；manifest 未設最終核准。 | 作者／權利審查人確認來源、相似性、第三方素材及出版狀態。 |
| SVG 技術正確性、可編輯性、可及性及印刷檢視 | NEEDS HUMAN REVIEW | XML 解析、hash 與輸出格式測試通過，SVG 保留可編輯。 | 專業編輯實際檢查技術比例、對比、雙語字型、閱讀順序及印刷縮放。 |
| 中英文網站路由、內容、ID、圖檔及 alt | BLOCKED | Astro 基線 check/build 為 0 診斷／123 頁；CH02 staging 尚未整合到 canonical，未測 CH02 route。 | 雙語編輯核稿後整合並建立章節頁，再測路由、資產和內容。 |
| DOCX 草稿建置與內嵌素材 | PASS | `dist/drafts/CH02-V4-20261018/` 中英 DOCX；封裝 CRC 通過、每份 5 張內嵌圖。 | 草稿，不代表內容已核准。 |
| PDF 建置、字型嵌入及繁中實際渲染 | PASS | 同目錄中英 PDF；20／16 頁，Microsoft JhengHei／Times New Roman 實際嵌入，PyMuPDF 抽取與含圖頁渲染抽查完成。 | 最終出版仍需全頁校樣及編輯核准。 |
| 中英文 EPUB 結構、雙語顯示及 EPUBCheck | PASS | 同目錄中英 EPUB；EPUBCheck 5.4.0 兩語均 0 errors／warnings／informational／references，封裝及 XHTML、5 張圖片通過。 | 需在目標閱讀器完成出版級閱讀校樣。 |
| 連結檢查及網路不確定項目 | NOT RUN | 本次 CH02 報告未提供逐連結檢查輸出；引用 URL 列於來源 crosswalk。 | 執行連結檢查並分類可核實、登入限制、暫時失敗及失效項。 |
| 單元、整合、專案結構與出版品質測試 | PASS | 40/40 unittest；`v2_validate.py`、`validate_project.py`、`sync_site_content.py --check`、compile、`git diff --check` 通過。 | 網站章節路由獨立維持 BLOCKED。 |
| registry、翻譯狀態及章節 metadata 同步 | NEEDS HUMAN REVIEW | run.json 中正式英文 title 空白、canonical 仍為 planned／translation-needed；staging 未寫入全書 registry。 | 編輯核定雙語正式章名後，再更新 registry／translation state。 |
| run log、history、備份 manifest 與重現指令 | PASS | run：`production/runs/CH02/20261018T215615+0800-55868375/run.json`；本報告列出主要建置工具／版本與備份路徑；本稽核同步寫入 `history.md`。 | 如需重現，依報告路徑與工具版本重建草稿。 |
| 作者／專業審稿人／權利核准狀態 | NEEDS HUMAN REVIEW | 尚無作者出版核准或專業審稿簽核記錄。 | 作者、雙語／研究／視覺／權利編輯逐項簽核。 |
| 未發布網站、未推送等授權邊界 | PASS | 本次僅本機建置草稿，未部署、未 commit、未 push；run log 和 history 有記錄。 | 若未來要發布或推送，需另有明確授權。 |

### 章末稽核結論

- 各狀態數量：PASS 18；FAIL 0；BLOCKED 1；NEEDS HUMAN REVIEW 12；NOT RUN 1。
- 可交付的草稿工作是否完成：是；繁中 staging 稿、英文編譯草稿、術語／對照、SVG 與 DOCX／PDF／EPUB 草稿及自動檢查證據均已交付。
- 是否達正式出版標準：否。未完成網站章節路由、連結檢查、來源／案例核驗、雙語與術語編輯、SVG／權利審查及作者核准。
- 尚未完成項目與解除條件：由雙語／電影研究／出版／視覺權利編輯處理本表 NEEDS HUMAN REVIEW；由章節編輯整合 canonical 後解除網站 BLOCKED；由工程執行者跑連結檢查解除 NOT RUN。
- 本章稽核完成日期：2026-10-18（Asia/Taipei）。
- 本章報告交付後停止；下一章由使用者另行指定。

## 本次正式外部來源

- Columbia University, [Camera Movement](https://filmglossary.ccnmtl.columbia.edu/term/camera-movement/) 與 [180-Degree Rule](https://filmglossary.ccnmtl.columbia.edu/term/180-degree-rule/)，查閱日期 2026-10-18。
- Jay Holben, [“Shot Craft: Tools for Camera Movement”](https://theasc.com/article/shot-craft-camera-movement/), *American Cinematographer*, 2024-04-05，查閱日期 2026-10-18。
- ZEISS, [“Zoom or Prime Lens? A Shootout Comparison”](https://lenspire.zeiss.com/photo/en/article/1-zoom-or-prime-lens-a-shootout-comparison/)，查閱日期 2026-10-18。
- Canon Europe, [Depth of Field](https://files.canon-europe.com/files/webcontent/rf-lens-world/knowledge/depth-of-field/index.html)，查閱日期 2026-10-18。
- Runway Help Center, [Gen-4 Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide)，查閱日期 2026-10-18；產品版本與功能具時效性。
- EPUBCheck 5.4.0 為 [W3C/DAISY 發布的 EPUB 一致性檢查工具](https://github.com/w3c/epubcheck/releases/tag/v5.4.0)，查閱日期 2026-10-18。

未發布網站、未 commit/push GitHub，未刪除或覆蓋 V1/V2 原稿及既有素材。
