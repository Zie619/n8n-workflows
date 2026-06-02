#!/usr/bin/env python3
"""
Generate Static Search Index for GitHub Pages
Creates a lightweight JSON index for client-side search functionality.
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any

# Add the parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from workflow_db import WorkflowDatabase


def generate_static_search_index(db_path: str, output_dir: str) -> Dict[str, Any]:
    """Generate a static search index for client-side searching."""

    # Initialize database
    db = WorkflowDatabase(db_path)

    # Get all workflows
    workflows, total = db.search_workflows(limit=10000)  # Get all workflows

    # Get statistics
    stats = db.get_stats()

    # Get categories from service mapping
    categories = db.get_service_categories()

    # Load existing categories from create_categories.py system
    existing_categories = load_existing_categories()

    # Create simplified workflow data for search
    search_workflows = []
    for workflow in workflows:
        # Create searchable text combining multiple fields
        searchable_text = " ".join(
            [
                workflow["name"],
                workflow["description"],
                workflow["filename"],
                " ".join(workflow["integrations"]),
                " ".join(workflow["tags"]) if workflow["tags"] else "",
            ]
        ).lower()

        # Use existing category from create_categories.py system, fallback to integration-based
        category = get_workflow_category(
            workflow["filename"],
            existing_categories,
            workflow["integrations"],
            categories,
        )

        search_workflow = {
            "id": workflow["filename"].replace(".json", ""),
            "name": workflow["name"],
            "description": workflow["description"],
            "filename": workflow["filename"],
            "active": workflow["active"],
            "trigger_type": workflow["trigger_type"],
            "complexity": workflow["complexity"],
            "node_count": workflow["node_count"],
            "integrations": workflow["integrations"],
            "tags": workflow["tags"],
            "category": category,
            "searchable_text": searchable_text,
            "download_url": f"https://raw.githubusercontent.com/Zie619/n8n-workflows/main/workflows/{extract_folder_from_filename(workflow['filename'])}/{workflow['filename']}",
        }
        search_workflows.append(search_workflow)

    # Create comprehensive search index
    search_index = {
        "version": "1.0",
        "generated_at": stats.get("last_indexed", ""),
        "stats": {
            "total_workflows": stats["total"],
            "active_workflows": stats["active"],
            "inactive_workflows": stats["inactive"],
            "total_nodes": stats["total_nodes"],
            "unique_integrations": stats["unique_integrations"],
            "categories": len(get_category_list(categories)),
            "triggers": stats["triggers"],
            "complexity": stats["complexity"],
        },
        "categories": get_category_list(categories),
        "integrations": get_popular_integrations(workflows),
        "workflows": search_workflows,
    }

    return search_index


def load_existing_categories() -> Dict[str, str]:
    """Load existing categories from search_categories.json created by create_categories.py."""
    try:
        with open("context/search_categories.json", "r", encoding="utf-8") as f:
            categories_data = json.load(f)

        # Convert to filename -> category mapping
        category_mapping = {}
        for item in categories_data:
            if item.get("category"):
                category_mapping[item["filename"]] = item["category"]

        return category_mapping
    except FileNotFoundError:
        print(
            "Warning: search_categories.json not found, using integration-based categorization"
        )
        return {}


def get_workflow_category(
    filename: str,
    existing_categories: Dict[str, str],
    integrations: List[str],
    service_categories: Dict[str, List[str]],
) -> str:
    """Get category for workflow, preferring existing assignment over integration-based."""

    # First priority: Use existing category from create_categories.py system
    if filename in existing_categories:
        return existing_categories[filename]

    # Fallback: Use integration-based categorization
    return determine_category(integrations, service_categories)


def determine_category(
    integrations: List[str], categories: Dict[str, List[str]]
) -> str:
    """Determine the category for a workflow based on its integrations."""
    if not integrations:
        return "Uncategorized"

    # Check each category for matching integrations
    for category, services in categories.items():
        for integration in integrations:
            if integration in services:
                return format_category_name(category)

    return "Uncategorized"


def format_category_name(category_key: str) -> str:
    """Format category key to display name."""
    category_mapping = {
        "messaging": "Communication & Messaging",
        "email": "Communication & Messaging",
        "cloud_storage": "Cloud Storage & File Management",
        "database": "Data Processing & Analysis",
        "project_management": "Project Management",
        "ai_ml": "AI Agent Development",
        "social_media": "Social Media Management",
        "ecommerce": "E-commerce & Retail",
        "analytics": "Data Processing & Analysis",
        "calendar_tasks": "Project Management",
        "forms": "Data Processing & Analysis",
        "development": "Technical Infrastructure & DevOps",
    }
    return category_mapping.get(category_key, category_key.replace("_", " ").title())


def get_category_list(categories: Dict[str, List[str]]) -> List[str]:
    """Get formatted list of all categories."""
    formatted_categories = set()
    for category_key in categories.keys():
        formatted_categories.add(format_category_name(category_key))

    # Add categories from the create_categories.py system
    additional_categories = [
        "Business Process Automation",
        "Web Scraping & Data Extraction",
        "Marketing & Advertising Automation",
        "Creative Content & Video Automation",
        "Creative Design Automation",
        "CRM & Sales",
        "Financial & Accounting",
    ]

    for cat in additional_categories:
        formatted_categories.add(cat)

    return sorted(list(formatted_categories))


def get_popular_integrations(workflows: List[Dict]) -> List[Dict[str, Any]]:
    """Get list of popular integrations with counts."""
    integration_counts = {}

    for workflow in workflows:
        for integration in workflow["integrations"]:
            integration_counts[integration] = integration_counts.get(integration, 0) + 1

    # Sort by count and take top 50
    sorted_integrations = sorted(
        integration_counts.items(), key=lambda x: x[1], reverse=True
    )[:50]

    return [{"name": name, "count": count} for name, count in sorted_integrations]


def extract_folder_from_filename(filename: str) -> str:
    """Extract folder name from workflow filename."""
    # Most workflows follow pattern: ID_Service_Purpose_Trigger.json
    # Extract the service name as folder
    parts = filename.replace(".json", "").split("_")
    if len(parts) >= 2:
        return parts[1].capitalize()  # Second part is usually the service
    return "Misc"


def save_search_index(search_index: Dict[str, Any], output_dir: str):
    """Save the search index to multiple formats for different uses."""

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Save complete index
    with open(
        os.path.join(output_dir, "search-index.json"), "w", encoding="utf-8"
    ) as f:
        json.dump(search_index, f, indent=2, ensure_ascii=False)

    # Save stats only (for quick loading)
    with open(os.path.join(output_dir, "stats.json"), "w", encoding="utf-8") as f:
        json.dump(search_index["stats"], f, indent=2, ensure_ascii=False)

    # Save categories only
    with open(os.path.join(output_dir, "categories.json"), "w", encoding="utf-8") as f:
        json.dump(search_index["categories"], f, indent=2, ensure_ascii=False)

    # Save integrations only
    with open(
        os.path.join(output_dir, "integrations.json"), "w", encoding="utf-8"
    ) as f:
        json.dump(search_index["integrations"], f, indent=2, ensure_ascii=False)

    print("Search index generated successfully:")
    print(f"   {search_index['stats']['total_workflows']} workflows indexed")
    print(f"   {len(search_index['categories'])} categories")
    print(f"   {len(search_index['integrations'])} popular integrations")
    print(f"   Files saved to: {output_dir}")


def main():
    """Main function to generate search index."""

    # Paths
    db_path = "database/workflows.db"
    output_dir = "docs/api"

    # Check if database exists
    if not os.path.exists(db_path):
        print(f"Database not found: {db_path}")
        print("Run 'python run.py --reindex' first to create the database")
        sys.exit(1)

    try:
        print("Generating static search index...")
        search_index = generate_static_search_index(db_path, output_dir)
        save_search_index(search_index, output_dir)

        print("Static search index ready for GitHub Pages!")

    except Exception as e:
        print(f"Error generating search index: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
