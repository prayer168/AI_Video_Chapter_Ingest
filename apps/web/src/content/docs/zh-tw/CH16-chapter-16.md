---
chapter_id: CH16
part_id: P04
title: "曝光、感光元件與影像形成"
translation_status: review-needed
revision: 2.1.0-draft
source_chapter: null
---

<!-- CH16 V2.1.0 research draft. Technical, bilingual, source-locator, rights, and author reviews remain open. -->

# 曝光、感光元件與影像形成

## 本章範圍與狀態

本章說明場景光線如何經由電影底片或數位感光元件形成可記錄的影像，以及攝影組如何將曝光意圖轉成可檢查的設定。重點是曝光量、感光材料反應、感光元件讀出、曝光指數、動態範圍、監看與紀錄。鏡頭透視、焦距、光圈的景深效果及完整色彩管理另見 CH17、CH18、CH20；本章只在曝光控制所需範圍提及。本文是可追溯來源支持的教學草稿，不等同攝影機操作手冊、校準程序或特定器材建議。所有數值和功能須依實際機型、韌體、記錄格式及測試結果確認。

<a id="CH16-S01"></a>
## Learning objectives
完成本章後，讀者應能：

1. 區分曝光、曝光指數（EI）、ISO 標示、監看亮度與後期調整各自代表的事情。
2. 描述底片感光乳劑與數位影像感光元件從受光至成像的主要步驟，並指出兩者不能簡化為完全相同的曲線或工作流程。
3. 用場景亮度、光圈、快門／曝光時間、ND、照明與 EI 的關係，規劃可檢查的曝光方案。
4. 使用測光表、灰卡、波形圖、斑馬紋或 false color 等輔助工具交叉檢查，而不將單一監看提示當作普遍安全界線。
5. 記錄曝光決策、影格率、快門角度、EI、ND、照明及參考監看條件，讓攝影、DIT 與後期能追溯素材。
6. 辨認 AI 生成畫面中的「曝光」描述與實際感光曝光的差別，並把模型輸出視為需人工驗證的視覺假設。

先備知識：建議了解光圈、快門、影格率、測光、灰階、影像訊號與基本攝影機操作；若尚未熟悉鏡頭光學，可先讀 CH17。術語翻譯及設備差異仍待攝影專業與雙語編輯審查。

<a id="CH16-S02"></a>
## Prerequisites
建議先閱讀 CH02（鏡頭與觀看位置）、CH17（構圖、透視、焦距與景深）及 CH20（色彩管理與攝影工作流）。本章的「曝光」是記錄介質接收的光及其造成的訊號，不是把監看螢幕調亮。若使用測光表或示波器，須確認測光表校準、攝影機 EI／ISO 設定、記錄曲線、LUT、監看亮度與訊號範圍。底片 EI 牽涉底片感光度、曝光方法及沖洗條件；數位機的 EI、ISO、增益、RAW／編碼格式如何互動則依廠商設計而異。不可把某台機器的基準 EI 或 false color 區域直接移植到其他機型。

