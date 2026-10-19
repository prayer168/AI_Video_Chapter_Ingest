# CH01 V2.1.0 最終驗收報告（雙語稿與五張插圖校樣）

> V4 pipeline validation addendum (2026-10-18): this report's existing editorial/rights verdict remains in force. The V4 test report is `CHAPTER-PIPELINE-TEST-REPORT.md`; its 35-test suite and bilingual 123-page website build passed. Existing CH01 finalproof PDF/EPUB evidence was reused because canonical CH01 sources were unchanged. The five illustrations remain pending review, and CH01 is **not publication-ready**. No image API, deployment, or GitHub push was used.

- 驗收日期：2026-10-18（Asia/Taipei；插圖匯入、版面修正與重建）
- 驗收範圍：CH01 繁體中文／英文 canonical 稿、術語與參考資料、翻譯對照、原創插圖紀錄、網站及章節級 PDF／EPUB 草稿
- 狀態：**章節內容已補齊；未達正式出版標準，等待作者及專業審校**
- 修改前備份：`backups/CH01-five-figures-20261018-204447/BACKUP-MANIFEST.json`（含修改前與備份 SHA-256）
- 此報告取代舊版空白區塊檢查結論；舊報告保留作歷史紀錄。

## 驗收摘要

先前列出的 9 個空白必要區塊已補成繁中及英文正文，並新增結語區塊。兩語稿均有 13 個相同穩定 section anchors、五組同 ID 電影案例，以及完整的 6 鏡頭虛構教學示範。26 個雙語術語已建立於 V2 glossary；逐節／案例／術語／圖說配對表見 `metadata/translations/CH01-alignment.yaml`。

五張 CH01 原創 AI 插圖已由下載資料夾的 ZIP 匯入 assets/chapters/CH01/figures/originals/，並插入繁中／英文稿。永久圖號維持 CH01-HOMAGE-FIG-001–005，顯示標籤為 1-3A、1-4A、1-4B、1-4C、1-5A。五張圖一律為 draft-generated、original-ai-illustration-pending-final-review；沒有任何圖片或章稿被標記為正式核准。網站、章節級 PDF／EPUB 技術草稿通過；作者及權利／電影研究／雙語編輯審查仍未完成。

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

五張 PNG 來自 C:/Users/user/Downloads/AI-Video-Bible-CH01-Five-Homage-Images-DRAFT.zip。python -m zipfile -t 通過；ZIP manifest 內五筆 SHA-256 均與匯入後原圖相符。目標 assets/chapters/CH01/figures/originals/ 原本已存在且沒有同名圖，五檔均以 imported 匯入，未覆蓋既有素材。檔案均為 PNG、1619 × 971 px；完整來源名、檔案大小、ZIP 與 PNG SHA-256 見 assets/chapters/CH01/figures/IMPORT-AND-RIGHTS-RECORD.md。

| 永久 figure ID | 顯示標籤 | 原始 PNG | SHA-256（完整值見來源紀錄） | 狀態 |
|---|---|---|---|---|
| CH01-HOMAGE-FIG-001 | 圖 1-3A | CH01-HOMAGE-001-Citizen-Kane.png | e19bb861…61266de0 | draft-generated / pending review |
| CH01-HOMAGE-FIG-002 | 圖 1-4A | CH01-HOMAGE-002-Rashomon.png | 298d54dc…57d2577 | draft-generated / pending review |
| CH01-HOMAGE-FIG-003 | 圖 1-4B | CH01-HOMAGE-003-A-City-of-Sadness.png | 339ef01d…e6e8a43 | draft-generated / pending review |
| CH01-HOMAGE-FIG-004 | 圖 1-4C | CH01-HOMAGE-004-In-the-Mood-for-Love.png | 18975a63…4f624f5 | draft-generated / pending review |
| CH01-HOMAGE-FIG-005 | 圖 1-5A | CH01-HOMAGE-005-Yi-Yi.png | 73cb8d09…44305aed | draft-generated / pending review |

