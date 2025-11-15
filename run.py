#!/usr/bin/env python3
"""
🚀 N8N Workflows Search Engine Launcher
Start the advanced search system with optimized performance.
"""

import sys
import os
import argparse


def print_banner():
    """Print application banner."""
    print("🚀 n8n-workflows Advanced Search Engine")
    print("=" * 50)


def check_requirements() -> bool:
    """Check if required dependencies are installed."""
    missing_deps = []

    try:
        import sqlite3
    except ImportError:
        missing_deps.append("sqlite3")

    try:
        import uvicorn
    except ImportError:
        missing_deps.append("uvicorn")

    try:
        import fastapi
    except ImportError:
        missing_deps.append("fastapi")

    if missing_deps:
        print(f"❌ Missing dependencies: {', '.join(missing_deps)}")
        print("💡 Install with: pip install -r requirements.txt")
        return False

    print("✅ Dependencies verified")
    return True


def setup_directories():
    """Create necessary directories."""
    directories = ["database", "static", "workflows"]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    print("✅ Directories verified")


def setup_database(force_reindex: bool = False, skip_index: bool = False) -> str:
    """Setup and initialize the database."""
    from workflow_db import WorkflowDatabase

    db_path = "database/workflows.db"

    print(f"🔄 Setting up database: {db_path}")
    db = WorkflowDatabase(db_path)

    # Skip indexing in CI mode or if explicitly requested
    if skip_index:
        print("⏭️  Skipping workflow indexing (CI mode)")
        stats = db.get_stats()
        print(f"✅ Database ready: {stats['total']} workflows")
        return db_path

    # Check if database has data or force reindex
    stats = db.get_stats()
    if stats["total"] == 0 or force_reindex:
        print("📚 Indexing workflows...")
        index_stats = db.index_all_workflows(force_reindex=True)
        print(f"✅ Indexed {index_stats['processed']} workflows")

        # Show final stats
        final_stats = db.get_stats()
        print(f"📊 Database contains {final_stats['total']} workflows")
    else:
        print(f"✅ Database ready: {stats['total']} workflows")

    return db_path


def start_server(host: str = "127.0.0.1", port: int = 8000, reload: bool = False):
    """Start the FastAPI server."""
    print(f"🌐 Starting server at http://{host}:{port}")
    print(f"📊 API Documentation: http://{host}:{port}/docs")
    print(f"🔍 Workflow Search: http://{host}:{port}/api/workflows")
    print()
    print("Press Ctrl+C to stop the server")
    print("-" * 50)

    # Configure database path
    os.environ["WORKFLOW_DB_PATH"] = "database/workflows.db"

    # Start uvicorn with better configuration
    import uvicorn

    uvicorn.run(
        "api_server:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info",
        access_log=False,  # Reduce log noise
    )


def main():
    """Main entry point with command line arguments."""
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(
        description="N8N Workflows Search Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run.py                    # Start with default settings
  python run.py --port 3000        # Start on port 3000
  python run.py --host 0.0.0.0     # Accept external connections
  python run.py --reindex          # Force database reindexing
  python run.py --dev              # Development mode with auto-reload
        """,
    )

    parser.add_argument(
        "--host", default="127.0.0.1", help="Host to bind to (default: 127.0.0.1)"
    )
    parser.add_argument(
        "--port", type=int, default=8000, help="Port to bind to (default: 8000)"
    )
    parser.add_argument(
        "--reindex", action="store_true", help="Force database reindexing"
    )
    parser.add_argument(
        "--dev", action="store_true", help="Development mode with auto-reload"
    )
    parser.add_argument(
        "--skip-index",
        action="store_true",
        help="Skip workflow indexing (useful for CI/testing)",
    )

    args = parser.parse_args()

    # Also check environment variable for CI mode
    ci_mode = os.environ.get("CI", "").lower() in ("true", "1", "yes")
    skip_index = args.skip_index or ci_mode

    print_banner()

    # Check dependencies
    if not check_requirements():
        sys.exit(1)

    # Setup directories
    setup_directories()

    # Setup database
    try:
        setup_database(force_reindex=args.reindex, skip_index=skip_index)
    except Exception as e:
        print(f"❌ Database setup error: {e}")
        sys.exit(1)

    # Start server
    try:
        start_server(host=args.host, port=args.port, reload=args.dev)
    except KeyboardInterrupt:
        print("\n👋 Server stopped!")
    except Exception as e:
        print(f"❌ Server error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
