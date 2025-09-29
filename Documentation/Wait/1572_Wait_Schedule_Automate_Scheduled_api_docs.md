# API Documentation: WhatsApp business bot

## Overview
Automated workflow: WhatsApp business bot. This workflow integrates 11 different services: filter, stickyNote, wait, googleSheetsTrigger, scheduleTrigger. It contains 19 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 24
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.whatsAppTrigger`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.googleSheetsTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.googleSheetsTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.whatsAppTrigger`
- `n8n-nodes-base.whatsApp`
- `n8n-nodes-base.if`
- `n8n-nodes-base.wait`

## Integrations
- Google
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `googleSheetsTriggerOAuth2Api`
- `whatsAppApi`
- `whatsAppTriggerApi`

## Environment Variables
- `WEBHOOK_URL`
