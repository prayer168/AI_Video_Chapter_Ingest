# 建置與編輯歷史

本文件記錄出版建置、驗證、工具鏈問題及編輯流程的重要事件，供後續維護者排查與重現。它補充 `CHANGELOG.md`：變更日誌記錄版本內容，本文件保留問題脈絡、原因、處理方式與驗證結果。

## 記錄原則

每次重要建置或編輯整合，請新增一筆最新紀錄，至少包含：

- 日期、時區、Git commit（若尚未提交，標示工作樹狀態）
- 變更章節或出版目標，以及原始輸入檔／來源包
- 作業系統、Python、Pandoc、XeLaTeX／MiKTeX、Inkscape、字型名稱與版本
- 執行命令、成功／失敗結果及關鍵錯誤原文
- 發現的原因、採用的修正或替代方案
- 輸出檔、頁數、字型嵌入、插圖和版面檢查結果
- 未解事項與下一位編輯可採取的步驟

避免只寫「已修復」；需記下可重現的條件及證據。對尚未完全查明的原因標示為「推定」或「待查」，不要寫成已確認事實。不要在此記錄金鑰、密碼或其他機密。

---

## 2026-10-18｜依現有 chapters 結構建立逐章整理流程

- 確認章稿採 `chapters/NN-NN-short-title.md`，章節素材採同 slug 的 `chapters/NN-NN-short-title-assets/`，原始來源採 `chapters/source-packs/`；第二章 Markdown、配套 assets 及 `AI-Filmmaking-Bible-CH02-Codex.zip` 已在此結構中，沒有移動或覆寫。第二章 ZIP 的路徑安全檢查及完整性測試通過。
- 擴充 `docs/CHAPTER-INGEST.md`、repo 內 `.codex/skills/ai-video-chapter-ingest/SKILL.md` 及個人安裝的 `C:\Users\user\.codex\skills\ai-video-chapter-ingest\SKILL.md`：以「第 N 章完成，請整理」為觸發，檢查該章根目錄稿件及素材、保存原稿、更新註冊資料、驗證和建置，並記錄歷史；Codex skill 不會背景監看資料夾。
- 明定沿用現有 slug 和路徑、不重複建立章稿；清楚的章號下可同步目錄標題，篇章 ID 有衝突時不自行猜測；保護其他未提交變更，只推送於使用者明確要求時。
- `PROJECT-STRUCTURE.md` 和 `README.md` 已加入資料夾結構及觸發方式說明。Repo 技能與個人安裝技能均已同步；素材包內的 `CODEX-INSTRUCTIONS.md` 將作為章節規格核對，不覆蓋使用者當前要求或專案規範。
- 整理時發現第二章稿標題與 `docs/TOC.md` 原規劃標題不同；素材包中的章節規格明確要求保留 TOC，因此下次整理應先保留現有目錄並回報差異，等待編輯決策。目前 front matter 缺少 schema 必要欄位 `id`，且狀態 `draft-for-editorial-review` 不在允許列舉值內；專案驗證器因此回報第二章 schema／status 錯誤，其他 metadata 欄位也需依 schema 一併檢查。本次未改第二章、目錄或任何原始素材。
- 驗證：repo 與個人技能 front matter 均可解析為 YAML；`git diff --check` 通過。專案驗證器目前因尚待整理的第二章 metadata 失敗；未執行出版建置，因本次變更範圍是工作流程文件。

---

## 2026-10-18｜MiKTeX 更新後 PDF 字型錯誤與替代建置

### 範圍與環境

- 專案：第一章草稿出版輸出，工作目錄 `D:\我的雲端硬碟\google drive\000000000backup\00000黑熊講師\00000著作\AI_Video_Bible`
- Git：`main`，建置排查前 HEAD 為 `6481fd3`（`fix: preserve CJK layout and chapter figures in exports`）；輸出目錄 `dist/` 已由 Git 忽略。
- MiKTeX 更新前版本：25.12；更新後 XeLaTeX 及 MPM 回報 MiKTeX 26.5。
- 出版字型：原設定 `Noto Serif TC`；替代 PDF 字型 `PMingLiU`。

### 問題經過

1. PowerShell 初次找不到 `inkscape` 命令，雖然程式已安裝；實際執行檔為 `C:\Program Files\Inkscape\bin\inkscape.com`。將該 `bin` 目錄加入目前 PowerShell 工作階段的 PATH 後即可呼叫。
2. PATH 順序需注意：Inkscape 目錄若放在 PATH 前端，可能優先呼叫 Inkscape 隨附的 Python 3.12，導致 `import markdown` 等專案套件在該 Python 環境找不到。先記錄專案 Python 執行檔，再把 Inkscape 目錄附加到 PATH 尾端；已知專案環境為 Hermes Python 3.11.15，依賴套件已安裝。
3. MiKTeX 第一次排版時，缺少 `parskip.sty`，Console 顯示該檔屬於 `parskip` 套件並提供安裝選項；安裝套件後可繼續排版。
4. MiKTeX Console 初次更新檢查出現「尚未檢查更新」提醒；按下檢查後，原鏡像站 `ctan.mirrortwds.com.tw` 發生 `SSL connect error`，更新當時未完成。
5. 使用者後續成功更新。版本檢查確認 MiKTeX 從 25.12 升至 26.5。
6. 更新後重新建置 DOCX 成功；使用原本 `Noto Serif TC` 字型建置 PDF 時，XeLaTeX／dvipdfmx 失敗：

   ```text
   dvipdfmx:fatal: Invalid font: -1 (0)
   ```

   MiKTeX 記錄亦出現 `Invalid argument`，來源為 `dvipdfmx` 執行階段。舊 PDF 因建置失敗仍留在 `dist/`，其時間戳早於本次建置，不能當作更新後產物。

