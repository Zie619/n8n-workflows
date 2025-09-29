# API Documentation: Manualtrigger Workflow

## Overview
Automated workflow: Manualtrigger Workflow. This workflow integrates 11 different services: itemLists, salesforce, stickyNote, httpRequest, spreadsheetFile. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 26
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.renameKeys`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.itemLists`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.salesforce`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.spreadsheetFile`
- `n8n-nodes-base.stopAndError`

## Integrations
- Salesforce
- Salesforce
- Salesforce

## Required Credentials
- `salesforceOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
