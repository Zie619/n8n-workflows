# API Documentation: ✨🩷Automated Social Media Content Publishing Factory + System Prompt Composition

## Overview
Automated workflow: ✨🩷Automated Social Media Content Publishing Factory + System Prompt Composition. This workflow integrates 16 different services: stickyNote, httpRequest, facebookGraphApi, code, agent. It contains 74 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 103
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.facebookGraphApi`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.googleDocs`
- `n8n-nodes-base.twitter`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.linkedIn`

## Integrations
- Google
- Google

## Required Credentials
- `openAiApi`
- `linkedInOAuth2Api`
- `gmailOAuth2`
- `googleDocsOAuth2Api`
- `facebookGraphApi`
- `twitterOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
