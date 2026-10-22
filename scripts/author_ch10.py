from pathlib import Path
import hashlib, xml.etree.ElementTree as ET
import yaml

R=Path(__file__).resolve().parents[1]
ZH='''---
chapter_id: CH10
part_id: P02
number: 10
slug: chapter-10
locale: zh-TW
title: "劇本格式、改編與版本管理"
status: draft
translation_status: source-draft
source_revision: 2.1.0-draft
last_researched: 2026-10-22
last_updated: 2026-10-22
claim_types: [verified-fact, theory, practice, ai-hypothesis, demo]
---

# 劇本格式、改編與版本管理 {#CH10-S00}

> 編輯狀態：繁體中文研究草稿；英文為工作譯稿。來源僅支持明列範圍；頁碼、全文解讀、電影版本／時間碼待查。圖稿為原創 SVG 草稿，權利及出版核准待辦。

## 學習目標與適用對象 {#CH10-S01}

完成本章後，讀者能夠：

1. 說明劇本格式如何服務閱讀、排演、估算和部門交接，並辨認不同市場與製作階段的差異。
2. 區分改編材料、已取得權利、創作轉化和待法律確認事項；完成劇本不代表已取得改編權。[R072]
3. 維護含日期、作者、稿次、修改摘要及影響場景的版本紀錄。
4. 以穩定場景 ID 比較稿件，將格式、連續性與創作決策分流處理。
5. 評估 Fountain 等文字標記格式是否適合作為特定專案交換檔，並先測試轉檔樣本。[R075]

適用於編劇、導演、製片、劇本統籌及跨部門稿件協作者。先備知識為基本場景標題、動作、角色名及對白；不假設所有人使用同一軟體或慣例。

## 核心概念與專業術語 {#CH10-S02}

| 術語 ID | 繁體中文 | English | 工作定義 |
|---|---|---|---|
| TERM-CH10-SCREENPLAY | 電影劇本 | screenplay | 供創作、閱讀及製作溝通的文本；格式服務於工作情境，不表示影像逐字照拍。[R070] |
| TERM-CH10-SCENE-HEADING | 場景標題 | scene heading | 標示內外景、地點、時間等資訊的場景起始行；欄位依採用規格或團隊約定。 |
| TERM-CH10-SLUGLINE | 場景行／slugline | slugline | 劇本場景標題的常見業界稱呼；地區與格式間用語可能不同。 |
| TERM-CH10-ADAPTATION | 改編 | adaptation | 將既有材料重新組織為另一作品形式；創作方法和權利狀態是不同問題。[R072] |
| TERM-CH10-DERIVATIVE-WORK | 衍生作品 | derivative work | 美國著作權法定義中，改編、轉換或改作既有作品的作品；不代表其他法域法律意見。[R072] |
| TERM-CH10-REVISION-SET | 修訂稿次 | revision set | 製作中標示特定稿次及其變更的工作慣例；顏色和標記須由劇組定義。[R073] |
| TERM-CH10-LOCKED-PAGES | 鎖定頁 | locked pages | 製作中維持頁碼參照的版本管理方式；時點及程序依工作流程而定。[R074] |
| TERM-CH10-SCREENPLAY-INTERCHANGE | 劇本交換格式 | screenplay interchange format | 在工具間傳遞劇本文字與結構的格式或約定；轉檔後須檢查元素、分頁及註記。[R075] |

詞條均為本書工作定義草案，待雙語術語編輯核定。Academy Nicholl 指出專業寫作者的格式存在差異；其指南是參考，不是全球強制標準。[R070]

## 歷史與基本原理 {#CH10-S03}

劇本頁面同時是敘事文本和協作介面。場景標題協助劇組定位內外景、地點與時間；動作、角色名及對白便於閱讀、排演和估算工作。格式可降低交接成本，不能取代導演、演員、美術、攝影、製片及剪輯的討論。Academy Nicholl 的公開資源整理常見美國格式並承認寫作者有差異；應先遵守委託方、比賽或製作方規格，再以通行格式作預設。[R070]

創作稿與製作稿任務不同。純文字標記便於差異比較和保存；專業軟體可能提供分頁、修訂顏色、鎖頁及部門交付。Fountain 以可讀標記表示場景行、角色、對白、轉場及註記，官方規格描述其語法；這不保證所有軟體完整支援或轉檔逐頁一致。[R075]

改編創作要決定哪些材料保留、重組、刪除或重新表達；權利審查則確認誰可授權哪些地區、期間、媒介、語言及用途。美國著作權法將翻譯、戲劇化、電影化等列作衍生作品例子，衍生作品權利不會自動涵蓋未獲授權的底本。[R072] 這是美國法條概述，不是全球法律意見或權利鏈證明。

## 傳統製作方法 {#CH10-S04}

1. **確認交付規格：**記錄媒介、語言、頁面或軟體格式、檔名、版本命名、收件人與期限；有明文要求時依其規格。
2. **整理創作稿：**以場景標題、動作、角色名和對白提供可讀稿件。只寫有助故事、表演或製作決策的資訊，避免把每個攝影想法或未定細節寫成硬性命令。
3. **準備製作資料：**另維護角色／場景清單、拍攝需求、修訂摘要和未決問題。需要場景編號時，指定負責人與編號時點。
4. **管理修訂：**Final Draft 文件描述 Revision Mode 的增刪標記、修訂色彩及修訂集；具體用法與色碼須由劇組定義。[R073]
5. **適時鎖頁：**Final Draft 建議不要過早鎖定頁面，並將鎖頁放在前期準備／製作流程中考量。[R074] 鎖頁不等於內容不可變更。
6. **交付封存：**保存可讀稿、修訂摘要、版本識別、送件日期、源檔與 SHA-256，便於辨認實際使用稿。

### 改編材料登錄

建立底本名稱與版本、作者／權利人、取得方式、授權文件位置、地區／期間／媒介／語言、宣傳用途、署名條件及限制清冊。未知欄位標為待確認。另用轉化表記錄保留、合併、刪除、重排及新增；該表是編輯工具，不是法律判定。

## AI 時代的技術轉換與限制 {#CH10-S05}

在團隊核准且資料權利確認後，程式或模型可協助抽取場景標題、角色、重複詞、版本差異、缺漏欄位及待查問題。這是可試驗的流程，不是任何當前工具功能保證。不可把未授權底本、保密劇本或個資送入未核准服務；先核對服務現行條款、資料保留政策與團隊安全規定。

- **程式檢查：**必要欄位、穩定場景 ID、版本標記、引用是否存在、作者／日期紀錄和輸出可讀性。
- **模型候選整理：**在允許的文本範圍內產生差異摘要或疑點，逐項指向原始行號／場景 ID；不得自動寫回主稿。
- **人類決策：**改編權利、人物再現、情節取捨、表演意圖、鎖頁及正式交付由作者、製片或法律專業人員決定。

模型可能把全大寫動作誤判成角色名、將縮寫誤認為場景標題或漏看手工修訂標記。差異摘要只能提供核查線索；文字相似度不能證明抄襲、授權或作者意圖。

## 詳細工作流程 {#CH10-S06}

| 步驟 | 負責與操作 | 產出及檢查 |
|---|---|---|
| 1. 收件 | 劇本統籌記錄提交人、日期、語言、來源檔雜湊及存取限制 | 唯讀來源副本、來源 ID、權利狀態 |
| 2. 確認格式 | 編劇／製片確認收件規格、模板、稿次規則與工具 | 格式決策紀錄；歧義向收件方核實 |
| 3. 建立主檔 | 作者使用選定工具寫作，建立穩定場景 ID 或對照表 | 可編輯主檔、修訂 ID、日期 |
| 4. 登錄改編依據 | 製片／權利窗口核對權利人與書面授權；作者建轉化表 | 權利文件位置及待辦；完成稿不等於獲授權 |
| 5. 檢查稿件 | 助理／程式檢查格式、角色名、重複場景、引用和交付包 | 可重現檢查報告；疑點人工確認 |
| 6. 記錄修訂 | 作者命名稿次；製作期由指定人管理色彩、頁碼和鎖頁 | 變更摘要、差異、頁碼及受影響部門 |
| 7. 交換格式 | 以代表樣本測試 Fountain、FDX、PDF 等轉換，檢查場景、對白、註記、字元和分頁 | 轉檔清單及工具相容矩陣 |
| 8. 交付封存 | 製片指定正式包並保存源檔、PDF、版本識別及收件紀錄 | 可回復檔案包、雜湊清單、存取權限 |

建議最小 JSON 版本欄位：`project_id`、`document_id`、`revision_id`、`parent_revision`、`author`、`created_at`、`change_summary`、`changed_scene_ids`、`rights_basis`、`approval_state`、`source_hash`。這是本章示範，不是跨軟體標準。

## 提示詞與技術參數 {#CH10-S07}

以下為模型中立示範，不代表任何服務實測或特定參數。只輸入獲准使用的最小文本。

```text
角色：劇本版本整理助理，不改寫或核准稿件。
輸入：兩份已獲准比較的稿件、版本 ID、穩定場景 ID 對照表。
任務：列出新增、刪除、移動與文字變更，附場景 ID 及來源行號。
限制：不補寫故事、不推斷作者意圖、不判定抄襲或權利；無法配對則回報 unknown；原稿唯讀。
輸出 JSON：
{"from_revision":"...","to_revision":"...","changes":[{"scene_id":"...","kind":"added|removed|moved|text-change|format-change","source_lines":["..."],"summary":"...","human_review":"required"}],"unmatched_items":[],"limitations":[]}
```

先以 3–5 個代表場景試跑並逐項比對；記錄工具、版本、日期、輸入範圍及錯誤。程式 diff 也須記錄編碼、換行、正規化和工具版本。

## 電影案例分析 {#CH10-S08}

### 《綠野仙蹤》（The Wizard of Oz, 1939）

AFI Catalog 將 1939 年電影連結至 L. Frank Baum 的 1900 年小說 *The Wonderful Wizard of Oz*，並記錄多位編劇和製作過程的改動線索。[R076] 這提供研究問題：人物動機如何改變、段落如何重組、哪些表達由文字轉為電影媒介。本文只根據目錄的書目及製作史資訊，不宣稱已觀看片源、確認個別作者意圖或取得完整劇本。

**分析練習：**使用合法取得的小說和電影版本，選短段落建立「底本事件／影片對應／媒介轉換／保留或刪除／效果假設」五欄表，逐項記頁碼或時間碼。權利狀態另行核查；某版本可取得不代表已獲電影改編權。

比較任何改編作品時，可分開研究底本事件、劇本結構、視聽表達與權利脈絡。鏡頭／表演分析須指定版本和觀片紀錄；法律結論須由適用法域專業人士審查。片目摘要或 AI 摘要不能代替全文或作品本身。

![原創流程圖：劇本從創作稿、修訂稿、製作稿到封存交付。](../../../assets/chapters/CH10/figures/originals/CH10-FIG-001-revision-lifecycle.svg){#CH10-FIG-001 fig-alt="四個稿件版本節點以箭頭連接，呈現創作稿、修訂稿、製作稿和交付封存。"}

**圖 10-1｜版本需追溯來源、作者、變更和交付狀態；流程是本書工作模型。本圖為原創可編輯 SVG 示意圖，非電影劇照；署名、權利及出版核准待審。**

![原創映射圖：底本、權利核對與創作選擇分流後形成新劇本。](../../../assets/chapters/CH10/figures/originals/CH10-FIG-002-adaptation-map.svg){#CH10-FIG-002 fig-alt="流程圖分列底本材料、權利審查、創作選擇及新劇本，並標示法律審查閘門。"}

**圖 10-2｜創作轉化紀錄與權利審查分開留存；圖示不構成法律意見。本圖為原創可編輯 SVG 示意圖，未描繪特定作品；權利與出版核准待審。**

![原創差異圖：以場景 ID 對照前稿、改稿及待審差異。](../../../assets/chapters/CH10/figures/originals/CH10-FIG-003-change-review.svg){#CH10-FIG-003 fig-alt="流程圖比較同一場景 ID 的前稿和改稿，產生差異摘要後交由人員判讀。"}

**圖 10-3｜差異工具提供核對線索，作者判斷是否採納及影響部門。本圖為原創可編輯 SVG 示意圖，非正式劇本頁面；權利及出版核准待審。**

## 常見錯誤與品質驗證 {#CH10-S09}

| 錯誤 | 風險 | 檢查 |
|---|---|---|
| 將單一格式當全球規則 | 不符合收件規定 | 確認要求並記錄格式決策。[R070] |
| 過早鎖頁或重編號 | 部門頁碼／場次參照失效 | 設定鎖頁時點，逐稿核對。[R074] |
| 將修訂色彩當通用標準 | 劇組誤讀稿次 | 在交付說明定義色彩及版本識別。[R073] |
| 把改編表當授權證明 | 權利及發行風險 | 由法律專業人員核對權利人、範圍及文件。[R072] |
| 轉檔只看字數 | 場景、對白、註記或分頁遺失 | 抽查代表場景、雙語字元、標記和頁面。[R075] |
| AI 差異摘要自動寫回主稿 | 未核准建議進入正式稿 | 分開保存分析結果；指定作者修改並留紀錄。 |

**可自動驗證：**metadata、S01–S12 對齊、引用與術語 ID、圖片路徑／雜湊／SVG XML、雙語圖說和 alt、網站路由及草稿格式。**需人工判斷：**收件方格式符合度、改編創作效果、案例解讀、文化再現、權利鏈、頁面校樣、英文語感及作者核准。不得將人工項目報為自動 PASS。

## 練習、評量與延伸研究 {#CH10-S10}

1. **格式拆解：**用合法可取得的一頁劇本，標示場景、動作、角色、對白、轉場與版本資訊，記錄來源，不大量複製文本。
2. **改編對照：**選有合法文本與看片來源的作品，完成五欄轉化表，註明版本和頁碼／時間碼；未核實處保留未知。
3. **版本差異：**為兩段自有短稿建立場景 ID，比較增刪、移動、格式修正與敘事改變。
4. **交換測試：**建立含內外景、中文角色名、雙語對白、括號、場景編號和註記的小樣，實測兩工具轉換並記錄損失。
5. **權利演練：**以虛構底本填寫來源／授權清單，未知欄位標待確認；不作法律建議。

評量各項 0–2 分：交付與版本可追溯；創作轉化與權利狀態分開；差異連回場景 ID；轉檔測試指出實際損失；人機責任和待辦明確。0 無證據、1 部分可追溯、2 步驟來源限制完整。此量表評估紀錄，不衡量藝術品質。

延伸研究：比較不同國家／媒介的交付規則；查閱劇本工具現行匯入／匯出文件並記錄版本；合法取得底本與影片後作場景比較；研究版本管理對劇組交接和創作決策的影響。

## 參考資料 {#CH10-S11}

- [R070] Academy of Motion Picture Arts and Sciences, “Nicholl Screenwriting Resources,” https://www.oscars.org/nicholl/screenwriting-resources. 格式指引與格式差異說明，僅在該頁範圍內引用。
- [R071] Writers Guild of America West, “WGAW Registry,” https://www.wgawregistry.org/. 官方登記說明；不是法律意見。
- [R072] U.S. Copyright Office, *Copyright Law of the United States (Title 17)*, Chapter 1, §§101–103, https://www.copyright.gov/title17/92chap1.html. 美國法條；不可外推至其他法域。
- [R073] Final Draft Knowledge Base, “How do I use Revision Mode?”, https://kb.finaldraft.com/hc/en-us/articles/27813588722708-How-do-I-use-Revision-Mode. 軟體官方文件；依實際版本核對。
- [R074] Final Draft Knowledge Base, “How do I lock or unlock script pages and use the locking tools?”, https://kb.finaldraft.com/hc/en-us/articles/27817054455828-How-do-I-lock-or-unlock-script-pages-and-use-the-locking-tools. 軟體流程說明，不代表每劇組皆採用。
- [R075] Fountain, “Syntax,” https://fountain.io/syntax/. 格式規格語法；工具支援及互轉效果須實測。
- [R076] American Film Institute, AFI Catalog, *The Wizard of Oz* (1939), https://catalog.afi.com/Film/7892-THE-WIZARDOFOZ. 片目與製作史線索，不代替觀片或權利審查。

線上來源查閱日期：2026-10-22。完整書籍定位、電影版本／時間碼、軟體互通實測均待人工查核。
'''

