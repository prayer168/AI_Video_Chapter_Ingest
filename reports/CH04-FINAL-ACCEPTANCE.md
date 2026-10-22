# CH04 章節草稿最終驗收報告

- 章節：CH04《電影形式、風格與作者性》
- 英文暫定標題：*Film Form, Style, and Authorship*
- 日期：2026-10-20（Asia/Taipei）
- revision：2.2.0-draft
- 範圍：CH04 雙語章稿、術語／引用／圖稿 metadata、網站投影、雙語本機出版草稿及自動驗證。
- 狀態：**草稿製作與自動化檢查完成；全書完稿後集中人工簽核。不是正式出版稿。**
- Pipeline run：`production/runs/CH04/20261020T203111+0800-3d34a58e/`
- 修改前備份：同 run 內 `backup/`；`backup/MANIFEST.json` 記錄 12 個原有目標檔案及 SHA-256；另以 `git show HEAD` 還原 `figure-captions.lua` 的修改前版本，並經 LF/CRLF 正規化 diff 確認工作副本差異僅為本輪兩筆 CH04 圖號映射後列入 manifest。
- 出版預覽：`tmp/CH04-draft-20261020-r1/`（gitignored，本機草稿；沒有發布）。

## 變更與保留

- 完成 canonical 繁中及英文研究草稿，維持 CH04-S00–S13 共 14 個穩定節次錨點；英文標題仍為暫譯。
- 新增 8 個 CH04 雙語術語、14 組逐節對照、R031–R038 來源紀錄與兩筆原創 SVG 圖稿登錄；章稿、全域圖稿 registry、資產清冊、翻譯狀態、章節 registry、整合矩陣及 Pandoc 圖說 filter 已同步。
- 新增可編輯 SVG：`CH04-FIG-001`（顯示圖號 4-1）及 `CH04-FIG-002`（顯示圖號 4-2）。兩圖原始 SHA-256 分別為 `44e64c3d18a3aae36983d1facd3a18defb32166178642d517dce50fbe3156c72`、`c645c4e784d23b27e9c0810ce46b0a9c400a09a5d84a14295b8c5b4b0bf5db1d`。圖稿為手寫 SVG；個人作者歸屬、技術、可及性、相似性及出版權利仍待人工確認。
- 保留 V1 原稿、CH01–CH03、其他 scaffold、既有圖片、來源 ZIP 及本輪前的 CH04 原始 scaffold；無檔案刪除或移動。修改前原始檔案 hash 見備份 manifest。
- 已同步 Astro 產生稿及原始 SVG 的網站衍生檔。同步腳本清單列出的舊生成 MDX 數量為 0；沒有部署網站或推送 GitHub。
- 初次測試發現 `data/assets.yaml` 中 CH04 資產的 `research_sources` 型別及 `production_log` 欄位不符 schema，並發現測試所用狀態文字與章稿不同；已修正後重跑。

## 研究與主張範圍

| 來源 | 本章用途與限制 |
|---|---|
| R031，Bordwell、Thompson、Smith，*Film Art: An Introduction*，第 13 版，McGraw Hill，2026 release | 出版者頁面支持作者、版次和教材涵蓋主題；本章尚未核對專案採用實體／電子版的章節頁碼。 |
| R032，Cinémathèque française，Truffaut 回顧資料 | 支持該館對 Truffaut 1954 年文章及其後來回憶的歷史摘要；不是原文校勘版。 |
| R033，Andrew Sarris，〈Notes on the Auteur Theory in 1962〉，*Film Culture* 27，Winter 1962–63 | 查閱了原文掃描；正式採用版及原始印刷頁碼尚待核對。 |
| R034，Pauline Kael，〈Circles and Squares〉，*Film Quarterly* 16.3（1963），DOI 10.2307/1210726 | 出版紀錄支持書目資訊；全文論證尚待核讀。 |
| R035，Berys Gaut，〈Film Authorship and Collaboration〉，Oxford University Press（1997），DOI 10.1093/acprof:oso/9780198159216.003.0007 | 出版者摘要支持章節對作者主張維度及單一／多重作者的限縮描述；詳細理論需核對全文。 |
| R036，C. Paul Sellors，〈Collective Authorship in Film〉，*The Journal of Aesthetics and Art Criticism* 65.3（2007），DOI 10.1111/j.1540-594X.2007.00257.x | 出版者摘要支持集體作者性議題；細節需核對全文。 |
| R037，British Film Institute，*Vertigo and Auteur Theory for KS5 Film Studies*，2026 教育活動頁 | 作為教學案例索引，不代表撰稿者實際看過任何版本或鏡頭；活動資訊有時效性。 |
| R038，Runway Help Center，*Gen-4 Video Prompting Guide*，2026-10-20 查閱 | 僅支持該供應商文件對特定版本提示流程的描述；不外推為其他工具效果，發布前須重查現行版本。 |

