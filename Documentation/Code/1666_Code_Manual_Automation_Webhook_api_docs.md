# API Documentation: Spot Workplace Discrimination Patterns with AI

## Overview
Automated workflow: Spot Workplace Discrimination Patterns with AI. This workflow integrates 12 different services: stickyNote, httpRequest, code, chainLlm, merge. It contains 49 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 70
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.quickChart`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.code`
- `n8n-nodes-base.html`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.informationExtractor`

## Integrations
- No external integrations detected

## Required Credentials
- `httpQueryAuth`
- `openAiApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
