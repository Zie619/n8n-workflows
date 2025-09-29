# API Documentation: Auto-create and publish AI social videos with Telegram, GPT-4 and Blotato

## Overview
Automated workflow: Auto-create and publish AI social videos with Telegram, GPT-4 and Blotato. This workflow integrates 11 different services: telegramTrigger, stickyNote, httpRequest, wait, telegram. It contains 90 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 175
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.telegramTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.wait`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `httpHeaderAuth`
- `httpBasicAuth`
- `httpCustomAuth`
- `telegramApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
