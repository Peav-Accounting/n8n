#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime
from github import Github
from pathlib import Path

def load_existing_errors(repo, file_path):
    """Load existing errors from GitHub."""
    try:
        content = repo.get_contents(file_path)
        return json.loads(content.decoded_content)
    except:
        return []

def update_error_log(token, repo_name, file_path, new_error):
    """Update error log in GitHub repository."""
    g = Github(token)
    repo = g.get_repo(repo_name)
    
    # Load existing errors
    errors = load_existing_errors(repo, file_path)
    
    # Add new error
    errors.append(new_error)
    
    # Update file in GitHub
    content = json.dumps(errors, indent=2)
    try:
        contents = repo.get_contents(file_path)
        repo.update_file(
            file_path,
            f"📝 Log agent error: {new_error['error_type']} for {new_error['agent_id']}",
            content,
            contents.sha
        )
    except:
        repo.create_file(
            file_path,
            f"📝 Create agent error log",
            content
        )

def main():
    # Get error data from n8n workflow
    if len(sys.argv) < 2:
        print("Error: No data provided")
        sys.exit(1)
        
    try:
        error_data = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        print("Error: Invalid JSON data")
        sys.exit(1)
    
    # Get GitHub token from environment
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set")
        sys.exit(1)
    
    # Configuration
    repo_name = "Peav-Accounting/n8n"
    file_path = ".github/feedback/agent_errors.json"
    
    # Update error log
    update_error_log(token, repo_name, file_path, error_data)
    print("Successfully logged error to GitHub")

if __name__ == "__main__":
    main()
