import json
import os
from pathlib import Path
import glob
import re

def load_def_categories():
    """Load the definition categories from def_categories.json"""
    def_categories_path = Path("context/def_categories.json")
    with open(def_categories_path, 'r', encoding='utf-8') as f:
        raw_map = json.load(f)

    # Normalize keys: strip non-alphanumerics and lowercase
    integration_to_category = {
        re.sub(r"[^a-z0-9]", "", item["integration"].lower()): item["category"]
        for item in raw_map
    }
    return integration_to_category

def extract_tokens_from_filename(filename):
    """Extract tokens from filename by splitting on '_' and removing '.json'"""
    # Remove .json extension
    name_without_ext = filename.replace('.json', '')
    
    # Split by underscore
    tokens = name_without_ext.split('_')
    
    # Convert to lowercase for matching
    tokens = [token.lower() for token in tokens if token]
    
    return tokens

def find_matching_category(tokens, integration_to_category):
    """Find the first matching category for the given tokens"""
    for token in tokens:
        # Normalize token same as keys
        norm = re.sub(r"[^a-z0-9]", "", token.lower())
        if norm in integration_to_category:
            return integration_to_category[norm]
    
    # Try partial matches for common variations
    for token in tokens:
        norm = re.sub(r"[^a-z0-9]", "", token.lower())
        for integration_key in integration_to_category:
            if norm in integration_key or integration_key in norm:
                return integration_to_category[integration_key]
    
    return ""

def categorize_by_filename(filename):
    """
    Categorize workflow based on filename patterns.
    Returns the most likely category or None if uncertain.
    """
    filename_lower = filename.lower()
    
    # Security & Authentication
    if any(word in filename_lower for word in ['totp', 'bitwarden', 'auth', 'security']):
        return "Technical Infrastructure & DevOps"

    # Data Processing & File Operations
    if any(word in filename_lower for word in ['process', 'writebinaryfile', 'readbinaryfile', 'extractfromfile', 'converttofile', 'googlefirebasecloudfirestore', 'supabase', 'surveymonkey', 'renamekeys', 'readpdf', 'wufoo', 'splitinbatches', 'airtop', 'comparedatasets', 'spreadsheetfile', 'calcslive']):
        return "Data Processing & Analysis"

    # Utility & Business Process Automation
    if any(word in filename_lower for word in ['noop', 'code', 'schedule', 'filter', 'splitout', 'wait', 'limit', 'aggregate', 'acuityscheduling', 'eventbrite', 'philipshue', 'stickynote', 'n8ntrainingcustomerdatastore', 'n8n']):
        return "Business Process Automation"

    # Webhook & API related
    if any(word in filename_lower for word in ['webhook', 'respondtowebhook', 'http', 'rssfeedread']):
        return "Web Scraping & Data Extraction"

    # Form & Data Collection
    if any(word in filename_lower for word in ['form', 'typeform', 'jotform']):
        return "Data Processing & Analysis"

    # Local file operations
    if any(word in filename_lower for word in ['localfile', 'filemaker']):
        return "Cloud Storage & File Management"

    # Database operations
    if any(word in filename_lower for word in ['postgres', 'mysql', 'mongodb', 'redis', 'elasticsearch', 'snowflake']):
        return "Data Processing & Analysis"

    # AI & Machine Learning
    if any(word in filename_lower for word in ['openai', 'awstextract', 'awsrekognition', 'humanticai', 'openthesaurus', 'googletranslate', 'summarize']):
        return "AI Agent Development"

    # E-commerce specific
    if any(word in filename_lower for word in ['woocommerce', 'gumroad']):
        return "E-commerce & Retail"

    # Social media specific
    if any(word in filename_lower for word in ['facebook', 'linkedin', 'instagram']):
        return "Social Media Management"

    # Customer support
    if any(word in filename_lower for word in ['zendesk', 'intercom', 'drift', 'pagerduty']):
        return "Communication & Messaging"

    # Analytics & Tracking
    if any(word in filename_lower for word in ['googleanalytics', 'segment', 'mixpanel']):
        return "Data Processing & Analysis"

    # Development tools
    if any(word in filename_lower for word in ['git', 'github', 'gitlab', 'travisci', 'jenkins', 'uptimerobot', 'gsuiteadmin', 'debughelper', 'bitbucket']):
        return "Technical Infrastructure & DevOps"

    # CRM & Sales tools
    if any(word in filename_lower for word in ['pipedrive', 'hubspot', 'salesforce', 'copper', 'orbit', 'agilecrm']):
        return "CRM & Sales"

    # Marketing tools
    if any(word in filename_lower for word in ['mailchimp', 'convertkit', 'sendgrid', 'mailerlite', 'lemlist', 'sendy', 'postmark', 'mailgun']):
        return "Marketing & Advertising Automation"

    # Project management
    if any(word in filename_lower for word in ['asana', 'mondaycom', 'clickup', 'trello', 'notion', 'toggl', 'microsofttodo', 'calendly', 'jira']):
        return "Project Management"

    # Communication
    if any(word in filename_lower for word in ['slack', 'telegram', 'discord', 'mattermost', 'twilio', 'emailreadimap', 'teams', 'gotowebinar']):
        return "Communication & Messaging"

    # Cloud storage
    if any(word in filename_lower for word in ['dropbox', 'googledrive', 'onedrive', 'awss3', 'googledocs']):
        return "Cloud Storage & File Management"

    # Creative tools
    if any(word in filename_lower for word in ['canva', 'figma', 'bannerbear', 'editimage']):
        return "Creative Design Automation"

    # Video & content
    if any(word in filename_lower for word in ['youtube', 'vimeo', 'storyblok', 'strapi']):
        return "Creative Content & Video Automation"

    # Financial tools
    if any(word in filename_lower for word in ['stripe', 'chargebee', 'quickbooks', 'harvest']):
        return "Financial & Accounting"

    # Weather & external APIs
    if any(word in filename_lower for word in ['openweathermap', 'nasa', 'crypto', 'coingecko']):
        return "Web Scraping & Data Extraction"

    return ""

