# API Documentation: Flux Dev Image Generation Fal.ai

## Overview
Automated workflow: Flux Dev Image Generation Fal.ai. This workflow integrates 8 different services: stickyNote, httpRequest, wait, googleDrive, set. It contains 21 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 42
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.wait`

## Integrations
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `httpHeaderAuth`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
