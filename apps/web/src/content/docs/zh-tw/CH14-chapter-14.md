---
chapter_id: CH14
part_id: P03
title: "分鏡、預視覺化與鏡頭清單"
translation_status: review-needed
revision: 2.1.0-draft
source_chapter: null
---

# 分鏡、預視覺化與鏡頭清單

> 雙語研究草稿；來源定位、校譯、案例觀片、圖稿權利及作者核准待人工審查。

<a id="CH14-S00"></a>
## 本章導讀
分鏡、預視覺化與鏡頭清單將戲劇意圖轉為可討論、排程及拍攝的視覺計畫。分鏡呈現畫面與動作；previs 測試時間、空間與技術條件；鏡頭清單記錄拍攝單位與需求。它們是協作工具，不是不可更改的命令。[R101][R102]

<a id="CH14-S01"></a>
## 學習目標與適用對象
讀者將學會選擇視覺規劃媒介、拆解戲劇節拍、建立鏡頭清單、比較方案對觀眾資訊和資源的影響，並檢查 AI 提案的連續性與可行性。適用導演、攝影、分鏡、美術、剪輯、製片及學習者。

<a id="CH14-S02"></a>
## 先備知識
建議具備場景目標、景別、視點、軸線、場面調度及剪接連續性概念（CH03、CH12、CH13）。不必會畫圖；簡筆圖、平面圖、照片板和文字卡均可溝通。

<a id="CH14-S03"></a>
## 核心術語
分鏡（storyboard）：連續圖格表達構圖、動作及資訊變化的溝通文件。預視覺化（previsualization/previs）：拍攝前測試影像和動作。技術預視覺化（techvis）：檢視攝影機、場地、器材和可行性。鏡頭清單（shot list）：可更新的鏡號、內容、技術需求及狀態紀錄。動態分鏡（animatic）：分鏡圖配暫定時間與剪接的粗剪。[R102][R103]

<a id="CH14-S04"></a>
## 歷史與基本原理
電影製作使用素描、平面圖、文字拆解、攝影草圖和剪接測試溝通畫面，並無各產業通用的單一順序。數位工具方便測試和共享，但不能取代敘事判斷。分鏡讓團隊檢視資訊、節奏、空間和資源，不保證逐格拍攝。[R101]

<a id="CH14-S05"></a>
## 傳統製作方法
導演與編劇先定場景目的、人物目標、轉折及觀眾所需資訊；分鏡師或導演畫關鍵節拍並註明景別、運動、動作、視線和聲音。攝影、美術、特效、剪輯和製片依限制審閱。簡單場景可用縮圖；複雜動作可製作 animatic、3D previs 或 techvis。訪談案例顯示分鏡是思考和溝通工具，現場可調整。[R104][R105]

<a id="CH14-S06"></a>
## AI 時代的技術轉換與限制
生成模型可產生構圖提案、整理描述或建立鏡頭表；3D／即時引擎可檢視空間和攝影機路徑。[R102][R103] 生成圖不能保證跨格人物、道具和時間連續，也無法證明實景安全。輸出標為提案，由人類審查；避免輸入未授權劇本、個資或機密。

<a id="CH14-S07"></a>
## 詳細工作流程
1. 寫場景意圖及觀眾資訊目標。2. 標節拍、轉折、必要動作。3. 列限制、連戲風險和覆蓋需求。4. 畫關鍵格，避免逐句台詞切鏡。5. 標人物、視線、攝影機、方向和聲音。6. 用 animatic 檢查時間。7. 複雜場景做低細節 previs／techvis。8. 鏡頭表列鏡號、場景、景別、運動、內容、設備、特效、風險、負責人、狀態、版本。9. 跨部門確認。10. 現場依安全、表演、天候、預算修訂並留原因。[R102][R106]

