# API Documentation: Load Prompts from Github Repo and auto populate n8n expressions

## Overview
Automated workflow: Load Prompts from Github Repo and auto populate n8n expressions. This workflow integrates 10 different services: stickyNote, code, agent, lmChatOllama, set. It contains 18 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 23
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.github`
- `@n8n/n8n-nodes-langchain.lmChatOllama`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Github

## Required Credentials
- `githubApi`
- `ollamaApi`

## Environment Variables
- No environment variables required
