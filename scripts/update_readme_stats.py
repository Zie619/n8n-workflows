#!/usr/bin/env python3
"""
Update README.md with current workflow statistics
Replaces hardcoded numbers with live data from the database.
"""

import json
import os
import re
import sys
from pathlib import Path
from datetime import datetime

# Add the parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from workflow_db import WorkflowDatabase


def get_current_stats():
    """Get current workflow statistics from the database."""
    db_path = "database/workflows.db"

    if not os.path.exists(db_path):
        print("Database not found. Run workflow indexing first.")
        return None

    db = WorkflowDatabase(db_path)
    stats = db.get_stats()

    # Get categories count
    categories = db.get_service_categories()

    return {
        'total_workflows': stats['total'],
        'active_workflows': stats['active'],
        'inactive_workflows': stats['inactive'],
        'total_nodes': stats['total_nodes'],
        'unique_integrations': stats['unique_integrations'],
        'categories_count': len(get_category_list(categories)),
        'triggers': stats['triggers'],
        'complexity': stats['complexity'],
        'last_updated': datetime.now().strftime('%Y-%m-%d')
    }


def get_category_list(categories):
    """Get formatted list of all categories (same logic as search index)."""
    formatted_categories = set()

    # Map technical categories to display names
    category_mapping = {
        'messaging': 'Communication & Messaging',
        'email': 'Communication & Messaging',
        'cloud_storage': 'Cloud Storage & File Management',
        'database': 'Data Processing & Analysis',
        'project_management': 'Project Management',
        'ai_ml': 'AI Agent Development',
        'social_media': 'Social Media Management',
        'ecommerce': 'E-commerce & Retail',
        'analytics': 'Data Processing & Analysis',
        'calendar_tasks': 'Project Management',
        'forms': 'Data Processing & Analysis',
        'development': 'Technical Infrastructure & DevOps'
    }

    for category_key in categories.keys():
        display_name = category_mapping.get(category_key, category_key.replace('_', ' ').title())
        formatted_categories.add(display_name)

    # Add categories from the create_categories.py system
    additional_categories = [
        "Business Process Automation",
        "Web Scraping & Data Extraction",
        "Marketing & Advertising Automation",
        "Creative Content & Video Automation",
        "Creative Design Automation",
        "CRM & Sales",
        "Financial & Accounting"
    ]

    for cat in additional_categories:
        formatted_categories.add(cat)

    return sorted(list(formatted_categories))


