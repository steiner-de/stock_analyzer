"""
Tests for analysis utilities
"""

import pytest
import polars as pl
import numpy as np
from app.utils.analysis import analyze_fundamentals, calculate_financial_ratios, screen_stocks


def test_analyze_fundamentals():
    """Test fundamental analysis function"""
    df = pl.DataFrame({
        "Date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "Close": [100.0, 101.0, 102.0]
    })
    
    results = analyze_fundamentals(df)
    
    assert "data_points" in results
    assert "date_range" in results
    assert "statistics" in results
    assert results["data_points"] == 3


def test_calculate_financial_ratios():
    """Test financial ratio calculation"""
    income_stmt = pl.DataFrame({})
    balance_sheet = pl.DataFrame({})
    
    ratios = calculate_financial_ratios(income_stmt, balance_sheet)
    
    assert "pe_ratio" in ratios
    assert "debt_to_equity" in ratios
    assert "roe" in ratios


def test_screen_stocks():
    """Test stock screening function"""
    df = pl.DataFrame({
        "Symbol": ["AAPL", "MSFT", "GOOGL"],
        "PE": [15.5, 20.3, 18.2],
        "ROE": [0.10, 0.15, 0.12]
    })
    
    criteria = {"PE": (10, 20)}
    filtered = screen_stocks(df, criteria)
    
    assert len(filtered) <= len(df)
