# API Documentation: Gmail to Vector Embeddings with PGVector and Ollama

## Overview
Automated workflow: Gmail to Vector Embeddings with PGVector and Ollama. This workflow integrates 15 different services: stickyNote, textSplitterRecursiveCharacterTextSplitter, code, gmailTrigger, splitOut. It contains 20 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 25
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.postgres`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.embeddingsOllama`
- `@n8n/n8n-nodes-langchain.vectorStorePGVector`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- No external integrations detected

## Required Credentials
- No credentials required

## Environment Variables
- No environment variables required
