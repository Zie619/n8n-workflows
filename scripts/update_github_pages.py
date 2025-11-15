#!/usr/bin/env python3
"""
Update GitHub Pages Files
Fixes the hardcoded timestamp and ensures proper deployment.
Addresses Issues #115 and #129.
"""

import json
from datetime import datetime
from pathlib import Path
import re


def update_html_timestamp(html_file: str):
    """Update the timestamp in the HTML file to current date."""
    file_path = Path(html_file)

    if not file_path.exists():
        print(f"Warning: {html_file} not found")
        return False

    # Read the HTML file
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Get current month and year
    current_date = datetime.now().strftime("%B %Y")

    # Replace the hardcoded timestamp
    # Look for pattern like "Last updated: Month Year"
    pattern = r'(<p class="footer-meta">Last updated:)\s*([^<]+)'
    replacement = f"\\1 {current_date}"

    updated_content = re.sub(pattern, replacement, content)

    # Also add a meta tag with the exact timestamp for better tracking
    if '<meta name="last-updated"' not in updated_content:
        timestamp_meta = (
            f'    <meta name="last-updated" content="{datetime.now().isoformat()}">\n'
        )
        updated_content = updated_content.replace("</head>", f"{timestamp_meta}</head>")

    # Write back the updated content
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"✅ Updated timestamp in {html_file} to: {current_date}")
    return True


def update_api_timestamp(api_dir: str):
    """Update timestamp in API JSON files."""
    api_path = Path(api_dir)

    if not api_path.exists():
        api_path.mkdir(parents=True, exist_ok=True)

    # Create or update a metadata file with current timestamp
    metadata = {
        "last_updated": datetime.now().isoformat(),
        "last_updated_readable": datetime.now().strftime("%B %d, %Y at %H:%M UTC"),
        "version": "2.0.1",
        "deployment_type": "github_pages",
    }

    metadata_file = api_path / "metadata.json"
    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"✅ Created metadata file: {metadata_file}")

    # Update stats.json if it exists
    stats_file = api_path / "stats.json"
    if stats_file.exists():
        with open(stats_file, "r", encoding="utf-8") as f:
            stats = json.load(f)

        stats["last_updated"] = datetime.now().isoformat()

        with open(stats_file, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2)

        print(f"✅ Updated stats file: {stats_file}")

    return True


def create_github_pages_config():
    """Create necessary GitHub Pages configuration files."""

    # Create/update _config.yml for Jekyll (GitHub Pages)
    config_content = """# GitHub Pages Configuration
theme: null
title: N8N Workflows Repository
description: Browse and search 2000+ n8n workflow automation templates
baseurl: "/n8n-workflows"
url: "https://zie619.github.io"

# Build settings
markdown: kramdown
exclude:
  - workflows/
  - scripts/
  - src/
  - "*.py"
  - requirements.txt
  - Dockerfile
  - docker-compose.yml
  - k8s/
  - helm/
  - Documentation/
  - context/
  - database/
  - static/
  - templates/
  - .github/
  - .devcontainer/
"""

    config_file = Path("docs/_config.yml")
    with open(config_file, "w", encoding="utf-8") as f:
        f.write(config_content)
    print(f"✅ Created Jekyll config: {config_file}")

    # Create .nojekyll file to bypass Jekyll processing (for pure HTML/JS site)
    nojekyll_file = Path("docs/.nojekyll")
    nojekyll_file.touch()
    print(f"✅ Created .nojekyll file: {nojekyll_file}")

    # Create a simple 404.html page
    error_page_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            text-align: center;
            padding: 2rem;
        }
        h1 { font-size: 6rem; margin: 0; }
        p { font-size: 1.5rem; margin: 1rem 0; }
        a {
            display: inline-block;
            margin-top: 2rem;
            padding: 1rem 2rem;
            background: white;
            color: #667eea;
            text-decoration: none;
            border-radius: 5px;
            transition: transform 0.2s;
        }
        a:hover { transform: scale(1.05); }
    </style>
</head>
<body>
    <div class="container">
        <h1>404</h1>
        <p>Page not found</p>
        <p>The n8n workflows repository has been updated.</p>
        <a href="/n8n-workflows/">Go to Homepage</a>
    </div>
</body>
</html>"""

    error_file = Path("docs/404.html")
    with open(error_file, "w", encoding="utf-8") as f:
        f.write(error_page_content)
    print(f"✅ Created 404 page: {error_file}")


def verify_github_pages_structure():
    """Verify that all necessary files exist for GitHub Pages deployment."""

    required_files = [
        "docs/index.html",
        "docs/css/styles.css",
        "docs/js/app.js",
        "docs/js/search.js",
        "docs/api/search-index.json",
        "docs/api/stats.json",
        "docs/api/categories.json",
        "docs/api/integrations.json",
    ]

    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
            print(f"❌ Missing: {file_path}")
        else:
            print(f"✅ Found: {file_path}")

    if missing_files:
        print(f"\n⚠️  Warning: {len(missing_files)} required files are missing")
        print("Run the following commands to generate them:")
        print("  python workflow_db.py --index --force")
        print("  python create_categories.py")
        print("  python scripts/generate_search_index.py")
        return False

    print("\n✅ All required files present for GitHub Pages deployment")
    return True


def fix_base_url_references():
    """Fix any hardcoded URLs to use relative paths for GitHub Pages."""

    # Update index.html to use relative paths
    index_file = Path("docs/index.html")
    if index_file.exists():
        with open(index_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace absolute paths with relative ones
        replacements = [
            ('href="/css/', 'href="css/'),
            ('src="/js/', 'src="js/'),
            ('href="/api/', 'href="api/'),
            ('fetch("/api/', 'fetch("api/'),
            ("fetch('/api/", "fetch('api/"),
        ]

        for old, new in replacements:
            content = content.replace(old, new)

        with open(index_file, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Fixed URL references in index.html")

    # Update JavaScript files
    js_files = ["docs/js/app.js", "docs/js/search.js"]
    for js_file in js_files:
        js_path = Path(js_file)
        if js_path.exists():
            with open(js_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Fix API endpoint references
            content = content.replace("fetch('/api/", "fetch('api/")
            content = content.replace('fetch("/api/', 'fetch("api/')
            content = content.replace("'/api/", "'api/")
            content = content.replace('"/api/', '"api/')

            with open(js_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Fixed URL references in {js_file}")


def main():
    """Main function to update GitHub Pages deployment."""

    print("🔧 GitHub Pages Update Script")
    print("=" * 50)

    # Step 1: Update timestamps
    print("\n📅 Updating timestamps...")
    update_html_timestamp("docs/index.html")
    update_api_timestamp("docs/api")

    # Step 2: Create GitHub Pages configuration
    print("\n⚙️  Creating GitHub Pages configuration...")
    create_github_pages_config()

    # Step 3: Fix URL references
    print("\n🔗 Fixing URL references...")
    fix_base_url_references()

    # Step 4: Verify structure
    print("\n✔️  Verifying deployment structure...")
    if verify_github_pages_structure():
        print("\n✨ GitHub Pages setup complete!")
        print("\nDeployment will be available at:")
        print("   https://zie619.github.io/n8n-workflows/")
        print(
            "\nNote: It may take a few minutes for changes to appear after pushing to GitHub."
        )
    else:
        print("\n⚠️  Some files are missing. Please generate them first.")


if __name__ == "__main__":
    main()
