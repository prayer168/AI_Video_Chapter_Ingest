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

## 2026-10-18｜CH01 V2 雙語致敬案例整合與驗收

### 工作目的與輸入盤點

- 使用者要求繼續第一章 V2 整合：遞迴查看 `staging/CH01-V2`、`staging/Homage-V1`，讀整合指令，對照中英文稿與章節規格，整合電影案例、雙語圖文和術語；保留原稿、先備份、執行網站／PDF／EPUB／字型／圖片權利檢查並產出最終驗收報告。
- 實測兩個 staging 目錄存在，但遞迴檔案數皆為 0；目錄有唯讀屬性。故改用 repo 中既有素材包：`chapters/AI-Video-Bible-Homage-V1-CH01-Supplement-DRAFT.zip` 及 `chapters/source-packs/AI-Filmmaking-Bible-CH01-Codex.zip`。讀取其 README 和 CODEX 整合／指令檔；ZIP 原件保持不變。
- Homage 素材包說明其為草稿補充包，要求保留原中英文稿、以 paragraph IDs 整合、`CH01-HOMAGE-FIG-*` 命名、候選片單不直接變正式目錄、插圖須原創及經人工權利／技術／編輯審查，不可部署或推送。依此要求操作。

### 備份與變更

- 所有 V2 canonical 稿、CH01 figure manifest、全域術語／引用／提示詞／資產 registry、章節 registry／workplan、validator、V2 metadata registries、既有驗收報告及本檔，在修改前複製到 `backups/CH01-V2-integration-20261018-132434/`；`MANIFEST.json` 記錄各檔與來源 ZIP 的基線 SHA-256 及長度。原始 V1 章稿及兩個來源 ZIP 未覆蓋、移動或刪除。
- 中英文 `CH01-S09` 加入五組案例與一致的 `CH01-P001`–`CH01-P005` IDs：*Citizen Kane*、*Rashomon*、*A City of Sadness*、*In the Mood for Love*、*Yi Yi*。保留可查證電影資料、評論性解讀、實務轉譯及教學練習的區分；版次、場景 timecode、完整鏡頭觀察仍待作者補查。
- 登錄六個雙語 CH01 詞條草案、R013–R021 九筆來源、五份雙語原創插圖 briefs 和圖說／alt 草案。五張插圖均未生成、未嵌入、未核准；未取用網路第三方圖片。
- `scripts/v2_validate.py` 放寬圖號規則，只允許 CH01 使用 `CH01-HOMAGE-FIG-###`；新增 namespace tests。將兩語參考文獻錨點改成 Pandoc span，避免草稿 PDF 內引用回鏈成 undefined refs。繁中圖像 brief 使用 repo 相對路徑文字，避免靜態網站暴露無法存取的資產超連結。
- 更新 Starlight canonical projection（120 章檔投影，改動 CH01 雙語兩檔）、整合差異報告及 `reports/CH01-V2-FINAL-ACCEPTANCE.md`。
- 把 `tmp/CH01-V2-draft-preview/` 加進 `.gitignore`，防止本機 PDF／EPUB smoke-test 輸出被誤當正式出版資產；本機檔案保留供檢視。

### 驗收證據

