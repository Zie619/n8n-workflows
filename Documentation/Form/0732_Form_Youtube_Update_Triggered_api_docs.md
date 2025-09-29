# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 10 different services: stickyNote, formTrigger, youTube, agent, outputParserStructured. It contains 13 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 16
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.form`
- `n8n-nodes-base.youTube`
- `n8n-nodes-base.formTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.googleDocsTool`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- No credentials required

## Environment Variables
- `BASE_URL`
