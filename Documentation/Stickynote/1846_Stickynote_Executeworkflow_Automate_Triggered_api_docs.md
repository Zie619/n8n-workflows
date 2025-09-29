# API Documentation: My workflow

## Overview
Automated workflow: My workflow. This workflow integrates 6 different services: stickyNote, code, chainLlm, outputParserStructured, lmChatOpenRouter. It contains 12 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 17
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.executeWorkflowTrigger`

## Integrations
- No external integrations detected

## Required Credentials
- `openRouterApi`

## Environment Variables
- No environment variables required
