# 🧠 n8n 工作流程收藏集

本儲存庫包含從多個來源收集的 **n8n 工作流程**，包括：

* 從 [n8n.io](https://n8n.io) 網站和社群論壇匯出的工作流程
* 在網路上公開分享的範例（GitHub、部落格等）

目標是為您的 n8n 專案提供有用的靈感、學習和重複使用資源。

---

## 📂 資料夾結構

* 每個 `.json` 檔案代表一個匯出的工作流程。
* 檔案根據原始標題或來源命名。
* 您可能還會發現一些已轉換為 `.json` 的 `.txt` 檔案（請參見下方說明）。

---

## 🔄 TXT 轉 JSON 轉換

一些工作流程最初儲存為 `.txt` 檔案或從線上來源複製。使用腳本來：

* 偵測 `.txt` 檔案
* 嘗試將它們解析為 JSON 或結構化鍵值對
* 將它們轉換為有效的 `.json` 格式

如果您想自己執行轉換，請查看本儲存庫中包含的 `convert_txt_to_json.py`。

---

## 🛠 使用說明

要將工作流程匯入您自己的 n8n 實例：

1. 開啟您的 [n8n 編輯器 UI](https://docs.n8n.io/hosting/editor-ui/)
2. 點擊右上角的**選單** (☰) → `匯入工作流程`
3. 從此資料夾選擇一個 `.json` 檔案
4. 點擊「匯入」來載入工作流程

在執行前，請確保檢查並修改所需的憑證或 webhook URL。

---

## 📋 工作流程清單

以下是所有可用的工作流程，按類別分組：

### 🤖 AI 智能代理和聊天機器人

* [🤖 Telegram 文字/音訊/圖片訊息代理](workflows/🤖%20Telegram%20Messaging%20Agent%20for%20Text_Audio_Images.json) - 支援多媒體的 Telegram 智能代理
* [🤖🧑‍💻 n8n 創作者排行榜 AI 代理](workflows/🤖🧑_💻%20AI%20Agent%20for%20Top%20n8n%20Creators%20Leaderboard%20Reporting.json) - 頂級 n8n 創作者排行榜報告
* [🤖🧠 AI 聊天機器人 + 長期記憶 + 筆記儲存 + Telegram](workflows/🤖🧠%20AI%20Agent%20Chatbot%20+%20LONG%20TERM%20Memory%20+%20Note%20Storage%20+%20Telegram.json) - 具備長期記憶功能的聊天機器人
* [🐋🤖 DeepSeek AI 代理 + Telegram + 長期記憶 🧠](workflows/🐋🤖%20DeepSeek%20AI%20Agent%20+%20Telegram%20+%20LONG%20TERM%20Memory%20🧠.json) - 基於 DeepSeek 的智能代理
* [🔐🦙🤖 私人本地 Ollama 自主 AI 助理](workflows/🔐🦙🤖%20Private%20&%20Local%20Ollama%20Self-Hosted%20AI%20Assistant.json) - 本地部署的私人 AI 助理
* [🔥📈🤖 n8n 創作者排行榜 AI 代理 - 尋找熱門工作流程](workflows/🔥📈🤖%20AI%20Agent%20for%20n8n%20Creators%20Leaderboard%20-%20Find%20Popular%20Workflows.json) - 發現熱門工作流程
* [🚀 本地多 LLM 測試與效能追蹤器](workflows/🚀%20Local%20Multi-LLM%20Testing%20&%20Performance%20Tracker.json) - 多模型效能比較工具
* [HR & IT 服務台聊天機器人與音訊轉錄](workflows/zmgSshZ5xESr3ozl_HR_&_IT_Helpdesk_Chatbot_with_Audio_Transcription.json) - 企業服務台解決方案
* [旅遊助理代理](workflows/znRwva47HzXesOYk_Travel_AssistantAgent.json) - 智能旅遊規劃助手
* [🐋DeepSeek V3 聊天與 R1 推理快速開始](workflows/🐋DeepSeek%20V3%20Chat%20&%20R1%20Reasoning%20Quick%20Start.json) - DeepSeek V3 模型使用指南
* [使用 LangChain 和 Gemini 建構自訂 AI 代理（自主託管）](workflows/yCIEiv9QUHP8pNfR_Build_Custom_AI_Agent_with_LangChain_&_Gemini_(Self-Hosted).json) - 自訂 AI 代理建構指南
* [使用 Jina.ai 網頁爬蟲的 AI 代理聊天機器人](workflows/xEij0kj2I1DHbL3I_🌐🪛_AI_Agent_Chatbot_with_Jina.ai_Webpage_Scraper.json) - 網頁內容理解聊天機器人
* [WhatsApp 文字、語音、圖片和 PDF AI 聊天機器人](workflows/zMtPPjJ80JJznrJP_AI-Powered_WhatsApp_Chatbot_for_Text,_Voice,_Images_&_PDFs.json) - 全功能 WhatsApp 助手
* [Line 聊天機器人使用 Groq 和 Llama3 處理 AI 回應](workflows/xibc6WDU53isYN1o_Line_Chatbot_Handling_AI_Responses_with_Groq_and_Llama3.json) - Line 平台聊天機器人
* [Microsoft Outlook AI 電子郵件助理](workflows/reQhibpNwU63Y8sn_Microsoft_Outlook_AI_Email_Assistant.json) - 智能郵件處理助手
* [電子郵件 AI 自動回覆器。總結並發送電子郵件](workflows/q8IFGLeOCGSfoWZu_Email_AI_Auto-responder._Summerize_and_send_email.json) - 智能郵件自動回覆
* [Discord MCP 聊天代理](workflows/xRclXA5QzrT3c6U8_Discord_MCP_Chat_Agent.json) - Discord 聊天機器人
* [Hubspot 聊天助理使用 OpenAI 和 Airtable](workflows/vAssistant%20for%20Hubspot%20Chat%20using%20OpenAi%20and%20Airtable.json) - CRM 整合聊天助手

### 📊 內容創作與分析

* [📚 使用 GPT 和 Docsify 自動生成 n8n 工作流程文件](workflows/📚%20Auto-generate%20documentation%20for%20n8n%20workflows%20with%20GPT%20and%20Docsify.json) - 自動文件生成
* [🔍 Perplexity 研究轉 HTML：AI 驅動的內容創作](workflows/🔍%20Perplexity%20Research%20to%20HTML_%20AI-Powered%20Content%20Creation.json) - 研究內容轉換
* [⚡AI 驅動的 YouTube 影片摘要與分析](workflows/⚡AI-Powered%20YouTube%20Video%20Summarization%20&%20Analysis.json) - 影片內容分析
* [🎨 使用 FLUX.1 填充工具的互動式圖片編輯器](workflows/🎨%20Interactive%20Image%20Editor%20with%20FLUX.1%20Fill%20Tool%20for%20Inpainting.json) - AI 圖片編輯
* [將 YouTube 影片轉換為摘要、轉錄和視覺洞察](workflows/wZBgoWrBZveMmzYi_Turn_YouTube_Videos_into_Summaries,_Transcripts,_and_Visual_Insights.json) - 影片內容分析
* [YouTube 評論情感分析器](workflows/xaC6zL4bWBo14xyJ_YouTube_Comment_Sentiment_Analyzer.json) - 評論情感分析
* [WordPress 部落格文章 AI 自動標記](workflows/siXUnQhJpCJ9rHzu_Auto-Tag_Blog_Posts_in_WordPress_with_AI.json) - 內容標記自動化
* [🎦💌進階 YouTube RSS 訂閱好幫手](workflows/tHgDFmFyuj6DnP6l_🎦💌Advanced_YouTube_RSS_Feed_Buddy_for_Your_Favorite_Channels.json) - YouTube 內容追蹤
* [n8n 圖形設計團隊](workflows/tnRYt0kDGMO9BBFd_n8n_Graphic_Design_Team.json) - 設計工作流程
* [使用 Perplexity AI 搜尋新聞並發布到 X (Twitter)](workflows/v9K61fCQhrG6gt6Z_Search_news_using_Perplexity_AI_and_post_to_X_(Twitter).json) - 新聞分享自動化
* [社群媒體發布器](workflows/r1u4HOJu5j5sP27x_Social_Media_Publisher.json) - 多平台內容發布
* [發布到 X](workflows/plzObaqgoEvV4UU0_Post_on_X.json) - Twitter 自動發布
* [YouTube 自動化](workflows/wLbJ7rE6vQzizCp2_Youtube_Automation.json) - YouTube 內容管理

### 🌐 網頁爬蟲與資料擷取

* [✨ 視覺基礎 AI 代理爬蟲 - 搭配 Google Sheets、ScrapingBee 和 Gemini](workflows/✨%20Vision-Based%20AI%20Agent%20Scraper%20-%20with%20Google%20Sheets,%20ScrapingBee,%20and%20Gemini.json) - 視覺化網頁爬蟲
* [智能網頁查詢和語意重新排序流程](workflows/wa2uEnSIowqSrHoY_Intelligent_Web_Query_and_Semantic_Re-Ranking_Flow.json) - 智能搜尋排序
* [使用 Jina.ai 的重要多頁網站爬蟲](workflows/xEij0kj2I1DHbL3I_💡🌐_Essential_Multipage_Website_Scraper_with_Jina.ai.json) - 多頁面爬蟲
* [使用 DeepSeek 爬取 Trustpilot 評論，使用 OpenAI 分析情感](workflows/w434EiZ2z7klQAyp_Scrape_Trustpilot_Reviews_with_DeepSeek,_Analyze_Sentiment_with_OpenAI.json) - 評論情感分析
* [使用 Bright Data 和 Gemini AI 擷取和總結維基百科資料](workflows/sczRNO4u1HYc5YV7_Extract_&_Summarize_Wikipedia_Data_with_Bright_Data_and_Gemini_AI.json) - 維基百科內容處理
* [使用 Bright Data 和 Google Gemini 從 LinkedIn 生成公司故事](workflows/q1DorytEoEw1QLGj_Generate_Company_Stories_from_LinkedIn_with_Bright_Data_&_Google_Gemini.json) - LinkedIn 內容分析
* [使用 Bright Data 進行品牌內容擷取、總結和情感分析](workflows/wTI77cpLkbxsRQat_Brand_Content_Extract,_Summarize_&_Sentiment_Analysis_with_Bright_Data.json) - 品牌內容分析
* [新聞擷取](workflows/xM8Z5vZVNTNjCySL_News_Extraction.json) - 新聞內容爬蟲

### 📱 通訊與訊息處理

* [WhatsApp 入門工作流程](workflows/yxv7OYbDEnqsqfa9_WhatsApp_starter_workflow.json) - WhatsApp 基礎設定
* [📈 從 FT.com 接收每日市場新聞到 Microsoft Outlook 收件匣](workflows/📈%20Receive%20Daily%20Market%20News%20from%20FT.com%20to%20your%20Microsoft%20outlook%20inbox.json) - 市場新聞推送

### 🗃️ 資料管理與同步

* [📦 新電子郵件 ➔ 建立 Google 任務](workflows/z0C6H2kYSgML2dib_📦_New_Email_➔_Create_Google_Task.json) - 郵件任務轉換
* [同步 Google Sheets 與 Postgres](workflows/wDD4XugmHIvx3KMT_Synchronize_your_Google_Sheets_with_Postgres.json) - 資料庫同步
* [從 Google Drive 同步新檔案到 Airtable](workflows/uLHpFu2ndN6ZKClZ_Sync_New_Files_From_Google_Drive_with_Airtable.json) - 檔案管理同步
* [同步 YouTube 影片 URL 到 Google Sheets](workflows/rJNvM4vU6SLUeC1d_Sync_Youtube_Video_Urls_with_Google_Sheets.json) - 影片清單管理
* [從 URL 匯入 CSV 到 Excel](workflows/xcl8D1sukz9Rak69_Import_CSV_from_URL_to_Excel.json) - 資料匯入
* [自動將 CSV 檔案匯入 postgres](workflows/q8GNbRhjQDwDpXoo_How_to_automatically_import_CSV_files_into_postgres.json) - 資料庫匯入
* [從 Google Sheets 匯入多個製造商到 Shopware 6](workflows/xLjE4IkQXARXOCZy_Import_multiple_Manufacturers_from_Google_Sheets_to_Shopware_6.json) - 電商資料匯入
* [匯入多個 CSV 到 Google Sheet](workflows/zic2ZEHvxHR4UAYI_Import_multiple_CSV_to_GoogleSheet.json) - 批次資料匯入
* [透過 Excel 更新角色](workflows/xzKlhjcc6QEzA98Z_Update_Roles_by_Excel.json) - 權限管理
* [壓縮多個檔案](workflows/r3qHlCVCczqTw3pP_Zip_multiple_files.json) - 檔案打包
* [合併多個執行成一個](workflows/ynTqojfUnGpG2rBP_Merge_multiple_runs_into_one.json) - 執行結果合併

### 🏢 企業與 CRM 管理

* [LinkedIn 自動化](workflows/yF1HNe2ucaE81fNl_Linkedin_Automation.json) - LinkedIn 行銷自動化
* [使用 Icypeas 執行電子郵件搜尋（單次）](workflows/zAkPoRdcG5M5x4KT_Perform_an_email_search_with_Icypeas_(single).json) - 電子郵件查找
* [會議預訂 - 到通訊和 CRM](workflows/xe9sXQUc7yW8P8im_Meeting_booked_-_to_newsletter_and_CRM.json) - 會議管理整合
* [ICP 公司評分](workflows/xyLfWaqdIoZmbTfv_ICP_Company_Scoring.json) - 潛在客戶評分
* [ProspectLens 公司研究](workflows/wwvUsosYUyMfpGbB_ProspectLens_company_research.json) - 客戶研究
* [HR 重點自動化流程與 AI](workflows/t1P14FvfibKYCh3E_HR-focused_automation_pipeline_with_AI.json) - 人力資源自動化
* [CV 評估 - 錯誤處理](workflows/vnhhf9aNsw0kzdBV_CV_Evaluation_-_Error_Handling.json) - 履歷評估系統
* [使用 AI 發現職場歧視模式](workflows/vzU9QRZsHcyRsord_Spot_Workplace_Discrimination_Patterns_with_AI.json) - 職場分析工具

### 🔧 開發與維運工具

* [在 n8n 實例之間複製工作流程使用 n8n API](workflows/yOhH9SGiZgZTDUB4_Clone_n8n_Workflows_between_Instances_using_n8n_API.json) - 工作流程遷移
* [憑證轉移](workflows/tlnJNm9t5H3VLU5K_Credentials_Transfer.json) - 憑證管理
* [[OPS] 從 GitHub 恢復工作流程到 n8n](workflows/uoBZx3eMvLMxlHCS_[OPS]_Restore_workflows_from_GitHub_to_n8n.json) - 工作流程備份恢復
* [工作流程節點更新檢查範本的附加元件](workflows/xlMrGt0c1eFi4J1U_Addon_for_Workflow_Nodes_Update_Check_Template.json) - 更新檢查工具
* [尋找受影響表達式的參數助手](workflows/zlHbtHIcCZ9enKwg_v1_helper_-_Find_params_with_affected_expressions.json) - 除錯工具
* [在 n8n 中測試 Webhooks 而不更改 WEBHOOK URL](workflows/sB6dC0GZ7zZHuMGF_Test_Webhooks_in_n8n_Without_Changing_WEBHOOK_URL_(PostBin_&_BambooHR_Example).json) - Webhook 測試
* [失敗重試除了已知錯誤範本](workflows/qAzZekQuABuH8uho_Retry_on_fail_except_for_known_error_Template.json) - 錯誤處理
* [網頁伺服器監控](workflows/pcLi17oUJK9pSaee_Web_Server_Monitor..json) - 系統監控
* [可疑登入偵測](workflows/xQHiKDTkezDY5lFu_Suspicious_login_detection.json) - 安全監控
* [MAIA - 健康檢查](workflows/wng5xcxlYA6jFS6n_MAIA_-_Health_Check.json) - 系統健康監控
* [追蹤工作時間和休息](workflows/pdgNdag49lwoTxUP_Track_Working_Time_and_Pauses.json) - 時間管理
* [基於位置觸發的自動化工作考勤](workflows/x2kgOnBLtqAjqUVS_Automated_Work_Attendance_with_Location_Triggers.json) - 考勤系統

### 🔌 API 與整合服務

* [OIDC 客戶端工作流程](workflows/zeyTmqqmXaQIFWzV_OIDC_client_workflow.json) - 身份驗證整合
* [使用 HttpRequest 節點透過 XMLRPC 發布到 Wordpress.com](workflows/yPIST7l13huQEjY5_Use_XMLRPC_via_HttpRequest-node_to_post_on_Wordpress.com.json) - WordPress 整合
* [圖片生成 API](workflows/wDD4XugmHIvx3KMT_Image_Generation_API.json) - 圖片生成服務
* [使用 Kling API 為服裝生成 360° 虛擬試穿影片](workflows/xQ0xqhNzFeEdBpFK_Generate_360°_Virtual_Try-on_Videos_for_Clothing_with_Kling_API.json) - 虛擬試穿
* [使用 Google 腳本上傳影片到雲端硬碟](workflows/wGv0NPBA0QLp4rQ6_Upload_video_to_drive_via_google_script.json) - 檔案上傳
* [反應 PDFMonkey 回調](workflows/s6nTFZfg6xjWyJRX_React_to_PDFMonkey_Callback.json) - PDF 處理回調
* [上傳發布圖片](workflows/ra8MrqshnzXPy55O_upload-post_images.json) - 圖片上傳
* [Luma AI - Webhook 回應 v1 - AK](workflows/rYuhIChQyjpGNvuR_Luma_AI_-_Webhook_Response_v1_-_AK.json) - AI 服務整合

### 📈 分析與報告

* [OpenSea 分析代理工具](workflows/yRMCUm6oJEMknhbw_OpenSea_Analytics_Agent_Tool.json) - NFT 市場分析
* [OpenSea AI 驅動的 Telegram 洞察](workflows/wi2ZWKN9XPR0jkvn_OpenSea_AI-Powered_Insights_via_Telegram.json) - NFT 市場智能分析
* [SERPBear 分析範本](workflows/qmmXKcpJOCm9qaCk_SERPBear_analytics_template.json) - SEO 分析
* [Google Maps 完整版](workflows/qhZvZVCoV3HLjRkq_Google_Maps_FULL.json) - 地圖服務整合
* [擷取 Squarespace 部落格和活動集合到 Google Sheets](workflows/sUGieRWulZJ7scll_Fetch_Squarespace_Blog_&_Event_Collections_to_Google_Sheets__.json) - 內容分析

### 🎯 專業領域應用

* [使用 Gmail 和 Mailjet 將 Netflix 電子郵件轉發到多個電子郵件地址](workflows/pkw1vY5q1p2nNfNC_Forward_Netflix_emails_to_multiple_email_addresses_with_GMail_and_Mailjet.json) - 郵件轉發
* [Namesilo 批次域名可用性檢查 [範本]](workflows/phqg5Kk3YowxoMHQ_Namesilo_Bulk_Domain_Availability_[Template].json) - 域名檢查
* [HDW Lead Geländewagen](workflows/piapgd2e6zmzFxAq_HDW_Lead_Geländewagen.json) - 專業業務流程
* [n8n-農產品](workflows/ziJG3tgG91Gkbina_n8n-農產品.json) - 農業應用
* [一般 3D 簡報](workflows/vpZ1wpsniCvKYjCF_General_3D_Presentation.json) - 3D 內容處理
* [翻譯](workflows/vssVsRO0FW6InbaY_Translate.json) - 多語言翻譯
* [puq-docker-immich-deploy](workflows/qps97Q4NEet1Pkm4_puq-docker-immich-deploy.json) - 容器部署
* [InstaTest](workflows/qww129cm4TM9N8Ru_InstaTest.json) - 測試自動化

### 🔍 文件與資料處理

* [使用 AI 分析螢幕截圖](workflows/wDD4XugmHIvx3KMT_Analyze_Screenshots_with_AI.json) - 圖片分析
* [使用 Vertex AI (Gemini) 從 PDF 和圖片擷取文字到 CSV](workflows/sUIPemKdKqmUQFt6_Extract_text_from_PDF_and_image_using_Vertex_AI_(Gemini)_into_CSV.json) - 文件內容擷取
* [從 Splunk 警報建立唯一的 Jira 票證](workflows/uD31xU0VYjogxWoY_Create_Unique_Jira_tickets_from_Splunk_alerts.json) - 事件管理

### 🎮 其他實用工具

* [我的工作流程](workflows/yYjRbTWULZuNLXM0_My_workflow.json) - 個人工作流程範例
* [我的工作流程 6](workflows/rLoXUoKSZ4a9XUAv_My_workflow_6.json) - 個人工作流程範例 6
* [工作流程 x2VUvhqV1YTJCIN0](workflows/x2VUvhqV1YTJCIN0_workflow_x2VUvhqV1YTJCIN0.json) - 自訂工作流程範例

---

## 🤝 貢獻

發現了有趣的工作流程或創建了自己的工作流程？
歡迎貢獻到這個收藏集！

請確保：

* 使用描述性的檔案名稱
* 如果適用，在頂部包含原始來源的簡短註釋

---

## ⚠️ 免責聲明

此處的所有工作流程都是**按原樣**分享。
在生產環境中使用之前，請務必在安全環境中檢查和測試它們。

---

## 📊 統計資訊

* **總工作流程數量**：107 個
* **主要類別**：AI 智能代理、內容創作、資料管理、企業應用、開發工具
* **支援的服務**：Telegram、WhatsApp、OpenAI、Google Sheets、n8n API、WordPress 等

---

*最後更新：2024年12月* 