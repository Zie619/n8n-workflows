# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 6 different services: stickyNote, formTrigger, merge, stopAndError, googleSheets. It contains 11 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 16
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
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.openAi`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`

## Environment Variables
- `WEBHOOK_URL`
