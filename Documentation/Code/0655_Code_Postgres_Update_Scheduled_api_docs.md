# API Documentation: Httprequest Workflow

## Overview
Automated workflow: Httprequest Workflow. This workflow integrates 12 different services: stickyNote, httpRequest, hubspot, code, scheduleTrigger. It contains 28 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 41
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.hubspot`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.if`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.postgres`
- `n8n-nodes-base.stopAndError`

## Integrations
- Hubspot
- Google

## Required Credentials
- `hubspotOAuth2Api`
- `postgres`
- `googleSheetsOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
