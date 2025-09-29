# API Documentation: Generate New Keywords with Search Volumes⚒️⚒️🟢🟢

## Overview
Automated workflow: Generate New Keywords with Search Volumes⚒️⚒️🟢🟢. This workflow integrates 7 different services: stickyNote, httpRequest, splitOut, set, stopAndError. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 23
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `googleAdsOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
