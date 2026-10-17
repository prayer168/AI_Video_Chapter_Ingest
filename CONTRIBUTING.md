# 貢獻指南

1. 由 `main` 建立分支，依 `templates/chapter-template.md` 新增章節。
2. 使用唯一章節 ID，更新 `docs/TOC.md`，並登錄術語與參考資料 ID。
3. 以自己的文字撰寫或摘要來源；保留定位資訊，並標記事實、理論、建議、假設或示範。
4. 執行 `python scripts/validate_project.py`；若有外部 URL，可另執行 `python scripts/check_links.py --online`。
5. 人工完成 `docs/QUALITY.md` 審查清單，更新章節狀態及日期。
6. 以清楚的 Git commit 訊息提交。重大更正更新 `CHANGELOG.md`。

不得提交 API 金鑰、私人素材、未授權影片、含個資的製片文件或來源不明的圖像。自動檢查通過不等同內容查證完成。
