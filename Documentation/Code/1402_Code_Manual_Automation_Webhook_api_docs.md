# API Documentation: LinkedIn Web Scraping with Bright Data MCP Server & Google Gemini

## Overview
Automated workflow: LinkedIn Web Scraping with Bright Data MCP Server & Google Gemini. This workflow integrates 13 different services: stickyNote, httpRequest, code, lmChatGoogleGemini, readWriteFile. It contains 27 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 40
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.code`
- `n8n-nodes-base.function`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.readWriteFile`
- `n8n-nodes-mcp.mcpClient`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.informationExtractor`

## Integrations
- Google

## Required Credentials
- `googlePalmApi`
- `mcpClientApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
