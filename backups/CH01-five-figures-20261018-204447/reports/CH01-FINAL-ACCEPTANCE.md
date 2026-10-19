# CH01 V2.0 最終驗收報告（稿件版 2.1.0）

- 驗收日期：2026-10-18（Asia/Taipei）
- 驗收範圍：CH01 繁體中文／英文 canonical 稿、術語與參考資料、翻譯對照、原創插圖紀錄、網站及章節級 PDF／EPUB 草稿
- 狀態：**章節內容已補齊；未達正式出版標準，等待作者及專業審校**
- 修改前備份：`backups/CH01-editorial-20261018-193937/MANIFEST.json`（含修改前與備份 SHA-256）
- 此報告取代舊版空白區塊檢查結論；舊報告保留作歷史紀錄。

## 驗收摘要

先前列出的 9 個空白必要區塊已補成繁中及英文正文，並新增結語區塊。兩語稿均有 13 個相同穩定 section anchors、五組同 ID 電影案例，以及完整的 6 鏡頭虛構教學示範。26 個雙語術語已建立於 V2 glossary；逐節／案例／術語／圖說配對表見 `metadata/translations/CH01-alignment.yaml`。

原創插圖目前仍是 **5 份 briefs、0 張實際圖檔**。章稿沒有嵌入任何圖片；圖說和 alt 僅為待核准文字，不代表成品存在或權利已核准。中英文章節級 PDF 與 EPUB 草稿已產生並通過技術檢查；正式全書建置仍受章節審稿狀態 gate 阻擋。

## 必要章節內容

| ID | 區塊 | 內容結果 | 狀態 |
|---|---|---|---|
| CH01-S01 | 學習目標／Learning objectives | 五項可觀察學習目標及學習證據 | PASS（結構與有內容）；目標適切性待教師審閱 |
| CH01-S02 | 先備知識／Prerequisites | 經驗、設備與 AI 工具版本查核說明 | PASS；教學對象需作者確認 |
| CH01-S03 | 核心術語／Key terms | 26 個中英詞條、工作定義與易混淆概念 | PASS（資料存在）；術語定義及頁碼待審 |
| CH01-S04 | 歷史與基本原理／History and principles | 電影形式、限定於美國 1907–1913 的早期史料、剪接脈絡、場面調度 | PASS（正文與來源）；歷史／理論專家需核對 |
| CH01-S05 | 傳統製作方法／Traditional production practice | 場景、空間、coverage、連戲、素材與剪輯流程 | PASS（正文）；依特定製作制度的差異待編輯檢查 |
| CH01-S06 | AI 轉換與限制／AI-era workflow and limitations | 傳統工作與 AI 協作對照、驗收證據及未測功能標示 | PASS（正文）；未聲稱任何特定工具已實測 |
| CH01-S07 | 詳細工作流程／Step-by-step workflow | 10 個鏡頭級製作與封存步驟 | PASS（正文）；流程可用性待製片實務者審閱 |
| CH01-S08 | 提示詞與技術參數／Prompt and technical parameters | 中立範本與玻璃杯虛構示範，明確不宣稱工具實測 | PASS（範本）；需指定工具實測版才可提供確切參數 |
| CH01-S09 | 鏡頭／影片案例／Shot and film cases | 5 組中英案例及 6 鏡頭虛構短片示範 | PASS（內容和配對）；版本／片段 timecode 待看片人補錄 |
| CH01-S10 | 錯誤與品質檢查／Errors and QA | 瑕疵表、逐鏡檢核及 PASS／FAIL／NEEDS HUMAN REVIEW 記錄方式 | PASS（正文）；實際作品尚未提供測片 |
| CH01-S11 | 練習與評量／Exercises and assessment | 30–60 秒作業、100 分規準及研究問題 | PASS（正文）；需教師試用並校準評分錨點 |
| CH01-S12 | 來源／References | 具來源 ID、連結、日期／版本及限制說明 | PASS（可追溯）；有未完成定位及人工連結複查項 |
| CH01-S13 | 結語／Conclusion | 本章總結與 CH02 銜接 | PASS（正文） |

自動完整度測試 `tests/test_ch01_content.py` 逐節確認中英文都有實質文字，避免只有標題或佔位文字。此測試不能判定內容學術正確、翻譯自然或教學有效。

## 中英對照、術語與來源

