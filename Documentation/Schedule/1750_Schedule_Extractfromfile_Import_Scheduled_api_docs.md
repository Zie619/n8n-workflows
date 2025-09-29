# API Documentation: Vector DB Loader from Google Drive

## Overview
Automated workflow: Vector DB Loader from Google Drive. This workflow integrates 12 different services: stickyNote, textSplitterRecursiveCharacterTextSplitter, scheduleTrigger, googleDrive, switch. It contains 22 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 27
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.extractFromFile`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.vectorStorePGVector`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `openAiApi`
- `postgres`

## Environment Variables
- `WEBHOOK_URL`
