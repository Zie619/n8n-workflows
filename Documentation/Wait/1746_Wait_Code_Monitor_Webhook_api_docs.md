# API Documentation: Live link checker

## Overview
Automated workflow: Live link checker. This workflow integrates 8 different services: stickyNote, httpRequest, wait, code, stopAndError. It contains 19 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 32
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.code`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.wait`

## Integrations
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `httpBasicAuth`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`
