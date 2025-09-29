# API Documentation: Gumroad sale trigger

## Overview
Automated workflow: Gumroad sale trigger. This workflow integrates 6 different services: stickyNote, httpRequest, stopAndError, mailerLite, googleSheets. It contains 11 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 20
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gumroadTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.mailerLite`
- `n8n-nodes-base.gumroadTrigger`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `gumroadApi`
- `googleSheetsOAuth2Api`
- `mailerLiteApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
