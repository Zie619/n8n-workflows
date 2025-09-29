# API Documentation: Automated Content Generation & Publishing - Wordpress

## Overview
Automated workflow: Automated Content Generation & Publishing - Wordpress. This workflow integrates 10 different services: stickyNote, wordpress, httpRequest, wait, code. It contains 21 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 30
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.wordpress`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.wait`

## Integrations
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `wordpressApi`

## Environment Variables
- `BASE_URL`