| 檢查 | 結果 | 證據與限制 |
|---|---|---|
| 圖檔、格式、尺寸及 SHA-256 | PASS | 5/5 為 PNG，1619 × 971 px；ZIP manifest 雜湊與匯入檔逐一一致。 |
| 永久圖號與章節位置 | PASS | 未改原 manifest IDs。圖 1-3A 位於 S02 後；1-4A 位於 S04 中段；1-4B 接 S04 的空間／場面調度論述；1-4C 位於 S04 後段；1-5A 位於 S05 與 S06 間。 |
| 雙語 caption 與 alt | PASS（草稿配對） | figure-manifest.yaml、metadata/figure-registry.yaml、CH01-alignment.yaml、figure-captions.md 及兩語正文一致；中英圖說均保留原創示意、參考片名、不是電影原劇照的明確聲明。 |
| 網站圖像輸出 | PASS | 中英文 CH01 頁各有 5 個帶永久 ID 的內容 figure、5 張圖、5 個圖說及非空 alt；最終 HTML 所有 ID 唯一，靜態資產雜湊與 canonical PNG 相同。 |
| 圖像來源與生成紀錄 | PARTIAL / NEEDS HUMAN REVIEW | ZIP README 僅聲明 AI-generated；逐圖來源檔名、archive／image hash、尺寸和匯入日期已記錄。工具、模型、版本、生成日期、完整提示詞、操作者及修改歷程未提供，故明確記為未知。 |
| 權利／技術／編輯核准 | NEEDS HUMAN REVIEW | 五項 rights_review、technical_review、editorial_review 均為 pending；asset_approved 為 null，publication_status 為 pending-publication-approval。不得將草稿上架或宣稱權利已清除。 |
| 原 brief 與成品一致性 | NEEDS HUMAN REVIEW | 目前生成圖均為寫實電影感場景，與既有部分向量圖／平面圖 brief 有實質差異；作者須決定接受為原創示意圖、要求重製，或排除。 |
| 相似性及第三方權利風險 | NEEDS HUMAN REVIEW | 尤其需人工檢視人物／演員 likeness、服裝、場景、美術、構圖、地標和歷史敘事；圖說引用電影不構成授權，也不保證不侵權。 |
| V1 舊資產 gate | BLOCKED（既存問題） | python scripts/image_policy.py --target zh-TW-book exit 2；列出 V1 ASSET-CH01-FIG-01 的創作者、授權、署名及出版許可未解。此舊政策工具尚不涵蓋 V2 manifest；V2 五圖的 pending 狀態另由 CH01 manifest、build gate 及測試明確保留。 |

所有圖片均維持待審狀態；本次僅產生本機建置與出版校樣，不代表正式出版許可。

## 實測與自動化檢查

| 項目 | 結果 | 證據 |
|---|---|---|
| 章節／圖檔／中英對照單元測試 | PASS | python -m unittest discover -s tests -v：29/29；包含圖檔存在、PNG signature／SHA、永久 ID、雙語 caption/alt、網站投影圖號測試。 |
| V2 架構驗證 | PASS | python scripts/v2_validate.py：12 篇、60 章 registry、雙語 scaffold、V1 遷移雜湊等通過；此測試非權利核准。 |
| 專案 registry | PASS | python scripts/validate_project.py：12 parts、60 chapters、52 legacy terms、24 references；CH01 另有 26 個 V2 術語。 |
| canonical → 網站資產同步 | PASS | python scripts/publishing/sync_site_content.py --check：雙語 Markdown、5 張 canonical PNG 及輸出副本均同步。 |
| Astro 診斷與網站建置 | PASS（本機草稿） | npm --prefix apps/web run check：0 errors／warnings／hints；載入修改後舊 store 曾印 duplicate-ID cache 訊息，建置重載後無 duplicate-id，實際診斷數為零。npm --prefix apps/web run build：123 頁完成；未部署。 |
| 網站圖片／ID／alt | PASS | 繁中與英文頁各 5 張圖片、5 個 figure IDs、5 個 figcaption、5 個非空 alt；dist 圖片存在且雜湊相符。 |
| PDF 草稿與字型 | PASS（章節校樣） | 最新中英 PDF 由 PyMuPDF `get_page_fonts`／`extract_font` 抽取 6／7 個實際嵌入字型串流；英文含 Times New Roman、繁中含 Microsoft JhengHei。逐頁抽文字及 raster 視覺校樣確認繁體圖名與中英字形可讀。此為草稿實測，正式版仍須出版全頁校樣。 |
| PDF 圖說／圖號排版 | PASS（本機校樣，非正式出版） | 修正首圖引言重複圖號及繁中圖名後，重新建置；PyMuPDF 抽文字及逐一渲染含圖頁確認：5 張圖均在含其完整圖說的頁面上，中英文各圖號只作為圖說標籤出現一次。頁面 PNG 存於 `visual-review-finalproof/`。 |
| EPUB 生成及 XHTML 圖像 | PASS | Pandoc 章節草稿；最新兩語 EPUB 結構及內容檢查確認各含 5 個 figure、5 張圖、5 個非空 alt、5 個穩定 ID。 |
| EPUBCheck | PASS | EPUBCheck 5.4.0，繁中及英文各 0 errors、0 warnings、0 informational messages、0 references。 |
| Pandoc 語系提示 | WARNING（非阻斷） | zh-TW EPUB 建置時 Pandoc 提示 translations/zh.yaml 未載入及 Abstract 無譯名；EPUBCheck 仍 0 錯誤／警告。正式出版前可補 zh 本地化字串或確認模板輸出。 |
| 外部參考連結 | PARTIAL | python scripts/validate/check_links.py：0 failures、5 個網路 URL 未獲結論；未核實不等於有效或失效。 |
| git diff --check 與 Python 語法 | PASS | whitespace check 無錯；僅見既有 LF→CRLF 提示。相關 Python scripts 與 test files py_compile 通過。 |
| 正式圖像出版 gate | BLOCKED（預期） | V1 ASSET-CH01-FIG-01 全專案 rights fields 尚未解；V2 五圖仍 pending。 |
| 正式書籍建置 | BLOCKED（預期） | CH01 仍 review-needed、translation 未 approved、五圖 pending；正式 60 章輸出 gate 應拒絕。 |
| V1 原稿／圖片保護 | PASS | 沒有修改 V1 原稿或既有原圖；五張原圖均為新檔匯入。GitHub push、commit、網站發布均未執行。 |

