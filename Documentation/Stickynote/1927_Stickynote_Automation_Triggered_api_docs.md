# API Documentation: SearchApi AI Agent

## Overview
Automated workflow: SearchApi AI Agent. This workflow integrates 7 different services: stickyNote, agent, stopAndError, lmChatOpenAi, memoryBufferWindow. It contains 10 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 15
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `@searchapi/n8n-nodes-searchapi.searchApiTool`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- No credentials required

## Environment Variables
- No environment variables required
