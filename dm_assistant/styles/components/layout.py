# app/styles/components/layout.py
from ..tokens import ThemeColors, Spacing

BASE_LAYOUT_CONTAINER = {
    "min_height": "100vh",
    "width": "100%",
}

DASHBOARD_HSTACK = {
    "width": "100%",
    "min_height": "100vh",
    "background_color": ThemeColors.BG_PAGE,
}

CONTENT_AREA = {
    "padding": Spacing.LG,
    "width": "100%",
    "max_width": "800px",  # Rulebooks are usually narrow for readability
    "margin": "0 auto",    # Center the content like a book page
    "display": "flex",
    "flex_direction": "column",
    "align_items": "center",
    "text_align": "center",
}