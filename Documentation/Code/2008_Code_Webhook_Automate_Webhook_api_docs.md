# API Documentation: Automated Work Attendance with Location Triggers

## Overview
Automated workflow: Automated Work Attendance with Location Triggers. This workflow integrates 8 different services: webhook, stickyNote, code, googleDrive, set. It contains 15 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 24
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `time-track`
- **Method**: `POST`
- **Webhook ID**: `801c8367-af7b-4371-8684-cc699090b97f`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `googleSheetsOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
