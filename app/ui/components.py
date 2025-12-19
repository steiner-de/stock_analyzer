"""
Reusable UI components for Stock Analyzer
"""

from shiny import ui
from config.theme import COLORS, SPACING, TYPOGRAPHY, BORDER_RADIUS


def card(
    *args,
    title: str|None = None,
    subtitle: str|None = None,
    class_: str = "",
    style: str = "",
    **kwargs
):
    """
    Create a styled card component
    
    Args:
        *args: Card content
        title: Card title
        subtitle: Card subtitle
        class_: Additional CSS classes
        style: Additional inline styles
        **kwargs: Additional card arguments
    
    Returns:
        Shiny card element
    """
    header_content = []
    
    if title:
        header_content.append(
            ui.div(
                ui.h3(title, style=f"margin: 0; color: {COLORS['dark']};"),
                style=f"margin-bottom: {SPACING['sm']};"
            )
        )
    
    if subtitle:
        header_content.append(
            ui.div(
                ui.p(
                    subtitle,
                    style=f"margin: 0; color: {COLORS['gray']}; font-size: {TYPOGRAPHY['font_size_sm']};"
                ),
                style=f"margin-bottom: {SPACING['md']};"
            )
        )
    
    card_style = f"""
        background: {COLORS['white']};
        border: 1px solid #E0E0E0;
        border-radius: {BORDER_RADIUS['lg']};
        padding: {SPACING['lg']};
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    """
    
    if style:
        card_style += style
    
    return ui.div(
        *header_content,
        *args,
        style=card_style,
        class_=class_,
        **kwargs
    )


def button_primary(label: str, id_: str = "", **kwargs):
    """Create a primary button"""
    return ui.input_action_button(
        id_,
        label,
        class_="btn btn-primary w-100",
        style=f"""
            background-color: {COLORS['primary']};
            border: none;
            padding: {SPACING['sm']} {SPACING['lg']};
            font-weight: 600;
            border-radius: {BORDER_RADIUS['md']};
        """,
        **kwargs
    )


def button_secondary(label: str, id_: str = "", **kwargs):
    """Create a secondary button"""
    return ui.input_action_button(
        id_,
        label,
        class_="btn btn-secondary w-100",
        style=f"""
            background-color: {COLORS['secondary']};
            border: none;
            padding: {SPACING['sm']} {SPACING['lg']};
            font-weight: 600;
            border-radius: {BORDER_RADIUS['md']};
        """,
        **kwargs
    )


def stat_box(label: str, value: str, icon: str = "📊"):
    """
    Create a statistics box component
    
    Args:
        label: Stat label
        value: Stat value
        icon: Icon/emoji
    
    Returns:
        Styled stat box
    """
    return card(
        ui.div(
            ui.div(
                icon,
                style=f"font-size: {TYPOGRAPHY['font_size_3xl']}; margin-bottom: {SPACING['md']};"
            ),
            ui.div(
                label,
                style=f"color: {COLORS['gray']}; font-size: {TYPOGRAPHY['font_size_sm']}; margin-bottom: {SPACING['sm']};"
            ),
            ui.div(
                value,
                style=f"color: {COLORS['dark']}; font-size: {TYPOGRAPHY['font_size_2xl']}; font-weight: 700;"
            ),
            style=f"text-align: center;"
        ),
        class_="stat-box"
    )


def metric_grid(*metrics, class_: str = ""):
    """
    Create a grid of metric boxes
    
    Args:
        *metrics: Metric components
        class_: Additional CSS classes
    
    Returns:
        Grid layout
    """
    return ui.div(
        *metrics,
        class_=f"row g-4 {class_}",
        style=f"display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: {SPACING['lg']};"
    )


def section_header(title: str, subtitle: str|None = None):
    """
    Create a section header
    
    Args:
        title: Section title
        subtitle: Optional subtitle
    
    Returns:
        Section header element
    """
    return ui.div(
        ui.h2(title, style=f"color: {COLORS['dark']}; margin-bottom: {SPACING['sm']};"),
        ui.p(
            subtitle or "",
            style=f"color: {COLORS['gray']}; margin: 0;"
        ) if subtitle else None,
        style=f"margin-bottom: {SPACING['lg']}; border-bottom: 2px solid {COLORS['primary']}; padding-bottom: {SPACING['md']};"
    )


def loading_spinner(message: str = "Loading..."):
    """Create a loading spinner"""
    return ui.div(
        ui.div(
            style="display: inline-block; width: 40px; height: 40px; border: 4px solid #f3f3f3; border-top: 4px solid " + COLORS['primary'] + "; border-radius: 50%; animation: spin 1s linear infinite;"
        ),
        ui.p(message, style=f"color: {COLORS['gray']}; margin-top: {SPACING['md']};"),
        style="text-align: center; padding: " + SPACING['xl'] + ";",
    )


def alert(message: str, alert_type: str = "info", dismissible: bool = True):
    """
    Create an alert component
    
    Args:
        message: Alert message
        alert_type: Type of alert ('success', 'danger', 'warning', 'info')
        dismissible: Whether alert is dismissible
    
    Returns:
        Alert element
    """
    alert_colors = {
        "success": COLORS["success"],
        "danger": COLORS["danger"],
        "warning": COLORS["warning"],
        "info": COLORS["info"],
    }
    
    return ui.div(
        message,
        class_=f"alert alert-{alert_type}" + (" alert-dismissible fade show" if dismissible else ""),
        style=f"""
            background-color: {alert_colors.get(alert_type, COLORS['info'])}20;
            border: 1px solid {alert_colors.get(alert_type, COLORS['info'])};
            border-radius: {BORDER_RADIUS['md']};
            padding: {SPACING['md']};
            color: {alert_colors.get(alert_type, COLORS['info'])};
        """
    )
