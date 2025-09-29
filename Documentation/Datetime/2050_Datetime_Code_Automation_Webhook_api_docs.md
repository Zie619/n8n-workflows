# API Documentation: Testing Mulitple Local LLM with LM Studio

## Overview
Automated workflow: Testing Mulitple Local LLM with LM Studio. This workflow integrates 11 different services: stickyNote, httpRequest, code, splitOut, chainLlm. It contains 25 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 34
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.dateTime`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`

## Environment Variables
- `WEBHOOK_URL`