EN='''---
chapter_id: CH10
part_id: P02
number: 10
slug: chapter-10
locale: en-US
title: "Screenplay Format, Adaptation, and Revision Management"
status: draft
translation_status: review-needed
source_revision: 2.1.0-draft
last_researched: 2026-10-22
last_updated: 2026-10-22
claim_types: [verified-fact, theory, practice, ai-hypothesis, demo]
---

# Screenplay Format, Adaptation, and Revision Management {#CH10-S00}

> Editorial state: English working translation of a Traditional Chinese research draft. The title follows the registry topic and needs approval. Sources support only their stated scope; book locators, full-text interpretation, viewing editions, and timecodes remain unchecked. Original SVGs are drafts pending rights and publication review.

## Learning Objectives and Audience {#CH10-S01}

Readers will be able to:

1. Explain how screenplay format supports reading, rehearsal, budgeting, and departmental handoffs, while recognizing variation by market and production stage.
2. Separate adaptation material, granted rights, creative transformation, and legal questions; a completed screenplay does not establish adaptation rights.[R072]
3. Maintain revision records with dates, authors, status, change summaries, and affected scenes.
4. Compare drafts by stable scene IDs and route formatting, continuity, and creative decisions to appropriate review.
5. Assess whether a text-markup format such as Fountain can serve a project's interchange needs, testing a sample first.[R075]

This chapter is for screenwriters, directors, producers, script coordinators, and AI practitioners who hand scripts across departments. Prerequisites are basic scene headings, action, character cues, and dialogue. No software or single industry convention is assumed.

## Core Concepts and Professional Terms {#CH10-S02}

| Term ID | 繁體中文 | English | Working definition |
|---|---|---|---|
| TERM-CH10-SCREENPLAY | 電影劇本 | screenplay | A text for creative work, reading, and production communication; format serves the task and does not require literal reproduction on screen.[R070] |
| TERM-CH10-SCENE-HEADING | 場景標題 | scene heading | A scene-opening line identifying information such as interior/exterior, location, and time; fields depend on the adopted specification or team convention. |
| TERM-CH10-SLUGLINE | 場景行／slugline | slugline | A common industry term for a screenplay scene heading; usage varies by region and format. |
| TERM-CH10-ADAPTATION | 改編 | adaptation | The creative process of reorganizing existing material into another work form; creative method and rights status are distinct.[R072] |
| TERM-CH10-DERIVATIVE-WORK | 衍生作品 | derivative work | A work adapting, transforming, or recasting a preexisting work as defined in U.S. copyright law; this is not advice for other jurisdictions.[R072] |
| TERM-CH10-REVISION-SET | 修訂稿次 | revision set | A production practice identifying a revision and its changes; the team defines colors and marks.[R073] |
| TERM-CH10-LOCKED-PAGES | 鎖定頁 | locked pages | A production version-management method for preserving page references; timing and procedure depend on workflow.[R074] |
| TERM-CH10-SCREENPLAY-INTERCHANGE | 劇本交換格式 | screenplay interchange format | A format or convention for transferring screenplay text and structure between tools; verify elements, pagination, and notes after conversion.[R075] |

These are draft working definitions awaiting bilingual terminology review. The Academy Nicholl resource notes variation among professional writers; its guide is a reference, not a global mandate.[R070]

## History and Principles {#CH10-S03}

A screenplay page is both narrative text and a collaboration interface. Scene headings help a crew locate interiors/exteriors, places, and times; action, character cues, and dialogue support reading, rehearsal, and production estimates. Format can reduce handoff friction but cannot replace discussion among directors, actors, design, camera, producing, and editorial teams. The Academy Nicholl resource collects common U.S. practices and acknowledges variation. Follow the commissioning party, contest, or production requirements first; use familiar conventions as a default only when requirements are absent.[R070]

A writing draft and a production draft have different jobs. Plain-text markup can support diffs and preservation; dedicated software may offer pagination, revision colors, locked pages, and departmental delivery. Fountain represents scene headings, characters, dialogue, transitions, and notes with readable markers. Its specification documents syntax, but this does not ensure every application supports every feature or produces identical pages.[R075]

Creative adaptation decides what to retain, reorganize, remove, or re-express. Rights review asks who may authorize which uses, territories, periods, media, languages, and scopes. U.S. copyright law lists translation, dramatization, and motion-picture versions among examples of derivative works; rights in a derivative do not automatically cover source material used unlawfully.[R072] This summarizes U.S. statutory text, not global law or legal advice.

## Traditional Production Practice {#CH10-S04}

1. **Confirm delivery requirements:** record medium, language, page or software format, filenames, revision naming, recipient, and deadline. Follow stated requirements.
2. **Prepare a readable writing draft:** use scene headings, action, character cues, and dialogue. Include information that supports story, performance, or production decisions; avoid turning every camera idea or undecided detail into a command.
3. **Prepare production information:** maintain character/location lists, shooting needs, revision summaries, and open questions separately as needed. If scene numbers are required, assign an owner and numbering milestone.
4. **Manage revisions:** Final Draft documentation describes Revision Mode additions/deletions, revision colors, and revision sets. The production defines its actual conventions.[R073]
5. **Lock pages at the right stage:** Final Draft advises against locking pages too early and discusses locking in a preproduction/production workflow.[R074] Locked pages can still change through a controlled process.
6. **Deliver and archive:** retain a readable draft, change summary, revision ID, delivery date, source file, and SHA-256 to identify the version actually used.

### Adaptation source register

Record source title and edition, author/rightsholder, acquisition source, license-document location, territory/term/media/language, promotional uses, credit terms, and restrictions. Mark unknowns pending. A separate transformation map records material retained, combined, removed, reordered, or added; it is an editorial tool, not a legal decision.

## AI-Era Technical Changes and Limits {#CH10-S05}

With team authorization and confirmed data rights, scripts or models may assist with extracting scene headings, characters, repeated terms, draft differences, missing fields, and questions. These are workflow experiments, not guarantees about current tools. Do not submit unlicensed source material, confidential scripts, or personal data to an unapproved service; check current terms, retention policies, and security rules.

- **Programmatic checks:** required fields, stable scene IDs, revision labels, reference existence, author/date records, and readable exports.
- **Model-assisted candidates:** within authorized text, produce a diff summary or questions linked to source lines/scene IDs; never write them into the master automatically.
- **Human decisions:** adaptation rights, representation, story choices, performance intent, page locking, and formal delivery belong to authors, producers, or legal professionals.

A model may misclassify uppercase action as a character cue, mistake abbreviations for scene headings, or miss manual revision marks. A diff is a review clue; textual similarity does not prove copying, authorization, or author intent.

## Step-by-Step Workflow {#CH10-S06}

| Step | Owner and operation | Deliverable and check |
|---|---|---|
| 1. Intake | Script coordinator records submitter, date, language, source hash, and access limits. | Read-only source, source ID, rights status. |
| 2. Confirm format | Writer/producer confirms delivery requirements, template, revision rules, and tools. | Format decision; clarify ambiguity with recipient. |
| 3. Establish master | Author writes in selected tool and assigns stable scene IDs or a crosswalk. | Editable master, revision ID, date. |
| 4. Register adaptation basis | Producer/rights contact checks source and written license; author maps transformations. | Rights-file location and open issues; completion is not authorization. |
| 5. Check draft | Assistant/software checks format, character names, duplicate scenes, citations, and package. | Reproducible report; confirm suspected issues manually. |
| 6. Record revisions | Author names revision set; production assignee manages colors, pages, and locks. | Change summary, diff, pagination, affected departments. |
| 7. Exchange formats | Test a representative sample among Fountain, FDX, PDF, or others; inspect elements, dialogue, notes, characters, and pagination. | Conversion checklist and compatibility matrix. |
| 8. Deliver/archive | Producer specifies package and retains source, PDF, revision ID, and receipt. | Recoverable package, hashes, access controls. |

Suggested JSON revision fields: `project_id`, `document_id`, `revision_id`, `parent_revision`, `author`, `created_at`, `change_summary`, `changed_scene_ids`, `rights_basis`, `approval_state`, and `source_hash`. This is a demonstration, not an interchange standard.

## Prompt and Technical Parameters {#CH10-S07}

This model-neutral example is illustrative, not a service test. It specifies no provider or unverified parameters. Use only authorized text and the minimum needed.

```text
Role: screenplay revision organization assistant; do not rewrite or approve.
Input: two authorized drafts, revision IDs, stable scene-ID crosswalk.
Task: list additions, removals, moves, and text changes with scene IDs and source lines.
Constraints: add no story; infer no intent; decide no copying or rights status;
report unmatched items as unknown; keep source drafts read-only.
JSON: {"from_revision":"...","to_revision":"...","changes":[{"scene_id":"...","kind":"added|removed|moved|text-change|format-change","source_lines":["..."],"summary":"...","human_review":"required"}],"unmatched_items":[],"limitations":[]}
```

Test 3–5 representative scenes and compare each result manually. Record tool, version, date, input scope, and errors. For software diffs record encoding, newline, normalization, and diff-tool version.

## Film Case Study {#CH10-S08}

### *The Wizard of Oz* (1939)

The AFI Catalog connects the 1939 film to L. Frank Baum's 1900 novel *The Wonderful Wizard of Oz* and records clues about multiple screenwriters and production changes.[R076] This creates research questions: which motivations changed, which passages were reorganized, and which expressions were redesigned for cinema? This section uses catalog-level bibliographic and production-history evidence only. It does not claim project viewing, a single author's intent, or access to the complete screenplay.

**Exercise:** Using lawfully available editions of the novel and film, select a short passage and record source event, film counterpart, medium-specific change, retained/removed material, and an effect hypothesis. Cite page or timecode. Check rights separately; availability of a source edition does not establish film adaptation permission.

For any adaptation, compare source events, screenplay structure, audiovisual expression, and rights context separately. Shot/performance analysis requires a selected edition and viewing log. Legal conclusions require qualified review in the applicable jurisdiction. Catalog or AI summaries do not substitute for the source text or film.

![Original process diagram: a screenplay moves from writing draft through revisions and production draft to archive.](../../../assets/chapters/CH10/figures/originals/CH10-FIG-001-revision-lifecycle.svg){#CH10-FIG-001 fig-alt="Four version nodes connect a writing draft, revision drafts, production draft, and archived delivery."}

**Figure 10-1.** Versions should trace source, author, changes, and delivery status; this is a working model. This is an original editable SVG illustration for this book, not a film still. Attribution, rights, and publication approval are pending.

![Original mapping diagram: source material, rights checks, and creative choices feed a new screenplay.](../../../assets/chapters/CH10/figures/originals/CH10-FIG-002-adaptation-map.svg){#CH10-FIG-002 fig-alt="A diagram separates source material, rights review, creative choices, and a new screenplay, with a legal-review gate."}

**Figure 10-2.** Creative transformation and rights review need separate records; the diagram is not legal advice. This is an original editable SVG illustration for this book and depicts no specific work. Rights and publication approval are pending.

![Original comparison diagram: stable scene IDs connect earlier and revised drafts to items for review.](../../../assets/chapters/CH10/figures/originals/CH10-FIG-003-change-review.svg){#CH10-FIG-003 fig-alt="A diagram compares earlier and revised drafts for one scene ID, summarizes differences, and routes them to human review."}

**Figure 10-3.** Diff tools provide review cues; authors decide whether to accept changes and which departments they affect. This is an original editable SVG illustration for this book, not a production screenplay page. Rights and publication approval are pending.

## Common Errors and Quality Checks {#CH10-S09}

| Error | Risk | Check |
|---|---|---|
| Treating one format as global | Fails recipient requirements | Confirm requirements and log the format decision.[R070] |
| Locking pages or renumbering too early | Department references drift | Set a milestone and compare revisions.[R074] |
| Treating revision colors as universal | Team misreads revision | Define colors and revision IDs in delivery notes.[R073] |
| Treating an adaptation map as permission | Rights/distribution risk | Legal review of rightsholder, scope, and documents.[R072] |
| Checking only word count after conversion | Elements or pagination may be lost | Compare representative scenes, bilingual characters, marks, and pages.[R075] |
| Writing AI summaries into the master | Unapproved changes become canonical | Isolate analysis; designated author edits and logs the master. |

**Automatable:** metadata, bilingual S01–S12 alignment, term/reference IDs, local image paths/hashes/SVG XML, captions/alt, site routes, and draft format structure. **Human judgment:** recipient compliance, adaptation merits, case analysis, representation, chain of title, page proofing, English fluency, and author approval. Automation must not report human items as PASS.

## Exercises, Assessment, and Further Research {#CH10-S10}

1. **Format analysis:** mark elements on one lawfully available screenplay page; record source and format rule without reproducing extensive text.
2. **Adaptation map:** use lawful source text and viewing access, complete a transformation table, and cite edition/page/timecode. Leave unknown differences unresolved.
3. **Revision diff:** assign stable scene IDs to two original short drafts and classify additions, removals, moves, formatting edits, and story changes.
4. **Interchange test:** create a sample with interior/exterior headings, Chinese names, bilingual dialogue, parentheticals, scene numbers, and notes. Test two verified tools and record losses.
5. **Rights exercise:** use fictional source material to complete the source/license checklist; leave unknowns pending. This is not legal advice.

Score each item 0–2: traceable delivery/version; separation of creative transformation and rights; diffs mapped to scene IDs; tested conversion losses; clear human/tool responsibilities and open tasks. 0 = no evidence, 1 = partly traceable, 2 = complete steps, sources, and limits. This assesses process records, not artistic quality.

Further research: compare delivery conventions across countries/media; inspect current tool import/export documentation and versions; conduct a scene comparison with lawfully obtained source and film; study the effect of revision systems on handoffs and creative decisions.

## References {#CH10-S11}

- [R070] Academy of Motion Picture Arts and Sciences, “Nicholl Screenwriting Resources,” https://www.oscars.org/nicholl/screenwriting-resources. Formatting guidance and variation, used within page scope.
- [R071] Writers Guild of America West, “WGAW Registry,” https://www.wgawregistry.org/. Official registry information; not legal advice.
- [R072] U.S. Copyright Office, *Copyright Law of the United States (Title 17)*, Chapter 1, §§101–103, https://www.copyright.gov/title17/92chap1.html. U.S. law; do not generalize to other jurisdictions.
- [R073] Final Draft Knowledge Base, “How do I use Revision Mode?”, https://kb.finaldraft.com/hc/en-us/articles/27813588722708-How-do-I-use-Revision-Mode. Vendor documentation; verify against installed version.
- [R074] Final Draft Knowledge Base, “How do I lock or unlock script pages and use the locking tools?”, https://kb.finaldraft.com/hc/en-us/articles/27817054455828-How-do-I-lock-or-unlock-script-pages-and-use-the-locking-tools. Vendor workflow; not universal practice.
- [R075] Fountain, “Syntax,” https://fountain.io/syntax/. Format syntax; application support and conversion require testing.
- [R076] American Film Institute, AFI Catalog, *The Wizard of Oz* (1939), https://catalog.afi.com/Film/7892-THE-WIZARDOFOZ. Catalog/production-history clues; not viewing or rights clearance.

Web sources accessed 2026-10-22. Book locators, film edition/timecodes, and tool interoperability require human verification.
'''

