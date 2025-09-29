# API Documentation: WordPress Contact Form (CF7) Responses and Classification

## Overview
Automated workflow: WordPress Contact Form (CF7) Responses and Classification. This workflow integrates 10 different services: textClassifier, webhook, stickyNote, lmChatGoogleGemini, chainLlm. It contains 33 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 42
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `61858d25-af82-4cab-bb1b-68bea4989e15`
- **Method**: `POST`
- **Webhook ID**: `61858d25-af82-4cab-bb1b-68bea4989e15`


## Node Types Used
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
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
- `googleSheetsOAuth2Api`
- `googlePalmApi`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`
