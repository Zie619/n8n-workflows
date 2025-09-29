# API Documentation: GitLab MR Auto-Review & Risk Assessment

## Overview
Automated workflow: GitLab MR Auto-Review & Risk Assessment. This workflow integrates 12 different services: stickyNote, httpRequest, code, agent, merge. It contains 27 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 40
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gitlabTrigger`
- `n8n-nodes-base.gitlabTrigger`
- `n8n-nodes-base.gitlabTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.lmChatAnthropic`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.outputParserAutofixing`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.gitlabTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `anthropicApi`
- `gmailOAuth2`
- `gitlabApi`

## Environment Variables
- `BASE_URL`
