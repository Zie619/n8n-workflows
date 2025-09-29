# API Documentation: Telegramtrigger Workflow

## Overview
Automated workflow: Telegramtrigger Workflow. This workflow integrates 9 different services: telegramTrigger, stickyNote, telegram, switch, set. It contains 37 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 42
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.telegramTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.set`
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `telegramApi`

## Environment Variables
- `WEBHOOK_URL`
