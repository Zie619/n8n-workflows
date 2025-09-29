# API Documentation: AI-Powered WhatsApp Chatbot for Text, Voice, Images & PDFs

## Overview
Automated workflow: AI-Powered WhatsApp Chatbot for Text, Voice, Images & PDFs. This workflow integrates 14 different services: stickyNote, httpRequest, code, agent, switch. It contains 43 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 60
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.whatsAppTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.code`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.whatsAppTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.whatsApp`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `whatsAppApi`
- `openAiApi`
- `httpHeaderAuth`
- `whatsAppTriggerApi`

## Environment Variables
- `BASE_URL`
