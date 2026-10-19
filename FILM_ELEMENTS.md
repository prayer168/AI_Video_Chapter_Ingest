# 全書共用電影核心元素

> 狀態：V2 整合草案；供章節規劃與交叉引用，不取代電影研究、逐片分析或專業審稿。更新日：2026-10-19（Asia/Taipei）。

本文件定義全書共用的十二個知識分類。每項提供工作定義、雙語術語、原理、技法、適用類型、案例研究入口、AI 轉換、錯誤、品質檢查及依賴關係。概念定義是編輯工作定義，不宣稱唯一理論定義。個別章節須以採用的教材版本／論文 locator 核對；引用中的電影案例只提供研究入口，未完成片段與版本核對前不得寫成完整鏡頭分析。

## 分類與關聯總覽

| ID | 元素（中／英） | 核心問題 | 主要依賴 |
|---|---|---|---|
| FE01 | 故事與劇本 / Story & Screenplay | 事件如何形成可理解、可感受的敘事？ | FE02、FE11、FE12 |
| FE02 | 角色塑造 / Character Development | 角色如何透過目標、選擇和改變成為戲劇行動者？ | FE01、FE09、FE11 |
| FE03 | 導演與敘事 / Directing & Storytelling | 如何把創作意圖轉成全片一致的視聽決策？ | FE01–FE12 |
| FE04 | 攝影 / Cinematography | 如何組織觀看位置、影像空間與攝影機表現？ | FE03、FE05、FE06、FE12 |
| FE05 | 燈光與色彩 / Lighting & Color | 如何以照明、曝光和色彩塑造可讀性、氛圍與連貫？ | FE04、FE06、FE11 |
| FE06 | 美術與場景設計 / Production Design | 如何建立故事所需的物質環境、道具、服裝與視覺系統？ | FE01–FE05、FE11 |
| FE07 | 剪輯與節奏 / Editing & Pacing | 如何選擇、排序與定時聲畫材料？ | FE01、FE03、FE04、FE08、FE12 |
| FE08 | 配樂與音效 / Music & Sound Design | 如何以對白、音樂、效果和空間聲音建構聆聽經驗？ | FE03、FE07、FE09、FE11 |
| FE09 | 表演、對白與聲音 / Performance & Dialogue | 如何讓身體、聲音、語言及沉默承載角色行動？ | FE02、FE03、FE07、FE08 |
| FE10 | 視覺特效與動畫 / VFX & Animation | 如何設計、製作和整合非單純現場攝影取得的動態影像？ | FE04–FE08、FE12 |
| FE11 | 情感與主題 / Emotion & Theme | 作品如何組織價值、情感和詮釋可能？ | FE01–FE10 |
| FE12 | 觀眾體驗 / Audience Experience | 作品如何引導觀眾注意、推論、感受與理解？ | FE01–FE11 |

## 元素規格

### FE01｜故事與劇本 — Story & Screenplay
- **核心概念：** 將人物、事件、時間、因果與資訊安排成可供製作的敘事藍圖；`story`（故事）與 `plot`（情節）須按採用理論分別定義。
- **術語：** 故事 / story；情節 / plot；場景 / scene；節拍 / beat；因果 / causality。
- **原理與技法：** 目標—阻力—選擇；場景目的；資訊揭露；因果／時間結構；劇本格式。技法不是公式，需服務作品形式與類型。
- **類型：** 劇情長短片、紀錄片、動畫、廣告、教育影片皆適用，但非虛構敘事須加入證據與倫理規範。
- **案例入口：** 《羅生門》（R014；多重證詞／觀點，仍須查採用版本及具體場面）。案例待片段定位.
- **AI 實務：** 先輸入創作簡報、受眾、倫理及限制，再由人類確認 beat sheet、劇本版本與權利；不得把模型建議當成事實或觀眾測試。
- **常見錯誤：** 把三幕式當普遍定律、混淆故事與情節、讓提示詞取代因果檢查、使用未授權或私人資料。
- **品質標準：** 人物目標／選擇可追蹤；場景改變資訊或關係；格式與版本有來源；非虛構主張可追溯。
- **依賴：** FE02、FE03、FE11、FE12。

