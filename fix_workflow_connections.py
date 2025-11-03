#!/usr/bin/env python3
"""
Fix Workflow Connections Script
Repairs broken workflow JSON files by removing orphaned nodes or fixing connections.
Addresses Issues #123 and #125: Missing/incomplete connections preventing import.
"""

import json
import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Tuple

def analyze_workflow(workflow_data: Dict) -> Tuple[Set[str], Set[str], Set[str]]:
    """
    Analyze a workflow to identify connected and orphaned nodes.

    Returns:
        Tuple of (connected_nodes, orphaned_nodes, all_nodes)
    """
    nodes = workflow_data.get('nodes', [])
    connections = workflow_data.get('connections', {})

    all_nodes = {node['name'] for node in nodes}
    connected_nodes = set()

    # Find all nodes that are sources or targets of connections
    for source_name, source_connections in connections.items():
        connected_nodes.add(source_name)

        if isinstance(source_connections, dict) and 'main' in source_connections:
            main_connections = source_connections['main']
            for output_connections in main_connections:
                if isinstance(output_connections, list):
                    for connection in output_connections:
                        if isinstance(connection, dict) and 'node' in connection:
                            connected_nodes.add(connection['node'])

    orphaned_nodes = all_nodes - connected_nodes

    return connected_nodes, orphaned_nodes, all_nodes

def fix_workflow_minimal(workflow_data: Dict) -> Tuple[Dict, Dict]:
    """
    Minimal fix: Remove orphaned error handler and documentation nodes.
    This preserves the original workflow logic while removing broken enhancements.

    Returns:
        Tuple of (fixed_workflow, statistics)
    """
    connected_nodes, orphaned_nodes, all_nodes = analyze_workflow(workflow_data)

    # Identify nodes to remove (orphaned error handlers and documentation)
    nodes_to_remove = set()
    for node in workflow_data.get('nodes', []):
        node_name = node['name']
        node_id = node.get('id', '')

        # Remove orphaned error handlers and documentation nodes
        if node_name in orphaned_nodes:
            if (node_id.startswith('error-handler-') or
                node_id.startswith('documentation-') or
                node_id.startswith('doc-') or
                node.get('type', '').lower() in ['n8n-nodes-base.stickyNote', 'n8n-nodes-base.noOp']):
                nodes_to_remove.add(node_name)

    # Filter out the nodes to remove
    original_node_count = len(workflow_data.get('nodes', []))
    workflow_data['nodes'] = [
        node for node in workflow_data.get('nodes', [])
        if node['name'] not in nodes_to_remove
    ]

    # Clean up connections that reference removed nodes
    clean_connections = {}
    for source_name, source_connections in workflow_data.get('connections', {}).items():
        if source_name not in nodes_to_remove:
            # Filter target nodes
            if isinstance(source_connections, dict) and 'main' in source_connections:
                clean_main = []
                for output_connections in source_connections['main']:
                    if isinstance(output_connections, list):
                        clean_output = [
                            conn for conn in output_connections
                            if isinstance(conn, dict) and conn.get('node') not in nodes_to_remove
                        ]
                        clean_main.append(clean_output)
                    else:
                        clean_main.append(output_connections)

                if any(clean_main):  # Only add if there are connections left
                    clean_connections[source_name] = {'main': clean_main}

    workflow_data['connections'] = clean_connections

    # Recalculate statistics
    new_connected, new_orphaned, new_all = analyze_workflow(workflow_data)

    statistics = {
        'original_node_count': original_node_count,
        'removed_nodes': len(nodes_to_remove),
        'final_node_count': len(workflow_data.get('nodes', [])),
        'original_orphaned': len(orphaned_nodes),
        'final_orphaned': len(new_orphaned),
        'connection_coverage_before': (len(connected_nodes) / len(all_nodes) * 100) if all_nodes else 0,
        'connection_coverage_after': (len(new_connected) / len(new_all) * 100) if new_all else 0
    }

    return workflow_data, statistics

