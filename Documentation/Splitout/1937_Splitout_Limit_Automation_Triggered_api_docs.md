# API Documentation: LinkedIn Profile Finder via Form using Bright Data & GPT-4o-mini

## Overview
Automated workflow: LinkedIn Profile Finder via Form using Bright Data & GPT-4o-mini. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 33
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-brightdata.brightData`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.form`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.html`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `brightdataApi`
- `openAiApi`
- `smtp`

## Environment Variables
- `BASE_URL`