def main():
    # Load definition categories
    integration_to_category = load_def_categories()
    
    # Get all JSON files from workflows directory
    workflows_dir = Path("workflows")
    json_files = glob.glob(
        os.path.join(workflows_dir, "**", "*.json"),
        recursive=True
    ) 
    
    # Process each file
    search_categories = []
    
    for json_file in json_files:
        path_obj = Path(json_file)
        filename = path_obj.name
        tokens = extract_tokens_from_filename(filename)
        category = find_matching_category(tokens, integration_to_category)
        
        search_categories.append({
            "filename": filename,
            "category": category
        })

    # Second pass for categorization
    for item in search_categories:
        if not item['category']:
            item['category'] = categorize_by_filename(item['filename'])
    
    # Sort by filename for consistency
    search_categories.sort(key=lambda x: x['filename'])
    
    # Write to search_categories.json
    output_path = Path("context/search_categories.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(search_categories, f, indent=2, ensure_ascii=False)
    
    print(f"Generated search_categories.json with {len(search_categories)} entries")
    
    # Generate unique categories list for API
    unique_categories = set()
    for item in search_categories:
        if item['category']:
            unique_categories.add(item['category'])
    
    # Always include 'Uncategorized' for workflows without categories
    unique_categories.add('Uncategorized')
    
    # Sort categories alphabetically
    categories_list = sorted(list(unique_categories))
    
    # Write unique categories to a separate file for API consumption
    categories_output_path = Path("context/unique_categories.json")
    with open(categories_output_path, 'w', encoding='utf-8') as f:
        json.dump(categories_list, f, indent=2, ensure_ascii=False)
    
    print(f"Generated unique_categories.json with {len(categories_list)} categories")
    
    # Print some statistics
    categorized = sum(1 for item in search_categories if item['category'])
    uncategorized = len(search_categories) - categorized
    print(f"Categorized: {categorized}, Uncategorized: {uncategorized}")
    
    # Print detailed category statistics
    print("\n" + "="*50)
    print("CATEGORY DISTRIBUTION (Top 20)")
    print("="*50)
    
    # Count categories
    category_counts = {}
    for item in search_categories:
        category = item['category'] if item['category'] else "Uncategorized"
        category_counts[category] = category_counts.get(category, 0) + 1
    
    # Sort by count (descending)
    sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Display top 20
    for i, (category, count) in enumerate(sorted_categories[:20], 1):
        print(f"{i:2d}. {category:<40} {count:>4} files")
    
    if len(sorted_categories) > 20:
        remaining = len(sorted_categories) - 20
        print(f"\n... and {remaining} more categories")

    # Write tips on uncategorized workflows
    print("\n" + "="*50)
    print("Tips on uncategorized workflows")
    print("="*50)
    print("1. At the search, you'll be able to list all uncategorized workflows.")
    print("2. If the workflow JSON filename has a clear service name (eg. Twilio), it could just be we are missing its category definition at context/def_categories.json.")
    print("3. You can contribute to the category definitions and then make a pull request to help improve the search experience.")


    # Done message
    print("\n" + "="*50)
    print("Done! Search re-indexed with categories.")
    print("="*50)

if __name__ == "__main__":
    main()