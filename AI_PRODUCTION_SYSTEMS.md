# 八大 AI 電影製作系統

> 狀態：架構規劃；除文中明列的現有本地出版／驗證工具外，均不是已整合系統。更新日：2026-10-19（Asia/Taipei）。

## 架構與治理

以章節 `chapter_id`、鏡頭 `shot_id`、資產 `asset_id`、提示詞 `prompt_id`、術語 `term_id`、來源 `reference_id` 作穩定識別。建議 JSON/YAML 使用 UTF-8、schema version、明確 locale、工具/model revision、時間戳、輸入／輸出 SHA-256、權利狀態及人類核准者。未知欄位用 `null` 或 `unknown`，不推測。凡會覆寫 canonical 章稿、外部呼叫、付費、發佈、上傳真實人物素材的步驟均須明確授權及可復原設計。

狀態區分：**已實際整合**＝repo 有可執行實作及測試；**規劃可行**＝設計候選尚無執行證據；**待查證**＝版本／授權／效能尚未核驗；**排除**＝作者指示不納入本架構。Remotion、Manim、Blender Python、ComfyUI 均為候選評估，沒有在本輪安裝或連接；Cinetic 與 TTS 依 2026-10-19 作者指示排除，不整合、不建立 adapter。

## 共用資料交接

```yaml
schema_version: 1
project_id: AI_VIDEO_BIBLE
chapter_id: CHXX
locale: zh-TW
artifact_id: SHOT-CHXX-001
artifact_type: shot-spec
status: draft
inputs: []       # 穩定 ID + sha256
outputs: []      # 穩定 ID + sha256
tool: {name: null, version: null, model: null}
parameters: {}
evidence: []     # reference_id / test_id / locator
rights_status: pending-review
human_review: {required: true, status: pending, reviewer: null, reviewed_on: null}
```

所有系統遵循 `draft → validated → human-reviewed → approved`；`approved` 僅由具名人類審查紀錄建立，不由模型或建置成功自動升級。

## 系統定義

### AIS01｜AI Screenwriting System
- **職責：** 劇本研究整理、結構檢查、版本差異、雙語素材及製片文件草擬。
- **輸入：** 創作 brief、受眾、既有稿、來源和授權／倫理限制。
- **輸出：** beat sheet、場景卡、劇本草稿、術語／來源 crosswalk、變更摘要。
- **格式：** Markdown + YAML front matter；JSON schema 的 scene list；Unicode UTF-8。
- **工具類型：** 文字模型、版本控制、文獻管理；供應商和價格逐次查證。
- **Codex：** repo 內安全讀寫、schema／引用／雙語差異檢查、變更報告、測試與版本管理。
- **Claude Code：** 可配置為本地 repo 編輯器；工具權限和模型行為須在部署環境實測，不視為現有整合。
- **人審：** 故事決策、歷史／真實性、人物倫理、改編權、英文定稿。
- **測試：** metadata、anchor、chapter/term/reference ID、diff 與禁止覆寫測試；創作品質由人評。
- **交接：** approved scene ID → directing；來源／術語 → research and QA。
- **狀態：** 本 repo 具 Markdown 章稿、chapter pipeline；研究生成及全自動撰稿未核准為正式流程。

### AIS02｜AI Directing System
- **職責：** 將場景意圖轉成表演、場面調度、鏡頭和聲音的協作計畫。
- **輸入：** approved scene、角色關係、場景限制、導演 intent、continuity ledger。
- **輸出：** beat map、blocking plan、shot list、預視覺化需求和 review notes。
- **格式：** shot-spec YAML/JSON、可編輯 SVG／分鏡圖，連回章節與資產 ID。
- **工具類型：** 多模態模型、分鏡／預視覺化工具、3D 場景工具。
- **Codex：** 產生結構化文件、欄位與鏡頭 ID 驗證、檔案差異及可重現工作說明。
- **Claude Code：** 可協助 code-based previs／專案腳本；目前無 repo 實測證據。
- **人審：** 表演意圖、倫理、演員同意、演出可行性、最終導演選擇。
- **測試：** shot list 完整性、場景／角色引用存在、相鄰鏡頭連續規則；審美由導演判讀。
- **交接：** shot spec → cinematography、production design、sound；批准剪輯意圖 → editing。
- **狀態：** 規劃可行，沒有現場導演 Agent 整合。

