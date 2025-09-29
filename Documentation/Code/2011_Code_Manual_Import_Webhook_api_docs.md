# API Documentation: Import multiple Manufacturers from Google Sheets to Shopware 6

## Overview
Automated workflow: Import multiple Manufacturers from Google Sheets to Shopware 6. This workflow integrates 9 different services: stickyNote, httpRequest, code, set, stopAndError. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 30
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
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `oAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
