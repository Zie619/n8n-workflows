# API Documentation: Jira Retrospective

## Overview
Automated workflow: Jira Retrospective. This workflow integrates 11 different services: stickyNote, agent, summarize, set, stopAndError. It contains 15 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 20
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.jiraTrigger`

## Node Types Used
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.jira`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleDocs`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.jiraTrigger`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `jiraSoftwareCloudApi`
- `openAiApi`
- `googleDocsOAuth2Api`

## Environment Variables
- `BASE_URL`
