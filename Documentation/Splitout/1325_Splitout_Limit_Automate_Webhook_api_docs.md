# API Documentation: Manualtrigger Workflow

## Overview
Automated workflow: Manualtrigger Workflow. This workflow integrates 15 different services: wordpress, httpRequest, stickyNote, markdown, splitOut. It contains 34 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 47
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.wordpress`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.html`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.set`
- `n8n-nodes-base.markdown`
- `@n8n/n8n-nodes-langchain.informationExtractor`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `wordpressApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
