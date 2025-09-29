# API Documentation: Analyze the sentiment of feedback and send a message on Mattermost

## Overview
Automated workflow: Analyze the sentiment of feedback and send a message on Mattermost. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 10
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.typeformTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.typeformTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.googleCloudNaturalLanguage`
- `n8n-nodes-base.mattermost`
- `n8n-nodes-base.if`

## Integrations
- Google

## Required Credentials
- `mattermostApi`
- `googleCloudNaturalLanguageOAuth2Api`
- `typeformApi`

## Environment Variables
- No environment variables required
