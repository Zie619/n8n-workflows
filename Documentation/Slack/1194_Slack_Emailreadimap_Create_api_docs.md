# API Documentation: New invoice email notification

## Overview
Automated workflow: New invoice email notification. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 21
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- Manual trigger (no automatic triggers configured)

## Node Types Used
- `n8n-nodes-base.emailReadImap`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.mindee`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- `slackApi`
- `mindeeInvoiceApi`
- `smtp`
- `imap`

## Environment Variables
- No environment variables required
