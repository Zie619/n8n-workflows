# API Documentation: Gmail Workflow

## Overview
Automated workflow: Gmail Workflow. This workflow integrates 7 different services: stickyNote, httpRequest, markdown, scheduleTrigger, splitOut. It contains 9 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 18
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
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `gmailOAuth2`

## Environment Variables
- `API_BASE_URL`
