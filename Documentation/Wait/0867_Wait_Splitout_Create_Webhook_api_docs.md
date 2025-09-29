# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 10 different services: stickyNote, httpRequest, formTrigger, wait, splitOut. It contains 25 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 42
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.formTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.if`
- `n8n-nodes-base.wait`

## Integrations
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
