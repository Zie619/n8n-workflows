# API Documentation: My workflow

## Overview
Automated workflow: My workflow. This workflow integrates 9 different services: stickyNote, formTrigger, hunter, noOp, discord. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 19
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.discord`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.if`
- `n8n-nodes-base.hunter`
- `n8n-nodes-base.gmail`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `gmailOAuth2`
- `discordWebhookApi`

## Environment Variables
- `WEBHOOK_URL`
