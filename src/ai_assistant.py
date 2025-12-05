#!/usr/bin/env python3
"""
AI Assistant for N8N Workflow Discovery
Intelligent chat interface for finding and understanding workflows.
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Dict, Optional
import json
import sqlite3


class ChatMessage(BaseModel):
    message: str
    user_id: Optional[str] = None


class AIResponse(BaseModel):
    response: str
    workflows: List[Dict] = []
    suggestions: List[str] = []
    confidence: float = 0.0


class WorkflowAssistant:
    def __init__(self, db_path: str = "workflows.db"):
        self.db_path = db_path
        self.conversation_history = {}

    def get_db_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def search_workflows_intelligent(self, query: str, limit: int = 5) -> List[Dict]:
        """Intelligent workflow search based on natural language query."""
        conn = self.get_db_connection()

        # Extract keywords and intent from query
        keywords = self.extract_keywords(query)
        intent = self.detect_intent(query)

        # Build search query
        search_terms = []
        for keyword in keywords:
            search_terms.append(
                f"name LIKE '%{keyword}%' OR description LIKE '%{keyword}%'"
            )

        where_clause = " OR ".join(search_terms) if search_terms else "1=1"

        # Add intent-based filtering
        if intent == "automation":
            where_clause += (
                " AND (trigger_type = 'Scheduled' OR trigger_type = 'Complex')"
            )
        elif intent == "integration":
            where_clause += " AND trigger_type = ?"
            params.append('Webhook')
        elif intent == "manual":
            where_clause += " AND trigger_type = 'Manual'"

        query_sql = f"""
            SELECT * FROM workflows 
            WHERE {where_clause}
            ORDER BY 
                CASE WHEN active = 1 THEN 1 ELSE 2 END,
                node_count DESC
            LIMIT ?
        """

        cursor = conn.execute(query_sql)
        workflows = []
        for row in cursor.fetchall():
            workflow = dict(row)
            workflow["integrations"] = json.loads(workflow["integrations"] or "[]")
            workflow["tags"] = json.loads(workflow["tags"] or "[]")
            workflows.append(workflow)

        conn.close()
        return workflows

    def extract_keywords(self, query: str) -> List[str]:
        """Extract relevant keywords from user query."""
        # Common automation terms
        automation_terms = {
            "email": ["email", "gmail", "mail"],
            "social": ["twitter", "facebook", "instagram", "linkedin", "social"],
            "data": ["data", "database", "spreadsheet", "csv", "excel"],
            "ai": ["ai", "openai", "chatgpt", "artificial", "intelligence"],
            "notification": ["notification", "alert", "slack", "telegram", "discord"],
            "automation": ["automation", "workflow", "process", "automate"],
            "integration": ["integration", "connect", "sync", "api"],
        }

        query_lower = query.lower()
        keywords = []

        for category, terms in automation_terms.items():
            for term in terms:
                if term in query_lower:
                    keywords.append(term)

        # Extract specific service names
        services = [
            "slack",
            "telegram",
            "openai",
            "google",
            "microsoft",
            "shopify",
            "airtable",
        ]
        for service in services:
            if service in query_lower:
                keywords.append(service)

        return list(set(keywords))

    def detect_intent(self, query: str) -> str:
        """Detect user intent from query."""
        query_lower = query.lower()

        if any(
            word in query_lower
            for word in ["automate", "schedule", "recurring", "daily", "weekly"]
        ):
            return "automation"
        elif any(
            word in query_lower for word in ["connect", "integrate", "sync", "webhook"]
        ):
            return "integration"
        elif any(
            word in query_lower for word in ["manual", "trigger", "button", "click"]
        ):
            return "manual"
        elif any(
            word in query_lower for word in ["ai", "chat", "assistant", "intelligent"]
        ):
            return "ai"
        else:
            return "general"

    def generate_response(self, query: str, workflows: List[Dict]) -> str:
        """Generate natural language response based on query and workflows."""
        if not workflows:
            return "I couldn't find any workflows matching your request. Try searching for specific services like 'Slack', 'OpenAI', or 'Email automation'."

        # Analyze workflow patterns
        trigger_types = [w["trigger_type"] for w in workflows]
        integrations = []
        for w in workflows:
            integrations.extend(w["integrations"])

        common_integrations = list(set(integrations))[:3]
        most_common_trigger = max(set(trigger_types), key=trigger_types.count)

        # Generate contextual response
        response_parts = []

        if len(workflows) == 1:
            workflow = workflows[0]
            response_parts.append(f"I found a perfect match: **{workflow['name']}**")
            response_parts.append(
                f"This is a {workflow['trigger_type'].lower()} workflow that {workflow['description'].lower()}"
            )
        else:
            response_parts.append(f"I found {len(workflows)} relevant workflows:")

            for i, workflow in enumerate(workflows[:3], 1):
                response_parts.append(
                    f"{i}. **{workflow['name']}** - {workflow['description']}"
                )

        if common_integrations:
            response_parts.append(
                f"\nThese workflows commonly use: {', '.join(common_integrations)}"
            )

        if most_common_trigger != "all":
            response_parts.append(
                f"Most are {most_common_trigger.lower()} triggered workflows."
            )

        return "\n".join(response_parts)

    def get_suggestions(self, query: str) -> List[str]:
        """Generate helpful suggestions based on query."""
        suggestions = []

        if "email" in query.lower():
            suggestions.extend(
                [
                    "Email automation workflows",
                    "Gmail integration examples",
                    "Email notification systems",
                ]
            )
        elif "ai" in query.lower() or "openai" in query.lower():
            suggestions.extend(
                [
                    "AI-powered workflows",
                    "OpenAI integration examples",
                    "Chatbot automation",
                ]
            )
        elif "social" in query.lower():
            suggestions.extend(
                [
                    "Social media automation",
                    "Twitter integration workflows",
                    "LinkedIn automation",
                ]
            )
        else:
            suggestions.extend(
                [
                    "Popular automation patterns",
                    "Webhook-triggered workflows",
                    "Scheduled automation examples",
                ]
            )

        return suggestions[:3]

    def calculate_confidence(self, query: str, workflows: List[Dict]) -> float:
        """Calculate confidence score for the response."""
        if not workflows:
            return 0.0

        # Base confidence on number of matches and relevance
        base_confidence = min(len(workflows) / 5.0, 1.0)

        # Boost confidence for exact matches
        query_lower = query.lower()
        exact_matches = 0
        for workflow in workflows:
            if any(word in workflow["name"].lower() for word in query_lower.split()):
                exact_matches += 1

        if exact_matches > 0:
            base_confidence += 0.2

        return min(base_confidence, 1.0)


# Initialize assistant
assistant = WorkflowAssistant()

# FastAPI app for AI Assistant
ai_app = FastAPI(title="N8N AI Assistant", version="1.0.0")


@ai_app.post("/chat", response_model=AIResponse)
async def chat_with_assistant(message: ChatMessage):
    """Chat with the AI assistant to discover workflows."""
    try:
        # Search for relevant workflows
        workflows = assistant.search_workflows_intelligent(message.message, limit=5)

        # Generate response
        response_text = assistant.generate_response(message.message, workflows)

        # Get suggestions
        suggestions = assistant.get_suggestions(message.message)

        # Calculate confidence
        confidence = assistant.calculate_confidence(message.message, workflows)

        return AIResponse(
            response=response_text,
            workflows=workflows,
            suggestions=suggestions,
            confidence=confidence,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Assistant error: {str(e)}")


@ai_app.get("/chat/interface")
async def chat_interface():
    """Get the chat interface HTML."""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>N8N AI Assistant</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .chat-container {
                width: 90%;
                max-width: 800px;
                height: 80vh;
                background: white;
                border-radius: 20px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                display: flex;
                flex-direction: column;
                overflow: hidden;
            }
            .chat-header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 20px;
                text-align: center;
            }
            .chat-header h1 {
                font-size: 24px;
                margin-bottom: 5px;
            }
            .chat-messages {
                flex: 1;
                padding: 20px;
                overflow-y: auto;
                background: #f8f9fa;
            }
            .message {
                margin-bottom: 15px;
                display: flex;
                align-items: flex-start;
            }
            .message.user {
                justify-content: flex-end;
            }
            .message.assistant {
                justify-content: flex-start;
            }
            .message-content {
                max-width: 70%;
                padding: 15px 20px;
                border-radius: 20px;
                word-wrap: break-word;
            }
            .message.user .message-content {
                background: #667eea;
                color: white;
                border-bottom-right-radius: 5px;
            }
            .message.assistant .message-content {
                background: white;
                color: #333;
                border: 1px solid #e9ecef;
                border-bottom-left-radius: 5px;
            }
            .workflow-card {
                background: #f8f9fa;
                border: 1px solid #e9ecef;
                border-radius: 10px;
                padding: 15px;
                margin: 10px 0;
            }
            .workflow-title {
                font-weight: bold;
                color: #667eea;
                margin-bottom: 5px;
            }
            .workflow-description {
                color: #666;
                font-size: 14px;
                margin-bottom: 10px;
            }
            .workflow-meta {
                display: flex;
                gap: 10px;
                flex-wrap: wrap;
            }
            .meta-tag {
                background: #e9ecef;
                padding: 4px 8px;
                border-radius: 12px;
                font-size: 12px;
                color: #666;
            }
            .suggestions {
                margin-top: 10px;
            }
            .suggestion {
                background: #e3f2fd;
                color: #1976d2;
                padding: 8px 12px;
                border-radius: 15px;
                margin: 5px 5px 5px 0;
                display: inline-block;
                cursor: pointer;
                font-size: 14px;
                transition: all 0.3s ease;
            }
            .suggestion:hover {
                background: #1976d2;
                color: white;
            }
            .chat-input {
                padding: 20px;
                background: white;
                border-top: 1px solid #e9ecef;
                display: flex;
                gap: 10px;
            }
            .chat-input input {
                flex: 1;
                padding: 15px;
                border: 2px solid #e9ecef;
                border-radius: 25px;
                font-size: 16px;
                outline: none;
                transition: border-color 0.3s ease;
            }
            .chat-input input:focus {
                border-color: #667eea;
            }
            .send-btn {
                background: #667eea;
                color: white;
                border: none;
                border-radius: 50%;
                width: 50px;
                height: 50px;
                cursor: pointer;
                font-size: 18px;
                transition: all 0.3s ease;
            }
            .send-btn:hover {
                background: #5a6fd8;
                transform: scale(1.05);
            }
            .typing {
                color: #666;
                font-style: italic;
            }
        </style>
    </head>
    <body>
        <div class="chat-container">
            <div class="chat-header">
                <h1>🤖 N8N AI Assistant</h1>
                <p>Ask me about workflows and automation</p>
            </div>
            <div class="chat-messages" id="chatMessages">
                <div class="message assistant">
                    <div class="message-content">
                        👋 Hi! I'm your N8N workflow assistant. I can help you find workflows for:
                        <div class="suggestions">
                            <span class="suggestion" onclick="sendMessage('Show me email automation workflows')">Email automation</span>
                            <span class="suggestion" onclick="sendMessage('Find AI-powered workflows')">AI workflows</span>
                            <span class="suggestion" onclick="sendMessage('Show me Slack integrations')">Slack integrations</span>
                            <span class="suggestion" onclick="sendMessage('Find webhook workflows')">Webhook workflows</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="chat-input">
                <input type="text" id="messageInput" placeholder="Ask about workflows..." onkeypress="handleKeyPress(event)">
                <button class="send-btn" onclick="sendMessage()">➤</button>
            </div>
        </div>
        
        <script>
            async function sendMessage(message = null) {
                const input = document.getElementById('messageInput');
                const messageText = message || input.value.trim();
                
                if (!messageText) return;
                
                // Add user message
                addMessage(messageText, 'user');
                input.value = '';
                
                // Show typing indicator
                const typingId = addMessage('Thinking...', 'assistant', true);
                
                try {
                    const response = await fetch('/chat', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ message: messageText })
                    });
                    
                    const data = await response.json();
                    
                    // Remove typing indicator
                    document.getElementById(typingId).remove();
                    
                    // Add assistant response
                    addAssistantMessage(data);
                    
                } catch (error) {
                    document.getElementById(typingId).remove();
                    addMessage('Sorry, I encountered an error. Please try again.', 'assistant');
                }
            }
            
            function addMessage(text, sender, isTyping = false) {
                const messagesContainer = document.getElementById('chatMessages');
                const messageDiv = document.createElement('div');
                const messageId = 'msg_' + Date.now();
                messageDiv.id = messageId;
                messageDiv.className = `message ${sender}`;
                
                const contentDiv = document.createElement('div');
                contentDiv.className = 'message-content';
                if (isTyping) {
                    contentDiv.className += ' typing';
                }
                contentDiv.textContent = text;
                
                messageDiv.appendChild(contentDiv);
                messagesContainer.appendChild(messageDiv);
                messagesContainer.scrollTop = messagesContainer.scrollHeight;
                
                return messageId;
            }
            
            function addAssistantMessage(data) {
                const messagesContainer = document.getElementById('chatMessages');
                const messageDiv = document.createElement('div');
                messageDiv.className = 'message assistant';
                
                const contentDiv = document.createElement('div');
                contentDiv.className = 'message-content';
                
                // Add response text
                contentDiv.innerHTML = data.response.replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');
                
                // Add workflow cards
                if (data.workflows && data.workflows.length > 0) {
                    data.workflows.forEach(workflow => {
                        const workflowCard = document.createElement('div');
                        workflowCard.className = 'workflow-card';
                        workflowCard.innerHTML = `
                            <div class="workflow-title">${workflow.name}</div>
                            <div class="workflow-description">${workflow.description}</div>
                            <div class="workflow-meta">
                                <span class="meta-tag">${workflow.trigger_type}</span>
                                <span class="meta-tag">${workflow.complexity}</span>
                                <span class="meta-tag">${workflow.node_count} nodes</span>
                                ${workflow.active ? '<span class="meta-tag" style="background: #d4edda; color: #155724;">Active</span>' : ''}
                            </div>
                        `;
                        contentDiv.appendChild(workflowCard);
                    });
                }
                
                // Add suggestions
                if (data.suggestions && data.suggestions.length > 0) {
                    const suggestionsDiv = document.createElement('div');
                    suggestionsDiv.className = 'suggestions';
                    data.suggestions.forEach(suggestion => {
                        const suggestionSpan = document.createElement('span');
                        suggestionSpan.className = 'suggestion';
                        suggestionSpan.textContent = suggestion;
                        suggestionSpan.onclick = () => sendMessage(suggestion);
                        suggestionsDiv.appendChild(suggestionSpan);
                    });
                    contentDiv.appendChild(suggestionsDiv);
                }
                
                messageDiv.appendChild(contentDiv);
                messagesContainer.appendChild(messageDiv);
                messagesContainer.scrollTop = messagesContainer.scrollHeight;
            }
            
            function handleKeyPress(event) {
                if (event.key === 'Enter') {
                    sendMessage();
                }
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(ai_app, host="127.0.0.1", port=8001)
