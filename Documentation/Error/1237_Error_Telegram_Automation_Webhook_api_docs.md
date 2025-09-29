# API Documentation: google drive to instagram, tiktok and youtube

## Overview
Automated workflow: google drive to instagram, tiktok and youtube. This workflow integrates 11 different services: writeBinaryFile, stickyNote, httpRequest, googleDriveTrigger, telegram. It contains 27 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 44
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.googleDriveTrigger`
- `n8n-nodes-base.errorTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.writeBinaryFile`
- `n8n-nodes-base.googleDriveTrigger`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.errorTrigger`
- `n8n-nodes-base.readBinaryFile`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `openAiApi`
- `httpHeaderAuth`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
