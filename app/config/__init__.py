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
]
