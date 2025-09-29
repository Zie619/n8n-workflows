# API Documentation: Vision-Based AI Agent Scraper - with Google Sheets, ScrapingBee, and Gemini

## Overview
Automated workflow: Vision-Based AI Agent Scraper - with Google Sheets, ScrapingBee, and Gemini. This workflow integrates 13 different services: stickyNote, httpRequest, markdown, lmChatGoogleGemini, agent. It contains 36 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 49
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `n8n-nodes-base.executeWorkflowTrigger`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `googleApi`
- `googlePalmApi`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`
