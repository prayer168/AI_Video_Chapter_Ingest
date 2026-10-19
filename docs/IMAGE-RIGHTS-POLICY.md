# AI Video Bible｜插圖原創與著作權管理規範 V1.0

- 規範 ID：`POLICY-IMAGE-RIGHTS-1.0`
- 生效日期：2026-10-18
- 適用範圍：繁體中文書籍、英文書籍、繁體中文網站、英文網站，以及對應的 PDF、EPUB、DOCX 和正式 HTML 輸出。
- 狀態：已納入專案；未完成必要審查的圖片維持 `pending`，不得進入正式出版輸出。

## 1. 基本原則

所有正式出版插圖必須為本專案原創製作，或已取得適當使用授權。網路搜尋取得的圖片僅供研究、理解技術與視覺參考，不得直接複製或下載後嵌入正式出版內容。

## 2. 原創製作方式

優先使用 ChatGPT Images 生成原創電影風格插圖；技術圖解優先採自行設計的 SVG、向量圖或程式化繪圖。不得直接重製、描摹或高度模仿特定第三方作品的獨創性表現。研究參考和視覺靈感要登錄來源及查閱日期，不把參考圖當成可出版素材。

## 3. 每張插圖的登錄資料

在 `data/assets.yaml` 為每張圖片建立穩定資產 ID，並使用 `schemas/image-asset.schema.json` 驗證。至少記錄：

- 圖號、檔案路徑、對應章節段落、教學目的及中英文圖說。
- 研究來源 ID、查證日期、用途及可確認的章節／頁碼定位。
- 原創提示詞或繪圖方法；生成工具及版本（可取得時）。未知資料明確填 `null` 或「待確認」，不得推測。
- 作者／創作者、製作日期（可確認時）、原始可編輯檔及每次製作／修改紀錄。
- 第三方作品、人物肖像、商標、訓練／參考輸入等權利風險審查結果。
- 技術、品質、權利及最終核准狀態，並分別記錄四種出版目標：`zh-TW-book`、`en-book`、`zh-TW-site`、`en-site`。

AI 生成圖像不得在未確認情況下宣稱具有完整、排他的著作權。`license` 與 `permission` 欄位應記錄有根據的權利狀態；不確定即填 `Unconfirmed` 並保持待審。

## 4. 正式出版關卡

圖片只有在以下條件全部成立，且對應出版目標核准後，才會被出版工具納入：

1. 圖片在 `data/assets.yaml` 有完整且通過 schema 的資產紀錄。
2. 研究來源、雙語圖說、提示詞／繪圖方法、工具版本（如可取得）及製作修改紀錄已填寫。
3. 技術、品質、權利風險及最終審查均為 `approved`。
4. 該圖片指定的出版目標為 `approved`，而非 `pending` 或 `rejected`。
5. 權利、授權及創作者／致謝資訊可追溯；不能因為圖像為 AI 生成就推定具有排他著作權。

正式建置 `scripts/build.py` 預設採 fail-closed：發現章稿引用的外部圖片、未登錄圖片或未核准圖片時，拒絕產生正式 HTML、DOCX、PDF 或 EPUB。網路圖片不得作為插圖缺口替代品。

草稿審閱可使用 `--preview`。預覽會將未核准圖片替換成「插圖待審核」文字，並省略該圖檔；輸出固定位於 `dist/preview/`，頁面／文稿會標記為草稿預覽，不可作正式出版物。

## 5. 例行命令

```powershell
# 查看繁中網站能否正式出版（不建置）
python scripts/image_policy.py --target zh-TW-site --include-docs

# 查看繁中書籍 PDF／EPUB／DOCX 能否正式出版（不建置）
python scripts/image_policy.py --target zh-TW-book

# 正式建置：未核准圖像將使命令中止
python scripts/build.py --format html
python scripts/build.py --format docx
python scripts/build.py --format pdf
python scripts/build.py --format epub

# 編輯中預覽：排除未核准圖像，輸出到 dist/preview/
python scripts/build.py --format html --preview
python scripts/build.py --format pdf --preview --font "PMingLiU"
```

英文書籍及英文網站在建立相應出版來源後，先分別執行 `python scripts/image_policy.py --target en-book` 或 `--target en-site`；不能以繁中版核准狀態替代英文目標核准。

## 6. 品質與權利審查規則

- 自動檢查確認資產登錄、必填欄位、來源 ID、目標核准狀態及未核准圖片是否被排除；自動化結果不替代人類權利審查。
- 每個章稿引用的圖片都要能對應唯一資產紀錄；外部圖片 URI、未登錄圖檔及內嵌 SVG 均不通過正式出版檢查。
- 有第三方作品、人物肖像、商標或不明參考輸入時，需補充審查證據或改為自製替代圖。
- 只有完成技術、內容品質、權利及目標出版審查後，才可以把圖片狀態改成核准。任何一項狀態改變均需在版本控制中留下可追溯變更。

## 7. 已知資產處理

第一章圖 1-1 為手工編寫的 SVG 教學圖，但目前作者、授權和歷史修改記錄未能完整追溯。登錄已降為 `Unconfirmed`／`pending`，正式出版建置會阻擋此圖；草稿預覽會省略圖片並顯示待審文字。須由編輯確認創作者及權利依據，再進行技術與品質核准。