def fix_workflow_aggressive(workflow_data: Dict) -> Tuple[Dict, Dict]:
    """
    Aggressive fix: Ensure all nodes have connections by creating a linear flow.
    This may alter workflow logic but guarantees importability.

    Returns:
        Tuple of (fixed_workflow, statistics)
    """
    connected_nodes, orphaned_nodes, all_nodes = analyze_workflow(workflow_data)

    if not orphaned_nodes:
        # No fix needed
        return workflow_data, {'status': 'already_fixed', 'orphaned_count': 0}

    nodes = workflow_data.get('nodes', [])
    if not nodes:
        return workflow_data, {'status': 'no_nodes', 'orphaned_count': 0}

    # Find trigger nodes (usually the starting point)
    trigger_nodes = [
        node for node in nodes
        if 'trigger' in node.get('type', '').lower() or
           'webhook' in node.get('type', '').lower() or
           'cron' in node.get('type', '').lower() or
           node.get('type', '') == 'n8n-nodes-base.start'
    ]

    # If no trigger found, use the first node
    if not trigger_nodes:
        trigger_nodes = [nodes[0]]

    # Create a linear connection chain for orphaned nodes
    connections = workflow_data.get('connections', {})

    # Get the last connected node to append orphaned ones
    last_connected = None
    for node in nodes:
        if node['name'] in connected_nodes and node['name'] != trigger_nodes[0]['name']:
            last_connected = node

    if not last_connected:
        last_connected = trigger_nodes[0]

    # Connect orphaned nodes in sequence
    orphaned_list = list(orphaned_nodes)
    for i, orphan_name in enumerate(orphaned_list):
        if i == 0:
            # Connect first orphan to last connected node
            if last_connected['name'] not in connections:
                connections[last_connected['name']] = {'main': [[]]}
            connections[last_connected['name']]['main'][0].append({
                'node': orphan_name,
                'type': 'main',
                'index': 0
            })
        else:
            # Connect each orphan to the previous orphan
            prev_orphan = orphaned_list[i - 1]
            connections[prev_orphan] = {
                'main': [[{
                    'node': orphan_name,
                    'type': 'main',
                    'index': 0
                }]]
            }

    workflow_data['connections'] = connections

    # Recalculate statistics
    new_connected, new_orphaned, new_all = analyze_workflow(workflow_data)

    statistics = {
        'original_orphaned': len(orphaned_nodes),
        'final_orphaned': len(new_orphaned),
        'nodes_connected': len(orphaned_nodes) - len(new_orphaned),
        'connection_coverage_before': (len(connected_nodes) / len(all_nodes) * 100) if all_nodes else 0,
        'connection_coverage_after': (len(new_connected) / len(new_all) * 100) if new_all else 0
    }

    return workflow_data, statistics

def process_workflows(fix_mode: str = 'minimal', dry_run: bool = False, limit: int = None):
    """
    Process all workflow files and fix connection issues.

    Args:
        fix_mode: 'minimal' (remove orphaned) or 'aggressive' (connect all)
        dry_run: If True, don't write changes, just analyze
        limit: Process only this many workflows (for testing)
    """
    workflows_path = Path('workflows')

    if not workflows_path.exists():
        print(f"Error: workflows directory not found at {workflows_path}")
        return

    # Create backup directory
    if not dry_run:
        backup_dir = Path(f'workflows_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}')
        backup_dir.mkdir(exist_ok=True)
        print(f"Creating backup in {backup_dir}")

    # Find all workflow JSON files
    workflow_files = list(workflows_path.rglob('*.json'))

    if limit:
        workflow_files = workflow_files[:limit]

    print(f"Processing {len(workflow_files)} workflow files...")

    # Statistics
    total_fixed = 0
    total_failed = 0
    total_already_ok = 0
    total_nodes_removed = 0

    fix_function = fix_workflow_minimal if fix_mode == 'minimal' else fix_workflow_aggressive

    for i, file_path in enumerate(workflow_files, 1):
        try:
            # Read workflow
            with open(file_path, 'r', encoding='utf-8') as f:
                workflow_data = json.load(f)

            # Analyze current state
            connected, orphaned, all_nodes = analyze_workflow(workflow_data)

            if not orphaned:
                total_already_ok += 1
                if i % 100 == 0:
                    print(f"[{i}/{len(workflow_files)}] Processed... ({total_fixed} fixed, {total_already_ok} already OK)")
                continue

            # Apply fix
            fixed_workflow, stats = fix_function(workflow_data)

            if not dry_run:
                # Backup original
                relative_path = file_path.relative_to(workflows_path)
                backup_path = backup_dir / relative_path
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file_path, backup_path)

                # Write fixed version
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(fixed_workflow, f, indent=2, ensure_ascii=False)

            total_fixed += 1
            if fix_mode == 'minimal':
                total_nodes_removed += stats.get('removed_nodes', 0)

            # Progress update
            if i % 100 == 0:
                print(f"[{i}/{len(workflow_files)}] Processed... ({total_fixed} fixed, {total_already_ok} already OK)")

        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            total_failed += 1

    # Final report
    print("\n" + "=" * 60)
    print("WORKFLOW FIX COMPLETE")
    print("=" * 60)
    print(f"Mode: {fix_mode.upper()}")
    print(f"Dry run: {dry_run}")
    print(f"Total workflows processed: {len(workflow_files)}")
    print(f"Workflows fixed: {total_fixed}")
    print(f"Workflows already OK: {total_already_ok}")
    print(f"Failed to process: {total_failed}")

    if fix_mode == 'minimal':
        print(f"Total nodes removed: {total_nodes_removed}")
        print(f"Average nodes removed per workflow: {total_nodes_removed / total_fixed if total_fixed else 0:.1f}")

    if not dry_run and total_fixed > 0:
        print(f"\nBackup created at: {backup_dir}")
        print("To restore: mv workflows_backup_*/workflows/* workflows/")

    return {
        'total': len(workflow_files),
        'fixed': total_fixed,
        'already_ok': total_already_ok,
        'failed': total_failed
    }

