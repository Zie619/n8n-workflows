# API Documentation: Open Deep Research - AI-Powered Autonomous Research Workflow

## Overview
Automated workflow: Open Deep Research - AI-Powered Autonomous Research Workflow. This workflow integrates 11 different services: stickyNote, httpRequest, code, agent, chainLlm. It contains 21 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 34
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.toolWikipedia`

## Integrations
- No external integrations detected

## Required Credentials
- `openRouterApi`
- `httpHeaderAuth`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`
