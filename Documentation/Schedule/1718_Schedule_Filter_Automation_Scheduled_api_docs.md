# API Documentation: Todoist Workflow

## Overview
Automated workflow: Todoist Workflow. This workflow integrates 7 different services: stickyNote, filter, scheduleTrigger, set, stopAndError. It contains 13 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 18
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.todoist`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `todoistApi`

## Environment Variables
- No environment variables required
