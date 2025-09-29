# API Documentation: Tech Radar

## Overview
Automated workflow: Tech Radar. This workflow integrates 26 different services: stickyNote, textSplitterRecursiveCharacterTextSplitter, executeWorkflow, if, cron. It contains 65 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 78
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.cron`
- `n8n-nodes-base.googleDriveTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `radar-rag`
- **Method**: `POST`
- **Webhook ID**: `80952aa8-031a-4987-80dd-e24ad9479af1`


## Node Types Used
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.googleDriveTrigger`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.googleDocs`
- `@n8n/n8n-nodes-langchain.vectorStorePinecone`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.embeddingsGoogleGemini`
- `n8n-nodes-base.mySql`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.if`
- `@n8n/n8n-nodes-langchain.lmChatAnthropic`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.lmChatGroq`
- `n8n-nodes-base.cron`
- `@n8n/n8n-nodes-langchain.toolVectorStore`
- `n8n-nodes-base.mySqlTool`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `googlePalmApi`
- `mySql`
- `googleApi`
- `googleDriveOAuth2Api`
- `anthropicApi`
- `pineconeApi`
- `groqApi`

## Environment Variables
- `WEBHOOK_URL`
