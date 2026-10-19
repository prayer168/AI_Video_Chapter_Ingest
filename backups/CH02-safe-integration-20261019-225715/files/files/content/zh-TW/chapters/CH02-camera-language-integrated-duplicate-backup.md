---
chapter_id: CH02
part_id: P01
locale: zh-TW
lang: zh-TW
title: "AI 電影製作聖經｜第二章"
slug: camera-language
book_title: AI 電影製作聖經
registry_title: "鏡頭、場面與剪接：電影語言的基本單位"
working_subtitle: "鏡頭景別、構圖與攝影機語言：從導演意圖到 AI 可操作、可驗證的鏡頭規格"
translation_status: review-needed
editorial_status: draft-for-human-review
canonical_status: draft-migration-pending
revision: 2.1.0-draft
source_legacy: chapters/01-02-camera-language.md
source_archive: chapters/source-packs/AI-Filmmaking-Bible-CH02-Codex.zip
source_archive_sha256: d448defde21abe8802ad87684928eaade0f7c39101b423159073391457a519a5
last_updated: 2026-10-18
claim_types: [verified-fact, theory, practice, ai-hypothesis, demo]
related_chapters: [CH01]
---
# CH02｜鏡頭、場面與剪接：電影語言的基本單位 {#CH02}

> 編輯註：來源稿副標題為「鏡頭景別、構圖與攝影機語言」；與全書 registry 題名之差異待編輯確認。

副標題：從導演意圖到 AI 可操作、可驗證的鏡頭規格

> 內容標記：本章中的電影史敘述以來源支持；術語與原理屬專業概念整理；流程與品質建議屬實務建議；提示詞和科普短片均為示範內容，尚無生成實測。
>
> 核心命題：鏡頭不是「拍得好看」的選擇，而是決定觀眾距離人物有多近、知道多少資訊、看向哪裡，以及在多長時間內建立何種感受的敘事行為。

**讀者定位**：已有基本剪輯概念、希望系統化掌握電影攝影與 AI 動畫製片的創作者、教師及技術人員。

**本章使用方式**：先學術語與原理，再做「同一場景不同景別」實驗；最後把導演意圖轉換為 Shot Spec、Prompt、生成素材和品質評估。文中的 AI 控制語句是目標描述，不保證模型按照物理攝影機精確執行。

## 本章摘要 {#CH02-S00}

本章建立從敘事意圖到可拍攝／可生成鏡頭規格的轉換方法，涵蓋景別、構圖、攝影角度、焦距、透視、景深、運鏡與跨鏡頭連續性。讀者將以傳統攝影工作流程為基準，再將可觀察的鏡頭要求寫成提示詞與 Shot Spec，並用可檢查的畫面證據驗收。AI 提示詞是意圖描述，不構成物理相機控制或生成成功的保證。

## 先備知識 {#CH02-S02}

- 建議具備基本剪輯與鏡頭概念；無需先備攝影器材操作經驗。
- 了解場景、鏡頭、畫格與時間碼等基本詞彙有助於完成本章實作。

## 學習成果 {#CH02-S01}

完成本章，應能：
1. 選擇並解釋 EWS、WS、FS、MS、MCU、CU、ECU 等景別。
2. 區分景別、構圖、攝影機角度、焦距、攝影機距離與景深。
3. 解釋透視的主要決定因素，以及 Dolly 與 Zoom 的差異。
4. 比較 Pan、Tilt、Truck、Dolly、Pedestal、Crane、Orbit、Handheld 與 Locked-off。
5. 使用視線、180 度軸線、Headroom、Lead Room 和 連續性原則設計跨鏡頭空間。
6. 為鏡頭建立可傳入 Codex 的 JSON 規格與驗收標準。
7. 製作 30–60 秒示範短片並提交反思與評量。

## 核心術語及中英文對照 {#CH02-S03}

定義是工作稿；景別邊界會隨製作語境而變，出版前需由攝影／電影教育編輯審校。焦距、透視與景深依光學條件使用，不以生成模型的文字提示代替實測。[R027][R028]

