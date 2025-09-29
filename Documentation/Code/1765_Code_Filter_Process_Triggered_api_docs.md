# API Documentation: Colombian Invoices Processing

## Overview
Automated workflow: Colombian Invoices Processing. This workflow integrates 19 different services: stickyNote, merge, switch, lmChatOpenAi, xml. It contains 29 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 34
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`

## Node Types Used
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.toolCalculator`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.compression`
- `n8n-nodes-base.xml`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.gmailTrigger`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`

## Integrations
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
