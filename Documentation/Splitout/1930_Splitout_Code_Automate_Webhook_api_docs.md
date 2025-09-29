# API Documentation: AI powered SEO Keyword Research Automation - The vibe Marketer

## Overview
Automated workflow: AI powered SEO Keyword Research Automation - The vibe Marketer. This workflow integrates 14 different services: webhook, stickyNote, code, agent, splitOut. It contains 41 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 50
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `ac7e989d-6e32-4850-83c4-f10421467fb8`
- **Method**: `POST`
- **Webhook ID**: `ac7e989d-6e32-4850-83c4-f10421467fb8`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-dataforseo.dataForSeo`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.nocoDb`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.code`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack
- Slack

## Required Credentials
- `slackApi`
- `openAiApi`
- `nocoDbApiToken`
- `dataForSeoApi`

## Environment Variables
- No environment variables required