### AIS03｜AI Production Design System
- **職責：** 管理世界設定、場景、道具、服裝、色彩與可製作性。
- **輸入：** 劇本、導演視覺 brief、尺寸／預算限制、原創素材與權利資料。
- **輸出：** design bible、資產 manifest、原創 SVG／概念圖 brief、continuity ledger。
- **格式：** YAML asset manifest、SVG、PNG/WebP proof、SHA-256 與權利欄位。
- **工具類型：** 向量繪圖、3D/CAD、圖像生成工具；不得把 web 搜尋圖當成出版插圖。
- **Codex：** 檢查 manifest、hash、授權狀態、路徑與圖稿輸出 gate。
- **Claude Code：** 可建資產轉換／程序化繪圖腳本；需經檔案差異及安全審查。
- **人審：** 美術原創、第三方相似性、肖像／商標、文化脈絡和設計決策。
- **測試：** SVG XML／尺寸／字型、圖號 caption alt 配對、asset source 欄位、rights gate。
- **交接：** approved design → animation/cinematography；dimensions/materials → production。
- **狀態：** 有既存資產及權利規範；自動設計產生器未整合。

### AIS04｜AI Animation System
- **職責：** 將動作、時間、角色／物件與鏡頭設計轉成可生成／可動畫、可檢查的序列。
- **輸入：** storyboard、角色／場景 reference、動作描述、fps／時長／畫幅、權利資料。
- **輸出：** 動畫／生成片段、keyframe notes、版本和失敗記錄。
- **格式：** shot spec JSON、常見中間影片容器、SVG/PNG sequence；codec 設定依工具驗證。
- **工具類型候選：** Manim（程序式技術動畫）、Blender Python／Blender MCP、ComfyUI workflow、商業影片模型。Manim 官方文件支持其以 Python 場景描述動畫；Blender MCP 需視為高權限程式執行面；ComfyUI 工作流／API 格式需鎖版本與模型授權。
- **Codex：** 建／驗 workflow metadata、執行已核准本機腳本、抽幀與檔案完整性測試。
- **Claude Code：** 可協助程式化場景與修補腳本；本 repo 未實測此交接。
- **人審：** 動作／人物一致性、偏見與 likeness、模型授權、正式使用核准。
- **測試：** 解碼、codec、fps、時長、黑幀／損毀檔、shot continuity；內容審看由人執行。
- **交接：** render → editing／VFX／sound；provenance → rights／producing QA。
- **狀態：** 有 fail-closed image adapter 和 test double，正式圖像生成仍 BLOCKED；Manim/Blender/ComfyUI 未整合。

### AIS05｜AI Cinematography System
- **職責：** 把視覺意圖轉成攝影／鏡頭參數、生成提示和可檢測的畫面驗收規則。
- **輸入：** shot spec、場景空間、畫幅、鏡頭參數、色彩／曝光意圖和參考素材。
- **輸出：** camera plan、prompt、生成／拍攝結果、鏡頭級 QA 記錄。
- **格式：** JSON/YAML shot schema；圖像／影片 metadata；原圖和 derivative 分別 hash。
- **工具類型：** 攝影機與鏡頭、生成式影像／影片模型、色彩分析和影像檢查工具。
- **Codex：** 驗欄位、提示與測試清單、版本及輸出檔案，報告自動指標。
- **Claude Code：** 可編寫影像分析或生成 adapter；需做模型及環境實測。
- **人審：** 構圖目的、視點倫理、曝光／膚色、藝術品質與發布決策。
- **測試：** 畫幅/fps/解析度、焦點／裁切／連戲抽查、指定主體/空間要求；不可宣稱語義自動測試等於電影審美通過。
- **交接：** verified shot → editing/VFX；prompt及模型 provenance → archive。
- **狀態：** 有 shot-list schema 和提示詞資料；未與攝影機或生成服務實際連接。

### AIS06｜AI Sound System
- **職責：** 管理聲音腳本、對白／旁白記錄、效果／配樂需求及聲音交付驗證。
- **輸入：** script/shot timing、錄音／音效來源、許可／同意、輸出 loudness spec。
- **輸出：** sound cue sheet、stems、字幕／時間碼 crosswalk、混音 QA 報告。
- **格式：** CSV/JSON cue sheet、WAV/BWF metadata、字幕格式；依交付規格確定採樣率與聲道。
- **工具類型：** DAW、聲音分析、語音辨識、合成聲音工具（若另行核准）。
- **Codex：** cue／字幕時間碼檢查、manifest、hash、規格及權利 gate。
- **Claude Code：** 可寫本地音訊批次處理／測試腳本；需經聽測和資料安全審查。
- **人審：** 混音、聲音表演、音樂創作、合成聲音同意、授權與文化審核。
- **測試：** codec、峰值、silence、同步與字幕欄位；主觀聽感由人檢聽。
- **交接：** locked picture/timecode → sound edit；approved stems → final package。
- **狀態：** 沒有整合聲音生成服務；依使用者指示，本架構不整合 TTS。