### 排查與原因

- 確認 `xelatex.exe`、`miktex-console.exe`、`mpm.exe` 均存在；版本顯示 MiKTeX 26.5。
- 以最小文件作對照：純英文 XeLaTeX 文件可輸出 PDF；指定 `Microsoft JhengHei` 的繁中 XeLaTeX 文件可輸出 PDF；指定 `Noto Serif TC` 的最小文件（包括只用作 `mainfont` 的純英文內容）重現相同錯誤。
- MiKTeX fontconfig 將 `Noto Serif TC` 解析到 `C:\Windows\Fonts\NotoSerifTC-VF.ttf`；該檔案提供多個字重樣式。重建 MiKTeX fontconfig 快取後，Noto Serif TC 測試仍失敗。
- 將 `PMingLiU` 或 `MingLiU` 指定為主字型及 CJK 字型時，最小繁中測試均成功。
- 因此已確認故障與目前 MiKTeX 26.5 的 Noto Serif TC 字型解析／嵌入路徑相關，不是 MiKTeX 整體不可用，也不是章節內容或 SVG 單獨造成。具體是可變字型格式本身、該字型檔的某項特性，或更新後的 XeTeX/dvipdfmx 相容性，尚未以更換靜態 Noto 字型檔等方式進一步區分；編輯者不應把「可變字型相容性」記成已確證的根因。

### 處理與驗證

- 用 `PMingLiU` 執行：

  ```powershell
  python scripts/build.py --format pdf --font "PMingLiU"
  ```

- PDF 建置成功，產生 `dist/AI-Filmmaking-Bible.pdf`，共 8 頁。
- PyMuPDF 擷取到繁體中文；4 個 PDF 字型項目均有非空嵌入字型資料。第二頁視覺抽查確認章節文字、表格／示意圖和頁碼可見。
- `scripts/check_fonts.py --font "PMingLiU" --pdf ...` 確認字型已安裝；此執行環境缺少 `pdffonts`，所以該腳本不能以外部命令查嵌入狀態。嵌入狀態另以 PyMuPDF 確認。
- DOCX 仍可用 `Noto Serif TC` 成功建置；本次只為 PDF 指定替代字型，未改動原始章稿、建置腳本或版本控制檔案。
- `dist/` 是忽略的生成目錄；產生的 DOCX/PDF 沒有納入 Git。建置當時工作樹乾淨。

### 後續建議

1. 正式出版可暫用 `PMingLiU` 建置 PDF；確認中文字形、標點、表格和全書版面後再定稿。
2. 若要恢復 `Noto Serif TC`，先找可取得的靜態字重字型檔或另一版字型，使用最小 XeLaTeX 文件檢查 `mainfont` 與 `CJKmainfont`，再跑完整書建置；保留測試結果與字型檔版本。
3. 正式發行前重建所有格式，確認 PDF 字型嵌入、全頁版面及插圖，並記錄 MiKTeX、Pandoc、字型和 Git commit。
4. 第一章仍是草稿；術語頁碼定位及部分理論來源審核仍待完成，不能因建置成功而標示為編輯定稿。

---

## 2026-10-18｜章節圖片路徑與 CJK 版面修正

- 章稿內相對於章節素材目錄的 SVG 路徑，先前被出版建置器以 repo 根目錄解析，造成圖片無法找到。`scripts/build.py` 已將本機圖片路徑正規化到 repo 根目錄，並分別轉成 DOCX 使用的 PNG、PDF 使用的 PDF 圖檔。
- PDF 曾出現繁中文字超出頁面右側的版面問題。建置器為 XeLaTeX 明確設定 `CJKmainfont` 後，先前 MiKTeX 25.12 環境下的 Noto Serif TC 建置版面恢復正常。
- 驗證紀錄：DOCX 含 1 張內嵌圖片；更新前 PDF 8 頁，視覺抽查圖像可見、無文字裁切，4 個字型均可由 PyMuPDF 擷取嵌入資料。
- 註：上述 PDF 是 MiKTeX 更新前的建置結果；更新至 26.5 後 Noto Serif TC 遇到另一項字型錯誤，請參見本文件最新紀錄。

---

## 2026-10-18｜第一章初次出版驗證摘要

- HTML、DOCX、PDF 均曾成功建置；HTML 章節頁含 4 個表格與 1 張圖片；PDF 為 8 頁。
- 專案驗證器確認 12 篇、60 章目錄、1 份正式章稿、20 筆術語、5 筆參考資料；章稿 metadata 與 S03 鏡頭 JSON 通過 schema 驗證。
- 本地連結、JSON、SVG XML、素材 ZIP 完整性及 ZIP 成員路徑檢查成功；原始稿雜湊值與素材包中的稿件相符。
- 線上參考連結檢查有部分站點回應 HTTP 403，需人工瀏覽確認；403 不等同來源失效。
- 第一章仍為草稿，鏡頭／場景定義仍需補來源頁碼定位，SAGE 文章全文仍待審閱。

