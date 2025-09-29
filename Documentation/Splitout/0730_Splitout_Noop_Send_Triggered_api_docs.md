# API Documentation: Gmailtrigger Workflow

## Overview
Automated workflow: Gmailtrigger Workflow. This workflow integrates 7 different services: stickyNote, gmailTrigger, splitOut, googleDrive, switch. It contains 9 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 14
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`
