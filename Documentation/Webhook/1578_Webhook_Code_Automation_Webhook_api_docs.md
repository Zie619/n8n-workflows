# API Documentation: Obsidian Notes Read Aloud: Available as a Podcast Feed

## Overview
Automated workflow: Obsidian Notes Read Aloud: Available as a Podcast Feed. This workflow integrates 11 different services: webhook, stickyNote, httpRequest, code, merge. It contains 37 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 62
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `64fac784-9b98-4bbc-aaf2-dd45763d3362`
- **Method**: `POST`
- **Webhook ID**: `64fac784-9b98-4bbc-aaf2-dd45763d3362`

- **Path**: `2f0a6706-54da-4b89-91f4-5e147b393bd8h`
- **Method**: `POST`
- **Webhook ID**: `2f0a6706-54da-4b89-91f4-5e147b393bd8`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.code`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `httpCustomAuth`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
