import reflex as rx

class ThemeColors:
    # Core aesthetic variables (mapped to globals.css)
    BG_PAGE = "var(--bg-page)"        # Aged paper/parchment
    BG_SURFACE = "var(--bg-surface)"  # Lighter paper for cards
    BG_OVERLAY = "var(--bg-overlay)"  # Translucent ink wash
    
    TEXT_MAIN = "var(--text-main)"    # Deep charcoal/ink
    TEXT_MUTED = "var(--text-muted)"  # Faded ink
    
    # Chat-specific colors
    CHAT_USER_BUBBLE = "var(--bg-surface)"  # User as "written notes"
    CHAT_AI_BUBBLE = "rgba(218, 165, 32, 0.1)" # AI as "magical/golden glow"
    
    PRIMARY = rx.color("crimson", 12)
    PRIMARY_HOVER = rx.color("crimson", 4)
    BORDER_SUBTLE = "2px solid var(--text-muted)"
    ANCIENT_GOLD = rx.color("gold", 9)
    # Aliases for compatibility
    DARK_INK = TEXT_MAIN
    FADED_INK = TEXT_MUTED

class Spacing:
    ZERO = "0"
    XS = "0.5rem"
    SM = "0.75rem"
    MD = "1rem"
    LG = "1.5rem"
    XL = "2rem"
    SIDEBAR_WIDTH = "20rem"
    NAVBAR_HEIGHT = "4rem"
    MAX_WIDTH = "1200px"