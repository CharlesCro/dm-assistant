import reflex as rx
from reflex_google_auth import google_login, google_oauth_provider
from ..styles.tokens import ThemeColors, Spacing
from ..styles.typography import Typography
from ..styles.components.inputs import AUTH_CARD_STYLE

def my_login_page():
    return rx.center(
        rx.vstack(
            # Thematic Header
            rx.heading(
                "Identify Thyself", 
                size="8", 
                margin_bottom=Spacing.MD
            ),
            rx.text(
                "Enter the chronicles to continue your quest.", 
                font_family=Typography.BODY_FONT,
                italic=True,
                color=ThemeColors.TEXT_MUTED,
                margin_bottom=Spacing.LG,
            ),
            
            # The "Scroll" Card
            rx.vstack(
                rx.text(
                    "Sign in with the Order of Google", 
                    font_family=Typography.HEADING_FONT,
                    font_size=Typography.SIZE_SM,
                    letter_spacing="0.1em",
                ),
                rx.divider(border_color=ThemeColors.TEXT_MUTED, width="50%"),
                
                # The Auth Component
                rx.box(
                    google_oauth_provider(
                        google_login(),
                    ),
                    # We wrap it in a box to desaturate/style the button if needed
                    padding_top=Spacing.MD,
                ),
                
                style=AUTH_CARD_STYLE,
                align="center",
                spacing="4",
                width="100%",
                max_width="450px",
            ),
            
            # Decorative Footer
            rx.text(
                "Property of the High Archives",
                font_family=Typography.HEADING_FONT,
                font_size="10px",
                margin_top=Spacing.XL,
                opacity=0.6,
                letter_spacing="2px",
            ),
            
            spacing="2",
            align="center",
        ),
        width="100%",
        height="100vh",
        background_color=ThemeColors.BG_PAGE,
        # Optional: Add a subtle paper texture overlay
        background_image="url('/paper-texture.png')", 
    )