# Chapter workflow prompt patterns

這些提示詞供 Skill 在對話內逐階段使用；不是已執行的研究或生成結果。每次使用前以章節 registry 和當下官方文件填入實際資訊。

## Research map

> 為 CHNN 建立可查證主張清單。逐項給出 claim、證據類型（verified-fact/theory/practice/ai-hypothesis/demo）、優先來源類型、來源 ID、版次/版本、日期、URL/DOI、來源能支持的範圍、限制和待查問題。不要先寫來源不存在的細節、頁碼或 timecode。對工具能力只用該版官方文件及可重現測試。

## Traditional Chinese draft

> 依已核實的 research map、既有本章草稿和 V4 章節模板撰寫繁體中文。保留有來源支持的論證，為每個可查證主張附來源 ID 和證據標籤。明確標示理論解讀、實務建議、AI 假設及虛構示範。未證實處用 `待查證`，不要填補想像內容。列出變更摘要和來源主張對照。

## English editorial translation

> 將已定稿的 CHNN zh-TW 逐節轉成 en-US，保持穩定 section/case/term/figure/reference IDs、範圍限定、否定語氣、數字、參數及權利聲明。術語依 registry；列疑義及不自然處。狀態一律 `review-needed`，不得自我批准或自行增加新事實。

## Film homage case

> 先說明本案例的教學問題，再查具名專業來源及合法觀看版次。將「來源明說的事實」「看片觀察」「作者解讀」分開。記錄影片版本、觀看來源、timecode 和觀察者；未實際核看片段時 timecode 留空並標 BLOCKED。把形式原理轉為全新人物、場景、構圖和道具；禁止重製片中鏡頭、角色、演員外觀、服裝、美術或標誌。提供原創練習和相似性待審清單。

## Original image brief

> 依 CHNN 教學目標建立一張不含大量文字的原創插圖 brief。指定畫面功能、版面比例、主體、動作、視線／空間、光線、避免元素、雙語 caption/alt 草案及可驗收項。不要引用第三方圖片作畫面輸入，不描摹電影劇照。若沒有獲授權的生成 provider，只輸出 brief 和 BLOCKED 記錄，不呼叫服務、不造圖。

## Quality review

> 對照 V4 必要閘門逐項檢查 CHNN 的 canonical 中英稿、來源 registry、術語、翻譯對照、figure manifest、圖片 hash、網站、PDF、EPUB 和測試。每項只能標 PASS/FAIL/BLOCKED/NEEDS HUMAN REVIEW/NOT RUN，引用實際證據。指出內容缺口，不可將格式檢查說成學術正確或作者核准。