---

## 2026-10-18｜第二章素材收錄與出版檢查

- 依使用者指示整理第二章。Git 分支 `main`；開始時已有 `.codex/skills/ai-video-chapter-ingest/SKILL.md`、`PROJECT-STRUCTURE.md`、`README.md`、`docs/CHAPTER-INGEST.md` 的未提交變更，並已有新第二章章稿、assets 目錄、來源 ZIP 與 history；本次保留並一併更新相關工作，不提交或推送。
- 原始包：`chapters/source-packs/AI-Filmmaking-Bible-CH02-Codex.zip`，SHA-256 `d448defde21abe8802ad87684928eaade0f7c39101b423159073391457a519a5`。ZIP 14 個成員，`ZipFile.testzip()` 無錯誤，未發現絕對路徑或 `..` 路徑穿越。ZIP 內章稿與匯入前 canonical Markdown SHA-256 相同：`719e7a1e59f88aaeb9a5a0e995d9ef686d335969f884f728585cc529265af422`（22,549 bytes）；ZIP 保持原樣。
- 將章稿 metadata 正規化為 `01-02`、第一篇第 2 章，狀態維持 `draft`；新增章節摘要、先備知識、來源支持的攝影機運動歷史摘要及傳統現場攝影流程。整合六個提示詞、26 筆術語來源資料、7 鏡頭／60 秒規劃清單及評量來源，均為素材包衍生可編輯副本，保留原始 ZIP、`CODEX-INSTRUCTIONS.md` 與其他原始來源。
- 新增來源登錄 R006–R012；Runway 資料標示為供應商文件，書籍採用版本與頁碼定位仍待核對。新增 TERM-01-02-* 術語草稿、PROMPT-CH02-P01–P06 未測試提示詞、ASSET-CH02-* 未確認授權素材登錄。禁止將示範提示詞或鏡頭清單描述為已生成／實測。
- 新增 `schemas/shot-list.schema.json`，並擴充 `scripts/validate_project.py` 檢查鏡頭清單結構、ID 唯一性、正時間長度、時間碼連續及總時長。
- 保留 `docs/TOC.md` 原規劃標題，因素材包明確要求不得修改目錄。章稿標題「鏡頭景別、構圖與攝影機語言」與 TOC 第 2 章規劃標題「鏡頭、場面與剪接：電影語言的基本單位」仍不一致，待編輯決策。
- 來源複核：Runway 官方 Academy/Help Center 與 Runway Resources 頁面、Columbia Film Language Glossary、Silman-James Press 出版社頁面已查閱。Columbia 詞彙表明確說明無法有把握識別電影史上首次攝影機運動；本章保留此不確定性。出版社書目頁面未提供本章採用版次與頁碼，故不補造定位。
- 工具版本：Python 3.11.15、Pandoc 3.12.1、MiKTeX XeLaTeX 4.18（MiKTeX 26.5）、Inkscape 1.4.4。執行 `python scripts/validate_project.py` 通過（12 篇、60 章、2 份 canonical 章稿、46 個術語、12 筆參考）；`python scripts/check_links.py` 語法檢查通過（15 個 URL）；`git diff --check` 通過。
- HTML：`python scripts/build.py --format html` 成功，產生 `dist/html/01-02-camera-language.html`；檢查輸出章頁存在且鏡頭清單相對連結有保留。
- DOCX：`python scripts/build.py --format docx --font "Noto Serif TC"` 成功，產生 `dist/AI-Filmmaking-Bible.docx`。
- PDF：`python scripts/build.py --format pdf --font "PMingLiU"` 成功，產生全書 PDF，共 20 頁；`scripts/check_fonts.py --font "PMingLiU" --pdf dist/AI-Filmmaking-Bible.pdf` 顯示 4 個字型項目均 `emb=yes`。PyMuPDF 可抽取繁中且章節標題和參考資料存在。已渲染並視覺抽查第 1、9–12、15–20 頁中的代表頁（含第二章章首、表格、案例、評量及文獻）；抽查頁未發現缺字、裁切或表格越界。
- 線上連結 best-effort 檢查未全數通過：Columbia 網站在此環境的 TLS 憑證鏈驗證失敗；既有 SAGE、Adobe 來源回覆 403；Inkscape 首頁回覆 HTTP 502。這些狀態均保留為人工複核，不判定來源已失效。Runway 與出版社頁面沒有列出失敗。
- 待辦：正式編輯核對書籍版次及頁碼；決定是否同步 TOC 標題；確認素材包作者／授權；製作可編輯示意圖；選定 AI 影片工具和版本做可重現實測；對科學折射示範使用實拍／可靠圖解核驗。

---

## 2026-10-18｜插圖原創與著作權規範及出版閘門

