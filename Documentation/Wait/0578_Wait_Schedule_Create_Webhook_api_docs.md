# API Documentation: Googledrive Workflow

## Overview
Automated workflow: Googledrive Workflow. This workflow integrates 17 different services: stickyNote, httpRequest, filter, wait, lmChatGoogleGemini. It contains 48 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 69
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.linear`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.wait`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `httpQueryAuth`
- `googlePalmApi`
- `linearApi`
- `googleDriveOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
