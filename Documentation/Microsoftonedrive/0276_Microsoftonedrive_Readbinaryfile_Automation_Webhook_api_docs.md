# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 11 different services: writeBinaryFile, stickyNote, httpRequest, readBinaryFile, spreadsheetFile. It contains 32 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 41
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.writeBinaryFile`
- `n8n-nodes-base.microsoftOneDrive`
- `n8n-nodes-base.ftp`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.readBinaryFile`
- `n8n-nodes-base.set`
- `n8n-nodes-base.spreadsheetFile`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Microsoft
- Google
- Microsoft

## Required Credentials
- `googleDriveOAuth2Api`
- `sftp`
- `microsoftOneDriveOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
