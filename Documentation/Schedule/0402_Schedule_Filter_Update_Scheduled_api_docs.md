# API Documentation: Filter Workflow

## Overview
Automated workflow: Filter Workflow. This workflow integrates 8 different services: filter, stickyNote, scheduleTrigger, merge, set. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 19
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`
