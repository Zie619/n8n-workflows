# API Documentation: Personal Portfolio Resume CV Chatbot

## Overview
Automated workflow: Personal Portfolio Resume CV Chatbot. This workflow integrates 19 different services: stickyNote, textSplitterRecursiveCharacterTextSplitter, scheduleTrigger, documentDefaultDataLoader, stopAndError. It contains 50 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 71
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.googleDriveTrigger`
- `n8n-nodes-base.googleDriveTrigger`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `chat`
- **Method**: `POST`
- **Webhook ID**: `3b67d073-6569-4b80-a54c-c06d59942569`

- **Path**: `update-conversation`
- **Method**: `POST`
- **Webhook ID**: `7d7d3488-beb9-435e-8728-7efcb8ea9f86`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.nocoDb`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.googleDriveTrigger`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.html`
- `@n8n/n8n-nodes-langchain.vectorStorePinecone`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.embeddingsGoogleGemini`
- `n8n-nodes-base.scheduleTrigger`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.toolVectorStore`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `googlePalmApi`
- `gmailOAuth2`
- `googleDriveOAuth2Api`
- `nocoDbApiToken`
- `pineconeApi`

## Environment Variables
- `WEBHOOK_URL`
