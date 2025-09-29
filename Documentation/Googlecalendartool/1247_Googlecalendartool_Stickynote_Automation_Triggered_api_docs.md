# API Documentation: AI Agent : Google calendar assistant using OpenAI

## Overview
Automated workflow: AI Agent : Google calendar assistant using OpenAI. This workflow integrates 7 different services: stickyNote, agent, stopAndError, lmChatOpenAi, memoryBufferWindow. It contains 16 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 21
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.googleCalendarTool`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `openAiApi`
- `googleCalendarOAuth2Api`

## Environment Variables
- No environment variables required
