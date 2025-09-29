# API Documentation: modelo do chatbot

## Overview
Automated workflow: modelo do chatbot. This workflow integrates 9 different services: stickyNote, toolHttpRequest, mySqlTool, memoryPostgresChat, set. It contains 18 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 31
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.memoryPostgresChat`
- `@n8n/n8n-nodes-langchain.openAi`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.mySqlTool`
- `@n8n/n8n-nodes-langchain.toolHttpRequest`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `postgres`
- `mySql`

## Environment Variables
- `WEBHOOK_URL`
