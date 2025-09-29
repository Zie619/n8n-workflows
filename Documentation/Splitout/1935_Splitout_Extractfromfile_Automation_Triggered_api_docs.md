# API Documentation: Extract spend details (template)

## Overview
Automated workflow: Extract spend details (template). This workflow integrates 14 different services: stickyNote, gmailTrigger, lmChatGoogleGemini, splitOut, chainLlm. It contains 29 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 34
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`
- `n8n-nodes-base.gmailTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.lmChatGroq`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.html`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `googlePalmApi`
- `gmailOAuth2`
- `groqApi`

## Environment Variables
- `WEBHOOK_URL`
