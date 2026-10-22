# CH08 最終驗收｜場景、節拍、對白與潛台詞

- 日期：2026-10-21（Asia/Taipei）
- 版本：2.1.0-draft
- 狀態：研究草稿完成；雙語、案例、來源定位與圖片權利仍待人工審查；**未達正式出版標準**。
- Run：`production/runs/CH08/20261021T200413+0800-16f990d8/`
- 編輯前備份：`production/runs/CH08/20261021T200413+0800-16f990d8/backup/pre-edit/MANIFEST.json`（17 個檔案及 SHA-256）
- 草稿輸出：`tmp/CH08-draft-20261021-r1/`
- 範圍：完成 CH08 雙語研究草稿、來源／術語／翻譯登錄、兩張原創 SVG、網站本機建置與 DOCX/PDF/EPUB 草稿測試；沒有改寫 CH01–CH07 正文，未發布網站、未 commit、未 push。

## 逐項驗收

| 檢查項目 | 狀態 | 實際證據與限制 |
|---|---|---|
| 必要章節區塊 | PASS（草稿結構） | 中英文均有 CH08-S01–S12：學習目標、先備知識、術語、歷史／原理、傳統方法、AI 技術轉換、詳細流程、提示詞、電影案例、錯誤／品質檢查、練習／評量／研究、參考資料。`tests.test_ch08_content` 檢查穩定錨點及非佔位內容。 |
| 繁中正文 | PASS（研究草稿）／NEEDS HUMAN REVIEW | 草稿已依章節模板撰寫；理論詮釋、編劇實務及課程適用性仍待電影／編劇專業編輯審閱。 |
| 英文對譯 | PASS（工作譯稿與段落結構）／NEEDS HUMAN REVIEW（語言） | `metadata/translations/CH08-alignment.yaml` 對齊 12 節、8 個詞條及 2 張圖。英文不是已核准譯文，需雙語編輯校譯。 |
| 術語 | PASS（登錄）／NEEDS HUMAN REVIEW（核定） | 8 個 TERM-CH08 詞條有繁中／英文建議詞形，狀態均為 `draft`；尚未核定為全書標準譯名。 |
| 參考來源與事實追溯 | PASS（登錄與限定）／NEEDS HUMAN REVIEW（主張定位） | R051、R058–R065 已登錄 YAML/BibTeX。出版者記錄、摘要、片目與教學資料的查證範圍和限制記於 `assets/chapters/CH08/CH08-SOURCE-AND-CASE-NOTES.md`。R058–R060、R062、R065 的全文／精確頁碼仍需按採用版本核對；Screenplayology 的 beat 分類標為實務資源，不宣稱普遍標準。 |
| 電影案例 | NEEDS HUMAN REVIEW | *Sweet Smell of Success* 及 *His Girl Friday* 的論述歸屬於可追溯二手資料或 AFI 片目；沒有聲稱已親看特定版本、沒有補造時間碼，也未引用電影對白。作者／編輯仍須決定合法觀看片版次、字幕、片長及是否需要 timecode。 |
| AI 技術說明與提示詞 | PASS（保守草稿）／NEEDS HUMAN REVIEW | 使用模型中立流程及示範提示詞，不宣稱未測的供應商功能或參數；需在採用工具時按官方文件／實測更新。 |
| 原創插圖與來源紀錄 | PASS（檔案／登錄）／NEEDS HUMAN REVIEW（權利／出版） | CH08-FIG-001、002 為本專案手繪可編輯 SVG，已記錄檔案路徑、SHA-256、製作方法、尺寸、雙語 caption／alt 及對應節次；SVG XML 解析與 hash 測試通過。沒有第三方圖片或生圖服務。圖稿作者個別署名、相似性、可及性、印刷品質、權利與出版許可均 pending，`asset_approved: null`、`approval_status: pending`。 |
| 中英文圖文同步 | PASS（資料一致） | `figure-manifest.yaml`、`figure-captions.md`、translation alignment、兩語正文及全域 registry 對應永久圖號 CH08-FIG-001/002，建議顯示圖 8-1／8-2。 |
| 網站同步／Astro check | PASS | `python scripts/publishing/sync_site_content.py --check` 通過；最終 `npm --prefix apps/web run check`：0 errors、0 warnings、0 hints。首次在同步前曾短暫顯示 duplicate loader ID，重新同步及後續乾淨 check/build 後未重現。 |
| 網站本機建置與路由 | PASS（未發布） | `npm --prefix apps/web run build` 成功，產出 123 頁。`/zh-tw/ch08-chapter-08/`、`/en/ch08-chapter-08/` 均存在；兩頁各有 39 個唯一 HTML IDs、2 張圖且 alt 非空。 |
| DOCX 草稿 | PASS（建置） | `tmp/CH08-draft-20261021-r1/CH08-zh-TW-draft.docx`、`CH08-en-US-draft.docx` 成功產生；SVG 原始檔保留。 |
| PDF 草稿、字型嵌入與文字抽取 | PASS（技術）／NEEDS HUMAN REVIEW（校樣） | 中英文 PDF 成功產生；strict `scripts/check_fonts.py --require-pdffonts` 各通過，檢查到繁中 Microsoft JhengHei 嵌入，所有列出的字型 `emb/sub/uni=yes`。PyMuPDF 抽取皆 0 個 U+FFFD；中文 9 頁、英文 12 頁，圖 8-1／8-2 各出現一次。校樣頁 PNG 已渲染並抽頁目視，仍需全章編輯校樣。 |
| EPUB 草稿與 EPUBCheck | PASS（格式） | 中英文 EPUB 均成功產生，EPUBCheck 5.4.0 各為 0 fatal errors、0 errors、0 warnings、0 informational references。此為格式驗證，不代表內容／出版核准。 |
| CH08 專項測試 | PASS | `python -m unittest tests.test_ch08_content -v`：5/5 PASS，涵蓋雙語錨點、8 個詞條、來源 ID、SVG XML/hash、雙語圖說／alt／pending 權利及非佔位內容。 |
| 全專案 validators | PASS | `python scripts/v2_validate.py` PASS；`python scripts/validate_project.py` PASS（12 parts、60 planned chapters、52 terms、60 references）；`sync_site_content.py --check` PASS。 |
| 全專案單元測試 | FAIL（既有 CH01 問題） | `python -m unittest discover -s tests -v`：66 tests，65 PASS、1 ERROR。錯誤為 `tests.test_ch01_content...test_chapter_terms_are_bilingual_and_registered` 的既有 CH01 詞條缺少 `status` 欄位而觸發 KeyError；CH07 先前整套測試也記錄同一錯誤。本輪遵守章節保護原則，沒有修改 CH01。 |
| 圖片正式出版閘門 | BLOCKED（預期） | `python scripts/image_policy.py --target zh-TW-book` 與 `--target en-book` 均以 exit 2 阻擋；回報目前專案中 CH01 等既有圖片尚缺核准、作者歸屬及授權。CH08 兩張圖本身也仍為 pending。草稿輸出不代表通過正式發布閘門。 |
| 作者／專業簽核 | NEEDS HUMAN REVIEW | 依作者指示，等全書章節完成後集中簽核；本章不得標記 `publication-ready`。 |

