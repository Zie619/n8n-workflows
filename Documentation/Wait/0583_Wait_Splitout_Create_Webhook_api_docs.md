# API Documentation: Gmail Workflow

## Overview
Automated workflow: Gmail Workflow. This workflow integrates 12 different services: stickyNote, httpRequest, wait, code, scheduleTrigger. It contains 34 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 63
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.code`
- `n8n-nodes-base.html`
- `n8n-nodes-base.wait`
- `n8n-nodes-base.openAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
