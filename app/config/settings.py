"""
Application configuration for Stock Analyzer
"""

from pathlib import Path
from typing import Optional

# Project structure
PROJECT_ROOT = Path(__file__).parent.parent.parent
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

# Application settings
APP_NAME = "Stock Analyzer"
APP_VERSION = "0.1.0"
APP_DESCRIPTION = "Comprehensive fundamental analysis web app for stocks"

# Shiny app configuration
SHINY_CONFIG = {
    "debug": False,
    "port": 8000,
    "reload": True,
    "host": "127.0.0.1",
}

# Data processing defaults
DATA_CONFIG = {
    "default_period": "1y",
    "default_symbol": "AAPL",
    "cache_enabled": True,
    "cache_ttl_hours": 24,
}

# Machine learning defaults
ML_CONFIG = {
    "train_test_split": 0.2,
    "random_state": 42,
    "model_type": "random_forest",
    "neural_network": {
        "epochs": 50,
        "batch_size": 32,
        "dropout_rate": 0.2,
    },
}

# Technical analysis defaults
TA_CONFIG = {
    "sma_short": 20,
    "sma_long": 50,
    "ema_short": 12,
    "ema_long": 26,
    "rsi_period": 14,
    "bollinger_period": 20,
    "bollinger_std": 2.0,
    "macd_fast": 12,
    "macd_slow": 26,
    "macd_signal": 9,
}

# Parquet configuration
PARQUET_CONFIG = {
    "compression": "snappy",
    "engine": "pyarrow",
}

# Logging configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        },
        "detailed": {
            "format": "%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(funcName)s() - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "detailed",
            "filename": PROJECT_ROOT / "logs" / "app.log",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"],
    },
}


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
