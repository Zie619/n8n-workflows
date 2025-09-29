# API Documentation: Splitout Workflow

## Overview
Automated workflow: Splitout Workflow. This workflow integrates 7 different services: stickyNote, httpRequest, scheduleTrigger, splitOut, set. It contains 27 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 44
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `googleOAuth2Api`
- `googleApi`
- `httpHeaderAuth`
- `googleSheetsOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