(R/'content/zh-TW/chapters/CH10-chapter-10.md').write_text(ZH,encoding='utf-8')
(R/'content/en-US/chapters/CH10-chapter-10.md').write_text(EN,encoding='utf-8')

figdir=R/'assets/chapters/CH10/figures/originals'; figdir.mkdir(parents=True,exist_ok=True)
defs=[('revision-lifecycle','稿件版本生命週期','SCREENPLAY REVISION LIFECYCLE',['創作稿 / Writing draft','修訂稿次 / Revision set','製作稿 / Production draft','交付封存 / Delivered archive']),('adaptation-map','改編來源與審查分流','ADAPTATION: CREATIVE WORK + RIGHTS REVIEW',['底本材料 / Source material','權利核對 / Rights review','創作轉化 / Creative choices','新劇本 / New screenplay']),('change-review','以場景 ID 核對改稿','REVIEW CHANGES BY STABLE SCENE ID',['前稿 / Earlier draft','場景 ID / Scene ID','改稿 / Revised draft','人工決策 / Human decision'])]
for stem,title,subtitle,labels in defs:
    rects=''.join(f'<g transform="translate({60+i*280},235)"><rect width="220" height="110" rx="20" fill="{["#23344d","#376477","#ad6d50","#374f43"][i]}"/><text x="110" y="45" text-anchor="middle" class="zh">{labels[i].split(" / ")[0]}</text><text x="110" y="77" text-anchor="middle" class="en">{labels[i].split(" / ")[1]}</text></g>' for i in range(4))
    arrows=''.join(f'<path d="M {280+i*280} 290 h 38" stroke="#b98a57" stroke-width="5" marker-end="url(#a)"/>' for i in range(3))
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="500" viewBox="0 0 1200 500" role="img"><title>{title}</title><desc>Original four-stage bilingual process diagram.</desc><defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#b98a57"/></marker></defs><rect width="1200" height="500" fill="#f2eee5"/><text x="600" y="75" text-anchor="middle" class="zh" fill="#24344a">{title}</text><text x="600" y="120" text-anchor="middle" class="en" fill="#526274">{subtitle}</text>{arrows}{rects}<text x="600" y="425" text-anchor="middle" class="foot">AI Video Bible · Original editable SVG · Review pending</text><style>.zh{{font:600 24px "Noto Sans CJK TC",sans-serif;fill:#fff}}.en{{font:500 16px Arial,sans-serif;fill:#fff}}.foot{{font:14px Arial,sans-serif;fill:#657080}}</style></svg>'
    (figdir/f'CH10-FIG-{len(list(figdir.glob("*.svg")))+1:03}-{stem}.svg').write_text(svg,encoding='utf-8')

