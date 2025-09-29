# API Documentation: Save New Sales Opportunities

## Overview
Automated workflow: Save New Sales Opportunities. This workflow integrates 6 different services: stickyNote, gmailTrigger, odoo, stopAndError, lmOpenAi. It contains 6 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 11
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.lmOpenAi`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `n8n-nodes-base.odoo`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- No external integrations detected

## Required Credentials
- `odooApi`
- `openAiApi`
- `gmailOAuth2`

## Environment Variables
- No environment variables required
