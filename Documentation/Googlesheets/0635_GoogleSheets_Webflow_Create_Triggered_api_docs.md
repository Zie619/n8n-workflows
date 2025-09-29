# API Documentation: Code Workflow

## Overview
Automated workflow: Code Workflow. This workflow integrates 5 different services: stickyNote, code, stopAndError, webflowTrigger, googleSheets. It contains 8 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 13
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webflowTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.webflowTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `webflowOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