章內將已查證書目／網頁敘述、電影理論、實務建議、AI 假設及教學示範分開表述。*Vertigo* 案例沒有虛構鏡頭觀察、版次或 timecode；實際看片紀錄留待集中人工審查補入。

## 主要閘門

| 閘門 | 狀態 | 證據 | 待辦 |
|---|---|---|---|
| 研究來源與主張 | NEEDS HUMAN REVIEW | 章稿 R031–R038；來源記錄含 URL、查閱日、版本／locator 限制；`python scripts/validate_project.py` PASS。 | 電影研究編輯核對全文、教材版次與頁碼、Sarris 原版頁碼及各主張支持範圍。 |
| 中英內容及術語同步 | PASS（結構）／語意 NEEDS HUMAN REVIEW | `metadata/translations/CH04-alignment.yaml`；`tests.test_ch04_content` 4/4 PASS。 | 雙語編輯校譯，核定英文標題、術語自然度及理論語意。 |
| 電影案例及合法版次／timecode | NEEDS HUMAN REVIEW | 章稿 §CH04-S09 引用 R037；明確聲明未看片、沒有 timecode。 | 作者／電影研究編輯選定合法版本、實際觀看並記錄片段、版次和時間碼，或決定改為非片段案例。 |
| 圖片來源、雜湊與權利 | NEEDS HUMAN REVIEW | 兩個 SVG 原始檔、`assets/chapters/CH04/figure-manifest.yaml`、`metadata/figure-registry.yaml`、`data/assets.yaml` 均有 hash／繪製法／圖說／alt／權利欄位；全部 rights、technical、editorial、approval 為 pending。 | 確認實際繪圖者署名、權利、相似性、技術可及性並由作者批准用途。 |
| 網站路由／ID／素材 | PASS（本機草稿） | `python scripts/publishing/sync_site_content.py --check` PASS；Astro build PASS，123 routes；逐頁檢查 `apps/web/dist/zh-tw/ch04-chapter-04/index.html`、`apps/web/dist/en/ch04-chapter-04/index.html`，各有 2 個唯一 figure IDs、2 張存在的圖片和非空 alt。 | 不發布；內容仍待審。 |
| DOCX／PDF／字型及實際渲染 | PASS（草稿） | Pandoc 3.12.1；中英文 DOCX 均含 2 張內嵌 PNG、ZIP CRC 通過。PDF：繁中 10 頁、英文 12 頁；`check_fonts.py --require-pdffonts` 中英 PASS，繁中 Microsoft JhengHei、英文 Times New Roman 與混排中文字型均實際嵌入；PDF 文字抽取無 U+FFFD。已渲染並檢查繁中第 7–8 頁、英文第 9、11 頁，涵蓋兩圖及圖說。 | 全書樣式校樣及專業美編終審待全書完成後執行。 |
| EPUBCheck／雙語文字 | PASS（草稿） | EPUBCheck 5.4.0 中英各 0 errors、0 warnings、0 informationals、0 references；ZIP CRC 通過，各含 2 張媒體圖、2 個 CH04 figure IDs，英文版亦含雙語術語表，未見 U+FFFD。 | 出版前由編輯實際抽讀兩語電子書。 |
| 單元／整合／品質閘門 | PASS（自動可測項） | `python -m unittest discover -s tests -v` 44/44；`python scripts/v2_validate.py` PASS；`python scripts/validate_project.py` PASS；`git diff --check` exit 0。 | 自動測試不代替學理、翻譯、圖稿或出版審查。 |
| 作者／專業編輯簽核 | NEEDS HUMAN REVIEW（依作者決策延後） | `metadata/chapters.yaml`、`metadata/translation-status.yaml` 維持 review-needed；figure approvals pending。 | 全書完稿後集中簽核。 |