## 尚待完成

1. 電影／編劇專業審閱場景目標、節拍、潛台詞與案例詮釋；對 R058–R060、R062、R065 查核採用全文版本及精確頁碼。
2. 雙語編輯校譯全文，並由術語編輯核定 8 組 CH08 詞條及英文標題。
3. 作者／編輯選擇合法觀看片版次；記錄字幕、片長、觀看片源及需引用的時間碼，或維持不作鏡頭級主張。
4. 確認兩張 SVG 的個人作者署名、相似性、無障礙、印刷品質與正式出版權利；未核准前保留 pending。
5. 完整編輯校樣 DOCX/PDF/EPUB；正式發布前須解除全專案圖片權利閘門。
6. 修復或另行核准 CH01 術語資料缺少 `status` 的既有測試錯誤，再重跑全套測試；本輪未改 CH01。
7. 依全書完成後的安排，完成作者及所需專業人員簽核。

## 判定

CH08 的研究草稿、英文工作譯稿、術語／引用登錄、兩張原創可編輯 SVG、網站本機建置、DOCX/PDF/EPUB 草稿及專項測試均已完成。全套測試仍有一項既有 CH01 資料錯誤；來源頁碼、雙語校譯、觀看片段、圖像權利及作者簽核尚未結案。**CH08 尚未達正式出版標準。** 本次完成 CH08 後停止，未自動開始 CH09。
