# API Documentation: Test Webhooks in n8n Without Changing WEBHOOK_URL (PostBin & BambooHR Example)

## Overview
Automated workflow: Test Webhooks in n8n Without Changing WEBHOOK_URL (PostBin & BambooHR Example). This workflow integrates 20 different services: stickyNote, merge, outputParserAutofixing, lmChatOpenAi, postBin. It contains 73 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 102
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.slack`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.renameKeys`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.noOp`
- `@n8n/n8n-nodes-langchain.outputParserAutofixing`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.wait`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.bambooHr`
- `n8n-nodes-base.debugHelper`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.postBin`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`

## Integrations
- Slack

## Required Credentials
- `slackApi`
- `openAiApi`
- `httpBasicAuth`
- `bambooHrApi`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`