refs=[('R070','professional-resource','Nicholl Screenwriting Resources','Academy of Motion Picture Arts and Sciences','https://www.oscars.org/nicholl/screenwriting-resources','Format guidance and acknowledgement of variation; page scope only.'),('R071','official-registry-documentation','WGAW Registry','Writers Guild of America West','https://www.wgawregistry.org/','Registry information; legal effect and scope require professional review.'),('R072','official-statute','Copyright Law of the United States, Chapter 1, §§101–103','United States Copyright Office','https://www.copyright.gov/title17/92chap1.html','U.S. statutory text only; not legal advice or guidance for other jurisdictions.'),('R073','official-product-documentation','How do I use Revision Mode?','Final Draft Knowledge Base','https://kb.finaldraft.com/hc/en-us/articles/27813588722708-How-do-I-use-Revision-Mode','Vendor documentation; confirm features against installed product.'),('R074','official-product-documentation','How do I lock or unlock script pages and use the locking tools?','Final Draft Knowledge Base','https://kb.finaldraft.com/hc/en-us/articles/27817054455828-How-do-I-lock-or-unlock-script-pages-and-use-the-locking-tools','Vendor workflow documentation; not universal practice.'),('R075','format-specification','Syntax','Fountain','https://fountain.io/syntax/','Syntax specification; project tool interoperability not tested.'),('R076','film-catalog','The Wizard of Oz (1939)','American Film Institute','https://catalog.afi.com/Film/7892-THE-WIZARDOFOZ','Catalog and production-history evidence; not viewing or rights clearance.')]
with (R/'data/references.yaml').open('a',encoding='utf-8') as f:
    for id,typ,title,pub,url,note in refs:
        f.write(f"\n- id: {id}\n  type: {typ}\n  title: '{title}'\n  authors: ['{pub}']\n  publisher: '{pub}'\n  edition: null\n  publication_date: null\n  version: Page checked 2026-10-22\n  doi: null\n  url: {url}\n  accessed: '2026-10-22'\n  locator: Main page; limited to scope described in notes\n  language: en\n  status: verified-source-page-scope-limited\n  notes: {note}\n")
