# API Documentation: Automate LinkedIn Posts with AI

## Overview
Automated workflow: Automate LinkedIn Posts with AI. This workflow integrates 9 different services: stickyNote, httpRequest, scheduleTrigger, merge, stopAndError. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 23
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.notion`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.linkedIn`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `linkedInOAuth2Api`
- `notionApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
