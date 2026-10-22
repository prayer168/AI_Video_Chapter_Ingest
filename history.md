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
# 2026-10-18 — V4 Codex chapter pipeline foundation and CH01 verification

- User requested an upgrade to a Codex one-stop chapter production workflow, preserving V1/V2, no paid API without authorization, no publishing/push, and an end-to-end CH01 check.
- Audited the existing bilingual V2 project and CH01 V2.1.0. Created the safety snapshot `backups/V4-pipeline-20261018-211633/` before modifying the current acceptance report or history.
- Added project Skill `.codex/skills/ai-video-bible-chapter-pipeline/SKILL.md`, workflow SOP, chapter and acceptance templates, reusable prompt templates, bilingual term schema, image generation setup notes, checkpoint runner, image adapter interface and safe test double. Mirrored the Skill to `C:\Users\user\.codex\skills\ai-video-bible-chapter-pipeline\SKILL.md`; validator passed with UTF-8 mode enabled.
- The checkpoint runner inventories existing CH01 canonical sources and SHA-256 values, creates resumable per-run JSON/checklists, and refuses to mark a run complete while any gate is non-PASS. It does not edit canonical chapter text or synthesize fake media.
- Image capability audit found no locally configured ComfyUI/Ollama in the previous environment inspection. Native image generation is exposed in this Codex environment, but actual billing/terms and an explicit budget cap are not approved. No generation tool, external API, or API key was used; adapter stays blocked by default.
- E2E checkpoint: `production/runs/CH01/20261018T211950+0800-6ddc17e8/`. Five already-existing CH01 images were neither regenerated nor modified. Existing editorial/rights and missing-provenance issues remain open; no canonical editable SVG was found, so no new figure number was invented.
- Validation: 35/35 Python tests PASS; `v2_validate.py` PASS; `validate_project.py` PASS (12 parts, 60 planned chapters, 52 terms, 24 references); site sync check PASS; Astro check 0 errors/warnings/hints; Astro build PASS with 123 pages. Existing CH01 finalproof PDF and EPUBCheck results are referenced in the acceptance report, not misrepresented as new V4 builds.
- Added `CHAPTER-PIPELINE-TEST-REPORT.md`; appended V4 status to `reports/CH01-FINAL-ACCEPTANCE.md`. CH01 remains not publication-ready pending source/timecode verification, professional bilingual editing, image provenance/rights and author approval.
- No V1 source, V2 canonical chapter, or existing illustration was overwritten or deleted. No website deploy, GitHub commit, or push was performed.

# 2026-10-18 — CH01 follow-up: reconcile superseded editorial report

- 使用者要求接續完成未竟章節工作，並在每章結束時回報章號；本次依 V4 Skill 與 SOP 先延續目前有明確草稿與工作紀錄的 CH01，不臆測後續章號。
- 重新讀取專案 Skill、V4 SOP、CH01 acceptance report、editorial/rights report、manifest、run log 及根目錄編輯規則。
- 發現 `reports/CH01-EDITORIAL-AND-RIGHTS-REVIEW.md` 仍保留五圖匯入前的陳述（圖檔不存在、manifest 無實檔），會與後續 V2.1.0 最終驗收報告衝突。修改前備份至 `backups/CH01-followup-20261018-214140/`，包括兩份報告及本歷程檔；`BACKUP-MANIFEST.json` 記錄原始 SHA-256。
- 已在舊審查報告頂端加日期更正，明確把匯入前段落標為歷史紀錄，並連結最新 `CH01-FINAL-ACCEPTANCE.md` 及 `IMPORT-AND-RIGHTS-RECORD.md`。沒有改動任何章稿、figure ID 或插圖；未改變 pending 權利／人工審查狀態。
- CH01 自動與出版技術檢查依前一輪實測：35/35 unittest PASS，V2／registry／站點同步 PASS，Astro diagnostics 0/0/0，網站 123 頁 PASS；既有 PDF／EPUB finalproof 有此前記錄的實測證據，本次沒有重建，避免把舊 proof 說成本次產物。
- CH01 仍不能宣稱「正式出版完成」：來源版本與 timecode、理論 locator、英文專業校稿、五圖 provenance／相似性／權利與作者核准需真人完成。尚未指定下一章號；待使用者指定後才開始下一章，避免自行選章。
- 未呼叫付費服務、未重生圖片、未發布網站、未 commit／push。


## 2026-10-18 — CH02 V4 chapter staging and validation

- 使用者選擇第 2 章作為下一個章節。依 `ai-video-bible-chapter-pipeline` Skill 與 V4 SOP，先盤點 V1、canonical V2、來源素材包及術語，再建立只新增、不覆蓋原稿的 staging 草稿。
- 已在變更前保存來源與 canonical 快照：`backups/CH02-pipeline-20261018-215634/`；完成收尾前再備份中文 staging、pipeline run 與 history 至 `backups/CH02-finalization-20261018/`。來源 ZIP CRC 通過，SHA-256 `d448defde21abe8802ad87684928eaade0f7c39101b423159073391457a519a5`。V1 章稿、V2 canonical 雙語 scaffold、來源 ZIP 均未覆蓋。
- 新增 `staging/CH02-V4/`：繁中章稿、英文編譯草稿、13 組穩定節點對照、26 組雙語術語、5 張原創可編輯 SVG、圖稿 manifest、對齊檔、暫存 bibliography、來源交叉表與檔案雜湊紀錄。所有文字保留 draft/review 狀態；SVG 權利及編輯審查仍 pending，提示詞未實際執行，也沒有呼叫付費圖像或影片服務。
- 文獻核對採限縮表述：Columbia Film Language Glossary 用於攝影機運動與 180 度軸線術語；American Cinematographer 文章支撐《大白鯊》dolly zoom 實務案例；ZEISS、Canon 技術資料支撐光學與景深相關說明；Runway Gen-4 文件僅當作特定版本供應商提示指南。繁中來源清單補列暫存來源 R025–R029。上述網頁查閱日 2026-10-18；教科書頁碼、電影版本及精確 timecode 仍待人工核實。
- 實測結果：40/40 unittest PASS；`v2_validate.py`、`validate_project.py`（12 篇、60 章、2 個 canonical 章稿、52 個舊術語、24 筆全書來源）、網站內容 sync check、Python compile 與 `git diff --check` PASS。Astro check 為 0 errors/warnings/hints，現有 canonical 網站 build 123 頁 PASS。這是網站基線 build；CH02 的 V4 staging 尚未投影到站點，故 CH02 路由仍 BLOCKED，未把 scaffold 網頁當成新章測試。
- 本環境目前 PowerShell PATH 找不到 Pandoc、XeLaTeX、pdffonts、EPUBCheck，故未產生或聲稱已驗證 CH02 DOCX/PDF/EPUB；PDF 字型嵌入、繁中實際渲染、EPUB 結構狀態均 BLOCKED，待裝妥工具後於新草稿輸出目錄重建及檢查。
- 驗收報告：`reports/CH02-V4-ACCEPTANCE-20261018.md`。Pipeline run 已記錄階段證據，run 狀態為 partial。未發布網站、未 commit/push GitHub，未修改 V1/V2 canonical 原稿或 TOC。第 2 章完成的是可供編輯審閱的雙語 staging 草稿與技術素材，不是正式出版定稿。

## 2026-10-18 — CH02 草稿出版輸出、EPUBCheck 修復與繁中字型校樣

- 前一筆記錄一度根據目前 shell 的 PATH 將書籍輸出判作 BLOCKED。後續定位到使用者帳號已安裝的 Pandoc 3.12.1、MiKTeX XeTeX 4.18 和 Inkscape；它們不在該 shell PATH，因此使用執行檔完整路徑／本次程序 PATH，不改永久系統 PATH。這次更正前述判斷。
- 於修改前建立 `backups/CH02-build-fixes-20261018/`，備份中英 stage 稿、`figure-captions.lua`、驗收報告、history 與 run.json，並記錄檔案雜湊。章稿新增 `lang`/`title` metadata；繁中稿將 Times New Roman 缺字的圈號 ①–⑥ 改為 (1)–(6)，中英文均將鏡頭清單改成「隨本章素材包附檔」描述，避免成品格式出現指向 repo 容器外的脆弱連結。
- 初次 PDF 命令把 XeLaTeX 完整路徑傳給 Pandoc 的 `--pdf-engine`，Pandoc 拒絕該參數；修正成允許值 `xelatex` 並於本次 PowerShell 程序 PATH 加入 MiKTeX 後，中英 PDF 編譯成功。第一次在無 Inkscape 轉換路徑時，DOCX/EPUB 對 SVG 發出無法轉換警告；後續以 Inkscape 將原 SVG 轉成 PNG 供 `tmp/CH02-V4-draft-20261018/` 草稿出版使用，原 SVG 保留可編輯、未替換。
- PDF 校樣發現 Pandoc Babel 標籤在繁中輸出為簡體「图」，原 filter 的 `tostring(doc.meta.lang)` 沒有讀到 Pandoc MetaInline 語言值。修正 `scripts/publishing/figure-captions.lua`：用 `pandoc.utils.stringify` 讀取語言，將 `\\captionsetup[figure]{name=圖}` 加入 LaTeX header。重新編譯並抽取 PDF 文字，確認 5 個圖說都以繁體「圖」起始；含圖頁的聯校圖重新渲染抽看。
- EPUBCheck 初次實測指出兩項真問題：缺少 `dc:title`，以及繁中稿素材 JSON 外部相對 URL 逃出 EPUB 容器。加入 locale-specific `title` metadata、將素材 JSON 改述為本章素材包附檔後重建。官方 EPUBCheck v5.4.0 發行 ZIP SHA-256 `33350c61038e71dfb3d45a76aed04bf5481e6d5500cb780f6e98db8bbd15a28c`，只暫存於 gitignored `tmp/epubcheck-5.4.0/`；中英文各 0 errors / warnings / informational / references。
- 最新草稿輸出在 gitignored `tmp/CH02-V4-draft-20261018/`：中英 DOCX 各含 5 張內嵌 PNG 圖；PDF 分別 20、16 頁，繁中 Microsoft JhengHei、英文 Times New Roman 字型全部實際嵌入，5 張圖與圖說同頁，PyMuPDF 抽取沒有 replacement character；EPUB 各含 5 張 media 圖，ZIP CRC 與 XML 解析通過。Pandoc 仍對 zh-TW 提示 `translations/zh.yaml`／Abstract/Table/Figure 翻譯字串不足；圖說標籤已由 filter 校正，其他通用詞彙待樣式審查。
- 驗收報告 `reports/CH02-V4-ACCEPTANCE-20261018.md` 已更正為 DOCX/PDF/EPUB draft build PASS，網站章節路由仍因未經編輯整合而 BLOCKED。網站基線 Astro check 0 errors/warnings/hints、build 123 頁；不能當成本章 route 驗收。
- 最後回歸測試：40/40 unittest PASS；`v2_validate.py`、`validate_project.py`、`sync_site_content.py --check`、Python compile、`git diff --check` 均通過。正式來源定位、英譯與術語專業校稿、影片 timecode、圖稿審閱、標題確認與作者核准仍待人工。沒有發布、commit 或 push。

- 最終中英文 DOCX/PDF/EPUB 草稿與含圖頁聯校圖另複製到 gitignored 的 `dist/drafts/CH02-V4-20261018/`，含 README 說明供本機編輯檢閱。`tmp/` 保留建置過程、PNG 衍生檔和 EPUBCheck 工具；V4 原始 SVG 與可編輯章稿仍在 staging。此處未將任何產物 commit 或 push。

## 2026-10-18 — 強制每章交付前完成全項目稽核

