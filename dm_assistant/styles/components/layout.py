# app/styles/components/layout.py
from ..tokens import ThemeColors, Spacing

BASE_LAYOUT_CONTAINER = {
    "min_height": "100vh",
    "width": "100%",
}

# app/styles/components/layout.py

DASHBOARD_HSTACK = {
    "width": "100%",
    "height": "100vh", # Lock to viewport height
    "background_color": ThemeColors.BG_PAGE,
    "overflow": "hidden", # Prevent the whole page from scrolling
}

CONTENT_AREA = {
    # "padding": Spacing.LG,
    "flex": "1", # Grow to fill remaining space next to sidebar
    "height": "100vh", # Match the viewport
    "overflow_y": "auto", # Allow scrolling ONLY inside the content area
    "display": "flex",
    "flex_direction": "column",
    # "align_items": "center", # Removed this to allow chat to fill width
}