<a id="CH16-S03"></a>
## Key terms
| 中文 | English | 本章工作定義 | 狀態 |
|---|---|---|---|
| 曝光 | exposure | 光在一定時間內作用於感光材料或感光元件所形成的記錄條件；在電影攝影中須同時說明場景照度、曝光時間及影像系統的測光／感光設定。 | 草案 |
| 曝光指數 | exposure index (EI) | 用以表示曝光／感光度參照的設定或標示；底片 EI 與數位攝影機 EI 的實作與意義不可逕行等同。 | 草案 |
| 感光度標示 | speed rating / ISO rating | 按指定標準或廠商方法描述感光材料／系統響應的標示；不代表任意提高數值就增加到達感光面上的光子。 | 草案 |
| 感光元件 | image sensor | 將入射光轉成電荷或電子訊號，再由讀出與影像處理鏈轉為影像資料的器件。 | 草案 |
| 光電二極體 | photodiode | 感光元件中吸收光並產生電荷的光敏結構；實際像素電路會因架構而不同。 | 草案 |
| 動態範圍 | dynamic range | 成像系統在可接受品質下同時記錄暗部至亮部的範圍；數值依定義、噪訊門檻、記錄格式與測試方法而異。 | 草案 |
| 飽和／剪裁 | saturation / clipping | 訊號到達系統可表示或可區分的上限後，更多入射光不再帶來可分辨的亮部資訊；顯示端的剪裁也可能與感光元件飽和不同。 | 草案 |
| 訊噪比 | signal-to-noise ratio (SNR) | 有用影像訊號相對於噪訊的比值；應標明量測條件，不用單一數值概括不同亮度、色彩通道與處理階段。 | 草案 |
| 感光測定 | sensitometry | 研究感光乳劑或感光材料對受控曝光的反應；底片特性曲線呈現曝光與處理後密度的關係。 | 草案 |
| 特性曲線 | characteristic curve | 顯示感光材料曝光量與處理後影像密度關係的曲線；數位 Log 編碼與底片密度曲線不能視為同一物理量。 | 草案 |
| 快門角度 | shutter angle | 以角度表示每一影格的曝光時間；對 ARRI ALEXA LF 手冊所列關係，曝光時間（秒）＝角度 ÷（360 × 感光影格率）。 | 草案 |
| 曝光寬容度 | exposure latitude | 曝光偏離參考值後仍可接受地重現影像的範圍；須指明底片、數位機、調色／觀看條件及「可接受」標準。 | 草案 |

詞條為本章工作定義，已連結 R112–R118；術語範圍、繁中用語及英文一致性仍待人工審查。

<a id="CH16-S04"></a>
## History and principles
電影攝影的影像形成，早期依賴感光底片：鏡頭形成的光學影像使乳劑發生化學變化，留下不可直接觀看的潛影；沖洗後形成負片密度，再經印片或掃描成為可觀看、可剪輯的材料。Kodak 的電影製作參考指南將電影史、底片結構、感光測定、曝光工具、沖洗和數位工作流分章說明，也提醒底片攝影的影像形成和後續處理是相連流程 [R112]。Kodak 術語表將曝光描述為光量與作用時間的關係，並將特性曲線界定為曝光與處理後密度之關係 [R115]。這些是廠商的技術教學定義；本章仍需攝影與影像科學專業者覆核。

電子影像感光元件則將光轉成電訊號。諾貝爾獎對 CCD 的圖文說明記載 Boyle 與 Smith 於 1969 年提出 CCD 影像感測技術，並概述光電轉換與讀出概念 [R117]。Sony Semiconductor 的說明比較 CCD 與 CMOS 讀出架構，並記錄其自身 CMOS 技術發展節點；這是 Sony 對自家技術的歷史與產品敘述，不可延伸成所有產業的唯一發展史 [R118]。Sony 另指出其列並行 A/D 轉換器如何在特定感光元件架構中協助高速讀取並降低類比傳輸噪訊 [R114]。

底片特性曲線描述處理後密度對曝光的反應；數位感光元件輸出則會經讀出、類比／數位轉換、色彩濾光陣列解碼（如適用）、降噪、色彩轉換或 Log 編碼等處理。兩條流程可能在影像呈現上有相似語言，卻不是相同的化學或電子機制。ARRI 的影像科學問答指出 Log C 編碼的傳遞特性與底片負片掃描相似，同時明確說明兩者色彩特性仍有差異 [R119]。本章以「相似之處可作為視覺溝通，不等於感測原理相同」作為教學界線。

<a id="CH16-S05"></a>
## Traditional production practice
### 先界定希望保留的資訊

曝光決策從場景需求開始：觀眾必須看見哪些暗部細節？亮部是否需要保留窗外資訊、反光或燈具核心？是否希望人物臉部、背景或實景燈具成為測光參照？曝光不是追求每一區域都亮度平均，也不是所有亮部都必須不剪裁；而是讓預定的影像層次落在媒介可記錄、調色可處理、呈現可讀的範圍內。場景反差若大於系統可用範圍，需在照明、反光／遮光、ND、場景調度、拍攝時間或後期預期之間取捨。

### 以工具交叉檢查

