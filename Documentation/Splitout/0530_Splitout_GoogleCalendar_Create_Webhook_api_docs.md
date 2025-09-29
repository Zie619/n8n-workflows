# API Documentation: Lmchatopenai Workflow

## Overview
Automated workflow: Lmchatopenai Workflow. This workflow integrates 15 different services: stickyNote, httpRequest, agent, splitOut, googleDrive. It contains 38 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 51
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `n8n-nodes-base.set`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.googleCalendar`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google
- Google

## Required Credentials
- `googleOAuth2Api`
- `openAiApi`
- `googleCalendarOAuth2Api`
- `googleDriveOAuth2Api`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`
