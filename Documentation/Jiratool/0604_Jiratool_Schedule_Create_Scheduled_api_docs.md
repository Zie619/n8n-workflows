# API Documentation: Lmchatopenai Workflow

## Overview
Automated workflow: Lmchatopenai Workflow. This workflow integrates 18 different services: textClassifier, notionTool, stickyNote, scheduleTrigger, agent. It contains 42 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 47
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.jira`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.slack`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.notionTool`
- `n8n-nodes-base.scheduleTrigger`
- `@n8n/n8n-nodes-langchain.sentimentAnalysis`
- `n8n-nodes-base.jiraTool`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack
- Slack

## Required Credentials
- `jiraSoftwareCloudApi`
- `slackApi`
- `openAiApi`
- `notionApi`

## Environment Variables
- No environment variables required