- **入射式測光表**估算落在被攝體上的光；**反射式測光表**讀取被攝場景反射回來的光。兩者量測對象不同，須依測光表說明、校準及預定影調判斷。
- **灰卡**可建立曝光、白平衡或後期參照，但需明確記錄卡片、光線及鏡頭／濾鏡等條件。不可假設灰卡所在位置代表整個場景的平均值。
- **波形圖／直方圖**協助查看記錄訊號分布；監看 LUT、色彩空間、範圍設定或外接設備可能改變顯示。以機內記錄訊號和校準監看為準。
- **斑馬紋與 false color**是可配置的監看輔助。ARRI 動態範圍白皮書的色彩區域及 18% 灰設定是 ARRI ALEXA／Log C 系統的說明 [R113]，不是通用色碼或所有攝影機的飽和門檻。
- **曝光紀錄**至少包括場景／鏡號、機身及韌體、影格率、快門角度或時間、EI／ISO／增益、光圈、ND、白平衡、記錄格式／曲線、監看 LUT、測光方式、灰卡／參照物、特殊燈光與變更理由。

<figure id="CH16-FIG-001"><img src="/images/chapters/CH16/CH16-FIG-001-image-formation-pipeline.svg" alt="雙欄流程圖比較電影底片與數位感光元件的受光、訊號形成、處理及交付路徑，並標示兩者不可直接等同。" /><figcaption>圖 16-1｜底片與數位影像形成路徑。</figcaption></figure> 本圖為本專案手繪原創技術示意圖，依 R112、R114、R117–R118 的文字資料自行繪製，未使用第三方圖片；不是任何電影劇照，也不代表所有相機架構。圖稿、可及性、相似性、署名與出版權利待人工審查。

<a id="CH16-S06"></a>
## AI-era workflow and limits
AI 影像工具可能把「過曝」「低調」「電影感高光」當成文字條件或生成控制，但同一詞句不代表感光元件接收了特定曝光量，也不保證輸出遵循某台攝影機的 EI、Log 曲線、曝光時間或噪訊特性。不同模型、版本與介面可能把提示詞轉成不同視覺結果；未有官方文件或可重現實測時，必須標示為生成假設，不把它寫成工具功能。

AI 可協助建立鏡頭曝光紀錄表、依使用者提供的場景亮度條件列出待測方案、將元資料整理為 JSON、協助比較不同曝光測試格，或提出可能需要檢查的高光／暗部位置。不得讓模型自行補造攝影機中繼資料、判定底片沖洗結果、以生成畫面代替測光，或把影像辨識對「剪裁」的判斷當成原始檔訊號證據。使用含演員或未公開素材的工具前，須先核對資料權限、隱私與服務條款。

本章示範資料格式僅供專案內測，非任何攝影機的官方 metadata schema。所有輸出應保留模型名稱／版本、日期、提示詞、輸入權利、人工修改與實測證據；未能確認則填 `unknown`，不要推測。

<a id="CH16-S07"></a>
## Step-by-step workflow
1. **寫下影像意圖**：標註希望保留的高光、暗部、人物膚色與場景參照；指出哪些區域可有意剪裁。
2. **盤點場景反差**：用測光、灰卡、波形或攝影機測試估計最亮與最暗的重要細節；記錄量測方式與監看轉換。
3. **鎖定運動條件**：確定影格率、快門角度／時間及運動模糊需求。只在分鏡與測試允許時變更快門，並留意照明閃爍及動作呈現。
4. **選擇媒介及記錄格式**：記錄底片乳劑及 EI／沖洗方案，或數位機身、韌體、記錄格式、Log／RAW 選項與廠商適用說明。
5. **設定光量控制**：依景深與鏡頭需求設定光圈；以 ND、照明、遮光、反光及場景安排控制到達感光面的光。光圈對景深的取捨詳見 CH17。
6. **建立 EI／測光參照**：把 EI／ISO 設定、測光表設定與攝影機文件核對；若測試 EI 偏移，記錄參照灰與高光／暗部後果。EI 設定本身不等於額外光子。
7. **拍攝測試格**：對有疑問的主體與關鍵光源拍攝包圍測試或灰卡／色卡測試；場景安排、曝光變化量和記錄格式由攝影師制定，不採通用固定步長。
8. **機內監看並回查**：查看波形、斑馬紋／false color、剪裁提示及錄製測試；以攝影機原始檔或可信監看輸出確認，不只依賴螢幕觀感。
9. **同步紀錄**：更新 camera report／metadata，將曝光設定和特別變更通知 DIT、場記及後期；若拍 RAW，照該機格式與廠商流程管理可調 metadata。
10. **日終與後期驗證**：核對素材、代理檔、LUT、色彩空間標記與曝光筆記；以校準監看及一致的顯示條件檢查高光、暗部、噪訊與畫面匹配。

