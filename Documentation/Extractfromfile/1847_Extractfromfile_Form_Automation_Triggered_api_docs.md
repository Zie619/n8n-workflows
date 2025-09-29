# API Documentation: HR Job Posting and Evaluation with AI

## Overview
Automated workflow: HR Job Posting and Evaluation with AI. This workflow integrates 16 different services: stickyNote, formTrigger, airtable, agent, googleDrive. It contains 46 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 55
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.googleCalendarTool`
- `n8n-nodes-base.form`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.airtableTool`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.emailSend`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `openAiApi`
- `googleCalendarOAuth2Api`
- `googleDriveOAuth2Api`
- `smtp`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
