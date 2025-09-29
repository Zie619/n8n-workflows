# API Documentation: Scheduletrigger Workflow

## Overview
Automated workflow: Scheduletrigger Workflow. This workflow integrates 12 different services: filter, stickyNote, scheduleTrigger, lmChatGoogleGemini, chainLlm. It contains 21 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 26
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`

## Integrations
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
