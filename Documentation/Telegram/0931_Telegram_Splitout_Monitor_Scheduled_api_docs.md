# API Documentation: N8N Financial Tracker Telegram Invoices to Notion with AI Summaries & Reports

## Overview
Automated workflow: N8N Financial Tracker Telegram Invoices to Notion with AI Summaries & Reports. This workflow integrates 14 different services: stickyNote, telegramTrigger, telegram, code, lmChatGoogleGemini. It contains 33 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 38
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.telegramTrigger`

## Node Types Used
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.notion`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.editImage`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.quickChart`
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `telegramApi`
- `googlePalmApi`
- `notionApi`

## Environment Variables
- `WEBHOOK_URL`
