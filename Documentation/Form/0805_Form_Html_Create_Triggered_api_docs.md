# API Documentation: Brightdata Workflow

## Overview
Automated workflow: Brightdata Workflow. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 20
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-brightdata.brightData`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.form`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.html`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-document-generator.documentGenerator`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `brightdataApi`
- `openAiApi`
- `smtp`

## Environment Variables
- `WEBHOOK_URL`
