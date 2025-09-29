# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 15 different services: stickyNote, httpRequest, wait, toolHttpRequest, agent. It contains 64 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 113
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.notion`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.toolHttpRequest`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.wait`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.removeDuplicates`

## Integrations
- No external integrations detected

## Required Credentials
- `serpApi`
- `openAiApi`
- `httpHeaderAuth`
- `notionApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
