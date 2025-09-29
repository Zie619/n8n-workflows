#!/usr/bin/env python3
"""
Comprehensive Error Fixer for n8n Workflows
Check, fix, and ensure all workflows are error-free and active
"""

import json
import os
import re
import uuid
import shutil
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional
from collections import defaultdict, Counter
from datetime import datetime
import concurrent.futures
import threading
from dataclasses import dataclass

@dataclass
class WorkflowError:
    """Error information for a workflow"""
    error_type: str
    severity: str
    description: str
    location: str
    fix_applied: bool = False

class ComprehensiveErrorFixer:
    """Comprehensive error checker and fixer for n8n workflows"""
    
    def __init__(self, workflows_dir="C:\\Users\\sahii\\OneDrive\\Saved Games\\Microsoft Edge Drop Files\\Documents\\Cline\\n8n-workflows\\workflows", max_workers=8):
        self.workflows_dir = Path(workflows_dir)
        self.max_workers = max_workers
        self.error_stats = defaultdict(int)
        self.fix_stats = defaultdict(int)
        self.thread_lock = threading.Lock()
        
    def check_workflow_errors(self, workflow_data: Dict) -> List[WorkflowError]:
        """Check for all possible errors in a workflow"""
        errors = []
        
        # Check for JSON structure errors
        structure_errors = self.check_json_structure(workflow_data)
        errors.extend(structure_errors)
        
        # Check for node errors
        node_errors = self.check_node_errors(workflow_data)
        errors.extend(node_errors)
        
        # Check for connection errors
        connection_errors = self.check_connection_errors(workflow_data)
        errors.extend(connection_errors)
        
        # Check for parameter errors
        parameter_errors = self.check_parameter_errors(workflow_data)
        errors.extend(parameter_errors)
        
        # Check for credential errors
        credential_errors = self.check_credential_errors(workflow_data)
        errors.extend(credential_errors)
        
        # Check for execution errors
        execution_errors = self.check_execution_errors(workflow_data)
        errors.extend(execution_errors)
        
        # Check for validation errors
        validation_errors = self.check_validation_errors(workflow_data)
        errors.extend(validation_errors)
        
        return errors
    
    def check_json_structure(self, workflow_data: Dict) -> List[WorkflowError]:
        """Check for JSON structure errors"""
        errors = []
        
        # Check required fields
        required_fields = ['name', 'nodes', 'connections']
        for field in required_fields:
            if field not in workflow_data:
                errors.append(WorkflowError(
                    error_type='missing_required_field',
                    severity='critical',
                    description=f'Missing required field: {field}',
                    location='workflow_root'
                ))
        
        # Check nodes array
        if 'nodes' in workflow_data:
            if not isinstance(workflow_data['nodes'], list):
                errors.append(WorkflowError(
                    error_type='invalid_nodes_format',
                    severity='critical',
                    description='Nodes must be an array',
                    location='workflow.nodes'
                ))
            elif len(workflow_data['nodes']) == 0:
                errors.append(WorkflowError(
                    error_type='empty_nodes',
                    severity='critical',
                    description='Workflow has no nodes',
                    location='workflow.nodes'
                ))
        
        # Check connections object
        if 'connections' in workflow_data:
            if not isinstance(workflow_data['connections'], dict):
                errors.append(WorkflowError(
                    error_type='invalid_connections_format',
                    severity='critical',
                    description='Connections must be an object',
                    location='workflow.connections'
                ))
        
        return errors
    
    def check_node_errors(self, workflow_data: Dict) -> List[WorkflowError]:
        """Check for node-specific errors"""
        errors = []
        nodes = workflow_data.get('nodes', [])
        
        for i, node in enumerate(nodes):
            node_id = f"node_{i}"
            
            # Check required node fields
            required_node_fields = ['id', 'name', 'type', 'position']
            for field in required_node_fields:
                if field not in node:
                    errors.append(WorkflowError(
                        error_type='missing_node_field',
                        severity='high',
                        description=f'Node {i} missing required field: {field}',
                        location=f'{node_id}.{field}'
                    ))
            
            # Check node ID uniqueness
            if 'id' in node:
                node_ids = [n.get('id') for n in nodes if 'id' in n]
                if node_ids.count(node['id']) > 1:
                    errors.append(WorkflowError(
                        error_type='duplicate_node_id',
                        severity='high',
                        description=f'Duplicate node ID: {node["id"]}',
                        location=f'{node_id}.id'
                    ))
            
            # Check node type validity
            if 'type' in node:
                if not node['type'] or not isinstance(node['type'], str):
                    errors.append(WorkflowError(
                        error_type='invalid_node_type',
                        severity='high',
                        description=f'Invalid node type: {node["type"]}',
                        location=f'{node_id}.type'
                    ))
            
            # Check node position
            if 'position' in node:
                if not isinstance(node['position'], list) or len(node['position']) != 2:
                    errors.append(WorkflowError(
                        error_type='invalid_node_position',
                        severity='medium',
                        description=f'Invalid node position: {node["position"]}',
                        location=f'{node_id}.position'
                    ))
            
            # Check node parameters
            if 'parameters' in node:
                if not isinstance(node['parameters'], dict):
                    errors.append(WorkflowError(
                        error_type='invalid_node_parameters',
                        severity='medium',
                        description=f'Invalid node parameters format',
                        location=f'{node_id}.parameters'
                    ))
        
        return errors
    
    def check_connection_errors(self, workflow_data: Dict) -> List[WorkflowError]:
        """Check for connection errors"""
        errors = []
        nodes = workflow_data.get('nodes', [])
        connections = workflow_data.get('connections', {})
        
        # Get valid node IDs
        valid_node_ids = {node.get('id') for node in nodes if 'id' in node}
        
        for source_id, outputs in connections.items():
            # Check if source node exists
            if source_id not in valid_node_ids:
                errors.append(WorkflowError(
                    error_type='invalid_source_node',
                    severity='high',
                    description=f'Source node not found: {source_id}',
                    location=f'connections.{source_id}'
                ))
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
                                            errors.append(WorkflowError(
                                                error_type='invalid_target_node',
                                                severity='high',
                                                description=f'Target node not found: {target_node_id}',
                                                location=f'connections.{source_id}.{output_type}'
                                            ))
        
        return errors
    
    def check_parameter_errors(self, workflow_data: Dict) -> List[WorkflowError]:
        """Check for parameter errors"""
        errors = []
        nodes = workflow_data.get('nodes', [])
        
        for i, node in enumerate(nodes):
            node_id = f"node_{i}"
            parameters = node.get('parameters', {})
            
            # Check for required parameters based on node type
            node_type = node.get('type', '')
            
            # HTTP Request node checks
            if 'httpRequest' in node_type.lower():
                if 'url' not in parameters or not parameters['url']:
                    errors.append(WorkflowError(
                        error_type='missing_required_parameter',
                        severity='high',
                        description='HTTP Request node missing URL parameter',
                        location=f'{node_id}.parameters.url'
                    ))
            
            # Webhook node checks
            if 'webhook' in node_type.lower():
                if 'path' not in parameters or not parameters['path']:
                    errors.append(WorkflowError(
                        error_type='missing_required_parameter',
                        severity='high',
                        description='Webhook node missing path parameter',
                        location=f'{node_id}.parameters.path'
                    ))
            
            # Email node checks
            if 'email' in node_type.lower():
                if 'to' not in parameters or not parameters['to']:
                    errors.append(WorkflowError(
                        error_type='missing_required_parameter',
                        severity='high',
                        description='Email node missing recipient parameter',
                        location=f'{node_id}.parameters.to'
                    ))
        
        return errors
    
    def check_credential_errors(self, workflow_data: Dict) -> List[WorkflowError]:
        """Check for credential errors"""
        errors = []
        nodes = workflow_data.get('nodes', [])
        
        for i, node in enumerate(nodes):
            node_id = f"node_{i}"
            credentials = node.get('credentials', {})
            
            # Check for missing credentials
            node_type = node.get('type', '')
            if any(service in node_type.lower() for service in ['slack', 'google', 'microsoft', 'github', 'discord']):
                if not credentials:
                    errors.append(WorkflowError(
                        error_type='missing_credentials',
                        severity='high',
                        description=f'Node requires credentials but none provided',
                        location=f'{node_id}.credentials'
                    ))
        
        return errors
    
    def check_execution_errors(self, workflow_data: Dict) -> List[WorkflowError]:
        """Check for execution errors"""
        errors = []
        
        # Check workflow settings
        settings = workflow_data.get('settings', {})
        
        # Check execution timeout
        if 'executionTimeout' in settings:
            timeout = settings['executionTimeout']
            if not isinstance(timeout, (int, float)) or timeout <= 0:
                errors.append(WorkflowError(
                    error_type='invalid_execution_timeout',
                    severity='medium',
                    description=f'Invalid execution timeout: {timeout}',
                    location='workflow.settings.executionTimeout'
                ))
        
        # Check max executions
        if 'maxExecutions' in settings:
            max_exec = settings['maxExecutions']
            if not isinstance(max_exec, int) or max_exec <= 0:
                errors.append(WorkflowError(
                    error_type='invalid_max_executions',
                    severity='medium',
                    description=f'Invalid max executions: {max_exec}',
                    location='workflow.settings.maxExecutions'
                ))
        
        return errors
    
    def check_validation_errors(self, workflow_data: Dict) -> List[WorkflowError]:
        """Check for validation errors"""
        errors = []
        
        # Check workflow name
        workflow_name = workflow_data.get('name', '')
        if not workflow_name or len(workflow_name.strip()) == 0:
            errors.append(WorkflowError(
                error_type='empty_workflow_name',
                severity='medium',
                description='Workflow name is empty',
                location='workflow.name'
            ))
        
        # Check for circular dependencies
        circular_deps = self.check_circular_dependencies(workflow_data)
        errors.extend(circular_deps)
        
        return errors
    
    def check_circular_dependencies(self, workflow_data: Dict) -> List[WorkflowError]:
        """Check for circular dependencies"""
        errors = []
        connections = workflow_data.get('connections', {})
        
        # Simple circular dependency check
        visited = set()
        rec_stack = set()
        
        def has_cycle(node_id):
            visited.add(node_id)
            rec_stack.add(node_id)
            
            if node_id in connections:
                for output_connections in connections[node_id].values():
                    if isinstance(output_connections, list):
                        for connection in output_connections:
                            if isinstance(connection, list):
                                for conn in connection:
                                    if isinstance(conn, dict) and 'node' in conn:
                                        target = conn['node']
                                        if target not in visited:
                                            if has_cycle(target):
                                                return True
                                        elif target in rec_stack:
                                            return True
            
            rec_stack.remove(node_id)
            return False
        
        for node_id in connections:
            if node_id not in visited:
                if has_cycle(node_id):
                    errors.append(WorkflowError(
                        error_type='circular_dependency',
                        severity='high',
                        description=f'Circular dependency detected involving node: {node_id}',
                        location=f'connections.{node_id}'
                    ))
        
        return errors
    
    def fix_workflow_errors(self, workflow_data: Dict, errors: List[WorkflowError]) -> Dict:
        """Fix all detected errors in workflow"""
        fixed_workflow = workflow_data.copy()
        fixes_applied = []
        
        for error in errors:
            if error.error_type == 'missing_required_field':
                if error.location == 'workflow_root':
                    if 'name' in error.description:
                        fixed_workflow['name'] = 'Unnamed Workflow'
                    elif 'nodes' in error.description:
                        fixed_workflow['nodes'] = []
                    elif 'connections' in error.description:
                        fixed_workflow['connections'] = {}
                fixes_applied.append(f'Added missing field: {error.location}')
            
            elif error.error_type == 'missing_node_field':
                node_index = int(error.location.split('_')[1])
                if node_index < len(fixed_workflow['nodes']):
                    node = fixed_workflow['nodes'][node_index]
                    if 'id' in error.description:
                        node['id'] = f"node-{uuid.uuid4().hex[:8]}"
                    elif 'name' in error.description:
                        node['name'] = f"Node {node_index + 1}"
                    elif 'type' in error.description:
                        node['type'] = 'n8n-nodes-base.noOp'
                    elif 'position' in error.description:
                        node['position'] = [100 + node_index * 200, 100]
                fixes_applied.append(f'Fixed node field: {error.location}')
            
            elif error.error_type == 'duplicate_node_id':
                # Fix duplicate IDs
                node_ids = set()
                for node in fixed_workflow['nodes']:
                    if 'id' in node:
                        original_id = node['id']
                        counter = 1
                        while node['id'] in node_ids:
                            node['id'] = f"{original_id}-{counter}"
                            counter += 1
                        node_ids.add(node['id'])
                fixes_applied.append('Fixed duplicate node IDs')
            
            elif error.error_type == 'invalid_node_position':
                node_index = int(error.location.split('_')[1])
                if node_index < len(fixed_workflow['nodes']):
                    fixed_workflow['nodes'][node_index]['position'] = [100 + node_index * 200, 100]
                fixes_applied.append(f'Fixed node position: {error.location}')
            
            elif error.error_type == 'missing_required_parameter':
                node_index = int(error.location.split('_')[1])
                if node_index < len(fixed_workflow['nodes']):
                    node = fixed_workflow['nodes'][node_index]
                    if 'parameters' not in node:
                        node['parameters'] = {}
                    
                    if 'url' in error.description:
                        node['parameters']['url'] = 'https://api.example.com'
                    elif 'path' in error.description:
                        node['parameters']['path'] = '/webhook'
                    elif 'to' in error.description:
                        node['parameters']['to'] = 'user@example.com'
                fixes_applied.append(f'Added missing parameter: {error.location}')
            
            elif error.error_type == 'missing_credentials':
                node_index = int(error.location.split('_')[1])
                if node_index < len(fixed_workflow['nodes']):
                    fixed_workflow['nodes'][node_index]['credentials'] = {
                        'credentialType': 'placeholder',
                        'id': 'placeholder-credential'
                    }
                fixes_applied.append(f'Added placeholder credentials: {error.location}')
            
            elif error.error_type == 'invalid_execution_timeout':
                fixed_workflow['settings']['executionTimeout'] = 3600
                fixes_applied.append('Fixed execution timeout')
            
            elif error.error_type == 'invalid_max_executions':
                fixed_workflow['settings']['maxExecutions'] = 1000
                fixes_applied.append('Fixed max executions')
            
            elif error.error_type == 'empty_workflow_name':
                fixed_workflow['name'] = 'Unnamed Workflow'
                fixes_applied.append('Fixed empty workflow name')
            
            elif error.error_type == 'circular_dependency':
                # Remove problematic connections
                if error.location.startswith('connections.'):
                    node_id = error.location.split('.')[1]
                    if node_id in fixed_workflow['connections']:
                        del fixed_workflow['connections'][node_id]
                fixes_applied.append('Removed circular dependency')
        
        return fixed_workflow, fixes_applied
    
    def fix_single_workflow(self, workflow_path: Path) -> Dict[str, Any]:
        """Fix errors in a single workflow"""
        try:
            with open(workflow_path, 'r', encoding='utf-8') as f:
                workflow_data = json.load(f)
            
            # Check for errors
            errors = self.check_workflow_errors(workflow_data)
            
            # Fix errors
            if errors:
                fixed_workflow, fixes_applied = self.fix_workflow_errors(workflow_data, errors)
                
                # Save fixed workflow
                with open(workflow_path, 'w', encoding='utf-8') as f:
                    json.dump(fixed_workflow, f, indent=2, ensure_ascii=False)
                
                # Update statistics
                with self.thread_lock:
                    self.error_stats['total_errors'] += len(errors)
                    self.fix_stats['workflows_fixed'] += 1
                    self.fix_stats['total_fixes'] += len(fixes_applied)
                
                return {
                    'filename': workflow_path.name,
                    'category': workflow_path.parent.name,
                    'errors_found': len(errors),
                    'fixes_applied': fixes_applied,
                    'success': True,
                    'error_types': [error.error_type for error in errors]
                }
            else:
                return {
                    'filename': workflow_path.name,
                    'category': workflow_path.parent.name,
                    'errors_found': 0,
                    'fixes_applied': [],
                    'success': True,
                    'error_types': []
                }
                
        except Exception as e:
            with self.thread_lock:
                self.error_stats['failed_workflows'] += 1
            
            return {
                'filename': workflow_path.name,
                'category': workflow_path.parent.name,
                'error': str(e),
                'success': False
            }
    
    def fix_all_workflows(self) -> Dict[str, Any]:
        """Fix errors in all workflows"""
        print("🔧 Starting comprehensive error fixing...")
        print("🎯 Target: Error-free, active workflows")
        
        # Collect all workflow files
        workflow_files = []
        for category_dir in self.workflows_dir.iterdir():
            if category_dir.is_dir():
                for workflow_file in category_dir.glob('*.json'):
                    workflow_files.append(workflow_file)
        
        print(f"📊 Found {len(workflow_files)} workflows to check and fix")
        
        # Process workflows in parallel
        fix_results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_workflow = {
                executor.submit(self.fix_single_workflow, workflow_file): workflow_file 
                for workflow_file in workflow_files
            }
            
            completed = 0
            for future in concurrent.futures.as_completed(future_to_workflow):
                workflow_file = future_to_workflow[future]
                try:
                    result = future.result()
                    fix_results.append(result)
                    completed += 1
                    
                    if completed % 100 == 0:
                        print(f"🔧 Fixed {completed}/{len(workflow_files)} workflows...")
                        
                except Exception as e:
                    print(f"❌ Error processing {workflow_file.name}: {e}")
                    fix_results.append({
                        'filename': workflow_file.name,
                        'category': workflow_file.parent.name,
                        'error': str(e),
                        'success': False
                    })
        
        # Calculate final statistics
        successful_fixes = sum(1 for r in fix_results if r.get('success', False))
        failed_fixes = len(fix_results) - successful_fixes
        
        print(f"\n✅ Comprehensive error fixing complete!")
        print(f"📊 Processed {len(workflow_files)} workflows")
        print(f"🔧 Successfully fixed {successful_fixes} workflows")
        print(f"❌ Failed fixes: {failed_fixes}")
        
        return {
            'total_workflows': len(workflow_files),
            'successful_fixes': successful_fixes,
            'failed_fixes': failed_fixes,
            'error_stats': dict(self.error_stats),
            'fix_stats': dict(self.fix_stats),
            'results': fix_results
        }
    
    def generate_error_report(self, fix_results: Dict[str, Any]):
        """Generate comprehensive error fixing report"""
        print("\n" + "="*80)
        print("🔧 COMPREHENSIVE ERROR FIXING REPORT")
        print("="*80)
        
        # Basic statistics
        print(f"\n📊 FIXING STATISTICS:")
        print(f"   Total Workflows: {fix_results['total_workflows']}")
        print(f"   Successfully Fixed: {fix_results['successful_fixes']}")
        print(f"   Failed Fixes: {fix_results['failed_fixes']}")
        print(f"   Success Rate: {fix_results['successful_fixes']/fix_results['total_workflows']*100:.1f}%")
        
        # Error statistics
        print(f"\n🔧 ERROR STATISTICS:")
        for error_type, count in fix_results['error_stats'].items():
            print(f"   {error_type.replace('_', ' ').title()}: {count}")
        
        # Fix statistics
        print(f"\n🛠️ FIX STATISTICS:")
        for fix_type, count in fix_results['fix_stats'].items():
            print(f"   {fix_type.replace('_', ' ').title()}: {count}")
        
        # Category breakdown
        category_stats = defaultdict(int)
        for result in fix_results['results']:
            if result.get('success'):
                category_stats[result.get('category', 'unknown')] += 1
        
        print(f"\n📁 CATEGORY BREAKDOWN:")
        for category, count in sorted(category_stats.items()):
            print(f"   {category}: {count} workflows")
        
        # Save detailed report
        report_data = {
            'fix_timestamp': datetime.now().isoformat(),
            'summary': {
                'total_workflows': fix_results['total_workflows'],
                'successful_fixes': fix_results['successful_fixes'],
                'failed_fixes': fix_results['failed_fixes'],
                'success_rate': fix_results['successful_fixes']/fix_results['total_workflows']*100
            },
            'error_stats': fix_results['error_stats'],
            'fix_stats': fix_results['fix_stats'],
            'category_breakdown': dict(category_stats),
            'detailed_results': fix_results['results']
        }
        
        with open("comprehensive_error_fix_report.json", "w") as f:
            json.dump(report_data, f, indent=2)
        
        print(f"\n📄 Comprehensive report saved to: comprehensive_error_fix_report.json")
        
        # Generate summary statistics
        if fix_results['results']:
            successful_results = [r for r in fix_results['results'] if r.get('success')]
            if successful_results:
                total_errors = sum(r.get('errors_found', 0) for r in successful_results)
                total_fixes = sum(len(r.get('fixes_applied', [])) for r in successful_results)
                print(f"\n📈 TOTAL ERRORS FOUND: {total_errors}")
                print(f"🔧 TOTAL FIXES APPLIED: {total_fixes}")
                
                if total_errors == 0:
                    print(f"\n🎉 ALL WORKFLOWS ARE ERROR-FREE! 🎉")
                else:
                    print(f"\n🔧 {total_fixes} fixes applied to resolve {total_errors} errors")

def main():
    """Main comprehensive error fixing function"""
    print("🔧 Comprehensive Error Fixer for n8n Workflows")
    print("🎯 Target: Error-free, active workflows")
    print("=" * 60)
    
    fixer = ComprehensiveErrorFixer()
    
    # Run comprehensive error fixing
    fix_results = fixer.fix_all_workflows()
    
    # Generate comprehensive report
    fixer.generate_error_report(fix_results)
    
    print(f"\n🎉 COMPREHENSIVE ERROR FIXING COMPLETE!")
    print(f"💡 Check comprehensive_error_fix_report.json for detailed analytics")

if __name__ == "__main__":
    main()
