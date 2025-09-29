# API Documentation: 🤖🧑‍💻 AI Agent  for Top n8n Creators Leaderboard Reporting

## Overview
Automated workflow: 🤖🧑‍💻 AI Agent  for Top n8n Creators Leaderboard Reporting. This workflow integrates 22 different services: convertToFile, stickyNote, scheduleTrigger, merge, lmChatOpenAi. It contains 59 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 72
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.convertToFile`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.sort`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.readWriteFile`
- `n8n-nodes-base.set`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google

## Required Credentials
- `openAiApi`
- `googlePalmApi`
- `gmailOAuth2`
- `googleDriveOAuth2Api`
- `telegramApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