with (R/'metadata/references.bib').open('a',encoding='utf-8') as f:
    for id,typ,title,pub,url,note in refs:
        f.write(f'\n@misc{{{id},\n author = {{{pub}}},\n title = {{{title}}},\n publisher = {{{pub}}},\n year = {{2026}},\n url = {{{url}}},\n note = {{{note} Accessed 2026-10-22}}\n}}\n')

terms=[('SCREENPLAY','電影劇本','screenplay','供創作、閱讀及製作溝通的文本；格式服務於工作情境，不表示影像逐字照拍。','A text for creative work, reading, and production communication; format serves the task, not literal screen reproduction.',['R070']),('SCENE-HEADING','場景標題','scene heading','標示內外景、地點、時間等資訊的場景起始行；格式依採用規格或約定。','A scene-opening line identifying interior/exterior, location, and time; details depend on the adopted convention.',['R070','R075']),('SLUGLINE','場景行／slugline','slugline','劇本場景標題的常見業界稱呼；用語依地區與格式而異。','A common industry term for a screenplay scene heading; usage varies by region and format.',['R075']),('ADAPTATION','改編','adaptation','將既有材料重組為另一作品形式；創作和權利狀態不同。','Reorganizing existing material into another work form; creative method and rights status differ.',['R072']),('DERIVATIVE-WORK','衍生作品','derivative work','美國法中基於既有作品改編、轉換或改作的作品；不代表其他法域。','A work adapting or transforming a preexisting work under U.S. law; other jurisdictions may differ.',['R072']),('REVISION-SET','修訂稿次','revision set','標示特定修訂稿與變更的製作慣例；色彩由團隊定義。','A production practice identifying a revision and its changes; the team defines colors.',['R073']),('LOCKED-PAGES','鎖定頁','locked pages','製作中保留頁碼參照的版本方式；程序依工作流程。','A production method for preserving page references; procedure depends on workflow.',['R074']),('SCREENPLAY-INTERCHANGE','劇本交換格式','screenplay interchange format','在工具間傳遞劇本文字及結構的格式；轉檔後須驗證。','A format for transferring screenplay text and structure between tools; verify after conversion.',['R075'])]
with (R/'metadata/terminology.yaml').open('a',encoding='utf-8') as f:
    for suf,zh,en,zd,ed,rs in terms:
        f.write(f"\n- term_id: TERM-CH10-{suf}\n  preferred: {{zh-TW: '{zh}', en-US: '{en}'}}\n  definitions:\n    zh-TW: '{zd}'\n    en-US: '{ed}'\n  status: draft\n  reviewed_by: null\n  reviewed_on: null\n  references: [{', '.join(rs)}]\n  domain: screenwriting and production\n  context: CH10 working definition; bilingual terminology review pending.\n  synonyms: {{zh-TW: [], en-US: []}}\n  see_also: []\n")

