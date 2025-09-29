# API Documentation: ✨🔪 Advanced AI Powered Document Parsing & Text Extraction with Llama Parse

## Overview
Automated workflow: ✨🔪 Advanced AI Powered Document Parsing & Text Extraction with Llama Parse. This workflow integrates 18 different services: textClassifier, webhook, stickyNote, httpRequest, telegram. It contains 73 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 90
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.gmailTrigger`

### Webhook Endpoints
- **Path**: `parse`
- **Method**: `POST`
- **Webhook ID**: `a9668054-5bd3-427d-8f18-932436441e42`


## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `httpHeaderAuth`
- `gmailOAuth2`
- `googleDriveOAuth2Api`
- `telegramApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
