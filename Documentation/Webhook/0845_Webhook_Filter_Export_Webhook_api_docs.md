# API Documentation: Webhook Workflow

## Overview
Automated workflow: Webhook Workflow. This workflow integrates 8 different services: webhook, stickyNote, filter, airtable, set. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 26
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `poc-retell-analysis`
- **Method**: `POST`
- **Webhook ID**: `0208331f-eb06-489b-b133-c42be86b76d8`


## Node Types Used
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.notion`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `notionApi`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