def update_readme_stats(stats):
    """Update README.md with current statistics."""
    readme_path = "README.md"

    if not os.path.exists(readme_path):
        print("README.md not found")
        return False

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define replacement patterns and their new values
    replacements = [
        # Main collection description
        (r'A professionally organized collection of \*\*[\d,]+\s+n8n workflows\*\*',
         f'A professionally organized collection of **{stats["total_workflows"]:,} n8n workflows**'),

        # Total workflows in various contexts
        (r'- \*\*[\d,]+\s+workflows\*\* with meaningful',
         f'- **{stats["total_workflows"]:,} workflows** with meaningful'),

        # Statistics section
        (r'- \*\*Total Workflows\*\*: [\d,]+',
         f'- **Total Workflows**: {stats["total_workflows"]:,}'),

        (r'- \*\*Active Workflows\*\*: [\d,]+ \([\d.]+%',
         f'- **Active Workflows**: {stats["active_workflows"]:,} ({(stats["active_workflows"]/stats["total_workflows"]*100):.1f}%'),

        (r'- \*\*Total Nodes\*\*: [\d,]+ \(avg [\d.]+ nodes',
         f'- **Total Nodes**: {stats["total_nodes"]:,} (avg {(stats["total_nodes"]/stats["total_workflows"]):.1f} nodes'),

        (r'- \*\*Unique Integrations\*\*: [\d,]+ different',
         f'- **Unique Integrations**: {stats["unique_integrations"]:,} different'),

        # Update complexity/trigger distribution
        (r'- \*\*Complex\*\*: [\d,]+ workflows \([\d.]+%\)',
         f'- **Complex**: {stats["triggers"].get("Complex", 0):,} workflows ({(stats["triggers"].get("Complex", 0)/stats["total_workflows"]*100):.1f}%)'),

        (r'- \*\*Webhook\*\*: [\d,]+ workflows \([\d.]+%\)',
         f'- **Webhook**: {stats["triggers"].get("Webhook", 0):,} workflows ({(stats["triggers"].get("Webhook", 0)/stats["total_workflows"]*100):.1f}%)'),

        (r'- \*\*Manual\*\*: [\d,]+ workflows \([\d.]+%\)',
         f'- **Manual**: {stats["triggers"].get("Manual", 0):,} workflows ({(stats["triggers"].get("Manual", 0)/stats["total_workflows"]*100):.1f}%)'),

        (r'- \*\*Scheduled\*\*: [\d,]+ workflows \([\d.]+%\)',
         f'- **Scheduled**: {stats["triggers"].get("Scheduled", 0):,} workflows ({(stats["triggers"].get("Scheduled", 0)/stats["total_workflows"]*100):.1f}%)'),

        # Update total in current collection stats
        (r'\*\*Total Workflows\*\*: [\d,]+ automation',
         f'**Total Workflows**: {stats["total_workflows"]:,} automation'),

        (r'\*\*Active Workflows\*\*: [\d,]+ \([\d.]+% active',
         f'**Active Workflows**: {stats["active_workflows"]:,} ({(stats["active_workflows"]/stats["total_workflows"]*100):.1f}% active'),

        (r'\*\*Total Nodes\*\*: [\d,]+ \(avg [\d.]+ nodes',
         f'**Total Nodes**: {stats["total_nodes"]:,} (avg {(stats["total_nodes"]/stats["total_workflows"]):.1f} nodes'),

        (r'\*\*Unique Integrations\*\*: [\d,]+ different',
         f'**Unique Integrations**: {stats["unique_integrations"]:,} different'),

        # Categories count
        (r'Our system automatically categorizes workflows into [\d]+ service categories',
         f'Our system automatically categorizes workflows into {stats["categories_count"]} service categories'),

        # Update any "2000+" references
        (r'2000\+', f'{stats["total_workflows"]:,}+'),
        (r'2,000\+', f'{stats["total_workflows"]:,}+'),

        # Search across X workflows
        (r'Search across [\d,]+ workflows', f'Search across {stats["total_workflows"]:,} workflows'),

        # Instant search across X workflows
        (r'Instant search across [\d,]+ workflows', f'Instant search across {stats["total_workflows"]:,} workflows'),
    ]

    # Apply all replacements
    updated_content = content
    replacements_made = 0

    for pattern, replacement in replacements:
        old_content = updated_content
        updated_content = re.sub(pattern, replacement, updated_content)
        if updated_content != old_content:
            replacements_made += 1

    # Write back to file
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"README.md updated with current statistics:")
    print(f"  - Total workflows: {stats['total_workflows']:,}")
    print(f"  - Active workflows: {stats['active_workflows']:,}")
    print(f"  - Total nodes: {stats['total_nodes']:,}")
    print(f"  - Unique integrations: {stats['unique_integrations']:,}")
    print(f"  - Categories: {stats['categories_count']}")
    print(f"  - Replacements made: {replacements_made}")

    return True


def main():
    """Main function to update README statistics."""
    try:
        print("Getting current workflow statistics...")
        stats = get_current_stats()

        if not stats:
            print("Failed to get statistics")
            sys.exit(1)

        print("Updating README.md...")
        success = update_readme_stats(stats)

        if success:
            print("README.md successfully updated with latest statistics!")
        else:
            print("Failed to update README.md")
            sys.exit(1)

    except Exception as e:
        print(f"Error updating README stats: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()