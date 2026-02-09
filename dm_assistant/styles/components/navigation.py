from ..tokens import ThemeColors, Spacing

SIDEBAR_CONTAINER = {
    "width": Spacing.SIDEBAR_WIDTH,
    "height": "100vh",
    "background_color": ThemeColors.BG_SURFACE,
    "border_right": ThemeColors.BORDER_SUBTLE,
    "padding": Spacing.MD,
}

# Base style to reduce repetition
BASE_NAV = {
    "width": "100%",
    "padding": f"{Spacing.SM} {Spacing.MD}",
    "cursor": "pointer",
    "transition": "color 0.2s ease", # Smooth color transition
}

NAV_ITEM_HOME = {
    **BASE_NAV,
    "color": ThemeColors.DARK_INK,
    "_hover": {"color": "crimson"},
}

NAV_ITEM_CHAT = {
    **BASE_NAV,
    "color": ThemeColors.DARK_INK,
    "_hover": {"color": "orange"},
}

NAV_ITEM_SETTINGS = {
    **BASE_NAV,
    "color": ThemeColors.DARK_INK,
    "_hover": {"color": "#3E63DD"},
}


NAV_ITEM_LOGOUT = {
    **BASE_NAV,
    "color": ThemeColors.DARK_INK,
    "_hover": {"color": "green"}, # Logout now turns grass on hover
}

# Used for the generic logout box
NAV_ITEM = {
    **BASE_NAV,
    "color": ThemeColors.DARK_INK,
    "_hover": {
        "background_color": ThemeColors.BG_OVERLAY,
        "color": "crimson",
    },
}
