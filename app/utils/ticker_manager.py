"""
Ticker management utilities for Stock Analyzer
Handles fetching, updating, and searching ticker data
"""

import requests
import pandas as pd
import sqlite3
import json
from datetime import datetime
from typing import List, Optional
from pathlib import Path
import os

from config.settings import get_data_path

from .database import get_db_connection, get_cache, set_cache


class TickerManager:
    """Manage stock ticker data from remote JSON source"""
    
    def __init__(self, json_url: str):
        """
        Initialize TickerManager
        
        Args:
            json_url: URL to JSON file containing ticker data
                     Expected format: [{"symbol": "AAPL", "name": "Apple Inc.", ...}, ...]
        """
        self.json_url = json_url
        self.cache_key = "tickers_data"
        self.cache_ttl = 24  # hours
    
    def fetch_tickers_from_url(self) -> Optional[pd.DataFrame]:
        """
        Download ticker data from JSON URL
        
        Returns:
            Pandas DataFrame with ticker data or None if failed
        """
        try:
            # SEC EDGAR requires User-Agent header with contact info
            headers = {
                'User-Agent': f'Stock Analyzer ({os.environ.get("SEC_EMAIL", "app@stock-analyzer.local")})'
            }
            response = requests.get(self.json_url, headers=headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # SEC returns dict with company CIK as keys, convert to list
            if isinstance(data, dict) and not isinstance(data, list):
                # Extract values from dict
                data = list(data.values())
            
            df = pd.DataFrame(data)
            
            # Ensure required columns
            required_cols = ['ticker', 'title']  # SEC uses 'ticker' and 'title'
            if not all(col in df.columns for col in required_cols):
                # Try alternative column names
                if 'symbol' not in df.columns and 'ticker' in df.columns:
                    df = df.rename(columns={'ticker': 'symbol'})
                if 'name' not in df.columns and 'title' in df.columns:
                    df = df.rename(columns={'title': 'name'})
            
            return df
            
        except requests.RequestException as e:
            print(f"Error fetching tickers from URL: {e}")
            return None
        except Exception as e:
            print(f"Error processing ticker data: {e}")
            return None
    
    def update_database(self, force: bool = False) -> bool:
        """
        Download and store tickers in database
        
        Args:
            force: Force update even if cache exists
        
        Returns:
            True if successful, False otherwise
        """
        try:
            # Check cache first
            if not force:
                cached_data = get_cache(self.cache_key)
                if cached_data:
                    print("Using cached ticker data")
                    return self._load_from_json(cached_data)
            
            # Fetch fresh data
            df = self.fetch_tickers_from_url()
            if df is None or df.empty:
                print("Failed to fetch ticker data")
                return False
            
            # Cache the JSON
            set_cache(self.cache_key, df.to_json(orient='records'), self.cache_ttl)
            
            # Store in database
            return self._store_to_database(df)
            
        except Exception as e:
            print(f"Error updating ticker database: {e}")
            return False
    
    def _load_from_json(self, json_str: str) -> bool:
        """Load ticker data from JSON string"""
        try:
            data = json.loads(json_str)
            df = pd.DataFrame(data)
            return self._store_to_database(df)
        except Exception as e:
            print(f"Error loading from JSON: {e}")
            return False
    
    def _store_to_database(self, df: pd.DataFrame) -> bool:
        """Store ticker data in SQLite database"""
        try:
            conn = get_db_connection()
            
            # Add last_updated timestamp
            df['last_updated'] = datetime.now().isoformat()
            df['is_active'] = df.get('is_active', True)
            
            # Fill NaN values with None for optional fields
            optional_cols = ['exchange', 'category', 'sector', 'industry']
            for col in optional_cols:
                if col not in df.columns:
                    df[col] = None
                else:
                    df[col] = df[col].fillna(value=pd.NA)
            
            # Write to database
            df.to_sql('tickers', conn, if_exists='replace', index=False)
            
            conn.close()
            print(f"Successfully stored {len(df)} tickers in database")
            return True
            
        except Exception as e:
            print(f"Error storing tickers in database: {e}")
            return False
    
    def search_tickers(self, query: str, limit: int = 20) -> pd.DataFrame:
        """
        Search for tickers by symbol or name
        
        Args:
            query: Search query (symbol or company name)
            limit: Maximum results to return
        
        Returns:
            DataFrame with matching tickers
        """
        try:
            conn = get_db_connection()
            
            sql = '''
                SELECT symbol, name, exchange, category, sector, industry, is_active
                FROM tickers
                WHERE (symbol LIKE ? OR name LIKE ?)
                AND is_active = 1
                ORDER BY 
                    CASE 
                        WHEN symbol LIKE ? THEN 0
                        ELSE 1
                    END,
                    LENGTH(symbol) ASC
                LIMIT ?
            '''
            
            pattern = f"%{query}%"
            results = pd.read_sql_query(
                sql, 
                conn, 
                params=(pattern, pattern, f"{query}%", limit)
            )
            conn.close()
            return results
            
        except Exception as e:
            print(f"Error searching tickers: {e}")
            return pd.DataFrame()
    
    def get_all_tickers(self) -> List[str]:
        """
        Get all active ticker symbols as list
        
        Returns:
            List of ticker symbols
        """
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT symbol FROM tickers 
                WHERE is_active = 1
                ORDER BY symbol
            ''')
            
            tickers = [row[0] for row in cursor.fetchall()]
            conn.close()
            return tickers
            
        except Exception as e:
            print(f"Error retrieving tickers: {e}")
            return []
    
    def get_ticker_by_symbol(self, symbol: str) -> Optional[dict]:
        """
        Get detailed information for a specific ticker
        
        Args:
            symbol: Ticker symbol
        
        Returns:
            Dictionary with ticker details or None
        """
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM tickers 
                WHERE symbol = ? AND is_active = 1
            ''', (symbol.upper(),))
            
            row = cursor.fetchone()
            conn.close()
            
            if row:
                return dict(row)
            return None
            
        except Exception as e:
            print(f"Error retrieving ticker {symbol}: {e}")
            return None
    
    def get_tickers_by_sector(self, sector: str) -> pd.DataFrame:
        """
        Get all tickers in a specific sector
        
        Args:
            sector: Sector name
        
        Returns:
            DataFrame with tickers in that sector
        """
        try:
            conn = get_db_connection()
            
            sql = '''
                SELECT symbol, name, exchange, category, sector, industry
                FROM tickers
                WHERE sector = ? AND is_active = 1
                ORDER BY symbol
            '''
            
            results = pd.read_sql_query(sql, conn, params=(sector,))
            conn.close()
            return results
            
        except Exception as e:
            print(f"Error retrieving tickers by sector: {e}")
            return pd.DataFrame()
    
    def get_ticker_count(self) -> int:
        """Get total count of active tickers"""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT COUNT(*) FROM tickers WHERE is_active = 1')
            count = cursor.fetchone()[0]
            conn.close()
            return count
            
        except Exception as e:
            print(f"Error getting ticker count: {e}")
            return 0


if __name__ == "__main__":
    # Example usage
    manager = TickerManager("https://your-url/tickers.json")
    manager.update_database(force=True)
    
    # Search example
    results = manager.search_tickers("apple")
    print(results)
    
    # Get all tickers
    all_tickers = manager.get_all_tickers()
    print(f"Total tickers: {len(all_tickers)}")