# Targeted registry updates; preserve unrelated changes.
p=R/'metadata/chapters.yaml'; s=p.read_text(encoding='utf-8').replace("  title_en: ''\n  legacy_status: planned\n  zh_status: planned\n  en_status: translation-needed","  title_en: 'Screenplay Format, Adaptation, and Revision Management'\n  legacy_status: planned\n  zh_status: draft\n  en_status: review-needed",1); p.write_text(s,encoding='utf-8')
p=R/'metadata/translation-status.yaml'; s=p.read_text(encoding='utf-8').replace('  CH10:\n    zh-TW: planned\n    en-US: translation-needed\n    sync_revision: null','  CH10:\n    zh-TW: source-draft\n    en-US: review-needed\n    sync_revision: 2.1.0-draft',1); p.write_text(s,encoding='utf-8')

zhheads=['學習目標與適用對象','核心概念與專業術語','歷史與基本原理','傳統製作方法','AI 時代的技術轉換與限制','詳細工作流程','提示詞與技術參數','電影案例分析','常見錯誤與品質驗證','練習、評量與延伸研究','參考資料']
enheads=['Learning Objectives and Audience','Core Concepts and Professional Terms','History and Principles','Traditional Production Practice','AI-Era Technical Changes and Limits','Step-by-Step Workflow','Prompt and Technical Parameters','Film Case Study','Common Errors and Quality Checks','Exercises, Assessment, and Further Research','References']
align={'chapter_id':'CH10','source_locale':'zh-TW','target_locale':'en-US','source_revision':'2.1.0-draft','target_revision':'2.1.0-draft','status':'review-needed','reviewed_by':None,'reviewed_on':None,'sections':[{'id':f'CH10-S{i:02}','zh':z,'en':e} for i,(z,e) in enumerate(zip(zhheads,enheads),1)],'terms':[f'TERM-CH10-{t[0]}' for t in terms],'references':[x[0] for x in refs],'figures':[{'id':f'CH10-FIG-{i:03}','display_number':f'10-{i}','section_id':'CH10-S08','zh_title':defs[i-1][1],'en_title':defs[i-1][2],'caption_id':f'CH10-CAP-{i:03}'} for i in range(1,4)],'editorial_note':'English working translation; bilingual and professional review pending.'}
(R/'metadata/translations/CH10-alignment.yaml').write_text(yaml.safe_dump(align,allow_unicode=True,sort_keys=False),encoding='utf-8')