| 檢查 | 結果 | 證據與限制 |
|---|---|---|
| 逐節錨點 | PASS | 繁中及英文均有 CH01-S01–S13；自動比對通過。 |
| 電影案例 | PASS（配對） | `CH01-P001`–`CH01-P005` 對應 *Citizen Kane*、*Rashomon*、*A City of Sadness*、*In the Mood for Love*、*Yi Yi*。 |
| 術語 | PASS（資料完整） | 26 個 ID、中文／英文首選詞與雙語定義已登錄於 `metadata/terminology.yaml`。全部保持 `draft`；教科書版本及頁碼／章節 locator 尚未人工核對。 |
| 翻譯管理 | PASS（結構配對） | `metadata/translations/CH01-alignment.yaml` 對照 13 節、26 詞條、5 案例、5 圖說及共享來源。中英稿均為 `review-needed`，英文尚非人工核准譯稿。 |
| 電影案例主張 | NEEDS HUMAN REVIEW | BFI／Criterion 等條目與評論已列來源；作者仍需指定合法觀看版本、記錄發行／修復版、播放來源、時間碼及逐鏡觀察。R016 是《海上花》評論中提及《悲情城市》片段，不是該片專論；原稿不再以其支撐長鏡頭／門框主張。 |
| 研究來源 | PARTIAL / NEEDS HUMAN REVIEW | R005（2016）及 R024（2024）研究書目及摘要資訊已查；需研究編輯閱讀完整方法、材料及限制。R023 Ned Thanhouser／Library of Congress 來源只支撐其明列的美國電影時段，不外推為全球電影史。R001《Film Art》尚無本章實際版本頁碼。 |
| 外部連結 | NEEDS HUMAN REVIEW | 自動檢查結果列於下方測試表；未能定論的來源不能僅按「未失敗」視為有效。出版前請編輯重試及保存來源快照。 |

## 插圖檔案與權利

| 檢查 | 結果 | 證據 |
|---|---|---|
| CH01 V2 實際圖片檔 | BLOCKED（尚未製作） | 遞迴檢查 `assets/chapters/CH01/`，找到 5 個 briefs 及 manifest，沒有 raster 或 SVG 圖檔。 |
| 圖片紀錄 | PASS（待製作紀錄） | `assets/chapters/CH01/figure-manifest.yaml` 登錄五個 ID、雙語 caption／alt、brief 路徑；`asset_original`、`asset_approved`、tool/version/date 均為 null。 |
| 權利／技術／編輯審查 | NEEDS HUMAN REVIEW | 五項皆為 `pending`。尚無圖片成品可審肖像、商標、構圖相似、文字、向量可編輯性或圖說一致性。 |
| 章稿引用圖片 | PASS | 兩語 Markdown 均 0 個嵌入圖片及外部圖片 URL；未用網路第三方圖片填補缺圖。 |
| 舊 V1 資產 | NEEDS HUMAN REVIEW | 專案既有 `ASSET-CH01-FIG-01` 權利資料仍待查；目前 V2 CH01 沒有引用它。全專案正式圖像 gate 仍須由作者補權利證據或明確記錄排除。 |

圖說及 alt 是版面文案草稿，不是已製作或已獲授權的圖片。缺圖不得輸入正式書籍或網站發行版。

## 實測與自動化檢查

| 項目 | 結果 | 證據 |
|---|---|---|
| 內容完整度與引用錨點測試 | PASS | `python -m unittest discover -s tests -v`：27/27；包含 5 個新增 CH01 測試。 |
| V2 metadata／章節／圖像政策 | PASS | `python scripts/v2_validate.py`：12 篇、60 章、雙語 scaffold、遷移雜湊、圖像 policy 通過。 |
| 專案 registry | PASS | `python scripts/validate_project.py`：12 parts、60 chapters、52 個全域舊制 terms、24 references。CH01 另有 26 個 V2 術語詞條。 |
| canonical → 網站投影 | PASS | `python scripts/publishing/sync_site_content.py --check` 通過。 |
| 雙語網站診斷 | PASS（最新檢查） | `npm --prefix apps/web run check`：0 errors、0 warnings、0 hints。更新 CH01 投影後的第一次增量檢查曾對兩個既有 CH01 IDs 印出 duplicate ID 訊息；檢查 Astro loader 後確認它在更新同 ID、不同 digest 的舊 store entry 時也會使用此訊息。立即重跑後 0 warnings；source tree 每個語系各只有一個 CH01 檔案。 |
| 雙語網站靜態建置 | PASS | 更新完成後的 `npm --prefix apps/web run build`：123 頁，無 duplicate ID 警告；包含 `/zh-tw/ch01-cinematic-language/` 及 `/en/ch01-cinematic-language/`。未發布。 |
| PDF 草稿 | PASS（章節樣張） | Pandoc 3.12.1 + MiKTeX XeLaTeX 生成中英章稿於 `tmp/CH01-revision-2.1.0-20261018/`；`pdftotext` 可抽取中英標題及術語。 |
| PDF 字型嵌入 | PASS（章節草稿） | `scripts/check_fonts.py --require-pdffonts`：中英字型均有 `emb=yes`、`sub=yes`、`uni=yes`；繁中字型 Microsoft JhengHei，英文字型 Times New Roman，英文亦嵌入 CJK fallback。兩份 XeLaTeX log 的缺字警告數皆 0。 |
| PDF 視覺抽查 | PASS（有限樣本） | 繁中頁 2–4 PNG 已抽查；雙欄術語表版面可讀，表格延頁有續頁標頭。全 13 頁及英文全頁仍需出版校樣。 |
| EPUB 生成 | PASS（章節草稿） | Pandoc 生成 `CH01-zh-TW-V2.1.0-draft.epub` 及 `CH01-en-US-V2.1.0-draft.epub`。 |
| EPUBCheck | PASS（結構符合） | EPUBCheck 5.4.0：兩份各 0 errors、0 warnings、0 informational messages、0 references；初次測試發現引用錨點缺失，已補 anchor 並重新建置，重測通過。 |
| 外部連結檢查 | PASS／部分待核 | `python scripts/validate/check_links.py`：0 failures；5 個網路連結未獲結論，未檢查不代表連結失效或有效。 |
| 正式圖像權利 gate | BLOCKED（預期） | `python scripts/image_policy.py --target zh-TW-book` 因舊 V1 `ASSET-CH01-FIG-01` 的 approval、rights、creator、attribution 和 publication permission 欄位未解而 exit 2。V2 CH01 沒有引用該圖，但本 gate 是全專案資產檢查。 |
| 正式書籍 builder | BLOCKED（預期） | `python scripts/publishing/build_books.py --locale zh-TW --format pdf` 及 `--locale en-US --format epub` 均 exit 2：CH01 尚非 editorially approved，符合防止未審稿輸出的設計。 |
| `git diff --check` | PASS | 無 whitespace error；輸出僅有 repo 既有 LF/CRLF 轉換提醒。 |
| V1 原稿保護 | PASS | 原始 V1 不在本輪修改清單；migration SHA-256 regression test 通過；本次另在修改前備份 V2 工作檔。 |
| 正式全書 PDF／EPUB | BLOCKED（預期） | `scripts/publishing/build_books.py` 只允許 60 章全部 `approved` 後出版。CH01 為 `review-needed`，其餘章節仍為 scaffold／未核准；本輪只建章節級草稿校樣。 |
| 網站部署／GitHub push | NOT PERFORMED | 未部署網站、未 commit、未 push。 |

