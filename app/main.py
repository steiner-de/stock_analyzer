"""
Stock Analyzer - Main Shiny Application
"""
from shiny import App
from ui.pages import create_ui
from server.handlers import setup_handlers
from config.settings import SHINY_CONFIG
from utils.database import init_db
from utils.ticker_manager import TickerManager

try:
    from config.secrets import TICKER_JSON_URL
except ImportError:
    # Fallback if secrets.py doesn't exist
    TICKER_JSON_URL = "https://www.sec.gov/files/company_tickers.json"


# Initialize database on startup
init_db()

# Initialize ticker data (update from SEC JSON URL)
ticker_manager = TickerManager(TICKER_JSON_URL)
ticker_manager.update_database()

# Create the main UI
app_ui = create_ui()
    
# Create the Shiny app
app = App(app_ui, server=setup_handlers)

if __name__ == "__main__":
    # Run the app with configured settings
    app.run(
        host=SHINY_CONFIG["host"],
        port=SHINY_CONFIG["port"],
        debug=SHINY_CONFIG["debug"],
        reload=SHINY_CONFIG["reload"],
    )
