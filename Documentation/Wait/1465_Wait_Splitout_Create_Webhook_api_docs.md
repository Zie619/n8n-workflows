# API Documentation: Search LinkedIn companies, Score with AI and add them to Google Sheet CRM

## Overview
Automated workflow: Search LinkedIn companies, Score with AI and add them to Google Sheet CRM. This workflow integrates 11 different services: stickyNote, httpRequest, wait, splitOut, set. It contains 25 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 38
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.wait`

## Integrations
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `httpHeaderAuth`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
