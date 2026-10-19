# CHAPTER_TEMPLATE_V2 導覽

本文件是 V2 章節模板的穩定入口，不複製另一份容易失同步的模板內容。唯一 canonical 模板為 [`templates/chapter-v2.md`](templates/chapter-v2.md)；雙語切分、術語、來源、圖像權利、出版與品質規則分別由以下規範管理：

- [`docs/TRANSLATION-V2.md`](docs/TRANSLATION-V2.md)：繁中主稿、英文人工審校譯稿及逐節對齊。
- [`docs/TERMINOLOGY-V2.md`](docs/TERMINOLOGY-V2.md)：永久術語 ID、雙語定義與審核狀態。
- [`docs/CITATION-V2.md`](docs/CITATION-V2.md)：來源登錄、locator、證據類型和引用追溯。
- [`docs/IMAGE-RIGHTS-V2.md`](docs/IMAGE-RIGHTS-V2.md)：原創圖稿來源、製作紀錄、權利狀態和出版 gate。
- [`docs/QUALITY-GATES-V2.md`](docs/QUALITY-GATES-V2.md) 與 [`FILM_QUALITY_RUBRIC.md`](FILM_QUALITY_RUBRIC.md)：機器可測條件與人類主觀審查。
- [`FILM_ELEMENTS.md`](FILM_ELEMENTS.md)：電影元素分類；章節 metadata 以 `film_element_ids` 連結。
- [`AI_PRODUCTION_SYSTEMS.md`](AI_PRODUCTION_SYSTEMS.md)：AI 製作系統；章節 metadata 以 `ai_system_ids` 連結。

## 模板擴充建議

後續更新 `templates/chapter-v2.md` 時，可增補選填 metadata 欄位：

```yaml
film_element_ids: [FE04, FE05]
ai_system_ids: [AIS05]
case_studies: []
acceptance_report: reports/CHXX-FINAL-ACCEPTANCE.md
```

新欄位應先更新 `metadata/chapters.yaml` 的契約／驗證器，再由作者或編輯補值；不可用標籤自動推定章節已完整涵蓋相關知識。章節正文模板保持可依主題裁剪，不要求每章機械填滿全部元素。
