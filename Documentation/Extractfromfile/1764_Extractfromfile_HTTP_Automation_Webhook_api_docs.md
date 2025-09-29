# API Documentation: Attachments Gmail to drive and google sheets

## Overview
Automated workflow: Attachments Gmail to drive and google sheets. This workflow integrates 13 different services: stickyNote, httpRequest, gmailTrigger, chainLlm, googleDrive. It contains 25 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 34
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.lmOpenAi`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- Google
- Google
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `googleSheetsOAuth2Api`
- `openAiApi`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