figures=[]
captions=['# CH10 雙語圖說與替代文字\n']
rights_names=['稿件版本生命週期','改編來源與審查分流','以場景 ID 核對改稿']
altz=['四個稿件版本節點以箭頭連接，呈現創作稿、修訂稿、製作稿和交付封存。','流程圖分列底本材料、權利審查、創作選擇及新劇本，並標示法律審查閘門。','流程圖比較同一場景 ID 的前稿和改稿，產生差異摘要後交由人員判讀。']
alte=['Four version nodes connect a writing draft, revision drafts, production draft, and archived delivery.','A diagram separates source material, rights review, creative choices, and a new screenplay, with a legal-review gate.','A diagram compares earlier and revised drafts for one scene ID, summarizes differences, and routes them to human review.']
captz=['版本需追溯來源、作者、變更和交付狀態；流程是本書工作模型。原創可編輯 SVG 示意圖，非電影劇照；署名、權利及出版核准待審。','創作轉化紀錄與權利審查分開留存；圖示不構成法律意見。原創可編輯 SVG，未描繪特定作品；權利與出版核准待審。','差異工具提供核對線索，作者判斷是否採納及影響部門。原創可編輯 SVG，非正式劇本頁面；權利及出版核准待審。']
capen=['Versions should trace source, author, changes, and delivery status; this is a working model. This is an original editable SVG illustration for this book, not a film still. Attribution, rights, and publication approval are pending.','Creative transformation and rights review need separate records; this diagram is not legal advice. This is an original editable SVG illustration for this book and depicts no specific work. Rights and publication approval are pending.','Diff tools provide review cues; authors decide whether to accept changes and which departments they affect. This is an original editable SVG illustration for this book, not a production screenplay page. Rights and publication approval are pending.']
filenames=['CH10-FIG-001-revision-lifecycle.svg','CH10-FIG-002-adaptation-map.svg','CH10-FIG-003-change-review.svg']
for i,fname in enumerate(filenames):
    path=figdir/fname; raw=path.read_bytes(); ET.parse(path); display=f'10-{i+1}'; sec=['CH10-S06','CH10-S08','CH10-S09'][i]
    fig={'figure_id':f'CH10-FIG-{i+1:03}','chapter_id':'CH10','section_id':sec,'placement_after':f'after:{sec}','source_ids':[['R073'],['R072'],['R073']][i],'asset_original':path.relative_to(R).as_posix(),'asset_approved':None,'rights_review':'pending','technical_review':'pending','editorial_review':'pending','publication_status':'pending-publication-approval','display_number':display,'asset_status':'draft-original-svg','rights_status':'original-project-svg-pending-human-review','sha256':hashlib.sha256(raw).hexdigest(),'width':1200,'height':500,'bytes':len(raw),'method':'Hand-authored editable bilingual SVG; no image model or third-party image.','caption_zh':f'圖 {display}｜{captz[i]}','caption_en':f'Figure {display}. {capen[i]}','alt_zh':altz[i],'alt_en':alte[i],'creator':'AI Video Bible project; individual attribution pending confirmation','attribution':'Creator and rights-holder attribution pending confirmation.','permission':'Publication approval pending.','original_prompt_or_method':'Hand-authored SVG geometry and bilingual labels; no generated or third-party artwork.','production_log':[{'date':'2026-10-22','change':'Created as an original editable diagram; SHA-256 recorded.'}],'review_status':{'technical':'pending','quality':'pending','rights':'pending','final':'pending'},'approval_status':'pending','publication_targets':{'zh-TW-book':'pending','en-book':'pending','zh-TW-site':'pending','en-US-site':'pending'}}
    figures.append(fig); captions.append(f"\n## {fig['figure_id']}｜Figure {display}\n\n- zh-TW：{fig['caption_zh']}\n- en-US：{fig['caption_en']}\n- alt zh-TW：{altz[i]}\n- alt en-US：{alte[i]}\n- 狀態：draft；人工權利與出版核准待辦。\n")
