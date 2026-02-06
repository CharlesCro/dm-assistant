import reflex as rx
from .tokens import ThemeColors
from .typography import Typography

base_theme = rx.theme(
    appearance="inherit", 
    accent_color="gold",
    gray_color="sand",
    radius="none",
)

STYLESHEET = [
    "https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=EB+Garamond:wght@400;600&display=swap",
    "/globals.css",
]

BASE_STYLE = {
    "font_family": Typography.BODY_FONT,
    "background_color": ThemeColors.BG_PAGE,
    "color": ThemeColors.TEXT_MAIN,
    
    rx.heading: {
        "font_family": Typography.HEADING_FONT,
        "color": ThemeColors.TEXT_MAIN,
        "text_transform": "uppercase",
        "letter_spacing": "0.05em",
    },
    rx.button: {
        "font_family": Typography.HEADING_FONT,
        "border_radius": "0", 
        # FIX: Changed from DARK_INK to TEXT_MAIN for dark mode support
        "border": f"1px solid {ThemeColors.TEXT_MAIN}",
        "box_shadow": "3px 3px 0px rgba(0,0,0,0.3)",
        "_active": {
            "box_shadow": "none",
            "transform": "translate(2px, 2px)",
        }
    }
}