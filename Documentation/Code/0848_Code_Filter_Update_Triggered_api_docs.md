# API Documentation: Set Workflow

## Overview
Automated workflow: Set Workflow. This workflow integrates 10 different services: filter, stickyNote, googleDriveTrigger, code, googleDrive. It contains 24 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 29
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.googleDriveTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleDriveTrigger`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
