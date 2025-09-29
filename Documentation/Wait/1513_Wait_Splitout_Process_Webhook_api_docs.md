# API Documentation: Lmopenai Workflow

## Overview
Automated workflow: Lmopenai Workflow. This workflow integrates 16 different services: stickyNote, httpRequest, wait, gmailTrigger, splitOut. It contains 34 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 51
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`

## Node Types Used
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.lmOpenAi`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.wait`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `httpHeaderAuth`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
