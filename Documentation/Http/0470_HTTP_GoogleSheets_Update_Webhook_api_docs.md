# API Documentation: Googlesheetstrigger Workflow

## Overview
Automated workflow: Googlesheetstrigger Workflow. This workflow integrates 7 different services: stickyNote, httpRequest, googleSheetsTrigger, stopAndError, googleSheets. It contains 10 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 19
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.googleSheetsTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.googleSheetsTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.removeDuplicates`

## Integrations
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `googleSheetsTriggerOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
