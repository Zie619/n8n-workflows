# API Documentation: Airtop Web Agent

## Overview
Automated workflow: Airtop Web Agent. This workflow integrates 12 different services: stickyNote, formTrigger, agent, airtopTool, outputParserStructured. It contains 21 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 26
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.lmChatAnthropic`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.airtopTool`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.airtop`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack
- Slack

## Required Credentials
- `airtopApi`
- `anthropicApi`
- `slackOAuth2Api`

## Environment Variables
- `BASE_URL`
