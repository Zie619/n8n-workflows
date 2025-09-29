# API Documentation: Scheduletrigger Workflow

## Overview
Automated workflow: Scheduletrigger Workflow. This workflow integrates 10 different services: microsoftOutlook, stickyNote, markdown, scheduleTrigger, chainLlm. It contains 13 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 18
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.microsoftOutlook`
- `n8n-nodes-base.jira`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.removeDuplicates`

## Integrations
- Microsoft

## Required Credentials
- `jiraSoftwareCloudApi`
- `openAiApi`
- `microsoftOutlookOAuth2Api`

## Environment Variables
- No environment variables required