### FE02｜角色塑造 — Character Development
- **核心概念：** 角色由可觀察的行動、關係、欲望、限制與變化構成；人物弧線是分析工具而非必備模式。
- **術語：** 角色 / character；目標 / objective；動機 / motivation；角色弧線 / character arc；人物關係 / character relationship。
- **原理與技法：** 行動與後果、衝突、關係網、角色資訊差、表演細節及反覆意象。
- **類型：** 劇情、動畫、系列、紀錄片人物呈現；紀錄片需區分被攝者真實行為與作者建構。
- **案例入口：** 《羅生門》（R014，觀點與證詞差異）；具體場景待核。
- **AI 實務：** 以 character bible 與關係／狀態表管理一致性；禁止將真實人物敏感特徵推定為角色事實。
- **常見錯誤：** 以標籤代替行動、弧線強迫一致、生成角色前後矛盾、把演員 likeness 當角色設計。
- **品質標準：** 角色決策能由文本證據說明；人物狀態跨場景一致；真實人物材料具同意與來源記錄。
- **依賴：** FE01、FE03、FE09、FE11。

### FE03｜導演與敘事 — Directing & Storytelling
- **核心概念：** 導演統整表演、空間、攝影、聲音、剪輯與美術，使多部門選擇共同實現可說明的敘事意圖。
- **術語：** 導演 / directing；場面調度 / mise-en-scène；走位 / blocking；預視覺化 / previsualization；鏡頭清單 / shot list。
- **原理與技法：** 導演簡報、場景目標、排演、調度、視點策略、跨部門溝通、覆蓋取捨及回看片。
- **類型：** 所有影視類型；工作方式依規模、實拍／動畫及紀錄倫理調整。
- **案例入口：** 《大國民》（R013、R020；BFI 對深焦特定場面的分析）；《十二怒漢》（BFI 逐格分析，正式 reference 待建；只作研究入口）。
- **AI 實務：** 把意圖拆成場景卡、鏡頭規格、表演意圖、風格約束和驗收條件；由導演／作者作最後取捨。
- **常見錯誤：** 將導演等同單一提示詞、缺少排演與連戲計畫、不同部門各自生成而失去整體方向。
- **品質標準：** 每項形式選擇能連回場景意圖；場面可執行；變更有決策記錄。
- **依賴：** FE01–FE12。

### FE04｜攝影 — Cinematography
- **核心概念：** 透過畫框、鏡頭、曝光、焦點、攝影機位置與運動組織影像資訊；技術規格須連結敘事目的。
- **術語：** 構圖 / framing；景別 / shot size；焦距 / focal length；景深 / depth of field；攝影機運動 / camera movement。
- **原理與技法：** 曝光、透視、對焦、鏡頭選擇、畫面比例、機位、運鏡、覆蓋和連續性。
- **類型：** 劇情、紀錄、廣告、直播、動畫／虛擬攝影棚；限制條件不同。
- **案例入口：** 《大國民》（R013、R020；BFI 對深焦特定場面的分析）；《十二怒漢》（新 reference 待建，作封閉空間調度案例）。
- **AI 實務：** Shot Spec 同時記錄意圖、畫面可觀察條件、模型／工具版本與實際輸出差異；不得假稱文字提示可精確控制物理鏡頭。
- **常見錯誤：** 混淆焦距與透視、只描述器材不說目的、提示詞技術參數無實測、鏡頭連續性未檢。
- **品質標準：** 曝光／解析度／幀率符合交付；焦點、構圖、動線和連戲經抽查；生成結果按鏡頭逐項比對。
- **依賴：** FE03、FE05、FE06、FE12。

