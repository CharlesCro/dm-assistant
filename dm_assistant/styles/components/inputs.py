from ..tokens import ThemeColors

PRIMARY_BUTTON = {
    "background_color": ThemeColors.PRIMARY,
    "color": "white",
    "_hover": {
        "background_color": ThemeColors.PRIMARY_HOVER,
    },
}

FLOATING_LINK_BUTTON = {
    **PRIMARY_BUTTON,
    "position": "fixed",
    "bottom": "2rem",
    "right": "2rem",
    "box_shadow": "0 4px 12px rgba(0,0,0,0.3)",
}