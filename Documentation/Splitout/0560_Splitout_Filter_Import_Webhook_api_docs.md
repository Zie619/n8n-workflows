# API Documentation: Spotify Workflow

## Overview
Automated workflow: Spotify Workflow. This workflow integrates 11 different services: stickyNote, httpRequest, filter, splitOut, switch. It contains 38 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 67
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.mqttTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.set`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.spotify`
- `n8n-nodes-base.if`
- `n8n-nodes-base.mqttTrigger`

## Integrations
- No external integrations detected

## Required Credentials
- `spotifyOAuth2Api`
- `mqtt`

## Environment Variables
- `API_BASE_URL`
