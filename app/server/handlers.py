"""
Server-side handlers for Stock Analyzer
"""

from shiny import reactive, render, ui
from utils.data_loader import fetch_stock_data
from utils.analysis import analyze_fundamentals


# ==================== HELPER FUNCTIONS ====================

def format_currency(value, default="N/A"):
    """Format value as currency with $ and 2 decimals"""
    if value is None or (isinstance(value, float) and value != value):  # Check for NaN
        return default
    try:
        return f"${float(value):,.2f}"
    except (ValueError, TypeError):
        return default


def format_percentage(value, default="N/A"):
    """Format value as percentage"""
    if value is None or (isinstance(value, float) and value != value):
        return default
    try:
        percent_val = float(value) * 100 if float(value) < 1 else float(value)
        return f"{percent_val:.2f}%"
    except (ValueError, TypeError):
        return default


def format_number(value, default="N/A"):
    """Format value as number with commas"""
    if value is None or (isinstance(value, float) and value != value):
        return default
    try:
        return f"{float(value):,.0f}"
    except (ValueError, TypeError):
        return default


def format_decimal(value, decimals=2, default="N/A"):
    """Format value with specified decimal places"""
    if value is None or (isinstance(value, float) and value != value):
        return default
    try:
        return f"{float(value):.{decimals}f}"
    except (ValueError, TypeError):
        return default


# ==================== HANDLER SETUP ====================

def setup_handlers(input, output, session):
    """Setup server-side handlers for the Shiny app"""
    
    # Reactive value to store analysis results
    analysis_results = reactive.Value(None)
    
    @reactive.Effect
    @reactive.event(input.analyze_btn)
    def _on_analyze():
        """Handle analysis button click"""
        symbol = input.stock_symbol()
        if symbol:
            try:
                # Fetch data
                data = fetch_stock_data(symbol)
                
                # Perform analysis
                results = analyze_fundamentals(data)
                
                # Store results in reactive value
                analysis_results.set(results)
                    
            except Exception as e:
                analysis_results.set({"error": str(e)})
    
    # ==================== SUMMARY OUTPUTS ====================
    
    @output
    @render.text
    def summary_symbol():
        """Display stock symbol"""
        results = analysis_results()
        if results and "summary" in results:
            return results["summary"].get("symbol", "N/A")
        return "—"
    
    @output
    @render.text
    def summary_name():
        """Display company name"""
        results = analysis_results()
        if results and "summary" in results:
            return results["summary"].get("company_name", "N/A")
        return "—"
    
    @output
    @render.text
    def summary_current_price():
        """Display current stock price"""
        results = analysis_results()
        if results and "summary" in results:
            price = results["summary"].get("current_price")
            return format_currency(price)
        return "—"
    
    @output
    @render.text
    def summary_date():
        """Display analysis date"""
        results = analysis_results()
        if results and "summary" in results:
            return results["summary"].get("analysis_date", "N/A")
        return "—"
    
    # ==================== METRICS OUTPUTS ====================
    
    @output
    @render.text
    def metric_pe():
        """Display P/E Ratio"""
        results = analysis_results()
        if results and "metrics" in results:
            pe = results["metrics"].get("pe_ratio")
            return format_decimal(pe) if pe else "—"
        return "—"
    
    @output
    @render.text
    def metric_eps():
        """Display EPS"""
        results = analysis_results()
        if results and "metrics" in results:
            eps = results["metrics"].get("eps")
            return format_currency(eps)
        return "—"
    
    @output
    @render.text
    def metric_market_cap():
        """Display Market Cap"""
        results = analysis_results()
        if results and "metrics" in results:
            cap = results["metrics"].get("market_cap")
            return format_currency(cap)
        return "—"
    
    @output
    @render.text
    def metric_shares():
        """Display Shares Outstanding"""
        results = analysis_results()
        if results and "metrics" in results:
            shares = results["metrics"].get("shares_outstanding")
            return format_number(shares)
        return "—"
    
    @output
    @render.text
    def metric_yield():
        """Display Dividend Yield"""
        results = analysis_results()
        if results and "metrics" in results:
            dividend_yield = results["metrics"].get("dividend_yield")
            return format_percentage(dividend_yield)
        return "—"
    
    @output
    @render.text
    def metric_dividend():
        """Display Dividend Per Share"""
        results = analysis_results()
        if results and "metrics" in results:
            dividend = results["metrics"].get("dividend_per_share")
            return format_currency(dividend)
        return "—"
    
    @output
    @render.text
    def metric_sales_growth():
        """Display Sales Growth"""
        results = analysis_results()
        if results and "metrics" in results:
            growth = results["metrics"].get("sales_growth")
            return format_percentage(growth)
        return "—"
    
    @output
    @render.text
    def metric_gross_margin():
        """Display Gross Profit Margin"""
        results = analysis_results()
        if results and "metrics" in results:
            margin = results["metrics"].get("gross_profit_margin")
            return format_percentage(margin)
        return "—"
    
    @output
    @render.text
    def metric_ebitda():
        """Display EBITDA"""
        results = analysis_results()
        if results and "metrics" in results:
            ebitda = results["metrics"].get("ebitda")
            return format_currency(ebitda)
        return "—"
    
    # ==================== VALUATION OUTPUTS ====================
    
    @output
    @render.text
    def valuation_10yr_cap():
        """Display 10-Year Cap Price"""
        results = analysis_results()
        if results and "valuations" in results:
            price = results["valuations"].get("ten_year_cap_price")
            return format_currency(price)
        return "—"
    
    @output
    @render.text
    def valuation_fair_value():
        """Display Fair Market Value"""
        results = analysis_results()
        if results and "valuations" in results:
            value = results["valuations"].get("fair_market_value")
            return format_currency(value)
        return "—"
    
    @output
    @render.text
    def valuation_payback():
        """Display Payback Period"""
        results = analysis_results()
        if results and "valuations" in results:
            years = results["valuations"].get("payback_period_years")
            if years is not None:
                return f"{format_decimal(years, 1)} years"
            return "—"
        return "—"
    
    @output
    @render.text
    def valuation_buy_price():
        """Display Recommended Buy Price"""
        results = analysis_results()
        if results and "valuations" in results:
            price = results["valuations"].get("price_to_buy")
            return format_currency(price)
        return "—"
    
    # ==================== OTHER HANDLERS ====================
    
    @reactive.Effect
    @reactive.event(input.refresh_cache)
    def _on_refresh_cache():
        """Handle cache refresh"""
        @output
        @render.text
        def data_info():
            return "Cache refreshed successfully"
    
    @reactive.Effect
    @reactive.event(input.save_settings)
    def _on_save_settings():
        """Handle settings save"""
        # Settings would be saved here
        pass
    
    @output
    @render.text
    def data_info():
        """Display data cache information"""
        return "No data cached yet. Load stock data to begin."
