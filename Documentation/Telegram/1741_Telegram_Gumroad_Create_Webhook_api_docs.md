# API Documentation: 2. Add Beehiiv newsletter subscribers from Gumroad sales

## Overview
Automated workflow: 2. Add Beehiiv newsletter subscribers from Gumroad sales. This workflow integrates 7 different services: stickyNote, httpRequest, telegram, set, stopAndError. It contains 16 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 29
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gumroadTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.gumroadTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `httpHeaderAuth`
- `gumroadApi`
- `telegramApi`
- `httpBearerAuth`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
