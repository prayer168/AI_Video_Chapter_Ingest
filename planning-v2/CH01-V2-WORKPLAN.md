# CH01 V2.0 雙語圖文樣章｜工作清單與驗收規範

**文件性質：** 編輯工作計畫，不是章節正文。  
**永久章節 ID：** `CH01`  
**狀態：** 尚未開始 V2 正文遷移；V1 原稿與素材只供編輯參照，保持不變。

## 工作範圍

- 建立一份經編輯審查的繁體中文 V2 主稿，以及一份人工翻譯、專業審校的英文稿。
- 使用相同章節／段落／術語／引用／圖片 ID；完成必要的原創電影式插圖和可編輯技術向量圖。
- 從 canonical Markdown 產出可審校的雙語網站及書籍樣章。
- 本工作不包含批次撰寫其餘 59 章，不把 V1 草稿未審核地直接搬成 V2，也不允許網路圖片成為正式插圖。

## 工作清單

### A. 編輯研究與章節設計

- [ ] 對照 V1 CH01、原始素材包與 V2 目錄，列出保留、重寫、刪節、待查的段落；不改動來源檔。
- [ ] 建立 CH01 節次大綱、學習目標及先備知識；各學習目標需能由章末練習驗證。
- [ ] 為各節建立永久錨點 `CH01-Sxx`，重要段落視交叉引用需求配置 `CH01-Pxxx`。
- [ ] 列出需查證的電影史、理論、製作慣例、技術功能主張；先找原始／專業來源，不先填未核實頁碼。
- [ ] 將每項主張標為已查證事實、理論、實務建議、AI 假設或示範內容；記錄不確定及反例。

### B. 繁中主稿與術語

- [ ] 完成繁中初稿，涵蓋章節模板規定的全部必要區塊。
- [ ] 每項重要名詞建立永久 term ID，提供中英文首選詞、定義、語境、易混淆詞和支持來源。
- [ ] 用術語庫統一章名、內文、圖說、圖中標註、鏡頭表與練習用語。
- [ ] 編輯核對敘述是否區分電影理論觀點、產業慣例與作者建議。

### C. 英文稿與雙語同步

- [ ] 由繁中主稿逐節人工翻譯；機器翻譯只能作草稿輔助，不得自動核准。
- [ ] 保留完全相同的章 ID、節／段落錨點、術語 ID、參考 ID、figure ID 和鏡頭 ID。
- [ ] 對照數字、單位、參數、引用頁碼、電影專有名詞、圖說與 alt；建立未決問題清單。
- [ ] 完成英文專業審校後，記錄譯者／審校者、日期、繁中 source revision 和 translation status。

### D. 圖像與圖解計畫

- [ ] 逐段建立 figure plan：永久圖號、插入錨點、教學目的、圖種、雙語 caption/alt、原創 prompt／繪圖方法、來源研究及審查責任人。
- [ ] 電影感插圖以原創生成／自行繪製為主；AI 生成底圖避免烘焙大段文字。
- [ ] 技術精度重要時製作可編輯 SVG；雙語標籤放在獨立 overlay，保留語言與層次可編修。
- [ ] 保存原始檔、版本／日期、生成工具、prompt、修改紀錄；原創合成圖不得冒充歷史實拍紀錄。
- [ ] 不下載、不嵌入搜尋引擎或第三方網站圖片；有疑義即建立待辦，不以替代網圖補空缺。

### E. 出版與樣章測試

- [ ] 在本機安裝並記錄 Node/npm、Astro/Starlight、Pandoc、XeLaTeX、字型與作業系統版本。
- [ ] 驗證網站 `/zh-tw/` 與 `/en/`、語言切換、缺譯提示、搜尋、目錄、響應式、鍵盤操作、圖片透明背景和可編輯向量轉出結果。
- [ ] 從同一 canonical Markdown 建立繁中／英文 DOCX、PDF、EPUB；任何輸出都不自動部署。
- [ ] PDF 以嚴格模式確認字型已嵌入且含預期繁中字型；抽查繁中文字形、標點、孤行寡行、圖說、跨頁和頁碼。
- [ ] EPUB 通過結構檢查並抽查目錄、語言 metadata、圖片、連結及閱讀器渲染。
- [ ] 產生測試報告並由編輯校樣；CI 通過不能替代專業內容審查或視覺校樣。

## 建議逐段插圖對應（figure briefs）

以下是待編輯確認的原創圖 brief，不是已完成插圖；實際 `placement_after` 要等 `CH01-Pxxx` 段落定稿後填入。禁止以網路圖片補位。

