

# 🤖 Telegram AI Bot Template

#

# Overview
A complete Telegram bot template that integrates with OpenAI to provide intelligent responses to user messages. This template demonstrates the most popular communication automation pattern found in the n8n workflows collection.

#

# Features

- ✅ **Real-time messaging*

* with Telegram integration

- ✅ **AI-powered responses*

* using OpenAI GPT models

- ✅ **Typing indicators*

* for better user experience

- ✅ **Message preprocessing*

* for clean data handling

- ✅ **Configurable AI settings*

* (temperature, tokens, system prompts)

- ✅ **Error handling*

* and response management

#

# Prerequisites

#

## Required Credentials

1. **Telegram Bot Token*

*

 

  - Create a bot via [@BotFather](<https://t.me/botfathe>r)

   - Save your bot token securely

2. **OpenAI API Key*

*

 

  - Get your API key from [OpenAI Platform](<https://platform.openai.com>/)

   - Ensure you have sufficient credits

#

## Environment Setup

- n8n instance (version 1.0+)

- Internet connectivity for API calls

#

# Installation Guide

#

## Step 1: Import the Template

1. Download `telegram-ai-bot-template.json`

2. In n8n, go to **Workflows*

* → **Import from File*

*

3. Select the downloaded template file

#

## Step 2: Configure Credentials

#

### Telegram Bot Setup

1. In the workflow, click on **Telegram Trigger*

* node

2. Go to **Credentials*

* tab

3. Create new credential with your bot token

4. Test the connection

#

### OpenAI Setup

1. Click on **OpenAI Chat*

* node

2. Go to **Credentials*

* tab

3. Create new credential with your API key

4. Test the connection

#

## Step 3: Customize Settings

#

### Bot Behavior
Edit the **Bot Settings*

* node to customize:

- **System Prompt**: Define your bot's personality and role

- **Temperature**: Control response creativity (0.0-1.0)

- **Max Tokens**: Limit response length

#

### Example System Prompts
```text

text

# Customer Support Bot
"You are a helpful customer support assistant. Provide friendly, accurate, and concise answers to customer questions."

# Educational Bot
"You are an educational assistant. Help students learn by providing clear explanations, examples, and study tips."

# Business Assistant
"You are a professional business assistant. Provide accurate information about company policies, procedures, and services."
```text

text

#

## Step 4: Test and Activate

1. **Test the workflow*

* using the test button

2. **Send a message*

* to your bot on Telegram

3. **Verify responses*

* are working correctly

4. **Activate the workflow*

* when satisfied

#

# Customization Options

#

## Adding Commands
To add slash commands (e.g., `/start`, `/help`):

1. Add a **Switch*

* node after **Preprocess Message*

*

2. Configure conditions for different commands

3. Create separate response paths for each command

#

## Adding Image Generation
To enable image generation:

1. Add an **OpenAI Image Generation*

* node

2. Create a command handler for `/image`

3. Send images via **Telegram Send Photo*

* node

#

## Adding Memory
To remember conversation history:

1. Add a **Memory Buffer Window*

* node

2. Store conversation context

3. Include previous messages in AI prompts

#

## Multi-language Support
To support multiple languages:

1. Detect user language in **Preprocess Message*

*

2. Set appropriate system prompts per language

3. Configure OpenAI to respond in user's language

#

# Troubleshooting

#

## Common Issues

#

### Bot Not Responding

- ✅ Check Telegram bot token is correct

- ✅ Verify bot is activated in Telegram

- ✅ Ensure workflow is active in n8n

#

### OpenAI Errors

- ✅ Verify API key is valid and has credits

- ✅ Check rate limits and usage quotas

- ✅ Ensure model name is correct

#

### Slow Responses

- ✅ Reduce max_tokens for faster responses

- ✅ Use GPT-3.5-turbo instead of GPT-4

- ✅ Optimize system prompt length

#

## Performance Optimization

#

### Response Speed

- Use **GPT-3.5-turbo*

* for faster responses

- Set **max_tokens*

* to 200-300 for quick replies

- Cache frequently used responses

#

### Cost Management

- Monitor OpenAI usage and costs

- Set token limits to control expenses

- Use shorter system prompts

#

# Security Considerations

#

## Data Protection

- 🔒 **Never log user messages*

* in production

- 🔒 **Use environment variables*

* for API keys

- 🔒 **Implement rate limiting*

* to prevent abuse

- 🔒 **Validate user input*

* before processing

#

## Privacy

- 🔒 **Don't store personal information*

* unnecessarily

- 🔒 **Comply with GDPR*

* and privacy regulations

- 🔒 **Inform users*

* about data usage

#

# Use Cases

#

## Customer Support

- Automated customer inquiries

- FAQ responses

- Ticket routing and escalation

#

## Education

- Study assistance

- Homework help

- Learning companion

#

## Business

- Lead qualification

- Appointment scheduling

- Information provision

#

## Entertainment

- Interactive games

- Storytelling

- Trivia and quizzes

#

# Advanced Features

#

## Analytics Integration
Add tracking nodes to monitor:

- Message volume

- Response times

- User satisfaction

#

## Multi-Channel Support
Extend to support:

- WhatsApp Business API

- Slack integration

- Discord bots

#

## AI Model Switching
Implement dynamic model selection:

- GPT-4 for complex queries

- GPT-3.5 for simple responses

- Custom models for specific domains

#

# Support and Updates

#

## Getting Help

- 📖 Check n8n documentation

- 💬 Join n8n community forums

- 🐛 Report issues on GitHub

#

## Template Updates
This template is regularly updated with:

- New features and improvements

- Security patches

- Performance optimizations

- Compatibility updates

--

-

*Template Version: 1.0

*  
*Last Updated: 2025-01-27

*  
*Compatibility: n8n 1.0+

*
