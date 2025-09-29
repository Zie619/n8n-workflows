# API Documentation: Googlesheetstrigger Workflow

## Overview
Automated workflow: Googlesheetstrigger Workflow. This workflow integrates 5 different services: stickyNote, code, googleSheetsTrigger, discord, stopAndError. It contains 6 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 11
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.googleSheetsTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.discord`
- `n8n-nodes-base.googleSheetsTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleSheetsTriggerOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
