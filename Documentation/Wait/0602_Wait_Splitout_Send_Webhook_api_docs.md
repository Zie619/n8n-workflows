# API Documentation: Whatsapptrigger Workflow

## Overview
Automated workflow: Whatsapptrigger Workflow. This workflow integrates 14 different services: stickyNote, httpRequest, wait, lmChatGoogleGemini, agent. It contains 48 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 73
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.whatsAppTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.whatsAppTrigger`
- `n8n-nodes-base.wait`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.whatsApp`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.toolWikipedia`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `whatsAppApi`
- `googlePalmApi`
- `whatsAppTriggerApi`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`
