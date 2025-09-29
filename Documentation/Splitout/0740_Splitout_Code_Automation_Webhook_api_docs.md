# API Documentation: YogiAI

## Overview
Automated workflow: YogiAI. This workflow integrates 14 different services: stickyNote, httpRequest, code, scheduleTrigger, agent. It contains 44 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 53
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.outputParserAutofixing`
- `@n8n/n8n-nodes-langchain.lmChatAzureOpenAi`
- `n8n-nodes-base.googleSheetsTool`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `httpHeaderAuth`
- `azureOpenAiApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
