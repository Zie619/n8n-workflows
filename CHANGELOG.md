# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **GitHub Pages Public Search Interface** - Complete client-side search application accessible at https://zie619.github.io/n8n-workflows
  - Responsive HTML/CSS/JavaScript interface with mobile optimization
  - Real-time search across 2,057+ workflows with instant results
  - Category filtering across 15 workflow categories
  - Dark/light theme support with system preference detection
  - Direct workflow JSON download functionality
  - Professional n8n-themed styling and animations
- **CalcsLive Custom Node Workflow** - Engineering calculations workflow showcasing CalcsLive custom node
  - Added `workflows/Calcslive/2058_Calcslive_Engineering_Calculations_Manual.json`
  - Comprehensive tags for searchability (calculation, engineering, custom-node, etc.)
  - Professional description with npm package reference
- **GitHub Actions Automation**
  - `deploy-pages.yml` - Automated deployment to GitHub Pages on workflow changes
  - `update-readme.yml` - Weekly automated README statistics updates
- **Search Index Generation System**
  - `scripts/generate_search_index.py` - Static search index generation for GitHub Pages
  - `scripts/update_readme_stats.py` - Automated README statistics synchronization
  - Support for both developer-chosen and integration-based categorization
- **Enhanced Documentation System**
  - Real-time workflow statistics in README
  - Accurate category counts (updated from 12 to 15 categories)
  - GitHub Pages interface solving Issue #84

### Enhanced
- **Workflow Database System** (`workflow_db.py`)
  - Enhanced CalcsLive custom node detection with pattern exclusions
  - Fixed false positive "Cal.com" detection from "CalcsLive" node names
  - Improved JSON description preservation and indexing
  - Better Unicode handling and error reporting
- **Categorization System** (`create_categories.py`)
  - Added CalcsLive to "Data Processing & Analysis" category
  - Enhanced service name recognition patterns
  - Improved category mapping for custom nodes
- **Search Index Prioritization**
  - Modified `generate_search_index.py` to respect developer-chosen categories
  - Added `load_existing_categories()` function to prioritize `create_categories.py` assignments
  - Maintains fairness by not favoring specific custom nodes

### Fixed
- **Unicode Encoding Issues** - Resolved 'charmap' codec errors in Python scripts
- **Category Assignment Logic** - Search index now properly respects developer category choices
- **Statistics Accuracy** - README now reflects live database statistics instead of hardcoded numbers
- **Documentation Inconsistencies** - Updated category documentation to match actual implementation

### Changed
- **README.md** - Updated with current workflow statistics (2,057 workflows, 367 integrations)
- **Repository Organization** - Enhanced with automated maintenance and public accessibility

## [Previous] - 2024-08-14

### Changed
- Repository history rewritten due to DMCA compliance (Issue #85)
- All existing workflows maintained with improved organization

---

## Contributing to the Changelog

When adding new changes:
- Use **Added** for new features
- Use **Changed** for changes in existing functionality
- Use **Deprecated** for soon-to-be removed features
- Use **Removed** for now removed features
- Use **Fixed** for any bug fixes
- Use **Security** for vulnerability fixes

Each entry should briefly explain the change and its impact on users or contributors.