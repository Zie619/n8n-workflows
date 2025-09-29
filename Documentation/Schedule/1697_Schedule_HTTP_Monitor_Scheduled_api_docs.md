# API Documentation: Amazon Product Price Tracker

## Overview
Automated workflow: Amazon Product Price Tracker. This workflow integrates 9 different services: stickyNote, httpRequest, scheduleTrigger, set, stopAndError. It contains 22 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 35
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
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
- `BASE_URL`
