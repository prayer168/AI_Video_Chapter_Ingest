# CH01 V2 編輯與插圖權利審查紀錄

- 審查日期：2026-10-18（Asia/Taipei）
- 審查者：Codex（自動化結構與編輯初審）
- 範圍：雙語 canonical 稿、CH01 figure manifest、插圖 briefs、圖片政策
- 結論：**審查已執行；章稿退修，插圖尚無可核准的成品。不可標為正式核准。**

## 編輯審查結果

### 已檢查

- 繁中與英文稿使用相同章節及段落 ID；目前 CH01-S01–S12 主要錨點相配。
- 五組電影案例有中英對應 paragraph ID，並區分影片資料、評論性解讀、實務轉譯及未實測練習。
- 引用 ID R013–R021 在兩語參考文獻中配對；章稿明確聲明尚缺觀看版本、場景 timecode 和更完整的電影理論來源。
- 英文正文仍大量使用中文參考文獻說明，缺少完整逐節翻譯與專業英文審校。

### 必須退修

1. 九個主要章節區塊只有標題或空白：學習目標、先備知識、歷史與原理、傳統製作方法、AI 技術轉換、詳細流程、提示詞與參數、常見錯誤／品質檢查、練習／評量／延伸研究。
2. 五個案例需補合法觀看版本、可複查的場景描述及該版本 timecode；電影史／理論總述需加入專業學術來源。不得從評論文章推導未被來源支持的普遍理論結論。
3. 英文題名仍標為待編；英文稿需逐節翻譯並由具電影製作／電影研究能力的編輯審校。
4. 六個術語需核對全專案首選詞、來源支持及適用語境；實際頁碼／定位只有在核對指定版本後才填入。

**狀態：** 本次 Codex 審查完成，結果為 `review-needed`（退修），不是 `approved`。`metadata/translation-status.yaml` 及章稿原本的 `draft-migration-pending`／`translation-needed` 狀態保留，正式書籍 gate 繼續阻擋。

## 插圖權利與技術審查結果

- 檢視 `assets/chapters/CH01/figure-manifest.yaml`：5 個項目只有 brief，`asset_original`、`asset_approved` 皆為空，生成工具／版本／日期未記錄，三項審查均為 `pending`。
- 兩語 CH01 正文沒有嵌入圖片或外部圖片 URL；目前沒有第三方網路圖片被納入章稿，也沒有可供權利審查的實際插圖檔。
- 因缺少成品，不能核驗像素／向量來源、人物肖像、標誌、相似構圖、修改紀錄或成品 caption／alt 與教學目的的一致性。
- 五個規劃項目保持 `pending`，不宣稱權利已核准。製作原創可編輯 SVG 或原創生成圖後，須把完整來源與修改紀錄登錄到 figure manifest 及 `data/assets.yaml`，再做權利風險、技術、編輯及作者發布目標審查。
- V1 `ASSET-CH01-FIG-01` 的授權／作者資料另屬待確認項目；在取得權利證據或正式排除該資產前，不得納入 V2 出版品。

## 本輪工程問題修復證據

| 項目 | 結果 | 證據 |
|---|---|---|
| Astro Duplicate ID | PASS | 檢查目前每語各 1 份 CH01 Markdown；`npm --prefix apps/web run build` 產生 123 頁，乾淨建置 log 無 `Duplicate id`；中英文 CH01 HTML 路由皆存在。舊警告本輪未能重現，因此不推定歷史根因。另移除過期手寫 sidebar link，改用 Starlight 語系導覽，避免中英導覽都指向不存在的 `/zh-tw/ch01/`。 |
| PDF 字型與缺字 | PASS（草稿技術檢查） | 兩語 CH01 PDF 先前及本輪檢查紀錄：strict `pdffonts` 字型嵌入成功、XeLaTeX missing-character 警告 0。正式完整書校樣仍須重驗。 |
| EPUBCheck | PASS（草稿 EPUB 符合性） | W3C／DAISY EPUBCheck 5.4.0；兩語 draft EPUB 各 0 errors、0 warnings、0 informational messages、0 references。 |
| 內容審查 | REVIEW NEEDED | 已完成初審並提出退修清單；章稿結構不完整，不能提升至正式核准。 |
| 插圖權利 | PENDING | 5 個圖片 brief 尚無檔案；未發現已嵌入第三方圖片。沒有可供成品權利簽核的資產。 |

## 出版狀態

本報告解除網站重複 ID 訊息和 EPUBCheck 缺席問題，並確認 PDF 技術缺字警告已歸零。章節編輯核准和插圖權利核准不是工具可代簽項目；目前實際稿件未達核准條件。此狀態代表審查已完成並退修，不代表完整章節已審稿通過或取得正式發行許可。
