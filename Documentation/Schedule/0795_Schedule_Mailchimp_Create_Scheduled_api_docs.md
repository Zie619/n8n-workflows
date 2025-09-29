# API Documentation: Manualtrigger Workflow

## Overview
Automated workflow: Manualtrigger Workflow. This workflow integrates 7 different services: stickyNote, scheduleTrigger, stopAndError, mailchimp, manualTrigger. It contains 7 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 12
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.mailchimp`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `mailchimpApi`
- `googleSheetsOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
