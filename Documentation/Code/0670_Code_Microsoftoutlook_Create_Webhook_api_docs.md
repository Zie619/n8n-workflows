# API Documentation: Gmailtrigger Workflow

## Overview
Automated workflow: Gmailtrigger Workflow. This workflow integrates 9 different services: stickyNote, httpRequest, code, gmailTrigger, microsoftOutlookTrigger. It contains 25 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 42
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`
- `n8n-nodes-base.microsoftOutlookTrigger`

## Node Types Used
- `n8n-nodes-base.jira`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.code`
- `n8n-nodes-base.microsoftOutlookTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- Microsoft

## Required Credentials
- `jiraSoftwareCloudApi`
- `openAiApi`
- `httpBasicAuth`
- `gmailOAuth2`
- `microsoftOutlookOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
