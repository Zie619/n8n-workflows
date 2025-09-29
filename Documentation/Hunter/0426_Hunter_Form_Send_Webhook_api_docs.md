# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 10 different services: stickyNote, httpRequest, formTrigger, hunter, hubspot. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 26
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.hubspot`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.hunter`
- `n8n-nodes-base.gmail`

## Integrations
- Hubspot
- Hubspot

## Required Credentials
- `hubspotOAuth2Api`
- `hunterApi`
- `httpHeaderAuth`
- `gmailOAuth2`

## Environment Variables
- `BASE_URL`
