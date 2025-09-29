# API Documentation: Manualtrigger Workflow

## Overview
Automated workflow: Manualtrigger Workflow. This workflow integrates 14 different services: textClassifier, filter, httpRequest, stickyNote, lmChatGoogleGemini. It contains 29 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 46
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.html`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googlePalmApi`
- `huggingFaceApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
