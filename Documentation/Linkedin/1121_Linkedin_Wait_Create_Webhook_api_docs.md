# API Documentation: Hacker News to Video Template - AlexK1919

## Overview
Automated workflow: Hacker News to Video Template - AlexK1919. This workflow integrates 22 different services: stickyNote, youTube, lmChatOpenAi, if, splitInBatches. It contains 82 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 147
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.twitter`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.microsoftOneDrive`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.toolHttpRequest`
- `n8n-nodes-base.hackerNews`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.wait`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.youTube`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.dropbox`
- `n8n-nodes-base.if`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.limit`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.s3`
- `n8n-nodes-base.set`
- `n8n-nodes-base.linkedIn`

## Integrations
- Google
- Microsoft

## Required Credentials
- `googleDriveOAuth2Api`
- `openAiApi`
- `httpCustomAuth`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`
