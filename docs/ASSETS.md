# 影像、影音與圖表資產管理

正式插圖必須遵守[插圖原創與著作權管理規範](IMAGE-RIGHTS-POLICY.md)。本文件補充儲存和媒體管理方式；圖片元資料以 `schemas/image-asset.schema.json` 為準。


## 目錄與命名

- 原始可編輯檔放在 `assets/` 下適當分類：`images/`, `audio/`, `video/`, `diagrams/`。
- 使用描述性小寫 ASCII 檔名，以連字號分詞；如 `shot-reverse-shot-diagram.svg`。
- 章節引用資產使用相對路徑，避免個人電腦絕對路徑。
- 生成或編修資產保留可編輯源檔及生成流程記錄；大型二進位檔先評估 Git LFS 或外部授權儲存。

## 每項資產的權利紀錄

在 `data/assets.yaml` 登記完整的圖號、段落、教學目的、研究來源與查證日期、雙語圖說、原創提示詞／繪圖方法、工具版本、製作修改紀錄、權利風險及分目標審查狀態。圖像來源與作者未知時留 `null` 或「待確認」，授權填 `Unconfirmed`，並保持 `pending`。

## 技術與內容要求

- 圖片優先使用可編輯 SVG 或無損來源檔；網頁交付的衍生圖記錄尺寸、色彩空間和轉檔方式。
- 影音記錄編碼、解析度、影格率、聲道、字幕及時間碼；不得將未授權電影片段提交到倉庫。
- 提供替代文字、字幕或文字稿；確認對比、色彩與資訊不只靠顏色呈現。
- 發佈前檢查外部資產連結、授權聲明、隱私和檔案中繼資料。

## 出版關卡

`python scripts/validate_project.py` 檢查圖片登錄、schema 及章稿引用；`python scripts/image_policy.py --target zh-TW-site --include-docs` 檢查正式繁中網站插圖核准狀態。正式建置會自動阻擋未登錄、外部或未核准圖片；`--preview` 會以待審文字代替圖片，並輸出到 `dist/preview/`。
