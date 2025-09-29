#!/usr/bin/env python3
"""
n8n Workflow Performance Analyzer
Analyzes workflow performance, complexity, and optimization opportunities
"""

import json
import os
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Tuple
from collections import defaultdict
import statistics

class WorkflowPerformanceAnalyzer:
    def __init__(self, workflows_dir="workflows"):
        self.workflows_dir = Path(workflows_dir)
        self.analysis_results = {
            'performance_metrics': {},
            'complexity_analysis': {},
            'optimization_opportunities': {},
            'best_practices_score': {},
            'recommendations': []
        }
        
    def analyze_workflow_complexity(self, workflow_data: Dict) -> Dict[str, Any]:
        """Analyze workflow complexity metrics"""
        nodes = workflow_data.get('nodes', [])
        connections = workflow_data.get('connections', {})
        
        complexity_metrics = {
            'node_count': len(nodes),
            'connection_count': sum(len(conns) for conns in connections.values()),
            'max_depth': self.calculate_max_depth(nodes, connections),
            'branching_factor': self.calculate_branching_factor(connections),
            'cyclomatic_complexity': self.calculate_cyclomatic_complexity(nodes, connections),
            'node_type_diversity': len(set(node.get('type', '') for node in nodes)),
            'complexity_score': 0
        }
        
        # Calculate overall complexity score (0-100)
        complexity_score = 0
        
        # Node count factor (0-25 points)
        if complexity_metrics['node_count'] <= 5:
            complexity_score += 25
        elif complexity_metrics['node_count'] <= 10:
            complexity_score += 20
        elif complexity_metrics['node_count'] <= 20:
            complexity_score += 15
        elif complexity_metrics['node_count'] <= 50:
            complexity_score += 10
        else:
            complexity_score += 5
        
        # Depth factor (0-25 points)
        if complexity_metrics['max_depth'] <= 3:
            complexity_score += 25
        elif complexity_metrics['max_depth'] <= 5:
            complexity_score += 20
        elif complexity_metrics['max_depth'] <= 8:
            complexity_score += 15
        elif complexity_metrics['max_depth'] <= 12:
            complexity_score += 10
        else:
            complexity_score += 5
        
        # Branching factor (0-25 points)
        if complexity_metrics['branching_factor'] <= 2:
            complexity_score += 25
        elif complexity_metrics['branching_factor'] <= 3:
            complexity_score += 20
        elif complexity_metrics['branching_factor'] <= 4:
            complexity_score += 15
        elif complexity_metrics['branching_factor'] <= 6:
            complexity_score += 10
        else:
            complexity_score += 5
        
        # Cyclomatic complexity (0-25 points)
        if complexity_metrics['cyclomatic_complexity'] <= 5:
            complexity_score += 25
        elif complexity_metrics['cyclomatic_complexity'] <= 10:
            complexity_score += 20
        elif complexity_metrics['cyclomatic_complexity'] <= 15:
            complexity_score += 15
        elif complexity_metrics['cyclomatic_complexity'] <= 25:
            complexity_score += 10
        else:
            complexity_score += 5
        
        complexity_metrics['complexity_score'] = complexity_score
        return complexity_metrics
    
    def calculate_max_depth(self, nodes: List[Dict], connections: Dict) -> int:
        """Calculate maximum depth of workflow execution"""
        # Find trigger nodes (nodes with no incoming connections)
        trigger_nodes = []
        for node in nodes:
            node_id = node.get('id', '')
            is_trigger = True
            for source_connections in connections.values():
                for output_connections in source_connections.values():
                    if isinstance(output_connections, list):
                        for connection in output_connections:
                            if isinstance(connection, dict) and connection.get('node') == node_id:
                                is_trigger = False
                                break
            if is_trigger:
                trigger_nodes.append(node_id)
        
        def get_depth(node_id, visited=None):
            if visited is None:
                visited = set()
            
            if node_id in visited:
                return 0  # Circular reference
            
            visited.add(node_id)
            max_child_depth = 0
            
            if node_id in connections:
                for output_connections in connections[node_id].values():
                    if isinstance(output_connections, list):
                        for connection in output_connections:
                            if isinstance(connection, dict) and 'node' in connection:
                                child_depth = get_depth(connection['node'], visited.copy())
                                max_child_depth = max(max_child_depth, child_depth)
            
            return max_child_depth + 1
        
        max_depth = 0
        for trigger in trigger_nodes:
            depth = get_depth(trigger)
            max_depth = max(max_depth, depth)
        
        return max_depth
    
    def calculate_branching_factor(self, connections: Dict) -> float:
        """Calculate average branching factor"""
        if not connections:
            return 0
        
        total_branches = 0
        total_nodes = 0
        
        for node_id, node_connections in connections.items():
            if 'main' in node_connections:
                for output_connections in node_connections['main']:
                    if isinstance(output_connections, list):
                        total_branches += len(output_connections)
                        total_nodes += 1
        
        return total_branches / total_nodes if total_nodes > 0 else 0
    
    def calculate_cyclomatic_complexity(self, nodes: List[Dict], connections: Dict) -> int:
        """Calculate cyclomatic complexity (simplified)"""
        decision_nodes = 0
        
        for node in nodes:
            node_type = node.get('type', '').lower()
            if any(decision_type in node_type for decision_type in ['if', 'switch', 'condition']):
                decision_nodes += 1
        
        # Cyclomatic complexity = Decision nodes + 1
        return decision_nodes + 1
    
    def analyze_performance_patterns(self, workflow_data: Dict) -> Dict[str, Any]:
        """Analyze performance-related patterns"""
        nodes = workflow_data.get('nodes', [])
        
        performance_metrics = {
            'http_requests': 0,
            'database_operations': 0,
            'file_operations': 0,
            'api_calls': 0,
            'loops': 0,
            'error_handling': 0,
            'caching_opportunities': 0,
            'performance_score': 0
        }
        
        # Count different operation types
        for node in nodes:
            node_type = node.get('type', '').lower()
            
            if 'http' in node_type:
                performance_metrics['http_requests'] += 1
            elif any(db_type in node_type for db_type in ['database', 'mysql', 'postgres', 'sql']):
                performance_metrics['database_operations'] += 1
            elif any(file_type in node_type for file_type in ['file', 'read', 'write']):
                performance_metrics['file_operations'] += 1
            elif 'api' in node_type:
                performance_metrics['api_calls'] += 1
            elif any(loop_type in node_type for loop_type in ['loop', 'repeat', 'batch']):
                performance_metrics['loops'] += 1
            elif 'error' in node_type or 'stop' in node_type:
                performance_metrics['error_handling'] += 1
        
        # Calculate performance score (0-100)
        performance_score = 100
        
        # Deduct points for potential performance issues
        if performance_metrics['http_requests'] > 5:
            performance_score -= min(20, performance_metrics['http_requests'] * 2)
        
        if performance_metrics['database_operations'] > 3:
            performance_score -= min(15, performance_metrics['database_operations'] * 3)
        
        if performance_metrics['loops'] > 2:
            performance_score -= min(10, performance_metrics['loops'] * 4)
        
        if performance_metrics['error_handling'] == 0:
            performance_score -= 10
        
        performance_metrics['performance_score'] = max(0, performance_score)
        return performance_metrics
    
    def identify_optimization_opportunities(self, workflow_data: Dict) -> List[str]:
        """Identify specific optimization opportunities"""
        opportunities = []
        nodes = workflow_data.get('nodes', [])
        connections = workflow_data.get('connections', {})
        
        # Check for sequential HTTP requests that could be parallelized
        http_nodes = [node for node in nodes if 'http' in node.get('type', '').lower()]
        if len(http_nodes) > 1:
            opportunities.append(f"Consider parallelizing {len(http_nodes)} HTTP requests")
        
        # Check for loops that could be optimized
        loop_nodes = [node for node in nodes if any(loop_type in node.get('type', '').lower() for loop_type in ['loop', 'repeat'])]
        if loop_nodes:
            opportunities.append(f"Optimize {len(loop_nodes)} loop operations")
        
        # Check for missing error handling
        has_error_handling = any('error' in node.get('type', '').lower() for node in nodes)
        if not has_error_handling:
            opportunities.append("Add error handling for better reliability")
        
        # Check for complex workflows that could be split
        if len(nodes) > 15:
            opportunities.append("Consider splitting complex workflow into smaller, focused workflows")
        
        # Check for data transformation opportunities
        transform_nodes = [node for node in nodes if any(transform_type in node.get('type', '').lower() for transform_type in ['set', 'transform', 'function'])]
        if len(transform_nodes) > 3:
            opportunities.append("Consolidate data transformation operations")
        
        return opportunities
    
    def calculate_best_practices_score(self, workflow_data: Dict) -> int:
        """Calculate best practices compliance score"""
        score = 0
        nodes = workflow_data.get('nodes', [])
        
        # Has proper naming (10 points)
        workflow_name = workflow_data.get('name', '')
        if workflow_name and len(workflow_name) >= 5:
            score += 10
        
        # Has error handling (20 points)
        has_error_handling = any('error' in node.get('type', '').lower() for node in nodes)
        if has_error_handling:
            score += 20
        
        # Has documentation (15 points)
        has_documentation = any('documentation' in node.get('name', '').lower() for node in nodes)
        if has_documentation:
            score += 15
        
        # Reasonable complexity (25 points)
        if len(nodes) <= 20:
            score += 25
        elif len(nodes) <= 50:
            score += 15
        else:
            score += 5
        
        # Has proper settings (10 points)
        settings = workflow_data.get('settings', {})
        if settings.get('saveManualExecutions') is not None:
            score += 10
        
        # Security best practices (20 points)
        # Check if workflow uses credentials properly (simplified check)
        has_credentials = any('credentials' in node for node in nodes)
        if has_credentials:
            score += 20
        
        return min(100, score)
    
    def analyze_single_workflow(self, workflow_path: Path) -> Dict[str, Any]:
        """Analyze a single workflow comprehensively"""
        try:
            with open(workflow_path, 'r', encoding='utf-8') as f:
                workflow_data = json.load(f)
            
            workflow_name = workflow_data.get('name', workflow_path.stem)
            
            analysis = {
                'filename': workflow_path.name,
                'workflow_name': workflow_name,
                'complexity': self.analyze_workflow_complexity(workflow_data),
                'performance': self.analyze_performance_patterns(workflow_data),
                'optimization_opportunities': self.identify_optimization_opportunities(workflow_data),
                'best_practices_score': self.calculate_best_practices_score(workflow_data),
                'overall_score': 0
            }
            
            # Calculate overall score (weighted average)
            overall_score = (
                analysis['complexity']['complexity_score'] * 0.3 +
                analysis['performance']['performance_score'] * 0.3 +
                analysis['best_practices_score'] * 0.4
            )
            analysis['overall_score'] = round(overall_score, 1)
            
            return analysis
            
        except Exception as e:
            return {
                'filename': workflow_path.name,
                'workflow_name': 'Error',
                'error': str(e),
                'overall_score': 0
            }
    
    def analyze_all_workflows(self) -> Dict[str, Any]:
        """Analyze all workflows and generate comprehensive report"""
        print("📊 Analyzing workflow performance...")
        
        analysis_results = {
            'timestamp': datetime.now().isoformat(),
            'total_workflows': 0,
            'workflow_analyses': [],
            'summary_statistics': {},
            'top_performers': [],
            'optimization_candidates': [],
            'recommendations': []
        }
        
        all_scores = []
        
        for category_dir in self.workflows_dir.iterdir():
            if category_dir.is_dir():
                for workflow_file in category_dir.glob('*.json'):
                    analysis_results['total_workflows'] += 1
                    analysis = self.analyze_single_workflow(workflow_file)
                    analysis_results['workflow_analyses'].append(analysis)
                    
                    if 'overall_score' in analysis:
                        all_scores.append(analysis['overall_score'])
        
        # Calculate summary statistics
        if all_scores:
            analysis_results['summary_statistics'] = {
                'average_score': round(statistics.mean(all_scores), 1),
                'median_score': round(statistics.median(all_scores), 1),
                'min_score': min(all_scores),
                'max_score': max(all_scores),
                'score_distribution': {
                    'excellent (90-100)': len([s for s in all_scores if s >= 90]),
                    'good (80-89)': len([s for s in all_scores if 80 <= s < 90]),
                    'fair (70-79)': len([s for s in all_scores if 70 <= s < 80]),
                    'poor (<70)': len([s for s in all_scores if s < 70])
                }
            }
        
        # Find top performers
        sorted_analyses = sorted(
            [a for a in analysis_results['workflow_analyses'] if 'overall_score' in a],
            key=lambda x: x['overall_score'],
            reverse=True
        )
        analysis_results['top_performers'] = sorted_analyses[:10]
        
        # Find optimization candidates
        optimization_candidates = [
            a for a in analysis_results['workflow_analyses']
            if 'overall_score' in a and a['overall_score'] < 70
        ]
        analysis_results['optimization_candidates'] = sorted(
            optimization_candidates,
            key=lambda x: x['overall_score']
        )[:10]
        
        # Generate recommendations
        if analysis_results['summary_statistics']['average_score'] < 75:
            analysis_results['recommendations'].append("Overall workflow quality needs improvement")
        
        if analysis_results['summary_statistics']['score_distribution']['poor (<70)'] > analysis_results['total_workflows'] * 0.3:
            analysis_results['recommendations'].append("Focus on improving low-performing workflows")
        
        return analysis_results
    
    def generate_performance_report(self, analysis_results: Dict[str, Any]):
        """Generate comprehensive performance report"""
        print("\n" + "="*60)
        print("📊 WORKFLOW PERFORMANCE ANALYSIS REPORT")
        print("="*60)
        
        stats = analysis_results['summary_statistics']
        print(f"\n📈 OVERALL STATISTICS:")
        print(f"   Total Workflows: {analysis_results['total_workflows']}")
        print(f"   Average Score: {stats.get('average_score', 'N/A')}")
        print(f"   Median Score: {stats.get('median_score', 'N/A')}")
        print(f"   Score Range: {stats.get('min_score', 'N/A')} - {stats.get('max_score', 'N/A')}")
        
        if 'score_distribution' in stats:
            print(f"\n⭐ SCORE DISTRIBUTION:")
            for range_name, count in stats['score_distribution'].items():
                percentage = (count / analysis_results['total_workflows'] * 100) if analysis_results['total_workflows'] > 0 else 0
                print(f"   {range_name}: {count} workflows ({percentage:.1f}%)")
        
        print(f"\n🏆 TOP PERFORMERS:")
        for i, workflow in enumerate(analysis_results['top_performers'][:5], 1):
            print(f"   {i}. {workflow['workflow_name']} - Score: {workflow['overall_score']}")
        
        print(f"\n🔧 OPTIMIZATION CANDIDATES:")
        for i, workflow in enumerate(analysis_results['optimization_candidates'][:5], 1):
            print(f"   {i}. {workflow['workflow_name']} - Score: {workflow['overall_score']}")
        
        if analysis_results['recommendations']:
            print(f"\n💡 RECOMMENDATIONS:")
            for rec in analysis_results['recommendations']:
                print(f"   • {rec}")
        
        # Save detailed report
        with open("workflow_performance_report.json", "w") as f:
            json.dump(analysis_results, f, indent=2)
        
        print(f"\n📄 Detailed performance report saved to: workflow_performance_report.json")

def main():
    """Main performance analysis function"""
    analyzer = WorkflowPerformanceAnalyzer()
    analysis_results = analyzer.analyze_all_workflows()
    analyzer.generate_performance_report(analysis_results)
    
    print(f"\n🎉 Performance analysis complete!")

if __name__ == "__main__":
    main()
