# API Documentation: OpenAI Assistant workflow: uploa file, create an Assistant, chat with it!

## Overview
Automated workflow: OpenAI Assistant workflow: uploa file, create an Assistant, chat with it!. This workflow integrates 6 different services: stickyNote, googleDrive, stopAndError, manualTrigger, openAi. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 19
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
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `openAiApi`

## Environment Variables
- `WEBHOOK_URL`
