"""
Data loading utilities for Stock Analyzer
"""

import yfinance as yf
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, Any, Optional


def fetch_stock_data(symbol: str, period: str = "1y") -> Dict[str, Any]:
    """
    Fetch stock data using yfinance
    
    Args:
        symbol: Stock ticker symbol (e.g., 'AAPL')
        period: Data period (e.g., '1y', '5y')
    
    Returns:
        Dictionary with stock data
    """
    try:
        hist_data = yf.download(symbol, period=period, progress=False)
        curr_data = yf.Ticker(symbol).history(period)
        return data.reset_index() # type: ignore
    except Exception as e:
        raise ValueError(f"Failed to fetch data for {symbol}: {str(e)}")


def load_parquet(filepath: str) -> pd.DataFrame:
    """
    Load data from Parquet file
    
    Args:
        filepath: Path to Parquet file
    
    Returns:
        Pandas DataFrame
    """
    return pd.read_parquet(filepath)


def save_parquet(df: pd.DataFrame, filepath: str) -> None:
    """
    Save DataFrame to Parquet file
    
    Args:
        df: Pandas DataFrame to save
        filepath: Path to save Parquet file
    """
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(filepath)


def fetch_fundamental_data(symbol: str) -> dict:
    """
    Fetch fundamental data using yfinance
    
    Args:
        symbol: Stock ticker symbol
    
    Returns:
        Dictionary with fundamental metrics
    """
    ticker = yf.Ticker(symbol)
    
    return {
        "info": ticker.info,
        "balance_sheet": ticker.balance_sheet,
        "income_stmt": ticker.income_stmt,
        "cash_flow": ticker.cash_flow,
        "quarterly_financials": ticker.quarterly_financials,
    }