| Term ID | 繁體中文 | English | 繁中工作定義 | English working definition |
|---|---|---|---|---|
| `TERM-CH02-EWS` | 極遠景 | Extreme Wide Shot (EWS) | 人物相對於環境極小、環境資訊主導的取景尺度。 | A framing scale in which the subject is very small relative to the environment. |
| `TERM-CH02-WS` | 遠景 | Wide Shot (WS) | 呈現人物全身或大部分身體及周遭空間的取景。 | A framing that shows a person’s full or most of their body with surrounding space. |
| `TERM-CH02-FS` | 全身景 | Full Shot (FS) | 通常讓人物頭至腳完整入畫；實際邊界依場景與慣例而異。 | A framing that generally includes the full body, with conventions varying by context. |
| `TERM-CH02-MLS` | 中遠景 | Medium Long Shot (MLS) | 人物約膝上或相近範圍的取景；非跨製作通用的硬邊界。 | A framing often around the knees upward; boundaries are not universal. |
| `TERM-CH02-MS` | 中景 | Medium Shot (MS) | 通常約腰部以上，兼顧表情、手勢與部分環境。 | Often frames roughly from the waist up, balancing expression, gesture and context. |
| `TERM-CH02-MCU` | 中近景 | Medium Close-Up (MCU) | 多以胸部以上呈現人物表情與有限環境。 | Often frames a person from the chest up with limited context. |
| `TERM-CH02-CU` | 特寫 | Close-Up (CU) | 使臉部或重要物件成為畫面主要資訊。 | A framing that makes a face or important object the primary visual information. |
| `TERM-CH02-ECU` | 大特寫 | Extreme Close-Up (ECU) | 只呈現臉或物件很小的局部細節。 | Shows only a very small detail of a face or object. |
| `TERM-CH02-OTS` | 越肩鏡頭 | Over-the-Shoulder (OTS) | 以前景人物肩部或頭部作框景，觀看另一人物或空間。 | Frames another person or space past a foreground shoulder or head. |
| `TERM-CH02-POV` | 主觀視角 | Point of View (POV) | 將畫面組織為角色所見或感知的視點；需由上下文建立。 | Organizes the image as a character’s view or perception, established by context. |
| `TERM-CH02-DOLLY` | 攝影機前後移動 | Dolly Movement | 攝影機機位在空間中前進或後退。 | Physical camera translation forward or backward through space. |
| `TERM-CH02-ZOOM` | 變焦 | Zoom | 透過改變焦距改變視角與畫面尺度；攝影機機位可維持不動。 | Changes focal length and angle of view, potentially from a fixed camera position. |
| `TERM-CH02-PAN` | 水平搖攝 | Pan | 攝影機繞固定或近似固定支點水平轉動。 | Horizontal rotation of the camera around a fixed or near-fixed position. |
| `TERM-CH02-TILT` | 垂直搖攝 | Tilt | 攝影機繞固定或近似固定支點垂直轉動。 | Vertical rotation of the camera around a fixed or near-fixed position. |
| `TERM-CH02-TRUCK` | 橫向平移 | Truck Movement | 攝影機機位向側方平移，與原地 Pan 不同。 | Camera translation sideways, distinct from a pan in place. |
| `TERM-CH02-PEDESTAL` | 上下平移 | Pedestal | 攝影機整體垂直升降，不等同 Tilt。 | Vertical translation of the whole camera, distinct from a tilt. |
| `TERM-CH02-ORBIT` | 環繞運鏡 | Orbit | 攝影機沿主體周圍弧線改變機位。 | Camera position moves along an arc around a subject. |
| `TERM-CH02-RACK-FOCUS` | 轉焦 | Rack Focus | 在同一鏡頭中把清晰焦點由一距離平面移向另一平面。 | Shifts the plane of sharp focus from one distance to another within a shot. |
| `TERM-CH02-DEPTH-OF-FIELD` | 景深 | Depth of Field (DoF) | 在指定觀看條件下看似可接受清晰的物距範圍。 | The range of object distances that appear acceptably sharp under specified viewing conditions. |
| `TERM-CH02-CONTINUITY` | 連續性 | Continuity | 維持跨鏡頭時間、空間、動作、視線與道具關係可理解的剪輯一致性。 | Editorial consistency that keeps temporal, spatial, action, eyeline and prop relations understandable. |
| `TERM-CH02-180-DEGREE-RULE` | 180 度軸線規則 | 180-Degree Rule | 常見連戲慣例：攝影機保持在動作軸線同側以維持螢幕方向；可有意跨越但須重新定位觀眾。 | A continuity convention that keeps cameras on one side of an action axis to preserve screen direction; intentional crossings require reorientation. |
| `TERM-CH02-LEAD-ROOM` | 前方留白／視線留白 | Lead Room | 人物注視或移動方向前方保留的畫面空間。 | Space left in front of a person in the direction of gaze or movement. |
| `TERM-CH02-HEADROOM` | 頭頂留白 | Headroom | 人物頭頂與畫框上緣之間的空間。 | Space between the top of a person’s head and the upper frame edge. |
| `TERM-CH02-NEGATIVE-SPACE` | 負空間 | Negative Space | 主體周圍未被主要物件佔據、但具構圖功能的區域。 | Areas around the subject not occupied by primary objects but functioning compositionally. |
| `TERM-CH02-FOCAL-LENGTH` | 焦距 | Focal Length | 鏡頭光學系統的焦距，與感光面尺寸共同關聯視角。 | A lens-system parameter that, together with sensor size, relates to angle of view. |
| `TERM-CH02-PERSPECTIVE` | 透視 | Perspective | 畫面中空間深度和物體相對大小／位置的投影關係，受攝影機位置影響。 | Projected spatial depth and relative size/position relations, affected by camera position. |

## 核心概念與歷史脈絡 {#CH02-S04}

攝影機運動既可以是攝影機器材在空間中的實際移動，也可以是觀眾感知到的移動。哥倫比亞大學電影語言詞彙表指出，早期攝影師 Eugenio Promio 曾把攝影機安裝在列車、電車、汽車及船上；約 1900 年可旋轉雲台的使用也增加了搖攝。該詞彙表同時提醒，無法有把握地指認電影史上第一次攝影機運動，因此本章不把 Promio 稱為「第一位運鏡者」。詞彙表將攝影機運動成為重要表現手段的發展，連結到 1920 年代德國表現主義等脈絡，並記錄有聲電影初期對攝影機固定的限制及 1930 年代起吊臂等設備帶來的變化；這是該教育詞彙表的歷史摘要，出版前仍應以電影史專書補充定位。[R012]

