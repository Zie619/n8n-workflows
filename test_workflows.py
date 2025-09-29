#!/usr/bin/env python3
"""
Test Sample Workflows
Validate that our upgraded workflows are working properly
"""

import json
from pathlib import Path
from typing import Dict, List, Any

def test_sample_workflows():
    """Test sample workflows to ensure they're working"""
    print("🔍 Testing sample workflows...")
    
    samples = []
    categories = ['Manual', 'Webhook', 'Schedule', 'Http', 'Code']
    
    for category in categories:
        category_path = Path('workflows') / category
        if category_path.exists():
            workflow_files = list(category_path.glob('*.json'))[:2]  # Test first 2 from each category
            
            for workflow_file in workflow_files:
                try:
                    with open(workflow_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # Validate basic structure
                    has_name = 'name' in data and data['name']
                    has_nodes = 'nodes' in data and isinstance(data['nodes'], list)
                    has_connections = 'connections' in data and isinstance(data['connections'], dict)
                    
                    samples.append({
                        'file': str(workflow_file),
                        'name': data.get('name', 'Unnamed'),
                        'nodes': len(data.get('nodes', [])),
                        'connections': len(data.get('connections', {})),
                        'has_name': has_name,
                        'has_nodes': has_nodes,
                        'has_connections': has_connections,
                        'valid': has_name and has_nodes and has_connections,
                        'category': category
                    })
                    
                except Exception as e:
                    samples.append({
                        'file': str(workflow_file),
                        'error': str(e),
                        'valid': False,
                        'category': category
                    })
    
    print(f"\n📊 Tested {len(samples)} sample workflows:")
    print("=" * 60)
    
    valid_count = 0
    for sample in samples:
        if sample['valid']:
            print(f"✅ {sample['name']} ({sample['category']}) - {sample['nodes']} nodes, {sample['connections']} connections")
            valid_count += 1
        else:
            print(f"❌ {sample['file']} - Error: {sample.get('error', 'Invalid structure')}")
    
    print(f"\n🎯 Result: {valid_count}/{len(samples)} workflows are valid and ready!")
    
    # Category breakdown
    category_stats = {}
    for sample in samples:
        category = sample.get('category', 'unknown')
        if category not in category_stats:
            category_stats[category] = {'valid': 0, 'total': 0}
        category_stats[category]['total'] += 1
        if sample['valid']:
            category_stats[category]['valid'] += 1
    
    print(f"\n📁 Category Breakdown:")
    for category, stats in category_stats.items():
        success_rate = (stats['valid'] / stats['total']) * 100 if stats['total'] > 0 else 0
        print(f"   {category}: {stats['valid']}/{stats['total']} ({success_rate:.1f}%)")
    
    return valid_count, len(samples)

if __name__ == "__main__":
    valid_count, total_count = test_sample_workflows()
    
    if valid_count == total_count:
        print(f"\n🎉 ALL SAMPLE WORKFLOWS ARE VALID! 🎉")
    elif valid_count > total_count * 0.8:
        print(f"\n✅ Most workflows are valid ({valid_count}/{total_count})")
    else:
        print(f"\n⚠️ Some workflows need attention ({valid_count}/{total_count})")
