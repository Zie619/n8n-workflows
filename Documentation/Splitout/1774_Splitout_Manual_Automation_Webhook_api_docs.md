# API Documentation: Extract Business Leads from Google Maps with Dumpling AI to Google Sheets

## Overview
Automated workflow: Extract Business Leads from Google Maps with Dumpling AI to Google Sheets. This workflow integrates 6 different services: stickyNote, httpRequest, splitOut, stopAndError, manualTrigger. It contains 8 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 17
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `httpHeaderAuth`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
