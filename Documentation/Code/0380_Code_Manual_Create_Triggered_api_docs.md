# API Documentation: Googledrive Workflow

## Overview
Automated workflow: Googledrive Workflow. This workflow integrates 9 different services: stickyNote, code, merge, googleDrive, set. It contains 11 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 16
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`

## Environment Variables
- No environment variables required
