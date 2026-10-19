# AI Video Bible｜章節製作與出版標準作業程序 V4.0

- 版本：4.0.0
- 制定日期：2026-10-18（Asia/Taipei）
- 適用範圍：本專案 12 篇、60 章；繁體中文主稿、英文人工審校譯稿、雙語網站及書籍草稿
- 原則：以現有 V2 內容模型、registry、出版腳本和章稿為基礎增量整合，不重建、不覆寫 V1/V2 原稿。

## 1. 角色與輸入

使用者在 Codex 輸入「製作第 X 章」或「製作 CHXX」。Codex Skill 依 `metadata/chapters.yaml` 判定章節，讀取現有版本和進度，建立可恢復執行紀錄，再完成可授權的研究、雙語稿整合、圖片規劃、測試和報告。Codex 可依需求使用可用的網頁研究工具；文字模型本身不代替來源核驗、人工翻譯審稿或出版核准。

不得自動監看資料夾或假稱背景工作。每次執行均由明確的 Codex 請求啟動。章節指令只授權該章的本機工作，不包含付費 API、登入、授權核准、commit/push 或部署。

## 2. 狀態模型

章節主要狀態沿用 `metadata/translation-status.yaml` 和 `metadata/chapters.yaml`。不得因自動測試或成功建置把內容改成 `approved`。報告使用以下判定：

- `PASS`：有可重跑命令、檔案、hash、測試輸出或人工簽核等證據支持。
- `FAIL`：已測項目未達規格；列明重現方法及影響。
- `BLOCKED`：依賴、授權、憑證、費用或輸入資料缺少，未能測試；不可寫成通過。
- `NEEDS HUMAN REVIEW`：需作者、電影研究／技術／法律／雙語／美術編輯作專業判斷。
- `NOT RUN`：尚未執行；不得合併到 PASS。

每項判定附證據與時間；外部服務資訊註明檢查日、官方文件版本／URL。非阻斷的警告另列，不隱藏。

## 3. 不可破壞操作原則

1. 先 `git status --short` 並辨識使用者既有變更；不清理、不重設、不覆蓋無關變更。
2. 找全 V1 `chapters/`、V2 `content/zh-TW`、`content/en-US`、source pack、manifest、figure registry、translation registry、references、terms、網站投影、既有 reports、dist 和最近 run。
3. 以 timestamp + run ID 建立 `backups/` 快照和 `production/runs/CHNN/` JSON/Markdown 日誌；對舊檔記錄 SHA-256。覆寫目標前先獨立備份，並以 diff 審閱。
4. 不刪除、搬移或改名原稿、圖片、來源包或舊建置。新建輸出限定在新唯一目錄；已有同名輸出先比較 hash，異內容另存版本。
5. 僅處理指定章節及其必要 registry/對照/網站投影。避免批次改寫所有 60 章。

## 4. 研究與引用 SOP

1. 從章節 registry 取得本章中英文題名、篇別、slug、狀態和永久 ID；列出尚缺的章節區塊、先備知識及學習目標。
2. 把每個可查證主張拆成 claim 記錄：主張、分類、證據需求、來源 ID、支持範圍、反例／限制、查證日及版本。
3. 電影理論優先原始文獻、學術出版社／期刊、電影檔案館及具名專業研究。AI 工具規格優先該工具官方文件、版本公告和可重現實測；一般媒體只作補充線索。
4. 建立或引用穩定 `R###`，欄位至少有作者／機構、年份、完整標題、出版者、DOI 或穩定 URL、版本／版次、存取日期、支持主張、限制和查證狀態。頁碼只在實際核對相同版次後記錄。
5. 時效性資料標註取得日期、版本和適用方案；過期文件不能支撐現行工具結論。HTTP 403、timeout、登入牆只記作未能查證，不推斷連結失效。
6. 分清五種證據：`verified-fact` 已查證事實、`theory` 理論主張及學派脈絡、`practice` 實務建議、`ai-hypothesis` AI 生成待驗假設、`demo` 虛構或示範材料。所有示範標明虛構，不拿來證明歷史或工具功能。
7. 每節至少連結可支持其核心知識的來源或標明該段為實務／示範；引用清單不代表段落內所有主張均被來源支持。

