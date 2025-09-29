# API Documentation: Google Drive Automation

## Overview
Automated workflow: Google Drive Automation. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 25
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.googleDriveTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `@n8n/n8n-nodes-langchain.embeddingsGoogleGemini`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
- `n8n-nodes-base.googleDriveTrigger`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.vectorStorePinecone`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `openRouterApi`
- `googlePalmApi`
- `pineconeApi`

## Environment Variables
- `WEBHOOK_URL`