### FE05｜燈光與色彩 — Lighting & Color
- **核心概念：** 控制光線方向、質地、強度、色彩與曝光，使人物／空間可讀並形成一致視覺策略。
- **術語：** 主光 / key light；補光 / fill light；色彩分級 / color grading；白平衡 / white balance；色彩管理 / color management。
- **原理與技法：** 光比、色溫與光譜、動機光、實景燈、反差、色彩腳本、曝光測試及跨鏡頭匹配。
- **類型：** 劇情、廣告、恐怖、科幻、紀錄、虛擬製作。
- **案例入口：** 《The Taste of Things》（American Cinematographer 色彩製作文章，正式 reference 待新增）；《The Shape of Water》（American Cinematographer 文章，正式 reference 待新增；案例細節須另核）。
- **AI 實務：** 以參考板／色彩腳本和鏡頭級曝光目標描述；生成圖逐鏡量測色彩偏移，人工校色；不得假設模型遵循色彩科學規格。
- **常見錯誤：** 把色彩象徵說成普遍心理定律、混用顯示色域、忽略膚色和字幕可讀性。
- **品質標準：** 色彩空間／白平衡／曝光標示；跨鏡頭連貫；可讀性與輸出端渲染檢驗。
- **依賴：** FE04、FE06、FE11。

### FE06｜美術與場景設計 — Production Design
- **核心概念：** 以場景、道具、服裝、材質、色彩與圖像建立故事世界及製作可行性。
- **術語：** 美術指導 / art direction；製作設計 / production design；場景 / set；道具 / prop；概念設計 / concept design。
- **原理與技法：** 劇本拆解、視覺研究、概念圖、材質板、預算／搭景／外景評估、部門交接與連戲。
- **類型：** 劇情、科幻、歷史、奇幻、動畫、廣告、教育內容。
- **案例入口：** 《Asteroid City》（BFI/Sight and Sound 製作設計訪談，正式 reference 待新增）；《Blade Runner》（BFI 文章，正式 reference 待新增並逐項核實）。
- **AI 實務：** 將可使用的原創 moodboard、尺寸／材質／動線規格餵入可追溯工作流；存 prompt、模型版本、seed（若有）、輸出 hash 和人工修改紀錄。
- **常見錯誤：** 用網路圖直接當出版插圖、只追風格而不檢查尺度／動線、忽略商標及第三方設計相似性。
- **品質標準：** 圖稿與實景／鏡頭設計可對應；尺寸與通行安全可檢；權利欄位完整。
- **依賴：** FE01–FE05、FE11。

### FE07｜剪輯與節奏 — Editing & Pacing
- **核心概念：** 選擇、排列與定時影像／聲音素材，建立時間、空間、注意與敘事關係。
- **術語：** 連續性剪輯 / continuity editing；匹配剪接 / match cut；節奏 / pacing；粗剪 / rough cut；版本 / edit version。
- **原理與技法：** 動作匹配、視線匹配、反應鏡頭、場景節奏、聲音先行／延續、素材整理、版本比較。
- **類型：** 全類型；紀錄片剪輯另需來源、脈絡和被攝者倫理審查。
- **案例入口：** 《哈姆雷特》（Hamlet, 1948；BFI 編輯回憶，正式 reference 待新增）；《十二怒漢》（BFI 逐格分析，正式 reference 待新增）。
- **AI 實務：** 以 EDL／XML／JSON 等明確規格交換素材清單；AI 產生建議而非自動核准剪輯；保留可回復版本和來源片段。
- **常見錯誤：** 將快速等同有節奏、丟失同步／素材來源、模型生成的時間碼未經媒體檢查。
- **品質標準：** 時碼、幀率、音畫同步、剪接點、字幕和交付版本完整；審看片可重現。
- **依賴：** FE01、FE03、FE04、FE08、FE12。

