# API Documentation: Exponential Backoff for Google APIs

## Overview
Automated workflow: Exponential Backoff for Google APIs. This workflow integrates 8 different services: stickyNote, wait, code, stopAndError, manualTrigger. It contains 9 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 14
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.code`
- `n8n-nodes-base.wait`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleApi`

## Environment Variables
- `WEBHOOK_URL`