(R/'assets/chapters/CH10/figure-manifest.yaml').write_text(yaml.safe_dump({'chapter_id':'CH10','figures':figures},allow_unicode=True,sort_keys=False),encoding='utf-8')
(R/'assets/chapters/CH10/figure-captions.md').write_text(''.join(captions),encoding='utf-8')

for p,txt in [(R/'assets/chapters/CH10/CH10-FIGURE-RIGHTS-AND-SOURCES.md','# CH10 插圖來源與權利紀錄\n\n三張圖為本專案手工編寫的可編輯 SVG；未用第三方圖像、網路圖片、電影劇照或圖像生成服務。尺寸與 SHA-256 記於 `figure-manifest.yaml`。作者署名、可及性、技術、相似性／權利及出版審查均 pending；`asset_approved: null`。不得當作正式出版插圖。R076 只支持片目／製作史線索，不支持鏡頭級分析。\n'),(R/'assets/chapters/CH10/CH10-SOURCE-AND-CASE-NOTES.md','# CH10 來源與案例研究紀錄\n\n來源 R070–R076 已登錄至 `data/references.yaml` 與 BibTeX，查閱日 2026-10-22。R070 Academy 格式指引；R071 WGAW Registry；R072 美國著作權法；R073–R074 Final Draft 修訂／鎖頁文件；R075 Fountain 語法；R076 AFI《綠野仙蹤》條目。各來源只支持其頁面明示範圍。未完成書籍定位、法律審核、實際軟體轉檔和電影觀片版次／時間碼查核。\n'),(R/'assets/chapters/CH10/CH10-HUMAN-REVIEW-CHECKLIST.md','# CH10 待人工審查\n\n- [ ] 作者核定章名、篇章界線和程序。\n- [ ] 雙語編輯校譯英文及術語。\n- [ ] 電影專業編輯核對格式史與市場差異。\n- [ ] 作者選定合法片源／底本版本並記錄頁碼、時間碼和觀片紀錄。\n- [ ] 法律專業人員核對改編權利、權利鏈及法域陳述。\n- [ ] 審查 SVG 署名、可及性、技術品質、權利與出版核准。\n- [ ] 網站及 PDF／EPUB 視覺校樣和作者最終簽核。\n\n未完成前皆維持 draft/pending，不得標示 publication-ready。\n')]: p.write_text(txt,encoding='utf-8')

# Append structured records without rewriting heterogeneous legacy data.
fr=R/'metadata/figure-registry.yaml'; fd=yaml.safe_load(fr.read_text(encoding='utf-8')); fd['figures'].extend([{'figure_id':f['figure_id'],'display_number':f['display_number'],'section_id':f['section_id'],'zh_title':rights_names[i],'en_title':defs[i][2],'caption_id':f"CH10-CAP-{i+1:03}"} for i,f in enumerate(figures)]); fr.write_text(yaml.safe_dump(fd,allow_unicode=True,sort_keys=False),encoding='utf-8')
with (R/'data/assets.yaml').open('a',encoding='utf-8') as f:
    for x in figures: f.write(f"\n- id: ASSET-{x['figure_id']}\n  path: {x['asset_original']}\n  type: original-svg-diagram\n  description: {x['caption_zh']}\n  creator: AI Video Bible project; individual attribution pending\n  source_url: null\n  created_at: '2026-10-22'\n  license: Unconfirmed pending author review\n  permission: Not approved for publication\n  attribution: Creator review pending\n  chapter_ids: [CH10]\n  figure_id: {x['figure_id']}\n  sha256: {x['sha256']}\n  notes: Original SVG; accessibility, technical, rights, and publication reviews pending.\n")

lp=R/'scripts/publishing/figure-captions.lua'; s=lp.read_text(encoding='utf-8'); needle='  ["CH09-FIG-003"] = "9-3",'; s=s.replace(needle,needle+'\n  ["CH10-FIG-001"] = "10-1",\n  ["CH10-FIG-002"] = "10-2",\n  ["CH10-FIG-003"] = "10-3",'); lp.write_text(s,encoding='utf-8')
print('CH10 authored and registered:',len(ZH),'ZH chars,',len(EN),'EN chars,',len(figures),'SVG figures')
