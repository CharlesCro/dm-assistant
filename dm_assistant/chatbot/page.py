import reflex as rx
from ..ui.base import base_page
from ..styles import ThemeColors, Spacing, Typography
from .state import ChatState, ChatMessage

def message_bubble(message: ChatMessage) -> rx.Component:
    """Render a single chat message bubble with 75% transparency."""
    is_user = message.role == "user"
    
    # We define the transparent colors here. 
    # rgba(..., 0.25) provides 75% transparency.
    user_bg = "rgba(255, 248, 225, 0.25)" # Light parchment tint
    ai_bg = "rgba(218, 165, 32, 0.25)"   # Golden tint
    border_color = "rgba(0, 0, 0, 0.25)" # Faded ink border

    return rx.box(
        rx.hstack(
            rx.cond(
                ~is_user,
                rx.avatar(
                    fallback="🎲",
                    size="6",
                    radius="full",
                    color_scheme="gold",
                    margin_top="10px",
                ),
            ),
            
            rx.box(
                rx.cond(
                    is_user,
                    rx.text(
                        message.content,
                        color=ThemeColors.TEXT_MAIN,
                        font_size="1.5rem",
                        line_height="1.6",
                        white_space="pre-wrap",
                    ),
                    rx.markdown(
                        message.content,
                        color=ThemeColors.TEXT_MAIN,
                        style={
                            "font-size": "1.5rem",
                            "line-height": "1.6",
                        }
                    ),
                ),
                padding=Spacing.LG,
                border_radius="12px",
                max_width="75%",
                # Apply 75% transparency to background and border
                bg=rx.cond(is_user, user_bg, ai_bg),
                border=f"1px solid {border_color}",
                box_shadow="4px 4px 8px rgba(0,0,0,0.1)",
                # Optional: Backdrop blur makes transparent bubbles look "frosted"
                backdrop_filter="blur(4px)", 
            ),
            
            spacing="4",
            align="start",
            justify=rx.cond(is_user, "end", "start"),
            width="100%",
        ),
        width="100%",
        padding_y=Spacing.MD,
    )

def chat_header() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading("The Grand Ledger", size="9", font_family=Typography.HEADING_FONT),
            rx.text("Archive of the Ancient Realms", size="2", color=ThemeColors.TEXT_MUTED),
            spacing="1",
            align="start",
        ),
        rx.spacer(),
        rx.hstack(
            rx.badge("Vertex AI RAG Active", color_scheme="gold", variant="outline", size="3"),
            rx.button(
                rx.icon("plus", size=24),
                rx.text("New Scroll", size="4"),
                on_click=ChatState.new_chat,
                variant="soft",
                color_scheme="gold",
                size="3",
            ),
            spacing="4",
        ),
        padding=Spacing.LG,
        width="100%",
        border_bottom=f"3px double {ThemeColors.TEXT_MAIN}",
        bg=ThemeColors.BG_SURFACE,
    )

def chat_input() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text_area(
                id="chat_input_field",
                value=ChatState.current_input,
                on_change=ChatState.set_current_input,
                placeholder="Type your command to the void...",
                size="3",
                width="100%",
                height="100px",
                bg=ThemeColors.BG_PAGE,
                border=f"2px solid {ThemeColors.TEXT_MAIN}",
                font_size="1.2rem",
                _focus={"border_color": ThemeColors.ANCIENT_GOLD},
            ),
            rx.button(
                rx.icon("send", size=32),
                "SEND",
                on_click=ChatState.send_message,
                disabled=ChatState.processing,
                height="100px",
                width="150px",
                color_scheme="gold",
                font_family=Typography.HEADING_FONT,
                font_size="1.2rem",
            ),
            spacing="0",
            width="100%",
            align="stretch",
        ),
        padding=Spacing.MD,
        bg=ThemeColors.BG_SURFACE,
        border_top=f"2px solid {ThemeColors.TEXT_MAIN}",
        width="100%",
    )

def chat_page() -> rx.Component:
    return base_page(
        rx.vstack(
            chat_header(),
            rx.box(
                rx.scroll_area(
                    # ... (messages)
                    rx.vstack(
                        rx.foreach(
                            ChatState.messages,
                            message_bubble,
                        ),
                        rx.cond(
                            ChatState.processing,
                            rx.box(
                                rx.text("The spirits are thinking...", font_family=Typography.BODY_FONT, italic=True), 
                                padding=Spacing.LG
                            ),
                        ),
                        width="100%",
                        padding_x="5%",
                        padding_y=Spacing.XL,
                        spacing="8",
                    ),
                    height="100%", 
                ),
                flex="1", # Takes up all available space between header and input
                width="100%",
                overflow="hidden",
                bg=ThemeColors.BG_PAGE,
            ),
            chat_input(),
            height="100%", # Changed from 100vh
            width="100%",
            spacing="0",
        ),
    )