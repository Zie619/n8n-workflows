# API Documentation: Code Review workflow

## Overview
Automated workflow: Code Review workflow. This workflow integrates 9 different services: stickyNote, httpRequest, code, agent, githubTrigger. It contains 18 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 27
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.githubTrigger`

## Node Types Used
- `n8n-nodes-base.githubTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.github`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.googleSheetsTool`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`

## Integrations
- Github
- Github
- Github
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `githubOAuth2Api`
- `githubApi`

## Environment Variables
- `BASE_URL`