- 將使用者提供的《AI Video Bible｜插圖原創與著作權管理規範 V1.0》納入專案政策 `docs/IMAGE-RIGHTS-POLICY.md`，涵蓋繁中／英文書籍、網站及 HTML、DOCX、PDF、EPUB 輸出。網路圖片只作研究參考；禁止直接複製／下載後當出版插圖。
- 新增 `schemas/image-asset.schema.json`，要求圖號與段落、教學目的、研究來源及查證日期、原創提示詞／繪圖方法、工具版本（未知可填 null）、修改紀錄、權利風險、中英文圖說、審查狀態及四個發行目標狀態。`scripts/validate_project.py` 會檢查圖像 schema、來源 ID、實際檔案存在、章稿圖片已登錄，並拒絕外部圖片 URI 和內嵌 SVG。
- 新增 `scripts/image_policy.py` 正式出版檢查器。正式 `build.py` 在寫出任何正式輸出前先檢查目標出版狀態，未登錄、外部或未核准插圖會以 exit code 2 阻擋 HTML、DOCX、PDF、EPUB；`--preview` 將未核准圖片改成清楚的待審標記並輸出至 `dist/preview/`，且複製網站資產時省略未核准圖片。新增 EPUB 建置支援，與其他格式共用出版閘門。
- 第一章圖 1-1 原有 `CC BY-SA 4.0` 與作者標記未有可追溯依據，已降為授權／作者待確認，四類技術、品質、權利與最終審查及四個出版目標皆設為 `pending`。章稿新增中英文圖說；未核准前正式建置預期被阻擋。未修改 SVG 原始繪圖檔。
- README、`docs/ASSETS.md`、`docs/QUALITY.md`、`docs/PUBLISHING.md` 和 GitHub CI 已更新；CI 執行自動檢查與測試，並建置不含未核准圖片的草稿預覽。
- 驗證：`python -m py_compile` 通過；`python scripts/validate_project.py` 通過（12 篇、60 章、2 份 canonical 章稿、46 個術語、12 筆參考）；`python -m unittest discover -s tests -v` 6 項通過（pending 阻擋、approved 通過、外部圖像阻擋、未登錄圖像阻擋、出版目標各別判斷、草稿預覽省略圖像）。實際 `build.py --format html/docx/pdf/epub` 均因圖 1-1 pending 按預期以 exit code 2 中止；`build.py --format html --preview` 成功，檢查確認頁面有待審標記、沒有 `<img>` 且未複製未核准 SVG。
- 完整預覽建置 `python scripts/build.py --format all --preview --font "PMingLiU"` 成功產生 HTML、DOCX、PDF、EPUB。封裝檢查確認 DOCX 和 EPUB 無圖片檔，PDF 共 20 頁、圖片數為 0 且包含草稿預覽標記；PDF 第 2 頁圖 1-1 待審標記已渲染抽查，文字可讀、無圖片。Pandoc 對 zh-TW 翻譯表與 “Abstract” 術語顯示非致命提示，輸出成功。
- 注意：`dist/` 中先前政策制定前的正式輸出是舊產物，可能仍含未審圖像；它們未被本次正式建置覆寫。不得直接發佈舊輸出；未完成審查期間使用 `dist/preview/` 預覽。
- 待辦：由編輯確認圖 1-1 創作者／權利依據，並完成四類審查後逐目標核准；若來源無法確認，重新原創製作替代圖。英文內容建置尚未實作；目前只建置繁中內容，英文目標檢查是為未來出版保留。

---

## 2026-10-18｜V2.0 雙語出版架構建置

> 專案紀錄用途：history.md 不只是程式變更摘要，也要保存需求脈絡、決策理由、操作步驟、測試證據、失敗原因與後續建議，供未來演習、教學、簡報及影片製作使用。每個重要建置階段與上下文交接前都應補記，避免只留下最終產物而失去建置歷程。

### 需求與限制

- 依 `planning-v2/ARCHITECTURE-V2.md`、`planning-v2/CODEX-BOOTSTRAP.md` 將本專案升級為 zh-TW / en-US 雙語書籍與網站架構。
- 使用者明確要求不覆蓋舊章節、不刪素材、不以網路圖片作正式插圖、不發布網站、不推送 GitHub；本次只在工作副本進行可逆的新增與文件修改。
- 建置前 Git 工作樹已有多項修改、未追蹤章二稿件、素材、source pack、規範及測試；均視為使用者既有內容，不重置、不清理、不提交。

### 建置內容

- 讀取架構規格與 bootstrap 指令，盤點 V1 第一、二章、兩個素材資料夾與 source-packs。新建 `legacy/2026-v1/chapters/` 備份，納入兩章原稿、素材目錄和 source-packs，共 20 個檔案；產生 `legacy/2026-v1/migration-manifest.csv` 及 `metadata/migration-manifest.csv`，每項比對來源和備份 SHA-256，狀態均為 verified。V1 canonical 原稿保留在原路徑。
- 建立 `content/zh-TW/`、`content/en-US/` 共 60 章配對 scaffold、12 篇及 60 章穩定 ID 登錄、翻譯狀態表、術語／參考／圖像登錄資料模型及每章影像資料夾。CH01/CH02 在 V2 標記待遷移審校；英文全部標記翻譯待辦，未冒充正式譯稿。
- 新增中英章節模板、圖像權利及來源規範、翻譯管理、引用證據規範、品質 gate、Cinematic Editorial 設計系統、出版說明及 `AGENTS.md`。
- 新增 Astro + Starlight 網站候選骨架、雙語占位頁與編輯式 CSS，未配置部署。新增根／網站 npm scripts 及 Python V2 驗證器、單元測試、GitHub Actions 驗證 workflow。出版文件記錄 Pandoc/XeLaTeX 路徑及字型驗收條件；目前未宣稱 PDF 字型或版面已驗收。
- 更新 README、CHANGELOG、`.gitignore`，加入 V2 操作入口和 Node 產物排除規則。

