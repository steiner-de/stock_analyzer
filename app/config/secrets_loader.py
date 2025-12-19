"""
Secrets loader module - loads secrets from a secure location into environment variables
"""
import os
import json
from pathlib import Path

def load_secrets_to_env():
    """Load secrets from a JSON file into environment variables"""
    secrets_file = Path(__file__).parent.parent.parent / 'secrets.json'
    
    if not secrets_file.exists():
        print(f"Warning: Secrets file not found at {secrets_file}")
        return
    
    try:
        with open(secrets_file, 'r') as f:
            secrets = json.load(f)
        
        for key, value in secrets.items():
            os.environ[key] = str(value)
        
        print(f"Loaded {len(secrets)} secrets into environment variables")
    except Exception as e:
        print(f"Error loading secrets: {e}")