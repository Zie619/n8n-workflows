# API Documentation: n8n Community Topic Tracker by Keyword

## Overview
Automated workflow: n8n Community Topic Tracker by Keyword. This workflow integrates 9 different services: stickyNote, httpRequest, googleSheetsTrigger, scheduleTrigger, splitOut. It contains 16 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 29
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.googleSheetsTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.googleSheetsTrigger`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Slack

## Required Credentials
- `googleSheetsOAuth2Api`
- `googleSheetsTriggerOAuth2Api`
- `smtp`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
