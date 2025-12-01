"""
Configuration settings for Stock Analyzer
"""

from pathlib import Path
from typing import Optional

# Project structure
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
APP_DIR = PROJECT_ROOT / "app"

# Data directories
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
CACHE_DIR = DATA_DIR / "cache"

# Model directories
TRAINED_MODELS_DIR = MODELS_DIR / "trained"
MODEL_CONFIGS_DIR = MODELS_DIR / "configs"

# API Configuration
DEFAULT_PERIOD = "1y"
DEFAULT_STOCK_SYMBOL = "AAPL"

# Machine Learning
TRAIN_TEST_SPLIT = 0.2
RANDOM_STATE = 42

# Shiny App
SHINY_DEBUG = True
SHINY_PORT = 8000

# Data Processing
PARQUET_COMPRESSION = "snappy"


def get_data_path(symbol: str, data_type: str = "price") -> Path:
    """
    Get file path for stock data
    
    Args:
        symbol: Stock ticker symbol
        data_type: Type of data ('price', 'fundamentals', etc.)
    
    Returns:
        Path object
    """
    return PROCESSED_DATA_DIR / f"{symbol}_{data_type}.parquet"


def get_model_path(model_name: str) -> Path:
    """
    Get file path for trained model
    
    Args:
        model_name: Name of the model
    
    Returns:
        Path object
    """
    return TRAINED_MODELS_DIR / f"{model_name}.pkl"
