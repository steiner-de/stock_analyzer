"""
Visualization utilities for Stock Analyzer
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Optional, Dict, List


def plot_price_history(data: pd.DataFrame, title: str = "Stock Price History") -> go.Figure:
    """
    Plot historical stock prices with Plotly (interactive)
    
    Args:
        data: DataFrame with Date and Close columns
        title: Plot title
    
    Returns:
        Plotly figure
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data["Date"],
        y=data["Close"],
        mode='lines',
        name='Close Price',
        line=dict(color='#1f77b4', width=2)
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Price ($)",
        hovermode='x unified',
        template='plotly_white',
        height=500
    )
    
    return fig


def plot_returns_distribution(data: pd.DataFrame, title: str = "Daily Returns Distribution") -> go.Figure:
    """
    Plot distribution of daily returns with Plotly
    
    Args:
        data: DataFrame with Close column
        title: Plot title
    
    Returns:
        Plotly figure
    """
    returns = data["Close"].pct_change().dropna()
    
    fig = go.Figure(data=[go.Histogram(
        x=returns,
        nbinsx=50,
        name='Returns',
        marker_color='#1f77b4'
    )])
    
    fig.add_vline(x=returns.mean(), line_dash="dash", line_color="red",
                  annotation_text=f"Mean: {returns.mean():.4f}")
    
    fig.update_layout(
        title=title,
        xaxis_title="Daily Return",
        yaxis_title="Frequency",
        hovermode='x',
        template='plotly_white',
        height=500
    )
    
    return fig


def plot_technical_indicators(data: pd.DataFrame, indicators: Dict[str, List[float]]) -> go.Figure:
    """
    Plot stock price with technical indicators using Plotly
    
    Args:
        data: DataFrame with Date and Close columns
        indicators: Dictionary of indicator names and values
    
    Returns:
        Plotly figure with secondary y-axis
    """
    fig = go.Figure()
    
    # Add price on primary y-axis
    fig.add_trace(go.Scatter(
        x=data["Date"],
        y=data["Close"],
        name="Close Price",
        line=dict(color='#1f77b4', width=2),
        yaxis='y'
    ))
    
    # Add indicators on secondary y-axis
    colors = ['#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
    for i, (name, values) in enumerate(indicators.items()):
        fig.add_trace(go.Scatter(
            x=data["Date"],
            y=values,
            name=name,
            line=dict(color=colors[i % len(colors)]),
            yaxis='y2',
            opacity=0.7
        ))
    
    fig.update_layout(
        title="Stock Price with Technical Indicators",
        xaxis_title="Date",
        yaxis=dict(title="Price ($)", side='left'),
        yaxis2=dict(title="Indicator Value", overlaying='y', side='right'),
        hovermode='x unified',
        template='plotly_white',
        height=600
    )
    
    return fig


def plot_model_performance(train_scores: List[float], test_scores: List[float], 
                          title: str = "Model Performance") -> go.Figure:
    """
    Plot model training and testing performance
    
    Args:
        train_scores: List of training scores
        test_scores: List of testing scores
        title: Plot title
    
    Returns:
        Plotly figure
    """
    epochs = list(range(1, len(train_scores) + 1))
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=epochs,
        y=train_scores,
        mode='lines+markers',
        name='Training Score',
        line=dict(color='#1f77b4'),
        marker=dict(size=6)
    ))
    
    fig.add_trace(go.Scatter(
        x=epochs,
        y=test_scores,
        mode='lines+markers',
        name='Testing Score',
        line=dict(color='#d62728'),
        marker=dict(size=6)
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title="Epoch",
        yaxis_title="Score",
        hovermode='x unified',
        template='plotly_white',
        height=500
    )
    
    return fig


def plot_candlestick(data: pd.DataFrame, title: str = "Candlestick Chart") -> go.Figure:
    """
    Plot candlestick chart for OHLC data
    
    Args:
        data: DataFrame with Date, Open, High, Low, Close columns
        title: Plot title
    
    Returns:
        Plotly candlestick figure
    """
    fig = go.Figure(data=[go.Candlestick(
        x=data["Date"],
        open=data["Open"],
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        name='OHLC'
    )])
    
    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Price ($)",
        template='plotly_white',
        height=500
    )
    
    return fig