### 驗證與限制

- `python scripts/v2_validate.py`：PASS，檢查 12 篇／60 章、雙語 60 對 scaffold、舊稿遷移雜湊、圖片核准 gate。
- `python -m unittest discover -s tests -p test_v2_architecture.py`：5 項測試全部通過，包括永久 ID 配對、遷移 SHA-256 與無自動部署 workflow。
- 嘗試 `npm --prefix apps/web install`；安裝命令在此環境持續無輸出，為免留下背景安裝程序而中止。故 Astro 依賴尚未安裝，網站 `npm run build` 尚未實際驗證；並非宣稱網站 build 通過。
- 尚未執行正式雙語書籍輸出；V2 章稿是占位 scaffold，不具出版內容。PDF 字型嵌入、渲染、雙語校對、引用外連檢查及網站視覺檢查均待後續。
- 沒有產生或下載正式插圖；待 CH01 figure plan 定稿後再製作原創底圖與可編輯 SVG overlay。
- 本次未提交、推送或發布任何內容。

### 後續檢查補記

- 新增 `scripts/validate/check_links.py`：預設檢查本地 Markdown 連結；只有明確加 `--network` 才對外部網站送 HEAD 請求，對 403/405/暫時網路錯誤標示為未能確認，不武斷判為失效。
- 首次執行本地連結檢查發現 README 指向尚不存在的 `docs/TERMINOLOGY.md`；已補建 V1/V2 術語導覽及 V2 術語資料契約，保留原 README 的連結，不改指向或移除。
- 重新核對全書目錄時發現第一章狀態使用全形括號，初始 parser 未拆出 status；修正目錄解析與 CH01/CH02 穩定 slug，並更新 V2 新建 scaffold 的標題、檔名及 metadata。只調整本次建立的 V2 占位檔，未更動 V1 原稿。
- 使用者特別要求 history.md 作為建置歷程教材素材，故本紀錄保存需求背景、決策、逐項改動、驗證命令與結果、失敗／中止原因，以及後續工作；重要建置階段及交接前均需補記。
- 最終重跑：`python scripts/validate/check_links.py`（本地 0 錯誤，3 外部 URL 未連網查證）、`python scripts/v2_validate.py`（PASS）、V2 unittest（5/5 PASS）、四個 V2 Python 腳本 `py_compile`（PASS）、`git diff --check`（PASS；Git 提示既有 CRLF autocrlf 轉換）。
- 將 history 維護要求寫入 `AGENTS.md`：未來重要整合需記錄背景、決策、變更、命令、測試、錯誤／限制和後續建議；交接或上下文壓縮前先補記，便於改編為演習、教材、簡報或影片。
- 依「書籍與網站共用 Markdown」原則補上 `scripts/publishing/sync_site_content.py`，把 `content/zh-TW` 和 `content/en-US` 的 120 個章節 scaffold 轉入 Astro 文件集合，並轉換 Pandoc heading ID 為網站可讀錨點。`apps/web/package.json` 的 build 會先同步；預設 Git 忽略生成的章節投影，以 canonical content 為唯一編輯來源。GitHub CI 增加同步與一致性檢查。
- 新增網站投影同步測試後共 6 項；同步腳本已生成 120 頁。網站 production build 仍因 Astro npm 相依安裝未完成而未驗證。

---

## 2026-10-18｜V2.0 架構驗證與 CH01 工作計畫

### Skill 警告檢查

- 使用者訊息中的路徑 `C:\Users\user.codex\...` 疑似缺少分隔反斜線；實際檔案位於 `C:\Users\user\.codex\skills\verify-content\SKILL.md`。
- YAML parser 確認開／閉 frontmatter 分隔、`name`、`description` 與名稱目錄一致性均有效；正文 309 行，`examples/`、`references/` 存在，該 Skill 已出現在 Codex 可用 Skill 清單。
- 因沒有證據顯示格式錯誤，未改動專案外 Skill 檔，也未建立新備份。目錄中已有一份 `SKILL.md.backup-20261018-114006`，未將其雜湊或新舊一致性視為本次驗收證據。若 UI 警告持續，後續應取得警告原文並重載 Codex 再定位；不以盲目改 frontmatter 掩蓋未知警告。

### 發現及修復

- V2 validator 原先只以文字模式比對章節 ID，並未完整核驗 parts、YAML、雙語狀態與錨點。現改為實際解析 metadata YAML、核對 12 篇及 CH01–CH60、翻譯 enum／frontmatter 一致性、雙語節錨點、術語 ID／雙語欄位／書目 ID，以及外部／inline 圖片阻擋。`translation-status.yaml` enum 補入實際採用的 planned、draft、draft-migration-pending。
- 新增 `schemas/term-v2.schema.json`，定義永久 term ID、繁中／英文首選詞和定義、語境、來源、狀態及審校 metadata。V2 validator 對新增詞條執行欄位及參考 ID 檢查；目前術語登錄為空，僅完成模型，沒有捏造詞條。
- `scripts/publishing/build_books.py` 原有 placeholder gate 但未檢查章稿正式審核、翻譯登錄或圖片權利。現要求完整 CH01–CH60、locale、章稿和 translation registry 均 approved；所有納入圖片需為本機存在、非外部／inline、已登錄、非空 alt、雙語 caption、權利／技術／編輯審查 approved 並有生成記錄。失敗在建置工具呼叫前中止。
- `scripts/check_fonts.py` 新增 `--require-pdffonts` 嚴格模式，遇檢查器缺失、字型未嵌、未包含指定字型家族或 font table 無法解析均非零退出；PDF 建置成功後自動呼叫該 strict gate。新增 mocked unit tests 覆蓋缺工具、未嵌入、錯誤字型、正確嵌入四種狀況。
- 建立 `planning-v2/CH01-V2-WORKPLAN.md`，內容僅是研究／寫作／翻譯／圖像／出版工作清單與驗收條件；未寫 CH01 正文或產生插圖。
- 新增 `BUILD-VALIDATION-V2.md` 記錄 Skill 檢查、架構結果、失敗命令、限制與建議；修正 `BUILD-REPORT-V2.md` 測試數及現況。

