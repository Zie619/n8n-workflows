# API Documentation: piepdrive-test

## Overview
Automated workflow: piepdrive-test. This workflow integrates 9 different services: pipedrive, stickyNote, httpRequest, markdown, code. It contains 12 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 21
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.pipedriveTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.code`
- `n8n-nodes-base.pipedriveTrigger`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.pipedrive`

## Integrations
- Slack

## Required Credentials
- `slackOAuth2Api`
- `openAiApi`
- `pipedriveApi`

## Environment Variables
- `API_BASE_URL`
