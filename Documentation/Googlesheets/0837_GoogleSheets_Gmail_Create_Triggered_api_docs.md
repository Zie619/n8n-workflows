# API Documentation: Googledrive Workflow

## Overview
Automated workflow: Googledrive Workflow. This workflow integrates 10 different services: stickyNote, gmailTrigger, function, googleDrive, set. It contains 25 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 30
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.function`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `googleSheetsOAuth2Api`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`
