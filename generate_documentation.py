#!/usr/bin/env python3
"""
N8N Workflow Documentation Generator

This script analyzes n8n workflow JSON files and generates a comprehensive HTML documentation page.
It performs static analysis of the workflow files to extract metadata, categorize workflows,
and create an interactive documentation interface.

Usage: python generate_documentation.py
"""

import json
import os
import glob
import datetime
from typing import Dict, List, Any, Optional, Tuple, Set

# Constants
DEFAULT_WORKFLOWS_DIR = "workflows"


class WorkflowAnalyzer:
    """Analyzes n8n workflow JSON files and generates documentation data."""
    
    def __init__(self, workflows_dir: str = DEFAULT_WORKFLOWS_DIR):
        self.workflows_dir = workflows_dir
        self.workflows = []
        self.stats = {
            'total': 0,
            'active': 0,
            'inactive': 0,
            'triggers': {},
            'complexity': {'low': 0, 'medium': 0, 'high': 0},
            'total_nodes': 0,
            'integrations': set()
        }
    
    def analyze_all_workflows(self) -> Dict[str, Any]:
        """Analyze all workflow files and return comprehensive data."""
        if not os.path.exists(self.workflows_dir):
            print(f"Warning: Workflows directory '{self.workflows_dir}' not found.")
            return self._get_empty_data()
        
        json_files = glob.glob(os.path.join(self.workflows_dir, "*.json"))
        
        if not json_files:
            print(f"Warning: No JSON files found in '{self.workflows_dir}' directory.")
            return self._get_empty_data()
        
        print(f"Found {len(json_files)} workflow files. Analyzing...")
        
        for file_path in json_files:
            try:
                workflow_data = self._analyze_workflow_file(file_path)
                if workflow_data:
                    self.workflows.append(workflow_data)
            except Exception as e:
                print(f"Error analyzing {file_path}: {str(e)}")
                continue
        
        self._calculate_stats()
        
        return {
            'workflows': self.workflows,
            'stats': self.stats,
            'timestamp': datetime.datetime.now().isoformat()
        }
    
    def _analyze_workflow_file(self, file_path: str) -> Optional[Dict[str, Any]]:
        """Analyze a single workflow file and extract metadata."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print(f"Error reading {file_path}: {str(e)}")
            return None
        
        filename = os.path.basename(file_path)
        
        # Extract basic metadata
        workflow = {
            'filename': filename,
            'name': data.get('name', filename.replace('.json', '')),
            'id': data.get('id', 'unknown'),
            'active': data.get('active', False),
            'nodes': data.get('nodes', []),
            'connections': data.get('connections', {}),
            'tags': data.get('tags', []),
            'settings': data.get('settings', {}),
            'createdAt': data.get('createdAt', ''),
            'updatedAt': data.get('updatedAt', ''),
            'versionId': data.get('versionId', '')
        }
        
        # Analyze nodes
        node_count = len(workflow['nodes'])
        workflow['nodeCount'] = node_count
        
        # Determine complexity
        if node_count <= 5:
            complexity = 'low'
        elif node_count <= 15:
            complexity = 'medium'
        else:
            complexity = 'high'
        workflow['complexity'] = complexity
        
        # Find trigger type and integrations
        trigger_type, integrations = self._analyze_nodes(workflow['nodes'])
        workflow['triggerType'] = trigger_type
        workflow['integrations'] = list(integrations)
        
        # Generate description
        workflow['description'] = self._generate_description(workflow, trigger_type, integrations)
        
        # Extract or generate step-by-step process
        steps = self._extract_or_generate_steps(workflow['nodes'], workflow['connections'])
        workflow['steps'] = steps
        
        # Debug logging
        if steps:
            print(f"Found/Generated {len(steps)} steps in workflow: {workflow['name']}")
        
        # Extract raw JSON for viewer
        workflow['rawJson'] = json.dumps(data, indent=2)
        
        return workflow
    
    def _analyze_nodes(self, nodes: List[Dict]) -> Tuple[str, Set[str]]:
        """Analyze nodes to determine trigger type and integrations."""
        trigger_type = 'Manual'
        integrations = set()
        
        for node in nodes:
            node_type = node.get('type', '')
            node_name = node.get('name', '')
            
            # Determine trigger type
            if 'webhook' in node_type.lower() or 'webhook' in node_name.lower():
                trigger_type = 'Webhook'
            elif 'cron' in node_type.lower() or 'schedule' in node_type.lower():
                trigger_type = 'Scheduled'
            elif 'trigger' in node_type.lower() and trigger_type == 'Manual':
                if 'manual' not in node_type.lower():
                    trigger_type = 'Webhook'  # Most non-manual triggers are webhook-based
            
            # Extract integrations
            if node_type.startswith('n8n-nodes-base.'):
                service = node_type.replace('n8n-nodes-base.', '')
                # Clean up service names
                service = service.replace('Trigger', '').replace('trigger', '')
                if service and service not in ['set', 'function', 'if', 'switch', 'merge', 'stickyNote']:
                    integrations.add(service.title())
        
        # Determine if complex based on node variety and count
        if len(nodes) > 10 and len(integrations) > 3:
            trigger_type = 'Complex'
        
        return trigger_type, integrations
    
    def _generate_description(self, workflow: Dict, trigger_type: str, integrations: Set[str]) -> str:
        """Generate a descriptive summary of the workflow."""
        name = workflow['name']
        node_count = workflow['nodeCount']
        
        # Start with trigger description
        trigger_descriptions = {
            'Webhook': "Webhook-triggered automation that",
            'Scheduled': "Scheduled automation that", 
            'Complex': "Complex multi-step automation that",
        }
        desc = trigger_descriptions.get(trigger_type, "Manual workflow that")
        
        # Add functionality based on name and integrations
        if integrations:
            main_services = list(integrations)[:3]  # Top 3 services
            if len(main_services) == 1:
                desc += f" integrates with {main_services[0]}"
            elif len(main_services) == 2:
                desc += f" connects {main_services[0]} and {main_services[1]}"
            else:
                desc += f" orchestrates {', '.join(main_services[:-1])}, and {main_services[-1]}"
        
        # Add workflow purpose hints from name
        name_lower = name.lower()
        if 'create' in name_lower:
            desc += " to create new records"
        elif 'update' in name_lower:
            desc += " to update existing data"
        elif 'sync' in name_lower:
            desc += " to synchronize data"
        elif 'notification' in name_lower or 'alert' in name_lower:
            desc += " for notifications and alerts"
        elif 'backup' in name_lower:
            desc += " for data backup operations"
        elif 'monitor' in name_lower:
            desc += " for monitoring and reporting"
        else:
            desc += " for data processing"
        
        desc += f". Uses {node_count} nodes"
        if len(integrations) > 3:
            desc += f" and integrates with {len(integrations)} services"
        
        desc += "."
        
        return desc
    
    def _extract_or_generate_steps(self, nodes: List[Dict], connections: Dict) -> List[Dict]:
        """Extract notes from nodes or generate steps from workflow structure."""
        steps = []
        
        # First, try to extract existing notes
        nodes_with_notes = []
        for node in nodes:
            note = node.get('notes')
            if note:
                nodes_with_notes.append({
                    'name': node.get('name', ''),
                    'type': node.get('type', ''),
                    'note': note,
                    'id': node.get('id', '')
                })
        
        # If we have notes, use them
        if nodes_with_notes:
            return nodes_with_notes
        
        # Otherwise, generate steps from workflow structure
        return self._generate_steps_from_structure(nodes, connections)
    
    def _generate_steps_from_structure(self, nodes: List[Dict], connections: Dict) -> List[Dict]:
        """Generate step descriptions from workflow node structure and connections."""
        if not nodes:
            return []
        
        # Create a map of nodes by ID for easy lookup
        node_map = {node.get('id', ''): node for node in nodes}
        
        # Find the starting node (trigger or first node)
        start_node = self._find_start_node(nodes, connections)
        if not start_node:
            # Fallback: just describe all nodes in order
            return self._generate_basic_steps(nodes)
        
        # Follow the workflow path
        steps = []
        visited = set()
        self._traverse_workflow(start_node, node_map, connections, steps, visited)
        
        return steps
    
    def _find_start_node(self, nodes: List[Dict], connections: Dict) -> Optional[Dict]:
        """Find the starting node of the workflow (trigger or node with no inputs)."""
        # Look for trigger nodes first
        for node in nodes:
            node_type = node.get('type', '').lower()
            if any(trigger in node_type for trigger in ['trigger', 'webhook', 'cron', 'schedule', 'manual']):
                return node
        
        # Find nodes that are not targets of any connections
        target_nodes = set()
        for source_connections in connections.values():
            if isinstance(source_connections, dict) and 'main' in source_connections:
                for main_connections in source_connections['main']:
                    if isinstance(main_connections, list):
                        for connection in main_connections:
                            if isinstance(connection, dict) and 'node' in connection:
                                target_nodes.add(connection['node'])
        
        # Return first node that's not a target
        for node in nodes:
            if node.get('name', '') not in target_nodes:
                return node
        
        # Fallback: return first node
        return nodes[0] if nodes else None
    
    def _traverse_workflow(self, current_node: Dict, node_map: Dict, connections: Dict, steps: List[Dict], visited: set):
        """Traverse the workflow following connections and generate step descriptions."""
        node_name = current_node.get('name', '')
        node_id = current_node.get('id', '')
        
        if node_id in visited:
            return
        
        visited.add(node_id)
        
        # Generate step description for current node
        step_description = self._generate_step_description(current_node)
        if step_description:
            steps.append({
                'name': node_name,
                'type': current_node.get('type', ''),
                'note': step_description,
                'id': node_id
            })
        
        # Find next nodes
        if node_name in connections:
            node_connections = connections[node_name]
            if isinstance(node_connections, dict) and 'main' in node_connections:
                for main_connections in node_connections['main']:
                    if isinstance(main_connections, list):
                        for connection in main_connections:
                            if isinstance(connection, dict) and 'node' in connection:
                                next_node_name = connection['node']
                                next_node = None
                                for node in node_map.values():
                                    if node.get('name') == next_node_name:
                                        next_node = node
                                        break
                                if next_node:
                                    self._traverse_workflow(next_node, node_map, connections, steps, visited)
    
    def _generate_step_description(self, node: Dict) -> str:
        """Generate a meaningful description for a workflow node based on its type and parameters."""
        node_type = node.get('type', '')
        node_name = node.get('name', '')
        parameters = node.get('parameters', {})
        
        # Clean up node type
        clean_type = node_type.replace('n8n-nodes-base.', '').replace('Trigger', '').replace('trigger', '')
        
        # Generate description based on node type
        if 'webhook' in node_type.lower():
            return f"Receives incoming webhook requests to trigger the workflow"
        elif 'cron' in node_type.lower() or 'schedule' in node_type.lower():
            return f"Runs on a scheduled basis to trigger the workflow automatically"
        elif 'manual' in node_type.lower():
            return f"Manual trigger to start the workflow execution"
        elif 'http' in node_type.lower() or 'httpRequest' in node_type:
            url = parameters.get('url', '')
            method = parameters.get('method', 'GET')
            return f"Makes {method} HTTP request" + (f" to {url}" if url else "")
        elif 'set' in node_type.lower():
            return f"Sets and transforms data values for use in subsequent steps"
        elif 'if' in node_type.lower():
            return f"Evaluates conditions to determine workflow path"
        elif 'switch' in node_type.lower():
            return f"Routes workflow execution based on multiple conditions"
        elif 'function' in node_type.lower() or 'code' in node_type.lower():
            return f"Executes custom JavaScript code for data processing"
        elif 'merge' in node_type.lower():
            return f"Combines data from multiple workflow branches"
        elif 'split' in node_type.lower():
            return f"Splits data into multiple items for parallel processing"
        elif 'filter' in node_type.lower():
            return f"Filters data based on specified conditions"
        elif 'gmail' in node_type.lower():
            operation = parameters.get('operation', 'send')
            return f"Performs Gmail {operation} operation"
        elif 'slack' in node_type.lower():
            return f"Sends message or performs action in Slack"
        elif 'discord' in node_type.lower():
            return f"Sends message or performs action in Discord"
        elif 'telegram' in node_type.lower():
            return f"Sends message or performs action in Telegram"
        elif 'airtable' in node_type.lower():
            operation = parameters.get('operation', 'create')
            return f"Performs Airtable {operation} operation on records"
        elif 'google' in node_type.lower():
            if 'sheets' in node_type.lower():
                return f"Reads from or writes to Google Sheets"
            elif 'drive' in node_type.lower():
                return f"Manages files in Google Drive"
            elif 'calendar' in node_type.lower():
                return f"Manages Google Calendar events"
            else:
                return f"Integrates with Google {clean_type} service"
        elif 'microsoft' in node_type.lower():
            if 'outlook' in node_type.lower():
                return f"Manages Microsoft Outlook emails"
            elif 'excel' in node_type.lower():
                return f"Works with Microsoft Excel files"
            else:
                return f"Integrates with Microsoft {clean_type} service"
        elif 'openai' in node_type.lower():
            return f"Processes data using OpenAI AI models"
        elif 'anthropic' in node_type.lower():
            return f"Processes data using Anthropic Claude AI"
        elif 'database' in node_type.lower() or 'mysql' in node_type.lower() or 'postgres' in node_type.lower():
            return f"Executes database operations"
        elif 'wait' in node_type.lower():
            return f"Pauses workflow execution for specified duration"
        elif 'error' in node_type.lower():
            return f"Handles errors and stops workflow execution"
        else:
            # Generic description based on service name
            service_name = clean_type.title()
            return f"Integrates with {service_name} to process data"
    
    def _generate_basic_steps(self, nodes: List[Dict]) -> List[Dict]:
        """Generate basic steps when workflow structure is unclear."""
        steps = []
        for i, node in enumerate(nodes, 1):
            description = self._generate_step_description(node)
            if description:
                steps.append({
                    'name': node.get('name', f'Step {i}'),
                    'type': node.get('type', ''),
                    'note': description,
                    'id': node.get('id', '')
                })
        return steps
    
    def _calculate_stats(self):
        """Calculate statistics from analyzed workflows."""
        self.stats['total'] = len(self.workflows)
        
        for workflow in self.workflows:
            # Active/inactive count
            if workflow['active']:
                self.stats['active'] += 1
            else:
                self.stats['inactive'] += 1
            
            # Trigger type count
            trigger = workflow['triggerType']
            self.stats['triggers'][trigger] = self.stats['triggers'].get(trigger, 0) + 1
            
            # Complexity count
            complexity = workflow['complexity']
            self.stats['complexity'][complexity] += 1
            
            # Node count
            self.stats['total_nodes'] += workflow['nodeCount']
            
            # Integrations
            self.stats['integrations'].update(workflow['integrations'])
        
        # Convert integrations set to count
        self.stats['unique_integrations'] = len(self.stats['integrations'])
        self.stats['integrations'] = list(self.stats['integrations'])
    
    def _get_empty_data(self) -> Dict[str, Any]:
        """Return empty data structure when no workflows found."""
        return {
            'workflows': [],
            'stats': {
                'total': 0,
                'active': 0,
                'inactive': 0,
                'triggers': {},
                'complexity': {'low': 0, 'medium': 0, 'high': 0},
                'total_nodes': 0,
                'unique_integrations': 0,
                'integrations': []
            },
            'timestamp': datetime.datetime.now().isoformat()
        }


def generate_html_documentation(data: Dict[str, Any]) -> str:
    """Generate the complete HTML documentation with embedded data."""
    
    # Convert Python data to JavaScript with proper escaping
    js_data = json.dumps(data, indent=2, ensure_ascii=False)
    # Escape any script tags and HTML entities in the JSON data
    js_data = js_data.replace('</script>', '<\\/script>').replace('<!--', '<\\!--')
    
    html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>N8N Workflow Documentation</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary-color: #4a5568;
            --secondary-color: #6b7280;
            --accent-color: #5b77a3;
            --light-bg: #f8fafc;
            --dark-bg: #1e293b;
            --card-bg: #ffffff;
            --card-bg-dark: #334155;
            --text-primary: #1a202c;
            --text-secondary: #4a5568;
            --text-muted: #718096;
            --text-light: #ffffff;
            --border-color: #e2e8f0;
            --border-color-dark: #475569;
            --success-color: #059669;
            --warning-color: #d97706;
            --error-color: #dc2626;
            --info-color: #0ea5e9;
            --surface-hover: #f1f5f9;
            --surface-hover-dark: #475569;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--light-bg);
            color: var(--text-primary);
            min-height: 100vh;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        .dark-mode {
            background: var(--dark-bg);
            color: var(--text-light);
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            margin-bottom: 40px;
            background: var(--card-bg);
            border-radius: 16px;
            padding: 40px 30px;
            border: 1px solid var(--border-color);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }

        .dark-mode .header {
            background: var(--card-bg-dark);
            border-color: var(--border-color-dark);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2);
        }

        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            color: var(--primary-color);
            font-weight: 700;
        }

        .header .subtitle {
            color: var(--text-secondary);
            font-size: 1.1rem;
            margin-bottom: 20px;
        }

        .dark-mode .header .subtitle {
            color: var(--text-muted);
        }

        .header .timestamp {
            font-size: 0.9rem;
            color: var(--text-muted);
        }

        .controls {
            display: flex;
            gap: 20px;
            margin-bottom: 30px;
            flex-wrap: wrap;
            align-items: center;
        }

        .search-container {
            flex: 1;
            min-width: 300px;
            position: relative;
        }

        .search-input {
            width: 100%;
            padding: 12px 45px 12px 20px;
            border: 2px solid var(--border-color);
            border-radius: 12px;
            background: var(--card-bg);
            color: var(--text-primary);
            font-size: 16px;
            transition: all 0.3s ease;
        }

        .dark-mode .search-input {
            border-color: var(--border-color-dark);
            background: var(--card-bg-dark);
            color: var(--text-light);
        }

        .search-input:focus {
            outline: none;
            border-color: var(--accent-color);
            box-shadow: 0 0 0 3px rgba(91, 119, 163, 0.1);
        }

        .search-input::placeholder {
            color: var(--text-muted);
        }

        .search-icon {
            position: absolute;
            right: 15px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
        }

        .filter-buttons {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .filter-btn {
            padding: 8px 16px;
            border: 2px solid var(--border-color);
            border-radius: 8px;
            background: var(--card-bg);
            color: var(--text-secondary);
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 14px;
            font-weight: 500;
        }

        .dark-mode .filter-btn {
            border-color: var(--border-color-dark);
            background: var(--card-bg-dark);
            color: var(--text-light);
        }

        .filter-btn:hover {
            background: var(--surface-hover);
            border-color: var(--accent-color);
        }

        .dark-mode .filter-btn:hover {
            background: var(--surface-hover-dark);
        }

        .filter-btn.active {
            background: var(--accent-color);
            border-color: var(--accent-color);
            color: white;
            box-shadow: 0 2px 4px rgba(91, 119, 163, 0.2);
        }

        .theme-toggle {
            padding: 10px 20px;
            border: 2px solid var(--border-color);
            border-radius: 8px;
            background: var(--card-bg);
            color: var(--text-secondary);
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 500;
        }

        .dark-mode .theme-toggle {
            border-color: var(--border-color-dark);
            background: var(--card-bg-dark);
            color: var(--text-light);
        }

        .theme-toggle:hover {
            background: var(--surface-hover);
            border-color: var(--accent-color);
        }

        .dark-mode .theme-toggle:hover {
            background: var(--surface-hover-dark);
        }

        .stats-dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .stat-card {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 24px 20px;
            text-align: center;
            border: 1px solid var(--border-color);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }

        .dark-mode .stat-card {
            background: var(--card-bg-dark);
            border-color: var(--border-color-dark);
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }

        .stat-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .dark-mode .stat-card:hover {
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }

        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: var(--accent-color);
            margin-bottom: 5px;
        }

        .stat-label {
            color: var(--text-muted);
            font-size: 0.9rem;
            font-weight: 500;
        }

        .workflow-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
            gap: 25px;
            overflow: visible;
        }

        .workflow-card {
            background: var(--card-bg);
            border-radius: 12px;
            border: 1px solid var(--border-color);
            overflow: visible;
            transition: all 0.3s ease;
            cursor: pointer;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }

        .dark-mode .workflow-card {
            background: var(--card-bg-dark);
            border-color: var(--border-color-dark);
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }

        .workflow-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
            border-color: var(--accent-color);
        }

        .dark-mode .workflow-card:hover {
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
        }

        .workflow-header {
            padding: 20px;
            border-bottom: 1px solid var(--border-color);
        }

        .dark-mode .workflow-header {
            border-bottom-color: var(--border-color-dark);
        }

        .workflow-title {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 8px;
            color: var(--text-primary);
        }

        .dark-mode .workflow-title {
            color: var(--text-light);
        }

        .workflow-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 10px;
        }

        .workflow-info {
            display: flex;
            align-items: center;
            gap: 15px;
            flex-wrap: wrap;
        }

        .status-indicator {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            margin-right: 8px;
            cursor: help;
            position: relative;
        }

        .status-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            position: relative;
            flex-shrink: 0;
            display: inline-block;
        }

        .status-active {
            background-color: var(--success-color);
            box-shadow: 0 0 0 2px rgba(5, 150, 105, 0.2);
            animation: pulse-green 2s infinite;
        }

        .status-inactive {
            background-color: var(--text-muted);
            box-shadow: 0 0 0 2px rgba(113, 128, 150, 0.2);
        }

        .status-text {
            font-size: 0.8rem;
            color: var(--text-muted);
            font-weight: 500;
        }

        .complexity-indicator {
            display: inline-block;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            margin-right: 4px;
        }

        .complexity-low {
            background-color: var(--success-color);
        }

        .complexity-medium {
            background-color: var(--warning-color);
        }

        .complexity-high {
            background-color: var(--error-color);
        }

        .workflow-stats {
            display: flex;
            gap: 15px;
            font-size: 0.85rem;
            color: var(--text-muted);
        }

        .workflow-description {
            color: var(--text-secondary);
            font-size: 0.9rem;
            line-height: 1.4;
            margin-bottom: 0;
        }

        .workflow-integrations {
            margin-top: 15px;
            padding-top: 15px;
            border-top: 1px solid var(--border-color);
        }

        .dark-mode .workflow-integrations {
            border-top-color: var(--border-color-dark);
        }

        .integrations-title {
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--text-secondary);
            margin: 0 0 8px 0;
        }

        .integrations-list {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }

        .integration-tag {
            background: var(--secondary-color);
            color: white;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
        }

        .workflow-footer {
            padding: 15px 20px;
            background: var(--surface-hover);
            border-radius: 0 0 12px 12px;
            display: flex;
            justify-content: flex-end;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
        }

        .dark-mode .workflow-footer {
            background: var(--surface-hover-dark);
        }

        .workflow-tags {
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }

        .tag {
            background: var(--accent-color);
            color: white;
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 500;
        }

        .trigger-badge {
            background: var(--info-color);
            color: white;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 500;
        }

        .action-buttons {
            display: flex;
            gap: 8px;
        }

        .btn {
            padding: 6px 12px;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            background: var(--card-bg);
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 0.8rem;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .dark-mode .btn {
            border-color: var(--border-color-dark);
            background: var(--card-bg-dark);
            color: var(--text-light);
        }

        .btn:hover {
            background: var(--accent-color);
            color: white;
            border-color: var(--accent-color);
        }

        .expanded .workflow-details {
            display: block;
        }

        .workflow-details {
            display: none;
            padding: 20px;
            border-top: 1px solid var(--border-color);
            background: var(--light-bg);
        }

        .dark-mode .workflow-details {
            border-top-color: var(--border-color-dark);
            background: var(--dark-bg);
        }

        .details-section {
            margin-bottom: 20px;
        }

        .details-title {
            font-weight: 600;
            margin-bottom: 10px;
            color: var(--text-primary);
        }

        .dark-mode .details-title {
            color: var(--text-light);
        }

        .workflow-steps {
            list-style: none;
            counter-reset: step-counter;
            padding-left: 0;
        }

        .workflow-step {
            counter-increment: step-counter;
            margin-bottom: 15px;
            padding: 12px;
            background: var(--surface-hover);
            border-radius: 8px;
            border-left: 3px solid var(--accent-color);
            position: relative;
        }

        .dark-mode .workflow-step {
            background: var(--surface-hover-dark);
        }

        .workflow-step::before {
            content: counter(step-counter);
            position: absolute;
            left: -15px;
            top: 12px;
            background: var(--accent-color);
            color: white;
            width: 24px;
            height: 24px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
            font-weight: bold;
        }

        .step-header {
            margin-bottom: 6px;
        }

        .step-type {
            color: var(--text-muted);
            font-size: 0.85rem;
            font-weight: normal;
            margin-left: 8px;
        }

        .step-note {
            color: var(--text-secondary);
            line-height: 1.4;
            white-space: pre-wrap;
        }

        .dark-mode .step-note {
            color: var(--text-muted);
        }

        .workflow-howitworks {
            color: var(--text-secondary);
            line-height: 1.5;
            padding: 10px 0;
        }

        .dark-mode .workflow-howitworks {
            color: var(--text-muted);
        }

        @keyframes pulse-green {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0.5;
            }
        }

        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(4px);
        }

        .modal-content {
            background-color: var(--card-bg);
            margin: 2% auto;
            padding: 0;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            width: 95%;
            max-width: 1200px;
            height: 90vh;
            display: flex;
            flex-direction: column;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }

        .dark-mode .modal-content {
            background-color: var(--card-bg-dark);
            border-color: var(--border-color-dark);
        }

        .modal-header {
            padding: 20px 24px;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: var(--surface-hover);
            border-radius: 12px 12px 0 0;
        }

        .dark-mode .modal-header {
            background: var(--surface-hover-dark);
            border-bottom-color: var(--border-color-dark);
        }

        .modal-title {
            font-size: 1.2rem;
            font-weight: 600;
            color: var(--text-primary);
            margin: 0;
        }

        .dark-mode .modal-title {
            color: var(--text-light);
        }

        .close-btn {
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: var(--text-muted);
            padding: 4px 8px;
            border-radius: 4px;
            transition: all 0.3s ease;
        }

        .close-btn:hover {
            background: rgba(0, 0, 0, 0.1);
            color: var(--text-primary);
        }

        .dark-mode .close-btn:hover {
            background: rgba(255, 255, 255, 0.1);
            color: var(--text-light);
        }

        .modal-body {
            flex: 1;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        .json-viewer {
            flex: 1;
            overflow: auto;
            padding: 20px;
            margin: 0;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            font-size: 0.9rem;
            line-height: 1.5;
            background: var(--light-bg);
            border: none;
            resize: none;
            white-space: pre;
            color: var(--text-primary);
            min-height: 0;
        }

        .dark-mode .json-viewer {
            background: var(--dark-bg);
            color: var(--text-light);
        }

        .legend-section {
            margin-bottom: 30px;
            padding: 20px;
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
        }

        .dark-mode .legend-section {
            background: var(--card-bg-dark);
            border-color: var(--border-color-dark);
        }

        .legend-title {
            margin-bottom: 15px;
            color: var(--text-primary);
            font-size: 1rem;
            font-weight: 600;
        }

        .dark-mode .legend-title {
            color: var(--text-light);
        }

        .legend-grid {
            display: flex;
            gap: 30px;
            flex-wrap: wrap;
            align-items: center;
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .legend-text {
            font-size: 0.9rem;
            color: var(--text-secondary);
        }

        .dark-mode .legend-text {
            color: var(--text-muted);
        }

        /* Utility classes for common patterns */
        .border-radius-md {
            border-radius: 12px;
        }

        .border-radius-sm {
            border-radius: 8px;
        }

        .padding-20 {
            padding: 20px;
        }

        .margin-bottom-20 {
            margin-bottom: 20px;
        }

        .margin-bottom-30 {
            margin-bottom: 30px;
        }

        .card-bg {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
        }

        .dark-mode .card-bg {
            background: var(--card-bg-dark);
            border-color: var(--border-color-dark);
        }

        .shadow-sm {
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }

        .dark-mode .shadow-sm {
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }

        .shadow-md {
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }

        .dark-mode .shadow-md {
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2);
        }

        .modal-footer {
            padding: 16px 24px;
            border-top: 1px solid var(--border-color);
            display: flex;
            justify-content: flex-end;
            gap: 12px;
            background: var(--surface-hover);
            border-radius: 0 0 12px 12px;
        }

        .dark-mode .modal-footer {
            border-top-color: var(--border-color-dark);
            background: var(--surface-hover-dark);
        }

        .loading {
            text-align: center;
            padding: 60px 20px;
            color: var(--text-muted);
            font-size: 1.1rem;
        }

        .no-results {
            text-align: center;
            padding: 60px 20px;
            color: var(--text-muted);
        }

        .no-results h3 {
            margin-bottom: 10px;
            color: var(--text-secondary);
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .container {
                padding: 15px;
            }

            .header {
                padding: 30px 20px;
            }

            .header h1 {
                font-size: 2rem;
            }

            .controls {
                flex-direction: column;
                align-items: stretch;
            }

            .workflow-grid {
                grid-template-columns: 1fr;
            }

            .workflow-meta {
                flex-direction: column;
                align-items: flex-start;
            }

            .modal-content {
                width: 98%;
                height: 95vh;
                margin: 1% auto;
            }

            .legend-grid {
                gap: 15px;
            }

            .legend-item {
                flex-basis: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 N8N Workflow Documentation</h1>
            <p class="subtitle">Comprehensive analysis and documentation of automated workflows</p>
            <p class="timestamp" id="generatedTimestamp">Generated: Loading...</p>
        </div>

        <div class="controls">
            <div class="search-container">
                <input type="text" id="searchInput" class="search-input" placeholder="Search workflows by name, description, or integration...">
                <span class="search-icon">🔍</span>
            </div>
            <div class="filter-buttons">
                <button class="filter-btn active" data-filter="all">All</button>
                <button class="filter-btn" data-filter="Webhook">Webhook</button>
                <button class="filter-btn" data-filter="Scheduled">Scheduled</button>
                <button class="filter-btn" data-filter="Manual">Manual</button>
                <button class="filter-btn" data-filter="Complex">Complex</button>
            </div>
            <button class="theme-toggle" id="themeToggle">🌙 Dark</button>
        </div>

        <div class="stats-dashboard">
            <div class="stat-card">
                <div class="stat-number" id="totalWorkflows">0</div>
                <div class="stat-label">Total Workflows</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="activeWorkflows">0</div>
                <div class="stat-label">Active Workflows</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="inactiveWorkflows">0</div>
                <div class="stat-label">Inactive Workflows</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="totalNodes">0</div>
                <div class="stat-label">Total Nodes</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="uniqueIntegrations">0</div>
                <div class="stat-label">Unique Integrations</div>
            </div>
        </div>

        <div class="legend-section">
            <h3 class="legend-title">Status Indicators</h3>
            <div class="legend-grid">
                <div class="legend-item">
                    <div class="status-dot status-active"></div>
                    <span class="legend-text">Active - Workflow will execute when triggered</span>
                </div>
                <div class="legend-item">
                    <div class="status-dot status-inactive"></div>
                    <span class="legend-text">Inactive - Workflow is disabled</span>
                </div>
                <div class="legend-item">
                    <div class="complexity-indicator complexity-low"></div>
                    <span class="legend-text">Low Complexity (≤5 nodes)</span>
                </div>
                <div class="legend-item">
                    <div class="complexity-indicator complexity-medium"></div>
                    <span class="legend-text">Medium Complexity (6-15 nodes)</span>
                </div>
                <div class="legend-item">
                    <div class="complexity-indicator complexity-high"></div>
                    <span class="legend-text">High Complexity (16+ nodes)</span>
                </div>
            </div>
        </div>

        <div class="loading" id="loadingIndicator">
            <p>📊 Analyzing workflows...</p>
        </div>

        <div class="workflow-grid" id="workflowGrid" style="display: none;">
            <!-- Workflow cards will be generated here -->
        </div>

        <div class="no-results" id="noResults" style="display: none;">
            <h3>No workflows found</h3>
            <p>Try adjusting your search terms or filters</p>
        </div>
    </div>

    <!-- JSON Viewer Modal -->
    <div id="jsonModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h2 class="modal-title" id="modalTitle">Workflow JSON</h2>
                <button class="close-btn" id="closeModal">&times;</button>
            </div>
            <div class="modal-body">
                <textarea class="json-viewer" id="jsonViewer" readonly></textarea>
            </div>
            <div class="modal-footer">
                <button class="btn" id="copyJson">📋 Copy</button>
                <button class="btn" id="downloadJson">💾 Download</button>
            </div>
        </div>
    </div>

    <script>
        // Embedded workflow data from Python analysis
        const WORKFLOW_DATA = ''' + js_data + ''';

        class WorkflowDocumentation {
            constructor() {
                this.workflows = WORKFLOW_DATA.workflows || [];
                this.stats = WORKFLOW_DATA.stats || {};
                this.filteredWorkflows = this.workflows;
                this.currentFilter = 'all';
                this.currentSearch = '';
                
                this.init();
            }

            init() {
                this.renderStats();
                this.renderWorkflows();
                this.setupEventListeners();
                this.hideLoading();
                this.updateTimestamp();
            }

            updateTimestamp() {
                const timestamp = WORKFLOW_DATA.timestamp || new Date().toISOString();
                const date = new Date(timestamp);
                document.getElementById('generatedTimestamp').textContent = 
                    `Generated: ${date.toLocaleDateString()} at ${date.toLocaleTimeString()}`;
            }

            renderStats() {
                document.getElementById('totalWorkflows').textContent = this.stats.total || 0;
                document.getElementById('activeWorkflows').textContent = this.stats.active || 0;
                document.getElementById('inactiveWorkflows').textContent = this.stats.inactive || 0;
                document.getElementById('totalNodes').textContent = this.stats.total_nodes || 0;
                document.getElementById('uniqueIntegrations').textContent = this.stats.unique_integrations || 0;
            }

            renderWorkflows() {
                const grid = document.getElementById('workflowGrid');
                const noResults = document.getElementById('noResults');
                
                if (this.filteredWorkflows.length === 0) {
                    grid.style.display = 'none';
                    noResults.style.display = 'block';
                    return;
                }

                grid.style.display = 'grid';
                noResults.style.display = 'none';
                
                grid.innerHTML = this.filteredWorkflows.map(workflow => this.createWorkflowCard(workflow)).join('');
            }

            createWorkflowCard(workflow) {
                const statusClass = workflow.active ? 'status-active' : 'status-inactive';
                const statusText = workflow.active ? 'Active' : 'Inactive';
                const statusTooltip = workflow.active ? 'Active - Workflow will execute when triggered' : 'Inactive - Workflow is disabled';
                const complexityClass = `complexity-${workflow.complexity}`;
                
                const tags = workflow.tags.map(tag => 
                    `<span class="tag">${typeof tag === 'string' ? tag : tag.name}</span>`
                ).join('');

                const integrations = workflow.integrations.slice(0, 5).map(integration => 
                    `<span class="integration-tag">${integration}</span>`
                ).join('');

                // Step-by-step process section
                let stepsSection = '';
                if (workflow.steps && workflow.steps.length > 0) {
                  stepsSection = `
                    <div class="details-section">
                      <h4 class="details-title">Step-by-step process (${workflow.steps.length} steps)</h4>
                      <ol class="workflow-steps">
                        ${workflow.steps.map(step => `
                          <li class="workflow-step">
                            <div class="step-header">
                              <strong>${step.name ? step.name : '(Unnamed node)'}</strong>
                              <span class="step-type">[${step.type.replace('n8n-nodes-base.', '')}]</span>
                            </div>
                            <div class="step-note">${step.note}</div>
                          </li>
                        `).join('')}
                      </ol>
                    </div>
                  `;
                } else {
                  // Debug: Show when no steps are found
                  stepsSection = `
                    <div class="details-section">
                      <h4 class="details-title">Step-by-step process</h4>
                      <p style="color: var(--text-muted); font-style: italic;">No step-by-step notes available for this workflow.</p>
                    </div>
                  `;
                }

                return `
                    <div class="workflow-card" data-trigger="${workflow.triggerType}" data-name="${workflow.name.toLowerCase()}" data-description="${workflow.description.toLowerCase()}" data-integrations="${workflow.integrations.join(' ').toLowerCase()}">
                        <div class="workflow-header">
                            <div class="workflow-meta">
                                <div class="workflow-info">
                                    <div class="status-indicator" title="${statusTooltip}">
                                        <div class="status-dot ${statusClass}"></div>
                                        <span class="status-text">${statusText}</span>
                                    </div>
                                    <div class="workflow-stats">
                                        <span><div class="complexity-indicator ${complexityClass}"></div>${workflow.nodeCount} nodes</span>
                                        <span>📁 ${workflow.filename}</span>
                                    </div>
                                </div>
                                <span class="trigger-badge">${workflow.triggerType}</span>
                            </div>
                            <h3 class="workflow-title">${workflow.name}</h3>
                            <p class="workflow-description">${workflow.description}</p>
                            
                            <!-- Integrations moved to main card -->
                            <div class="workflow-integrations">
                                <h4 class="integrations-title">Integrations (${workflow.integrations.length})</h4>
                                <div class="integrations-list">
                                    ${integrations}
                                    ${workflow.integrations.length > 5 ? `<span class="integration-tag">+${workflow.integrations.length - 5} more</span>` : ''}
                                </div>
                            </div>
                        </div>
                        
                        <div class="workflow-details">
                            ${stepsSection}
                            ${workflow.tags.length > 0 ? `
                                <div class="details-section">
                                    <h4 class="details-title">Tags</h4>
                                    <div class="workflow-tags">${tags}</div>
                                </div>
                            ` : ''}
                            ${workflow.createdAt ? `
                                <div class="details-section">
                                    <h4 class="details-title">Metadata</h4>
                                    <div style="font-size: 0.85rem; color: var(--text-muted);">
                                        <p>Created: ${new Date(workflow.createdAt).toLocaleDateString()}</p>
                                        ${workflow.updatedAt ? `<p>Updated: ${new Date(workflow.updatedAt).toLocaleDateString()}</p>` : ''}
                                        ${workflow.versionId ? `<p>Version: ${workflow.versionId.substring(0, 8)}...</p>` : ''}
                                    </div>
                                </div>
                            ` : ''}
                        </div>

                        <div class="workflow-footer">
                            <div class="action-buttons">
                                <button class="btn toggle-details">View Details</button>
                                <button class="btn view-json" data-workflow-name="${workflow.name}" data-filename="${workflow.filename}">View File</button>
                            </div>
                        </div>
                    </div>
                `;
            }

            setupEventListeners() {
                // Search functionality
                document.getElementById('searchInput').addEventListener('input', (e) => {
                    this.currentSearch = e.target.value.toLowerCase();
                    this.filterWorkflows();
                });

                // Filter buttons
                document.querySelectorAll('.filter-btn').forEach(btn => {
                    btn.addEventListener('click', (e) => {
                        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                        e.target.classList.add('active');
                        this.currentFilter = e.target.dataset.filter;
                        this.filterWorkflows();
                    });
                });

                // Theme toggle
                document.getElementById('themeToggle').addEventListener('click', this.toggleTheme);

                // Workflow card interactions
                document.addEventListener('click', (e) => {
                    if (e.target.classList.contains('toggle-details')) {
                        const card = e.target.closest('.workflow-card');
                        card.classList.toggle('expanded');
                        e.target.textContent = card.classList.contains('expanded') ? 'Hide Details' : 'View Details';
                    }

                    if (e.target.classList.contains('view-json')) {
                        const workflowName = e.target.dataset.workflowName;
                        const filename = e.target.dataset.filename;
                        this.showJsonModal(workflowName, filename);
                    }
                });

                // Modal functionality
                document.getElementById('closeModal').addEventListener('click', this.hideJsonModal);
                document.getElementById('jsonModal').addEventListener('click', (e) => {
                    if (e.target === e.currentTarget) this.hideJsonModal();
                });
                document.getElementById('copyJson').addEventListener('click', this.copyJsonToClipboard);
                document.getElementById('downloadJson').addEventListener('click', this.downloadJson);

                // Escape key to close modal
                document.addEventListener('keydown', (e) => {
                    if (e.key === 'Escape') this.hideJsonModal();
                });
            }

            filterWorkflows() {
                this.filteredWorkflows = this.workflows.filter(workflow => {
                    const matchesFilter = this.currentFilter === 'all' || workflow.triggerType === this.currentFilter;
                    const matchesSearch = !this.currentSearch || 
                        workflow.name.toLowerCase().includes(this.currentSearch) ||
                        workflow.description.toLowerCase().includes(this.currentSearch) ||
                        workflow.integrations.some(integration => 
                            integration.toLowerCase().includes(this.currentSearch)
                        ) ||
                        workflow.filename.toLowerCase().includes(this.currentSearch);
                    
                    return matchesFilter && matchesSearch;
                });

                this.renderWorkflows();
            }

            showJsonModal(workflowName, filename) {
                const workflow = this.workflows.find(w => w.name === workflowName);
                if (!workflow) return;

                document.getElementById('modalTitle').textContent = `${workflowName} - JSON`;
                document.getElementById('jsonViewer').value = workflow.rawJson;
                document.getElementById('jsonModal').style.display = 'block';
                document.body.style.overflow = 'hidden';
            }

            hideJsonModal() {
                document.getElementById('jsonModal').style.display = 'none';
                document.body.style.overflow = 'auto';
            }

            copyJsonToClipboard() {
                const jsonViewer = document.getElementById('jsonViewer');
                jsonViewer.select();
                document.execCommand('copy');
                
                const btn = document.getElementById('copyJson');
                const originalText = btn.textContent;
                btn.textContent = '✅ Copied!';
                setTimeout(() => {
                    btn.textContent = originalText;
                }, 2000);
            }

            downloadJson() {
                const jsonContent = document.getElementById('jsonViewer').value;
                const workflowName = document.getElementById('modalTitle').textContent.split(' - ')[0];
                const filename = `${workflowName.replace(/[^a-z0-9]/gi, '_').toLowerCase()}.json`;
                
                const blob = new Blob([jsonContent], { type: 'application/json' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = filename;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
            }

            toggleTheme() {
                document.body.classList.toggle('dark-mode');
                const isDark = document.body.classList.contains('dark-mode');
                document.getElementById('themeToggle').textContent = isDark ? '☀️ Light' : '🌙 Dark';
                localStorage.setItem('darkMode', isDark);
            }

            hideLoading() {
                document.getElementById('loadingIndicator').style.display = 'none';
                document.getElementById('workflowGrid').style.display = 'grid';
            }
        }

        // Initialize the application
        document.addEventListener('DOMContentLoaded', () => {
            // Load saved theme preference
            if (localStorage.getItem('darkMode') === 'true') {
                document.body.classList.add('dark-mode');
                document.getElementById('themeToggle').textContent = '☀️ Light';
            }

            // Initialize the documentation
            new WorkflowDocumentation();
        });
    </script>
</body>
</html>'''
    
    return html_template


def main():
    """Main function to generate the workflow documentation."""
    print("🔍 N8N Workflow Documentation Generator")
    print("=" * 50)
    
    # Initialize analyzer
    analyzer = WorkflowAnalyzer()
    
    # Analyze workflows
    data = analyzer.analyze_all_workflows()
    
    # Generate HTML
    print("📝 Generating HTML documentation...")
    html_content = generate_html_documentation(data)
    
    # Write HTML file
    output_file = "workflow-documentation.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Documentation generated successfully!")
    print(f"📄 Output file: {output_file}")
    print(f"📊 Analyzed {data['stats']['total']} workflows")
    print(f"🔗 Open {output_file} in your browser to view the documentation")


if __name__ == "__main__":
    main()