#!/usr/bin/env python3
"""
Fix Duplicate Workflow Display Issue
Addresses Issue #99: UI displays duplicate entries for same workflows.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Set
import hashlib

def find_duplicate_workflows(workflows_dir: str = "workflows") -> Dict[str, List[Path]]:
    """Find duplicate workflow files based on content hash."""
    workflows_path = Path(workflows_dir)

    if not workflows_path.exists():
        print(f"Error: workflows directory not found at {workflows_path}")
        return {}

    # Dictionary to store hash -> list of file paths
    hash_to_files = {}

    # Process all JSON files
    json_files = list(workflows_path.rglob('*.json'))
    print(f"Analyzing {len(json_files)} workflow files for duplicates...")

    for file_path in json_files:
        try:
            # Read and normalize the JSON content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = json.load(f)

            # Remove volatile fields that might differ between duplicates
            normalized = content.copy()
            normalized.pop('createdAt', None)
            normalized.pop('updatedAt', None)
            normalized.pop('id', None)  # Workflow ID might be different

            # Create hash of normalized content
            content_str = json.dumps(normalized, sort_keys=True)
            content_hash = hashlib.sha256(content_str.encode()).hexdigest()

            # Store file path by hash
            if content_hash not in hash_to_files:
                hash_to_files[content_hash] = []
            hash_to_files[content_hash].append(file_path)

        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue

    # Filter to only keep hashes with duplicates
    duplicates = {
        hash_val: files
        for hash_val, files in hash_to_files.items()
        if len(files) > 1
    }

    return duplicates

def find_name_duplicates(workflows_dir: str = "workflows") -> Dict[str, List[Path]]:
    """Find workflows with duplicate names (not necessarily same content)."""
    workflows_path = Path(workflows_dir)

    if not workflows_path.exists():
        return {}

    # Dictionary to store workflow name -> list of file paths
    name_to_files = {}

    json_files = list(workflows_path.rglob('*.json'))

    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = json.load(f)

            workflow_name = content.get('name', 'Unnamed')

            if workflow_name not in name_to_files:
                name_to_files[workflow_name] = []
            name_to_files[workflow_name].append(file_path)

        except Exception as e:
            continue

    # Filter to only keep names with duplicates
    duplicates = {
        name: files
        for name, files in name_to_files.items()
        if len(files) > 1
    }

    return duplicates

def remove_exact_duplicates(duplicates: Dict[str, List[Path]], dry_run: bool = True) -> int:
    """Remove exact duplicate files, keeping only one copy."""
    removed_count = 0

    for content_hash, file_paths in duplicates.items():
        # Sort by path to ensure consistent ordering
        file_paths.sort()

        # Keep the first file, remove the rest
        to_keep = file_paths[0]
        to_remove = file_paths[1:]

        print(f"\nFound {len(file_paths)} identical workflows:")
        print(f"  Keeping: {to_keep.name}")
        for path in to_remove:
            print(f"  Removing: {path.name}")

            if not dry_run:
                try:
                    os.remove(path)
                    removed_count += 1
                    print(f"    ✅ Removed {path}")
                except Exception as e:
                    print(f"    ❌ Error removing {path}: {e}")

    return removed_count

def update_workflow_database():
    """Update the workflow database to remove duplicate entries."""
    try:
        import sys
        sys.path.append(str(Path(__file__).parent))
        from workflow_db import WorkflowDatabase

        # Re-index the database
        db = WorkflowDatabase()
        db.index_all_workflows(force_reindex=True)
        print("✅ Database re-indexed to remove duplicate entries")
        return True
    except Exception as e:
        print(f"Error updating database: {e}")
        return False

def fix_ui_duplicate_display():
    """Fix the UI to handle duplicate workflows properly."""

    # Update search_categories.json to remove duplicates
    categories_file = Path('context/search_categories.json')

    if categories_file.exists():
        with open(categories_file, 'r', encoding='utf-8') as f:
            categories_data = json.load(f)

        # Remove duplicate entries based on filename
        seen_filenames = set()
        unique_data = []

        for item in categories_data:
            filename = item.get('filename')
            if filename and filename not in seen_filenames:
                seen_filenames.add(filename)
                unique_data.append(item)

        # Save deduplicated data
        with open(categories_file, 'w', encoding='utf-8') as f:
            json.dump(unique_data, f, indent=2, ensure_ascii=False)

        print(f"✅ Removed {len(categories_data) - len(unique_data)} duplicate entries from search_categories.json")

    # Regenerate search index
    try:
        import subprocess
        result = subprocess.run(
            ['python3', 'scripts/generate_search_index.py'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("✅ Regenerated search index")
        else:
            print(f"Error regenerating search index: {result.stderr}")
    except Exception as e:
        print(f"Error regenerating search index: {e}")

def main():
    """Main function to fix duplicate workflow issues."""
    import argparse

    parser = argparse.ArgumentParser(description='Fix duplicate workflow display issues')
    parser.add_argument('--check', action='store_true', help='Only check for duplicates, do not fix')
    parser.add_argument('--fix-files', action='store_true', help='Remove duplicate files')
    parser.add_argument('--fix-ui', action='store_true', help='Fix UI duplicate display')
    parser.add_argument('--fix-all', action='store_true', help='Fix everything')

    args = parser.parse_args()

    print("🔍 Duplicate Workflow Fixer")
    print("=" * 60)

    # Find exact content duplicates
    print("\n📄 Checking for exact duplicate workflows...")
    exact_duplicates = find_duplicate_workflows()

    if exact_duplicates:
        print(f"\n⚠️  Found {len(exact_duplicates)} groups of duplicate workflows")
        total_duplicates = sum(len(files) - 1 for files in exact_duplicates.values())
        print(f"   Total duplicate files that can be removed: {total_duplicates}")

        if args.fix_files or args.fix_all:
            print("\n🗑️  Removing duplicate files...")
            removed = remove_exact_duplicates(exact_duplicates, dry_run=False)
            print(f"\n✅ Removed {removed} duplicate files")
    else:
        print("✅ No exact duplicate workflows found")

    # Find name duplicates (might be different content)
    print("\n📝 Checking for workflows with duplicate names...")
    name_duplicates = find_name_duplicates()

    if name_duplicates:
        print(f"\n⚠️  Found {len(name_duplicates)} workflow names used multiple times")
        for name, files in list(name_duplicates.items())[:5]:  # Show first 5
            print(f"   '{name}': {len(files)} files")
        if len(name_duplicates) > 5:
            print(f"   ... and {len(name_duplicates) - 5} more")
    else:
        print("✅ No duplicate workflow names found")

    # Fix UI display issues
    if args.fix_ui or args.fix_all:
        print("\n🖥️  Fixing UI duplicate display...")
        fix_ui_duplicate_display()
        update_workflow_database()
        print("✅ UI display fixes applied")

    if args.check:
        print("\n💡 Run with --fix-all to automatically fix all issues")

    print("\n✨ Duplicate check complete!")

if __name__ == "__main__":
    main()