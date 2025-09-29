# API Documentation: Agent Workflow

## Overview
Automated workflow: Agent Workflow. This workflow integrates 97 different services: vectorStoreInMemory, if, gumroadTrigger, wait, toolSerpApi. It contains 142 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 175
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`
- `n8n-nodes-base.googleSheetsTrigger`
- `n8n-nodes-base.calendlyTrigger`
- `n8n-nodes-base.googleDriveTrigger`
- `n8n-nodes-base.gumroadTrigger`
- `n8n-nodes-base.localFileTrigger`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.gmailTrigger`
- `n8n-nodes-base.googleSheetsTrigger`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `5d58aa36-a90f-4ec3-ab44-2006a370ae56`
- **Method**: `POST`
- **Webhook ID**: `5d58aa36-a90f-4ec3-ab44-2006a370ae56`


## Node Types Used
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.memoryRedisChat`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `n8n-nodes-base.emailSendTool`
- `n8n-nodes-base.googleCalendar`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.executionData`
- `@n8n/n8n-nodes-langchain.outputParserItemList`
- `n8n-nodes-base.dateTime`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.emailReadImap`
- `@n8n/n8n-nodes-langchain.embeddingsGoogleGemini`
- `@n8n/n8n-nodes-langchain.chainRetrievalQa`
- `n8n-nodes-base.gumroadTrigger`
- `n8n-nodes-base.postgresTool`
- `n8n-nodes-base.executeCommand`
- `@n8n/n8n-nodes-langchain.toolWikipedia`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.googleSheetsTrigger`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.twitter`
- `n8n-nodes-base.googleDocsTool`
- `n8n-nodes-base.noOp`
- `@n8n/n8n-nodes-langchain.toolHttpRequest`
- `@n8n/n8n-nodes-langchain.outputParserAutofixing`
- `n8n-nodes-base.html`
- `@n8n/n8n-nodes-langchain.informationExtractor`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.rssFeedRead`
- `@n8n/n8n-nodes-langchain.toolWolframAlpha`
- `n8n-nodes-base.pushbullet`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.removeDuplicates`
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.splitInBatches`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-elevenlabs.elevenLabs`
- `n8n-nodes-base.gmail`
- `@n8n/n8n-nodes-langchain.toolSerpApi`
- `@n8n/n8n-nodes-langchain.openAi`
- `@n8n/n8n-nodes-langchain.memoryPostgresChat`
- `n8n-nodes-base.redisTool`
- `@n8n/n8n-nodes-langchain.vectorStoreInMemory`
- `@watzon/n8n-nodes-perplexity.perplexity`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.vectorStorePinecone`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `n8n-nodes-base.reddit`
- `@n8n/n8n-nodes-langchain.vectorStorePGVector`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.dropbox`
- `n8n-nodes-base.gmailTrigger`
- `@n8n/n8n-nodes-langchain.lmChatAnthropic`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.toolVectorStore`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.vectorStoreSupabase`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `n8n-nodes-base.googleCalendarTool`
- `n8n-nodes-base.calendlyTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.ftp`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.bitly`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `@n8n/n8n-nodes-langchain.toolCalculator`
- `@n8n/n8n-nodes-langchain.memoryManager`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.renameKeys`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.localFileTrigger`
- `n8n-nodes-base.googleDriveTrigger`
- `@n8n/n8n-nodes-langchain.mcpClientTool`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.googleDocs`
- `n8n-nodes-base.convertToFile`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.wait`
- `@n8n/n8n-nodes-langchain.toolCode`
- `n8n-nodes-base.youTube`
- `n8n-nodes-base.scheduleTrigger`
- `@n8n/n8n-nodes-langchain.sentimentAnalysis`
- `n8n-nodes-base.if`
- `n8n-nodes-base.sort`
- `n8n-nodes-base.aiTransform`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.filter`
- `@muench-dev/n8n-nodes-bluesky.bluesky`
- `n8n-nodes-base.googleSheetsTool`
- `n8n-nodes-base.gmailTool`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `dropboxOAuth2Api`
- `openAiApi`
- `googleCalendarOAuth2Api`
- `googleSheetsOAuth2Api`
- `googleDriveOAuth2Api`
- `elevenLabsApi`
- `serpApi`

## Environment Variables
- No environment variables required