<a id="CH16-S08"></a>
## Prompt and technical parameters
### 曝光測試規劃提示詞（示範內容）

```text
任務：依我提供且有權使用的拍攝條件，整理曝光測試計畫草案；不得聲稱已替我測光或確認任何相機功能。
專案／場景／鏡號：{識別碼}
攝影機、韌體與記錄格式：{實測或官方資料；未知填 unknown}
底片乳劑／批次／沖洗方式（若適用）：{資料}
影格率、快門角度／時間：{值與單位}
EI／ISO／增益：{值、設定位置及來源}
重要高光與暗部：{由攝影師指定}
測光工具、校準／參照灰、監看 LUT：{資料}
輸出：1. 已知事實與來源 2. 待實測假設 3. 測試格方案 4. 每格記錄欄位
5. 需檢查的剪裁／噪訊／閃爍／連戲風險 6. 對 DIT／後期的交接問題。
限制：不預設通用 EI、false-color 門檻、感光度或最佳曝光；不補造 metadata；模型建議均標記「待實測」。
```

### 通用拍攝紀錄 JSON 範例（示範 schema，非相機原生格式）

```json
{
  "schema_version": "1.0-draft",
  "chapter_id": "CH16",
  "shot_id": "SCENE-SHOT",
  "camera_model": "unknown",
  "firmware": "unknown",
  "recording_format": "unknown",
  "frame_rate_fps": null,
  "shutter_angle_degrees": null,
  "exposure_time_seconds": null,
  "ei_or_iso": null,
  "aperture_t_stop": null,
  "nd_filter": "unknown",
  "metering_method": "unknown",
  "reference_card": "unknown",
  "monitor_transform_lut": "unknown",
  "highlight_priority": "operator-defined",
  "notes": "Fill with measured data; do not infer missing camera metadata."
}
```

如使用快門角度表示曝光時間，可依 ARRI ALEXA LF SUP 4.0 使用手冊所列公式計算：角度 ÷（360 × 感光影格率）[R116]。例：該公式在 24 fps、180° 下為 1/48 秒，這只是算式示範，不是本章推薦設定；不同攝影機可能有可選角度、電子快門讀出與防閃爍限制。ALEXA LF 手冊另說明 EI 使用 ASA 標示、其基準感光度和 ARRIRAW EI 行為，均限於該機型／手冊版本 [R116]。

<figure id="CH16-FIG-002"><img src="/images/chapters/CH16/CH16-FIG-002-exposure-decision-workflow.svg" alt="流程圖從敘事優先事項開始，經場景反差與拍攝條件，進入測量、測試、訊號驗證與拍攝紀錄。" /><figcaption>圖 16-2｜曝光決策與驗證工作流。</figcaption></figure> 本圖為本專案手繪原創技術示意圖，以本章工作建議為依據；不是電影畫面，也不是特定器材的操作順序。技術、可及性、權利及出版核准待人工審查。

<a id="CH16-S09"></a>
## Shot / film case study
### 技術案例一：Kodak 底片感光測定與特性曲線

Kodak《Essential Reference Guide for Filmmakers》將「Basic Sensitometry and Characteristics of Film」列於底片原理部分，並另列曝光、測光工具及沖洗流程 [R112]。Kodak 術語表把特性曲線描述為感光材料曝光與處理後密度的關係，並定義曲線的 toe、直線區及 shoulder [R115]。教學上可將其用來理解：增加曝光會改變底片的潛影與沖洗後密度；底片曲線的肩部如何呈現高光，需連同底片種類、處理與印片／掃描條件閱讀。不可把這條密度曲線直接當成數位攝影機的 Log waveform。