### 驗證命令與結果

- Skill frontmatter Python/PyYAML 檢查：PASS；未改檔。
- `python -m json.tool schemas/term-v2.schema.json`：PASS。
- `python -m py_compile scripts/v2_validate.py scripts/publishing/build_books.py scripts/check_fonts.py tests/test_font_validation.py`：PASS。
- `python scripts/v2_validate.py`：PASS；60 章、雙語配對、狀態、錨點、術語／圖片結構與 V1 備份雜湊通過。
- `python scripts/publishing/sync_site_content.py --check`：PASS，120 個 Astro 章節投影與 canonical Markdown 同步。
- `python scripts/validate/check_links.py`：PASS；本地連結 0 失效，3 個外部連結未進行網路查證。
- `python -m unittest discover -s tests -v`：PASS，17/17。含 V1 圖片權利 gate、V2 結構、書籍預檢及 strict PDF 字型的單元測試。
- `python scripts/publishing/build_books.py --locale en-US --format epub`：預期 fail closed，exit 2，原因為 CH01 `translation-needed`，未呼叫 Pandoc、未產出 EPUB。
- `npm --prefix apps/web run build`：Astro 網站 build 未通過；同步階段成功，後續報 `'astro' is not recognized`。`npm install` 先前長時間無輸出而中止；目前不能宣稱 web build 驗收成功。
- `Get-Command pandoc, xelatex, pdffonts`：三者皆不在 PATH。`Noto Serif TC` 可從 Windows 字型登錄找到，但這不是 PDF 字型嵌入證據。以 `--require-pdffonts` 試查指定 PDF 時，strict gate 正確 exit 2；沒有執行環境能實際產 PDF／確認嵌入。
- `git diff --check`：PASS；僅有 repository 既存 autocrlf 換行提示。本次未 commit、push 或部署。

### 後續

- 按 `planning-v2/CH01-V2-WORKPLAN.md` 由 ChatGPT/編輯完成研究、繁中稿與英文人工審校稿；Codex 再收錄、審核、建置與出版。
- 使用者安裝 Astro 依賴、Pandoc、MiKTeX XeLaTeX 和 Poppler `pdffonts` 後，重做網站、書籍與 PDF 嵌入實測；保留工具版本及輸出校樣。
- 若 verify-content Skill 的 UI 警告還在，請先重新載入 Codex 並提供精確訊息；frontmatter 檢查已通過，現階段沒有安全且必要的 Skill 文件修補。

### 後續建議：CH01 雙語圖文樣章

1. 逐節審校 V1 CH01 內容並遷移到 V2 zh-TW；補足來源原件頁碼及理論審查，保留可追溯來源 ID。
2. 建立 CH01 英文人工譯稿；對照章節錨點、術語、引文及圖說，完成專業編輯審校。
3. 定稿逐段 figure plan（永久圖號、插入錨點、教學目的、雙語 caption/alt、原創提示詞及審查人欄位）；生成 6–12 張依內容需求的原創圖或可編輯 SVG，不將此數量當硬性門檻。
4. 逐圖進行權利、技術及編輯審查；未三項核准不得進正式書籍／網站輸出。
5. 解決 npm 依賴安裝環境後 build Astro 樣站；在同一樣章驗證 zh-TW/en-US 路由、行動版、鍵盤操作、搜尋和圖說。
6. 從同源 Markdown 建置雙語 HTML、DOCX、PDF、EPUB；檢查中文字型嵌入、繁中文字形、英文斷行、圖表位置及實際校樣，記錄工具與字型版本。
7. 將章稿、雙語圖、figure manifest、術語、參考、鏡頭資料及測試報告封裝 CH01 V2 release pack；編輯驗收後才規劃批次遷移後續章節。

## 2026-10-18｜V2.0 雙語出版驗證與 CH01 重製計畫

