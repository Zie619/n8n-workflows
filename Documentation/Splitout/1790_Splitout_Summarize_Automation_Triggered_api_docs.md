# API Documentation: Easily Compare LLMs Using OpenAI and Google Sheets

## Overview
Automated workflow: Easily Compare LLMs Using OpenAI and Google Sheets. This workflow integrates 13 different services: stickyNote, agent, splitOut, summarize, set. It contains 22 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 27
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `@n8n/n8n-nodes-langchain.memoryManager`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `openRouterApi`
- `googleApi`

## Environment Variables
- `WEBHOOK_URL`
