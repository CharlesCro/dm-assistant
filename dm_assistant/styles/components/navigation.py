from ..tokens import ThemeColors, Spacing

SIDEBAR_CONTAINER = {
    "width": Spacing.SIDEBAR_WIDTH,
    "height": "100vh",
    "background_color": ThemeColors.BG_SURFACE, # Dynamic color
    "border_right": f"2px solid {ThemeColors.BORDER_SUBTLE}",
    "padding": Spacing.MD,
}

NAV_ITEM = {
    "width": "100%",
    "padding": f"{Spacing.SM} {Spacing.MD}",
    "_hover": {
        "background_color": ThemeColors.BG_OVERLAY, # Dynamic hover
        "cursor": "pointer",
    },
}