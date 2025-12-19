"""
Secrets loader utility - exports secrets to environment variables
"""
import os
from typing import Dict, Any


def load_secrets_to_env():
    """
    Load all secrets from config/secrets.py into environment variables
    This ensures EdgarTools and other services can access credentials
    """
    try:
        from config.secrets import (
            SEC_EMAIL,
            TICKER_JSON_URL,
            API_KEYS,
            DATABASE,
            FEATURES
        )
        
        # Export to environment variables
        os.environ['SEC_EMAIL'] = SEC_EMAIL
        os.environ['TICKER_JSON_URL'] = TICKER_JSON_URL
        
        # Export API keys
        if API_KEYS and isinstance(API_KEYS, dict):
            for key, value in API_KEYS.items():
                if value and value != "your_" + key + "_key_here":
                    os.environ[f'API_KEY_{key.upper()}'] = value
        
        # Export database credentials
        if DATABASE and isinstance(DATABASE, dict):
            for key, value in DATABASE.items():
                if value and not str(value).startswith('your_'):
                    os.environ[f'DB_{key.upper()}'] = str(value)
        
        # Export feature flags
        if FEATURES and isinstance(FEATURES, dict):
            for key, value in FEATURES.items():
                os.environ[f'FEATURE_{key.upper()}'] = str(value)
        
        print("✓ Secrets loaded to environment variables")
        return True
        
    except ImportError as e:
        print(f"Warning: Could not load secrets.py: {e}")
        print("Using fallback configuration...")
        # Set fallback SEC email if not provided
        if 'SEC_EMAIL' not in os.environ:
            os.environ['SEC_EMAIL'] = 'app@stock-analyzer.local'
        if 'TICKER_JSON_URL' not in os.environ:
            os.environ['TICKER_JSON_URL'] = 'https://www.sec.gov/files/company_tickers.json'
        return False
    except Exception as e:
        print(f"Error loading secrets: {e}")
        return False
