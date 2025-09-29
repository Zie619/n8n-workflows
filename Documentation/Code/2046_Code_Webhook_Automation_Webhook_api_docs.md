# API Documentation: Docsify example

## Overview
Automated workflow: Docsify example. This workflow integrates 21 different services: convertToFile, stickyNote, merge, switch, outputParserAutofixing. It contains 77 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 106
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `/:file`
- **Method**: `POST`
- **Webhook ID**: `135bc21f-c7d0-4afe-be73-f984d444b43b`

- **Path**: `135bc21f-c7d0-4afe-be73-f984d444b43b`
- **Method**: `POST`
- **Webhook ID**: `8b719afe-8be3-4cd5-84ed-aca521b31a89`


## Node Types Used
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.code`
- `n8n-nodes-base.n8n`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.noOp`
- `@n8n/n8n-nodes-langchain.outputParserAutofixing`
- `n8n-nodes-base.html`
- `n8n-nodes-base.convertToFile`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.if`
- `n8n-nodes-base.executeCommand`
- `n8n-nodes-base.sort`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.readWriteFile`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `n8nApi`

## Environment Variables
- No environment variables required
