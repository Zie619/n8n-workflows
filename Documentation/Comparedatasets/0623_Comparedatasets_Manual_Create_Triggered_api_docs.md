# API Documentation: Comparedatasets Workflow

## Overview
Automated workflow: Comparedatasets Workflow. This workflow integrates 7 different services: stickyNote, youTube, set, spotify, manualTrigger. It contains 12 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 17
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.youTube`
- `n8n-nodes-base.compareDatasets`
- `n8n-nodes-base.set`
- `n8n-nodes-base.spotify`

## Integrations
- No external integrations detected

## Required Credentials
- `youTubeOAuth2Api`
- `spotifyOAuth2Api`

## Environment Variables
- No environment variables required