## 章末全項目稽核（每章必填）

### 內容完整性

| 必要項目 | 狀態 | 證據 | 待辦／責任角色 |
|---|---|---|---|
| 學習目標 | PASS | 中英文 §CH04-S01 均列可觀察學習成果；anchors 配對測試通過。 | 編輯可於全書審稿時核對難度。 |
| 先備知識 | PASS | §CH04-S02 明列 CH01–CH03 及觀片資料要求。 | 無自動阻擋。 |
| 專業名詞中英文對照與定義 | NEEDS HUMAN REVIEW | §CH04-S03、8 個 `TERM-CH04-*` 已登錄並雙語對照；定義文字仍為 draft。 | 電影理論／出版編輯核定譯名與定義。 |
| 電影製作歷史與基本原理 | NEEDS HUMAN REVIEW | §CH04-S04 對電影形式、作者論及合作作者性作有來源且有限定的草稿；引用 R031–R036。 | 對照原始文章及學術全文，確認歷史脈絡與論述平衡。 |
| 傳統電影製作方法 | NEEDS HUMAN REVIEW | §CH04-S05 有意圖轉譯、跨作品比較、預視覺化、拍攝剪輯及修訂流程。 | 導演／製片專業編輯驗證流程適用性。 |
| AI 時代技術轉換、能力與限制 | NEEDS HUMAN REVIEW | §CH04-S06 明示工具差異、生成變異及不得把提示詞當保證；R038 只支撐供應商指引。 | AI 影像技術編輯重核版本及提示建議；本輪沒有模型實測。 |
| 詳細工作流程 | PASS | §CH04-S07 有分步輸入、操作、交接及檢查方式。 | 實際團隊試跑可列入後續驗收。 |
| 提示詞與技術參數（含版本／未實測聲明） | NEEDS HUMAN REVIEW | §CH04-S08 為原創示範場景及提示詞，明確不宣稱生成結果；R038 標示版本／日期。 | 若要展示實測需有授權帳戶、版本、參數和輸出紀錄；由 AI 製片編輯檢視。 |
| 實際鏡頭／影片案例與來源 | NEEDS HUMAN REVIEW | §CH04-S09 以 BFI 的 *Vertigo* 教育頁作案例入口，另外提供依 *Film Art* 分類的觀片練習；不捏造鏡頭、版次或時間碼。 | 作者／電影研究編輯看片並完成版本與 locator 紀錄。 |
| 常見錯誤與品質驗證 | NEEDS HUMAN REVIEW | §CH04-S11 包含常見錯誤、修正及快速檢核表。 | 導演／電影研究編輯確認評量標準的實務效度。 |
| 練習與評量 | NEEDS HUMAN REVIEW | §CH04-S12 含跨作品分析、反例、原創 style sheet 與 0–4 評量錨點。 | 教學編輯確認學習負荷、評分一致性。 |
| 延伸研究 | PASS | §CH04-S12 列可追溯理論與跨章研究方向。 | 後續各章完成時補充連結。 |
| 主張分類及引用可追溯性 | NEEDS HUMAN REVIEW | Frontmatter 標示五類 claim；章稿引用的 R031–R038 均存在於 bibliography；自動測試引用 ID 通過。 | 專業編輯按句核對來源支持範圍與完整全文。 |

### 雙語、素材與出版完整性

