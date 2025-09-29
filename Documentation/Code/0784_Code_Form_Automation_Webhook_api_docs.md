# API Documentation: Formtrigger Workflow

## Overview
Automated workflow: Formtrigger Workflow. This workflow integrates 6 different services: stickyNote, httpRequest, formTrigger, code, googleDrive. It contains 11 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 20
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `googleDocsOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
