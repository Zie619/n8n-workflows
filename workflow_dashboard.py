#!/usr/bin/env python3
"""
Workflow Monitoring Dashboard
Real-time monitoring and analytics for n8n workflows
"""

import json
import os
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import time

@dataclass
class WorkflowStats:
    """Workflow statistics and health metrics"""
    name: str
    category: str
    nodes: int
    connections: int
    last_modified: datetime
    file_size: int
    quality_score: int
    status: str  # active, inactive, error, unknown
    execution_count: int = 0
    success_rate: float = 0.0
    avg_execution_time: float = 0.0
    last_execution: Optional[datetime] = None
    error_count: int = 0

class WorkflowDashboard:
    """Real-time workflow monitoring dashboard"""
    
    def __init__(self, workflows_dir: str = "workflows"):
        self.workflows_dir = Path(workflows_dir)
        self.stats: Dict[str, WorkflowStats] = {}
        self.categories = {}
        self.last_scan = None
        
    def scan_workflows(self) -> Dict[str, Any]:
        """Scan all workflows and collect statistics"""
        print("🔍 Scanning workflows for dashboard...")
        
        self.stats = {}
        self.categories = {}
        
        total_workflows = 0
        total_nodes = 0
        total_connections = 0
        total_size = 0
        
        for category_path in self.workflows_dir.iterdir():
            if category_path.is_dir():
                category = category_path.name
                self.categories[category] = {
                    'count': 0,
                    'nodes': 0,
                    'connections': 0,
                    'size': 0,
                    'active': 0,
                    'inactive': 0,
                    'errors': 0
                }
                
                for workflow_file in category_path.glob('*.json'):
                    try:
                        with open(workflow_file, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                        
                        # Get file stats
                        file_stat = workflow_file.stat()
                        last_modified = datetime.fromtimestamp(file_stat.st_mtime)
                        file_size = file_stat.st_size
                        
                        # Calculate quality score (simplified)
                        quality_score = self._calculate_quality_score(data)
                        
                        # Determine status
                        status = self._determine_status(data, quality_score)
                        
                        # Create workflow stats
                        workflow_name = data.get('name', workflow_file.stem)
                        stats = WorkflowStats(
                            name=workflow_name,
                            category=category,
                            nodes=len(data.get('nodes', [])),
                            connections=len(data.get('connections', {})),
                            last_modified=last_modified,
                            file_size=file_size,
                            quality_score=quality_score,
                            status=status
                        )
                        
                        self.stats[workflow_name] = stats
                        
                        # Update category stats
                        self.categories[category]['count'] += 1
                        self.categories[category]['nodes'] += stats.nodes
                        self.categories[category]['connections'] += stats.connections
                        self.categories[category]['size'] += file_size
                        
                        if status == 'active':
                            self.categories[category]['active'] += 1
                        elif status == 'error':
                            self.categories[category]['errors'] += 1
                        else:
                            self.categories[category]['inactive'] += 1
                        
                        # Update totals
                        total_workflows += 1
                        total_nodes += stats.nodes
                        total_connections += stats.connections
                        total_size += file_size
                        
                    except Exception as e:
                        print(f"⚠️ Error processing {workflow_file}: {e}")
                        continue
        
        self.last_scan = datetime.now()
        
        return {
            'total_workflows': total_workflows,
            'total_nodes': total_nodes,
            'total_connections': total_connections,
            'total_size_mb': round(total_size / (1024 * 1024), 2),
            'categories': self.categories,
            'last_scan': self.last_scan.isoformat()
        }
    
    def _calculate_quality_score(self, data: Dict) -> int:
        """Calculate quality score for a workflow"""
        score = 0
        
        # Basic structure (20 points)
        if 'name' in data and data['name']:
            score += 5
        if 'nodes' in data and data['nodes']:
            score += 10
        if 'connections' in data and data['connections']:
            score += 5
        
        # Node quality (30 points)
        nodes = data.get('nodes', [])
        if nodes:
            score += 10  # Has nodes
            if len(nodes) > 5:
                score += 10  # Substantial workflow
            if len(nodes) > 20:
                score += 10  # Complex workflow
        
        # Documentation (20 points)
        if 'description' in data and data['description']:
            score += 10
        if 'tags' in data and data['tags']:
            score += 10
        
        # Error handling (15 points)
        has_error_handling = any(
            node.get('type') in ['ErrorTrigger', 'If', 'Switch'] 
            for node in nodes
        )
        if has_error_handling:
            score += 15
        
        # Best practices (15 points)
        has_webhook = any(node.get('type') == 'n8n-nodes-base.webhook' for node in nodes)
        has_schedule = any(node.get('type') == 'n8n-nodes-base.cron' for node in nodes)
        if has_webhook or has_schedule:
            score += 15
        
        return min(score, 100)
    
    def _determine_status(self, data: Dict, quality_score: int) -> str:
        """Determine workflow status"""
        if quality_score >= 90:
            return 'active'
        elif quality_score >= 70:
            return 'inactive'
        else:
            return 'error'
    
    def get_dashboard_data(self) -> Dict[str, Any]:
        """Get comprehensive dashboard data"""
        scan_data = self.scan_workflows()
        
        # Calculate health metrics
        active_workflows = sum(1 for stats in self.stats.values() if stats.status == 'active')
        error_workflows = sum(1 for stats in self.stats.values() if stats.status == 'error')
        inactive_workflows = sum(1 for stats in self.stats.values() if stats.status == 'inactive')
        
        total_workflows = len(self.stats)
        health_percentage = (active_workflows / total_workflows * 100) if total_workflows > 0 else 0
        
        # Top categories by workflow count
        top_categories = sorted(
            self.categories.items(),
            key=lambda x: x[1]['count'],
            reverse=True
        )[:5]
        
        # Recent activity (workflows modified in last 7 days)
        recent_cutoff = datetime.now() - timedelta(days=7)
        recent_workflows = [
            stats for stats in self.stats.values()
            if stats.last_modified > recent_cutoff
        ]
        
        return {
            'overview': {
                'total_workflows': total_workflows,
                'active_workflows': active_workflows,
                'inactive_workflows': inactive_workflows,
                'error_workflows': error_workflows,
                'health_percentage': round(health_percentage, 1),
                'total_nodes': scan_data['total_nodes'],
                'total_connections': scan_data['total_connections'],
                'total_size_mb': scan_data['total_size_mb']
            },
            'categories': top_categories,
            'recent_activity': {
                'count': len(recent_workflows),
                'workflows': [
                    {
                        'name': wf.name,
                        'category': wf.category,
                        'last_modified': wf.last_modified.isoformat(),
                        'quality_score': wf.quality_score
                    }
                    for wf in recent_workflows[:10]  # Top 10 recent
                ]
            },
            'quality_distribution': self._get_quality_distribution(),
            'last_scan': self.last_scan.isoformat() if self.last_scan else None
        }
    
    def _get_quality_distribution(self) -> Dict[str, int]:
        """Get quality score distribution"""
        distribution = {
            'excellent (90-100)': 0,
            'good (70-89)': 0,
            'fair (50-69)': 0,
            'poor (0-49)': 0
        }
        
        for stats in self.stats.values():
            if stats.quality_score >= 90:
                distribution['excellent (90-100)'] += 1
            elif stats.quality_score >= 70:
                distribution['good (70-89)'] += 1
            elif stats.quality_score >= 50:
                distribution['fair (50-69)'] += 1
            else:
                distribution['poor (0-49)'] += 1
        
        return distribution
    
    def display_dashboard(self):
        """Display the dashboard in console"""
        data = self.get_dashboard_data()
        
        print("\n" + "="*80)
        print("🚀 N8N WORKFLOW DASHBOARD")
        print("="*80)
        
        # Overview
        overview = data['overview']
        print(f"\n📊 OVERVIEW:")
        print(f"   Total Workflows: {overview['total_workflows']}")
        print(f"   Active: {overview['active_workflows']} ({overview['health_percentage']}%)")
        print(f"   Inactive: {overview['inactive_workflows']}")
        print(f"   Errors: {overview['error_workflows']}")
        print(f"   Total Nodes: {overview['total_nodes']:,}")
        print(f"   Total Connections: {overview['total_connections']:,}")
        print(f"   Total Size: {overview['total_size_mb']} MB")
        
        # Quality Distribution
        print(f"\n🎯 QUALITY DISTRIBUTION:")
        for range_name, count in data['quality_distribution'].items():
            percentage = (count / overview['total_workflows'] * 100) if overview['total_workflows'] > 0 else 0
            print(f"   {range_name}: {count} ({percentage:.1f}%)")
        
        # Top Categories
        print(f"\n📁 TOP CATEGORIES:")
        for category, stats in data['categories']:
            print(f"   {category}: {stats['count']} workflows, {stats['nodes']} nodes")
        
        # Recent Activity
        recent = data['recent_activity']
        print(f"\n🕒 RECENT ACTIVITY (Last 7 days): {recent['count']} workflows modified")
        for wf in recent['workflows'][:5]:
            print(f"   • {wf['name']} ({wf['category']}) - Score: {wf['quality_score']}")
        
        print(f"\n🔄 Last Scan: {data['last_scan']}")
        print("="*80)

def main():
    """Main dashboard function"""
    dashboard = WorkflowDashboard()
    dashboard.display_dashboard()
    
    # Save dashboard data to file
    data = dashboard.get_dashboard_data()
    with open('dashboard_data.json', 'w') as f:
        json.dump(data, f, indent=2, default=str)
    
    print(f"\n💾 Dashboard data saved to: dashboard_data.json")

if __name__ == "__main__":
    main()
