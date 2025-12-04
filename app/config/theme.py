"""
UI theme and styling configuration for Stock Analyzer
"""

# Color palette - Modern, professional theme
COLORS = {
    # Primary colors
    "primary": "#0066CC",      # Blue
    "secondary": "#6C757D",    # Gray
    "success": "#28A745",      # Green
    "warning": "#FFC107",      # Amber
    "danger": "#DC3545",       # Red
    "info": "#17A2B8",         # Cyan
    
    # Neutral colors
    "white": "#FFFFFF",
    "light": "#F8F9FA",
    "dark": "#212529",
    "gray": "#6C757D",
    
    # Chart colors
    "chart_blue": "#1f77b4",
    "chart_orange": "#ff7f0e",
    "chart_green": "#2ca02c",
    "chart_red": "#d62728",
    "chart_purple": "#9467bd",
    "chart_brown": "#8c564b",
    
    # Stock specific
    "bullish": "#00B050",      # Green for up
    "bearish": "#FF0000",      # Red for down
}

# Typography
TYPOGRAPHY = {
    "font_family": "system-ui, -apple-system, sans-serif",
    "font_size_xs": "0.75rem",
    "font_size_sm": "0.875rem",
    "font_size_base": "1rem",
    "font_size_lg": "1.125rem",
    "font_size_xl": "1.25rem",
    "font_size_2xl": "1.5rem",
    "font_size_3xl": "1.875rem",
    "font_size_4xl": "2.25rem",
}

# Spacing
SPACING = {
    "xs": "0.25rem",
    "sm": "0.5rem",
    "md": "1rem",
    "lg": "1.5rem",
    "xl": "2rem",
    "2xl": "3rem",
}

# Breakpoints
BREAKPOINTS = {
    "xs": "0px",
    "sm": "576px",
    "md": "768px",
    "lg": "992px",
    "xl": "1200px",
    "2xl": "1400px",
}

# Border radius
BORDER_RADIUS = {
    "sm": "0.25rem",
    "md": "0.375rem",
    "lg": "0.5rem",
    "xl": "1rem",
    "full": "9999px",
}

# Shadows
SHADOWS = {
    "sm": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
    "md": "0 4px 6px -1px rgba(0, 0, 0, 0.1)",
    "lg": "0 10px 15px -3px rgba(0, 0, 0, 0.1)",
    "xl": "0 20px 25px -5px rgba(0, 0, 0, 0.1)",
}

# Button styles
BUTTON_STYLES = {
    "primary": {
        "background": COLORS["primary"],
        "color": COLORS["white"],
        "border": "none",
        "padding": f"{SPACING['sm']} {SPACING['lg']}",
        "border_radius": BORDER_RADIUS["md"],
        "font_weight": "600",
        "cursor": "pointer",
    },
    "secondary": {
        "background": COLORS["secondary"],
        "color": COLORS["white"],
        "border": "none",
        "padding": f"{SPACING['sm']} {SPACING['lg']}",
        "border_radius": BORDER_RADIUS["md"],
        "font_weight": "600",
        "cursor": "pointer",
    },
    "outline": {
        "background": "transparent",
        "color": COLORS["primary"],
        "border": f"2px solid {COLORS['primary']}",
        "padding": f"{SPACING['sm']} {SPACING['lg']}",
        "border_radius": BORDER_RADIUS["md"],
        "font_weight": "600",
        "cursor": "pointer",
    },
}

# Card styles
CARD_STYLES = {
    "background": COLORS["white"],
    "border": f"1px solid #E0E0E0",
    "border_radius": BORDER_RADIUS["lg"],
    "padding": SPACING["lg"],
    "box_shadow": SHADOWS["sm"],
}

# Input styles
INPUT_STYLES = {
    "background": COLORS["white"],
    "border": f"1px solid #D0D0D0",
    "border_radius": BORDER_RADIUS["md"],
    "padding": f"{SPACING['sm']} {SPACING['md']}",
    "font_size": TYPOGRAPHY["font_size_base"],
    "font_family": TYPOGRAPHY["font_family"],
}

# Theme configuration
THEME = {
    "colors": COLORS,
    "typography": TYPOGRAPHY,
    "spacing": SPACING,
    "breakpoints": BREAKPOINTS,
    "border_radius": BORDER_RADIUS,
    "shadows": SHADOWS,
    "button_styles": BUTTON_STYLES,
    "card_styles": CARD_STYLES,
    "input_styles": INPUT_STYLES,
}
