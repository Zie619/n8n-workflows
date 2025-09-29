# API Documentation: Manualtrigger Workflow

## Overview
Automated workflow: Manualtrigger Workflow. This workflow integrates 7 different services: stickyNote, splitOut, stopAndError, manualTrigger, gmail. It contains 9 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 14
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.linkedIn`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `linkedInOAuth2Api`
- `gmailOAuth2`

## Environment Variables
- No environment variables required