### FE08｜配樂與音效 — Music & Sound Design
- **核心概念：** 組織對白、旁白、音樂、效果、環境聲與空間感，構成具有敘事功能的聲音軌跡。
- **術語：** 聲音設計 / sound design；配樂 / score；音效 / sound effects；擬音 / Foley；聲畫關係 / audiovisual relationship。
- **原理與技法：** 聆聽視點、聲音層次、動機、音樂與效果分工、空間／混響、混音與 loudness 交付。
- **類型：** 全類型；紀錄及新聞需明確標示重建／合成聲音。
- **案例入口：** 《烈火焚身》（Incendies；BFI 對開場音樂與剪接的描述，正式 reference 待新增）；《侏羅紀公園》（Academy 官方摘要，音效與 VFX 教學入口，正式 reference 待新增）。
- **AI 實務：** 使用有授權的聲音來源和工具；保留生成模型、提示、授權條款、stem、取樣率／位深及混音紀錄；聲音合成及仿聲需額外同意審查。
- **常見錯誤：** 把 AI 生成聲音當授權完成、未檢測削波／相位／對白清晰度、聲畫情緒過度說明。
- **品質標準：** 峰值／響度規格依交付平台確認；聲道、同步、噪音與授權清單可查。
- **依賴：** FE03、FE07、FE09、FE11。

### FE09｜表演、對白與聲音 — Performance & Dialogue
- **核心概念：** 演員或受訪者以身體、語音、節奏、姿態及沉默完成角色／人物的可見行動。
- **術語：** 表演 / performance；對白 / dialogue；潛台詞 / subtext；聲音表演 / voice performance；排演 / rehearsal。
- **原理與技法：** 給定情境、行動動詞、聆聽與反應、節奏、走位、連戲、錄音與後期對白。
- **類型：** 劇情、動畫配音、紀錄片訪談、教育演示；被攝者不等同演員，須遵守倫理及知情同意。
- **案例入口：** 《Faces》（BFI 對表演與獨立製作的評論性入口，正式 reference 待新增）；《十二怒漢》（群戲與反應鏡頭入口，正式 reference 待新增）。
- **AI 實務：** 未取得授權不得仿製真實演員／講者聲音或 likeness；劇本表演意圖、聲音克隆、合成字幕需單獨記錄同意和版本。
- **常見錯誤：** 對白只傳資訊、生成語音情緒與角色不合、用剪接掩蓋表演／收音問題。
- **品質標準：** 發音／可懂度、情緒一致、嘴型同步、表演連戲、肖像與聲音同意均人工核驗。
- **依賴：** FE02、FE03、FE07、FE08。

### FE10｜視覺特效與動畫 — VFX & Animation
- **核心概念：** 透過逐格、程序、合成、CG 或生成方法建立／改造動態影像，並與攝影、剪輯、聲音整合。
- **術語：** 視覺特效 / visual effects (VFX)；動畫 / animation；合成 / compositing；追蹤 / tracking；影格 / frame。
- **原理與技法：** 動作設計、時間、關鍵影格、參考影像、鏡頭資料、色彩／透視匹配、合成與版本管理。
- **類型：** 動畫、奇幻、科幻、廣告、紀錄重建、虛擬製作；標示與真實性責任隨用途改變。
- **案例入口：** 《侏羅紀公園》（Academy 官方摘要提及 CG 與 stop-motion 的轉換，正式 reference 待新增）；《Buñuel in the Labyrinth of the Turtles》（BFI 訪談，動畫與再現議題，正式 reference 待新增）。
- **AI 實務：** 以可插拔 adapter 封裝模型；模型、權重、授權、參數和輸出 hash 入檔；圖像／影片素材逐鏡人工驗收；不在本文件授權付費或雲端 API。
- **常見錯誤：** 假設一致性已解決、忽略物理／遮擋／運動連續性、將生成影片誤稱實拍。
- **品質標準：** 尺寸、色彩空間、fps、時間長度、邊緣／遮罩、鏡頭匹配、權利與來源檢查。
- **依賴：** FE04–FE08、FE12。