- `python scripts/v2_validate.py` PASS；`python scripts/validate_project.py` PASS（12 篇、60 章、52 術語、21 引用）；`python scripts/validate/check_links.py` PASS（0 failures，3 外部 URL unchecked）。
- `python -m unittest discover -s tests -v` PASS，22/22。第一次測試因網站投影落後 canonical 稿而有 1 個失敗；執行 `sync_site_content.py` 後重新測試通過。另新增回歸測試，確認英文 PDF 因雙語 glossary 也指定 Microsoft JhengHei CJK font。最終 `git diff --check` 沒有 whitespace error，僅提示 repo 既有 CRLF/LF 轉換設定。
- `npm --prefix apps/web run check`：0 errors／warnings／hints。Starlight content loader 另各印一個中／英文 CH01 duplicate ID 訊息。`npm --prefix apps/web run build` 完成 123 pages，但 duplicate ID 訊息仍須追查；網站未部署。
- Pandoc 3.12.1 + MiKTeX XeLaTeX 將 canonical CH01 雙語稿生成暫存 PDF／EPUB。PDF 的 `pdffonts` strict gate 顯示 Microsoft JhengHei（中）與 Times New Roman（英）有 embed=yes；中英 `pdftotext`、PDF 首頁 PNG 渲染及視覺檢查通過。初驗發現英文 PDF 未設定 CJK fallback，造成中文缺字警告；`build_books.py` 已修正為中英文 PDF 都指定 Microsoft JhengHei CJK font 與 Times New Roman main font。兩語 PDF 均 `pdffonts` strict PASS、XeLaTeX missing-character warning=0，文字抽取和 PNG 渲染通過。
- PDF 視覺抽查發現 glossary 寬表格欄位擠壓；兩語稿改為逐詞條版式，英文雙語術語頁重新輸出及目視檢查無重疊。全章其餘版面須待正文完整後驗收。
- 中英文 EPUB ZIP CRC、mimetype 順序／壓縮方式、container、OPF language、案例文字 smoke checks 通過；EPUBCheck 未安裝，因此正式 EPUB 規格符合性仍 BLOCKED。
- `image_policy.py --target zh-TW-book/en-book` BLOCKED，原因為舊 V1 `ASSET-CH01-FIG-01` 的作者、授權、權利及核准狀態未解；CH01 V2 本身無嵌入圖，新增 5 份圖像計畫仍 pending。正式 builder 分別因繁中 `draft-migration-pending`、英文 `translation-needed` 而安全拒絕輸出。
- 草稿 PDF/EPUB 都放在 `tmp/CH01-V2-draft-preview/`，不是正式出版物。沒有部署、commit 或 push。

### 未完成與後續

- CH01 大部分 S01–S12 仍為空白模板；英文正式題名、完整翻譯、電影版本及 timecode、理論學術來源需補齊及編輯審查。
- 生成五張原創示意圖後，保存工具／版本／日期／prompt／修改履歷，完成 rights、technical、editorial reviews 後才能入正式書稿。
- 排除網站 loader duplicate IDs；正式正文完成後重做多頁 PDF 版面檢查；安裝 EPUBCheck 並在閱讀器複測。
- 判定 V1 pending 插圖是否仍進入正式出版範圍，未經授權不可將 V1 asset 帶入 V2 正式輸出。
- 詳細執行狀態、命令與解決方式見 `reports/CH01-V2-INTEGRATION-DIFF.md` 與 `reports/CH01-V2-FINAL-ACCEPTANCE.md`。

## 2026-10-18｜CH01 技術警告與出版審查狀態修復

### 使用者要求

- 排除雙語網站 Duplicate ID 警告、PDF 繁中字型缺字、EPUBCheck 未安裝，以及 CH01 編輯審稿／插圖權利待審問題。
- 依專案既有規範，不把未完成稿或未審核圖片宣稱正式核准；不部署網站、不推送 GitHub。

### 修復與實測

