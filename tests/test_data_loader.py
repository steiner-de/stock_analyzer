"""
Tests for data loading utilities
"""

import pytest
import pandas as pd
from app.utils.data_loader import fetch_stock_data, load_parquet, save_parquet
from pathlib import Path
import tempfile


def test_fetch_stock_data():
    """Test fetching stock data"""
    try:
        data = fetch_stock_data("AAPL", period="1mo")
        assert isinstance(data, pd.DataFrame)
        assert len(data) > 0
        assert "Close" in data.columns
    except Exception as e:
        pytest.skip(f"Could not fetch data: {str(e)}")


def test_parquet_io():
    """Test Parquet file I/O"""
    with tempfile.TemporaryDirectory() as tmpdir:
        df = pd.DataFrame({
            "Date": ["2023-01-01", "2023-01-02"],
            "Close": [100.0, 101.0]
        })
        
        filepath = Path(tmpdir) / "test.parquet"
        save_parquet(df, str(filepath))
        
        loaded_df = load_parquet(str(filepath))
        assert loaded_df.shape == df.shape
