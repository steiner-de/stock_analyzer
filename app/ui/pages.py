"""
UI pages and components for Stock Analyzer
"""

from shiny import ui
from config import APP_NAME, COLORS, SPACING
from ui.components import (
    card,
    button_primary,
    section_header,
    stat_box,
    metric_grid,
    alert,
)
from ui.styles import GLOBAL_CSS


def create_ui():
    """Create the main UI for the Shiny app"""
    
    return ui.page_navbar(
        # Add global CSS to page header
        ui.head_content(
            ui.tags.style(GLOBAL_CSS),
            ui.tags.meta(name="viewport", content="width=device-width, initial-scale=1"),
        ),
        # Home page
        ui.nav_panel(
            "Home",
            ui.div(
                ui.div(
                    ui.h1(
                        APP_NAME,
                        style=f"color: {COLORS['primary']}; margin-bottom: {SPACING['md']};"
                    ),
                    ui.p(
                        "Comprehensive fundamental analysis with machine learning",
                        style=f"font-size: 1.25rem; color: {COLORS['gray']}; margin-bottom: {SPACING['lg']};"
                    ),
                    ui.div(
                        metric_grid(
                            stat_box("📊", "Real-time Data", "Live stock prices"),
                            stat_box("🤖", "ML Analysis", "Predictive models"),
                            stat_box("📈", "Technical", "200+ indicators"),
                        ),
                        style=f"margin-top: {SPACING['xl']};"
                    ),
                    style="text-align: center; padding: " + SPACING['2xl'] + ";",
                    class_="fade-in"
                ),
                style=f"background: linear-gradient(135deg, {COLORS['primary']}20 0%, {COLORS['info']}20 100%); border-radius: 1rem; margin-bottom: {SPACING['xl']};"
            ),
        ),
        
        # Analysis page
        ui.nav_panel(
            "Analysis",
            ui.div(
                section_header(
                    "Stock Fundamental Analysis",
                    "Enter a stock symbol to analyze valuations and key metrics"
                ),
                ui.layout_sidebar(
                    ui.sidebar(
                        ui.input_text(
                            "stock_symbol",
                            "Stock Symbol",
                            placeholder="e.g., AAPL"
                        ),
                        ui.input_date_range(
                            "date_range",
                            "Date Range",
                            start="2023-01-01",
                        ),
                        button_primary("Analyze", "analyze_btn"),
                        alert("Enter a valid stock symbol to get started", alert_type="info"),
                        width="300px",
                    ),
                    ui.div(
                        # SUMMARY CARD - Top Section
                        card(
                            ui.div(
                                ui.div(
                                    ui.h3(ui.output_text("summary_symbol"), style="margin: 0; display: inline;"),
                                    ui.span(
                                        ui.output_text("summary_name"),
                                        style=f"margin-left: {SPACING['md']}; color: {COLORS['gray']}; font-size: 0.95rem;"
                                    ),
                                    style="display: flex; align-items: center; gap: 1rem;"
                                ),
                                ui.div(
                                    ui.div(
                                        ui.span("Current Price:", style="font-weight: 600;"),
                                        ui.span(ui.output_text("summary_current_price"), style=f"color: {COLORS['primary']}; font-size: 1.25rem; font-weight: 700; margin-left: {SPACING['sm']};"),
                                        style=f"margin-bottom: {SPACING['md']};"
                                    ),
                                    ui.div(
                                        ui.span("Analysis Date:", style="font-weight: 600;"),
                                        ui.span(ui.output_text("summary_date"), style=f"margin-left: {SPACING['sm']};"),
                                        style=f"margin-bottom: {SPACING['md']};"
                                    ),
                                    style=f"margin-top: {SPACING['lg']};"
                                ),
                                style=f"padding: {SPACING['lg']};"
                            ),
                            title="Summary",
                            subtitle="Company overview"
                        ),
                        
                        # FINANCIAL METRICS CARD
                        card(
                            ui.div(
                                ui.div(
                                    ui.div(
                                        ui.span("P/E Ratio:", style="font-weight: 600; display: block;"),
                                        ui.span(ui.output_text("metric_pe"), style=f"color: {COLORS['primary']}; font-size: 1.15rem; font-weight: 600;"),
                                        style=f"padding: {SPACING['md']}; text-align: center; background: {COLORS['light']}; border-radius: var(--border-radius-md); margin-bottom: {SPACING['sm']};"
                                    ),
                                    ui.div(
                                        ui.span("EPS:", style="font-weight: 600; display: block;"),
                                        ui.span(ui.output_text("metric_eps"), style=f"color: {COLORS['primary']}; font-size: 1.15rem; font-weight: 600;"),
                                        style=f"padding: {SPACING['md']}; text-align: center; background: {COLORS['light']}; border-radius: var(--border-radius-md); margin-bottom: {SPACING['sm']};"
                                    ),
                                    ui.div(
                                        ui.span("Market Cap:", style="font-weight: 600; display: block;"),
                                        ui.span(ui.output_text("metric_market_cap"), style=f"color: {COLORS['primary']}; font-size: 1.15rem; font-weight: 600;"),
                                        style=f"padding: {SPACING['md']}; text-align: center; background: {COLORS['light']}; border-radius: var(--border-radius-md); margin-bottom: {SPACING['sm']};"
                                    ),
                                    ui.div(
                                        ui.span("Shares Outstanding:", style="font-weight: 600; display: block;"),
                                        ui.span(ui.output_text("metric_shares"), style=f"color: {COLORS['primary']}; font-size: 1.15rem; font-weight: 600;"),
                                        style=f"padding: {SPACING['md']}; text-align: center; background: {COLORS['light']}; border-radius: var(--border-radius-md); margin-bottom: {SPACING['sm']};"
                                    ),
                                    ui.div(
                                        ui.span("Dividend Yield:", style="font-weight: 600; display: block;"),
                                        ui.span(ui.output_text("metric_yield"), style=f"color: {COLORS['primary']}; font-size: 1.15rem; font-weight: 600;"),
                                        style=f"padding: {SPACING['md']}; text-align: center; background: {COLORS['light']}; border-radius: var(--border-radius-md); margin-bottom: {SPACING['sm']};"
                                    ),
                                    ui.div(
                                        ui.span("Dividend Per Share:", style="font-weight: 600; display: block;"),
                                        ui.span(ui.output_text("metric_dividend"), style=f"color: {COLORS['primary']}; font-size: 1.15rem; font-weight: 600;"),
                                        style=f"padding: {SPACING['md']}; text-align: center; background: {COLORS['light']}; border-radius: var(--border-radius-md); margin-bottom: {SPACING['sm']};"
                                    ),
                                    ui.div(
                                        ui.span("Sales Growth:", style="font-weight: 600; display: block;"),
                                        ui.span(ui.output_text("metric_sales_growth"), style=f"color: {COLORS['primary']}; font-size: 1.15rem; font-weight: 600;"),
                                        style=f"padding: {SPACING['md']}; text-align: center; background: {COLORS['light']}; border-radius: var(--border-radius-md); margin-bottom: {SPACING['sm']};"
                                    ),
                                    ui.div(
                                        ui.span("Gross Profit Margin:", style="font-weight: 600; display: block;"),
                                        ui.span(ui.output_text("metric_gross_margin"), style=f"color: {COLORS['primary']}; font-size: 1.15rem; font-weight: 600;"),
                                        style=f"padding: {SPACING['md']}; text-align: center; background: {COLORS['light']}; border-radius: var(--border-radius-md); margin-bottom: {SPACING['sm']};"
                                    ),
                                    ui.div(
                                        ui.span("EBITDA:", style="font-weight: 600; display: block;"),
                                        ui.span(ui.output_text("metric_ebitda"), style=f"color: {COLORS['primary']}; font-size: 1.15rem; font-weight: 600;"),
                                        style=f"padding: {SPACING['md']}; text-align: center; background: {COLORS['light']}; border-radius: var(--border-radius-md);"
                                    ),
                                    style=f"display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: {SPACING['md']};"
                                ),
                                style=f"padding: {SPACING['lg']};"
                            ),
                            title="Financial Metrics",
                            subtitle="Key performance indicators"
                        ),
                        
                        # VALUATIONS - 4 Cards in a Grid
                        ui.div(
                            ui.h3("Valuation Analysis", style=f"margin-bottom: {SPACING['lg']}; margin-top: {SPACING['xl']};"),
                            ui.div(
                                # 10-Year Cap Price Card
                                card(
                                    ui.div(
                                        ui.span("10-Year Cap Price", style="font-weight: 600; display: block; margin-bottom: 0.5rem;"),
                                        ui.span(ui.output_text("valuation_10yr_cap"), style=f"font-size: 1.75rem; font-weight: 700; color: {COLORS['success']};"),
                                        ui.p("The maximum price you should pay today", style=f"color: {COLORS['gray']}; font-size: 0.85rem; margin-top: {SPACING['sm']};"),
                                        style=f"text-align: center; padding: {SPACING['lg']};"
                                    ),
                                    style="border-left: 4px solid " + COLORS['success']
                                ),
                                # Fair Market Value Card
                                card(
                                    ui.div(
                                        ui.span("Fair Market Value", style="font-weight: 600; display: block; margin-bottom: 0.5rem;"),
                                        ui.span(ui.output_text("valuation_fair_value"), style=f"font-size: 1.75rem; font-weight: 700; color: {COLORS['info']};"),
                                        ui.p("Intrinsic value based on fundamentals", style=f"color: {COLORS['gray']}; font-size: 0.85rem; margin-top: {SPACING['sm']};"),
                                        style=f"text-align: center; padding: {SPACING['lg']};"
                                    ),
                                    style="border-left: 4px solid " + COLORS['info']
                                ),
                                # Payback Period Card
                                card(
                                    ui.div(
                                        ui.span("Payback Period", style="font-weight: 600; display: block; margin-bottom: 0.5rem;"),
                                        ui.span(ui.output_text("valuation_payback"), style=f"font-size: 1.75rem; font-weight: 700; color: {COLORS['warning']};"),
                                        ui.p("Years for earnings to recover investment", style=f"color: {COLORS['gray']}; font-size: 0.85rem; margin-top: {SPACING['sm']};"),
                                        style=f"text-align: center; padding: {SPACING['lg']};"
                                    ),
                                    style="border-left: 4px solid " + COLORS['warning']
                                ),
                                # Price to Buy Card
                                card(
                                    ui.div(
                                        ui.span("Recommended Buy Price", style="font-weight: 600; display: block; margin-bottom: 0.5rem;"),
                                        ui.span(ui.output_text("valuation_buy_price"), style=f"font-size: 1.75rem; font-weight: 700; color: {COLORS['primary']};"),
                                        ui.p("Target price for optimal entry point", style=f"color: {COLORS['gray']}; font-size: 0.85rem; margin-top: {SPACING['sm']};"),
                                        style=f"text-align: center; padding: {SPACING['lg']};"
                                    ),
                                    style="border-left: 4px solid " + COLORS['primary']
                                ),
                                style=f"display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: {SPACING['lg']};"
                            ),
                            style=f"margin-top: {SPACING['xl']};"
                        ),
                        
                        style=f"padding: {SPACING['lg']};"
                    )
                )
            )
        ),
        
        # Models page
        ui.nav_panel(
            "Models",
            ui.div(
                section_header(
                    "Machine Learning Models",
                    "Train and evaluate predictive models"
                ),
                metric_grid(
                    card(
                        ui.p("Random Forest"),
                        ui.p("Fast ensemble method for classification", style=f"color: {COLORS['gray']};"),
                        button_primary("Train", "train_rf"),
                        title="Random Forest"
                    ),
                    card(
                        ui.p("Neural Network"),
                        ui.p("Deep learning for complex patterns", style=f"color: {COLORS['gray']};"),
                        button_primary("Train", "train_nn"),
                        title="Neural Network"
                    ),
                    card(
                        ui.p("Gradient Boosting"),
                        ui.p("Sequential ensemble method", style=f"color: {COLORS['gray']};"),
                        button_primary("Train", "train_gb"),
                        title="Gradient Boosting"
                    ),
                )
            )
        ),
        
        # Data page
        ui.nav_panel(
            "Data",
            ui.div(
                section_header(
                    "Data Management",
                    "View and manage cached data"
                ),
                card(
                    ui.p("Cached Data"),
                    ui.output_text_verbatim("data_info"),
                    ui.br(),
                    button_primary("Refresh Cache", "refresh_cache"),
                    title="Cache Status"
                )
            )
        ),
        
        # Settings page
        ui.nav_panel(
            "Settings",
            ui.div(
                section_header(
                    "Application Settings",
                    "Configure application behavior"
                ),
                card(
                    ui.div(
                        ui.div(
                            ui.input_checkbox("debug_mode", "Enable debug logging"),
                            style="margin-bottom: 1.5rem;"
                        ),
                        ui.div(
                            ui.input_numeric("cache_ttl", "Cache expiration (hours)", value=24, min=1, max=168),
                            style="margin-bottom: 1.5rem;"
                        ),
                        ui.div(
                            ui.input_select(
                                "default_period",
                                "Historical data period",
                                {"1y": "1 Year", "5y": "5 Years", "10y": "10 Years", "max": "All Time"}
                            ),
                            style="margin-bottom: 1.5rem;"
                        ),
                        button_primary("Save Settings", "save_settings"),
                    ),
                    title="Configuration"
                )
            )
        ),
        
        title=APP_NAME,
        navbar_options=ui.navbar_options(
            inverse=False,
            position="fixed-top"
        ),
        theme=None,
    )