- Astro/Starlight 目前檔案樹有每語各一份 CH01 Markdown。2026-10-18 乾淨重建 `npm --prefix apps/web run build` 產生 123 頁，log 無 `Duplicate id`；確認 `/zh-tw/ch01-cinematic-language/` 與 `/en/ch01-cinematic-language/` 頁面存在。舊警告在現況未能重現，故不推定歷史根因；移除指向不存在路由的手寫 sidebar，採 Starlight 語系導覽。
- 安裝 W3C／DAISY EPUBCheck v5.4.0 至 `%LOCALAPPDATA%\Programs\EPUBCheck\5.4.0\epubcheck-5.4.0\`（Java 18）；新增 `scripts/publishing/check_epub.ps1` 供重跑。CH01 繁中、英文 draft EPUB 均通過，errors/warnings/informational messages/references 全為 0。
- 從已生成的 CH01 繁中／英文 PDF 重新以 MiKTeX `pdffonts` 嚴格檢查：各 7 個字型項目全部 `emb=yes`、`sub=yes`、`uni=yes`；繁中 PDF 有 Microsoft JhengHei Regular/Bold，英文 PDF 亦嵌入 Times New Roman 及 Microsoft JhengHei fallback。抽取 PDF 文字可還原預期中英文字。XeLaTeX 缺字警告=0 維持先前建置證據。此為草稿技術 PASS，完整出版校樣仍需重做。
- 建立 `reports/CH01-EDITORIAL-AND-RIGHTS-REVIEW.md`。Codex 審查已完成，結論為退修：九個必要章節區塊空白；英文需完整翻譯審校；案例缺合法觀看版次、timecode 及學術理論來源。原創插圖只有五個 briefs、沒有實際圖檔；章稿無嵌入圖片或第三方圖片。故沒有成品可核准，也不偽造權利人／作者簽核。
- 更新 `reports/CH01-V2-FINAL-ACCEPTANCE.md`，修正 duplicate／EPUBCheck 的過期描述，記錄上述新測試與仍未解的內容／授權條件；`docs/PUBLISHING-V2.md` 補 EPUBCheck 固定版本、安裝位置、官方連結與 Windows 驗證命令。

### 狀態判定

- 已解決：網站 duplicate ID 警告（本輪建置未再現）、PDF 字型嵌入／缺字技術警告、EPUBCheck 缺席。
- 已完成審查但需退修：CH01 內容編輯審查；章稿不可核准／正式出版。
- 尚待作者／權利審批：五張未製作插圖及 V1 `ASSET-CH01-FIG-01`。無實際圖檔，不能執行成品權利審批；未將 pending 改成 approved。
- 未部署、未 commit、未 push。完整審查證據：`reports/CH01-EDITORIAL-AND-RIGHTS-REVIEW.md`。
- 專案回歸測試：`python scripts/v2_validate.py` PASS；`python scripts/validate_project.py` PASS（12 parts、60 chapter IDs、52 terms、21 references）；`python -m unittest discover -s tests -v` PASS（22/22）；`sync_site_content.py --check` PASS；`npm --prefix apps/web run check` 0 errors/warnings/hints；`git diff --check` PASS（僅有既有 CRLF 提醒）。`python scripts/image_policy.py --target zh-TW-book` 依預期 BLOCKED，唯一資產是 V1 `ASSET-CH01-FIG-01`，缺作者／授權與審核資料。兩份 V2 CH01 Markdown 均確認 0 embedded image refs。

## 2026-10-18｜CH01 V2.1.0 雙語正文補齊與最終章節級驗收

### 使用者要求與保護範圍

- 使用者指出不要只重報先前 22/22 技術測試，而要讀最新驗收報告、補齊 9 個空白必要章節、完成中英案例／術語／來源／圖說與逐節對照、查實際插圖及權利狀態，重跑網站／PDF／EPUB／全測試並交付 `CH01-FINAL-ACCEPTANCE.md`。
- 不覆蓋 V1、不發布網站、不 push GitHub；未 commit、未部署。
- 在修改 canonical CH01、V2 metadata、圖 manifest、舊驗收報告前，先建立 `backups/CH01-editorial-20261018-193937/`。`MANIFEST.json` 記錄 11 個工作檔的 source 與 backup SHA-256；V1 原稿仍位於 `legacy/2026-v1/` 且 migration hash tests 通過。

### 內容與研究整理

- 更新 `content/zh-TW/chapters/CH01-cinematic-language.md` 和 `content/en-US/chapters/CH01-cinematic-language.md` 至 revision `2.1.0`，13 個共用 section anchors：學習目標、先備知識、術語、歷史原理、傳統製作、AI 轉換限制、詳細 workflow、模型中立 prompt、案例、錯誤與 QA、練習評量、來源及結語。正文不是 placeholder；每節均有中英實質內容。
- 保留五組電影致敬案例 ID `CH01-P001`–`P005`，加入具體原創轉譯練習、圖說與 alt 草案；另整理 V1《窗邊的第一道光》六鏡頭虛構教學例。片段時間碼明確說明是腳本估計值／尚未依合法觀看片版記錄，不能被當成片源量測資料。
- 新增 `metadata/translations/CH01-alignment.yaml`，配對 S01–S13、26 個術語 IDs、5 個電影案例、5 個圖說與共享來源；中英稿狀態由 scaffold 狀態改為 `review-needed`，未標成 approved。
- 將 20 個電影語言基礎詞條補入 `metadata/terminology.yaml`（V2 CH01 總計 26 個雙語詞條）；全部保留 `draft`，術語採用版本及頁碼 locator 尚待人審。更新 CH01 的中英章名、翻譯狀態與 registry title。
- 清理引用編號碰撞，新增 R022（Graig Uhlin, *Introduction to Film & TV*）、R023（Ned Thanhouser, LOC 早期美國電影文章）、R024（Cao et al., PLOS ONE Kuleshov 2024）到 bibliography／project references。網頁資料核對來源包括 [Oklahoma State open textbook](https://open.library.okstate.edu/introfilmtv/)、[Library of Congress PDF](https://lcweb2.loc.gov/static/programs/national-film-preservation-board/documents/evidence.pdf)、[Lund University 2016 study record](https://portal.research.lu.se/en/publications/does-the-kuleshov-effect-really-exist-revisiting-a-classic-film-e/) 和 [PLOS ONE 2024 study](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0308295)。歷史敘述特別限定在來源明確討論的美國 ca. 1907–1913，不外推全球。
- 刪除正文原先借用 R017《紐約客》頁面支撐長鏡頭／門框構圖的說法；目前此來源不再作正文證據。R016 被準確標記為《海上花》評論中引用《悲情城市》一幕，而非《悲情城市》專論。對 Kuleshov 用 R005 2016 及 R024 2024 設計和結果作限縮摘要，不寫成普遍心理定律。

### 插圖與權利盤點

- 以實際遞迴檔案清單查 `assets/chapters/CH01/`：只有五份 `homage/briefs/CH01-HOMAGE-FIG-*.md` 及 `figure-manifest.yaml`，沒有對應 raster 或 SVG 成品。V2 CH01 章稿 0 個 image embed／外部圖片 URL；`chapters/01-01-cinematic-language-assets/` 的現存檔只有 shot JSON 和 image-to-video 提示詞，不是插圖。
- 對齊五個中英文 caption／alt 到 `assets/chapters/CH01/figure-manifest.yaml`。五筆 `asset_original`／`asset_approved`、生成工具／版本／日期均 null；rights、technical、editorial 均保持 pending。沒有把不存在的圖片宣稱完成。

### 出版建置與測試

- 加入 `tests/test_ch01_content.py` 五個回歸測試：逐節實質正文、translation ID/case anchors、26 個雙語 term 對照及 registry、引用鍵及 fragment anchors、五張缺圖不得標 approved。新測試加既有測試共 27/27 pass。
- 重新生成 canonical-to-Astro 投影；更新章稿後第一次增量 `npm --prefix apps/web run check` 會對兩個 CH01 IDs 報 duplicate id。讀取 Astro `glob.js` 後確認：loader 在 store 已有同 ID、但內容 digest 改變時亦使用 duplicate 訊息，之後覆寫同一筆；這次每語系來源樹各只有一個 CH01 檔案。完成該次 store 更新後立即再跑 check：0 errors/warnings/hints；再跑 `npm --prefix apps/web run build`：123 頁、無 duplicate id。故判定是內容變更後的增量 store 訊息，不是雙份來源文件；最新檢查與建置乾淨。網站未部署。
- 章節級草稿文件輸出至 gitignored 暫存 `tmp/CH01-revision-2.1.0-20261018/`。初次 EPUBCheck 發現 16 個 RSC-012 undefined fragment errors，定位為 citation 有 href 但 bibliography anchor 沒被空 Markdown link 輸出。改用明確 `<span id="ref-Rxxx"></span>`、增加回歸測試後重建；中英文 EPUBCheck 5.4.0 各 0 errors／warnings／informational／references。
- 最終中英文 PDF 均用 Pandoc 3.12.1、MiKTeX XeLaTeX、Times New Roman + Microsoft JhengHei CJK。`pdffonts` 嚴格檢查所有列出的字型 emb/sub/uni 均 yes；`pdftotext` 可抽取中英正文／術語，XeLaTeX log 缺字警告 0。PDF 初次看到四欄 glossary 的 ID 欄過寬，改為雙欄術語／定義後重建；抽查繁中 PDF pages 2–4 可讀且續頁有表頭。這是章節級草稿 proof，不是正式 60 章書籍。
- `python scripts/v2_validate.py`、`python scripts/validate_project.py`（12 parts、60 chapters、52 legacy terms、24 refs）、`python scripts/publishing/sync_site_content.py --check`、`python scripts/validate/check_links.py`（0 failures；0 network checked、5 not conclusively checked）、27/27 unittest、`git diff --check` 均通過。`git diff --check` 僅提示既有 LF→CRLF 設定。

### 報告與現況

- 建立完整 [`reports/CH01-FINAL-ACCEPTANCE.md`](reports/CH01-FINAL-ACCEPTANCE.md)，逐項列明通過、blocked 和 needs-human-review、輸出證據與正式出版判定。
- 更新 `reports/CH01-EDITORIAL-AND-RIGHTS-REVIEW.md` 以反映九區塊已補正文但退修、圖像 pending；將舊 `reports/CH01-V2-FINAL-ACCEPTANCE.md` 改成指向最新報告的相容索引，避免舊結論繼續聲稱九區塊仍空白。
- 結論為 **CH01 未達正式出版標準**。具體待辦：作者選定五片合法觀看版本並補 timecode／逐鏡觀察；電影研究者核對理論和術語 locator；專業雙語編輯核稿；五張圖製作或明確排除並完成 rights／technical／editorial 審查；處置 V1 `ASSET-CH01-FIG-01` 權利記錄；完成 PDF 全頁與 EPUB 閱讀器校樣。正式全書 build gate 在 60 章全部 approved 前仍拒絕輸出，此為預期。
- 本輪沒有 commit、push、部署或修改 V1。所有草稿原始檔保持可編輯。

## 2026-10-18 — CH01 V2.1.0 五張插圖整合受阻（來源檔不可讀取）

- 使用者要求將五張 CH01 電影致敬原創插圖納入中英文章稿、圖稿 manifest、圖說、權利來源紀錄及驗收報告，並重跑網站、PDF、EPUB 與圖號／同步檢查。
- 收到的來源位置為 `/mnt/data/黑白電影感的沉思室內_сц景.png`、`/mnt/data/霧林三視角_劍刃下的求生瞬間.png`、`/mnt/data/雨巷門前的沉默一家人.png`、`/mnt/data/紅綠暮色中的擦肩而過.png`、`/mnt/data/暮色窗前的城市凝望.png`。目前 Windows Codex 工作環境無法讀取 `/mnt/data`；以精確檔名檢查專案、`Downloads`、使用者 Temp 和 `/mnt/data`、`C:\mnt\data` 候選路徑，均未找到檔案。
- 已確認 V2.1.0 中英文原稿、manifest 與最新驗收報告仍在；章稿目前保留舊的 CH01-HOMAGE-FIG 草案紀錄。由於實際 PNG 不存在於可讀工作區，未改動章稿、manifest 或出版輸出，亦未把既有草案冒充為新圖、未標記核准，沒有重跑無法代表新素材的出版測試。
- 整合待來源 PNG 可讀後進行。請將五張圖直接附加到此工作對話，或複製至 `assets/chapters/CH01/originals/`；收到可讀檔案後再備份並執行實際圖檔、圖說與權利狀態整合及全套測試。
- 本次只更新此歷史紀錄；沒有修改 V1／V2 章稿、移動或刪除素材、推送 GitHub 或部署網站。修改前 history 備份：`backups/CH01-figure-ingest-attempt-20261018-203728/history.md`。

## 2026-10-18 — CH01 五張致敬插圖完成匯入及出版校樣修正

- 後續收到使用者提供的 ZIP：`C:\Users\user\Downloads\AI-Video-Bible-CH01-Five-Homage-Images-DRAFT.zip`。`python -m zipfile -t` 驗證封裝完整；ZIP SHA-256 為 `98099DA5F231060FE6548AFE1238CE2C6000545F250CF47CDA9E862670D392EC`。五張 PNG 均為 1619 × 971 px，逐檔 SHA-256 與 ZIP manifest 一致。原目標目錄當時為空，檔案以新名稱匯入，無覆蓋；ZIP 留在 Downloads。
- 修改前備份位於 `backups/CH01-five-figures-20261018-204447/`，含 `BACKUP-MANIFEST.json` 和受影響原稿、manifest、registry、翻譯對照、測試、網站投影與報告的副本。V1 原稿和既有圖片未修改。
- 依既有永久 ID CH01-HOMAGE-FIG-001–005，完成中英稿插圖位置、alt、雙語圖說、`figure-manifest.yaml`、`figure-registry.yaml`、`CH01-alignment.yaml`、`figure-captions.md` 及 `IMPORT-AND-RIGHTS-RECORD.md`。顯示標籤為 1-3A、1-4A、1-4B、1-4C、1-5A。五張圖片保持 `draft-generated`、rights pending、technical/editorial pending、`asset_approved: null`、`pending-publication-approval`。ZIP 未提供模型、工具版本、日期、完整 prompt、操作者及修改歷程，均明確記作未知；圖像與原始 briefs 風格差異交由作者判斷。
- 初次視覺校樣發現 HTML 圖片可用，但 Pandoc 直接由 canonical Markdown 建 PDF 時圖片相對路徑基準不一致。網站同步腳本現把資產投影至網站公開路徑，並驗雜湊／防止衝突覆寫；出版校樣另使用暫存 Markdown 將資產引用改為專案根相對路徑，canonical 原稿保持不變。
- 新增 `scripts/publishing/figure-captions.lua`，將 Markdown 圖片與後續圖說合成 Pandoc Figure，固定圖片和圖說同頁，保留 alt 和永久 ID。抽查發現首圖前導讀重複顯示圖號、繁中自動圖名顯示簡體「图」；已將前導讀標籤改為一般視覺觀察並由 Lua filter 將繁中 `\\figurename` 設為「圖」。需以最新 finalproof 檢查所有五圖分頁、圖號文字與圖說。舊版 layoutproof／figureproof 保留作差異紀錄，不視為最新輸出。
- 自動檢查：網站 Astro check 0 errors／warnings／hints，build 123 pages；雙語網站各 5 figure／5 圖／5 captions／5 alt，網站副本 SHA-256 與 canonical 圖片一致。兩語 EPUB 章節草稿及 EPUBCheck 5.4.0 均為 0 errors、warnings、informational、references。`python -m unittest discover -s tests -v` 29/29 PASS；`v2_validate.py`、`validate_project.py`（12 parts、60 chapters、52 legacy terms、24 references）、`sync_site_content.py --check`、`check_links.py`（0 failures、5 inconclusive）及 Python compile 通過。`image_policy.py --target zh-TW-book` 仍因舊 V1 `ASSET-CH01-FIG-01` 權利欄缺件而 BLOCKED，這是 V1 舊 gate，不代表 V2 五圖已核准。
- PDF 重新排版時先用 PyMuPDF 文字抽取確認圖與 caption 同頁；後續校樣發現首圖觀察段重複寫出顯示圖號且 zh-TW 自動標籤需繁體化，已修正並重建。請完成當前 finalproof 編譯後再記錄各頁標籤、caption 配置。Windows 此次 shell 找不到 `pdffonts`／`pdftotext`，不得據此聲稱最新 PDF 的嵌入字型已通過；可在有 Poppler 的環境或 PDF 閱讀器字型面板補驗。此前版 PDF 的字型檢查不得直接轉作新檔證據。
- 更新 `reports/CH01-FINAL-ACCEPTANCE.md`：交代實際檔案／hash、建置測試、待審項目及正式出版未達標；待 finalproof 完成後補入最後校樣證據。`history.md` 保留此前來源不可讀的失敗嘗試作為過程紀錄，本段記錄後續實際完成與更正。
- 本次未發布網站、未 commit／push GitHub、未核准任何插圖或章稿。下一步需完成 finalproof 編譯與抽頁目視、重建 EPUB／網站及回歸測試，核對報告，並列出人工權利／電影研究／翻譯審查。

### 2026-10-18 — finalproof、雙語 EPUB 與網站校驗完成

- 依上一筆記錄完成兩語 PDF finalproof（繁中 14 頁、英文 20 頁），再以 PyMuPDF 從文件中抽取字型串流：繁中 7 種、英文 6 種均有非空嵌入資料；繁中 PDF 包含 Microsoft JhengHei，英文包含 Times New Roman。將含圖頁逐頁轉成 PNG 檢視；五張圖都與各自完整圖說位於同一頁，指定圖號各出現為圖說標籤一次，繁中顯示「圖 1-3A」等繁體圖名。檢視影像存於 gitignored `tmp/CH01-V2.1.0-five-figures-20261018/visual-review-finalproof/`。
- 修正後網站已重新同步及建置；`astro check` 0 errors／warnings／hints，完整 build 123 pages。Astro 初次 loader 會短暫提示 canonical page ID 重複，完整同步後內容 IDs 唯一、`astro check` 無診斷；不是網站輸出錯誤。最後 HTML 確認各語 5 個 CH01 內容 figure、5 圖、5 圖說、5 alt，全部 ID 唯一且圖片雜湊相符。
- 兩語 EPUB 已依最新稿和 filter 重建。Pandoc 對 `translations/zh.yaml` 和 Abstract 翻譯有非阻斷 warning；EPUBCheck 5.4.0 中英各 0 errors／warnings／informational／references。ZIP CRC、五個 XHTML figure、圖片、alt、caption 與穩定 IDs 均通過。
- 29/29 unittest、`scripts/v2_validate.py`、`scripts/validate_project.py`、`sync_site_content.py --check`、`git diff --check` 全通過。外部連結檢查仍有 5 個網路 URL 無法定論；正式出版 gate 因正文審稿與圖像 rights／technical／editorial pending 按預期 BLOCKED。舊 V1 圖權利資料仍待單獨處置。
- 更新 `reports/CH01-FINAL-ACCEPTANCE.md` 的 PDF／EPUB／網站證據與 finalproof 檔案位置，加入缺少模型／生成提示詞、人物／服裝／構圖相似性等人工待審項。結論仍是 CH01 未達正式出版標準。
- 此次全程未覆蓋 V1 或既有原圖；未批准任何圖、未部署網站、未 commit／push GitHub。所有 build 及頁面 PNG 僅存於 tmp 草稿目錄。
