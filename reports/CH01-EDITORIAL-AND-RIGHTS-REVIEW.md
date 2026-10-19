# CH01 V2 編輯與插圖權利審查紀錄

> **狀態更正（2026-10-18，V2.1.0／V4）：** 下方「插圖權利審查」及「技術驗收摘要」是五張 PNG 匯入前的歷史檢查，不能代表目前資產狀態。五張圖已匯入 `assets/chapters/CH01/figures/originals/`，並列於 `assets/chapters/CH01/figure-manifest.yaml`；實際檔案、SHA-256、圖說、alt 及 pending 權利狀態以 [`CH01-FINAL-ACCEPTANCE.md`](CH01-FINAL-ACCEPTANCE.md) 和 [`IMPORT-AND-RIGHTS-RECORD.md`](../assets/chapters/CH01/figures/IMPORT-AND-RIGHTS-RECORD.md) 為準。圖片來源 metadata 不完整，rights／technical／editorial review 仍 pending。CH01 尚未達正式出版標準。

- 更新日期：2026-10-18（Asia/Taipei）
- 審查者：Codex（自動結構、來源登錄與編輯初審；非出版核准人）
- 最新完整結果：[`CH01-FINAL-ACCEPTANCE.md`](CH01-FINAL-ACCEPTANCE.md)
- 狀態：**章節必要正文已補齊；仍為 `review-needed`，未達正式出版標準。**

## 本輪處理

初版審查發現的 9 個空白必要區塊，已在中英文 canonical 稿逐項補成正文。新增／補強學習目標、先備知識、歷史與基本原理、傳統製作方法、AI 技術轉換、鏡頭級流程、模型中立提示詞與示範、常見錯誤及品質檢查、練習／評量／研究問題，並建立結語。另完成五組中英電影案例和六鏡頭虛構教學案例。

中英 section anchors 為 CH01-S01–S13；案例 IDs 為 CH01-P001–P005。26 個雙語術語已加入 `metadata/terminology.yaml`，所有詞條維持 `draft`。逐節、術語、案例及圖說對照見 `metadata/translations/CH01-alignment.yaml`。

來源使用範圍已收窄：早期電影歷史主張限定於 Library of Congress 所收美國電影約 1907–1913 的材料；Kuleshov 段落同時標出 2016 及 2024 研究的特定設計與限制；未能支持的《悲情城市》長鏡頭／門框主張已刪除。R017 New Yorker 頁面未作正文證據。教科書頁碼、完整研究評估、電影版本與場景 timecode 仍待人工審稿。

## 插圖權利審查

- 實際遞迴檢查 `assets/chapters/CH01/`：只有五份圖像 brief 和 manifest，沒有對應實際 raster／SVG 圖檔。
- 五個 figure records 的 `asset_original`、`asset_approved`、生成工具／版本／日期皆為 null；權利、技術和編輯狀態全為 `pending`。
- 雙語 CH01 章稿沒有嵌入圖檔或外部圖片 URL；本輪未用網路圖片。
- 雙語圖說與 alt 已細化，但明確只是待核准文案，不代表圖片已生成。
- 舊 V1 `ASSET-CH01-FIG-01` 權利／作者證據仍未解；它沒有納入 V2 CH01 正文，專案正式圖像 gate 仍須補權利證據或由作者明確記錄排除。

## 技術驗收摘要

- Astro `check` 最新結果：0 errors／warnings／hints。更新 CH01 投影後第一次增量載入曾印出兩筆 CH01 Duplicate ID；檢查 Astro loader 後確認它在更新相同 ID、不同內容 digest 的既有 store entry 時也印出此訊息。立即重跑 0 warnings；每語系來源檔各只有一份。
- Astro 靜態建置：123 pages，包含中英 CH01 路由；最終 build 無 Duplicate ID 警告，未部署。
- 雙語章節 PDF：Microsoft JhengHei 與 Times New Roman 字型嵌入通過，缺字警告 0；已抽取文字並抽查繁中頁 2–4。
- 雙語章節 EPUB：EPUBCheck 5.4.0 各 0 errors／warnings／informational messages／references。首次 EPUBCheck 的缺少來源 anchor 問題已修正並重建重測。
- 全套 Python unittest：27/27 通過；新增 5 個 CH01 完整度、翻譯配對、引用錨點及圖片未核准測試。
- V2 validator、專案 registry 驗證、網站投影檢查、local link check 及 `git diff --check` 通過。

## 尚須人工作業

1. 作者提供五部片合法觀看版本、發行／修復版本及可複查時間碼，完成逐鏡核對。
2. 電影研究者核對電影史／理論及術語定義；依採用教材版本補上準確頁碼或章節定位。
3. 專業雙語編輯逐節審校英文、術語、電影譯名和引用；兩語審查均完成後才能將狀態升至 `approved`。
4. 製作或決定排除五項原創插圖；如製作，先登記實檔、prompt／繪圖源、工具版本、修改紀錄及權利證據，完成技術、編輯和權利審查後才可納入。
5. 查明 V1 圖像資產權利並記錄正式處置。
6. 核准稿後重做完整 PDF／EPUB 閱讀器和全頁校樣；其他 59 章也需完成核准才能正式建置全書。

不得將本紀錄理解為出版批准。詳細狀態、證據路徑及每個驗收項目請以 [`CH01-FINAL-ACCEPTANCE.md`](CH01-FINAL-ACCEPTANCE.md) 為準。
