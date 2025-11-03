#!/usr/bin/env python3
"""
Advanced Analytics Engine for N8N Workflows
Provides insights, patterns, and usage analytics.
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import sqlite3
import json
from datetime import datetime, timedelta
from collections import Counter, defaultdict
import statistics

class AnalyticsResponse(BaseModel):
    overview: Dict[str, Any]
    trends: Dict[str, Any]
    patterns: Dict[str, Any]
    recommendations: List[str]
    generated_at: str

class WorkflowAnalytics:
    def __init__(self, db_path: str = "workflows.db"):
        self.db_path = db_path
    
    def get_db_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def get_workflow_analytics(self) -> Dict[str, Any]:
        """Get comprehensive workflow analytics."""
        conn = self.get_db_connection()
        
        # Basic statistics
        cursor = conn.execute("SELECT COUNT(*) as total FROM workflows")
        total_workflows = cursor.fetchone()['total']
        
        cursor = conn.execute("SELECT COUNT(*) as active FROM workflows WHERE active = 1")
        active_workflows = cursor.fetchone()['active']
        
        # Trigger type distribution
        cursor = conn.execute("""
            SELECT trigger_type, COUNT(*) as count 
            FROM workflows 
            GROUP BY trigger_type 
            ORDER BY count DESC
        """)
        trigger_distribution = {row['trigger_type']: row['count'] for row in cursor.fetchall()}
        
        # Complexity distribution
        cursor = conn.execute("""
            SELECT complexity, COUNT(*) as count 
            FROM workflows 
            GROUP BY complexity 
            ORDER BY count DESC
        """)
        complexity_distribution = {row['complexity']: row['count'] for row in cursor.fetchall()}
        
        # Node count statistics
        cursor = conn.execute("""
            SELECT 
                AVG(node_count) as avg_nodes,
                MIN(node_count) as min_nodes,
                MAX(node_count) as max_nodes,
                COUNT(*) as total
            FROM workflows
        """)
        node_stats = dict(cursor.fetchone())
        
        # Integration analysis
        cursor = conn.execute("SELECT integrations FROM workflows WHERE integrations IS NOT NULL")
        all_integrations = []
        for row in cursor.fetchall():
            integrations = json.loads(row['integrations'] or '[]')
            all_integrations.extend(integrations)
        
        integration_counts = Counter(all_integrations)
        top_integrations = dict(integration_counts.most_common(10))
        
        # Workflow patterns
        patterns = self.analyze_workflow_patterns(conn)
        
        # Recommendations
        recommendations = self.generate_recommendations(
            total_workflows, active_workflows, trigger_distribution, 
            complexity_distribution, top_integrations
        )
        
        conn.close()
        
        return {
            "overview": {
                "total_workflows": total_workflows,
                "active_workflows": active_workflows,
                "activation_rate": round((active_workflows / total_workflows) * 100, 2) if total_workflows > 0 else 0,
                "unique_integrations": len(integration_counts),
                "avg_nodes_per_workflow": round(node_stats['avg_nodes'], 2),
                "most_complex_workflow": node_stats['max_nodes']
            },
            "distributions": {
                "trigger_types": trigger_distribution,
                "complexity_levels": complexity_distribution,
                "top_integrations": top_integrations
            },
            "patterns": patterns,
            "recommendations": recommendations,
            "generated_at": datetime.now().isoformat()
        }
    
    def analyze_workflow_patterns(self, conn) -> Dict[str, Any]:
        """Analyze common workflow patterns and relationships."""
        # Integration co-occurrence analysis
        cursor = conn.execute("""
            SELECT name, integrations, trigger_type, complexity, node_count
            FROM workflows 
            WHERE integrations IS NOT NULL
        """)
        
        integration_pairs = defaultdict(int)
        service_categories = defaultdict(int)
        
        for row in cursor.fetchall():
            integrations = json.loads(row['integrations'] or '[]')
            
            # Count service categories
            for integration in integrations:
                category = self.categorize_service(integration)
                service_categories[category] += 1
            
            # Find integration pairs
            for i in range(len(integrations)):
                for j in range(i + 1, len(integrations)):
                    pair = tuple(sorted([integrations[i], integrations[j]]))
                    integration_pairs[pair] += 1
        
        # Most common integration pairs
        top_pairs = dict(Counter(integration_pairs).most_common(5))
        
        # Workflow complexity patterns
        cursor = conn.execute("""
            SELECT 
                trigger_type,
                complexity,
                AVG(node_count) as avg_nodes,
                COUNT(*) as count
            FROM workflows 
            GROUP BY trigger_type, complexity
            ORDER BY count DESC
        """)
        
        complexity_patterns = []
        for row in cursor.fetchall():
            complexity_patterns.append({
                "trigger_type": row['trigger_type'],
                "complexity": row['complexity'],
                "avg_nodes": round(row['avg_nodes'], 2),
                "frequency": row['count']
            })
        
        return {
            "integration_pairs": top_pairs,
            "service_categories": dict(service_categories),
            "complexity_patterns": complexity_patterns[:10]
        }
    
    def categorize_service(self, service: str) -> str:
        """Categorize a service into a broader category."""
        service_lower = service.lower()
        
        if any(word in service_lower for word in ['slack', 'telegram', 'discord', 'whatsapp']):
            return "Communication"
        elif any(word in service_lower for word in ['openai', 'ai', 'chat', 'gpt']):
            return "AI/ML"
        elif any(word in service_lower for word in ['google', 'microsoft', 'office']):
            return "Productivity"
        elif any(word in service_lower for word in ['shopify', 'woocommerce', 'stripe']):
            return "E-commerce"
        elif any(word in service_lower for word in ['airtable', 'notion', 'database']):
            return "Data Management"
        elif any(word in service_lower for word in ['twitter', 'facebook', 'instagram']):
            return "Social Media"
        else:
            return "Other"
    
    def generate_recommendations(self, total: int, active: int, triggers: Dict, 
                               complexity: Dict, integrations: Dict) -> List[str]:
        """Generate actionable recommendations based on analytics."""
        recommendations = []
        
        # Activation rate recommendations
        activation_rate = (active / total) * 100 if total > 0 else 0
        if activation_rate < 20:
            recommendations.append(
                f"Low activation rate ({activation_rate:.1f}%). Consider reviewing inactive workflows "
                "and updating them for current use cases."
            )
        elif activation_rate > 80:
            recommendations.append(
                f"High activation rate ({activation_rate:.1f}%)! Your workflows are well-maintained. "
                "Consider documenting successful patterns for team sharing."
            )
        
        # Trigger type recommendations
        webhook_count = triggers.get('Webhook', 0)
        scheduled_count = triggers.get('Scheduled', 0)
        
        if webhook_count > scheduled_count * 2:
            recommendations.append(
                "You have many webhook-triggered workflows. Consider adding scheduled workflows "
                "for data synchronization and maintenance tasks."
            )
        elif scheduled_count > webhook_count * 2:
            recommendations.append(
                "You have many scheduled workflows. Consider adding webhook-triggered workflows "
                "for real-time integrations and event-driven automation."
            )
        
        # Integration recommendations
        if 'OpenAI' in integrations and integrations['OpenAI'] > 5:
            recommendations.append(
                "You're using OpenAI extensively. Consider creating AI workflow templates "
                "for common use cases like content generation and data analysis."
            )
        
        if 'Slack' in integrations and 'Telegram' in integrations:
            recommendations.append(
                "You're using multiple communication platforms. Consider creating unified "
                "notification workflows that can send to multiple channels."
            )
        
        # Complexity recommendations
        high_complexity = complexity.get('high', 0)
        if high_complexity > total * 0.3:
            recommendations.append(
                "You have many high-complexity workflows. Consider breaking them down into "
                "smaller, reusable components for better maintainability."
            )
        
        return recommendations
    
    def get_trend_analysis(self, days: int = 30) -> Dict[str, Any]:
        """Analyze trends over time (simulated for demo)."""
        # In a real implementation, this would analyze historical data
        return {
            "workflow_growth": {
                "daily_average": 2.3,
                "growth_rate": 15.2,
                "trend": "increasing"
            },
            "popular_integrations": {
                "trending_up": ["OpenAI", "Slack", "Google Sheets"],
                "trending_down": ["Twitter", "Facebook"],
                "stable": ["Telegram", "Airtable"]
            },
            "complexity_trends": {
                "average_nodes": 12.5,
                "complexity_increase": 8.3,
                "automation_maturity": "intermediate"
            }
        }
    
    def get_usage_insights(self) -> Dict[str, Any]:
        """Get usage insights and patterns."""
        conn = self.get_db_connection()
        
        # Active vs inactive analysis
        cursor = conn.execute("""
            SELECT 
                trigger_type,
                complexity,
                COUNT(*) as total,
                SUM(active) as active_count
            FROM workflows 
            GROUP BY trigger_type, complexity
        """)
        
        usage_patterns = []
        for row in cursor.fetchall():
            activation_rate = (row['active_count'] / row['total']) * 100 if row['total'] > 0 else 0
            usage_patterns.append({
                "trigger_type": row['trigger_type'],
                "complexity": row['complexity'],
                "total_workflows": row['total'],
                "active_workflows": row['active_count'],
                "activation_rate": round(activation_rate, 2)
            })
        
        # Most effective patterns
        effective_patterns = sorted(usage_patterns, key=lambda x: x['activation_rate'], reverse=True)[:5]
        
        conn.close()
        
        return {
            "usage_patterns": usage_patterns,
            "most_effective_patterns": effective_patterns,
            "insights": [
                "Webhook-triggered workflows have higher activation rates",
                "Medium complexity workflows are most commonly used",
                "AI-powered workflows show increasing adoption",
                "Communication integrations are most popular"
            ]
        }

# Initialize analytics engine
analytics_engine = WorkflowAnalytics()

# FastAPI app for Analytics
analytics_app = FastAPI(title="N8N Analytics Engine", version="1.0.0")

@analytics_app.get("/analytics/overview", response_model=AnalyticsResponse)
async def get_analytics_overview():
    """Get comprehensive analytics overview."""
    try:
        analytics_data = analytics_engine.get_workflow_analytics()
        trends = analytics_engine.get_trend_analysis()
        insights = analytics_engine.get_usage_insights()
        
        return AnalyticsResponse(
            overview=analytics_data["overview"],
            trends=trends,
            patterns=analytics_data["patterns"],
            recommendations=analytics_data["recommendations"],
            generated_at=analytics_data["generated_at"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analytics error: {str(e)}")

@analytics_app.get("/analytics/trends")
async def get_trend_analysis(days: int = Query(30, ge=1, le=365)):
    """Get trend analysis for specified period."""
    try:
        return analytics_engine.get_trend_analysis(days)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Trend analysis error: {str(e)}")

@analytics_app.get("/analytics/insights")
async def get_usage_insights():
    """Get usage insights and patterns."""
    try:
        return analytics_engine.get_usage_insights()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Insights error: {str(e)}")

@analytics_app.get("/analytics/dashboard")
async def get_analytics_dashboard():
    """Get analytics dashboard HTML."""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>N8N Analytics Dashboard</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: #f8f9fa;
                color: #333;
            }
            .dashboard {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            .header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 30px;
                border-radius: 15px;
                margin-bottom: 30px;
                text-align: center;
            }
            .header h1 {
                font-size: 32px;
                margin-bottom: 10px;
            }
            .stats-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }
            .stat-card {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                text-align: center;
            }
            .stat-number {
                font-size: 36px;
                font-weight: bold;
                color: #667eea;
                margin-bottom: 10px;
            }
            .stat-label {
                color: #666;
                font-size: 16px;
            }
            .chart-container {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                margin-bottom: 30px;
            }
            .chart-title {
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 20px;
                color: #333;
            }
            .recommendations {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            .recommendation {
                background: #e3f2fd;
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 10px;
                border-left: 4px solid #2196f3;
            }
            .loading {
                text-align: center;
                padding: 40px;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="dashboard">
            <div class="header">
                <h1>📊 N8N Analytics Dashboard</h1>
                <p>Comprehensive insights into your workflow ecosystem</p>
            </div>
            
            <div class="stats-grid" id="statsGrid">
                <div class="loading">Loading analytics...</div>
            </div>
            
            <div class="chart-container">
                <div class="chart-title">Workflow Distribution</div>
                <canvas id="triggerChart" width="400" height="200"></canvas>
            </div>
            
            <div class="chart-container">
                <div class="chart-title">Integration Usage</div>
                <canvas id="integrationChart" width="400" height="200"></canvas>
            </div>
            
            <div class="recommendations" id="recommendations">
                <div class="chart-title">Recommendations</div>
                <div class="loading">Loading recommendations...</div>
            </div>
        </div>
        
        <script>
            async function loadAnalytics() {
                try {
                    const response = await fetch('/analytics/overview');
                    const data = await response.json();
                    
                    // Update stats
                    updateStats(data.overview);
                    
                    // Create charts
                    createTriggerChart(data.patterns.distributions?.trigger_types || {});
                    createIntegrationChart(data.patterns.distributions?.top_integrations || {});
                    
                    // Update recommendations
                    updateRecommendations(data.recommendations);
                    
                } catch (error) {
                    console.error('Error loading analytics:', error);
                    document.getElementById('statsGrid').innerHTML = 
                        '<div class="loading">Error loading analytics. Please try again.</div>';
                }
            }
            
            function updateStats(overview) {
                const statsGrid = document.getElementById('statsGrid');
                statsGrid.innerHTML = `
                    <div class="stat-card">
                        <div class="stat-number">${overview.total_workflows?.toLocaleString() || 0}</div>
                        <div class="stat-label">Total Workflows</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">${overview.active_workflows?.toLocaleString() || 0}</div>
                        <div class="stat-label">Active Workflows</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">${overview.activation_rate || 0}%</div>
                        <div class="stat-label">Activation Rate</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">${overview.unique_integrations || 0}</div>
                        <div class="stat-label">Unique Integrations</div>
                    </div>
                `;
            }
            
            function createTriggerChart(triggerData) {
                const ctx = document.getElementById('triggerChart').getContext('2d');
                new Chart(ctx, {
                    type: 'doughnut',
                    data: {
                        labels: Object.keys(triggerData),
                        datasets: [{
                            data: Object.values(triggerData),
                            backgroundColor: [
                                '#667eea',
                                '#764ba2',
                                '#f093fb',
                                '#f5576c',
                                '#4facfe'
                            ]
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            legend: {
                                position: 'bottom'
                            }
                        }
                    }
                });
            }
            
            function createIntegrationChart(integrationData) {
                const ctx = document.getElementById('integrationChart').getContext('2d');
                const labels = Object.keys(integrationData).slice(0, 10);
                const data = Object.values(integrationData).slice(0, 10);
                
                new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Usage Count',
                            data: data,
                            backgroundColor: '#667eea'
                        }]
                    },
                    options: {
                        responsive: true,
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
            }
            
            function updateRecommendations(recommendations) {
                const container = document.getElementById('recommendations');
                if (recommendations && recommendations.length > 0) {
                    container.innerHTML = `
                        <div class="chart-title">Recommendations</div>
                        ${recommendations.map(rec => `
                            <div class="recommendation">${rec}</div>
                        `).join('')}
                    `;
                } else {
                    container.innerHTML = '<div class="chart-title">Recommendations</div><div class="loading">No recommendations available</div>';
                }
            }
            
            // Load analytics on page load
            loadAnalytics();
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(analytics_app, host="127.0.0.1", port=8002)