電影攝影的基本區分是：景別描述主體在畫面中的尺度，角度描述攝影機相對主體的位置，焦距描述鏡頭光學參數，攝影機距離影響透視關係，運鏡描述相機位置或方向隨時間的變化。這些術語常被合併成風格形容詞，但在製作文件中應分欄記錄。以下分類與應用包含專業概念整理及實務建議；相關書目列於章末，頁碼定位仍待編輯複核。[R001][R009][R010][R011][R026][R027]

## 2.1 鏡頭語言的六個獨立維度

設計一個鏡頭時，至少拆成：(1)景別（Shot size：主體在畫面中佔多大）；(2)構圖（Composition：元素在畫面何處）；(3)角度（Angle：從何種視點觀看）；(4)鏡頭／光學表現（Lens look：視角、景深、畸變與散景）；(5)運動（Movement：攝影機與主體如何變化）；(6)時間（Duration & temporal progression：從起點到終點的過程）。另外要註記敘事目的、場面調度、聲音、連續性與評估準則。

反例：「電影感、35mm、特寫、鏡頭快速拉遠」可能互相牴觸：若同時要求主體始終保持相同大小，又要求鏡頭迅速後退，必須有明確變焦或角色移動補償。導演應先選擇最重要的效果，而不是堆疊形容詞。

### 2.1.1 操作順序

先問：希望觀眾注意什麼？再問：人物和場景的關係為何？再決定景別、角度、運鏡和光學效果。最後才決定工具生成參數。**觀眾意圖→可見行為→鏡頭規格→生成指令→審片證據**，應是整章一以貫之的轉換鏈。

## 2.2 景別大全（Shot Size）

景別依主體在畫面中的相對尺度命名，不是焦距大小。各劇組對邊界略有不同，以下以人物為主要參考。

| 英文 | 中文慣用稱呼 | 典型人物取景 | 主要敘事任務 | AI 模型提示寫法 |
|---|---|---|---|---|
| Extreme Wide Shot (EWS/ELS) | 極遠景／大遠景 | 人物極小，環境主導 | 建立尺度、距離、處境 | subject appears small in vast environment |
| Wide Shot (WS/LS) | 遠景／全景（依語境） | 人物全身與大量環境 | 交代空間及動作路線 | full body visible, surrounding classroom |
| Full Shot (FS) | 全身景 | 人物頭到腳可見 | 姿態、服裝、肢體動作 | head-to-toe framing |
| Medium Long Shot (MLS) | 中遠景／膝上景 | 通常膝部以上 | 人物動作與部分環境 | knees-up framing |
| Medium Shot (MS) | 中景 | 大致腰部以上 | 人物互動、對白與手勢 | waist-up framing |
| Medium Close-Up (MCU) | 中近景 | 胸部或肩胸以上 | 表情、語氣、親近感 | chest-up framing |
| Close-Up (CU) | 近景／特寫 | 頭臉或重要物件 | 表情、關鍵資訊 | face fills frame, eyes prominent |
| Extreme Close-Up (ECU) | 大特寫 | 眼睛、手指、細小細節 | 極度聚焦、揭示線索 | extreme close-up of fingertip |



![景別尺度對照示意圖：五種人物景別比較。](../figures/CH02-DIAG-01-shot-scale.svg)

**CH02-DIAG-001｜景別尺度對照。** 原創可編輯 SVG 草圖；景別邊界依語境而異，尚未編入正式圖號。

**教學提醒**：同樣是 CU，可能是對人臉，也可能是對桌上的玻璃杯；不要把人像取景定義誤用到所有物件。畫面必須容納字幕及後製裁切空間時，也要提前保留安全區域。

### 2.2.1 景別的選擇不是「越近越有感」

遠景可讓觀眾觀察角色與空間的關係，也可能塑造自由或壓迫。特寫可以表現情感，但亦可能傳遞資訊、引發不安或刻意隱去環境。意義取決於前後鏡頭、表演、聲音及文化脈絡。

**練習 A｜同一行動三種景別**：教師拿起透明玻璃杯。EWS 告訴觀眾人身在何處；MS 顯示教師如何操作；CU 顯示杯壁的光影。試著交換順序並記錄觀眾的理解差異。

