"""
Fundamental analysis utilities for Stock Analyzer
"""
from edgar import Company, set_identity
import pandas as pd
from typing import Dict, Any, Optional
import os

# Initialize EdgarTools with SEC_EMAIL from environment variable
SEC_EMAIL = os.getenv("SEC_EMAIL", "your-email@example.com")
set_identity(SEC_EMAIL)

def analyze_fundamentals(
    stock_data: Dict[str, Any],
    current_price: Optional[float|None] = None
) -> Dict[str, Any]:
    """
    Perform comprehensive fundamental analysis on stock
    
    Args:
        stock_data: Dictionary with stock fundamental data (from yfinance ticker.info)
        current_price: Current stock price (optional)
    
    Returns:
        Dictionary with analysis results including valuations and metrics
    """
    
    results = {
        "valuations": {},
        "metrics": {},
        "summary": {}
    }
    
    # Convert stock_data to DataFrame 
    stock_df = pd.DataFrame([stock_data])
    
    # Extract current price from stock_data if not provided
    if current_price is None:
        current_price = stock_data.get("currentPrice") or stock_data.get("regularMarketPrice")
    
    # ==================== VALUATION CALCULATIONS ====================
    # 1. Calculate 10-Year Cap Price (TODO: Implement your logic)
    results["valuations"]["ten_year_cap_price"] = calculate_ten_year_cap_price(stock_data)
    
    # 2. Calculate Fair Market Value (TODO: Implement your logic)
    results["valuations"]["fair_market_value"] = calculate_fair_market_value(stock_data)
    
    # 3. Calculate Payback Period (Years until earnings pay back investor)
    results["valuations"]["discounted_cash_flow"] = calculate_discounted_cash_flow(stock_data)
    
    # 4. Calculate Price to Buy (Target entry price)
    results["valuations"]["price_to_buy"] = calculate_price_to_buy(stock_data)
    
    # ==================== KEY METRICS ====================
    results["metrics"]["market_cap"] = stock_data.get("marketCap")
    results["metrics"]["shares_outstanding"] = stock_data.get("sharesOutstanding")
    results["metrics"]["pe_ratio"] = stock_data.get("trailingPE")
    results["metrics"]["eps"] = stock_data.get("trailingEps")
    results["metrics"]["dividend_yield"] = stock_data.get("dividendYield")
    results["metrics"]["dividend_per_share"] = stock_data.get("dividendRate")
    results["metrics"]["sales_growth"] = stock_data.get("revenueGrowth")
    results["metrics"]["gross_profit_margin"] = stock_data.get("grossMargins")
    results["metrics"]["ebitda"] = stock_data.get("ebitda")
    results["metrics"]["pb_ratio"] = stock_data.get("priceToBook")
    results["metrics"]["debt_to_equity"] = stock_data.get("debtToEquity")
    results["metrics"]["current_ratio"] = stock_data.get("currentRatio")
    results["metrics"]["peg_ratio"] = stock_data.get("pegRatio")
    results["metrics"]["roe"] = stock_data.get("returnOnEquity")
    results["metrics"]["roa"] = stock_data.get("returnOnAssets")
    results["metrics"]["revenue_growth"] = stock_data.get("revenueGrowth")
    results["metrics"]["earnings_growth"] = stock_data.get("earningsGrowth")
    
    # ==================== SUMMARY ====================
    results["summary"]["analysis_date"] = pd.Timestamp.now().strftime("%Y-%m-%d")
    results["summary"]["current_price"] = current_price
    results["summary"]["symbol"] = stock_data.get("symbol", "N/A")
    results["summary"]["company_name"] = stock_data.get("longName", "N/A")
    
    return results


def calculate_ten_year_cap_price(stock_data: Dict[str, Any]) -> Optional[float]:
    """
    Calculate the 10-year cap price for the stock
    
    TODO: Implement your valuation logic here
    Examples:
    - PEG ratio based valuation
    - Earnings growth projected over 10 years
    - Discounted cash flow model
    
    Args:
        stock_data: Dictionary with stock data
    
    Returns:
        Calculated 10-year cap price or None
    """
    # Placeholder - implement your calculation
    pass


def calculate_fair_market_value(stock_data: Dict[str, Any]) -> Optional[float]:
    """
    Calculate the fair market value of the stock
    
    TODO: Implement your valuation logic here
    Examples:
    - Graham number formula
    - P/E ratio based on historical average
    - PEG ratio analysis
    - Intrinsic value models
    
    Args:
        stock_data: Dictionary with stock data
    
    Returns:
        Calculated fair market value or None
    """
    # Placeholder - implement your calculation
    pass


def calculate_discounted_cash_flow(stock_data: Dict[str, Any], 
                                   discount_rate: float=0.05) -> Optional[float]:
    """
    Calculate years until earnings pay back the investor
    
    TODO: Implement your calculation here
    Example formula: Current Price / EPS = Years for earnings to payback investment
    
    Args:
        stock_data: Dictionary with stock data
    
    Returns:
        Number of years or None
    """
    # Placeholder - implement your calculation
    pass


def calculate_price_to_buy(stock_data: Dict[str, Any],
                           desired_annual_return: float=0.15,
                           discount_price: float=0.5) -> Optional[float]:
    """
    Calculate the target price to buy the stock with a margin of safety
    
    TODO: Implement your target price logic here
    Examples:
    - Fair market value with safety margin (e.g., 20% discount)
    - Support level based on technical analysis
    - Value that provides margin of safety
    
    Args:
        stock_data: Dictionary with stock data
        desired_annual_return: Desired annual return rate
        discount_percentage: Margin of safety percentage
    
    Returns:
        Recommended buy price or None
    """
    # Placeholder - implement your calculation
    pass
