# 圖像生成方案評估與設定

- 查證日期：2026-10-18（Asia/Taipei）
- 狀態：**BLOCKED — 尚未啟用任何生成請求**。Codex 圖像生成工具可用；Gemini API 金鑰變數在本機環境存在，但帳戶計費／額度、預算上限與使用條款授權未確認。未輸出、記錄或呼叫該金鑰。
- 費用規則：ChatGPT 訂閱和 API 平台分開計費；本專案不推定訂閱包含 API 額度。沒有使用者明確預算和開通前，不呼叫付費 provider。

## 選項盤點

| 方案 | 本環境觀察 | 解析度與出版適用 | 成本／批次 | 條款／主要限制 | 結論 |
|---|---|---|---|---|---|
| Codex 內建 `image_gen.imagegen` | 此 Codex 工作階段工具目錄可見；它是對話／Codex 工具，不等於 Python 可呼叫 API | 工具 schema 只要求 prompt／透明背景等，未在此環境確認最大像素、色彩空間或可重現參數；需用實際授權後的 benchmark 確認 | 本環境未顯示此工具的價格、帳戶額度、批次額度或可寫入路徑權限 | 訂閱／工具服務具體條款、儲存方式及出版用途需依帳戶與服務條款確認 | 供 Codex 互動生成候選圖；目前費用與條款未確認，故不啟用 |
| OpenAI API GPT Image 2.5 Sunburst / Flare | 官方支援 Image API 生成／編輯與 Responses API 工具流程；Flare 偏速度，Sunburst 偏精細編輯 | 支援自訂尺寸、格式、品質及背景；常見出版母檔可先評估 1536×1024 或 2560×1600（需符合當前 API pixel/edge limits）。超過 2K 的實際穩定性要以 benchmark 驗證；印刷裁切／300 dpi 所需像素由實際版心尺寸計算 | 費用按 prompt／image tokens 計，且受尺寸、品質、輸入圖影響，不應以固定「每張」估算；2026-10-18 官方標準 rates：image input $8/M、output $30/M；Batch $4/M、$15/M（prompt text tokens 另計）。用官方 calculator 和 response usage 估算；Batch 約可省 50%，非即時，官方文件說最長 24 小時 | ChatGPT 與 API 分開帳務。商業條款在適用範圍內將 Output 權利給客戶，但相似輸出可能發生、客戶需確保輸入有權利及自行評估輸出。這不保證 AI 產物在所在地可取得排他著作權或無侵權 | 目前優先評估；任何 API 調用仍須帳戶/預算/條款確認 |
| Stability AI API | 官方 API、模型與 credits 方案可用性須按當時帳戶查看 | 官方宣稱有多種生成服務和最高 4K upscaler；實際母圖尺寸／重繪品質按模型實測；重繪 upscaler 可能改變畫面內容 | 官方價目表（2026-10-18 擷取）以 1 credit=$0.01；Stable Image Core 3 credits、Ultra 8 credits、Fast Upscaler 2 credits 等；價格可能變動 | 當前條款版本有效日期為 2026-09-30；使用者須確認上傳輸入權利；條款給服務方為維持／提供服務所需內容權利。詳閱帳戶實際契約及資料處理選項 | 可作替代候選；未選用／未開通 |
| 本機 ComfyUI／SDXL 類模型 | PATH 查無 `ollama`、`comfy`／`comfyui`；本機有 NVIDIA GeForce RTX 3060 Laptop GPU 6 GB VRAM | 模型輸出、VRAM、採樣和批次需依模型與記憶體實測；6 GB 不保證可穩定跑高解析度，可能需低 VRAM／分塊或 upscaler | 無 provider 推論費，但下載、硬體、耗電、設定維護有成本；目前未安裝模型／工作流 | 權利和用途依每個模型 license；例如 Stability 模型需核對對應 OpenRAIL 或商業授權，不能只看「開源」字樣 | 可行的後續 self-host 路線；未安裝模型，沒有生成 |

## 本次決定

1. 未呼叫 Codex imagegen、Gemini、OpenAI、Stability 或任何 API，沒有發生生成費用。
2. 加入 adapter protocol、BLOCKED adapter 和 test double；test double 只回傳 simulated metadata，絕不寫圖片檔或假裝輸出成功。
3. 任何未來 provider 實作必須先經作者確認：provider、帳單帳戶、可用條款、單次／單章／月預算、最大圖數、資料保存地點、能否把提示詞／參考圖傳到雲端、格式及目標尺寸。API adapter 必須同時要求程式旗標、正數 budget cap 和明確 `budget_approved=true`。
4. 就算獲准生成，也只進 `originals/`、標 `draft-generated`、加入 SHA-256 及 generation record；rights／technical／editorial 三個 gate 仍 pending。

## 本機 adapter 狀態

- config example：`production/image_generation/provider.example.json`（`provider: disabled`、`max_spend_usd: 0`）
- adapter：`production/image_generation/adapter.py`
- 安全測試：`tests/test_image_generation_adapter.py`
- 目前狀態：`BLOCKED`（無已授權／已驗證的執行 provider；Codex 原生工具雖可見，但費用與服務條款尚未核實；API key 存在不代表授權）

## 官方來源（存取日均為 2026-10-18）

- [OpenAI Image generation guide](https://developers.openai.com/api/docs/guides/image-generation)：模型、endpoint、尺寸／品質／格式、`n` 批次及費用 calculator。
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)：GPT Image 2.5 standard/batch token rates；價格依 tokens，不以固定單張價推算。
- [OpenAI Batch API](https://developers.openai.com/api/docs/guides/batch)：支援 Images endpoints、約 50% 折扣及最長 24 小時作業時間。
- [OpenAI API and ChatGPT billing separation](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)：API 與 ChatGPT 分開帳務。
- [OpenAI Business Terms](https://openai.com/policies/may-2025-business-terms/)：Output 權利安排、相似輸出和使用者責任（僅適用於受該契約管轄的客戶；應核實自己的合同）。
- [Stability AI pricing](https://platform.stability.ai/pricing) 與 [Terms](https://platform.stability.ai/legal/terms-of-service)：價格及有效條款需在實際開通前重新查證。
- [Gemini API image generation](https://ai.google.dev/gemini-api/docs/image-generation) 與 [pricing](https://ai.google.dev/gemini-api/docs/pricing)：Gemini API 模型／價格會更新；本環境憑證未被使用。

所有價格、模型 ID、解析度與條款都會變更；每次實際生成前重新查官方文件並將版本、日期與預估記錄至 run log。以上比較不是法律意見，也沒有宣稱圖像可取得完整或排他著作權。