### FE11｜情感與主題 — Emotion & Theme
- **核心概念：** 主題是作品可支持的價值／觀念組織；情感是觀眾在具體形式、文化和觀看條件下的反應，不可視為普遍可預測。
- **術語：** 主題 / theme；情感 / emotion；母題 / motif；觀眾認同 / audience alignment；情感節點 / emotional beat。
- **原理與技法：** 以選擇、後果、形式重複、聲畫對照、節奏和留白建立多義詮釋。
- **類型：** 全類型，跨文化解讀需說明脈絡與受眾。
- **案例入口：** 《花樣年華》（R018、R021，評論性來源，需具體段落定位）；其他案例須先建立來源與版本 locator。
- **AI 實務：** 模型可以產生詮釋假設，但應標作 hypothesis；以不同讀者回饋、文本證據及作者討論修訂，不把情緒分類當客觀測量。
- **常見錯誤：** 以色彩心理作跨文化定律、把作者意圖等同所有觀眾解讀、將情緒標籤當受眾研究。
- **品質標準：** 詮釋有鏡頭／聲音／敘事證據；不同讀法被保留；受眾研究方法、樣本和限制清楚。
- **依賴：** FE01–FE10、FE12。

### FE12｜觀眾體驗 — Audience Experience
- **核心概念：** 描述觀眾如何接收資訊、定位空間與視點、預測事件並形成理解；觀眾不是同質群體。
- **術語：** 觀眾 / audience；注意 / attention；認知負荷 / cognitive load；敘事資訊 / narrative information；可及性 / accessibility。
- **原理與技法：** 注意引導、資訊排序、節奏、字幕／音訊描述、播放情境與可用性測試。
- **類型：** 電影院、行動短片、教育、直播、互動敘事、無障礙版本。
- **案例入口：** 《大國民》（R013、R020，構圖與深焦作觀眾注意研究入口）；《駭客任務》（BFI 文章，正式 reference 待新增，案例細節待核）。
- **AI 實務：** 產生可讀性檢查清單／多種觀眾假設；需要實際觀眾測試時不可用模型代替人類樣本。
- **常見錯誤：** 把導演意圖當成觀眾必然接收、忽略裝置／字幕／文化差異、以未記錄樣本的 AI 評分宣稱受眾效果。
- **品質標準：** 受眾與播放場景明確；字幕、對比、音量和可及性實測；研究結論記錄樣本與方法。
- **依賴：** FE01–FE11。

## 案例來源台帳與待辦

下列來源是專業案例入口，不是免除看片、版本定位或逐主張查證的替代品。搜尋日期 2026-10-19；應把使用來源的完整書目與 locator 正式登錄 `data/references.yaml` 後才放入正式章稿。

