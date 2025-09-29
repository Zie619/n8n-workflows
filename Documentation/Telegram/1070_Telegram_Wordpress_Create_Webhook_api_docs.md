# API Documentation: 🔍🛠️Generate SEO-Optimized WordPress Content with Perplexity Research

## Overview
Automated workflow: 🔍🛠️Generate SEO-Optimized WordPress Content with Perplexity Research. This workflow integrates 13 different services: stickyNote, wordpress, httpRequest, formTrigger, telegram. It contains 37 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 58
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.wordpress`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `telegramApi`
- `openAiApi`
- `wordpressApi`
- `httpHeaderAuth`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
