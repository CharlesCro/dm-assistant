from ..tokens import ThemeColors, Spacing


PRIMARY_BUTTON = {
    "background_color": "transparent",
    "color": ThemeColors.TEXT_MAIN,
    "border": f"1px solid {ThemeColors.TEXT_MAIN}",
    "font_family": "Cinzel",
    "text_transform": "uppercase",
    "box_shadow": "2px 2px 0px rgba(0,0,0,0.2)",
    "_hover": {
        "background_color": ThemeColors.ANCIENT_GOLD,
        "color": "white",
    },
}

FLOATING_LINK_BUTTON = {
    **PRIMARY_BUTTON,
    "position": "fixed",
    "bottom": "2rem",
    "right": "2rem",
    "box_shadow": "0 4px 12px rgba(0,0,0,0.3)",
}

CHAT_INPUT_STYLE = {
    "background_color": "rgba(0,0,0,0.05)",
    "border_bottom": f"0px solid {ThemeColors.TEXT_MAIN}",
    "border_top": "none",
    "border_left": "none",
    "border_right": "none",
    "border_radius": "0",
    # "padding": Spacing.SM,
    "font_family": "EB Garamond",
}

CHAT_BUBBLE_BASE = {
    "padding": Spacing.MD,
    "border_radius": "2px",
    "max_width": "80%",
    "box_shadow": "inset 0 0 10px rgba(0,0,0,0.05)",
    "border": f"1px solid {ThemeColors.TEXT_MUTED}",
}