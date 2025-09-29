# API Documentation: Postgrestrigger Workflow

## Overview
Automated workflow: Postgrestrigger Workflow. This workflow integrates 7 different services: filter, stickyNote, code, stopAndError, postgresTrigger. It contains 10 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 15
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.postgresTrigger`
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.code`
- `n8n-nodes-base.postgresTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `postgres`

## Environment Variables
- `WEBHOOK_URL`
