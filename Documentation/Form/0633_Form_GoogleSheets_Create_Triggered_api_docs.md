# API Documentation: Googlesheets Workflow

## Overview
Automated workflow: Googlesheets Workflow. This workflow integrates 10 different services: stickyNote, formTrigger, crypto, merge, set. It contains 23 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 32
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.form`
- `n8n-nodes-base.crypto`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `smtp`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
