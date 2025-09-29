# API Documentation: Googlesheetstool Workflow

## Overview
Automated workflow: Googlesheetstool Workflow. This workflow integrates 14 different services: stickyNote, formTrigger, filter, code, scheduleTrigger. It contains 23 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 28
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.form`
- `@n8n/n8n-nodes-langchain.code`
- `@n8n/n8n-nodes-langchain.informationExtractor`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.googleSheetsTool`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`
