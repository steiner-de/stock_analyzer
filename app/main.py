"""
Main Shiny application for Stock Analyzer
"""

from shiny import App, ui, render
from app.ui.pages import create_ui
from app.server.handlers import create_server


def main():
    """Initialize and run the Shiny app"""
    app = App(create_ui(), create_server())
    return app


if __name__ == "__main__":
    app = main()
