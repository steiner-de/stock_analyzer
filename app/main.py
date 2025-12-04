"""
Stock Analyzer - Main Shiny Application
"""
from shiny import App
from ui.pages import create_ui
from server.handlers import setup_handlers
from config.settings import SHINY_CONFIG


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
