#!/usr/bin/env python3
"""
Test Sample Workflows
Validate that our upgraded workflows are working properly
"""

import json
from pathlib import Path
from typing import Any, Dict, Iterable, List

DEFAULT_CATEGORIES: List[str] = [
    'Manual',
    'Webhook',
    'Schedule',
    'Http',
    'Code',
]


def _load_workflow_samples(categories: Iterable[str]) -> List[Dict[str, Any]]:
    """Collect workflow metadata for the requested categories."""

    samples: List[Dict[str, Any]] = []

    for category in categories:
        category_path = Path('workflows') / category
        if not category_path.exists():
            continue

        # Test first 2 workflows from each category to limit CI runtime
        workflow_files = list(category_path.glob('*.json'))[:2]

        for workflow_file in workflow_files:
            try:
                with open(workflow_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Validate basic structure
                has_name = 'name' in data and bool(data['name'])
                has_nodes = 'nodes' in data and isinstance(data['nodes'], list)
                has_connections = (
                    'connections' in data
                    and isinstance(data['connections'], dict)
                )

                samples.append(
                    {
                        'file': str(workflow_file),
                        'name': data.get('name', 'Unnamed'),
                        'nodes': len(data.get('nodes', [])),
                        'connections': len(data.get('connections', {})),
                        'has_name': has_name,
                        'has_nodes': has_nodes,
                        'has_connections': has_connections,
                        'valid': has_name and has_nodes and has_connections,
                        'category': category,
                    }
                )

            except Exception as e:  # pragma: no cover - defensive logging
                samples.append(
                    {
                        'file': str(workflow_file),
                        'error': str(e),
                        'valid': False,
                        'category': category,
                    }
                )

    return samples


def _print_summary(samples: List[Dict[str, Any]]) -> tuple[int, int]:
    print("🔍 Testing sample workflows...")
    print(f"\n📊 Tested {len(samples)} sample workflows:")
    print("=" * 60)

    valid_count = 0
    for sample in samples:
        if sample['valid']:
            print(
                f"✅ {sample['name']} ({sample['category']}) - "
                f"{sample['nodes']} nodes, {sample['connections']} connections"
            )
            valid_count += 1
        else:
            error = sample.get('error', 'Invalid structure')
            print(f"❌ {sample['file']} - Error: {error}")

    print(
        "\n🎯 Result: "
        f"{valid_count}/{len(samples)} workflows are valid and ready!"
    )

    # Category breakdown
    category_stats: Dict[str, Dict[str, int]] = {}
    for sample in samples:
        category = sample.get('category', 'unknown')
        if category not in category_stats:
            category_stats[category] = {'valid': 0, 'total': 0}
        category_stats[category]['total'] += 1
        if sample['valid']:
            category_stats[category]['valid'] += 1

    print("\n📁 Category Breakdown:")
    for category, stats in category_stats.items():
        success_rate = (
            (stats['valid'] / stats['total']) * 100
            if stats['total'] > 0
            else 0
        )
        print(
            f"   {category}: {stats['valid']}/{stats['total']} "
            f"({success_rate:.1f}%)"
        )

    return valid_count, len(samples)


def test_sample_workflows() -> None:
    """Test sample workflows to ensure they're working."""

    samples = _load_workflow_samples(DEFAULT_CATEGORIES)

    assert samples, "No workflow samples were discovered."

    invalid_samples = [
        f"{sample['file']}: {sample.get('error', 'Invalid structure')}"
        for sample in samples
        if not sample['valid']
    ]

    if invalid_samples:
        details = '\n'.join(invalid_samples)
        raise AssertionError(f"Invalid workflow samples detected:\n{details}")


if __name__ == "__main__":
    workflow_samples = _load_workflow_samples(DEFAULT_CATEGORIES)
    valid_count, total_count = _print_summary(workflow_samples)

    if total_count == 0:
        print("\n⚠️ No workflows found to validate.")
    elif valid_count == total_count:
        print("\n🎉 ALL SAMPLE WORKFLOWS ARE VALID! 🎉")
    elif valid_count > total_count * 0.8:
        print(
            "\n✅ Most workflows are valid "
            f"({valid_count}/{total_count})"
        )
    else:
        print(
            "\n⚠️ Some workflows need attention "
            f"({valid_count}/{total_count})"
        )