| Figure ID | 對應內容 | 畫面與教學目的 | 繁中／英文圖說核心 |
|---|---|---|---|
| `CH01-FIG-001` | S01 導讀 | 同一原創場景以遠景、中景、特寫形成三格敘事 | 三個鏡頭改變資訊層級／Three shots change the hierarchy of information. |
| `CH01-FIG-002` | S02 觀看練習 | 以光線與視線引導觀者先後注意不同物件 | 畫面安排注意順序／An image directs what the viewer notices first. |
| `CH01-FIG-003` | S03 術語 | 可編輯巢狀時間軸說明 shot、scene、sequence | 鏡頭組成場景與段落／Shots form scenes and sequences. |
| `CH01-FIG-004` | S04 原理 | 角色跨越門檻前後的構圖、視線與動線 overlay | 構圖與順序建立因果期待／Composition and ordering create causal expectation. |
| `CH01-FIG-005` | S05 傳統流程 | 原創片場俯視圖標示演員、主鏡與 coverage | Coverage 保留剪接選擇／Coverage preserves editing options. |
| `CH01-FIG-006` | S06 AI 邊界 | 腳本、生成預視覺與人工審核閘門 | 生成結果仍須人工審查／Generated results still require human review. |
| `CH01-FIG-007` | S07 工作流 | 意圖→分鏡→生成／拍攝→剪輯→驗證→修訂 | 檢查點連結選擇與輸出／Checkpoints connect choices to outputs. |
| `CH01-FIG-008` | S08 參數 | 同角色同場景，只改一項鏡頭變因的對照 | 一次只改一個變因／Change one visual variable at a time. |
| `CH01-FIG-009` | S09 案例 | 六格原創微敘事 storyboard | 鏡頭由段落位置獲得意義／A shot gains meaning from its place in a sequence. |
| `CH01-FIG-010` | S10 錯誤 | 視線、動作方向與道具位置的正誤對照 | 連續性錯誤改變空間理解／Continuity errors alter spatial understanding. |
| `CH01-FIG-011` | S11 評量 | 無品牌 storyboard worksheet 與觀察欄 | 檢查意圖、資訊排序與連續性／Review intent, information order, and continuity. |
| `CH01-FIG-012` | S12 統整 | 鏡頭、聲音、剪輯、敘事與監督的概念圖 | 視聽語言是可檢驗的選擇系統／Audiovisual language is a testable system of choices. |

每張圖都須有雙語 caption／alt、教學目的、原創 prompt 或繪圖方法、工具版本、日期、修改紀錄，以及 rights／technical／editorial 三項審查。底圖避免烘焙文字；雙語文字使用可編輯 SVG overlay。

## 完成驗收條件

### 內容與來源

- [ ] CH01 繁中稿包含學習目標、先備知識、雙語術語、歷史／原理、傳統流程、AI 轉換、詳細步驟、提示詞／參數、案例、錯誤與品質檢查、練習評量、延伸研究、參考來源。
- [ ] 所有可查證主張均有可追溯來源；電影理論優先專業研究來源，時效性 AI 功能有官方文件／版本及查證日。
- [ ] 不存在捏造的史料、論文、頁碼、DOI、URL、工具功能；來源不確定者明確標示待查。
- [ ] 英文稿完成專業人工審校，狀態核准且與繁中 source revision 同步。

### 術語、翻譯及圖像

- [ ] 中英文各章共用穩定 ID；所有節錨點與 figure ID 配對完整，無重複／孤立 ID。
- [ ] 所有正式圖片均在 figure manifest 登錄，檔案存在；權利、技術及編輯審查皆 approved。
- [ ] 每張圖有來源／原創記錄、prompt 或繪圖方法、製作修改紀錄、雙語圖說與非空雙語 alt。
- [ ] 技術 SVG 可編輯、幾何與術語正確；輸出圖清晰且不含未審核標註。

### 網站與書籍

- [ ] 網站兩語路由、搜尋、目錄、缺譯提示、無障礙基本檢查和 Cinematic Editorial 樣式均完成實測。
- [ ] DOCX、PDF、EPUB 都由 canonical Markdown 重建；記錄工具版本及輸出 SHA-256。
- [ ] 繁中 PDF 的預期字型可確認嵌入，繁中文字形人工抽查通過；EPUB 結構和閱讀器抽查通過。
- [ ] 正式發行前由編輯／作者核准校樣；無自動發布或 GitHub 推送。

## 交付檔案

- `content/zh-TW/chapters/CH01-cinematic-language.md`
- `content/en-US/chapters/CH01-cinematic-language.md`
- `assets/chapters/CH01/figure-manifest.yaml`、原創底圖、可編輯 SVG overlay 及輸出圖
- CH01 術語與參考登錄、提示詞／圖像製作記錄
- 雙語網站與 DOCX/PDF/EPUB 校樣
- CH01 驗收紀錄及 release pack；所有審查未完成前標為 draft，不得發布