def validate_single_workflow(file_path: str):
    """
    Validate and display analysis for a single workflow file.
    """
    path = Path(file_path)

    if not path.exists():
        print(f"File not found: {file_path}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        workflow_data = json.load(f)

    connected, orphaned, all_nodes = analyze_workflow(workflow_data)

    print(f"\nWorkflow Analysis: {path.name}")
    print("=" * 60)
    print(f"Total nodes: {len(all_nodes)}")
    print(f"Connected nodes: {len(connected)}")
    print(f"Orphaned nodes: {len(orphaned)}")
    print(f"Connection coverage: {len(connected) / len(all_nodes) * 100:.1f}%")

    if orphaned:
        print("\nOrphaned nodes:")
        for node_name in sorted(orphaned):
            # Find node details
            for node in workflow_data.get('nodes', []):
                if node['name'] == node_name:
                    print(f"  - {node_name} (ID: {node.get('id', 'N/A')}, Type: {node.get('type', 'N/A')})")
                    break

    print("\nRecommended fix: MINIMAL")
    print("This will remove orphaned error handlers and documentation nodes")
    print("while preserving the original workflow logic.")

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == 'validate':
            # Validate a specific workflow
            if len(sys.argv) > 2:
                validate_single_workflow(sys.argv[2])
            else:
                print("Usage: python fix_workflow_connections.py validate <workflow_file>")
        elif sys.argv[1] == 'dry-run':
            # Dry run - analyze but don't fix
            print("Running in DRY RUN mode - no changes will be made")
            process_workflows(fix_mode='minimal', dry_run=True, limit=10)
        elif sys.argv[1] == 'fix-minimal':
            # Fix with minimal approach
            response = input("This will modify all workflow files. Create backup? (yes/no): ")
            if response.lower() == 'yes':
                process_workflows(fix_mode='minimal', dry_run=False)
            else:
                print("Aborted. No changes made.")
        elif sys.argv[1] == 'fix-aggressive':
            # Fix with aggressive approach
            response = input("WARNING: Aggressive mode may alter workflow logic. Continue? (yes/no): ")
            if response.lower() == 'yes':
                process_workflows(fix_mode='aggressive', dry_run=False)
            else:
                print("Aborted. No changes made.")
        else:
            print("Unknown command:", sys.argv[1])
    else:
        print("Workflow Connection Fixer")
        print("=" * 60)
        print("Usage:")
        print("  python fix_workflow_connections.py validate <file>  - Analyze a single workflow")
        print("  python fix_workflow_connections.py dry-run          - Test fix on 10 workflows")
        print("  python fix_workflow_connections.py fix-minimal      - Remove orphaned nodes")
        print("  python fix_workflow_connections.py fix-aggressive   - Connect all nodes")
        print("\nRecommended: Start with 'dry-run' then use 'fix-minimal'")