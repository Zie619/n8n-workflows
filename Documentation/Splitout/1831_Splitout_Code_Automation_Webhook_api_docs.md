# API Documentation: 🎦🚀 YouTube Video Comment Analysis Agent

## Overview
Automated workflow: 🎦🚀 YouTube Video Comment Analysis Agent. This workflow integrates 16 different services: stickyNote, httpRequest, markdown, code, agent. It contains 31 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 44
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.code`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.gmail`

## Integrations
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `openAiApi`
- `gmailOAuth2`

## Environment Variables
- `BASE_URL`
