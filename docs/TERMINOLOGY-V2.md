# V2 術語資料模型

術語使用永久 `term_id`，例如 `TERM-FRAME`；跨語言共用同一 ID。建議欄位：

```yaml
schema_version: 1
terms:
  - term_id: TERM-FRAME
    preferred:
      zh-TW: 畫格
      en-US: frame
    definitions:
      zh-TW: "在指定電影語境中的定義，應附可靠來源。"
      en-US: "A reviewed English definition in the same declared context."
    domain: cinematography
    context: "明確說明影格、畫格等多義詞所屬語境"
    synonyms: {zh-TW: [], en-US: []}
    see_also: []
    references: [R001]
    status: review-needed
    reviewed_by: null
    reviewed_on: null
```

狀態使用 `draft`、`review-needed`、`approved`、`deprecated`。`approved` 必須經雙語專業審校，並確認參考來源支持該定義；定義有分歧時記錄流派、地區、年代或製作語境，不強行合併成唯一答案。
