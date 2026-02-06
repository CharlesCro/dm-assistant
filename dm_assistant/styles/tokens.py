import reflex as rx

class ThemeColors:
    # We reference CSS variables that we will define in globals.css
    # This avoids the "rawColorMode" Javascript error entirely.
    
    BG_PAGE = "var(--bg-page)"
    BG_SURFACE = "var(--bg-surface)"
    BG_OVERLAY = "var(--bg-overlay)"
    
    TEXT_MAIN = "var(--text-main)"
    TEXT_MUTED = "var(--text-muted)"

    # These can stay as Radix colors as they handle themselves well
    PRIMARY = rx.color("crimson", 12)
    PRIMARY_HOVER = rx.color("crimson", 4)
    BORDER_SUBTLE = rx.color("sand", 10)
    ANCIENT_GOLD = rx.color("gold", 9)

    # Aliases for compatibility
    DARK_INK = TEXT_MAIN
    FADED_INK = TEXT_MUTED
    ANCIENT_GOLD = rx.color("gold", 9)

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