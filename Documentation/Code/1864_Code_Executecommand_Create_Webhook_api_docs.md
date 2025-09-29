# API Documentation: AutoClip – Automatically Generate Video Clips and Upload to YouTube

## Overview
Automated workflow: AutoClip – Automatically Generate Video Clips and Upload to YouTube. This workflow integrates 11 different services: stickyNote, httpRequest, code, readWriteFile, merge. It contains 39 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 52
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
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.code`
- `n8n-nodes-base.readWriteFile`
- `n8n-nodes-base.set`
- `n8n-nodes-base.executeCommand`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google
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