| 必要項目 | 狀態 | 證據 | 待辦／責任角色 |
|---|---|---|---|
| 中英文節次、穩定 ID、術語、案例和圖號逐項對齊 | PASS（結構） | `metadata/translations/CH04-alignment.yaml` 有 S00–S13、8 term pairs、2 figure pairs、references；專項測試通過。 | 語意核對另見下一列。 |
| 中英文語意、單位、引用位置及專業用語編輯狀態 | NEEDS HUMAN REVIEW | 兩語稿均有 14 相同節次 IDs，frontmatter 為 review-needed；一致性腳本 4/4 PASS。 | 雙語編輯逐節校譯。 |
| 來源存在、版本／日期／頁碼或 locator 已核對 | NEEDS HUMAN REVIEW | R031–R038 有可追溯 URL/DOI、查閱日、版本或 locator 及限制。 | 多筆只查摘要／書目／機構頁，須核對原始全文、採用版次、頁碼。 |
| 電影案例版次、合法觀看來源與 timecode | NEEDS HUMAN REVIEW | §CH04-S09 明確沒有聲稱已看片或填入 timecode。 | 作者／電影研究者完成觀看紀錄。 |
| 原稿及素材備份、差異與保留情形 | PASS | run backup manifest 保存 12 個修改前檔案 hash；V1、其他章稿、既有素材均保留。 | 無。 |
| 圖片／SVG 原檔、hash、生成或繪製紀錄 | PASS（記錄存在） | 兩原始 SVG 均存在，hash/bytes 與 manifest 一致；有方法、日期、修改紀錄，沒有 AI 或第三方圖片生成。 | 個人作者署名仍待確認。 |
| 圖號、雙語標題／圖說／alt 與正文位置 | PASS（機器核對） | CH04-FIG-001/002 對應圖 4-1/4-2；雙語正文 §S10、manifest、網站、DOCX/PDF/EPUB 各 2 張；alt 非空。 | 排版藝術審查待全書校樣。 |
| 圖片權利、相似性、肖像及標誌人工審查 | NEEDS HUMAN REVIEW | 圖稿為專案手寫 SVG，不含第三方影像；rights/approval 欄位仍 pending。 | 確認具名作者、權利及相似性；作者批准出版用途。 |
| SVG 技術正確性、可編輯性、可及性及印刷檢視 | NEEDS HUMAN REVIEW | 兩檔可解析且可由 Inkscape 1.4.4 輸出 1600px PNG；PDF 圖頁已渲染抽檢。 | 人工核對標籤、對比、閱讀順序及小尺寸可讀性。 |
| 中英文網站路由、內容、ID、圖檔及 alt | PASS（本機 build） | Astro check 0 errors／warnings／hints；build 123 頁；CH04 兩語路由各有 2 unique figure IDs、圖片存在、alt 非空。 | 未發布。 |
| DOCX 草稿建置與內嵌素材 | PASS（草稿） | Pandoc 3.12.1；中英文 DOCX ZIP CRC 通過，`word/media/` 各 2 張 PNG。 | Word 字型替換與實際閱讀由編輯校樣。 |
| PDF 建置、字型嵌入及繁中實際渲染 | PASS（草稿） | XeLaTeX/MiKTeX；中英 `pdffonts` 嵌入列皆 yes；strict `check_fonts.py` 通過；繁中圖頁 7–8、英文圖頁 9、11 已查，抽文字無替代字元。 | 全書印刷校樣和更多頁面審查。 |
| 中英文 EPUB 結構、雙語顯示及 EPUBCheck | PASS（草稿） | EPUBCheck 5.4.0 雙語皆零錯誤／警告／informationals／references；ZIP CRC、雙圖、圖 ID、雙語文字通過。 | 人工閱讀器抽查待做。 |
| 連結檢查及網路不確定項目 | NEEDS HUMAN REVIEW | `python scripts/validate/check_links.py`：0 failures、0 network checked、5 inconclusive。 | 目前沒有報告為 broken；5 筆需網路／人工複查，來源頁亦需出版前再確認。 |
| 單元、整合、專案結構與出版品質測試 | PASS（自動可測項） | 44/44 unittest；V2 validator、project validator、網站 sync check、diff check 均 PASS。 | 人工判斷品質不屬於自動測試。 |
| registry、翻譯狀態及章節 metadata 同步 | PASS（結構） | `metadata/chapters.yaml`、`translation-status.yaml`、terms、references、figure registry、asset list、alignment 和 matrix 已更新。 | 章名仍暫譯、狀態仍 draft/review-needed。 |
| run log、history、備份 manifest 與重現指令 | PASS | run JSON/checklist/backup manifest；本報告列出重現命令；`history.md` 追加本輪過程及錯誤修復。 | 無。 |
| 作者／專業審稿人／權利核准狀態 | NEEDS HUMAN REVIEW（集中審核延後） | 翻譯狀態、圖稿權利／審核／作者批准均未設 approved。 | 全書完成後統一簽核，之後再更新本章版本與狀態。 |
| 未發布網站、未推送等授權邊界（如適用） | PASS | 本輪只作本機 Astro build；沒有部署、Git commit 或 push。 | 後續發布須另有明確指示。 |

