# API Documentation: LINE BOT - Google Sheets Record Receipt

## Overview
Automated workflow: LINE BOT - Google Sheets Record Receipt. This workflow integrates 8 different services: webhook, stickyNote, httpRequest, code, googleDrive. It contains 20 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 37
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `23ba996d-3242-42a1-946c-f04a680b320a`
- **Method**: `POST`
- **Webhook ID**: `23ba996d-3242-42a1-946c-f04a680b320a`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `googleSheetsOAuth2Api`
- `httpHeaderAuth`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
