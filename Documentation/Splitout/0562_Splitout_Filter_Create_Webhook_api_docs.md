# API Documentation: Gmailtrigger Workflow

## Overview
Automated workflow: Gmailtrigger Workflow. This workflow integrates 11 different services: filter, stickyNote, httpRequest, gmailTrigger, splitOut. It contains 19 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 32
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.html`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `gmailOAuth2`

## Environment Variables
- `API_BASE_URL`