- 依使用者要求閱讀三份 V2 啟動文件並驗證雙語架構、網站、出版工具、字型與圖片權利；不覆蓋 V1 第一、二章，不下載網圖，不發布、不推送，也不把 scaffold 標成正式出版。
- 新增 `BUILD-VALIDATION-V2.md`。報告將結果分為通過、預期阻擋與環境受阻，並建立 CH01 雙語逐段重製流程、12 張原創 figure brief、書籍及網站樣章驗收規準。
- 架構證據：60 個唯一章節 ID；zh-TW／en-US 各 60 檔。繁中 CH01–02 為 `draft-migration-pending`、其餘 58 章為 `planned`；英文 60 章皆 `translation-needed`，正式英文標題皆空白。V2 術語與 figure registry 目前為空，故只能判定架構完成。
- 網站：120 個 Markdown 投影一致性通過。npm 初次安裝長時間無輸出後中止；離線重試因 cache 缺件回報 `ENOTCACHED`，workspace cache 網路重試回報 registry `EACCES`；`astro` 未安裝，production build 未通過。
- 工具鏈：Pandoc 3.12.1 可用。以明確標示 DRAFT-SMOKE 的 CH01 暫存稿建立 EPUB 成功，ZIP 完整性通過（10 entries）；正式 build 對中英文未核准章稿均正確阻擋。XeLaTeX／pdfinfo／pdffonts 由 MiKTeX 提供，但初始化無權寫入使用者設定目錄，故 V2 PDF、實際字型嵌入與版面未驗收。
- 系統有 Noto Sans／Serif TC、PMingLiU、MingLiU、KaiU 字型。修正 `scripts/check_fonts.py` 的 Noto TC／CJK TC 雙向別名；未放寬嵌入或錯誤字型的失敗條件。
- 測試：`python scripts/v2_validate.py` PASS；`python -m unittest discover -s tests` 16/16 PASS；連結檢查本機 0 failures、3 個 URL 未決定性查證；網站投影 `--check` PASS；EPUB smoke PASS。Astro build 與 V2 PDF 明列為受阻，不列為通過。
- 未改動 `chapters/` 或 `legacy/` 原稿，未製作正式插圖，未發布、未提交、未推送。暫存 EPUB 只作工具鏈 smoke evidence。
- 下一步：先完成 CH01 繁中遷移、證據、段落 ID 與術語；凍結 revision 後進行英文人工編審；再完成 figure manifest 與少量代表圖；於可連 registry 的環境鎖定 npm；建立可重現 TeX 環境後做 PDF 嵌入、抽字及逐頁視覺驗收。

### 驗證紀錄環境差異補記（同日後續檢查）

- 同一 Google Drive 工作樹後續出現 `tmp/publishing-smoke/CH01-zh-TW-DRAFT-SMOKE.epub`。本次以 Python `zipfile` 重驗，10 個 ZIP members、`testzip()` 無錯；可證明暫存 EPUB 封裝完整，但不等於正式出版品或能證明目前 PATH 可呼叫 Pandoc。
- 先前同期紀錄記載 Pandoc 3.12.1 可用及 MiKTeX 初始化權限錯誤；本次 shell 的 `where.exe pandoc/xelatex/pdffonts` 則未找到。保留兩次觀察並標記為環境／PATH 差異；本次不宣稱可重現 Pandoc，也未聲稱已產生或驗證 V2 PDF。
- `BUILD-VALIDATION-V2.md` 已同步改成以上可重現範圍。`pdfinfo` 雖可能由 Codex bundled Poppler 路徑取得，也不能代替 `pdffonts` 檢查字型嵌入。
- V2 CI workflow 加入 `pip install -r requirements-v2.txt`，確保 PyYAML 等執行相依存在；並擴展路徑觸發條件。此 workflow 為 repo 設定，尚未由 GitHub Actions 遠端執行。

---

## 2026-10-18｜V2 出版環境實測與工具鏈修復

### 需求與安全邊界

- 使用者要求驗證 Astro 雙語網站、Pandoc 與新 PowerShell PATH、XeLaTeX PDF、字型實際嵌入／渲染，以及雙語 EPUB 結構；更新 `BUILD-VALIDATION-V2.md` 並清楚標出 PASS、FAIL、BLOCKED。
- 不寫正式章節、不動 V1 原稿、不取用網路圖片、不部署、不推送。所有書籍格式測試只用合成文字，產物寫在 `tmp/publishing-smoke/`。

### 網站故障定位與修正

- `apps/web/package.json` 已聲明 Astro、Starlight、TypeScript，但 `node_modules` 未裝；先前同步輸出 `.mdx`，遇到 V2 章稿中的 HTML 編輯註解時報 `Unexpected character !`。
- `npm ci --prefix apps/web --ignore-scripts --no-audit --no-fund` 依鎖定檔成功安裝 445 個套件；加入 `@astrojs/check` 和 `apps/web/src/content.config.ts` 的 Starlight `docsLoader()`/`docsSchema()`。
- `scripts/publishing/sync_site_content.py` 改為把 canonical `.md` 投影為 `.md`；不把資料庫專用 `locale`、`slug` 搬進 Starlight 頁面 metadata，保留同檔名語系配對及語系目錄路由。同步器移除的是舊版產生的 CH*.mdx 投影；canonical 原稿未修改。
- 生產建置前曾看到 Starlight auto collection 的重複 ID，確認由投影 frontmatter `slug` 跨語言相同造成；明確設定官方 docs loader 並省略 `slug` 後，警告消失，語系路由分別生成。
- 最終 `npm --prefix apps/web run build` PASS：123 pages built；`dist/en` 與 `dist/zh-tw` 各 61 個頁面（首頁 + 60 章）。`npm --prefix apps/web run check` 為 0 errors/warnings/hints；同步檢查 PASS。

### Pandoc / MiKTeX / PATH

