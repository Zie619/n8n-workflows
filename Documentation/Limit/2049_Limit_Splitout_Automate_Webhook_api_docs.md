# API Documentation: 🔥📈🤖 AI Agent for n8n Creators Leaderboard - Find Popular Workflows

## Overview
Automated workflow: 🔥📈🤖 AI Agent for n8n Creators Leaderboard - Find Popular Workflows. This workflow integrates 19 different services: convertToFile, stickyNote, merge, lmChatOpenAi, chatTrigger. It contains 50 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 63
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.lmChatOllama`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.convertToFile`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.sort`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.readWriteFile`
- `n8n-nodes-base.set`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `ollamaApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
