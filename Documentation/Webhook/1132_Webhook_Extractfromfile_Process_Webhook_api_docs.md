# API Documentation: Convert Squarespace Profiles to Shopify Customers in Google Sheets

## Overview
Automated workflow: Convert Squarespace Profiles to Shopify Customers in Google Sheets. This workflow integrates 7 different services: webhook, stickyNote, splitInBatches, stopAndError, manualTrigger. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 23
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.manualTrigger`

### Webhook Endpoints
- **Path**: `submit-profiles`
- **Method**: `POST`
- **Webhook ID**: `e09976b5-7525-422b-9834-3bc6e1c4a1b6`


## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