- 使用者要求每完成一章，必須重新檢核本章所有應完成事項，再回報並等待下一章指示。流程解讀為：各項要有單獨狀態及證據；未完成的人工核准仍如實標示，不阻止交付草稿，但不得稱為正式出版完成；每章報告交付後停止，不在同一輪自動開始下一章。
- 修改前備份專案 SOP、Skill、驗收模板、CH02 報告、pipeline runner、測試與 history 至 `backups/CH02-post-chapter-audit-20261018-222009/`；`BACKUP-MANIFEST.json` 保存備份檔 SHA-256。
- 更新 `AI-VIDEO-BIBLE-SOP-V4.md`、`.codex/skills/ai-video-bible-chapter-pipeline/SKILL.md` 和 Skill acceptance report template，加入完整章末稽核步驟及內容、雙語、研究、案例、資產權利、網站、DOCX/PDF/字型、EPUB、連結、測試、registry、run/history/backup、作者核准等逐項表格。明訂每列必須記錄 PASS／FAIL／BLOCKED／NEEDS HUMAN REVIEW／NOT RUN 和證據，稽核交付後等使用者指定下一章。
- 更新 `scripts/chapter_pipeline.py`：新增 `chapter-audit` stage，run 不得在 audit 未標 PASS 時 finish；測試 `tests/test_chapter_pipeline.py` 加入強制 audit 的驗證，避免只靠文件提醒。首次回寫既有 CH02 run 時，舊 checkpoint 尚無新 stage，runner 拒絕未知 stage；已調整成只允許目前定義的 `STEP_IDS`，並可將新增 stage 寫入舊 run，再成功記錄 audit 和 partial finish。
- 對 CH02 已有報告套用全項目檢核，新增 32 列逐項稽核：PASS 18、FAIL 0、BLOCKED 1、NEEDS HUMAN REVIEW 12、NOT RUN 1。章稿及雙語草稿、圖稿和 DOCX/PDF/EPUB 草稿已完成；CH02 網站路由未整合故 BLOCKED，連結檢查未執行，英譯／來源／電影版本／圖稿權利等仍待人工。正式出版標準仍未達成。
- 既有 CH02 run 保持 `partial`，並在完成章末報告後新增 `chapter-audit=pass`（表示稽核程序已完整執行，非每一列均 PASS）；人工作業與網站整合仍保持其原狀，不能把章節標為出版完成。
- 驗證結果：`python -m unittest discover -s tests -v` 40/40 PASS；`python scripts/v2_validate.py` PASS；`python scripts/validate_project.py` PASS（12 篇、60 章 registry）；`python scripts/publishing/sync_site_content.py --check` PASS；`python -m compileall -q scripts tests` PASS；`git diff --check` exit 0（只回報既有工作樹檔案 LF→CRLF 提示）。沒有修改章稿或原素材，沒有發布／commit／push，沒有啟動 CH03。

## 2026-10-19 — V2 電影知識體系增量整合（Cinetic／TTS 排除）

