# V2 電影知識整合與遷移計畫

更新：2026-10-19（Asia/Taipei）。本計畫是對既有 V2 專案的增量整合，不重建專案、不重排既有章節、不自動把 staging 稿升為 canonical。

## 基準與保護範圍

- 專案基準：`main` / `6481fd3`；盤點時 `origin/main` 與本地 HEAD 相同。
- 工作區有大量既有未提交變更。這些變更視為作者／先前任務在進行的工作；本輪只新增知識架構文件、現況報告、導覽入口與歷史紀錄，不整理、不重置、不提交、不推送。
- V1 檔案保留於既有 `chapters/` 及遷移備份；V2 canonical bilingual source 在 `content/`。任何 V1/V2 原稿、圖片、ZIP、staging 均不因本計畫搬動或覆蓋。
- CH01 為已有完整草稿但有專業／權利人工待審；CH02 是實質雙語 staging 稿和素材包，canonical 整合、語意翻譯、案例及網站 route 仍有阻擋；CH03 只有中英 scaffold，尚無證據顯示已開始撰稿。
- 工作區既有修改中包含 CH01、CH02 稿件與大量素材，因此明確排除這些檔案的本輪修改。

## 整合方式

1. 將十二大電影元素集中在 `FILM_ELEMENTS.md`；每章只引用其實際適用的 `FE01`–`FE12`。
2. 將八大 AI 製作系統及狀態／交接定義集中在 `AI_PRODUCTION_SYSTEMS.md`；排除 Cinetic 和 TTS，僅把 Remotion、Manim、Blender、ComfyUI 留在待驗候選，不宣稱已整合。
3. 以 `CHAPTER_INTEGRATION_MATRIX.md` 顯示 60 章的現況證據、缺口、補強位置和風險。模板 scaffold 不當成內容覆蓋。
4. 以 `FILM_QUALITY_RUBRIC.md` 區分人類創作評分和機器可測的檔案／出版閘門；Rubric 分數不得替代權利／作者核准。
5. `CHAPTER_TEMPLATE_V2.md` 僅作入口，保留 `templates/chapter-v2.md` 為 canonical 模板，避免兩套正文模板漂移。
6. 原有 V2 SOP、章節 pipeline、術語／翻譯／引用／圖片權利／出版文件保持為執行規範；本次新增文件連結它們，不覆寫其既有工作流。

## 第一至第三章補強計畫

| 章 | 狀態及基準 | 低風險補強位置 | 不在本輪做的事 | 風險／前置 |
|---|---|---|---|---|
| CH01 | 中英 substantive draft；最新報告仍列專業來源、雙語、圖稿權利／原創性與作者核准待辦 | 先將 FE 分類及章節交叉引用在 acceptance／matrix 層呈現；其後由章節編輯查證補充 | 不改稿、caption、manifest、圖檔、術語與已完成出版 proof | 需研究者、雙語編輯、圖像權利審查及作者核准 |
| CH02 | `staging/CH02-V4/` 為中英實質 staging 稿；32 項 audit 為 PASS 18、NEEDS HUMAN REVIEW 12、BLOCKED 1、NOT RUN 1 | mapping 指向場面、攝影、剪接、觀眾觀看；編輯完成後再整合 canonical、網站 route 和 reference locator | 不搬入、不覆蓋 staging／canonical、不更改永久圖號 | 需編輯核准、來源／片段核實及網站內容同步 |
| CH03 | `metadata/chapters.yaml` 有中英 scaffold；正文模板仍空，manifest `figures: []`；未發現章節 staging/run/assets | 將景別／視點主題映射至 FE04、FE12、AIS02、AIS05；正式寫作前研究／案例規劃 | 不自行開始撰稿、不把 scaffold 標為涵蓋 | 需先確認章節作者 brief 及英文章名 |

## 工具整合順序

| 順序 | 動作 | 完成條件 | 禁止條件 |
|---|---|---|---|
| 1 | 建置既有 schema、matrix、Rubric validator | 60 個 ID、來源欄位、狀態標籤可重複驗證 | 不回寫章稿 |
| 2 | CH01 / CH02 對照矩陣進編輯會議 | 每個 gap 指定責任角色、來源和插入點 | 未核實來源不可標 COVERED |
| 3 | 人工核准後執行 chapter-specific additions | 備份、diff、引用及雙語對照通過 | 禁止覆寫原稿或重做已完成資產 |
| 4 | 評估候選程式工具（Remotion / Manim / Blender / ComfyUI） | 隔離 prototype、固定版本／授權／hash、重現測試 | 本計畫不安裝模型、不產生費用、不抓未授權權重 |
| 5 | 達到人工 review 與出版閘才可 release | 章末完整驗收、作者簽核、當次輸出證據 | 無作者授權不部署、不推送 GitHub |

## 本輪範圍及退回條件

新增五份核心知識／規劃文件、一份模板入口、一份現況報告、README/CHANGELOG/history 導覽紀錄；不改章稿、不修改 chapter registry／模板本體、不執行出版或 AI 工具安裝。若未來發現碰到原章節或素材衝突，立即停止該檔編輯，保留 backup 與 diff，改列計畫。
