# API Documentation: Build Custom AI Agent with LangChain & Gemini (Self-Hosted)

## Overview
Automated workflow: Build Custom AI Agent with LangChain & Gemini (Self-Hosted). This workflow integrates 6 different services: stickyNote, code, lmChatGoogleGemini, stopAndError, memoryBufferWindow. It contains 10 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 15
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.code`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googlePalmApi`

## Environment Variables
- No environment variables required