- 使用者要求在既有 AI Video Bible V2 repo 中整合十二大電影核心元素、八大 AI 製作系統、60 章矩陣、電影品質 Rubric、章節模板入口及遷移計畫；明確指示 Cinetic 和 TTS 不整合。既有任務規則要求保護 CH01–CH03、避免重寫及保留未提交工作。
- 確認工作區位於 `D:\我的雲端硬碟\google drive\000000000backup\00000黑熊講師\00000著作\AI_Video_Bible`；HEAD `6481fd3`、branch `main`，盤點時與 `origin/main` 相同。工作樹已有大量未提交內容（初始約 18 個 tracked modifications、547 個 untracked paths），包含 CH01/CH02 稿件、assets、staging、pipeline 和出版產物。此輪沒有清理、重設、提交、推送或部署。
- 改檔前將 `README.md`、`CHANGELOG.md`、`history.md` 複製至 `backups/V2-knowledge-integration-20261019-223343/`；另 snapshot `metadata/chapters.yaml`，對前三個文件寫出 SHA-256。
- 新增 `FILM_ELEMENTS.md`：定義 FE01–FE12 的概念、雙語術語、原理／技法、適用類型、專業電影案例來源入口、AI 實務、常見錯誤、品質標準和相依關係。既有 R013–R024 及已讀 BFI／Criterion 等案例來源作入口；新引用明確留待登錄和逐鏡 locator 審查。沒有把評論性來源冒充原始製作紀錄。
- 新增 `AI_PRODUCTION_SYSTEMS.md`：定義 AIS01–AIS08 的職責、輸入／輸出、資料格式、工具類型、Codex／Claude Code 角色、人工審查、自動測試及系統交接。依作者指示將 Cinetic 和 TTS 標為排除，不評估、不安裝、不整合。Remotion、Manim、Blender Python/MCP、ComfyUI 僅作官方文件導向的可行性候選，未安裝、未連線、未呼叫模型或付費 API；Blender MCP 額外標示其 code execution 風險與隔離前置條件。
- 新增 `CHAPTER_INTEGRATION_MATRIX.md`，按 `metadata/chapters.yaml` 的穩定 ID 生成 60 列，將元素／系統標籤與可讀證據分開。CH01、CH02 僅列 `PARTIAL` 並保留各自 acceptance 限制；CH03 是 scaffold、標 `MISSING / NOT RUN`；CH04–CH60 未按標題推論已有正文，列 `MISSING / NOT RUN`。矩陣映射為規劃而非正式的全內容稽核。
- 新增 `FILM_QUALITY_RUBRIC.md`：採用使用者指定權重，定義 0–10 人類評審錨點、加權公式、機器可測條件、不可自動替代事項及 publication gates。
- 新增 `CHAPTER_TEMPLATE_V2.md` 作穩定導覽入口，保留 `templates/chapter-v2.md` 為唯一 canonical 正文模板；新增 `MIGRATION_PLAN_V2.md` 記錄保護範圍、第一至第三章的低風險補強計畫及工具評估順序。
- 新增 `reports/PROJECT-STATUS-V2-20261019.md`，記錄 repo/章節盤點、來源狀態、AI 工具整合狀態、測試與未完成項；在 `README.md` 增加導覽，在 `CHANGELOG.md` 加入 Unreleased 記錄。
- 外部來源檢視日期 2026-10-19。候選工具依據官方文件：[Remotion render](https://www.remotion.dev/docs/render)、[Remotion parameterized rendering](https://www.remotion.dev/docs/parameterized-rendering)、[Manim quickstart](https://docs.manim.community/en/stable/tutorials/quickstart.html)、[Blender Python API](https://docs.blender.org/api/blender_python_api/)、[Blender Lab MCP](https://www.blender.org/lab/mcp-server/)、[ComfyUI](https://github.com/Comfy-Org/ComfyUI) 與 [ComfyUI API example](https://github.com/Comfy-Org/ComfyUI/blob/master/script_examples/basic_api_example.py)。電影案例來源入口含 [BFI 12 Angry Men](https://www.bfi.org.uk/features/how-12-angry-men-works-25-frames)、[BFI Hamlet editing](https://www.bfi.org.uk/features/tales-film-editor-making-olivier-hamlet)、[BFI Faces](https://www.bfi.org.uk/features/john-cassavetes-faces-indie-filmmaking)、[ASC The Taste of Things](https://theasc.com/article/the-taste-of-things-color/)、[BFI Asteroid City production design](https://www.bfi.org.uk/sight-and-sound/features/pictures-how-west-was-done-wes-anderson-asteroid-citys-production-design)、[Academy Jurassic Park](https://www.oscars.org/events/jurassic-park)。以上新增書目仍須正式入庫、保存存取日與文章 locator 後才可視為章稿正式引用。
- 實際測試：`python scripts/v2_validate.py` PASS；`python -m unittest discover -s tests -v` 40/40 PASS；臨時 Python 檢查確認矩陣 60 列且順序等於 registry；`git diff --check` exit 0，僅列出既有 LF→CRLF working-copy 提示。沒有跑網站／PDF／EPUB build，因本輪未改出版程式、模板或章稿；驗收報告標註 NOT RUN。測試總結果也寫入 `reports/PROJECT-STATUS-V2-20261019.md`。
- CH01、CH02、CH03 原稿、V1 原稿、圖片、manifest、staging、chapter registry、出版輸出、pipeline 程式均未改；未改全書 TOC 或章節順序。沒有發布網站、沒有 commit、沒有 push。
- 下一步：研究編輯檢查新增案例來源和 locator；章節編輯核准 element/system mapping；由使用者指定後再按 CH01/CH02 acceptance 缺口做人審和非破壞補強；CH03 在另行 brief 後才規劃開稿；候選工具先做隔離 prototype，Cinetic/TTS 維持排除。
- 驗收報告測試表補記：`python scripts/validate/check_links.py` 本輪實際結果為 0 failures、0 network checked、5 not conclusively checked；此結果只表示無本地檢查失敗，不能當作新案例來源已通過外網／內容查證。網站、PDF、EPUB build 仍 NOT RUN。
- 追加執行 `python scripts/validate_project.py`，結果 PASS（12 parts、60 planned chapters、2 canonical chapter files、52 terms、24 references），並以臨時檔案檢查確認六份核心文件及 Cinetic／TTS 排除聲明存在。期間一個一次性文件檢查的輔助斷言把排除字串的預期寫反而失敗；檢視後修正該檢查條件並重跑 PASS，沒有修改任何專案內容或影響正式測試。


## 2026-10-19 — CH02 逐項審稿與安全整合

- 使用者要求開始 CH02 逐項審稿與安全整合。依 `ai-video-bible-chapter-pipeline` 技能，先核查 CH02 V1、V2 canonical scaffold、staging V4、術語／來源／圖稿資料及 repo 狀態；沒有清理既有 dirty worktree，也沒有 commit/push/deploy。
- 建立 pipeline checkpoint：`production/runs/CH02/20261019T225451+0800-a105b6d9/`。整合前備份 11 個已存在目標檔與 SHA-256 manifest：`backups/CH02-safe-integration-20261019-225715/`；測試與 Lua filter 修改前另存於同一備份資料夾。中途試插入重複圖版的 canonical 草稿另存為 `*-integrated-duplicate-backup.md`，隨後以 staging 原稿重建 canonical，確保每張圖只出現一次。
- 來源基準：V1 `chapters/01-02-camera-language.md` SHA-256 `a669651d795bba3e02933f1771a1ee5b53855daebb11fa2452850c38363138af`；來源 ZIP SHA-256 `d448defde21abe8802ad87684928eaade0f7c39101b423159073391457a519a5`，CRC 通過。兩語 staging 原稿與五張 SVG 保持原樣；第一、三章未修改。
- 安全整合繁中與英文草稿到 `content/zh-TW/chapters/CH02-camera-language.md`、`content/en-US/chapters/CH02-camera-language.md`，狀態設為 `draft-migration-pending`／`review-needed`，未設 `approved`。合併 26 個雙語 TERM-CH02 詞條與來源 R025–R029；建立 `metadata/translations/CH02-alignment.yaml` 保留 13 個 section、26 個 term、5 個 figure pair 對照。全域英文正式標題欄仍留空待編輯確認。
- 五張 hand-authored SVG 從 staging 位元複製至 `assets/chapters/CH02/figures/originals/`，不變更原圖；建立 CH02-FIG-001–005、顯示圖號 2-1A–2-1E，更新雙語圖說與 alt，並納入 per-chapter 及全域 figure manifest。所有圖稿保持 `draft-original-svg`、權利／技術／編輯 review `pending`、`pending-publication-approval`；individual SVG creator 尚未記名，須人工補登。
- 首輪整合同步發現 staging 文字本來已有五個 SVG 引用；第一次插入流程重複加圖，且舊 CH02 測試仍要求 canonical scaffold 雜湊不變。已由原 staging 文本重新建置 canonical、只替換圖片路徑和對應圖號／圖說，並將測試改為驗證來源 ZIP/V1 不變而 canonical 為未核准遷移草稿。第二次整體測試 40/40 PASS。
- 初次 Astro check 在同步前看到兩語舊生成投影 duplicate-ID 警告；執行 `sync_site_content.py` 之後再 check 為 0 errors、warnings、hints。中英 Astro build 共產生 123 頁，CH02 雙語 route 各含 5 張 canonical 圖及非空 alt。沒有部署。
- 第一輪 Pandoc 單章草稿試建時：繁中 DOCX/EPUB 成功；PDF 使用 Noto Serif TC 遇到 MiKTeX `dvipdfmx:fatal: Invalid font: -1 (1)`，並有字型缺字訊息。改用 Microsoft JhengHei（繁中）與 Times New Roman（英文字型；中英均另設 CJK fallback）後 PDF 編譯及 `pdffonts` strict 驗證通過。輸出頁數繁中 20、英文 16，所有列出字型均有嵌入。PyMuPDF 抽取未含 U+FFFD；五個圖號存在。檢視含圖校樣，正文與圖稿可讀，無明顯截切。
- 最初 PDF filter 對英文圖說未移除手動顯示圖號，造成 `Figure 2-1B: 2-1B | ...` 重複；已備份並修改 `scripts/publishing/figure-captions.lua`，增加 CH02 圖號映射及分隔符清除。以 `captionfix.pdf` 重新建置，抽文字確認重複消失。DOCX/EPUB caption 在目標閱讀格式不重複。
- 第一輪 Python 捕捉 XeLaTeX log 曾受 Windows cp950 解碼失敗中斷；改用 `encoding=utf-8, errors=replace` 捕捉輸出再建置。英文稿第一次單章建置也因前一個中斷而未建立臨時 source markdown，已生成該臨時檔後重跑成功。這些均為建置器／臨時腳本流程問題，不影響 V1、staging 或 canonical source 完整性。
- 最終草稿輸出位於 gitignored `tmp/CH02-draft-integration-20261019-r1/`：中英 DOCX 各含五張圖、ZIP CRC 通過；中英 EPUB 各含五張 media，EPUBCheck 5.4.0 exit 0；中英 PDF 以 captionfix 版本交付。Pandoc 3.12.1，MiKTeX-XeTeX 4.18 (MiKTeX 26.5)，Node 24.15.0，npm 11.12.1，EPUBCheck 5.4.0。生成檔 SHA-256 列在該資料夾 `OUTPUT-MANIFEST.json`。
- 最終驗證：`python scripts/v2_validate.py` PASS；`python scripts/validate_project.py` PASS（12 part、60 chapter、2 complete canonical drafts）；`python scripts/publishing/sync_site_content.py --check` PASS；`python -m unittest discover -s tests -v` 40/40 PASS；`python scripts/validate/check_links.py` 0 failures、0 network checked、5 not conclusively checked；`git diff --check` exit 0（只有既有 LF/CRLF working-copy 提示）；客製 CH02 完整性檢查確認 15 個引用 ID 均已註冊、雙語圖稿各 5 張、全域 10 個 figure IDs 唯一、V1/ZIP hash 不變。
- 圖片政策閘門刻意維持 BLOCKED：CH02 五張 SVG 尚未人工核准，且全站 CH01 圖片仍有 pending 權利／技術審查。全書 `build_books.py` 需全 60 章雙語 approved，故沒有嘗試繞過正式出版閘門；這輪只產生單章 gitignored 預覽。未發布網站、未 commit、未 push GitHub。
- 驗收文件：`reports/CH02-FINAL-ACCEPTANCE.md`；舊報告 `reports/CH02-V4-ACCEPTANCE-20261018.md` 保留供歷史參考，不視為目前整合狀態。結論：本輪安全整合及自動出版測試完成，但因英文校譯、理論／來源 locator、合法 film edition/timecode、術語與 SVG 專業／權利審查及作者核准未完成，CH02 尚未達正式出版標準。
- 下一步先由作者／雙語與攝影專業編輯按新驗收報告完成 NEEDS HUMAN REVIEW 項目，補錄 SVG creator 及電影片段版本/timecode；回填簽核後再跑正式圖像及章稿出版門檻。CH03 不在本輪修改範圍。
## 2026-10-20 — CH03《景別、視點與觀看位置》雙語草稿製作與出版預檢

- 使用者要求依前述進度接續 CH03，並沿用「每章完成後逐項檢核；全書完成後集中人工簽核」流程。盤點時 CH02 驗收文件仍是 `review-needed`，未有簽核證據；依使用者本次明確將 CH03 指定為下一步，僅在此工作順序上開始 CH03，沒有把 CH02 或 CH03 標為核准。
- 讀取 `AGENTS.md`、V4 Skill、`CHAPTER-PIPELINE-README.md`、V4 SOP、章節 registry、CH03 雙語 scaffold、素材目錄、術語／引用／圖片 registry、章節矩陣及報告。CH03 原有雙語文件只有空白模板；未找到 CH03 staging 包或章節素材 ZIP。CH01、CH02、V1 原稿及其他章節均不在本輪正文修改範圍。
- 建立 pipeline run `production/runs/CH03/20261020T060229+0800-cc9a6553/`。起始備份 `backups/CH03-start-20261020-060306/` 保存 10 個原始檔案的位元組數及 SHA-256；修改 Pandoc 圖說 filter 前另備份至 `backups/CH03-caption-filter-20261020-061102/`。未刪除、移動或覆蓋舊素材。
- 研究方面，2026-10-20 直接查讀 Oklahoma State University 開放教材 *Introduction to Film & TV* 的 Cinematography「Framing」「Types of Framing」及 Narrative「Point of View」章節，作為 R022 locator；查讀 Columbia Film Language Glossary 的 “Point of View” 詞條，新增 R030。引用只涵蓋可見頁面支持範圍；沒有虛構發行版、頁碼或片段 timecode。電影索引不等於作者已看片，明確保留此限制。
- 將 CH03 中英文稿從 scaffold 擴寫為研究草稿：錨點 CH03-S00–S14 配對；增加八組雙語術語、敘事及製作原理、傳統方法、AI 能力限制、步驟流程、模型中立 shot-spec YAML、電影案例入口、錯誤／驗收、練習與評量。英文只作對照譯稿，未人工批准。
- 新增 `TERM-CH03-*` 八項，全數 `draft`；新增 `metadata/translations/CH03-alignment.yaml`。將章節 registry／translation status 更新為 review-needed，暫定英文標題寫入 registry；章節矩陣 CH03 列改為 PARTIAL。新增並登錄兩張自行編寫 SVG：CH03-FIG-001（3-1）與 CH03-FIG-002（3-2），包含雙語圖說、alt、hash、source/method/creator/rights 欄位。個別創作者未記名，兩圖 rights、technical、editorial 均 pending。沒有呼叫付費生圖服務或使用網路圖片。
- 更新 R022 的直接存取日和章節 locator，於 `data/references.yaml` 與 `metadata/references.bib` 同步；新增 Columbia R030 到兩份來源 registry。來源用於正文引文，沒有將引用 registry 書目數字誤當成全域 V2 數字。
- 產出本機草稿 DOCX、PDF、EPUB 各兩語於 gitignored `tmp/CH03-draft-20261020/`，沒有輸出正式書籍。Pandoc 初次在 Unicode repo 工作目錄遇到 Windows console `hPutChar` 編碼問題；從 ASCII 工作目錄設 `LANG=C.UTF-8`／`LC_ALL=C.UTF-8` 後成功。Pandoc 沒有 `rsvg-convert`，故用 Inkscape 1.4.4 將原始 SVG 輸出 1600px PNG 作為排版衍生檔；原 SVG 未變更。PDF 抽頁發現重複圖號，先備份後在 `scripts/publishing/figure-captions.lua` 增加 CH03-FIG-001/002 的 3-1/3-2 mapping，再建置和抽文確認修復。
- 出版證據：中英 DOCX ZIP CRC 完整、各含 2 張 media；中英 EPUB 各含 2 張 media 與 figure IDs，EPUBCheck 5.4.0 均為 0 errors／warnings／informationals／references。中英 PDF 以 XeLaTeX/MiKTeX 26.5 建置；strict `check_fonts.py --require-pdffonts --font "Microsoft JhengHei"` 均通過，四種嵌入字型列皆 `emb=yes`；抽取文字無已知替代字元，PDF 第 1 頁及含圖第 7 頁已檢視。Pandoc 繁中 Table/Abstract/Figure 字串仍有 localization warnings，列待處理。
- 自動驗證：`python scripts/v2_validate.py` PASS；`python scripts/validate_project.py` PASS；`python scripts/publishing/sync_site_content.py --check` PASS；Astro check 0 errors／warnings／hints；`npm --prefix apps/web run build` 123 頁 PASS；`python -m unittest discover -s tests -v` 40/40 PASS；`python scripts/validate/check_links.py` 0 failures、0 network checked、5 inconclusive；`git diff --check` exit 0，僅有既有 LF/CRLF 工作副本提醒。CH03 專項檢查確認兩語錨點、八術語、兩圖 IDs、manifest hash、非空 alt、pending 權利狀態及中英網站／EPUB 圖數一致。
- 驗收文件 `reports/CH03-FINAL-ACCEPTANCE.md` 列出逐項 PASS、BLOCKED、NEEDS HUMAN REVIEW 及證據。未解項目包括英文專業校譯、攝影與電影理論審查、教材採用版本／頁碼、合法電影版本及 timecode、SVG 個人創作者歸屬／權利／技術／可及性終審、全書作者核准。依使用者要求，這些人工審核統一留到全書完稿後，不影響按章草稿製作，但 CH03 不可標 approved/publication-ready。
- 本輪未發布網站、未 commit、未 push GitHub。下一步：停止 CH03 工作，等待使用者明確指定下一章；全書完成後整合集中人工審核清單。

- CH03 packaging follow-up: created `tmp/CH03-draft-20261020/CH03-Codex-Materials-DRAFT.zip` and then a non-overwriting `-r2` archive after the acceptance report was amended; both are retained and the output manifest records hashes. Updated the CH03 matrix from pending to automated draft checks passed. Material pack remains explicitly draft and unapproved.

## 2026-10-20 — CH04《電影形式、風格與作者性》雙語草稿與章末完整驗收

- 使用者指定 `ch04`；依 `ai-video-bible-chapter-pipeline` Skill、`CHAPTER-PIPELINE-README.md`、`AI-VIDEO-BIBLE-SOP-V4.md` 與 acceptance template 執行。當前 Windows 工作目錄不是儲存庫，先定位到既有 repo `D:\我的雲端硬碟\google drive\000000000backup\00000黑熊講師\00000著作\AI_Video_Bible`；未另建專案。Git branch 為 `main`，原本有多項未提交變更；只在既有章節與相依 registry 範圍內工作，沒有 commit/push。
- CH04 開始前 registry 顯示中文題名《電影形式、風格與作者性》、英文未定；canonical zh/en 檔及圖 manifest 是 scaffold。以 pipeline run `production/runs/CH04/20261020T203111+0800-3d34a58e/` 建立 checkpoint，備份 12 個修改目標的舊檔並記錄 SHA-256 至 `backup/MANIFEST.json`；其中原中英 scaffold hash 分別為 `70c3f451bf6fac08beaf6aba373f9331ee86b8b8cc67cf07567b17b107f0fc3f`、`16455ddee4fb802765fab4bded30df2ad2154d2dced5a4e1a540d42f75f9b863`，空 manifest 為 `28fb624839293eabccd4c60a2579fa00f86d11a49c2f6ce78aea91eb0e17e91b`。
- 以 CH04-S00–S13 建立繁中研究草稿及英文對照稿，含 14 個穩定節次、學習目標、先備知識、8 個雙語術語、電影形式／作者論／集體作者性理論脈絡、傳統製作方法、AI 流程與限制、逐步工作流、示範 prompt、電影案例入口、錯誤與品質檢查、練習評量及延伸研究。英文題名暫定為 *Film Form, Style, and Authorship*，兩語均維持 `review-needed`，對齊檔 `metadata/translations/CH04-alignment.yaml` 明列待人工校譯。
- 新增 R031–R038 書目／來源項：McGraw Hill *Film Art* 第 13 版（出版者頁面）、Cinémathèque française Truffaut 回顧、Andrew Sarris 原文掃描、Pauline Kael 期刊紀錄、Oxford Academic 的 Gaut／Sellors 章節或摘要、BFI *Vertigo* 教育案例頁及 Runway Gen-4 官方提示指南。來源檔標明查閱日、版本、locator 與摘要／全文限制；沒有虛構觀片內容、發行版本或 timecode。理論來源全文和頁碼、電影案例看片仍待集中人工審稿。
- 新增並登錄兩張手寫、可編輯 SVG：CH04-FIG-001（圖 4-1，作者性證據線）與 CH04-FIG-002（圖 4-2，風格規格循環）。更新章稿、章節 manifest、全域 figure registry、資產表、圖說 Lua filter；兩圖均有中英圖說、alt、製作法、hash、source links、權利／技術／編輯狀態，均 pending。沒有網路抓圖、付費生圖或將圖標為 approved。
- 初次 `test_ch04_content` 暴露 `figure-manifest.yaml` 中重複的 `research_sources` key、圖說欄位缺失及測試狀態字串不吻合；初次專案驗證另指出 `data/assets.yaml` 的引用來源格式不符 schema、缺 `production_log` 及雙語 caption。已修正資料結構、補雙語 alt/caption/source locator/production log、移除重複 manifest/source key 並修正測試；之後 CH04 專項測試 4/4 PASS、整合 validators PASS。
- 首次完整 unittest 在網站 canonical source 尚未投影時有 1 項 stale projection 失敗；執行 `sync_site_content.py` 更新兩語 CH04 頁及四個本地 SVG 圖檔後，網站 sync check 與全套測試通過。一次並行啟動的 Astro check 在 loader 輸出 duplicate-ID warning；等待並行程序結束後單獨重跑 `npm --prefix apps/web run check`，結果 0 errors／warnings／hints，後續 Astro build 也無 duplicate warning，產出 123 頁。另以 HTML parser 核對中英 CH04 路由各有唯一 CH04-FIG-001/002、兩張可載入圖片及非空 alt。
- 本環境的 shell PATH 沒有 Pandoc、XeLaTeX、pdffonts、Inkscape、Java/EPUBCheck 命令；依 history 先前已安裝紀錄定位已存在的使用者本機工具完整路徑，不改永久 PATH、不下載工具。Pandoc 3.12.1、Inkscape 1.4.4、MiKTeX XeLaTeX、Poppler、Java 18 及 repo 暫存 EPUBCheck 5.4.0 均成功用於本機草稿建置。排版用 PNG 由 Inkscape 1600px 輸出到新 gitignored `tmp/CH04-draft-20261020-r1/`，SVG 母檔未改。
- 中英 DOCX、PDF、EPUB 各 1 份：DOCX ZIP CRC 完整，各嵌入 2 圖；繁中 PDF 10 頁、英文 12 頁，字型 checker strict 模式通過，繁中 Microsoft JhengHei、英文字型 Times New Roman 及混排 CJK 均實際嵌入；PDF 抽字無 U+FFFD，已檢視繁中第 7 頁和英文第 9 頁的圖文排版。EPUBCheck 5.4.0 中英文各 0 errors／warnings／informationals／references，檔案 ZIP CRC 完整、各有 2 張圖與圖號；Pandoc 仍提示繁中 `zh.yaml`、Abstract、Table、Figure 通用翻譯字串不足，記入驗收報告。
- 完成 `reports/CH04-FINAL-ACCEPTANCE.md`，逐列填妥 32 項章末核對：PASS 16、NEEDS HUMAN REVIEW 16、FAIL/BLOCKED/NOT RUN 為 0（草稿內容完整性／出版可重現檢查，不代表專業或作者核准）。`python scripts/validate/check_links.py` 結果為 0 failures、0 network checked、5 inconclusive；不把未確認連結說成失效或已成功。
- 產出 `OUTPUT-MANIFEST.json`，並建立 non-overwriting `CH04-Codex-Materials-DRAFT-r2.zip`（18 個成員，ZIP CRC 通過，SHA-256 `d347a28da6a50635f5550c8619a6df5af3122bed2e371d923450d846755c86a2`）。較早的 r1 包亦保留在同 gitignored temp 目錄，r2 含修正後報告。CH04 整合矩陣更新為自動草稿／技術檢核通過，知識涵蓋仍標 PARTIAL。
- 最終測試：`python scripts/v2_validate.py` PASS；`python scripts/validate_project.py` PASS（12 parts、60 planned chapters、2 canonical chapter files、52 terms、33 references）；`python -m unittest discover -s tests -v` 44/44 PASS；`sync_site_content.py --check` PASS；Astro check 0/0/0；Astro build 123 頁 PASS；`git diff --check` exit 0（僅保留既有 LF/CRLF conversion warnings）。
- 尚待人工：英文編輯及標題核定；電影理論原文／學術全文及頁碼定位；合法 *Vertigo* 版次、實際片段與 timecode 或撤換觀片主張；兩 SVG 個人繪圖者署名、權利、相似性、無障礙和印刷終審；作者簽核。依使用者「全書完成後再做人工審核」的決定，維持 review-needed/pending，將其納入全書集中簽核，不阻止本章草稿交付。
- 沒有覆蓋 V1/CH01–CH03 或其他素材、沒有發布網站、沒有 Git commit/push。CH04 完成本輪草稿和章末檢核後停止；下一章須使用者另行指定。
- CH04 視覺校樣補充：在 PDF 文字抽查後，另以 Poppler/MuPDF 將繁中第 7、8 頁與英文第 9、11 頁渲染成 PNG，逐頁目視確認圖 4-1／4-2 和雙語圖說均在版面內；沒有發現裁切。將驗收報告的抽查頁碼更新，並將新頁面影像和四個 Inkscape PNG 排版衍生檔加進 `OUTPUT-MANIFEST.json` 雜湊清單。
- 為使壓縮素材包內也包含更新後頁碼的驗收報告，另建不覆蓋的 `CH04-Codex-Materials-DRAFT-r3.zip`（18 個 members、ZIP CRC PASS、SHA-256 `b103ea811dba2fbfff4da1ab15a4ffdc46466144108ece59278cfaef4bc002fa`）；r1、r2 仍保留於同一個 gitignored 草稿目錄以供追溯。`OUTPUT-MANIFEST.json` 現列 16 個媒體／文件輸出項及 r3 包 hash。

- CH04 backup/packaging follow-up: final diff audit found scripts/publishing/figure-captions.lua had only the two new CH04 mapping additions, but the initial run manifest omitted that file. Reconstructed the exact pre-CH04 tracked bytes from git show HEAD, verified the LF/CRLF-normalized file equals the current filter after removing those two additions, and stored the baseline under production/runs/CH04/20261020T203111+0800-3d34a58e/backup/pre-edit/; SHA-256 cf55a73b45d72ed4a61f70ef9435f7ae7ceb36a329f20faef7c384b192f505ff. Updated report and backup manifest to include it; generated non-overwriting CH04-Codex-Materials-DRAFT-r4.zip with updated report (18 members, CRC PASS). r1–r3 remain intact in the ignored draft directory.

## 2026-10-20 — CH05《類型、再現與影視倫理》雙語草稿與出版預檢

- 使用者輸入 `ch05`。依 `.codex/skills/ai-video-bible-chapter-pipeline/SKILL.md`、V4 SOP 和 acceptance template 開始單章工作；repo 為 `D:\我的雲端硬碟\google drive\000000000backup\00000黑熊講師\00000著作\AI_Video_Bible`。CH05 registry 原狀為中文題名《類型、再現與影視倫理》、英文題名空白，雙語 canonical 僅 scaffold，章圖 manifest 空白；未找到 CH05 staging/source ZIP。開始前存在未提交 CH04 工作；本輪保留，不 reset/clean/stage/commit/push/deploy。建立 run `production/runs/CH05/20261020T225328+0800-59388910/`。
- 編輯前建立 `backups/CH05-start-20261020-225446/` 保存 CH05 及必要全域索引原內容，hash 見 run `backup-sha256.txt`。初次漏列共用 Lua 圖說 filter；事後將不含 CH05 mapping 的前編輯快照保存至 `backup/pre-edit/scripts/publishing/figure-captions.lua`，並記錄 hash。快照保留既有 CH04 mapping，與現行檔僅差 CH05-FIG-001/002 的 5-1/5-2 兩行。CH01–CH04 內容未由本輪改寫。
- 網路查證日 2026-10-20：JSTOR R039 核對 Altman 論文書目與摘要（全文論證定位待核）；SAGE R040 核對 Hall 編著書資訊（章節頁碼待核）；BFI R041 多元標準頁、R043 再現教學頁；UNESCO R042 2021 AI 倫理建議；BFI R044 片目核實 *Get Out*（2017）片名／年份，沒有看片、不宣稱鏡頭細節或時間碼。電影案例只作合法版次觀片待辦。來源 ID 加入 `data/references.yaml`、`metadata/references.bib` 及雙語稿。
- 建立繁中研究主稿與英文對照譯稿，各 13 節穩定 IDs；8 個雙語術語；英文題名暫定 *Genre, Representation, and Screen Ethics*。建立 `metadata/translations/CH05-alignment.yaml`。兩語 metadata 維持 `review-needed`。內容包含類型語義／句法、Hall 再現理論、傳統製作倫理、AI 限制與工作流、模型中立示範 prompt、案例入口、品質檢查、練習及延伸研究。
- 原創繪製 CH05-FIG-001/002 兩張 SVG（類型關係圖、再現倫理檢核圖），各 1200×420，記錄 SHA-256、方法、製作日期、雙語 caption/alt；更新章節 manifest、全域 figure registry、data assets 及 `assets/chapters/CH05/figure-captions.md`。所有圖權利、作者署名、技術／可及性／出版狀態 pending。未下載網路圖片、未用付費生圖、未使用電影劇照。
- 初次網站同步因圖片路徑多退一層而安全拒絕 project-root escape；修正路徑後通過。資料驗證接續指出 BibTeX 漏 R039–R042、asset schema 欠 permission/attribution/source_ids；補齊後 validators 通過。Astro check 曾在首輪載入輸出 duplicate-ID warning 但 diagnostics 為 0；最後重跑 check 無警告，build 也無該警告，產生 123 頁。雙語 CH05 route 各 40 個唯一 IDs、2 張本地圖與非空 alt。
- 草稿輸出位於 gitignored `tmp/CH05-draft-20261020-r1/`。Inkscape 1.4.4 將 SVG 轉排版 PNG 衍生檔，母檔不變。Pandoc 3.12.1 中英 DOCX/EPUB 成功；XeLaTeX 首次因未在 PATH 找到而失敗，改用 MiKTeX 絕對引擎路徑後中英 PDF 成功。Pandoc 繁中仍有 zh.yaml、Abstract、Table、Figure 通用字串翻譯警告，留在 log。EPUBCheck 5.4.0 中英皆 0 errors/warnings/informationals/references；DOCX ZIP CRC PASS 且各含 2 張圖；EPUB 各含 2 張圖。PyMuPDF 1.28.0 抽取兩 PDF 的字型 streams 均非空（Microsoft JhengHei、Times New Roman/CJK fallback），抽字 0 U+FFFD，圖文頁渲染並目視檢查。此環境無 `pdffonts`；strict helper 的獨立執行被阻擋，未冒稱該工具通過。
- 最終檢查：CH05 專項 3/3 PASS；完整 unittest 47/47 PASS；`scripts/v2_validate.py` PASS；`scripts/validate_project.py` PASS（12 parts、60 chapters、52 terms、39 references）；網站 sync check PASS；Astro check 0 errors/warnings/hints；Astro build 123 pages PASS；本地雙語路由／唯一 IDs／alt PASS；EPUBCheck、DOCX CRC/media PASS；PyMuPDF 字型抽取／渲染 PASS；`check_links.py` 0 failures、0 network checked、5 inconclusive；`git diff --check` exit 0（僅既有 CH04/history LF/CRLF 訊息）。
- `reports/CH05-FINAL-ACCEPTANCE.md` 已依範本完成 32 項逐條 audit：PASS 19、NEEDS HUMAN REVIEW 13、FAIL/BLOCKED/NOT RUN 為 0。剩餘：英文人工校譯；理論全文與頁碼/主張定位；合法 *Get Out* 版次觀片及 locator/timecode；製作倫理、AI/法律/社群專業審查；兩 SVG 個人創作者確認、權利、可及性與出版核准；正式逐頁校樣及作者簽核。依作者偏好，全書人工簽核留到全部章節完成後。
- 後續封裝雙語 DOCX/PDF/EPUB、canonical 稿、caption/alignment/terms/references/manifest/SVG 原稿及驗收報告為草稿 ZIP，產生 output hash manifest 並更新 run logs；run 應以 `partial` 完成，因人工審核仍待辦。此後停止等待使用者指定 CH06；沒有發布、commit 或 push。

- CH05 packaging follow-up: created `tmp/CH05-draft-20261020-r1/CH05-Codex-Materials-DRAFT.zip` (18 members; CRC PASS; SHA-256 `bdc4c2ddd1c69831ad7ff88ee1303fba9476f9c0786b78e5f20342fa222cd282`). External `OUTPUT-MANIFEST.json` lists artifact hashes; run `verification.json` records route checks, DOCX/EPUB integrity, PDF font streams, and render evidence. Acceptance report now includes package checksum. Pipeline run finished `partial` with chapter audit and automated work done, while English/source/film/rights/editor review and author approval remain pending. No publication, commit, or push.
- CH05 package revision follow-up: the first archive r1 was retained; after adding the final package section to the acceptance report, created non-overwriting `CH05-Codex-Materials-DRAFT-r2.zip` (18 members, CRC PASS, SHA-256 `5779da3446aa9aeacff7707b0994e01923aa076eb1347d45354d287df3de73f3`). Verified the report inside r2 is byte-identical to the repository report. `OUTPUT-MANIFEST.json` points to r2 and records its checksum; r1 remains preserved for audit history.

## 2026-10-21 — CH05 待辦解法說明與素材包來源清單修正

- 使用者詢問 CH05 驗收報告所列「非正式出版標準」項目的解法。先核對 `reports/CH05-FINAL-ACCEPTANCE.md`、pipeline run 和草稿 ZIP；區分可以自動驗證的出版工程與須由作者／專業審稿者完成的出版決策。未改寫 CH05 正文。
- 封裝抽查發現 r2 素材包內 `CH05-sources.yaml` 因 ID 篩選錯誤為空，但 canonical `data/references.yaml` 有 R039–R044 六筆來源。由 canonical registry 重新產生來源快照，保留來源各自狀態與定位限制；在驗收報告註明修正範圍，未變更 canonical references、正文、已存在 r1/r2 ZIP。
- 建立不覆蓋的 `tmp/CH05-draft-20261020-r1/CH05-Codex-Materials-DRAFT-r3.zip`；18 members，ZIP CRC PASS，SHA-256 `88bc374f18691bbcdf7a40028f4a59293cb200a6c279285b40cac4145681854b`。封包內來源清單核對為 R039、R040、R041、R042、R043、R044；外部 `OUTPUT-MANIFEST.json` 已刷新所有檔案長度與 SHA-256。r1/r2 保留供稽核。
- 正式出版未核准；未執行 commit/push/deploy，未開始 CH06。人工項目仍依使用者決定留待全書完成後集中審核。

## 2026-10-21 — CH05 問題修復與 CH06 接續製作

- 使用者要求先處理 CH05 報告所列問題，再接續 CH06。依其先前規則，CH05 完成章末逐項稽核後才開始下一章；人工簽核仍留至全書完成後集中辦理。
- CH05 完成安全修補：新增專案自帶 Pandoc zh.yaml 翻譯資料並讓圖書建置器與 smoke test 明確使用 `--data-dir`；新增測試驗證本地繁中翻譯檔。MiKTeX 現有 `pdffonts.exe` 可供嚴格 PDF 字型檢查，未另行安裝工具。中英文 PDF 均確認 7 個字型物件有 embed/subset/ToUnicode，繁中字型正常嵌入，抽字未見 U+FFFD；兩語 EPUBCheck 5.4.0 均 0 errors/warnings/informationals/references。
- CH05 最新本機輸出為 `tmp/CH05-draft-20261021-r3/`；網站 build 123 pages。CH05 中英路由各 40 個唯一 ID、2 張本地圖片 alt 非空。緊接同步後的一次 Astro check 有 transient loader duplicate-ID console warning；獨立重跑診斷 0/0/0，輸出頁面 ID 實測唯一。此 transient 訊息保留於驗收報告，不宣稱每次執行均無警告。
- 更新 `reports/CH05-FINAL-ACCEPTANCE.md` 至 2.1.1-draft，修正舊輸出路徑、版本號、網站瞬態 warning 說明、嚴格字型驗證證據和逐項狀態數（PASS 20、NEEDS HUMAN REVIEW 12、FAIL/BLOCKED/NOT RUN 0）。報告結論仍為非正式出版標準。所有未簽核項目維持人工審查狀態。
- 建立非覆寫素材包 `tmp/CH05-draft-20261021-r3/CH05-Codex-Materials-DRAFT-r4.zip`：29 members，ZIP CRC PASS，SHA-256 `fb39c460d307037612c5e1876465ad4148dc0fe0733b3b4b554f1969a14a48e8`；`OUTPUT-MANIFEST.json` 保存逐檔 SHA-256。原有素材包版本皆保留。CH05 pipeline checkpoint 以 `partial` 結束，章末 audit stage PASS 僅代表逐項稽核程序完成，不是作者或出版核准。
- 然後按使用者明確指示開始 CH06。初步檢查顯示 canonical 中英檔為空白 scaffold，章名《故事、情節與因果結構》，沒有既存完整正文；本章必須另開獨立 run、先備份並補研究與雙語草稿。已查得主要資料來源為 MIT Internet Classics Archive 的 Aristotle *Poetics*（英譯文本）、Criterion Collection《Rashomon》片目及 Stephen Prince 影評、AFI Silver《Rashomon》資料。其後需謹慎限制理論解讀歸屬，不虛構觀片版次或時間碼。
- 未發布網站、未 commit、未 push；保留工作區既有 CH04/CH05 及其他未提交變更。

### CH05 packaging correction

- 最初的 r4/r5 素材包封裝檢查發現 canonical CH05 稿的路徑 basename 假設錯誤；不修改或刪除已產生 ZIP，將其作為歷史版本保留。修正打包腳本使用實際檔名 `CH05-chapter-05.md` 後重新封裝 r6。
- CH05 最終素材包為 `tmp/CH05-draft-20261021-r3/CH05-Codex-Materials-DRAFT-r6.zip`，31 members、ZIP CRC PASS、SHA-256 `fc5aff192e51cf4909bb31d606f60b5611281d5f2a3e188342e5bd4de914e974`；來源稿、manifest、build outputs 和報告在包內核對，r1–r5 均保留。

## 2026-10-21 — CH06《故事、情節與因果結構》雙語研究草稿與出版預檢

- 使用者要求修復 CH05 後接續 CH06。本次先完成 CH05 report/r6 package/run audit，再另開 CH06 pipeline run `production/runs/CH06/20261021T065143+0800-f153e02e/`，並在修改前備份 8 個原 scaffold、registry、引用與矩陣檔案；SHA-256 於 `backup/MANIFEST.json`。CH06 起始只有空白中英 scaffold。V1、CH01–CH05 正文未被本輪改寫；所有既有未提交檔案保持原狀。
- 2026-10-21 查讀／搜尋 MIT Internet Classics Archive 的 Butcher 英譯 Aristotle *Poetics* 第 6–11 章、University of Wisconsin Press 的 David Bordwell 專書介紹、Criterion《Rashomon》片目與 Stephen Prince 具名影評、AFI Silver 片目。逐來源限制明列於 `production/runs/CH06/.../RESEARCH-SOURCE-CHECK.md`。沒有取得 Bordwell 全文或印刷頁碼；未宣稱作者觀看任何特定《羅生門》版次或鏡頭 timecode。R046–R050 登錄到 YAML/BibTeX。
- 將 CH06 中英文 canonical 從空白 scaffold 擴寫為 12 個對齊章節錨點的研究稿：術語中英對照、歷史理論及適用範圍、傳統寫作／場景流程、AI 可用工作假設與限制、10 步工作流程、模型中立 JSON 診斷提示詞、*Rashomon* 多視點案例與原創練習、常見錯誤、品質驗收、評量及延伸研究。建立 8 個 draft 術語與 `metadata/translations/CH06-alignment.yaml`；雙語均 review-needed，未標 approved。
- 一次 metadata 編輯將 CH06 術語區塊插入 CH01 第一條詞目未完成欄位之前，導致 CH01 單元測試暫時失敗；立即用前備份與 YAML 結構定位，將 CH01-DEEP-FOCUS 原 references/status 還原，並將 CH06 詞條移至術語資料庫尾端。CH01 原文／權利／圖片不變；CH01 相關測試重新通過，全套 51 tests 最終 PASS。修復腳本保存在 CH06 run 內。
- 初次 CH06 format script 找不到 Pandoc，因本 PowerShell session 的 PATH 未載入；確認實際位置 `C:\Users\user\AppData\Local\Pandoc\pandoc.exe` 和 MiKTeX bin 後在 run script 明確使用已安裝路徑。首個空輸出資料夾保留；成功輸出在 `tmp/CH06-draft-20261021-r2/`。沒有重新安裝軟體。
- 出版預檢：中英文 DOCX/PDF/EPUB 六份草稿建置 exit 0；DOCX ZIP CRC 各 16 members、EPUB ZIP CRC 各 9 members；EPUBCheck 5.4.0 中英皆 0 errors/warnings/informationals/references。strict pdffonts 兩本各 7 字型列均 emb/sub/uni=yes；PyMuPDF 抽字無 U+FFFD；中英文首末頁 proof 已目視檢視，版面可讀且沒有明顯截切。中文 PDF 6 頁、英文 PDF 8 頁。Astro check 0/0/0；site build 123 頁；CH06 route 中英各 32 unique IDs、目前未置入圖片。一次 sync 緊接的 check 曾有 transient duplicate-ID loader console 訊息；獨立重跑和最終 build 無警告，輸出頁 ID 實測唯一。
- 最終自動驗證：V2 validator PASS；project validator PASS（12 parts、60 planned chapters、52 terms、45 references）；site sync check PASS；全套 unittest 51/51 PASS（含 CH01 regression 和 CH06 專項 3/3）；`git diff --check` exit 0，僅有既有 LF/CRLF working-copy warnings；全域連結掃描 0 failures、0 network-checked、5 inconclusive。嚴格 PDF／EPUB／route 證據記於 `production/runs/CH06/.../verification.json`。
- 建立 `assets/chapters/CH06/CH06-RASHOMON-VIEWING-LOG.md` 與 `CH06-HUMAN-REVIEW-CHECKLIST.md`；明確留下作者須填合法版本、字幕和 timecodes。CH06 未使用任何圖片，因此沒有第三方影像；原創因果圖、多視點圖、figure manifest 和雙語 caption/alt 尚未製作，報告明列 NEEDS HUMAN REVIEW，沒有把缺圖假報完成。
- `reports/CH06-FINAL-ACCEPTANCE.md` 列出自動 PASS、來源/雙語/插圖人工項目與證據；結論：可審查雙語草稿和技術草稿完成，但未達正式出版標準。素材包 `tmp/CH06-draft-20261021-r2/CH06-Codex-Materials-DRAFT-r1.zip` 44 members、CRC PASS、SHA-256 `3ebeaf837789f17a5029377e2a156a575a126b7138a099f98050531e032df006`；外部 `OUTPUT-MANIFEST.json` 有逐檔雜湊。CH06 run 應以 partial 結束。
- 未發布網站、未 commit/push GitHub。下一章不得自動開始，等待使用者明確指定；全書人工簽核仍於所有章節完成後集中辦理。
## 2026-10-21 — CH06 未完成項目續作與雙語原創圖整合

- 使用者要求續做 CH06。遵循 `ai-video-bible-chapter-pipeline`；建立 continuation run `production/runs/CH06/20261021T164101+0800-10139b29/`，先備份兩語章稿、章圖 manifest、全域圖登錄、資產登錄、來源 BibTeX、測試、驗收報告、矩陣、history、Lua caption filter 和書籍建置器；雜湊列於 run 備份 MANIFEST。CH01–CH05、V1、既有 CH06 r2 草稿包未覆蓋；未發布、未 commit/push。
- 查證 David Bordwell 作者網站公開 *Poetics of Cinema* 第 3 章 “Three Dimensions of Film Narrative” PDF；其中 “Narration and story” 印刷頁 14–15（PDF 頁 13–14）區分 fabula、syuzhet 與視聽風格。新增 R051 至 `data/references.yaml`、`metadata/references.bib`、雙語章稿及 translation alignment。保留 R047 書目，但不把沒有查閱全文的主張歸給該書。亞里斯多德仍限於悲劇理論詮釋；沒有虛構紙本頁碼。
- 手寫兩張原創、透明背景、可編輯雙語 SVG：CH06-FIG-001 因果鏈、CH06-FIG-002 故事時間／呈現順序。已附中英文題名、caption、alt、章節 ID、穩定圖號 6-1/6-2、來源用途、製作方式／日期、尺寸／雜湊和 rights/approval 欄位；`figure-captions.md` 及獨立 `CH06-FIGURE-RIGHTS-AND-SOURCES.md` 一併建立。原圖只用抽象文字與向量形狀，無第三方圖片、劇照或特定電影鏡頭。rights/status 皆 pending；創作者／權利人歸屬、可及性、相似性及出版核准保留人工審查。
- 將 CH06-FIG-001 放在 S07 工作流程之後、提示詞節之前；CH06-FIG-002 放在 S09 案例／觀影練習之後。中英文章稿、manifest、registry、asset registry、對照 YAML、網站投影與 Pandoc caption mapping 同步。新增圖檔雜湊與 pending-rights 測試，並新增 PDF SVG 暫存轉檔的 regression test。
- 新圖整合初次暴露兩個實際出版缺口：Pandoc 相對資源路徑造成 EPUB/PDF 找不到 SVG；調整 Pandoc 工作目錄後 EPUB/DOCX 可嵌圖。MiKTeX 的 XeLaTeX 需要 `rsvg-convert`，本機未安裝，雖有 Inkscape；因此更新 `build_books.py`，建置前將圖片複製到暫存工作區，PDF 輸出時以 Inkscape 將 SVG 轉成向量 PDF，不改原 SVG。一次初次 `validate_project.py` 因新增 asset 欠 `research_sources` 失敗，已補來源 ID、查閱日及用途後通過。初次未轉檔 r3 PDF 保留於 `tmp/CH06-draft-20261021-r3/` 作錯誤紀錄。
- 成功輸出雙語 DOCX/PDF/EPUB 至 `tmp/CH06-draft-20261021-r4/`。EPUBCheck 5.4.0 中英文各 0 errors/warnings/informationals/references；DOCX 各含 2 media；EPUB 各含 2 圖與 alt。PDF 嚴格字型檢查中英各 14 個 font entries，全數 emb/sub/uni=yes；MuPDF 抽字 0 replacement chars；圖頁渲染目視檢查通過。Astro check 最終 0 errors/warnings/hints，建置 123 pages；中英文 CH06 route 均含 2 張本章 SVG、非空 alt、無重複 IDs。初次 Astro check 有 transient duplicate loader IDs，後續獨立 clean check/build 無警告，實際輸出唯一。
- `scripts/v2_validate.py` PASS；`scripts/validate_project.py` PASS（12 parts、60 planned chapters、2 canonical chapter files、52 terms、46 references）；全測試 55/55 PASS（CH06 專項 5/5）。其中 SVG 轉 PDF regression test 使用 test double 驗證 staging 不更動原稿，實際 r4 PDF 則另由本機 Inkscape/XeLaTeX 建置。
- 人工事項仍未完成：全書末由作者／雙語編輯校譯和術語核定；選定合法《羅生門》版次實看並補版本／字幕／片長／timecodes；確認圖像作者署名／權利、可及性與出版核准。遵循使用者「全部章節完成後再人工審核」安排，本輪不代簽、不標 publication-ready，亦不開始 CH07。

- 封裝雙語原稿、CH06 專屬術語／來源快照、兩張 SVG、權利與觀看紀錄、manifest、驗收報告、build script/log、雙語 DOCX/PDF/EPUB 及校樣 PNG 為非覆寫 `tmp/CH06-draft-20261021-r4/CH06-Codex-Materials-DRAFT-r3.zip`（42 members、CRC PASS）；較早 r2 包保留。`PACKAGE-CHECKSUM.json` 記錄 SHA-256。
- 實際執行中英書籍與網站 image policy；四個目標均 BLOCKED，原因是全專案仍有圖片 approval/rights/creator/attribution 待核（包含 CH06 pending 圖）。此結果確認正式發布閘門有效；網站僅本地建置。

- 最終 run 狀態依流水線逐項記錄並以 `partial` 結束（自動工程工作完成；人工簽核依作者安排留待全書完成）。更新正式驗收報告與 history 後，另封裝 `CH06-Codex-Materials-DRAFT-r4.zip`，保留 r2/r3，封包含 finalized run.json。

- 回歸審查發現原書籍建置器把 AI 生成模型欄位硬套於手繪 SVG，會阻擋未來合法核准後的向量圖。依檔案類型修正驗收：SVG 必須有方法與製作紀錄；點陣生成圖仍須完整生成 provenance。新增兩項測試；CH06 7/7、全套 55/55 PASS。兩張實際圖權利仍 pending。最終報告／封包升版至 r5，r2–r4 保留。

## 2026-10-21 — CH07《人物、欲望、衝突與角色弧線》雙語草稿與稽核

- 依使用者指定開始 CH07；本輪僅處理 CH07，未開始 CH08。工作前確認 canonical 中英文檔僅為 scaffold，章名為《人物、欲望、衝突與角色弧線》，英文章名先列 working title。Run 為 production/runs/CH07/20261021T185845+0800-c279f9b1；修改前檔案與 SHA-256 留在 run/backup/pre-edit/MANIFEST.json。未覆蓋 CH01–CH06 章稿；專案既有 CH04–CH06 未提交變更保持原狀。
- 建立 CH07 中英文研究草稿與 CH07-S00–S13 對齊節次，涵蓋角色欲望、目標、阻礙、選擇、代價、角色弧線、傳統寫作流程、AI 工作假設／限制、詳細流程、模型中立提示詞、案例、常見錯誤、練習及研究來源。登錄 8 個 TERM-CH07 詞條、translation alignment、章節來源／案例筆記及人類審查清單；雙語及術語狀態保留 review-needed。未將未核實電影鏡頭時間碼或工具能力寫成已查證事實。
- 新增兩張透明底、可編輯的原創 SVG：CH07-FIG-001 目標—阻力—選擇—代價流程、CH07-FIG-002 角色弧線證據矩陣。已登錄雙語標題、圖說、alt、SHA-256、原創方法及 pending 權利狀態；非電影劇照、未標核准。為 DOCX staging 及 PDF 向量轉檔新增建置器修正；修復 Pandoc 章節圖號 filter 以顯示 7-1／7-2。SVG 原圖與編輯紀錄保留。
- 修正過程曾發現透明 SVG 全畫布 rect 在 PDF 渲染成黑底；刪除該透明背景物件後以 r5 重建，人工查看白底 SVG 及 PDF proof，圖文清晰。r1–r4 輸出留作診斷歷史。最終草稿為 tmp/CH07-draft-20261021-r5/，包括中英文 DOCX/PDF/EPUB、build logs 與 proof。
- 最終測試：CH07 專項 unittest 6/6 PASS；V2 validator PASS；project validator PASS（12 parts、60 planned chapters、52 terms、52 references）。Astro check 0 errors/warnings/hints，網站本機建置 123 pages；中英文 CH07 頁各 43 個唯一 ID、2 張本章圖、所有 alt 非空。網站未發布。中英 PDF strict pdffonts 均有 Microsoft JhengHei，所有字型 emb/sub/uni=yes；PyMuPDF 抽字無 replacement character；PDF 9／12 頁，圖號 7-1/7-2 各出現一次。中英 EPUBCheck logs 均記錄 EPUB 3.4 規則下 0 errors/warnings/references（工具版本未記錄）；DOCX 內含已 staging 圖片。圖面與版面 proof 已人工目視。
- 全套 unittest discovery 實測 61 tests，60 pass、1 error：既有 CH01 詞條缺少 status 導致 CH01 測試 KeyError。前置備份確認為既有資料問題；尊重章節保護，本輪不改 CH01。外部連結掃描 0 failures、7 inconclusive，待來源審查時人工複查。
- reports/CH07-FINAL-ACCEPTANCE.md 列出逐項狀態及待人工事項；判定本章完成可審查草稿與技術預檢，但未達正式出版標準。英文校譯、理論／案例核查、術語、圖權、作者核准依使用者安排待全書完成後集中處理。素材包只含草稿，不具發布核准；本機執行沒有發布、commit 或 push。
- pipeline run 以 partial 結束，表示可自動執行的製作與章末稽核完成，而人工編審、rights 和作者核准閘門仍開啟。素材包與每檔雜湊另記於 tmp/CH07-draft-20261021-r5/PACKAGE-MANIFEST-r3.json。

## 2026-10-21 — CH08《場景、節拍、對白與潛台詞》製作、驗收與全書進度表

- 依使用者 `ch08` 指示，只製作 CH08，沿用 `.codex/skills/ai-video-bible-chapter-pipeline/SKILL.md` 與 V4 SOP。開始時原 Windows cwd 不在 repo，依使用者既定路徑定位既有專案；Git 有多項 CH04–CH07 未提交變更，全部保留。CH08 原 canonical 中英文稿是 scaffold，圖 manifest 為空。建立 run `production/runs/CH08/20261021T200413+0800-16f990d8/`，編輯前備份 17 個目標檔案並記錄 SHA-256；未改寫 CH01–CH07 正文。
- 建立 CH08-S01–S12 繁中研究草稿與英文工作譯稿；登錄 8 個雙語 draft 術語、R058–R065 來源及 BibTeX、翻譯 alignment、電影案例限制、人類審查清單。英文仍需校譯；來源摘要／書目查證不等於全文頁碼查證。案例只按可追溯片目和二手評論陳述，不宣稱已親看特定版次、不虛構時間碼或複製對白。
- 新增兩張可編輯、手繪的原創 SVG：CH08-FIG-001（圖 8-1，場景行動／反應與節拍狀態）及 CH08-FIG-002（圖 8-2，對白／潛台詞證據層次）。更新雙語圖說、alt、manifest、hash、alignment、全域 figure／asset registry 和圖號 Lua filter。兩圖皆未標核准；權利、署名、相似性、可及性及正式出版核准維持 pending。
- 建立 `reports/CHAPTER-PROGRESS-TRACKER.md`，以 `metadata/chapters.yaml` 產生 CH01–CH60 一章一列的進度表，並新增可重跑的 `scripts/update_chapter_progress_tracker.py`。狀態字典明確區分草稿完成、部分完成、待完成、待人工審查；後續每章結束都應更新該表及該章報告。
- 章節測試 `python -m unittest tests.test_ch08_content -v`：5/5 PASS。`python scripts/v2_validate.py` PASS；`python scripts/validate_project.py` PASS（12 parts、60 planned chapters、52 terms、60 references）；網站 sync check PASS。全套 unittest：66 tests、65 PASS、1 ERROR，唯一錯誤是既有 CH01 詞條缺 `status` 欄位所致 KeyError；本輪沒有修改 CH01。
- 執行 `npm --prefix apps/web run check` 最終結果 0 errors／warnings／hints；Astro 本機 build 123 pages。同步後中英文 CH08 routes 均存在，各有 39 個唯一 HTML IDs、兩張本章圖與非空 alt。一次較早的同步前 check 曾出現短暫 duplicate loader ID 警告；重新同步後的最終 check/build 未重現。
- Pandoc、MiKTeX XeLaTeX、Poppler pdffonts、Inkscape、Java 與 EPUBCheck 5.4.0 均以本機既有安裝建構，不安裝新工具、不付費。中英文 DOCX/PDF/EPUB 草稿產生於 `tmp/CH08-draft-20261021-r1/`。兩份 PDF strict 字型檢查均 pass，字型列 `emb/sub/uni=yes`；繁中 Microsoft JhengHei 可確認嵌入；抽取文字 U+FFFD 為 0；繁中 9 頁、英文 12 頁，圖 8-1/8-2 各一次。中英 EPUBCheck 各 0 fatal errors、0 errors、0 warnings、0 informational references。Astro 路由及 PDF 圖頁 proof 已實際檢查。
- `image_policy.py --target zh-TW-book` 與 `--target en-book` 均正確以 exit 2 阻擋正式出版，回報至少 CH01 圖片尚欠 rights、作者歸屬及核准；CH08 兩張圖本身亦 pending。兩語草稿格式通過不等於出版授權。
- 新增 `reports/CH08-FINAL-ACCEPTANCE.md`，判定 CH08 未達正式出版標準，列出 7 項集中人工審查工作及既有 CH01 測試錯誤。`reports/CHAPTER-PROGRESS-TRACKER.md` 作為後續每章完成後更新的總表。未發布網站、未 commit、未 push；本輪止於 CH08，不開始 CH09。
- 依使用者補充指示，將 CH08 驗收報告的人工審查事項持續保留為開啟待辦；擴充 `assets/chapters/CH08/CH08-HUMAN-REVIEW-CHECKLIST.md`，逐列列出理論審稿、全文／頁碼定位、雙語校譯、術語核定、合法案例觀片紀錄、兩張 SVG 權利與出版審查、出版校樣及作者／專業簽核。更新全書進度表生成規則，CH08 列明來源定位、校譯、觀片、圖權與簽核皆待全書完成後審查；沒有把任何人工項目標為完成。


## 2026-10-21｜CH09 類型劇作、系列敘事與非線性結構

- 依 CH09 SOP 先建立 run checkpoint 與編輯前備份，保留工作區原有未提交變更；未重置、刪除、發布、commit 或 push。
- 盤點章節 registry 為 planned，canonical 中英文檔為 scaffold，figure manifest 為空；依章名完成中英文 S01–S12 研究草稿。英文標題暫定 `Genre Writing, Serial Narrative, and Nonlinear Structure`。
- 登錄 R066–R069、9 個雙語術語草案與 CH09 雙語對照資料。來源查核日期為 2026-10-21；書籍頁碼、全文解讀、電影版次／timecode 保留人工查證。
- 新增 3 張原創可編輯 SVG、雙語圖說／alt、雜湊與待審權利紀錄；觀察校樣發現 SVG 路徑填色及 XML 重複屬性問題，已修正後重建 r7。沒有將圖稿標記為核准。
- 發現 `scripts/publishing/sync_site_content.py` 在既有生成圖片雜湊不同時僅回報 stale 而未同步，修正非 `--check` 模式會更新派生圖片；網站同步檢查其後通過。
- `scripts/publishing/build_books.py` 的 Inkscape 擷取輸出原依 Windows 系統 code page 解碼，非 ASCII 路徑曾造成讀取錯誤；改為 UTF-8／替代字元解碼，供可重現建置。
- CH09 測試 4/4 通過；V2 validator、project validator、網站同步、Astro 123 頁建置、雙語 PDF 字型嵌入及雙語 EPUBCheck 通過。全套 70 測試有 69 通過，1 項既有 CH01 缺少術語 `status` 欄位而報錯，未在本章修改。
- 驗收報告：`reports/CH09-FINAL-ACCEPTANCE.md`；全書進度列更新於 `reports/CHAPTER-PROGRESS-TRACKER.md`；章節矩陣已更新。人類審查／出版核准仍 pending。
- 草稿輸出：`tmp/CH09-draft-20261021-r7/`。本次只完成 CH09，未開始 CH10。

## 2026-10-22｜CH10 劇本格式、改編與版本管理

- 依章節 SOP 建立 CH10 checkpoint `production/runs/CH10/20261022T062041+0800-d6ab6deb/`。盤點 registry 記錄的章名為「劇本格式、改編與版本管理」，英文名原先空白；canonical 中英文稿僅 scaffold，figure manifest 空白，未找到 CH10 staging 素材包。開始前 Git 工作區已有大量 CH04–CH09 及出版流程未提交變更，均保留。
- 編輯前備份 13 個目標檔案與 SHA-256 manifest；結束前逐檔核對備份雜湊，13/13 通過。原有 CH01–CH09 原稿及素材未被刪除或覆寫。
- 建立 CH10 S01–S12 繁中研究稿與英文工作譯稿，內容涵蓋劇本格式差異、改編與權利分流、修訂／鎖頁、Fountain 交換格式、AI 限制、流程、模型中立 prompt、《綠野仙蹤》（1939）研究案例、品質檢查與練習。暫定英文標題為 `Screenplay Format, Adaptation, and Revision Management`，待作者及雙語編輯核定。
- 瀏覽並核對 R070–R076：Academy Nicholl、WGAW Registry、美國著作權法、Final Draft 修訂模式及鎖頁文件、Fountain 語法、AFI Catalog《The Wizard of Oz》。書目及來源使用範圍記於 `assets/chapters/CH10/CH10-SOURCE-AND-CASE-NOTES.md`；不宣稱觀看片源、時間碼或法律核准。新增 8 筆雙語 draft 詞條及翻譯 alignment。
- 手工繪製 3 張可編輯雙語 SVG（版本生命週期、改編來源／權利分流、場景 ID 差異審查），新增雙語圖說／alt、figure manifest、figure registry、asset registry、製作紀錄及待審清單。PDF 圖頁校樣發現標題文字對比過低，已改為深色並同步 SHA-256；所有圖稿保持 pending，未使用第三方圖片或 AI 圖像服務。
- 更新 `metadata/chapters.yaml`、`metadata/translation-status.yaml`、`metadata/terminology.yaml`、`metadata/translations/CH10-alignment.yaml`、`data/references.yaml`、`metadata/references.bib`、`data/assets.yaml`、`metadata/figure-registry.yaml`、`scripts/publishing/figure-captions.lua` 與 CH10 列於 `CHAPTER_INTEGRATION_MATRIX.md`。更新 `reports/CHAPTER-PROGRESS-TRACKER.md` 的 CH10 狀態，保留人工審核未完成。
- 新增 `tests/test_ch10_content.py` 與本機草稿建置工具 `scripts/publishing/build_chapter_drafts.py`。CH10 測試 4/4 通過；`scripts/v2_validate.py` 通過；`scripts/validate_project.py` 通過（60 章登錄、52 術語、71 來源）；`scripts/check_links.py` 通過 73 個唯一 URL 的語法檢查。
- 雙語網站內容同步及 `--check` 通過。最終 `npm --prefix apps/web run check` 為 0 errors／warnings／hints；網站 build 產生 123 頁。CH10 中英文頁各有 38 個唯一 HTML id、3 張本機圖及非空 alt；未部署。
- 出版草稿 r1 使用 Noto Serif TC 時，MiKTeX/dvipdfmx 出現 `Invalid font: -1 (0)`，log 記為 `fwrite` invalid argument，並有字型缺字警告。改以 Microsoft JhengHei 執行 r3：中英文 DOCX、8／10 頁 PDF、EPUB 均生成；PDF pdffonts 各有 16 個嵌入字型項目。EPUBCheck 兩語各為 0 fatal errors、0 errors、0 warnings，ZIP CRC 通過。PDF 圖頁已抽查，Noto Serif TC 環境根因仍待另查；出版草稿的視覺校樣及字型選型仍待人工確認。
- 全套測試 `python -m unittest discover -s tests -v` 為 74 項中 73 項通過、1 項既有 CH01 術語缺 `status` 欄位而出現 `KeyError`；本次未修改 CH01。最終 Astro check 未重現同步前的暫時重複 ID 警告。
- 新增 `reports/CH10-FINAL-ACCEPTANCE.md`，判定未達正式出版標準；作者、雙語、電影專業、法律／權利及插圖審查均列待辦。未發布網站、未 commit、未 push；完成 CH10 後停止，未開始 CH11。
- 下一步：待作者／全書階段審查時核定 CH10 英文標題和雙語文字、選定合法底本／觀看片源補充頁碼及時間碼、請適用法域法律專業人員審查改編權利、完成 SVG 署名與出版核准、抽查所有輸出；另行查明 MiKTeX 使用 Noto Serif TC 的根因及修復既有 CH01 測試錯誤。

## 2026-10-22｜CH11 導演工作：意圖、溝通與決策

- 依既有 `ai-video-bible-chapter-pipeline` SOP 啟動 CH11 run：`production/runs/CH11/20261022T181247+0800-46c00c02/`。開始前工作區已有 CH04–CH10 及出版流程的大量未提交變更；未清理或重置。先將 17 個 CH11 目標檔案及相關註冊表備份至 `backup/pre-edit/`，附 SHA-256 manifest，保留所有既有 V1 與已完成章節材料。
- 依 registry 章名「導演工作：意圖、溝通與決策」撰寫繁中 S00–S12 研究草稿及英文工作譯稿。內容涵蓋導演意圖的可觀察化、跨部門溝通、傳統前期與現場流程、AI 作為研究／整理輔助的假設及限制、模型中立提示詞、《教父》（1972）來源型案例、品質檢核與練習；未將 AI 假設寫成已驗證產品功能。
- 新增及核對 R077–R086 公開來源（AFI、DGA、ASC、AFI Catalog、Oxford Bibliographies、Rutgers/JSTOR 書目及 Library of Congress），同步進入 YAML 與 BibTeX；八個雙語術語以 draft 登錄。來源定位、適用範圍和證據限制詳列 `assets/chapters/CH11/CH11-SOURCE-AND-CASE-NOTES.md`，引用連結檢查有 27 項無法在本次確認，不能視為已失效或已通過。
- 手工製作兩張可編輯雙語原創 SVG（導演意圖驗證循環、部門交接問題），加入 manifest、資產／圖稿註冊、圖說、alt text 與製作紀錄。初次 PDF 校樣發現回饋線貼近圖中文字、部門卡片文字緊湊；重排 SVG 並刷新三份註冊的 SHA-256、位元組數與尺寸。未使用第三方劇照或圖像生成工具；署名、權利與出版核准保持 pending。
- 首輪校樣亦發現提示詞行太長；縮短中英文範本，並在本機單章 PDF staging 加入長縮排行折行，保留 canonical Markdown 的可讀格式。r3 PDF 圖頁校樣確認兩圖標籤和圖說可讀，提示詞不越出頁邊；完整版面仍待編輯校樣。
- 更新章節／翻譯／術語／來源／圖稿 metadata、CH11 雙語站點投影、章節整合矩陣、CH11 的 60 章進度檢核列與 pipeline run。CH11 專屬測試 5/5 通過；V2 validator、project validator、網站 sync check 通過。Astro check 為 0 errors/warnings/hints，Astro 本機建置輸出 123 頁；建置時未部署。中英文 DOCX、PDF、EPUB 草稿均輸出；中文 PDF 9 頁、英文 11 頁，字型嵌入檢查通過；EPUBCheck 5.4.0 雙語均 0 fatal errors／0 errors／0 warnings／0 informational references。
- 全套 79 個測試有 78 通過，唯一錯誤是原有 CH01 `test_chapter_terms_are_bilingual_and_registered` 缺 `status` 欄位產生 `KeyError`；未因 CH11 任務改動 CH01。外部連結檢查報告 0 failures、27 項未能確證。驗收報告為 `reports/CH11-FINAL-ACCEPTANCE.md`；人工審核表為 `assets/chapters/CH11/CH11-HUMAN-REVIEW-CHECKLIST.md`。
- 結論：CH11 可供審閱的研究草稿與本機出版預覽已完成，但正式出版標準未達成。電影史／導演實務與來源定位、英文校譯、合法觀片版次及時間碼、DGA 用語範圍、圖稿署名與權利、作者核准仍待人工審查。未發布網站、未 commit、未 push；完成 CH11 後停止，未開始 CH12。


## 2026-10-22｜CH12 演員調度、走位與表演連續性

- 依 `ai-video-bible-chapter-pipeline` SOP 執行 CH12 單章工作。開始前工作區已有 CH04–CH11、網站投影、註冊表及出版工程的大量未提交變更；保留原狀，未 reset、clean、刪除或覆寫其他章節。Run 為 `production/runs/CH12/20261022T202702+0800-a0742107/`；預先備份 18 個相關目標檔於 `backup/pre-edit/`，附 `MANIFEST.json` 與開始前 `git-status-before.txt`。
- CH12 初始狀態：章節登錄已有主題「演員調度、走位與表演連續性」，中英文 canonical 檔只有模板 scaffold，空 figure manifest，未找到章節來源包或既有插圖；CH13 內容未修改。
- 建立繁中 S00–S13 研究草稿及對應英文工作譯稿；涵蓋目標與動作節拍、表演協作、場面設計、部門交接、連戲紀錄、非順拍、AI 假設／隱私限制、模型中立提示詞、原創練習及評量。狀態維持繁中 `source-draft`、英文 `review-needed`；英文章名仍是 working title。
- 登錄九個雙語工作術語、章節翻譯對照及七筆 R087–R093 來源（YAML／BibTeX）。來源依可查範圍標示：Oxford UP 只查摘要；英國 ScreenSkills 職務及職業標準限定其法域；《畢業生》《發條橘子》使用已歸屬的製作回憶；《蘿拉・蒙特斯》使用 BFI 評論分析。沒有宣稱作者已觀片，也沒有杜撰片源版本或時間碼。完整 locator、法域和案例分析待專業審查。
- 手繪兩張可編輯中英雙語 SVG：CH12-FIG-001 走位協作流程、CH12-FIG-002 連戲交接紀錄；加入雙語圖說、alt、source IDs、尺寸、byte、SHA-256、方法及權利欄。無第三方劇照、無付費生圖。作者署名、相似性、技術／可及性、權利及正式刊用全部維持 pending。
- 更新 CH12 章節／翻譯 metadata、術語／引用／圖片 registry、`CHAPTER_INTEGRATION_MATRIX.md`、`CHAPTER-PROGRESS-TRACKER.md` 與 tracker updater。新增來源紀錄、人工審查表及 CH12 測試。初次全專案 validator 發現新 asset 少 schema 欄位 `media_kind`，補齊後 `validate_project.py` 通過。
- 網站 canonical 投影同步成功；`npm --prefix apps/web run check` 重跑為 0 errors/warnings/hints；本機 Astro build 完成 120 routes。第一次 check 曾出現 CH12 duplicate-ID loader notice，重跑未再出現；兩個輸出頁各有 41 個唯一 ID、兩張圖及非空 alt。未發布網站。
- 以 `scripts/publishing/build_chapter_drafts.py` 建置 zh-TW/en-US DOCX、PDF、EPUB 至 `tmp/CH12-draft-20261022-r1/`。PDF 共 8／12 頁，無 U+FFFD；兩份 PDF 的 `pdffonts` 12 個字型項目均嵌入，含 Microsoft JhengHei／Times New Roman；抽查繁中第 4–5 頁、英文第 6、8 頁，圖表與圖說可見。EPUBCheck 5.4.0 兩語皆為 0 fatal / 0 errors / 0 warnings / 0 info；ZIP CRC、圖號及替代字元檢查通過。以上是草稿證據，不是最終排版核准。
- CH12 專項測試 5/5 通過；V2 validator、project schema validator、site sync check 通過。全套測試 83/84；唯一失敗為既有 `tests/test_ch01_content.py::test_chapter_terms_are_bilingual_and_registered` 的 `KeyError: 'status'`，未修改 CH01。連結掃描 0 failures、27 URLs 未能確證。圖片出版政策不授權刊用（符合待審狀態；且全站還有既有 CH01 pending 圖）。
- 建立 `reports/CH12-FINAL-ACCEPTANCE.md` 並逐項列明 PASS／PARTIAL／FAIL／BLOCKED／NEEDS HUMAN REVIEW；建立 draft-only ZIP `tmp/CH12-draft-20261022-r1/CH12-Codex-Materials-DRAFT.zip`（20 members，CRC PASS；SHA-256 記於同目錄 `OUTPUT-MANIFEST.json`）。驗收報告保留在 ZIP 外以免循環雜湊。
- 結論：CH12 研究草稿與本機出版預覽完成，但**未達正式出版標準**。英文校譯、來源定位、合法觀片版次／時間碼、表演／導演／安全專業審查、插圖署名與權利、作者核准仍待人工處理；全套測試既有 CH01 問題和 27 個未確證連結亦列入後續。此輪只處理 CH12，未開始 CH13、未發布、未 commit、未 push。

- 素材 ZIP 首次封裝時，CRC 驗證程式誤在寫入模式尚未關閉的同一個 ZipFile 上呼叫 testzip，返回值被誤判為失敗；關閉後的唯讀重驗證確認 r1 CRC 完整。為避免 ZIP 內驗收報告快照與最終報告版本不同，保留 r1 不刪除，另製最終 r2（19 members，不含自我引用的驗收報告），閉檔後 CRC PASS；r2 SHA-256 及逐檔 hash 記於 `OUTPUT-MANIFEST-r2.json`。最終驗收報告在 ZIP 外維護。


## 2026-10-22 — CH13 製作與檢核

- 依使用者指示只處理 CH13「場面調度：空間、動線與視線」；工作區已有 CH04–CH12 等未提交變更，均予保留，未發布、未 commit、未 push。
- 初始稿件是中英文 scaffold，圖稿 manifest 為空；建立 run `production/runs/CH13/20261022T205359+0800-185a8aa8/`，預先備份 18 個既有目標檔案，SHA-256 清單與 Git 起始狀態存於 `backup/pre-edit/`。
- 新增 CH13 中英文研究稿（S00–S12）、七筆來源 R094–R100、六個雙語術語、逐節對照表及兩張手繪可編輯 SVG。所有來源限制、圖稿雜湊及權利待審狀態已記錄。
- 網站：Astro check/build 通過；初次同步檢查曾報 CH13 重複 loader ID，後續建置未重現；雙語路由各 38 個唯一 ID，兩個 figure ID 均存在。
- 出版草稿：中英文 DOCX/PDF/EPUB 產出；PDF 字型清單顯示嵌入 Microsoft JhengHei、Times New Roman 等字型；EPUBCheck 5.4.0 對兩檔均為 0 fatal/0 error/0 warning；EPUB ZIP CRC 正常。
- 測試：CH13 專項 5/5 通過；全套 89 項中 88 項通過，唯一失敗為既有 `tests/test_ch01_content.py::test_chapter_terms_are_bilingual_and_registered` 的 `KeyError: status`，本輪未改 CH01。
- 仍待作者、雙語編輯、電影理論／製作專業及權利審查；電影觀看片源、版本與時間碼未取得，未宣稱出版完成。
- 將 CH13 人工審查清單改為中英文對照，逐項保留待審狀態與責任角色；同步更新 CH13 草稿素材 ZIP 內的清單及雜湊。


## 2026-10-22 — CH14 研究草稿

- 已備份 CH14 原稿、登錄和工作區狀態於 `backups/CH14-start-20261022-224652/`；保留既有未提交變更。
- 新增雙語 S00–S12 草稿、R101–R106 來源、五個雙語術語、章節對照及兩張原創 SVG。
- 翻譯、理論、觀片定位、圖稿權利及作者核准待人工審查；未發布、未 commit、未 push；未開始 CH15。

## 2026-10-22 — CH14 技術驗收結果

- 專案 schema 與 V2 registry 驗證、CH14 專項測試 4/4 通過；Astro check/build、同步檢查、兩語 DOCX/PDF/EPUB 草稿、PDF 嵌字型驗證及 EPUBCheck 5.4.0 通過。
- 全套測試 92/93；唯一錯誤為既有 CH01 詞條 `status` 欄位 KeyError，未改動 CH01。外部連結仍有 27 項無法確認可達性。
- CH14 run 狀態為 `partial`；作者、雙語、電影專業及插圖權利審查未完成。詳見 `reports/CH14-FINAL-ACCEPTANCE.md`。


## 2026-10-23 — CH15 研究草稿與出版驗收

- 先盤點並記錄專案既有大量未提交變更；CH15 原為中英文骨架、空圖稿 manifest。建立 `backups/CH15-start-20261023-060700/`，19 個檔案備份，run checkpoint 留存初始原稿與 manifest SHA-256。所有舊章、V1 原稿和未提交工作均保留。
- 新增繁中與英文 S01–S12 研究草稿及 12 節翻譯對照；未核實的電影觀看片源／時間碼沒有假稱完成。R107–R111 收錄 ScreenSkills、American Cinematographer、DGA 資料並標示適用範圍與定位待辦；登錄 6 個雙語工作術語。
- 手繪兩張可編輯雙語 SVG，加入 manifest、雙語圖說／alt、製作雜湊、來源與權利待審紀錄。同步更新 chapter/translation registry、figure/asset/term/source registries、BibTeX、矩陣及 60 章 tracker。
- 修正新增 data asset 欄位以符合 image schema；網站圖稿轉換需在 Markdown 圖片與 caption 間保留空白行，Astro projection 才會產生語意化 figure 和穩定圖號。兩語輸出頁各含 43 個唯一 ID、2 張含 alt 圖及 CH15-FIG-001/002。
- MiKTeX 使用 Noto Serif TC 建 PDF 曾報 `dvipdfmx:fatal: Invalid font: -1` 並有缺字；改用 Microsoft JhengHei 後 PDF 通過，英文 Times New Roman 亦通過。雙語 PDF 字型各 13 項均嵌入；EPUBCheck 5.4.0 雙語均 0 fatal／error／warning／info。這個失敗與替代字型證據保留在 run 建置資料及本章驗收報告。
- Astro check 0 errors/warnings/hints，靜態網站 build 123 頁；前置 sync 出現 loader duplicate-id notices，但輸出 HTML 實測無重複 ID。CH15 專項測試 5/5，V2／schema／site sync validators 通過；全套測試 97/98，唯一既有 CH01 glossary `KeyError: status`，本輪未改 CH01。
- 產出本機雙語 DOCX/PDF/EPUB 草稿及 `tmp/CH15-draft-20261023-r4/CH15-Codex-Materials-DRAFT.zip`，ZIP CRC PASS。更新 `reports/CH15-FINAL-ACCEPTANCE.md` 與 `reports/CHAPTER-PROGRESS-TRACKER.md`。英文校譯、來源精確定位、電影版本／時間碼、片場專業審查、插圖權利及作者簽核仍待人工；CH15 未達正式出版標準。未開始 CH16、未發布、未 commit、未 push。


## 2026-10-23｜CH16 曝光、感光元件與影像形成｜研究草稿與出版預覽

- 使用者要求依 V4 SOP 只處理 CH16；先盤點登錄、章稿、圖 manifest、Git 狀態及素材。工作樹已有 CH04–CH15 等大量未提交改動；全部保留，未清理、重設、覆蓋其他章節。
- 備份：`backups/CH16-start-20261023-062121/`，含起始 CH16 中英文 scaffold、空 figure manifest、重要登錄／網站投影及 Git 狀態；SHA-256 清單：`SHA256SUMS.txt`。
- 主要 pipeline run：`production/runs/CH16/20261023T061952+0800-95526c49/`。起始 registry 原為 planned／translation-needed，沒有可整合的完整章稿。
- 建立中英文 S01–S12 實質研究草稿、12 節翻譯對照、12 個雙語術語、R112–R119 來源資料及兩張原創可編輯 SVG；圖稿均維持 draft／review pending，登錄製作方法、尺寸、SHA-256、雙語 captions／alt 及權利審查欄。
- 查證內容：Kodak 電影底片感光測定與曝光指南、ARRI ALEXA／Log C 動態範圍白皮書及 ALEXA LF 手冊、Sony Semiconductor 感光元件讀出技術、Nobel Prize CCD 背景。更正英文稿 Log C 與底片負片掃描類比的來源，由 R113 改為 ARRI 官方 VFX FAQ R119；中英稿、來源註記與 registry 同步。
- 修正 metadata 登錄腳本造成的 terms nesting 問題，並依專案 asset schema 補齊 SVG production log／rights risk review 欄位；`v2_validate.py`、`validate_project.py` 與 CH16 tests 通過。
- 網站：只同步 CH16 兩語投影及原創 SVG；同步檢查 PASS。Astro check 顯示 0 errors／warnings／hints，但載入初期印出 CH16 duplicate-id notices；最後產生的兩頁各有 42 個唯一 HTML IDs、2 個具 alt 圖片。Astro build 本機成功，123 頁，未發布。
- 出版預覽：新增 `tmp/CH16-draft-20261023-r3/`，含中英 DOCX／PDF／EPUB、全套測試 log 及繁中 PDF 第 1 頁與第 5 頁渲染抽查圖。PDF 為 10／14 頁；pdffonts 中英文所有 23／22 個字型皆 embedded。已視覺抽查中文標題／目錄頁及含 FIG-001 頁，圖文未截斷，圖上小字可讀性仍須人工設計審查。中英文 EPUBCheck 5.4.0 各 0 fatal／error／warning／info。
- 測試：`python -m unittest tests.test_ch16_content -v` 5/5 PASS；`v2_validate.py`、`validate_project.py`、site sync check PASS；網站 build PASS。全套 103 tests 有 1 個既有 CH01 `KeyError: status` error（102 pass／1 error）；本次未改 CH01。
- 文件更新：CH16 acceptance report、CHAPTER_INTEGRATION_MATRIX、CH01–CH60 tracker、CH16 human-review checklist、source/case notes 與本 history。所有作者、專業、英文、片例、來源 locator、插圖權利與可及性審查仍待辦；CH16 未達正式出版標準。
- 原 CH16 指令限定不部署、不 commit、不 push；驗收後使用者另行明確要求 commit/push。僅本機建置，沒有部署網站；整批已存在的 CH04–CH16 章節變更及 CH16 產出，與各章備份／run／報告一併提交並推送至 `origin/main`，commit `7a5721d39e982559d921030abec45c39842fc3c2`。本機 `production/runs/CH14/test.tmp` 未納入提交，原樣保留。

### Git 推送紀錄（使用者後續授權）

- 2026-10-23：`git push origin main` 成功；遠端 `refs/heads/main` 與本機 `7a5721d39e982559d921030abec45c39842fc3c2` 一致。
- Commit message：`Complete AI Video Bible chapters CH04-CH16`；共 580 個檔案變更（包含 CH04–CH16 的未提交稿件、圖稿、驗收資料與備份）。未部署網站。
