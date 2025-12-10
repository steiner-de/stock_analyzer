"""
Configuration module for Stock Analyzer
"""

from .theme import THEME, COLORS, TYPOGRAPHY, SPACING, BORDER_RADIUS
from .settings import (
    APP_NAME,
    APP_VERSION,
    SHINY_CONFIG,
    DATA_CONFIG,
    ML_CONFIG,
    TA_CONFIG,
    get_data_path,
    get_model_path,
)

# Try to import secrets (optional - only if secrets.py exists)
try:
    from .secrets import SEC_EMAIL, API_KEYS, DATABASE, FEATURES
    HAS_SECRETS = True
except ImportError:
    HAS_SECRETS = False
    SEC_EMAIL = None
    API_KEYS = {}
    DATABASE = {}
    FEATURES = {}

__all__ = [
    "THEME",
    "COLORS",
    "TYPOGRAPHY",
    "SPACING",
    "BORDER_RADIUS",
    "APP_NAME",
    "APP_VERSION",
    "SHINY_CONFIG",
    "DATA_CONFIG",
    "ML_CONFIG",
    "TA_CONFIG",
    "get_data_path",
    "get_model_path",
    "SEC_EMAIL",
    "API_KEYS",
    "DATABASE",
    "FEATURES",
    "HAS_SECRETS",
]

