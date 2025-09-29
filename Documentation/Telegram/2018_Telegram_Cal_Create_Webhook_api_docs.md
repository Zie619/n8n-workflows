# API Documentation: Meeting booked - to newsletter and CRM

## Overview
Automated workflow: Meeting booked - to newsletter and CRM. This workflow integrates 8 different services: stickyNote, httpRequest, calTrigger, telegram, splitOut. It contains 13 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 22
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.calTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.calTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `calApi`
- `googleSheetsOAuth2Api`
- `telegramApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
