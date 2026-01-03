#!/usr/bin/env python3
"""
N8N 工作流发现 AI 助手
用于查找和理解工作流的智能聊天界面。
"""

from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import json
import asyncio
import sqlite3
from datetime import datetime
import re

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
        """基于自然语言查询的智能工作流搜索。"""
        conn = self.get_db_connection()
        
        # 从查询中提取关键词和意图
        keywords = self.extract_keywords(query)
        intent = self.detect_intent(query)
        
        # 构建搜索查询
        search_terms = []
        for keyword in keywords:
            search_terms.append(f"name LIKE '%{keyword}%' OR description LIKE '%{keyword}%'")
        
        where_clause = " OR ".join(search_terms) if search_terms else "1=1"
        
        # 添加基于意图的过滤
        if intent == "automation":
            where_clause += " AND (trigger_type = 'Scheduled' OR trigger_type = 'Complex')"
        elif intent == "integration":
            where_clause += " AND trigger_type = 'Webhook'"
        elif intent == "manual":
            where_clause += " AND trigger_type = 'Manual'"
        
        query_sql = f"""
            SELECT * FROM workflows 
            WHERE {where_clause}
            ORDER BY 
                CASE WHEN active = 1 THEN 1 ELSE 2 END,
                node_count DESC
            LIMIT {limit}
        """
        
        cursor = conn.execute(query_sql)
        workflows = []
        for row in cursor.fetchall():
            workflow = dict(row)
            workflow['integrations'] = json.loads(workflow['integrations'] or '[]')
            workflow['tags'] = json.loads(workflow['tags'] or '[]')
            workflows.append(workflow)
        
        conn.close()
        return workflows
    
    def extract_keywords(self, query: str) -> List[str]:
        """从用户查询中提取相关关键词。"""
        # 常见的自动化术语
        automation_terms = {
            'email': ['email', 'gmail', 'mail'],
            'social': ['twitter', 'facebook', 'instagram', 'linkedin', 'social'],
            'data': ['data', 'database', 'spreadsheet', 'csv', 'excel'],
            'ai': ['ai', 'openai', 'chatgpt', 'artificial', 'intelligence'],
            'notification': ['notification', 'alert', 'slack', 'telegram', 'discord'],
            'automation': ['automation', 'workflow', 'process', 'automate'],
            'integration': ['integration', 'connect', 'sync', 'api']
        }
        
        query_lower = query.lower()
        keywords = []
        
        for category, terms in automation_terms.items():
            for term in terms:
                if term in query_lower:
                    keywords.append(term)
        
        # 提取特定服务名称
        services = ['slack', 'telegram', 'openai', 'google', 'microsoft', 'shopify', 'airtable']
        for service in services:
            if service in query_lower:
                keywords.append(service)
        
        return list(set(keywords))
    
    def detect_intent(self, query: str) -> str:
        """从查询中检测用户意图。"""
        query_lower = query.lower()
        
        if any(word in query_lower for word in ['automate', 'schedule', 'recurring', 'daily', 'weekly']):
            return "automation"
        elif any(word in query_lower for word in ['connect', 'integrate', 'sync', 'webhook']):
            return "integration"
        elif any(word in query_lower for word in ['manual', 'trigger', 'button', 'click']):
            return "manual"
        elif any(word in query_lower for word in ['ai', 'chat', 'assistant', 'intelligent']):
            return "ai"
        else:
            return "general"
    
    def generate_response(self, query: str, workflows: List[Dict]) -> str:
        """基于查询和工作流生成自然语言响应。"""
        if not workflows:
            return "我找不到符合您请求的工作流。尝试搜索特定服务，如 'Slack'、'OpenAI' 或 'Email automation'。"
        
        # 分析工作流模式
        trigger_types = [w['trigger_type'] for w in workflows]
        integrations = []
        for w in workflows:
            integrations.extend(w['integrations'])
        
        common_integrations = list(set(integrations))[:3]
        most_common_trigger = max(set(trigger_types), key=trigger_types.count)
        
        # 生成上下文响应
        response_parts = []
        
        if len(workflows) == 1:
            workflow = workflows[0]
            response_parts.append(f"我找到了完美匹配：**{workflow['name']}**")
            response_parts.append(f"这是一个 {workflow['trigger_type'].lower()} 工作流，{workflow['description'].lower()}")
        else:
            response_parts.append(f"我找到了 {len(workflows)} 个相关工作流：")
            
            for i, workflow in enumerate(workflows[:3], 1):
                response_parts.append(f"{i}. **{workflow['name']}** - {workflow['description']}")
        
        if common_integrations:
            response_parts.append(f"\n这些工作流通常使用：{', '.join(common_integrations)}")
        
        if most_common_trigger != 'all':
            response_parts.append(f"大多数是 {most_common_trigger.lower()} 触发的工作流。")
        
        return "\n".join(response_parts)
    
    def get_suggestions(self, query: str) -> List[str]:
        """基于查询生成有用的建议。"""
        suggestions = []
        
        if 'email' in query.lower():
            suggestions.extend([
                "电子邮件自动化工作流",
                "Gmail 集成示例",
                "电子邮件通知系统"
            ])
        elif 'ai' in query.lower() or 'openai' in query.lower():
            suggestions.extend([
                "AI 驱动的工作流",
                "OpenAI 集成示例",
                "聊天机器人自动化"
            ])
        elif 'social' in query.lower():
            suggestions.extend([
                "社交媒体自动化",
                "Twitter 集成工作流",
                "LinkedIn 自动化"
            ])
        else:
            suggestions.extend([
                "流行的自动化模式",
                "Webhook 触发的工作流",
                "计划自动化示例"
            ])
        
        return suggestions[:3]
    
    def calculate_confidence(self, query: str, workflows: List[Dict]) -> float:
        """计算响应的置信度分数。"""
        if not workflows:
            return 0.0
        
        # 基于匹配数量和相关性计算基础置信度
        base_confidence = min(len(workflows) / 5.0, 1.0)
        
        # 为精确匹配提升置信度
        query_lower = query.lower()
        exact_matches = 0
        for workflow in workflows:
            if any(word in workflow['name'].lower() for word in query_lower.split()):
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
    """与 AI 助手聊天以发现工作流。"""
    try:
        # 搜索相关工作流
        workflows = assistant.search_workflows_intelligent(message.message, limit=5)
        
        # 生成响应
        response_text = assistant.generate_response(message.message, workflows)
        
        # 获取建议
        suggestions = assistant.get_suggestions(message.message)
        
        # 计算置信度
        confidence = assistant.calculate_confidence(message.message, workflows)
        
        return AIResponse(
            response=response_text,
            workflows=workflows,
            suggestions=suggestions,
            confidence=confidence
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"助手错误：{str(e)}")

@ai_app.get("/chat/interface")
async def chat_interface():
    """获取聊天界面 HTML。"""
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
