# API Documentation: 🌐 Confluence Page AI Powered Chatbot

## Overview
Automated workflow: 🌐 Confluence Page AI Powered Chatbot. This workflow integrates 11 different services: stickyNote, httpRequest, markdown, telegram, agent. It contains 22 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 35
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.manualChatTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.manualChatTrigger`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `telegramApi`
- `openAiApi`
- `httpHeaderAuth`

## Environment Variables
- `BASE_URL`