**練習分析**：用一張自行繪製、不模仿廠商原圖的示意曲線標出 toe、直線區與 shoulder；在旁邊列出「物理量」「實驗條件」「可支持的結論」。將高光肩部與數位感光元件飽和區比較時，先說明兩者量測量不同。這是基於 Kodak 教材的教學轉譯，不是特定電影鏡頭案例。

### 技術案例二：ARRI ALEXA 曝光指數與動態範圍說明

ARRI《Dynamic Range – White Paper》說明其 ALEXA 的曝光、ND、光圈及快門時間如何影響感光元件訊號，並指出該系統的 EI 會選擇 Log C 影像及監看影像中何者作為中灰參照；白皮書特別列出以 false color／灰卡檢查訊號的方法 [R113]。同一文件提醒，當場景反差超過攝影機動態範圍時，攝影師須選擇優先保留高光或暗部；ARRIRAW 後期 EI 行為也只適用於文件指明的格式與相機情境 [R113]。這是廠商系統文件與技術案例，不代表所有相機 EI 行為一致。

**練習分析**：以一個自設的窗邊人物場景，列出「不改光線」「補暗部」「降低曝光保高光」三種可測方案。對每種方案列出感光元件訊號、監看亮度、暗部噪訊／高光飽和的預期變化，再實際拍攝比較。這個場景為假設練習，不是任何電影案例。

**觀片／電影案例待辦**：目前沒有完成合法版本觀片、鏡頭時間碼與製作來源定位的具體電影片例。本章不虛構片名、版本、時間碼或攝影師意圖；作者／研究編輯可選擇可合法觀看、適合分析曝光策略的電影場景，完成記錄後再補入。

<a id="CH16-S10"></a>
## Common errors and quality checks
| 常見錯誤 | 可能後果 | 檢查／改善 |
|---|---|---|
| 把提高 EI／ISO 說成感光面收到了更多光 | 混淆光量與監看／曝光參照，誤判噪訊與高光餘裕 | 記錄光圈、ND、快門、照明與格式；以機型手冊和實拍對照 |
| 用顯示器亮度判斷原始素材曝光 | 不同 LUT、亮度及訊號範圍造成錯判 | 查看記錄訊號、校準顯示與色彩管理，保留 LUT metadata |
| 把某台機器的 EI、灰卡位置或 false color 門檻套用到其他機型 | 可能造成錯誤曝光或高光剪裁 | 每次標明型號、韌體、Log 版本與監看設定；按官方手冊驗證 |
| 只看平均測光值，忽略關鍵高光／暗部 | 故事資訊消失或主體層次不符意圖 | 明列優先資訊，量測關鍵區域並拍測試格 |
| 以底片特性曲線代替數位 Log 曲線 | 混淆密度、電子訊號與編碼數值 | 清楚標記物理量、階段與媒介；分開繪圖和解釋 |
| 忽略感光時間與照明閃爍 | 亮度／色彩不均、條紋或動作呈現偏差 | 依市電頻率、燈具調光方式、快門與影格率實測 |
| AI 替缺失資料補上攝影機、EI 或光圈 | 假 metadata 導致錯誤交接 | 缺值標 `unknown`；核對原始檔、場記、camera report 與官方文件 |

章末可自動或人工驗收：每個技術主張有來源或明確標為實務建議；兩語段落與術語對齊；設備規格均附機型／版本；JSON 語法有效且未知值不捏造；圖檔與 hash 一致、圖說與 alt 齊備；網站和出版草稿可重建。藝術曝光意圖、膚色觀感、底片／數位匹配與權利狀態仍需人類判斷。

<a id="CH16-S11"></a>
## Exercises, assessment, and research
1. 畫出底片和數位感光元件各自的影像形成流程，標記受光、轉換、處理、記錄和顯示階段；說明哪些步驟只屬特定媒介。
2. 以同一場景設計三組曝光測試，分別優先保留高光、暗部及參考中灰；描述所改設定和不應一起改動的變因。
3. 用實際攝影機手冊查出影格率、快門角度、EI 與記錄格式的語意及可選值。引用手冊版本、章節／頁碼，不以網路討論替代官方規格。
4. 建立一份拍攝報告，至少含本章 JSON 欄位；拍攝／研究條件未提供的欄位保留 `unknown`。
5. 對一段合法取得的電影或自攝素材，記錄版本／來源與時間碼，分析曝光如何支援敘事資訊；不要只以畫面「明暗」推定攝影師意圖。
6. 延伸研究：比較感光測定文獻中的底片密度曲線與數位相機的量測方法，明確說明測試條件、噪訊定義、色彩通道及可比較範圍。

