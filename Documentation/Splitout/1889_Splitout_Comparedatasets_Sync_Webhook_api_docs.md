# API Documentation: Entra Contacts to Zammad User Sync

## Overview
Automated workflow: Entra Contacts to Zammad User Sync. This workflow integrates 10 different services: stickyNote, httpRequest, splitOut, merge, set. It contains 16 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 25
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.zammad`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.compareDatasets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `microsoftOAuth2Api`
- `microsoftGraphSecurityOAuth2Api`
- `zammadTokenAuthApi`

## Environment Variables
- `WEBHOOK_URL`