![戲劇意圖、分鏡、previs 與鏡頭清單的交接示意。](/images/chapters/CH14/CH14-FIG-001-planning-handoff.svg){#CH14-FIG-001 fig-alt="戲劇節拍經分鏡、previs 成為鏡頭清單；回饋箭頭代表每階段審查。"}
**圖 14-1｜從意圖到拍攝計畫。** 本圖為專案手繪原創示意圖，並非任何電影原劇照或特定作品畫面的重製；權利及出版核准待審。

<a id="CH14-S08"></a>
## 提示詞與技術參數
提示詞指定場景目的、人物位置、動作前後、景別、畫幅、視線、運動、連戲條件、排除項和格式。示例：「六格黑白線稿，原創虛構兩人走廊對話；服裝、門窗、180 度軸線一致；逐格列鏡號、景別、動作、視線、運動和節拍目的；不模仿電影畫面或商標；附可編輯 JSON。」參數只記錄實測工具與版本；不虛構 seed 或 API 欄位。

<a id="CH14-S09"></a>
## 電影案例分析
《三塊廣告牌》（Three Billboards Outside Ebbing, Missouri）：攝影指導 Ben Davis 說導演 McDonagh 事前畫粗略分鏡；拍攝時未必逐格參照，但團隊已有共同理解，顯示分鏡可作溝通而非命令。[R104]《魔宮奇兵》（Indiana Jones and the Temple of Doom）：Spielberg 訪談談以分鏡溝通及剪輯中評估鏡頭資訊量；這是個別案例，不是通用格數規範。[R105] 合法觀看片源版次與時間碼待補。

![三格原創示意分鏡對應鏡頭識別碼。](/images/chapters/CH14/CH14-FIG-002-beats-to-shotlist.svg){#CH14-FIG-002 fig-alt="三格呈現人物進入、注意鑰匙、望向畫外門口；每格對應鏡頭清單編號。"}
**圖 14-2｜節拍轉成可追蹤鏡頭。** 本圖為專案手繪原創示意圖，並非任何電影原劇照或場景重製；權利及出版核准待審。

<a id="CH14-S10"></a>
## 常見錯誤與品質檢查
錯誤：逐句切鏡、缺少戲劇目的、鏡號不一、視線或道具跳變、不可行運鏡、將 previs 當安全審查、AI 偷換角色空間。檢查：逐格寫目的；縮圖看節奏；平面圖核軸線；校驗鏡號和版本；請攝影、製片、特效、安全人員審查；保留修改理由。[R102][R103]

<a id="CH14-S11"></a>
## 練習、評量與延伸研究
用自寫 30–60 秒雙人場景，列四節拍，設計 A 少鏡維持空間、B 以反應鏡頭改變資訊兩套方案。提交 6–10 格分鏡、短 animatic、鏡頭清單及修訂紀錄。評量目的清晰、資訊可讀、空間連續、可行性和交接完整；創意須人工評閱。延伸比較 2D、animatic、3D previs 的溝通成本。

<a id="CH14-S12"></a>
## 參考資料
來源以出版社、製作人員訪談、專業協會及官方軟體文件為主。出版社摘要不等同全書；製作文章不代替合法觀片和時間碼紀錄。參見 R101–R106。

### 來源

- [R101] Bruce Block，《The Visual Story》第 3 版，Routledge（出版社頁，未查全書） — https://www.routledge.com/The-Visual-Story-Creating-the-Visual-Structure-of-Film-TV-and-Digital-Media/Block/p/book/9781315794839
- [R102] Epic Games／Unreal Engine 官方虛擬製作說明 — https://www.unrealengine.com/explainers/virtual-production/what-is-virtual-production?lang=en
- [R103] Blender Manual 官方 Storyboarding 文件 — https://docs.blender.org/manual/en/latest/video_editing/storyboarding/index.html
- [R104] American Cinematographer：Ben Davis 訪談 — https://theasc.com/article/three-billboards-interview-ben-davis/
- [R105] American Cinematographer：Spielberg 訪談重刊 — https://theasc.com/article/spielberg-temple-of-doom/
- [R106] Blender Studio Storyboard 工作流程 — https://studio.blender.org/tools/artist-guide/pre-production/storyboard