def calculate_rate(period: str="annual",
                   timeframe: int=10,
                   present_value: float=0.0,
                   future_value: float=0.0) -> float:
    """
    Determine the number of periods in a year
    
    Args:
        period: Time period ("annual", "quarterly")
    
    Returns:
        Rate of return
    """
    if period == "annual":
        num_periods = 1 * timeframe
    elif period == "quarterly":
        num_periods = 4 * timeframe
    else:
        raise ValueError("Unsupported period type. Use 'annual' or 'quarterly'.")
    
    # Calcuate the growth rate
    return ((future_value / present_value) ** (1 / num_periods)) - 1

def calculate_growth_rates(company_ticker: str|None=None, 
                          period: str="annual",
                          currency: str="USD",
                          timeframe: int=10) -> dict:
    """
    Calculate growth rates for financial data
    
    Args:
        company_ticker: Ticker symbol of the company
        period: Time period ("annual", "quarterly")
        currency: Currency for financial data
        timeframe: Number of years for the growth rate calculation
    Returns:
        Dictionary with growth rates
    """
    if company_ticker is None:
        print("Company ticker is required for growth rate calculation.")
        return {}
    
    # Intialize Edgartools
    try:
        company = Company(company_ticker)
        
        # Fetch 10-K filings (annual reports)
        ten_ks = company.get_filings(form="10-K").latest(timeframe)
        
        # Extract financial data from filings
        financials = []
        for filing in ten_ks:
            try:
                income_stmt = filing.income_statement()
                balance_sheet = filing.balance_sheet()
                cash_flow = filing.cash_flow()
                
                # Calculate metrics from financial statements
                financials.append({
                    "period": filing.filing_date,
                    "revenue": income_stmt.get("revenues", 0) if income_stmt is not None else 0,
                    "net_income": income_stmt.get("net_income", 0) if income_stmt is not None else 0,
                    "total_assets": balance_sheet.get("assets", 0) if balance_sheet is not None else 0,
                    "total_liabilities": balance_sheet.get("liabilities", 0) if balance_sheet is not None else 0,
                    "operating_cash_flow": cash_flow.get("operating", 0) if cash_flow is not None else 0,
                })
            except Exception as e:
                print(f"Error extracting data from filing: {e}")
                continue
        
        # Calculate growth rates from historical data
        if len(financials) >= 2:
            # Sort by period (oldest first)
            financials = sorted(financials, key=lambda x: x["period"])
            
            # Calculate year-over-year growth rates
            growth_rates["growth_rates"]["sales"] = calculate_growth_rate(
                financials[-1]["revenue"], 
                financials[0]["revenue"], 
                timeframe
            )
            growth_rates["growth_rates"]["equity"] = calculate_growth_rate(
                financials[-1]["total_assets"] - financials[-1]["total_liabilities"],
                financials[0]["total_assets"] - financials[0]["total_liabilities"],
                timeframe
            )
            growth_rates["growth_rates"]["cash_flow"] = calculate_growth_rate(
                financials[-1]["operating_cash_flow"],
                financials[0]["operating_cash_flow"],
                timeframe
            )
    except Exception as e:
        print(f"Error fetching EdgarTools data for {company_ticker}: {e}")
    
    return growth_rates


def calculate_rate(period: str, timeframe: int) -> float:
    """
    Calculate rate of change
    
    Args:
        period: Time period type
        timeframe: Number of years
    
    Returns:
        Calculated rate as float
    """
    # Placeholder calculation - replace with your logic
    return 0.0


def calculate_growth_rate(current_value: float, prior_value: float, years: int) -> float:
    """
    Calculate compound annual growth rate (CAGR)
    
    Args:
        current_value: Current period value
        prior_value: Prior period value
        years: Number of years between periods
    
    Returns:
        CAGR as decimal (e.g., 0.15 for 15%)
    """
    if prior_value == 0 or years == 0:
        return 0.0
    
    try:
        cagr = ((current_value / prior_value) ** (1 / years)) - 1
        return round(cagr, 4)
    except (ValueError, ZeroDivisionError):
        return 0.0

def calculate_financial_ratios(income_stmt: pd.DataFrame, balance_sheet: pd.DataFrame) -> Dict[str, float]:
    """
    Calculate key financial ratios
    
    Args:
        income_stmt: Income statement data
        balance_sheet: Balance sheet data
    
    Returns:
        Dictionary with calculated ratios
    """
    # Placeholder for ratio calculations
    ratios = {
        "pe_ratio": 0.0,
        "pb_ratio": 0.0,
        "debt_to_equity": 0.0,
        "current_ratio": 0.0,
        "roa": 0.0,
        "roe": 0.0,
    }
    
    return ratios


def screen_stocks(data: pd.DataFrame, criteria: Dict[str, Any]) -> pd.DataFrame:
    """
    Filter stocks based on fundamental criteria
    
    Args:
        data: DataFrame with stock data
        criteria: Dictionary with screening criteria
    
    Returns:
        Filtered DataFrame
    """
    filtered = data
    
    for key, value in criteria.items():
        if key in filtered.columns:
            if isinstance(value, tuple):
                filtered = filtered[
                    (filtered[key] >= value[0]) & (filtered[key] <= value[1])
                ]
    
    return filtered
