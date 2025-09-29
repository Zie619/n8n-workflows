# API Documentation: Youtube Workflow

## Overview
Automated workflow: Youtube Workflow. This workflow integrates 10 different services: stickyNote, youTube, httpRequest, filter, scheduleTrigger. It contains 20 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 33
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.rssFeedRead`
- `n8n-nodes-base.youTube`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `youTubeOAuth2Api`
- `smtp`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`