完整引用資料模型遵循 `docs/CITATION-V2.md` 和 `metadata/references.yaml`。不得編造書目、論文、DOI、URL、頁碼、發行版本或電影時間碼。

## 5. 雙語寫作及術語 SOP

1. 繁體中文為源稿；依模板先完稿及來源標記，再以相同 section/case/figure/term ID 製作英文對譯稿。
2. 英文是可由 AI 協助的譯稿，不得自動批准。翻譯須保留論證強弱、條件、否定範圍、單位、引用位置和例子的權利聲明。
3. 每個術語沿用穩定 `TERM-*`，記錄 `preferred.zh-TW/en-US`、雙語定義、領域、使用情境、異名、易混淆詞、來源 ID、狀態、審校人及日期。各語第一次出現使用首選詞；後文保持同一寫法。
4. 新稿與 `metadata/terminology.yaml`、翻譯對照 YAML、章節 frontmatter 及網站錨點同步；修改源稿時將舊譯文標記 `out-of-sync` 或 `review-needed`。
5. 僅作者／指定專業編輯可將內容或翻譯設成 `approved`，並留下姓名／角色、版本與日期。機器 diff、術語 script 和網站 build 只能檢查一致性，不能判定翻譯自然或事實正確。

## 6. 電影致敬案例 SOP

1. 案例用於分析電影形式或概念轉譯，先確定教學目標，再以可信來源和合法可觀看版本查片。
2. 記錄片名（原名／繁中名）、導演／年份等有來源的資料、版本／修復版／發行資訊、觀看來源、時間碼、觀察者、分析主張及來源 ID。沒有實際看過的片段，不捏造時間碼或鏡頭細節。
3. 把受啟發的抽象形式轉成新人物、新場景、新道具和新構圖。不得以「致敬」為由重現原片劇照、鏡頭、版面、角色、演員肖像、服裝、標誌或可識別美術。
4. 案例分析須限制主張範圍，區分來源描述、作者觀察和解讀；不同敘述者不必然等於說謊，畫面相似也不證明因果。
5. 權利／相似性由作者或權利顧問審查。自動化不能判定合理使用、侵權或不具實質相似；存疑時重作或排除。

## 7. 圖像及向量圖 SOP

1. 圖號永久且不依檔名變動。每圖記錄 `figure_id`、章／節、教學目的、原始檔與 SHA-256、尺寸／格式、來源與製作日期、提示詞／繪圖方法、工具與版本、修改履歷、雙語標題／圖說／alt、權利依據及 rights/technical/editorial review 狀態。
2. 原始圖存 `assets/chapters/CHNN/figures/originals/`；經人工核准的無字底圖放 `approved/`；編輯標註放 `overlays/*.svg`；書籍或網站衍生檔放 `exports/`。保留母檔，不把出版文字烘焙進唯一圖檔。
3. AI 圖一律依適用工具條款記錄 provenance。AI 生成不保證獨創、排他權利或無侵權。人物肖像、商標、受保護場景／服飾／構圖、歷史制服、生成亂字與參考輸入權利都需人工查核。
4. 網路圖片只作研究參考；不得下載後直接作正式插圖。缺圖時產生 figure brief 和待辦，不造假圖片、不以 placeholder PNG 測試正式流程。
5. 技術圖優先原創 SVG／程式化向量檔並驗證標籤、比例、色彩對比、閱讀順序及縮放。實際生成圖只在適用服務可用、條款／費用授權明確後呼叫；批次數量需受明確預算上限控制。
6. 圖片狀態預設 `draft-generated`、`original-ai-illustration-pending-final-review`、各 review `pending`、`asset_approved: null`、`publication_status: pending-publication-approval`。除非所有必需人員已簽核，不能進正式網站或書籍。

