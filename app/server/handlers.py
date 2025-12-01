"""
Server-side handlers for Stock Analyzer
"""

from shiny import reactive
from app.utils.data_loader import fetch_stock_data
from app.utils.analysis import analyze_fundamentals


def create_server():
    """Create server-side functions for the Shiny app"""
    
    def server(input, output, session):
        """Server function with reactive logic"""
        
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
                    
                    output.analysis_output.set(
                        f"Analysis for {symbol}:\n{str(results)}"
                    )
                except Exception as e:
                    output.analysis_output.set(f"Error: {str(e)}")
    
    return server
