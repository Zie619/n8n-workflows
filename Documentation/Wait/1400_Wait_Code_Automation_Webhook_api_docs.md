# API Documentation: AutoQoutesV2_template

## Overview
Automated workflow: AutoQoutesV2_template. This workflow integrates 10 different services: stickyNote, httpRequest, wait, code, readWriteFile. It contains 53 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 90
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.code`
- `n8n-nodes-base.readWriteFile`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.executeCommand`
- `n8n-nodes-base.wait`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `googleSheetsOAuth2Api`
- `youTubeOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
