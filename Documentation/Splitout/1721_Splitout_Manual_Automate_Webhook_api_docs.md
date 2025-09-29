# API Documentation: Automate Etsy Data Mining with Bright Data Scrape & Google Gemini

## Overview
Automated workflow: Automate Etsy Data Mining with Bright Data Scrape & Google Gemini. This workflow integrates 12 different services: stickyNote, httpRequest, lmChatGoogleGemini, readWriteFile, function. It contains 29 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 46
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.function`
- `n8n-nodes-base.readWriteFile`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.informationExtractor`

## Integrations
- Google
- Google

## Required Credentials
- `openAiApi`
- `httpHeaderAuth`
- `googlePalmApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
