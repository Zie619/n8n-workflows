# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 13 different services: stickyNote, formTrigger, wordpress, httpRequest, code. It contains 44 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 57
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.wordpress`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.form`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `@n8n/n8n-nodes-langchain.toolWikipedia`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `wordpressApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
