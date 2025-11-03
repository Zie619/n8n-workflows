#!/usr/bin/env python3
"""
N8N Workflow Importer (Fixed)
Handles nested directory structure and provides better error reporting.
Fixes Issue #124: Empty UI after import.
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import List, Dict, Any
import time
from datetime import datetime

# Try to import categorization function, but continue if not available
try:
    from create_categories import categorize_by_filename
except ImportError:
    def categorize_by_filename(filename):
        """Fallback categorization function."""
        return "Uncategorized"

def load_categories():
    """Load the search categories file."""
    try:
        with open('context/search_categories.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Create the context directory if it doesn't exist
        Path('context').mkdir(exist_ok=True)
        return []

def save_categories(data):
    """Save the search categories file."""
    Path('context').mkdir(exist_ok=True)
    with open('context/search_categories.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

class WorkflowImporter:
    """Import n8n workflows with progress tracking and error handling."""

    def __init__(self, workflows_dir: str = "workflows", recursive: bool = True):
        self.workflows_dir = Path(workflows_dir)
        self.recursive = recursive
        self.imported_count = 0
        self.failed_count = 0
        self.skipped_count = 0
        self.errors = []
        self.import_log = []

    def validate_workflow(self, file_path: Path) -> Dict[str, Any]:
        """
        Validate workflow JSON before import.
        Returns dict with 'valid' boolean and 'issues' list.
        """
        issues = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Basic validation
            if not isinstance(data, dict):
                issues.append("Not a valid JSON object")
                return {"valid": False, "issues": issues}

            # Check required fields
            required_fields = ['nodes', 'connections']
            for field in required_fields:
                if field not in data:
                    issues.append(f"Missing required field: {field}")

            # Check nodes
            if 'nodes' in data:
                if not isinstance(data['nodes'], list):
                    issues.append("'nodes' must be an array")
                elif len(data['nodes']) == 0:
                    issues.append("Workflow has no nodes")

            # Check connections
            if 'connections' in data:
                if not isinstance(data['connections'], dict):
                    issues.append("'connections' must be an object")

            # Check for orphaned nodes (basic check)
            if 'nodes' in data and 'connections' in data:
                node_names = {node.get('name') for node in data['nodes']}
                connected_nodes = set()

                for source_name, source_connections in data['connections'].items():
                    connected_nodes.add(source_name)
                    if isinstance(source_connections, dict) and 'main' in source_connections:
                        for output_connections in source_connections['main']:
                            if isinstance(output_connections, list):
                                for conn in output_connections:
                                    if isinstance(conn, dict) and 'node' in conn:
                                        connected_nodes.add(conn['node'])

                orphaned = node_names - connected_nodes
                if len(orphaned) > len(node_names) * 0.5:  # More than 50% orphaned
                    issues.append(f"Too many orphaned nodes ({len(orphaned)}/{len(node_names)})")

            return {"valid": len(issues) == 0, "issues": issues}

        except json.JSONDecodeError as e:
            issues.append(f"Invalid JSON: {e}")
            return {"valid": False, "issues": issues}
        except Exception as e:
            issues.append(f"Error reading file: {e}")
            return {"valid": False, "issues": issues}

    def import_workflow(self, file_path: Path) -> bool:
        """Import a single workflow file."""
        try:
            # Validate first
            validation = self.validate_workflow(file_path)
            if not validation['valid']:
                self.errors.append(f"{file_path.name}: {', '.join(validation['issues'])}")
                print(f"⚠️  Skipped (validation failed): {file_path.name}")
                for issue in validation['issues']:
                    print(f"    - {issue}")
                self.skipped_count += 1
                return False

            # Check if n8n is running
            if not self.check_n8n_running():
                print("⚠️  n8n is not running. Please start n8n first:")
                print("    n8n start")
                return False

            # Run n8n import command
            result = subprocess.run([
                'npx', 'n8n', 'import:workflow',
                f'--input={file_path}'
            ], capture_output=True, text=True, timeout=30)

            if result.returncode == 0:
                print(f"✅ Imported: {file_path.name}")
                self.import_log.append({
                    "filename": file_path.name,
                    "path": str(file_path),
                    "status": "success",
                    "timestamp": datetime.now().isoformat()
                })

                # Categorize the workflow and update search_categories.json
                suggested_category = categorize_by_filename(file_path.name)

                all_workflows_data = load_categories()

                found = False
                for workflow_entry in all_workflows_data:
                    if workflow_entry.get('filename') == file_path.name:
                        workflow_entry['category'] = suggested_category
                        found = True
                        break

                if not found:
                    # Add new workflow entry if not found (e.g., first import)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        workflow_data = json.load(f)

                    all_workflows_data.append({
                        "filename": file_path.name,
                        "category": suggested_category,
                        "name": workflow_data.get('name', file_path.stem),
                        "description": workflow_data.get('description', ''),
                        "nodes": [node.get('type', '') for node in workflow_data.get('nodes', [])]
                    })

                save_categories(all_workflows_data)
                return True
            else:
                error_msg = result.stderr.strip() or result.stdout.strip()
                self.errors.append(f"{file_path.name}: {error_msg}")
                print(f"❌ Failed: {file_path.name}")
                print(f"    Error: {error_msg[:100]}...")  # Show first 100 chars
                self.import_log.append({
                    "filename": file_path.name,
                    "path": str(file_path),
                    "status": "failed",
                    "error": error_msg,
                    "timestamp": datetime.now().isoformat()
                })
                return False

        except subprocess.TimeoutExpired:
            self.errors.append(f"Timeout importing {file_path.name}")
            print(f"⏰ Timeout: {file_path.name}")
            return False
        except Exception as e:
            self.errors.append(f"Error importing {file_path.name}: {str(e)}")
            print(f"❌ Error: {file_path.name} - {str(e)}")
            return False

    def check_n8n_running(self) -> bool:
        """Check if n8n is running by trying to connect to its API."""
        try:
            # Try to access n8n's health endpoint
            import urllib.request
            response = urllib.request.urlopen('http://localhost:5678/healthz', timeout=2)
            return response.status == 200
        except:
            # n8n might not be running or might be on a different port
            return True  # Assume it's running to avoid blocking

    def get_workflow_files(self) -> List[Path]:
        """Get all workflow JSON files, handling nested directories."""
        if not self.workflows_dir.exists():
            print(f"❌ Workflows directory not found: {self.workflows_dir}")
            return []

        if self.recursive:
            # Look for JSON files in subdirectories (our structure)
            json_files = list(self.workflows_dir.rglob("*.json"))
        else:
            # Look for JSON files in the root directory only
            json_files = list(self.workflows_dir.glob("*.json"))

        if not json_files:
            print(f"❌ No JSON files found in: {self.workflows_dir}")
            if not self.recursive:
                print("   Tip: Use --recursive flag to search subdirectories")
            return []

        return sorted(json_files)

    def import_all(self, limit: int = None) -> Dict[str, Any]:
        """Import all workflow files."""
        workflow_files = self.get_workflow_files()

        if limit:
            workflow_files = workflow_files[:limit]

        total_files = len(workflow_files)

        if total_files == 0:
            return {"success": False, "message": "No workflow files found"}

        print(f"🚀 Starting import of {total_files} workflows...")
        print(f"   Directory: {self.workflows_dir}")
        print(f"   Recursive: {self.recursive}")
        print("-" * 50)

        # Track start time
        start_time = time.time()

        for i, file_path in enumerate(workflow_files, 1):
            # Show progress
            progress = (i / total_files) * 100
            print(f"[{i}/{total_files}] ({progress:.1f}%) Processing {file_path.name}...")

            if self.import_workflow(file_path):
                self.imported_count += 1
            else:
                self.failed_count += 1

            # Add a small delay to avoid overwhelming n8n
            if i % 10 == 0:
                time.sleep(1)

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # Save import log
        self.save_import_log()

        # Summary
        print("\n" + "=" * 50)
        print(f"📊 Import Summary:")
        print(f"✅ Successfully imported: {self.imported_count}")
        print(f"⚠️  Skipped (validation): {self.skipped_count}")
        print(f"❌ Failed imports: {self.failed_count}")
        print(f"📁 Total files processed: {total_files}")
        print(f"⏱️  Time elapsed: {elapsed_time:.1f} seconds")

        if self.imported_count > 0:
            print(f"\n✨ Success! {self.imported_count} workflows have been imported to n8n.")
            print("   You can now access them in the n8n UI at http://localhost:5678")
            print("   Or use the search interface at http://localhost:8000")

        if self.errors:
            print(f"\n❌ Errors encountered:")
            for error in self.errors[:10]:  # Show first 10 errors
                print(f"   • {error}")
            if len(self.errors) > 10:
                print(f"   ... and {len(self.errors) - 10} more errors")

        return {
            "success": self.failed_count == 0 and self.imported_count > 0,
            "imported": self.imported_count,
            "skipped": self.skipped_count,
            "failed": self.failed_count,
            "total": total_files,
            "errors": self.errors,
            "elapsed_time": elapsed_time
        }

    def save_import_log(self):
        """Save import log for debugging."""
        log_file = Path('import_log.json')
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "summary": {
                    "imported": self.imported_count,
                    "failed": self.failed_count,
                    "skipped": self.skipped_count
                },
                "logs": self.import_log
            }, f, indent=2)
        print(f"\n📝 Import log saved to: {log_file}")


def check_n8n_available() -> bool:
    """Check if n8n CLI is available."""
    try:
        result = subprocess.run(
            ['npx', 'n8n', '--version'],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            print(f"✅ n8n CLI found: {result.stdout.strip()}")
            return True
        return False
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def main():
    """Main entry point."""
    import argparse

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Import n8n workflows')
    parser.add_argument('--dir', default='workflows', help='Workflows directory (default: workflows)')
    parser.add_argument('--limit', type=int, help='Limit number of workflows to import (for testing)')
    parser.add_argument('--no-recursive', action='store_true', help='Do not search subdirectories')

    args = parser.parse_args()

    # Setup
    if sys.platform == 'win32':
        # Fix for Windows console encoding
        sys.stdout.reconfigure(encoding='utf-8')

    print("🔧 N8N Workflow Importer (Fixed)")
    print("=" * 40)

    # Check if n8n is available
    if not check_n8n_available():
        print("❌ n8n CLI not found. Please install n8n first:")
        print("   npm install -g n8n")
        print("\nOr use npx:")
        print("   npx n8n start")
        sys.exit(1)

    # Create importer and run
    importer = WorkflowImporter(
        workflows_dir=args.dir,
        recursive=not args.no_recursive
    )

    result = importer.import_all(limit=args.limit)

    # Exit with appropriate code
    sys.exit(0 if result["success"] else 1)


if __name__ == "__main__":
    main()