### 草稿產物路徑

- `tmp/CH01-revision-2.1.0-20261018/CH01-zh-TW-V2.1.0-draft.pdf`
- `tmp/CH01-revision-2.1.0-20261018/CH01-en-US-V2.1.0-draft.pdf`
- `tmp/CH01-revision-2.1.0-20261018/CH01-zh-TW-V2.1.0-draft.epub`
- `tmp/CH01-revision-2.1.0-20261018/CH01-en-US-V2.1.0-draft.epub`

以上位於本機草稿／暫存目錄，不是核准版出版物；勿以其檔名或技術通過推定正式完稿。

## NEEDS HUMAN REVIEW：具體剩餘工作

1. **作者／電影研究者看片：** 為五部案例逐一選定可合法觀看的版次，填入發行／修復版、來源、精確時間碼、鏡頭描述及觀察者；核對影評所指片段與正文解讀。沒有可看片源就保留待審，不猜時間碼。
2. **電影史／理論審稿：** 對照 R001 所採 13 版實體／電子書，補 S04 及術語的章節／頁碼；評估早期電影史敘述是否需加入其他地區史料；研究編輯完整核讀 R005 與 R024 的方法和結果。
3. **中英文專業編輯：** 審校 title、每節語義、電影專名／譯名、術語首選、自然度、文化語境及引用格式。驗收後才可把兩語狀態從 `review-needed` 改成 approved。
4. **完成五張原創圖：** 依五份 briefs 製作可編輯 SVG 或原創生成圖。登記實際檔案、作者／工具／版本／日期、提示詞或繪圖來源、修改紀錄、雜湊、權利風險審查及中英文 caption／alt；再分別做權利、技術、編輯核准。無圖可選擇明確從章稿排除，並保留決策紀錄。
5. **解決 V1 資產紀錄：** 查 `ASSET-CH01-FIG-01` 的來源和授權；若不用於 V2，須在資產 registry 記錄排除決策，不能假裝已取得授權。
6. **教育短片案例：** 如用於自然科學教學，請學科教師驗證玻璃杯／晨光表現；目前明確是故事示範，不是科學事實的實驗紀錄。
7. **完整出版校樣：** 人工核准稿與圖像後，重建網站、PDF、EPUB；逐頁檢查兩語字形、表格跨頁、目錄、引文連結、圖說、alt、EPUB 閱讀器相容性及正式輸出 metadata。正式 60 章建置需在其餘章節也完成核准後再執行。

## 最終判定

**CH01 是否已達到正式出版標準？否。** 內容骨架與雙語草稿已由本輪補齊；技術草稿建置通過，但電影片段校核、理論頁碼、英文專業審稿、實際插圖／權利核准與完整全頁校樣仍未完成。現階段狀態為 `review-needed`，不是正式出版完成。
