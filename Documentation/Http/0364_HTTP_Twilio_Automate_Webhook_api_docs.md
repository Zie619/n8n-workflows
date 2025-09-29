# API Documentation: BillBot

## Overview
Automated workflow for data processing and integration.

## Workflow Metadata
- **Total Nodes**: 6
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.telegramTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.twilio`
- `n8n-nodes-base.set`
- `n8n-nodes-base.telegramTrigger`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `telegramApi`
- `httpHeaderAuth`
- `twilioApi`

## Environment Variables
- `BASE_URL`
