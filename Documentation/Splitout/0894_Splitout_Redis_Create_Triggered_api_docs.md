# API Documentation: Set Workflow

## Overview
Automated workflow: Set Workflow. This workflow integrates 19 different services: stickyNote, switch, redis, executeWorkflow, lmChatOpenAi. It contains 47 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 52
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.mcpTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.n8n`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.mcpClientTool`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.executeWorkflowTrigger`
- `@n8n/n8n-nodes-langchain.mcpTrigger`
- `n8n-nodes-base.redis`
- `n8n-nodes-base.if`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `n8nApi`
- `redis`

## Environment Variables
- `API_ENDPOINT`
