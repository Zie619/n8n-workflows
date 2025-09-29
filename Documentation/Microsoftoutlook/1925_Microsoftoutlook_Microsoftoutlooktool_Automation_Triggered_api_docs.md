# API Documentation: Outlook

## Overview
Automated workflow: Outlook. This workflow integrates 6 different services: stickyNote, agent, microsoftOutlookTrigger, stopAndError, lmChatOpenAi. It contains 10 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 15
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.microsoftOutlookTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.microsoftOutlookTool`
- `n8n-nodes-base.microsoftOutlookTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`

## Integrations
- Microsoft
- Microsoft

## Required Credentials
- `openAiApi`
- `microsoftOutlookOAuth2Api`

## Environment Variables
- No environment variables required