### 草稿產物路徑

- tmp/CH01-V2.1.0-five-figures-20261018/CH01-zh-TW-V2.1.0-five-figures-finalproof.pdf
- tmp/CH01-V2.1.0-five-figures-20261018/CH01-en-US-V2.1.0-five-figures-finalproof.pdf
- tmp/CH01-V2.1.0-five-figures-20261018/CH01-zh-TW-V2.1.0-five-figures-finalproof.epub
- tmp/CH01-V2.1.0-five-figures-20261018/CH01-en-US-V2.1.0-five-figures-finalproof.epub
- tmp/CH01-V2.1.0-five-figures-20261018/visual-review-finalproof/（中英文全部含圖頁 PNG；暫存）
- apps/web/dist/zh-tw/ch01-cinematic-language/index.html
- apps/web/dist/en/ch01-cinematic-language/index.html

以上是本機草稿／暫存校樣，不是正式核准出版物；未發布至網站或 GitHub。PDF 嵌入字型由 PyMuPDF 抽取實際字型資料驗證，並非僅檢查系統已安裝。


## NEEDS HUMAN REVIEW：具體剩餘工作

1. **作者／電影研究者看片：** 為五部案例逐一選定可合法觀看的版次，填入發行／修復版、來源、精確時間碼、鏡頭描述及觀察者；核對影評所指片段與正文解讀。沒有可看片源就保留待審，不猜時間碼。
2. **電影史／理論審稿：** 對照 R001 所採 13 版實體／電子書，補 S04 及術語的章節／頁碼；評估早期電影史敘述是否需加入其他地區史料；研究編輯完整核讀 R005 與 R024 的方法和結果。
3. **中英文專業編輯：** 審校 title、每節語義、電影專名／譯名、術語首選、自然度、文化語境及引用格式。驗收後才可把兩語狀態從 `review-needed` 改成 approved。
4. **補齊並審查五張原創圖：** 作者提供每張圖的生成工具／模型／版本／日期、完整提示詞、操作者與修改紀錄；確認寫實風格與原 brief 的差異是否接受。逐一完成相似性／權利、技術品質及編輯核准；需要時由作者決定重製或從章稿排除，保留決策紀錄。
5. **解決 V1 資產紀錄：** 查 `ASSET-CH01-FIG-01` 的來源和授權；若不用於 V2，須在資產 registry 記錄排除決策，不能假裝已取得授權。
6. **教育短片案例：** 如用於自然科學教學，請學科教師驗證玻璃杯／晨光表現；目前明確是故事示範，不是科學事實的實驗紀錄。
7. **完整出版校樣：** 人工核准稿與圖像後，重建網站、PDF、EPUB；逐頁檢查兩語字形、表格跨頁、目錄、引文連結、圖說、alt、EPUB 閱讀器相容性及正式輸出 metadata。正式 60 章建置需在其餘章節也完成核准後再執行。

## 最終判定

**CH01 是否已達到正式出版標準？否。** 內容骨架與雙語草稿已由本輪補齊；技術草稿建置通過，但電影片段校核、理論頁碼、英文專業審稿、實際插圖／權利核准與完整全頁校樣仍未完成。現階段狀態為 `review-needed`，不是正式出版完成。
