# API Documentation: Make OpenAI Citation for File Retrieval RAG

## Overview
Automated workflow: Make OpenAI Citation for File Retrieval RAG. This workflow integrates 11 different services: stickyNote, httpRequest, markdown, code, splitOut. It contains 24 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 37
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.set`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`

## Environment Variables
- `BASE_URL`
