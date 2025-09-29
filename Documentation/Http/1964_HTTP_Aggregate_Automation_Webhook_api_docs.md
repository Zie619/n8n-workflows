# API Documentation: Google Maps FULL

## Overview
Automated workflow: Google Maps FULL. This workflow integrates 12 different services: stickyNote, httpRequest, toolSerpApi, agent, stopAndError. It contains 26 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 43
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.toolSerpApi`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `serpApi`
- `openAiApi`
- `googleSheetsOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
