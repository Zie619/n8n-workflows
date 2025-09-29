# API Documentation: Readpdf Workflow

## Overview
Automated workflow: Readpdf Workflow. This workflow integrates 11 different services: stickyNote, code, gmailTrigger, readPDF, merge. It contains 20 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 25
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.readPDF`
- `n8n-nodes-base.openAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `openAiApi`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`
