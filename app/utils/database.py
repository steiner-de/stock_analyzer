"""
Database initialization and management for Stock Analyzer
"""

import sqlite3
from pathlib import Path
from datetime import datetime
from config.settings import get_data_path


DB_PATH = Path(get_data_path()) / "stock_analyzer.db"


def get_db_connection():
    """Get a database connection"""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize database with required tables"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create tickers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT UNIQUE NOT NULL,
            name TEXT,
            exchange TEXT,
            category TEXT,
            sector TEXT,
            industry TEXT,
            last_updated TIMESTAMP,
            is_active BOOLEAN DEFAULT 1
        )
    ''')
    
    # Create index for faster searches
    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_symbol ON tickers(symbol)
    ''')
    
    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_name ON tickers(name)
    ''')
    
    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_active ON tickers(is_active)
    ''')
    
    # Create cache table for storing API responses
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cache (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE NOT NULL,
            value TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP
        )
    ''')
    
    # Create index for cache
    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_cache_key ON cache(key)
    ''')
    
    conn.commit()
    conn.close()


def get_cache(key: str) -> str | None:
    """Retrieve value from cache if not expired"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT value FROM cache
        WHERE key = ? AND (expires_at IS NULL OR expires_at > datetime('now'))
    ''', (key,))
    
    result = cursor.fetchone()
    conn.close()
    
    return result[0] if result else None


def set_cache(key: str, value: str, ttl_hours: int = 24) -> None:
    """Store value in cache with optional TTL"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    expires_at = None
    if ttl_hours:
        from datetime import timedelta
        expires_at = (datetime.now() + timedelta(hours=ttl_hours)).isoformat()
    
    cursor.execute('''
        INSERT OR REPLACE INTO cache (key, value, created_at, expires_at)
        VALUES (?, ?, datetime('now'), ?)
    ''', (key, value, expires_at))
    
    conn.commit()
    conn.close()


def clear_cache(key: str|None = None) -> None:
    """Clear cache entries"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if key:
        cursor.execute('DELETE FROM cache WHERE key = ?', (key,))
    else:
        cursor.execute('DELETE FROM cache')
    
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print(f"Database initialized at {DB_PATH}")
