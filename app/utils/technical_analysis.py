"""
Technical analysis utilities using pandas_ta
"""

import pandas as pd
import pandas_ta as ta
from typing import Dict, Optional, List


def add_moving_averages(data: pd.DataFrame, short_window: int = 20, 
                        long_window: int = 50) -> pd.DataFrame:
    """
    Add moving averages to price data
    
    Args:
        data: DataFrame with Close column
        short_window: Short MA period
        long_window: Long MA period
    
    Returns:
        DataFrame with MA columns added
    """
    df = data.copy()
    
    df['SMA_' + str(short_window)] = ta.sma(df['Close'], length=short_window)
    df['SMA_' + str(long_window)] = ta.sma(df['Close'], length=long_window)
    df['EMA_' + str(short_window)] = ta.ema(df['Close'], length=short_window)
    df['EMA_' + str(long_window)] = ta.ema(df['Close'], length=long_window)
    
    return df


def add_rsi(data: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    """
    Add Relative Strength Index
    
    Args:
        data: DataFrame with Close column
        period: RSI period
    
    Returns:
        DataFrame with RSI column added
    """
    df = data.copy()
    df['RSI_' + str(period)] = ta.rsi(df['Close'], length=period)
    return df


def add_macd(data: pd.DataFrame, fast: int = 12, slow: int = 26, 
             signal: int = 9) -> pd.DataFrame:
    """
    Add MACD indicator
    
    Args:
        data: DataFrame with Close column
        fast: Fast EMA period
        slow: Slow EMA period
        signal: Signal line period
    
    Returns:
        DataFrame with MACD columns added
    """
    df = data.copy()
    
    macd_result = ta.macd(df['Close'], fast=fast, slow=slow, signal=signal)
    df = df.join(macd_result)
    
    return df


def add_bollinger_bands(data: pd.DataFrame, period: int = 20, 
                       std_dev: float = 2.0) -> pd.DataFrame:
    """
    Add Bollinger Bands
    
    Args:
        data: DataFrame with Close column
        period: MA period
        std_dev: Standard deviation multiplier
    
    Returns:
        DataFrame with Bollinger Bands columns added
    """
    df = data.copy()
    
    bb_result = ta.bbands(df['Close'], length=period, lower_std=std_dev)
    df = df.join(bb_result)
    
    return df


def add_atr(data: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    """
    Add Average True Range
    
    Args:
        data: DataFrame with High, Low, Close columns
        period: ATR period
    
    Returns:
        DataFrame with ATR column added
    """
    df = data.copy()
    
    df['ATR_' + str(period)] = ta.atr(
        df['High'], 
        df['Low'], 
        df['Close'], 
        length=period
    )
    
    return df


def add_stochastic(data: pd.DataFrame, k_period: int = 14, 
                   d_period: int = 3) -> pd.DataFrame:
    """
    Add Stochastic Oscillator
    
    Args:
        data: DataFrame with High, Low, Close columns
        k_period: K period
        d_period: D period (signal line)
    
    Returns:
        DataFrame with Stochastic columns added
    """
    df = data.copy()
    
    stoch_result = ta.stoch(
        df['High'],
        df['Low'],
        df['Close'],
        k=k_period,
        d=d_period
    )
    df = df.join(stoch_result)
    
    return df


# def calculate_all_indicators(data: pl.DataFrame) -> pl.DataFrame:
#     """
#     Calculate all common technical indicators
    
#     Args:
#         data: DataFrame with OHLC data
    
#     Returns:
#         DataFrame with all indicators
#     """
#     df = data.to_pandas() if isinstance(data, pl.DataFrame) else data
    
#     # Moving averages
#     df['SMA_20'] = ta.sma(df['Close'], length=20)
#     df['SMA_50'] = ta.sma(df['Close'], length=50)
#     df['EMA_12'] = ta.ema(df['Close'], length=12)
    
#     # Momentum indicators
#     df['RSI_14'] = ta.rsi(df['Close'], length=14)
#     macd_result = ta.macd(df['Close'], fast=12, slow=26, signal=9)
#     df = df.join(macd_result)
    
#     # Volatility
#     bb_result = ta.bbands(df['Close'], length=20, std=2)
#     df = df.join(bb_result)
    
#     # Volume-based (if Volume column exists)
#     if 'Volume' in df.columns:
#         df['OBV'] = ta.obv(df['Close'], df['Volume'])
    
#     # Trend
#     df['ATR_14'] = ta.atr(df['High'], df['Low'], df['Close'], length=14)
    
#     return pl.from_pandas(df) if isinstance(data, pl.DataFrame) else df


def get_signal_summary(data: pd.DataFrame) -> Dict[str, str]:
    """
    Generate trading signal summary from technical indicators
    
    Args:
        data: DataFrame with calculated indicators
    
    Returns:
        Dictionary with signal interpretations
    """
    df = data.dropna()
    
    if len(df) == 0:
        return {}
    
    latest = df.iloc[-1]
    signals = {}
    
    # RSI signal
    if 'RSI_14' in df.columns:
        rsi = latest['RSI_14']
        if rsi > 70:
            signals['RSI'] = 'Overbought'
        elif rsi < 30:
            signals['RSI'] = 'Oversold'
        else:
            signals['RSI'] = 'Neutral'
    
    # Moving average crossover
    if 'EMA_12' in df.columns and 'EMA_26' in df.columns:
        if latest['EMA_12'] > latest['EMA_26']:
            signals['EMA'] = 'Bullish'
        else:
            signals['EMA'] = 'Bearish'
    
    # Bollinger Bands
    bb_cols = [col for col in df.columns if col.startswith('BB')]
    if bb_cols:
        close = latest['Close']
        upper_col = [c for c in bb_cols if 'U' in c]
        lower_col = [c for c in bb_cols if 'L' in c]
        
        if upper_col and close > latest[upper_col[0]]:
            signals['BB'] = 'Above Upper Band'
        elif lower_col and close < latest[lower_col[0]]:
            signals['BB'] = 'Below Lower Band'
        else:
            signals['BB'] = 'Within Bands'
    
    return signals
