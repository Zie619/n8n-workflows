# API Documentation: Email Summary Agent

## Overview
Automated workflow: Email Summary Agent. This workflow integrates 6 different services: stickyNote, scheduleTrigger, stopAndError, gmail, aggregate. It contains 10 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 15
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `gmailOAuth2`

## Environment Variables
- No environment variables required