| 來源入口 | 支持範圍 | 限制 |
|---|---|---|
| [BFI: Citizen Kane](https://www.bfi.org.uk/film/f4c92833-af39-5cd6-a41e-8df5933d0dc1/citizen-kane)；R013 | 電影基本資料及 BFI 所列特徵 | 精確場面、版本、timecode 待看片核實 |
| [BFI: 20 Inspired Visual Moments in Citizen Kane](https://www.bfi.org.uk/features/20-inspired-visual-moments-citizen-kane)；R020 | 特定深焦場面評論 | 評論不是原始製作紀錄；逐格定位待核 |
| [BFI: Where to Begin with Akira Kurosawa](https://www.bfi.org.uk/features/where-begin-with-akira-kurosawa)；R014 | 《羅生門》多重證詞／觀點分析入口 | 作者、日期、片段定位待補 |
| [BFI: A City of Sadness](https://www.bfi.org.uk/film/989a6349-4d1c-54da-8ea1-0abd2a558d8a/a-city-of-sadness)；R015 | 基本資料與背景 | 不支撐未經核實的鏡頭美學主張 |
| [Criterion: In the Mood for Love](https://www.criterion.com/films/198-in-the-mood-for-love)；R018；[Notes on In the Mood for Love](https://www.criterion.com/current/posts/7976-notes-on-in-the-mood-for-love)；R021 | 片目及評論性形式分析 | 評論需與影片材料區分 |
| [Yi Yi: Time and Space](https://www.criterion.com/current/posts/429-yi-yi-time-and-space)；R019 | 評論性構圖／空間分析 | 二手評論，鏡頭定位待核 |
| [BFI: The Matrix](https://www.bfi.org.uk/features/matrix-wachowskis-keanu-reeves) | 導演／設計／效果／產業評論入口 | 須登錄新 reference ID；不將評論當作原始製作檔案 |
| [BFI: Asteroid City production design](https://www.bfi.org.uk/sight-and-sound/features/pictures-how-west-was-done-wes-anderson-asteroid-citys-production-design) | 導演及製作設計師談視覺研究與場景 | 訪談／評論來源，需記錄作者與定位 |
| [ASC: The Taste of Things color](https://theasc.com/article/the-taste-of-things-color/)；[ASC: John Wick Chapter 3](https://theasc.com/article/john-wick-chapter-3-slayin-in-the-rain/) | 攝影師／調光師關於色彩、燈光流程的訪談 | 個案不是通用規則；技術規格按來源逐項引用 |
| [BFI: How 12 Angry Men works](https://www.bfi.org.uk/features/how-12-angry-men-works-25-frames) | 以畫格分析一場對話片中的構圖、光線、剪接與張力 | 評論性逐格分析；若用於教材，需核對採用版本與 locator |
| [BFI: Tales of a film editor — Hamlet](https://www.bfi.org.uk/features/tales-film-editor-making-olivier-hamlet) | BFI 保存的剪輯師回憶錄節錄及剪接工作 | 第一人稱回憶，勿視為普遍剪輯規則 |
| [BFI: Faces and independent filmmaking](https://www.bfi.org.uk/features/john-cassavetes-faces-indie-filmmaking) | 《Faces》製作背景、表演及低預算工作方式 | BFI 二手回顧；製作細節仍須比對原始訪談／檔案 |
| [BFI: The Matrix](https://www.bfi.org.uk/features/matrix-wachowskis-keanu-reeves) | 電影形式及產業影響的評論性入口 | 需逐項查片與來源，不推論普遍因果 |
| [BFI: Buñuel in the Labyrinth of the Turtles](https://www.bfi.org.uk/interviews/how-we-animated-luis-bunuel-making-bunuel-labyrinth-turtles) | 導演訪談中的動畫再現觀點 | 訪談需與影片材料及其他研究交叉核對 |
| [BFI: Lynne Ramsay’s visual world](https://www.bfi.org.uk/features/lynne-ramsay-you-were-never-really-here) | 導演作品中的視聽風格分析入口 | 評論性分析，需明確區分作者觀察與可直接觀察事實 |
| [Academy: Jurassic Park](https://www.oscars.org/events/jurassic-park) | Academy 對影片聲音與視覺效果的簡介 | 官方簡介不是完整製作史 |
| [BFI: Olivier’s Hamlet editing](https://www.bfi.org.uk/features/tales-film-editor-making-olivier-hamlet) | 編輯回憶及剪接決策 | 回憶錄節錄，需標示第一人稱來源 |
| [Academy: Jurassic Park](https://www.oscars.org/events/jurassic-park) | Academy 對聲音、效果及 CG 製作史的摘要 | 官方活動摘要非完整製作檔案 |
| [BFI: Buñuel in the Labyrinth of the Turtles](https://www.bfi.org.uk/interviews/how-we-animated-luis-bunuel-making-bunuel-labyrinth-turtles) | 導演訪談、動畫與再現 | 訪談主張需由影片及其他來源交叉核對 |

## AI 時代的共通工作單

每一章引用本分類時，在章節 metadata 或研究卡補列 `film_element_ids`、`source_ids`、案例片名／版本／觀看合法來源／片段 locator、主張類型、模型／工具版本（若有）和測試證據。影像生成結果、模型解讀與示例提示詞均標成示範或假設，除非有可重現實測記錄。

