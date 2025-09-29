# API Documentation: 🤖🧠 AI Agent Chatbot + LONG TERM Memory + Note Storage + Telegram

## Overview
Automated workflow: 🤖🧠 AI Agent Chatbot + LONG TERM Memory + Note Storage + Telegram. This workflow integrates 12 different services: stickyNote, telegram, agent, merge, set. It contains 28 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 33
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.googleDocs`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.googleDocsTool`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google
- Google

## Required Credentials
- `telegramApi`
- `openAiApi`
- `googleDocsOAuth2Api`

## Environment Variables
- `BASE_URL`
