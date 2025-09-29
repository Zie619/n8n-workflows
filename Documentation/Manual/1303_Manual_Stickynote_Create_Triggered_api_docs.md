# API Documentation: Build an OpenAI Assistant with Google Drive Integration

## Overview
Automated workflow: Build an OpenAI Assistant with Google Drive Integration. This workflow integrates 7 different services: stickyNote, googleDrive, stopAndError, manualTrigger, memoryBufferWindow. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 22
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `openAiApi`

## Environment Variables
- `WEBHOOK_URL`