專案既有權利政策以 `docs/IMAGE-RIGHTS-V2.md` 為準。生成工具選型與費用閘門見 `IMAGE-GENERATION-SETUP.md`。

## 8. 章節模板及結構

每章有中英配對的 frontmatter 和穩定 section IDs，依學科適用度包括：學習目標、先備知識、術語、歷史／原理、傳統流程、AI 轉換／限制、詳細流程、提示詞／技術參數、案例、錯誤／QA、練習／評量、引用及結語。章節可調順序，但不得省略必要題目；不適用項標明理由。

原文模板：`.codex/skills/ai-video-bible-chapter-pipeline/templates/chapter-template-v4.md`。報告模板：同目錄 `templates/acceptance-report.md`。

## 9. 自動製作工作流程

| 階段 | Codex 工作 | 證據／輸出 | 阻擋／人工節點 |
|---|---|---|---|
| A. 啟動與盤點 | 解析章節 ID；git/status；讀 registry、現稿、素材、歷史；建 backup/run | `run.json`、工作清單、backup manifest | ID 衝突先停止修改並回報 |
| B. 研究 | 建 claim/source map；查學理／技術文件；驗連結與版本 | source IDs、查證日期、limits | 付費資料庫登入或無法查片列 BLOCKED |
| C. 繁中主稿 | 用模板補缺、保留原稿價值；逐主張對來源 | canonical zh-TW Markdown、diff | 不以佔位內容冒充正文 |
| D. 英文譯稿 | 源稿對譯；術語及 IDs 對齊；維持 review-needed | canonical en-US Markdown、alignment | 必須人工核稿才可 approved |
| E. 案例與術語 | 更新案例索引、term DB、citation/translation map | 有來源的案例及 TERM/R IDs | 未實際看片不填 timecode |
| F. 視覺資產 | brief；依授權使用 native/API provider 或 SVG | prompts、manifest、hash、rights log | 無授權／費用確認時 BLOCKED，只交 brief/SVG 技術圖 |
| G. 網站及出版 | sync/build zh/en; DOCX/PDF/EPUB draft | 本機 dist/temp 及版本輸出 | 章節 gate 不等同正式全書 gate |
| H. QA | 測試結構、引用、同步、路由、圖、PDF 字型渲染、EPUBCheck | 命令、版本、log、抽查圖 | 外部／視覺驗收不可以 CI 取代 |
| I. 驗收 | 產生 `reports/CHNN-FINAL-ACCEPTANCE.md`；更新 history、run 狀態 | 最終報告及可恢復日誌 | human review 未完成不得寫 publication-ready |

## 10. 必要出版品質閘門

### 10.1 每章章末全項目稽核（必要步驟）

每一章的本機製作、整合或更新工作，在交付前都必須完成 `.codex/skills/ai-video-bible-chapter-pipeline/templates/acceptance-report.md` 的「章末全項目稽核」。不得只重跑技術測試或複製前次報告。逐項對照本章實際內容、素材、來源、網站與書籍輸出，為每列填入 `PASS`、`FAIL`、`BLOCKED`、`NEEDS HUMAN REVIEW` 或 `NOT RUN`，並提供可定位的檔案／行節、命令輸出、版本、雜湊或簽核紀錄。狀態需反映本次檢查；沿用先前證據時要註明證據日期及檔案未變更的依據。

稽核至少涵蓋：

