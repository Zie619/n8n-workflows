# API Documentation: Manualtrigger Workflow

## Overview
Automated workflow: Manualtrigger Workflow. This workflow integrates 15 different services: stickyNote, httpRequest, filter, code, splitOut. It contains 58 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 79
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google
- Google
- Google

## Required Credentials
- `hubspotOAuth2Api`
- `httpHeaderAuth`
- `gmailOAuth2`
- `googleSheetsOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
