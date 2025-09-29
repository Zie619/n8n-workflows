# API Documentation: Post New YouTube Videos to X

## Overview
Automated workflow: Post New YouTube Videos to X. This workflow integrates 6 different services: stickyNote, youTube, scheduleTrigger, stopAndError, twitter. It contains 7 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 12
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.youTube`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.twitter`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `twitterOAuth2Api`
- `youTubeOAuth2Api`

## Environment Variables
- No environment variables required
