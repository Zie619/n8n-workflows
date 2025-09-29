# API Documentation: Optimise images uploaded to GDrive

## Overview
Automated workflow: Optimise images uploaded to GDrive. This workflow integrates 5 different services: stickyNote, httpRequest, googleDriveTrigger, googleDrive, stopAndError. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 30
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.googleDriveTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleDriveTrigger`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`