### AIS07｜AI Editing System
- **職責：** 以版本化時間線管理鏡頭選擇、剪接、字幕、聲畫同步與輸出。
- **輸入：** verified media、scene/shot IDs、剪輯意圖、frame rate、音訊與字幕資料。
- **輸出：** EDL/XML/JSON timeline、proxy/master、字幕、版本比較報告。
- **格式：** 可移植 timeline/interchange 格式及機器可讀 asset manifest；NLE 專用格式需另測。
- **工具類型：** NLE、程序式影片組裝工具及影像／音訊檢測器。Remotion 是候選的 React 程式化影片組裝工具，非通用 NLE。
- **Codex：** 版本／路徑／timeline schema checks、建置可重現報告和輸出 hash。
- **Claude Code：** 可協助時間線轉換與 render code；不得直接宣稱編輯意圖準確。
- **人審：** 剪接點、表演節奏、資訊、字幕、色彩、音畫藝術決策。
- **測試：** 影格率、解析度、時長、音畫同步、片尾字幕、播放解碼、檔案校驗。
- **交接：** picture lock → sound/color/VFX finishing；master → producing QA/archive。
- **狀態：** Remotion 待查與評估、未整合；現有書籍 build 不等於影片剪輯系統。

### AIS08｜AI Producing & Quality Assurance System
- **職責：** 控制需求、成本、權利、風險、資料治理、驗收、交付與可追溯記錄。
- **輸入：** brief、預算／排程、各部門交付、授權／同意、品質 rubric 與 release checklist。
- **輸出：** production plan、風險登錄、cost log、章節／影片 acceptance report、可復原版本。
- **格式：** YAML/JSON schemas、Markdown 報告、Git commit／tag 和 SHA-256 manifest。
- **工具類型：** issue/project tracker、版本控制、測試工具、可選估價／計帳資料源。
- **Codex：** 執行本機檢查、追蹤缺口、產生可審 diff／備份／測試報告；不擅自發布或承擔作者核准。
- **Claude Code：** 可處理本機程式／文件整合；角色權限與審核由 repo 規則設定。
- **人審：** 預算承諾、合約、法務意見、出版核准、風險接受及最終藝術判斷。
- **測試：** schema、完整性、來源／權利狀態、link check、build、PDF 字型、EPUBCheck、audit 的實際證據。
- **交接：** 每系統先產 draft → QA 對證 → 專業／作者核准 → 有權者執行發佈。
- **狀態：** repo 具章節 pipeline、驗證、出版工具與人工 gate；非電影製片 ERP，不能替代合約／法務／作者決策。

## 工具整合評估（非已整合聲明）

| 工具 | 定位與潛在用途 | 本 repo 狀態 | 限制／下一個驗證 |
|---|---|---|---|
| Remotion | 以 React/程式化資料產生影片或教學動畫；[官方 render 文件](https://www.remotion.dev/docs/render)、[參數化渲染](https://www.remotion.dev/docs/parameterized-rendering) | 可行候選，未安裝／未實作 | 先做無商業費用條款承諾的本機 prototype，驗 license、字型、音訊、render 可重現性 |
| Manim Community | Python 場景產生數學／技術動畫；[官方 quickstart](https://docs.manim.community/en/stable/tutorials/quickstart.html) | 可行候選，未安裝／未實作 | 先驗中文字型、SVG／公式輸出及授權，定位為說明圖而非電影生成器 |
| Blender Python | 3D 場景、預視覺化、批次 render；[官方 API](https://docs.blender.org/api/blender_python_api/) | 可行候選，未連接 | 在隔離環境測試版本、外掛、render farm、檔案寫入範圍 |
| Blender MCP | 對 Blender 暴露工具化操作的第三方／實驗性 MCP 方案；[Blender Lab 說明](https://www.blender.org/lab/mcp-server/) | 未整合，安全審查前不啟用 | 官方頁面說明此 MCP 會將 LLM 生成程式碼傳到 Blender Python Console，且沒有 guardrails；須 sandbox、最小權限、程式碼審查，否則不採用 |
| ComfyUI | 節點式本機生成圖像 workflow；[官方 repository](https://github.com/Comfy-Org/ComfyUI)、[API 範例](https://github.com/Comfy-Org/ComfyUI/blob/master/script_examples/basic_api_example.py) | 未整合 | 固定 commit／模型 hash、license、VRAM、prompt/workflow provenance、權利 gate；不得抓取未授權 checkpoint |
| Cinetic | **依作者指示排除** | 不評估、不安裝、不整合 | 變更此範圍需作者日後明確要求 |
| TTS | **依作者指示排除** | 不評估、不安裝、不整合 | 不呼叫、安裝或連接任何 TTS；真人仿聲另屬高度敏感權利工作，與本次無關 |

截至 2026-10-19 的來源檢視只用來形成候選評估，不代表版本、授權、價格、支援狀況已實測；開始 prototype 時須記錄查閱日期、鎖定版本和測試結果。來源均為官方文件／官方專案頁。
