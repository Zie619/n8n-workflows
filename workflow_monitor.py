#!/usr/bin/env python3
"""
n8n Workflow Monitor
Real-time monitoring and health check system for n8n workflows
"""

import json
import os
import time
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any
import requests
from collections import defaultdict

class WorkflowMonitor:
    def __init__(self, workflows_dir="workflows"):
        self.workflows_dir = Path(workflows_dir)
        self.monitoring_data = {
            'last_check': None,
            'workflow_status': {},
            'performance_metrics': {},
            'error_counts': defaultdict(int),
            'execution_stats': defaultdict(int)
        }
        
    def check_workflow_health(self, workflow_data: Dict) -> Dict[str, Any]:
        """Check health status of a single workflow"""
        health_status = {
            'status': 'healthy',
            'issues': [],
            'warnings': [],
            'metrics': {}
        }
        
        nodes = workflow_data.get('nodes', [])
        
        # Check for common issues
        if not nodes:
            health_status['status'] = 'critical'
            health_status['issues'].append('No nodes found')
        
        # Check for error handling
        has_error_handling = any('error' in node.get('type', '').lower() for node in nodes)
        if not has_error_handling:
            health_status['warnings'].append('No error handling found')
        
        # Check for webhooks (security risk if not properly configured)
        webhook_nodes = [node for node in nodes if 'webhook' in node.get('type', '').lower()]
        if webhook_nodes:
            health_status['warnings'].append(f'{len(webhook_nodes)} webhook nodes found - ensure proper security')
        
        # Check workflow complexity
        if len(nodes) > 20:
            health_status['warnings'].append(f'Complex workflow with {len(nodes)} nodes')
        
        # Calculate complexity score
        complexity_score = min(100, max(0, 100 - len(nodes) * 2))
        health_status['metrics']['complexity_score'] = complexity_score
        
        return health_status
    
    def generate_health_report(self) -> Dict[str, Any]:
        """Generate comprehensive health report for all workflows"""
        print("🏥 Generating workflow health report...")
        
        health_report = {
            'timestamp': datetime.now().isoformat(),
            'total_workflows': 0,
            'healthy_workflows': 0,
            'warning_workflows': 0,
            'critical_workflows': 0,
            'workflow_details': {},
            'common_issues': defaultdict(int),
            'recommendations': []
        }
        
        for category_dir in self.workflows_dir.iterdir():
            if category_dir.is_dir():
                for workflow_file in category_dir.glob('*.json'):
                    try:
                        with open(workflow_file, 'r', encoding='utf-8') as f:
                            workflow_data = json.load(f)
                        
                        health_status = self.check_workflow_health(workflow_data)
                        workflow_name = workflow_data.get('name', workflow_file.stem)
                        
                        health_report['total_workflows'] += 1
                        health_report['workflow_details'][workflow_name] = health_status
                        
                        if health_status['status'] == 'healthy':
                            health_report['healthy_workflows'] += 1
                        elif health_status['status'] == 'warning':
                            health_report['warning_workflows'] += 1
                        else:
                            health_report['critical_workflows'] += 1
                        
                        # Track common issues
                        for issue in health_status['issues']:
                            health_report['common_issues'][issue] += 1
                        for warning in health_status['warnings']:
                            health_report['common_issues'][warning] += 1
                            
                    except Exception as e:
                        health_report['workflow_details'][workflow_file.name] = {
                            'status': 'error',
                            'issues': [f'Failed to parse: {str(e)}']
                        }
                        health_report['critical_workflows'] += 1
        
        # Generate recommendations
        if health_report['warning_workflows'] > health_report['total_workflows'] * 0.3:
            health_report['recommendations'].append('Consider adding error handling to more workflows')
        
        if health_report['common_issues']['No error handling found'] > 0:
            health_report['recommendations'].append('Add error handling nodes to workflows without them')
        
        return health_report
    
    def create_dashboard_html(self, health_report: Dict[str, Any]) -> str:
        """Create HTML dashboard for workflow monitoring"""
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>n8n Workflow Monitor Dashboard</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; text-align: center; }}
        .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 30px; }}
        .stat-card {{ background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center; }}
        .stat-number {{ font-size: 2.5em; font-weight: bold; margin-bottom: 10px; }}
        .healthy {{ color: #4CAF50; }}
        .warning {{ color: #FF9800; }}
        .critical {{ color: #F44336; }}
        .total {{ color: #2196F3; }}
        .workflow-list {{ background: white; border-radius: 10px; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        .workflow-item {{ padding: 15px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center; }}
        .workflow-item:last-child {{ border-bottom: none; }}
        .status-badge {{ padding: 5px 15px; border-radius: 20px; color: white; font-size: 0.9em; }}
        .status-healthy {{ background: #4CAF50; }}
        .status-warning {{ background: #FF9800; }}
        .status-critical {{ background: #F44336; }}
        .recommendations {{ background: #fff3cd; border: 1px solid #ffeaa7; border-radius: 10px; padding: 20px; margin-top: 20px; }}
        .recommendations h3 {{ color: #856404; margin-top: 0; }}
        .recommendations ul {{ color: #856404; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔧 n8n Workflow Monitor Dashboard</h1>
            <p>Last updated: {health_report['timestamp']}</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number total">{health_report['total_workflows']}</div>
                <div>Total Workflows</div>
            </div>
            <div class="stat-card">
                <div class="stat-number healthy">{health_report['healthy_workflows']}</div>
                <div>Healthy</div>
            </div>
            <div class="stat-card">
                <div class="stat-number warning">{health_report['warning_workflows']}</div>
                <div>Warnings</div>
            </div>
            <div class="stat-card">
                <div class="stat-number critical">{health_report['critical_workflows']}</div>
                <div>Critical</div>
            </div>
        </div>
        
        <div class="workflow-list">
            <h2>📊 Workflow Health Status</h2>
"""
        
        # Add workflow items
        for workflow_name, details in health_report['workflow_details'].items():
            status_class = f"status-{details['status']}"
            html_content += f"""
            <div class="workflow-item">
                <div>
                    <strong>{workflow_name}</strong>
                    <br><small>Complexity Score: {details.get('metrics', {}).get('complexity_score', 'N/A')}</small>
                </div>
                <div>
                    <span class="status-badge {status_class}">{details['status'].upper()}</span>
                </div>
            </div>
"""
        
        html_content += """
        </div>
        
        <div class="recommendations">
            <h3>💡 Recommendations</h3>
            <ul>
"""
        
        for recommendation in health_report['recommendations']:
            html_content += f"<li>{recommendation}</li>"
        
        html_content += """
            </ul>
        </div>
    </div>
    
    <script>
        // Auto-refresh every 5 minutes
        setTimeout(() => location.reload(), 300000);
    </script>
</body>
</html>
"""
        
        return html_content
    
    def save_dashboard(self, health_report: Dict[str, Any]):
        """Save monitoring dashboard to HTML file"""
        html_content = self.create_dashboard_html(health_report)
        
        with open("workflow_dashboard.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print("📊 Dashboard saved to: workflow_dashboard.html")
    
    def run_monitoring(self):
        """Run complete monitoring process"""
        print("🔍 Starting workflow monitoring...")
        
        health_report = self.generate_health_report()
        
        # Print summary
        print(f"\n📊 HEALTH SUMMARY:")
        print(f"   Total Workflows: {health_report['total_workflows']}")
        print(f"   Healthy: {health_report['healthy_workflows']} ({health_report['healthy_workflows']/health_report['total_workflows']*100:.1f}%)")
        print(f"   Warnings: {health_report['warning_workflows']} ({health_report['warning_workflows']/health_report['total_workflows']*100:.1f}%)")
        print(f"   Critical: {health_report['critical_workflows']} ({health_report['critical_workflows']/health_report['total_workflows']*100:.1f}%)")
        
        if health_report['recommendations']:
            print(f"\n💡 RECOMMENDATIONS:")
            for rec in health_report['recommendations']:
                print(f"   • {rec}")
        
        # Save dashboard
        self.save_dashboard(health_report)
        
        # Save detailed report
        with open("workflow_health_report.json", "w") as f:
            json.dump(health_report, f, indent=2)
        
        print(f"\n📄 Detailed health report saved to: workflow_health_report.json")
        print(f"🌐 Open workflow_dashboard.html in your browser to view the dashboard")

def main():
    """Main monitoring function"""
    monitor = WorkflowMonitor()
    monitor.run_monitoring()

if __name__ == "__main__":
    main()