### 章末稽核結論

- 狀態統計（內容完整性 13 列 + 雙語／素材／出版完整性 19 列）：**PASS 16；FAIL 0；BLOCKED 0；NEEDS HUMAN REVIEW 16；NOT RUN 0**。
- 可交付草稿工作是否完成：是；證據為雙語章稿、metadata、原始 SVG、雙語六種書籍草稿、網站本機建置及測試紀錄。
- 是否達正式出版標準：**否**。
- 尚未完成：雙語專業校譯；電影理論／書目全文和頁碼定位；合法電影版本與實際片段 timecode；作者性論述與案例專業審查；SVG 作者歸屬、權利、相似性、技術、可及性和印刷核准；讀者實際抽讀；作者簽核。責任角色為作者及相應電影研究、雙語、視覺／權利編輯；依使用者決策，集中於全書完成後進行。
- 本章稽核完成日期：2026-10-20。
- 報告後停止；不在本輪開始下一章。

## 未解決的人工作業

1. 電影研究編輯取得並核對採用的 *Film Art* 版本、R033 原始印刷頁碼、R034–R036 全文及精確引文支持範圍。
2. 作者／電影研究編輯選擇合法 *Vertigo* 版本，看片後填寫發行／修復版、合法觀看來源、觀察者及實際 timecode；否則刪除／改寫為未看片的教育案例索引。
3. 英文編輯校譯並核定英文標題和術語。
4. 圖稿作者／權利編輯確認兩個 SVG 的實際繪圖者署名、權利及相似性；美術／無障礙編輯核對閱讀順序、對比與可讀性；作者逐出版目標簽核。
5. 依全書共同簽核流程完成本章簽核後，才能將狀態升至 approved 或 publication-ready。

## 草稿輸出與重現

輸出資料夾：`tmp/CH04-draft-20261020-r1/`。工具版本：Pandoc 3.12.1、Inkscape 1.4.4、MiKTeX XeLaTeX、EPUBCheck 5.4.0。SVG 原始檔以 Inkscape 產生 1600px PNG 僅作排版衍生檔，原始可編輯 SVG 保留。

- 中英 DOCX：各含 2 張內嵌圖，`word/media/` CRC 通過。
- 中英 PDF：繁中 10 頁、英文 12 頁；繁中圖頁 7–8，英文圖頁 9、11；要求字型實際嵌入並由 strict font checker 通過。
- 中英 EPUB：各有 2 張媒體圖及兩個 CH04 figure IDs；EPUBCheck 各零錯誤與警告。
- Pandoc 仍輸出繁中缺少通用翻譯字串的警告（`zh.yaml`、Abstract、Table、Figure）；圖說中文內容與圖號有 filter 規則。這是草稿樣式待辦，不是隱藏的測試通過項。
- 單章草稿不是全書正式出版建置；未核准圖稿保持 pending，正式出版 gate 未繞過。

成品 SHA-256 收錄於同目錄 `OUTPUT-MANIFEST.json`；章節整合包為 `CH04-Codex-Materials-DRAFT-r4.zip`（18 個檔案成員，ZIP CRC 通過）；草稿圖頁預覽亦保留在同目錄供檢視。

## 最終判定

**CH04 是否達到正式出版標準？否。** 本次完成 CH04 雙語草稿、章節 metadata、原創可編輯圖稿及其 pending 權利記錄、網站本機驗證、DOCX/PDF/EPUB 草稿及章末全項目稽核。未完成項目均明列為 NEEDS HUMAN REVIEW；全書集中人工簽核尚未進行。因此本章仍是 `review-needed`，不能標示為 `approved` 或 `publication-ready`。




