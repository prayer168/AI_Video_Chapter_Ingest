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

## 本次正式外部來源

- Columbia University, [Camera Movement](https://filmglossary.ccnmtl.columbia.edu/term/camera-movement/) 與 [180-Degree Rule](https://filmglossary.ccnmtl.columbia.edu/term/180-degree-rule/)，查閱日期 2026-10-18。
- Jay Holben, [“Shot Craft: Tools for Camera Movement”](https://theasc.com/article/shot-craft-camera-movement/), *American Cinematographer*, 2024-04-05，查閱日期 2026-10-18。
- ZEISS, [“Zoom or Prime Lens? A Shootout Comparison”](https://lenspire.zeiss.com/photo/en/article/1-zoom-or-prime-lens-a-shootout-comparison/)，查閱日期 2026-10-18。
- Canon Europe, [Depth of Field](https://files.canon-europe.com/files/webcontent/rf-lens-world/knowledge/depth-of-field/index.html)，查閱日期 2026-10-18。
- Runway Help Center, [Gen-4 Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide)，查閱日期 2026-10-18；產品版本與功能具時效性。
- EPUBCheck 5.4.0 為 [W3C/DAISY 發布的 EPUB 一致性檢查工具](https://github.com/w3c/epubcheck/releases/tag/v5.4.0)，查閱日期 2026-10-18。

未發布網站、未 commit/push GitHub，未刪除或覆蓋 V1/V2 原稿及既有素材。
