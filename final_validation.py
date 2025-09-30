#!/usr/bin/env python3
"""
Final Validation Script for n8n Workflows
Ensure all workflows are error-free, active, and production-ready
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional, Union
from collections import defaultdict, Counter
from datetime import datetime
import concurrent.futures
import threading
from dataclasses import dataclass

@dataclass
class ValidationResult:
    """Validation result for a workflow"""
    is_valid: bool
    is_active: bool
    is_production_ready: bool
    issues: List[str]
    score: float
    category: str

class FinalValidator:
    """Final validator for n8n workflows"""

    def __init__(
        self,
        workflows_dir: Optional[Union[str, Path]] = None,
        max_workers: int = 8,
    ):
        """Create a validator bound to the repository workflows directory by default."""

        if workflows_dir is None:
            workflows_dir = Path(__file__).resolve().parent / "workflows"

        self.workflows_dir = Path(workflows_dir).expanduser().resolve()

        if not self.workflows_dir.exists():
            raise FileNotFoundError(
                f"Workflows directory not found: {self.workflows_dir}"
            )

        self.max_workers = max_workers
        self.validation_stats = defaultdict(int)
        self.thread_lock = threading.Lock()
        
    def validate_workflow(self, workflow_data: Dict) -> ValidationResult:
        """Comprehensive validation of a workflow"""
        issues = []
        score = 100.0
        
        # Basic structure validation
        if not self.validate_basic_structure(workflow_data):
            issues.append("Invalid basic structure")
            score -= 20
        
        # Node validation
        node_issues = self.validate_nodes(workflow_data)
        issues.extend(node_issues)
        score -= len(node_issues) * 5
        
        # Connection validation
        connection_issues = self.validate_connections(workflow_data)
        issues.extend(connection_issues)
        score -= len(connection_issues) * 3
        
        # Parameter validation
        parameter_issues = self.validate_parameters(workflow_data)
        issues.extend(parameter_issues)
        score -= len(parameter_issues) * 2
        
        # Security validation
        security_issues = self.validate_security(workflow_data)
        issues.extend(security_issues)
        score -= len(security_issues) * 10
        
        # Performance validation
        performance_issues = self.validate_performance(workflow_data)
        issues.extend(performance_issues)
        score -= len(performance_issues) * 3
        
        # Documentation validation
        doc_issues = self.validate_documentation(workflow_data)
        issues.extend(doc_issues)
        score -= len(doc_issues) * 2
        
        # Determine validation status
        is_valid = len(issues) == 0
        is_active = self.is_workflow_active(workflow_data)
        is_production_ready = is_valid and is_active and score >= 80
        
        # Determine category
        if score >= 95:
            category = "excellent"
        elif score >= 85:
            category = "good"
        elif score >= 70:
            category = "fair"
        else:
            category = "poor"
        
        return ValidationResult(
            is_valid=is_valid,
            is_active=is_active,
            is_production_ready=is_production_ready,
            issues=issues,
            score=max(0, score),
            category=category
        )
    
    def validate_basic_structure(self, workflow_data: Dict) -> bool:
        """Validate basic workflow structure"""
        required_fields = ['name', 'nodes', 'connections']
        
        # Check required fields
        for field in required_fields:
            if field not in workflow_data:
                return False
        
        # Check nodes is array
        if not isinstance(workflow_data['nodes'], list):
            return False
        
        # Check connections is object
        if not isinstance(workflow_data['connections'], dict):
            return False
        
        # Check workflow name
        if not workflow_data['name'] or len(workflow_data['name'].strip()) == 0:
            return False
        
        return True
    
    def validate_nodes(self, workflow_data: Dict) -> List[str]:
        """Validate all nodes in workflow"""
        issues = []
        nodes = workflow_data.get('nodes', [])
        
        if len(nodes) == 0:
            issues.append("No nodes in workflow")
            return issues
        
        node_ids = set()
        for i, node in enumerate(nodes):
            # Check required fields
            required_fields = ['id', 'name', 'type', 'position']
            for field in required_fields:
                if field not in node:
                    issues.append(f"Node {i} missing {field}")
            
            # Check node ID uniqueness
            if 'id' in node:
                if node['id'] in node_ids:
                    issues.append(f"Duplicate node ID: {node['id']}")
                node_ids.add(node['id'])
            
            # Check node type
            if 'type' in node:
                if not node['type'] or not isinstance(node['type'], str):
                    issues.append(f"Node {i} has invalid type")
            
            # Check node position
            if 'position' in node:
                if not isinstance(node['position'], list) or len(node['position']) != 2:
                    issues.append(f"Node {i} has invalid position")
        
        return issues
    
    def validate_connections(self, workflow_data: Dict) -> List[str]:
        """Validate workflow connections"""
        issues = []
        nodes = workflow_data.get('nodes', [])
        connections = workflow_data.get('connections', {})
        
        # Get valid node IDs
        valid_node_ids = {node.get('id') for node in nodes if 'id' in node}
        
        for source_id, outputs in connections.items():
            # Check source node exists
            if source_id not in valid_node_ids:
                issues.append(f"Connection from non-existent node: {source_id}")
                continue
            
            # Check output connections
            if isinstance(outputs, dict):
                for output_type, connections_list in outputs.items():
                    if isinstance(connections_list, list):
                        for connection in connections_list:
                            if isinstance(connection, list):
                                for conn in connection:
                                    if isinstance(conn, dict) and 'node' in conn:
                                        target_node_id = conn['node']
                                        if target_node_id not in valid_node_ids:
                                            issues.append(f"Connection to non-existent node: {target_node_id}")
        
        return issues
    
    def validate_parameters(self, workflow_data: Dict) -> List[str]:
        """Validate node parameters"""
        issues = []
        nodes = workflow_data.get('nodes', [])
        
        for i, node in enumerate(nodes):
            parameters = node.get('parameters', {})
            node_type = node.get('type', '')
            
            # Check for required parameters based on node type
            if 'httpRequest' in node_type.lower():
                if 'url' not in parameters or not parameters['url']:
                    issues.append(f"HTTP Request node {i} missing URL")
            
            if 'webhook' in node_type.lower():
                if 'path' not in parameters or not parameters['path']:
                    issues.append(f"Webhook node {i} missing path")
            
            if 'email' in node_type.lower():
                if 'to' not in parameters or not parameters['to']:
                    issues.append(f"Email node {i} missing recipient")
        
        return issues
    
    def validate_security(self, workflow_data: Dict) -> List[str]:
        """Validate security aspects"""
        issues = []
        
        # Check for hardcoded credentials
        hardcoded_creds = self.find_hardcoded_credentials(workflow_data)
        if hardcoded_creds:
            issues.append(f"Hardcoded credentials found: {len(hardcoded_creds)}")
        
        # Check for sensitive data
        sensitive_data = self.find_sensitive_data(workflow_data)
        if sensitive_data:
            issues.append(f"Sensitive data found: {len(sensitive_data)}")
        
        return issues
    
    def validate_performance(self, workflow_data: Dict) -> List[str]:
        """Validate performance aspects"""
        issues = []
        nodes = workflow_data.get('nodes', [])
        
        # Check for too many nodes
        if len(nodes) > 50:
            issues.append(f"Too many nodes: {len(nodes)}")
        
        # Check for execution timeout
        settings = workflow_data.get('settings', {})
        if 'executionTimeout' in settings:
            timeout = settings['executionTimeout']
            if timeout > 3600:  # 1 hour
                issues.append(f"Execution timeout too high: {timeout}")
        
        return issues
    
    def validate_documentation(self, workflow_data: Dict) -> List[str]:
        """Validate documentation"""
        issues = []
        
        # Check workflow description
        if not workflow_data.get('description'):
            issues.append("Missing workflow description")
        
        # Check for documentation nodes
        nodes = workflow_data.get('nodes', [])
        has_doc_node = any('sticky' in node.get('type', '').lower() for node in nodes)
        if not has_doc_node:
            issues.append("No documentation node found")
        
        return issues
    
    def is_workflow_active(self, workflow_data: Dict) -> bool:
        """Check if workflow is active"""
        # Check if workflow has proper settings for activation
        settings = workflow_data.get('settings', {})
        
        # Check for execution settings
        if 'executionTimeout' not in settings:
            return False
        
        # Check for proper node structure
        nodes = workflow_data.get('nodes', [])
        if len(nodes) == 0:
            return False
        
        # Check for trigger nodes
        trigger_nodes = [node for node in nodes if any(trigger in node.get('type', '').lower() 
                          for trigger in ['webhook', 'schedule', 'manual', 'cron'])]
        
        return len(trigger_nodes) > 0
    
    def find_hardcoded_credentials(self, workflow_data: Dict) -> List[str]:
        """Find hardcoded credentials"""
        credentials = []
        
        def search_credentials(obj, path=""):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    current_path = f"{path}.{key}" if path else key
                    if any(cred in key.lower() for cred in ['password', 'token', 'key', 'secret']):
                        if isinstance(value, str) and value.strip() and value != "":
                            credentials.append(f"{current_path}: {value[:20]}...")
                    search_credentials(value, current_path)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    search_credentials(item, f"{path}[{i}]")
        
        search_credentials(workflow_data)
        return credentials
    
    def find_sensitive_data(self, workflow_data: Dict) -> List[str]:
        """Find sensitive data"""
        sensitive = []
        
        def search_sensitive(obj, path=""):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    current_path = f"{path}.{key}" if path else key
                    if any(sens in key.lower() for sens in ['api_key', 'access_token', 'secret']):
                        if isinstance(value, str) and value.strip() and value != "":
                            sensitive.append(f"{current_path}: {value[:20]}...")
                    search_sensitive(value, current_path)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    search_sensitive(item, f"{path}[{i}]")
        
        search_sensitive(workflow_data)
        return sensitive
    
    def validate_single_workflow(self, workflow_path: Path) -> Dict[str, Any]:
        """Validate a single workflow"""
        try:
            with open(workflow_path, 'r', encoding='utf-8') as f:
                workflow_data = json.load(f)
            
            # Validate workflow
            validation_result = self.validate_workflow(workflow_data)
            
            # Update statistics
            with self.thread_lock:
                self.validation_stats['total_workflows'] += 1
                if validation_result.is_valid:
                    self.validation_stats['valid_workflows'] += 1
                if validation_result.is_active:
                    self.validation_stats['active_workflows'] += 1
                if validation_result.is_production_ready:
                    self.validation_stats['production_ready_workflows'] += 1
                
                self.validation_stats[f'{validation_result.category}_workflows'] += 1
            
            return {
                'filename': workflow_path.name,
                'category': workflow_path.parent.name,
                'is_valid': validation_result.is_valid,
                'is_active': validation_result.is_active,
                'is_production_ready': validation_result.is_production_ready,
                'score': validation_result.score,
                'category': validation_result.category,
                'issues': validation_result.issues,
                'success': True
            }
            
        except Exception as e:
            with self.thread_lock:
                self.validation_stats['failed_workflows'] += 1
            
            return {
                'filename': workflow_path.name,
                'category': workflow_path.parent.name,
                'error': str(e),
                'success': False
            }
    
    def validate_all_workflows(self) -> Dict[str, Any]:
        """Validate all workflows"""
        print("🔍 Starting final validation...")
        print("🎯 Target: Error-free, active, production-ready workflows")
        
        # Collect all workflow files
        workflow_files = []
        for category_dir in self.workflows_dir.iterdir():
            if category_dir.is_dir():
                for workflow_file in category_dir.glob('*.json'):
                    workflow_files.append(workflow_file)
        
        print(f"📊 Found {len(workflow_files)} workflows to validate")
        
        # Process workflows in parallel
        validation_results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_workflow = {
                executor.submit(self.validate_single_workflow, workflow_file): workflow_file 
                for workflow_file in workflow_files
            }
            
            completed = 0
            for future in concurrent.futures.as_completed(future_to_workflow):
                workflow_file = future_to_workflow[future]
                try:
                    result = future.result()
                    validation_results.append(result)
                    completed += 1
                    
                    if completed % 100 == 0:
                        print(f"🔍 Validated {completed}/{len(workflow_files)} workflows...")
                        
                except Exception as e:
                    print(f"❌ Error validating {workflow_file.name}: {e}")
                    validation_results.append({
                        'filename': workflow_file.name,
                        'category': workflow_file.parent.name,
                        'error': str(e),
                        'success': False
                    })
        
        # Calculate final statistics
        successful_validations = sum(1 for r in validation_results if r.get('success', False))
        failed_validations = len(validation_results) - successful_validations
        
        print(f"\n✅ Final validation complete!")
        print(f"📊 Processed {len(workflow_files)} workflows")
        print(f"🔍 Successfully validated {successful_validations} workflows")
        print(f"❌ Failed validations: {failed_validations}")
        
        return {
            'total_workflows': len(workflow_files),
            'successful_validations': successful_validations,
            'failed_validations': failed_validations,
            'validation_stats': dict(self.validation_stats),
            'results': validation_results
        }
    
    def generate_validation_report(self, validation_results: Dict[str, Any]):
        """Generate comprehensive validation report"""
        print("\n" + "="*80)
        print("🔍 FINAL VALIDATION REPORT")
        print("="*80)
        
        # Basic statistics
        print(f"\n📊 VALIDATION STATISTICS:")
        print(f"   Total Workflows: {validation_results['total_workflows']}")
        print(f"   Successfully Validated: {validation_results['successful_validations']}")
        print(f"   Failed Validations: {validation_results['failed_validations']}")
        print(f"   Success Rate: {validation_results['successful_validations']/validation_results['total_workflows']*100:.1f}%")
        
        # Validation statistics
        print(f"\n🔍 VALIDATION BREAKDOWN:")
        for stat_type, count in validation_results['validation_stats'].items():
            print(f"   {stat_type.replace('_', ' ').title()}: {count}")
        
        # Quality distribution
        quality_dist = defaultdict(int)
        for result in validation_results['results']:
            if result.get('success') and 'category' in result:
                quality_dist[result['category']] += 1
        
        print(f"\n🎯 QUALITY DISTRIBUTION:")
        for category, count in quality_dist.items():
            print(f"   {category.title()}: {count} workflows")
        
        # Production readiness
        production_ready = sum(1 for r in validation_results['results'] 
                             if r.get('success') and r.get('is_production_ready', False))
        active_workflows = sum(1 for r in validation_results['results'] 
                             if r.get('success') and r.get('is_active', False))
        valid_workflows = sum(1 for r in validation_results['results'] 
                            if r.get('success') and r.get('is_valid', False))
        
        print(f"\n🚀 PRODUCTION READINESS:")
        print(f"   Valid Workflows: {valid_workflows}")
        print(f"   Active Workflows: {active_workflows}")
        print(f"   Production Ready: {production_ready}")
        print(f"   Production Ready Rate: {production_ready/validation_results['successful_validations']*100:.1f}%")
        
        # Save detailed report
        report_data = {
            'validation_timestamp': datetime.now().isoformat(),
            'summary': {
                'total_workflows': validation_results['total_workflows'],
                'successful_validations': validation_results['successful_validations'],
                'failed_validations': validation_results['failed_validations'],
                'success_rate': validation_results['successful_validations']/validation_results['total_workflows']*100,
                'valid_workflows': valid_workflows,
                'active_workflows': active_workflows,
                'production_ready_workflows': production_ready
            },
            'validation_stats': validation_results['validation_stats'],
            'quality_distribution': dict(quality_dist),
            'detailed_results': validation_results['results']
        }
        
        with open("final_validation_report.json", "w") as f:
            json.dump(report_data, f, indent=2)
        
        print(f"\n📄 Comprehensive report saved to: final_validation_report.json")
        
        # Final status
        if production_ready == validation_results['successful_validations']:
            print(f"\n🎉 ALL WORKFLOWS ARE PRODUCTION-READY! 🎉")
        elif active_workflows == validation_results['successful_validations']:
            print(f"\n✅ ALL WORKFLOWS ARE ACTIVE! ✅")
        elif valid_workflows == validation_results['successful_validations']:
            print(f"\n✅ ALL WORKFLOWS ARE VALID! ✅")
        else:
            print(f"\n🔧 {validation_results['successful_validations'] - valid_workflows} workflows need attention")

def main():
    """Main final validation function"""
    print("🔍 Final Validator for n8n Workflows")
    print("🎯 Target: Error-free, active, production-ready workflows")
    print("=" * 60)
    
    validator = FinalValidator()
    
    # Run final validation
    validation_results = validator.validate_all_workflows()
    
    # Generate comprehensive report
    validator.generate_validation_report(validation_results)
    
    print(f"\n🎉 FINAL VALIDATION COMPLETE!")
    print(f"💡 Check final_validation_report.json for detailed analytics")

if __name__ == "__main__":
    main()
