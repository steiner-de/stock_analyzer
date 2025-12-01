"""
UI pages and components for Stock Analyzer
"""

from shiny import ui


def create_ui():
    """Create the main UI for the Shiny app"""
    return ui.page_navbar(
        ui.nav(
            "Home",
            ui.div(
                ui.h1("Stock Fundamental Analysis"),
                ui.p("Welcome to Stock Analyzer - Comprehensive fundamental analysis with machine learning"),
                class_="container mt-5"
            )
        ),
        ui.nav(
            "Analysis",
            ui.div(
                ui.layout_sidebar(
                    ui.sidebar(
                        ui.input_text("stock_symbol", "Stock Symbol", placeholder="e.g., AAPL"),
                        ui.input_date_range("date_range", "Date Range"),
                        ui.input_action_button("analyze_btn", "Analyze", class_="btn btn-primary w-100 mt-3"),
                    ),
                    ui.div(
                        ui.output_text_verbatim("analysis_output"),
                        class_="p-3"
                    )
                ),
                class_="container-fluid mt-5"
            )
        ),
        ui.nav(
            "Models",
            ui.div(
                ui.h2("Machine Learning Models"),
                ui.p("Model management and training interface"),
                class_="container mt-5"
            )
        ),
        ui.nav(
            "Data",
            ui.div(
                ui.h2("Data Management"),
                ui.p("View and manage cached data"),
                class_="container mt-5"
            )
        ),
        title="Stock Analyzer",
    )