1. 內容：學習目標、先備知識、雙語術語及定義、電影史與基本原理、傳統方法、AI 技術轉換與限制、逐步工作流程、提示詞與參數、可追溯案例、常見錯誤與品質驗證、練習評量、延伸研究、引用及主張支持範圍。
2. 雙語與編輯：中英節次／穩定 ID／術語／案例／圖號對照；語意、用詞、數字單位及引用位置審閱狀態。
3. 來源與案例：來源真實存在且可追溯；版本、日期、locator、電影合法版本與 timecode 未臆造；工具功能以適用官方文件或實測支持。
4. 素材與權利：原稿／素材備份與保留、資產原檔及 hash、生成／繪製紀錄、雙語圖說與 alt、SVG 可編輯性、權利／相似性／技術／可及性審查狀態。
5. 出版與工程：網站兩語路由／內容／ID／資產；DOCX；PDF 字型嵌入與實際繁中渲染；EPUB 結構及 EPUBCheck；連結檢查；單元／整合／專案品質測試；草稿輸出位置與工具版本。
6. 治理與可重現性：registry／translation status、作者與專業審稿簽核、run log、`history.md`、備份 manifest、未發布／未推送狀態（如適用）。

只有每列均完成狀態判定和證據記錄，才可將章節稽核標記為「已完成」。存在 `FAIL`、`BLOCKED`、`NEEDS HUMAN REVIEW` 或 `NOT RUN` 時，必須在結論列明剩餘事項及負責角色／解除條件；已完成的章稿可作為草稿交付，但不得稱為正式出版完成。章末稽核和報告交付後，停止並回報本章狀態；下一章須由使用者另行指定或要求，不能在同一輪自行接續。此流程閘門不會把必要人工核准改成機器判定。

正式出版稿每項皆必須 PASS，否則最多是 draft / review-needed：

- 主張能追到來源；來源支持範圍和引用版本已核對。
- 中文／英文各節、術語、引用、圖號和穩定 IDs 成對一致；英文已由人工編輯核稿。
- 正式插圖原創或有可追溯授權；生成記錄、hash、雙語圖說和 alt 齊備；相似性與肖像權已人工審查。
- 無未授權第三方圖、外部圖片 URL、placeholder、未核准圖或圖說缺漏。
- PDF 每字型實際嵌入；繁體中文字形在實際頁面渲染／抽查可讀；無未處置缺字警告、圖說漂頁或截斷。
- EPUB 結構及引用錨點由 EPUBCheck 驗證通過，中英各自實際檢查。
- 中英網站 routes 均建置成功；頁面 IDs 唯一、內容和圖/alt/caption完整、靜態資產 hash 相同。
- 單元與整合測試通過；正式出版全書 gate、章節 gate 和草稿建置的狀態分開報告。
- 作者及必要專業審稿人的核准有姓名/角色、版號、時間和範圍記錄。

## 11. 工具鏈及基本命令

使用 repo 現有 Python、Astro/Starlight、Pandoc、XeLaTeX/MiKTeX、字型驗證、EPUBCheck 和 validators。先查 `CHAPTER-PIPELINE-README.md` 的依賴狀態，不因單次 build 成功推論字型或權利通過。

```powershell
python scripts/chapter_pipeline.py --chapter 1
python scripts/v2_validate.py
python scripts/validate_project.py
python -m unittest discover -s tests -v
python scripts/publishing/sync_site_content.py --check
npm --prefix apps/web run check
npm --prefix apps/web run build
```

其餘格式僅於章節 gates 和工具可用時建置；EPUB 用 `scripts/publishing/check_epub.ps1`；PDF 需查 `pdffonts` 或等效 PDF parser，再實際渲染抽查。完整命令請記錄於章節報告。

## 12. CH01 V4 端到端驗證基準

CH01 的雙語稿及五張插圖已存在。V4 首次驗證需重用現有素材、figure IDs、來源、manifest、網站和出版流程；不得重生五圖。當前已知待辦是作者與電影研究者選擇合法影片版本並補 timecode、電影理論／術語頁碼、英譯編輯審核、五張圖生成來源 metadata／相似性／權利／技術／編輯核准、舊 V1 資產處置和最終全頁出版校樣。歷史驗收見 `reports/CH01-FINAL-ACCEPTANCE.md`。

先讓 runner 盤點並建立 run checkpoint，再只做未完成且可安全執行的步驟。不得因 V4 Skill 建立完成而重寫既有章節或將 CH01 升為正式出版。
