#!/usr/bin/env python3
"""
测试示例工作流
验证我们升级后的工作流是否正常工作
"""

import json
from pathlib import Path
from typing import Dict, List, Any

def test_sample_workflows():
    """测试示例工作流以确保它们正常工作"""
    print("🔍 测试示例工作流中...")
    
    samples = []
    categories = ['Manual', 'Webhook', 'Schedule', 'Http', 'Code']
    
    for category in categories:
        category_path = Path('workflows') / category
        if category_path.exists():
            workflow_files = list(category_path.glob('*.json'))[:2]  # 每个分类测试前2个工作流
            
            for workflow_file in workflow_files:
                try:
                    with open(workflow_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # 验证基本结构
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
    
    print(f"\n📊 已测试 {len(samples)} 个示例工作流:")
    print("=" * 60)
    
    valid_count = 0
    for sample in samples:
        if sample['valid']:
            print(f"✅ {sample['name']} ({sample['category']}) - {sample['nodes']} 个节点, {sample['connections']} 个连接")
            valid_count += 1
        else:
                    print(f"❌ {sample['file']} - 错误: {sample.get('error', '结构无效')}")
    
    print(f"\n🎯 结果: {valid_count}/{len(samples)} 个工作流有效且就绪!")
    
    # Category breakdown
    category_stats = {}
    for sample in samples:
        category = sample.get('category', 'unknown')
        if category not in category_stats:
            category_stats[category] = {'valid': 0, 'total': 0}
        category_stats[category]['total'] += 1
        if sample['valid']:
            category_stats[category]['valid'] += 1
    
    print(f"\n📁 分类统计:")
    for category, stats in category_stats.items():
        success_rate = (stats['valid'] / stats['total']) * 100 if stats['total'] > 0 else 0
        print(f"   {category}: {stats['valid']}/{stats['total']} ({success_rate:.1f}%)")
    
    return valid_count, len(samples)

if __name__ == "__main__":
    valid_count, total_count = test_sample_workflows()
    
    if valid_count == total_count:
        print(f"\n🎉 所有示例工作流都有效! 🎉")
    elif valid_count > total_count * 0.8:
        print(f"\n✅ 大多数工作流有效 ({valid_count}/{total_count})")
    else:
        print(f"\n⚠️ 部分工作流需要注意 ({valid_count}/{total_count})")
