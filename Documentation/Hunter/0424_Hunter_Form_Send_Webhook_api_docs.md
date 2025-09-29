# API Documentation: Formtrigger Workflow

## Overview
Automated workflow: Formtrigger Workflow. This workflow integrates 8 different services: stickyNote, httpRequest, formTrigger, hunter, stopAndError. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 23
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.hunter`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `hunterApi`
- `httpHeaderAuth`
- `gmailOAuth2`

## Environment Variables
- `BASE_URL`
