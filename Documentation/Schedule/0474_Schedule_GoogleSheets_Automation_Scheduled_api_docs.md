# API Documentation: Scheduletrigger Workflow

## Overview
Automated workflow: Scheduletrigger Workflow. This workflow integrates 5 different services: stickyNote, scheduleTrigger, stopAndError, googleSheets, twitter. It contains 8 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 13
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.twitter`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `twitterOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