- 本次查明原本 Pandoc 已安裝：`C:\Users\user\AppData\Local\Pandoc\pandoc.exe`，版本 3.12.1；該目錄本已在 User PATH，但 Codex 原始 process PATH 是啟動時快照，故當前 shell 最初無法直接解析。
- 從 Pandoc 官方 release 下載 3.12.1 zip 並解壓到使用者目錄 `C:\Users\user\AppData\Local\Programs\Pandoc\3.12.1`，版本也是 3.12.1；同時把該目錄及 MiKTeX bin 加到 User PATH。新 PowerShell 行程讀取系統／使用者 PATH 後，`Get-Command pandoc,xelatex,pdffonts` 成功；依 PATH 順序解析 Pandoc 到原本的 `AppData\Local\Pandoc`。
- 本機 XeLaTeX 26.5、pdffonts 24.04.0、pdftotext、pdftoppm 均在 MiKTeX bin 可用。
- 診斷：本次在 `D:\мой\tmp\tools\pandoc-3.12.1` 留有下載與解壓暫存檔；多出的 Pandoc 本機安裝副本也留在 `AppData\Local\Programs\Pandoc\3.12.1`。清理用遞迴刪除命令遭執行環境 policy 阻擋，沒有改用其他方式繞過。既有 Pandoc 及新 MiKTeX PATH 均可用；若日後整理，可人工移除這兩個本次新增位置及 User PATH 對應片段。

### 中英 PDF 實測與字型原因

- 新增 `scripts/publishing/smoke_test_formats.py`，產出 `SMOKE-zh-TW`、`SMOKE-en-US` 的 Markdown、PDF、EPUB、文字抽取和 PNG 頁面；這些不是出版內容。
- `Microsoft JhengHei` 繁中和 `Times New Roman` 西文作為 PDF 字型。兩語 PDF 的 `pdffonts` 都顯示 requested font `emb=yes`、`sub=yes`、`uni=yes`；繁中 PDF 也嵌入 Microsoft JhengHei Regular/Bold。兩語文字抽取、PNG 渲染成功，並人工檢視頁面：繁中字形正常，英文襯線字及段落正常。
- `Noto Serif TC` 雖在 Windows Fonts 登錄，其檔案名是 `NotoSerifTC-VF.ttf`。XeLaTeX/dvipdfmx 生成 PDF 報 `dvipdfmx:fatal: Invalid font: -1 (0)`；把該字型僅用於英語 `mainfont`、完全不設 CJK 字型後仍相同，故已排除「只有 CJKmainfont 設定」的解釋。直接故障確認在目前 MiKTeX/dvipdfmx 的字型輸出／嵌入階段；variable-font 相容性是待測根因假說，靜態 Noto 字型尚未對照。
- 因 Microsoft JhengHei 已通過實際嵌入／渲染，`build_books.py` 將它作為繁中預設，西文預設 Times New Roman；所有正式 PDF（中／英）均先用 XeLaTeX 並經 strict `pdffonts` gate。

### 雙語 EPUB 驗證

- smoke EPUB 用 Pandoc 3.12.1 生成，Python 驗證 ZIP CRC、`mimetype` 首項且未壓縮、`container.xml` rootfile、OPF `dc:language` 與 XHTML 對應語文文字。`zh-TW` 和 `en-US` 均 PASS。
- Pandoc 對 `zh-TW` 顯示內建 UI 翻譯檔缺失（`translations/zh.yaml`、`Abstract` 未翻譯）警告；EPUB 語言 metadata 和本文字沒有缺損。正式章樣要以閱讀器和 EPUBCheck 再做最終驗收。

### 書籍正式 gate 與最終測試

- `build_books.py --locale zh-TW --format pdf` exit 2，因 CH01 為 `draft-migration-pending`；`--locale en-US --format epub` exit 2，因 CH01 為 `translation-needed`。這是預期 BLOCKED，沒有正式整書輸出。
- `python scripts/v2_validate.py` PASS；`python scripts/validate/check_links.py` 本地連結 PASS，3 個外部 URL 未網路查證；`python -m unittest discover -s tests -v` 17/17 PASS；五個 Python 腳本 `py_compile` PASS。
- 不使用網站部署流程、不建立正式輸出到 `dist/`、沒有 commit/push。`BUILD-VALIDATION-V2.md` 更新 current-state 矩陣，並明確標示本節覆蓋先前「工具缺失」敘述；`docs/PUBLISHING-V2.md` 補上重跑方式與實測字型結果。

### 下一步

1. 若需要用 Noto Serif TC 作正式字體，先以該字型的靜態 Regular/Bold OTF/TTF 與 MiKTeX 重跑相同 smoke test，保留 `xelatex` log、`pdffonts` 結果和 PNG；不要在目前結果未解前把 Noto 設為預設。
2. 對已審核的中英文 CH01 樣章執行正式 EPUB/PDF gate；加跑 EPUBCheck，檢視目錄、頁碼、註腳、連結和兩種閱讀器顯示。
3. 補查 3 個外部連結與 CH01 理論來源；完成稿件人工核准前，正式整書輸出維持 BLOCKED。
4. 如要清理本次多出的 Pandoc 副本與暫存，可在人工確認後移除 `C:\Users\user\AppData\Local\Programs\Pandoc\3.12.1`、`D:\мой\tmp\tools\pandoc-3.12.1`，再從 User PATH 移除完全相符的兩個路徑片段；原本的 `C:\Users\user\AppData\Local\Pandoc` 不要移除。
