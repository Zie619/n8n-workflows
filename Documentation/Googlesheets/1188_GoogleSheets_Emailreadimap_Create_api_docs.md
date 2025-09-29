# API Documentation: Extract expenses from emails and add to Google Sheet

## Overview
Automated workflow: Extract expenses from emails and add to Google Sheet. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 16
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- Manual trigger (no automatic triggers configured)

## Node Types Used
- `n8n-nodes-base.emailReadImap`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.mindee`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `mindeeReceiptApi`
- `googleSheetsOAuth2Api`
- `imap`

## Environment Variables
- No environment variables required
