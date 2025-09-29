# API Documentation: Lmchatopenai Workflow

## Overview
Automated workflow: Lmchatopenai Workflow. This workflow integrates 16 different services: stickyNote, httpRequest, airtable, agent, merge. It contains 58 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 95
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.toolCode`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `httpQueryAuth`
- `openAiApi`
- `airtableTokenApi`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`
