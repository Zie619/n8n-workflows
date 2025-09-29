# API Documentation: 💥AI Social Video Generator with GPT-4, Kling & Blotato —Auto-Post to Instagram, Facebook,, TikTok...

## Overview
Automated workflow: 💥AI Social Video Generator with GPT-4, Kling & Blotato —Auto-Post to Instagram, Facebook,, TikTok, Twitter & Pinterest - vide. This workflow integrates 12 different services: telegramTrigger, stickyNote, httpRequest, wait, telegram. It contains 81 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 154
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
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.wait`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `httpHeaderAuth`
- `httpBasicAuth`
- `telegramApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