評量重點是媒介區分、來源可追溯、技術條件完整、測量與觀察分開、決策理由清楚。視覺風格偏好屬主觀評價，由電影攝影專業者審查，不以自動化測試代替。

<a id="CH16-S12"></a>
## References
- [R112] Eastman Kodak Company, *The Essential Reference Guide for Filmmakers*. Kodak, “Basic Sensitometry and Characteristics of Film” pp. 49–55；“Exposing Film” pp. 109–114；“Exposure Tools” pp. 115–122。官方 PDF；查閱日期：2026-10-23。<https://www.kodak.com/content/products-brochures/Film/kodak-essential-reference-guide-for-filmmakers.pdf>
- [R113] ARRI, *Dynamic Range – White Paper*, 2022-09-28, PDF pp. 13–18（曝光、EI、false color、動態範圍與曝光寬容度）；範圍限於文件討論的 ALEXA／Log C 系統。查閱日期：2026-10-23。<https://www.arri.com/resource/blob/295460/e10ff8a5b3abf26c33f8754379b57442/2022-09-28-arri-dynamic-range-whitepaper-data.pdf>
- [R114] Sony Semiconductor Solutions Group, “Column-Parallel A/D Conversion Circuit,” overview and technical features；廠商技術說明，適用範圍限於該頁所述架構。查閱日期：2026-10-23。<https://www.sony-semicon.com/en/technology/is/columnad.html>
- [R115] Eastman Kodak Company, “Glossary of Motion Picture Terms,” entries “Exposure,” “Exposure Index,” “Characteristic Curve,” “Toe,” “Straight-Line Region,” “Shoulder,” and “Sensitometry.” Official glossary；查閱日期：2026-10-23。<https://www.kodak.com/en/motion/page/glossary-of-motion-picture-terms/>
- [R116] ARRI, *ALEXA LF User Manual, Software Update Package 4.0*, “Camera Controls,” p. 59；“Shutter,” pp. 66–67。機型／手冊版本特定；快門角度公式、ASA/EI 設定與 ARRIRAW 限制不得普遍化。查閱日期：2026-10-23。<https://www.arri.com/resource/blob/147832/ccb47e7386f7e1f9161a885bf42781a0/arri-alexa-lf-user-manual-sup-4-0-data.pdf>
- [R117] Nobel Prize Outreach, “The Nobel Prize in Physics 2009 — Illustrated Information,” CCD image-sensor description and Boyle/Smith chronology；Nobel Prize 2009 background. 查閱日期：2026-10-23。<https://www.nobelprize.org/prizes/physics/2009/illustrated-information/?print=1>
- [R118] Sony Semiconductor Solutions Group, “Common Technology of Image Sensors,” CCD/CMOS descriptions and Sony technology chronology. 公司自述，技術史範圍限於頁面所列 Sony 技術與產品。查閱日期：2026-10-23。<https://www.sony-semicon.com/en/technology/is/index.html>
- [R119] ARRI, “Visual Effects FAQ,” “What is the Log C format?” 官方影像科學 FAQ；Log C 與底片掃描的相似性只作編碼／傳遞特性類比，頁面並指出色彩特性仍不同。查閱日期：2026-10-23。<https://www.arri.com/en/learn/camera-systems/image-science/vfx-faq>

## Chapter status

繁體中文研究草稿與英文工作譯稿已依相同 S01–S12 結構建立；八項來源、十二個雙語術語與兩張原創可編輯 SVG 已登錄。作者、攝影／影像科學專業、英語校譯、來源定位、案例觀片與時間碼、圖稿技術／可及性／相似性／權利審查尚未完成。此章不是正式出版成品。