![示意五種景別中人物相對畫框的尺度。](../../../assets/chapters/CH02/figures/originals/CH02-DIAG-01-shot-scale.svg){#CH02-FIG-001 fig-alt="示意五種景別中人物相對畫框的尺度。"}

**圖 2-1A｜示意五種景別中人物相對畫框的尺度。 本圖為原創可編輯 SVG 示意圖，非實拍或工具實測。**

## 2.3 構圖（Composition）與視覺重心

### 2.3.1 三分法與中心構圖

三分法（Rule of Thirds）以兩條水平和兩條垂直等分線輔助定位主體；它是一種設計方法，不是不可違反的定律。中心構圖能讓主體直接、對稱、儀式感強；偏離中心則可能保留觀看方向的空間，或暗示失衡。任何構圖都應服務故事。

### 2.3.2 Headroom、Lead Room、Negative Space

**Headroom（頭頂留白）**：人物頭頂與畫框上方的空間，過多可營造壓縮或渺小，也可能只是錯誤留白。**Lead Room / Look Room（前方留白／視線留白）**：人物移動或注視方向留下的空間。**Negative Space（負空間）**：主體之外的區域，能形成視覺平衡、孤寂、等待或揭示空間。AI 生成時應描述主體位置、目光方向及畫面空白處的用途。

### 2.3.3 前景、中景、背景與視覺層次

將前景實驗器材、主體老師、背景學生安排在不同深度，可以同時透露故事資訊。但景深不足可能讓背景線索完全不可辨，景深過深也可能分散注意力。需依敘事取捨。

### 2.3.4 Leading Lines、Symmetry、Frame within Frame

引導線將視線引至主體；對稱可以建立秩序或不安；框中框可以強調觀察、隔閡或空間層次。例如教室窗框圍住玻璃杯，既構成畫中畫，也呼應光線探索主題。不要機械套用構圖法則：一個畫面可能同時運用多種方法。

### 2.3.5 畫面比例與裁切

16:9 適合一般橫式影片，9:16 適合直式短影音，1:1 和其他比例亦有特定展示情境。多平台交付時，關鍵人物、文字和道具不要壓在可能被裁掉的邊界。不同平台的 UI 安全區可能隨產品變化，正式輸出須另外查核。

![16:9 到 9:16 裁切與安全構圖示意圖。](../figures/CH02-DIAG-05-aspect-safe-area.svg)

**CH02-DIAG-005｜橫直式重構圖。** 原創可編輯 SVG 草圖；平台介面安全區仍須依當前規格查證。

![示意直式裁切範圍及主體安全構圖。](../../../assets/chapters/CH02/figures/originals/CH02-DIAG-05-aspect-safe-area.svg){#CH02-FIG-005 fig-alt="示意直式裁切範圍及主體安全構圖。"}

**圖 2-1E｜示意直式裁切範圍及主體安全構圖。 本圖為原創可編輯 SVG 示意圖，非實拍或工具實測。**

## 2.4 攝影角度與敘事視點

| 術語 | 定義 | 可用效果 | 注意事項 |
|---|---|---|---|
| Eye Level | 與主體視線相近 | 平視、自然觀察 | 不表示必然中立 |
| High Angle | 向下俯視主體 | 顯示位置、脆弱或空間全貌 | 不等於鳥瞰 |
| Low Angle | 從低處向上拍 | 建立高度、力量或壓迫 | 誇張透視受距離影響 |
| Bird's-eye / Overhead | 高處接近垂直向下 | 展示配置、幾何或活動路徑 | 對物體相對位置須嚴格驗收 |
| Dutch Angle | 傾斜水平線 | 不穩定、失衡、風格化 | 過度使用易失去效果 |
| POV Shot | 從角色視角觀看 | 使觀眾共享視覺資訊 | 需要前後鏡頭建立主觀關係 |
| Over-the-Shoulder | 越肩鏡頭 | 建立對話及關係 | 必須檢查肩膀、視線、軸線 |

**重要區分**：角度不等於景別。一個低角度鏡頭仍可同時是 WS 或 CU。

## 2.5 光學語言：焦距、視角、距離、透視、景深

### 2.5.1 焦距不是景別

焦距以毫米描述鏡頭的光學參數，與感光元件尺寸共同影響視角；景別則是畫面中主體所佔的尺度。攝影機移動到不同距離，即使焦距不變，景別也會改變；不同焦距配合不同距離，也能得到相似的主體大小。

討論「24mm、35mm、50mm、85mm」的視覺特性時，務必聲明感光元件格式或標示「全片幅等效」。否則單報焦距常缺乏可比較意義。

### 2.5.2 透視主要由攝影機位置決定

常聽到「長焦壓縮透視」，更精確的說法是：為保持相同主體大小而使用長焦鏡頭時，攝影機通常會後退；**攝影機與場景的相對距離**造成前後景相對大小關係的改變。單純從同一位置變更焦距，然後裁切到相同畫面範圍，不會改變物體的透視幾何。

### 2.5.3 景深（Depth of Field）

景深是觀眾可感到清晰的距離範圍，受到光圈、焦距、對焦距離、感光元件及觀看條件等因素共同影響。[R027][R028] **Shallow Depth of Field（淺景深）**可把主體從背景分離；**Deep Focus（深焦）**讓近處與遠處資訊同時可辨。AI 模型輸入「f/1.8」未必真的依鏡頭光學計算，應以「sharp face and softly blurred background」等可見結果描述並驗證。[R027][R028]

### 2.5.4 Dolly 與 Zoom 的核心差異

**Dolly-in**：攝影機實際向主體前進，前後景相對位置和視差可能隨運動改變。**Zoom-in**：攝影機位置不變，改變焦距而放大畫面；理想情況下不會創造由攝影機平移帶來的視差。**Dolly Zoom**：同時移動攝影機與反向變焦，使主體尺度大致維持，背景透視關係發生明顯變化。在 AI 生成中，若只輸入「dolly zoom」，經常要另外驗證主體尺度、背景變化與形變。

![攝影機平移改變視點與視差；變焦改變視角。](../../../assets/chapters/CH02/figures/originals/CH02-DIAG-02-dolly-vs-zoom.svg){#CH02-FIG-002 fig-alt="攝影機平移改變視點與視差；變焦改變視角。"}

**圖 2-1B｜攝影機平移改變視點與視差；變焦改變視角。 本圖為原創可編輯 SVG 示意圖，非實拍或工具實測。**

## 2.6 運鏡（Camera Movement）完整入門

| 運鏡 | 攝影機如何動 | 與容易混淆的概念比較 | 示例用途 |
|---|---|---|---|
| Locked-off / Static | 攝影機固定 | 主體仍可移動 | 讓觀眾觀察細微動作 |
| Pan | 攝影機水平轉動 | 不是整台橫移 | 跟隨學生從左走到右 |
| Tilt | 攝影機垂直轉動 | 不是上下升降 | 從桌面望向老師表情 |
| Dolly In / Out | 整台攝影機前後移動 | 與 Zoom 不同 | 逐步聚焦物件 |
| Truck / Track Lateral | 攝影機橫向平移 | 與 Pan 不同 | 平行跟拍走廊人物 |
| Pedestal | 攝影機上下平移 | 與 Tilt 不同 | 從低位置升到視線高度 |
| Crane / Jib | 攝影機沿弧線或高低路徑移動 | 可結合多軸移動 | 展示教室全貌 |
| Orbit / Arc | 攝影機繞主體移動 | 與主體自轉不同 | 展示器材的空間結構 |
| Handheld | 手持的細小不穩定運動 | 不等於故意亂抖 | 臨場感、主觀緊張 |
| Tracking | 攝影機追蹤移動主體 | 可用軌道、穩定器等完成 | 跟著老師走入教室 |
| Rack Focus | 焦點在不同距離間轉換 | 不是攝影機移動 | 從玻璃杯轉焦到學生 |
| Whip Pan | 很快速的水平搖攝 | 會產生明顯動態模糊 | 快節奏轉場 |

![Dolly 與 Zoom 對照示意圖。](../figures/CH02-DIAG-02-dolly-vs-zoom.svg)

**CH02-DIAG-002｜Dolly 與 Zoom。** 原創可編輯 SVG 草圖。

運鏡至少要說清楚四件事：起點、運動方向、速度曲線、終點。例如「從老師半身中景緩慢推進至手中種子近景，5 秒內連續完成，背景自然產生視差」。若工具只能提供 5 秒固定長度，先調整鏡頭設計並在剪輯中試驗，不要假設提示詞可保證每秒的精確位置。

### 2.6.1 動作與運鏡應分開描述

「鏡頭推進」是 camera motion；「老師轉身」是 subject motion；「樹葉隨風搖動」是 environment motion。混在一起容易增加生成錯誤，建議先成功控制主要動作，再逐項增加副動作。

### 2.6.2 不是每個鏡頭都要動

固定鏡頭能呈現觀察、等待、幾何構圖和真實時間。部分生成模型可能預設產生不必要的飄移，應明確描述 locked-off camera、minimal subject motion，生成後必要時使用編輯器穩定影像。

![Pan 改變方向，Truck 改變攝影機位置。](../../../assets/chapters/CH02/figures/originals/CH02-DIAG-03-pan-vs-truck.svg){#CH02-FIG-003 fig-alt="Pan 改變方向，Truck 改變攝影機位置。"}

**圖 2-1C｜Pan 改變方向，Truck 改變攝影機位置。 本圖為原創可編輯 SVG 示意圖，非實拍或工具實測。**

## 2.7 空間連續性與 180 度規則

人物 A、B 對話時，先建立兩者關係的想像軸線。同一場對話若在同側拍攝，通常較容易維持左右與視線方向的理解。跨越軸線並非禁止，但應以中性鏡頭、人物走位、鏡頭運動或敘事動機重新建立空間關係。

### 2.7.1 對 AI 影片的特別要求

每一鏡記錄：角色站位（screen-left/right）、看向何處（eyeline）、道具與門窗位置、光線方向、是否跨軸。若角色參考影像與場景參考圖不一致，優先修正參考輸入，不要只堆疊文字否定描述。

![對話動作軸與常用攝影機側的俯視示意圖。](../figures/CH02-DIAG-04-180-axis.svg)

**CH02-DIAG-004｜180 度軸線。** 原創可編輯 SVG 草圖；此為連戲慣例示意，不是禁令。

### 2.7.2 專業審片問題

觀眾能否說出誰在左誰在右？人物的目光是否能合理接到所看事物？主體走出右側後，下一鏡是否有可理解的入畫方向？鏡頭反轉是否是創作選擇而非生成失誤？

![Pan 與 Truck 運鏡差異示意圖。](../figures/CH02-DIAG-03-pan-vs-truck.svg)

**CH02-DIAG-003｜Pan 與 Truck。** 原創可編輯 SVG 草圖。

![以俯視示意對話動作軸及常用攝影機側。](../../../assets/chapters/CH02/figures/originals/CH02-DIAG-04-180-axis.svg){#CH02-FIG-004 fig-alt="以俯視示意對話動作軸及常用攝影機側。"}

**圖 2-1D｜以俯視示意對話動作軸及常用攝影機側。 本圖為原創可編輯 SVG 示意圖，非實拍或工具實測。**

## 傳統攝影製作流程 {#CH02-S05}

以下是可依片型與劇組規模調整的實務框架，不是唯一標準流程。攝影機角度、連戲、構圖與剪輯的相互影響，可參照 Mascelli 的專業製作書目；本書目前尚未逐頁核對版本與頁碼。[R010]

1. **從劇本和導演意圖出發**：標出觀眾需要知道、注意或感受的資訊，以及場景中人物和道具的關係。
2. **安排場面與動線**：導演、攝影指導及相關部門確認人物走位、視線方向、場景出入口、光線方向和鏡頭軸線。
3. **建立鏡頭清單與覆蓋**：依敘事需要選擇建立鏡頭、主鏡頭、對話覆蓋、反應鏡頭及必要細節鏡頭；逐項標明景別、角度、機位、鏡頭、運動、焦點及預計時長。
4. **勘景與技術準備**：依場地、器材、鏡頭、支撐設備、照明、收音及安全條件確認可行性；焦距數值須與攝影機格式一起記錄。
5. **排演、拍攝與連續性紀錄**：依排演調整構圖和運鏡；場記記錄鏡次、表演、道具狀態、視線、動作銜接與選用 Take，攝影組依現場流程完成曝光、焦點及機位檢查。
6. **回看素材並交接剪輯**：檢查焦點、曝光、運動、表演、軸線與素材完整性，記錄需補拍項目，並將鏡頭清單、場記和素材識別資訊交給剪輯。

現場實際分工、器材選擇與交接格式會因製作規模而變；本流程作為讀者練習及與 AI 工作流比較的基線，不宣稱每個劇組都採用相同表格或順序。

## AI 時代的鏡頭語言轉換與限制 {#CH02-S06}

本節流程與提示詞是模型中立的規格方法。Runway 文件只支援對該文件所述模型／功能的版本化提示建議，不代表可用物理相機方式精確控制；請依實際工具與版本另作測試。[R029]

### AI 輔助製作工作流程 {#CH02-S07}

1. 鎖定敘事意圖與可觀察結果。
2. 建立參考影格、角色／道具位置及 Shot Spec。
3. 分離主體動作、環境動態、攝影機運動及時間變化。
4. 選一項主要變化先生成；保存輸入、提示、模型版本及輸出雜湊。
5. 以視差、構圖、身份、連續性和物理合理性逐鏡驗收。
6. 將失敗 take 和修正記錄保留；需要精準機位時改採實拍、3D 或傳統合成。

### 提示詞與技術參數 {#CH02-S08}

本書採用分層格式，避免單一句「cinematic masterpiece」取代具體導演工作：

1. **Intent（目的）**：希望觀眾理解或感受什麼。
2. **Composition（取景）**：景別、主體位置、背景線索。
3. **Camera（視點）**：角度、距離感、運鏡與速度。
4. **Action（動作）**：主體、場景、攝影機分離描述。
5. **Continuity（連續性）**：人物、道具、空間、燈光參考。
6. **Deliverable（交付）**：預期時長、比例、輸出規格。
7. **Acceptance（驗收）**：可觀察、可比較的結果。

**Text-to-Video**：提示詞需要包含主體、場景、構圖與動作等資訊。

**Image-to-Video**：若已提供高品質參考圖，提示詞通常更應聚焦「哪些物件動、鏡頭怎麼動、按什麼順序動」。Runway 官方文件也主張依工作模式分配描述重點，從簡單提示逐次增加約束。[R002][R006][R003]

**不可假設精準控制**：對於焦距、焦點、攝影機實際路徑與物理相機參數，應列為「欲呈現的視覺表現」，不是模型已提供物理模擬的證明。生成時長、畫面比例、參考圖數量與攝影控制選項，需以當前使用工具的官方文件為準。

### 2.8.1 可複製提示詞示例

**P01｜Text-to-Video｜EWS 建立場景**

> Extreme wide establishing shot of a quiet elementary science classroom at dawn. The teacher appears small in the background. Morning light streams through the left windows. Locked-off camera, subtle dust particles moving in the light, restrained natural motion, calm atmosphere, continuous shot.

**P02｜Image-to-Video｜MS 跟拍**

> The camera tracks slowly alongside the teacher from left to right as the teacher walks toward the experiment table. Stable medium framing, natural footsteps, smooth motion, one continuous take. The background shifts with consistent parallax.

**P03｜Image-to-Video｜CU 緩慢推進**

> The camera makes a very slow dolly-in toward the transparent glass on the desk. The glass remains stationary. Sunlight patterns remain coherent as the perspective changes subtly. Single continuous shot, gentle movement, no abrupt reframing.

**P04｜Image-to-Video｜固定鏡頭**

> Locked-off camera remains stationary. The teacher's hand slowly reaches into frame and picks up the notebook. Only the hand and notebook move; the surrounding classroom remains still. Continuous natural action.

**P05｜反應鏡頭**

> Medium close-up, eye-level framing. The teacher looks at the refracted light, then raises the eyebrows slightly in quiet curiosity. Stationary camera, subtle believable facial motion, consistent morning window light.

**P06｜視覺連續性核對指令（給多模態審片模型或人工檢查）**

> Compare the reference frame and candidate shot. Report differences in character identity, clothing, glass shape, prop position, window direction, eyeline, lighting direction and camera framing. Separate observed mismatches from uncertain observations. Do not claim physical accuracy from appearance alone.

## 示範案例：《光從哪裡來？》60 秒科普短片 {#CH02-S09}

**案例狀態**：教學設計示範，尚無實際拍攝或 AI 生成影像；本節的時長、比例與格率是規劃值，不是工具實測參數。完整可編輯鏡頭清單另附於本章素材包（`CH02-science-shortfilm.json`）。

**Logline**：學生發現玻璃杯後方的字看起來改變，老師以一個問題，引導孩子思考光線行進與折射現象。

**科學界線**：影像只能作為動機與觀察示意，不能將生成光學效果當作實驗證據。若要說明折射原因，應補充實拍、圖解、條件控制與可再現的科學演示。

| Shot | 時間碼 | 景別／角度 | 動作與運鏡 | 敘事功能 | 音訊 |
|---|---|---|---|---|---|
| S01 | 00:00–00:07 | EWS 平視 | 教室晨光、固定 | 建立時間地點 | 環境聲 |
| S02 | 00:07–00:16 | MS 平視 | 學生拿杯子，緩慢橫移 | 人物與事件 | 桌面聲 |
| S03 | 00:16–00:24 | CU 平視 | 文字透過杯水變化，固定 | 聚焦觀察 | 音樂提示 |
| S04 | 00:24–00:31 | MCU 平視 | 學生疑惑，固定 | 反應 | 「為什麼不同？」 |
| S05 | 00:31–00:42 | OTS 略俯角 | 老師示範，微推進 | 引導問題 | 教師旁白 |
| S06 | 00:42–00:53 | Insert／俯拍 | 手畫出觀察與假設 | 觀察轉思考 | 筆觸音效 |
| S07 | 00:53–01:00 | WS 平視 | 拉遠到討論情境 | 收束與提問 | 音樂結尾 |

### 2.9.1 S03 鏡頭案例的技術細化

- 鏡頭目的：在不揭露答案前吸引觀眾觀察。
- 起始構圖：透明杯與杯後字卡同時可見，讓觀眾理解空間關係。
- 視角：接近桌面高度，固定攝影機優先，避免誇張運鏡掩蓋觀察線索。
- 光學：要求文字與杯身清晰，但不用無法驗證的「真實物理折射」當作模型保證。
- 連續性：字卡位置、杯子形狀、水位、光線方向維持一致。
- 科學驗收：與實際裝置對照；若效果不符，標示為示意或改用實拍。

## 常見錯誤與品質檢查 {#CH02-S10}

| 觀察到的問題 | 可能原因 | 改善次序 |
|---|---|---|
| 角色的臉或衣服變了 | 缺少固定參考；場景描述重複生成 | 固定角色參考→減少變動描述→重新生成 |
| 鏡頭說 Dolly 實際只是放大 | 模型用數位裁切代替透視移動 | 檢查前後景視差→指定相機實際平移→必要時改用 3D／實拍 |
| 固定鏡頭還在飄 | 模型偏好動態 | 明確 locked-off→縮小主體動作→後製穩定 |
| 人物左右位置翻轉 | 缺場景配置與軸線資訊 | 建立 blocking map→固定 screen direction→跨鏡比對 |
| 特寫失去情境 | 缺少建立鏡頭 | 前置 WS／OTS 或補一個 contextual insert |
| 景深很淺卻看不清線索 | 敘事焦點與光學風格衝突 | 改焦點位置→加深景深→分兩鏡頭 |
| 物理效果不正確 | 模型模擬不具實驗可靠性 | 實拍或以標記圖解示意，註明限制 |
| 9:16 裁切切掉手和器材 | 未設安全構圖 | 拆版本、重新構圖，勿僅機械裁切 |

### 2.10.1 建議紀錄的生成資料

模型與版號、提示詞文字、參考圖 URI/檔案雜湊、設定參數、候選 Take ID、審片人、品質評分、已知問題與最終素材檔。對不支援的參數留 `null`，不可虛構。

## 練習、評量與延伸研究 {#CH02-S11}

### 任務 A｜相同主題的景別比較

拍攝或生成「手拿起一顆種子」，各做 EWS、MS、CU 三個版本。寫下每段畫面讓觀眾注意到的資訊，並對照是否達成目標。

### 任務 B｜Dolly vs Zoom

使用場景中前、中、後景可辨識的擺設，分別製作 Dolly-in 與 Zoom-in。逐格觀察前後景相對位移；若 AI 不符合預期，留下失敗版本，描述如何修改。

### 任務 C｜30–60 秒敘事短片

用 5–8 個鏡頭說出「一個發現」。至少包含 WS、MS、CU、兩種角度、一段固定攝影機鏡頭，以及一個有明確理由的運鏡。繳交 Shot List、2 組 Prompt 版本與最後成品，另交一頁反思。

### 評量量規（總分 100）

| 面向 | 配分 | 達標描述 |
|---|---:|---|
| 景別與構圖的敘事目的 | 25 | 選擇能清楚解釋且確有作用 |
| 攝影角度／運鏡正確性 | 20 | 能區分各運動並合理使用 |
| 時空與動作連續性 | 20 | 人物位置、軸線、道具與動作可理解 |
| AI 規格與版本紀錄 | 20 | 規格、提示詞、參考、候選和修正可追溯 |
| 品質驗證與反思 | 15 | 能指出偏差、修復依據與模型限制 |

建議成績等級：90–100 優秀；80–89 良好；70–79 基礎達標；60–69 待加強；低於 60 應重新修訂。級距為本書教學建議而非官方標準。

### 思考題

1. 攝影機位置不動，把 35mm 改為 85mm，透視一定改變嗎？為何？
2. 什麼時候選擇固定鏡頭，比持續運鏡更有效？
3. 為什麼同一段 AI 影片中「臉清楚」不代表跨鏡頭人物一致？
4. 若為 9:16 重剪 16:9 科普影片，哪幾種鏡頭應優先重構圖？
5. 當生成畫面漂亮但折射不符合真實實驗，該如何處理？

**簡答提示**：第 1 題，固定攝影機位置時透視幾何不因單純改焦距而改變；觀看畫角與裁切範圍會改變。第 5 題，避免把 AI 圖像當證據；可改用實拍與驗證過的科學圖解，或清楚標示為示意。

## 2.12 章末摘要

- 景別決定主體相對尺度；角度決定觀看方向；構圖決定畫面元素關係。
- 焦距、相機距離、感光元件與景深不能混為一談。
- Dolly、Pan、Truck、Zoom 各代表不同的運動或光學操作。
- AI 提示詞應描述可看見、可檢查的運動結果，不能把術語視為精準執行的保證。
- 敘事意圖與跨鏡頭連續性，比單一鏡頭的華麗特效更重要。

**本章最重要的一句話**：先決定讓觀眾看見什麼，再決定攝影機怎麼看；最後才決定讓 AI 如何生成。

## 參考資料 {#CH02-S12}

正式線上文件於 2026-10-18 查閱；AI 產品功能屬時效資訊，出版前須重新核對文件、模型版本及實測條件。Runway 文件屬供應商文件或產品教育內容，不作為獨立電影理論證據。

- [R001] Bordwell, David, Kristin Thompson, and Jeff Smith. *Film Art: An Introduction*. 13th ed. McGraw Hill. 出版社列示 2026 年版；本章頁碼定位待查。
- [R002] Runway Academy. “Prompting Guide.” Image-to-video prompting and iteration guidance. 查閱日期：2026-10-18。
- [R003] Runway Help Center. “Image to Video Prompting Guide.” 查閱日期：2026-10-18。
- [R006] Runway Help Center. “Gen-4 Video Prompting Guide.” 查閱日期：2026-10-18。此文件針對特定產品版本；不得推定適用於所有目前模型。
- [R007] Leah Retta. “AI camera prompts: How to control camera movement, angles and shots in AI video.” Runway Resources, 2026-08-21. 查閱日期：2026-10-18。供應商教學內容，產品能力描述需依實測確認。
- [R008] Leah Retta. “AI camera control: 5 methods and how to choose one.” Runway Resources, 2026-10-12. 查閱日期：2026-10-18。供應商教學內容，功能與支援模型具時效性。
- [R009] Bruce Block. *The Visual Story: Creating the Visual Structure of Film, TV, and Digital Media*. Routledge. ISBN 9781138014152；版次及本章頁碼定位待查。
- [R010] Joseph V. Mascelli. *The Five C’s of Cinematography: Motion Picture Filming Techniques*. Silman-James Press. ISBN 9781879505414；出版方頁面列 252 頁，本章頁碼定位待查。
- [R011] Blain Brown. *Cinematography: Theory and Practice: Image Making for Cinematographers and Directors*. Routledge. ISBN 9780367373450；版次及本章頁碼定位待查。
- [R012] Columbia University, Center for New Media Teaching and Learning. “Camera Movement.” *Columbia Film Language Glossary*. https://filmglossary.ccnmtl.columbia.edu/term/camera-movement/. 查閱日期：2026-10-18。教育詞彙表；其歷史摘要需與電影史專書交叉核對。

### 編輯待辦（本稿不得標示為出版完成）

- 核對 [R001]、[R009]、[R010]、[R011] 實際採用版次並補充支撐各項概念的頁碼／章節定位；目前不提供未核實頁碼。
- 為構圖、攝影機運動、180 度軸線及橫直式安全區製作可編輯原創示意圖；目前素材包僅預留插圖目錄，尚無可發布圖像。
- 以指定工具與模型記錄提示詞實測、輸入資產、參數、生成日期、版本及結果；本章示範提示詞尚未執行。
- 科學折射畫面應以實拍或有來源的科學圖解核對；生成畫面不作實驗證據。
- 目前章名與 `docs/TOC.md` 第 2 章規劃標題不同。依素材包要求保留全書目錄，等待編輯決定是否同步標題。

