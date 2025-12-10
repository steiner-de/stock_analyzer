"""
Example secrets configuration file

IMPORTANT: 
- Copy this file to secrets.py
- Fill in your actual credentials
- secrets.py is in .gitignore and should NEVER be committed
"""

# SEC Edgar configuration (required for EdgarTools)
# Get your email from SEC - it's required to identify yourself when accessing SEC data
SEC_EMAIL = "john.steiner.de@gmail.com"

# Ticker data source
TICKER_JSON_URL = "https://www.sec.gov/files/company_tickers.json"

# Optional: API keys for other services
API_KEYS = {
    "yfinance": "your_yfinance_key_here",  # if using premium features
    "alpha_vantage": "your_av_key_here",    # if using Alpha Vantage
}

# Optional: Database credentials
DATABASE = {
    "host": "localhost",
    "user": "your_user",
    "password": "your_password",
    "database": "stock_analyzer",
}

# Optional: Feature flags
FEATURES = {
    "enable_caching": True,
    "cache_ttl_hours": 24,
    "enable_ml_models": True,
}
