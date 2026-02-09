import reflex as rx
from ..ui.base import base_page
from ..styles import ThemeColors, Spacing, Typography
from .state import ChatState, ChatMessage
from ..auth.state import GoogleState

def message_bubble(message: ChatMessage) -> rx.Component:
    """Render chat bubbles with conditional avatars for both AI and User."""
    is_user = message.role == "user"
    
    # 75% transparency (0.25 alpha)
    user_bg = "rgba(255, 248, 225, 0.25)" 
    ai_bg = "rgba(218, 165, 32, 0.25)"   

    return rx.box(
        rx.flex(
            # --- AVATAR LOGIC ---
            rx.cond(
                is_user,
                rx.avatar(
                    src=GoogleState.user_picture,
                    fallback=GoogleState.user_name[0],
                    size="3",
                    radius="full",
                    margin_top="4px",
                    color_scheme="indigo",
                ),
                rx.avatar(
                    fallback="🎲",
                    size="6",
                    radius="full",
                    color_scheme="gold",
                    margin_top="4px",
                    padding_y='2rem',
                    padding_x='2rem'
                ),
            ),
            
            # --- MESSAGE BUBBLE ---
            rx.box(
                rx.cond(
                    is_user,
                    rx.text(
                        message.content,
                        color=ThemeColors.TEXT_MAIN,
                        font_size="1.2rem",
                        line_height="1.4",
                        white_space="pre-wrap",
                        text_align="left", # Keeps text inside bubble left-aligned
                    ),
                    rx.markdown(
                        message.content,
                        color=ThemeColors.TEXT_MAIN,
                        style={
                            "font-size": "1.2rem",
                            "line-height": "1.4",
                        }
                    ),
                ),
                padding_x="1rem",
                padding_y="0.75rem",
                border_radius="15px",
                max_width="80%",
                width="fit-content",
                # # Added dynamic background color for clarity
                # bg=rx.cond(is_user, user_bg, ai_bg), 
            ),
            
            spacing="3",
            align="start",
            # FIXED: In 'row-reverse', "start" is the right side of the screen.
            # We don't need a condition for 'justify' if we use 'row-reverse' correctly.
            justify="start", 
            flex_direction=rx.cond(is_user, "row-reverse", "row"),
            width="100%",
        ),
        width="100%",
        padding_y=Spacing.SM,
        # This ensures the entire flex container is pushed to the correct side
        display="flex",
        justify_content=rx.cond(is_user, "flex-end", "flex-start"),
    )

def chat_header() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading("The Scribe", size="5", font_family=Typography.HEADING_FONT),
            rx.text("Archive of the Ancient Realms", size="2", color=ThemeColors.TEXT_MUTED),
            spacing="1",
            align="start", 
        ),
        rx.spacer(),
        rx.hstack(
            # rx.badge("Vertex AI RAG Active", color_scheme="gold", variant="outline", size="3"),
            rx.button(
                rx.icon("plus", size=24),
                rx.text("New Chat", size="4"),
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
                # Use rx.auto_scroll instead of rx.scroll_area
                rx.auto_scroll(
                    rx.vstack(
                        rx.foreach(
                            ChatState.messages,
                            message_bubble,
                        ),
                        rx.cond(
                            ChatState.processing,
                            rx.box(
                                rx.text("The spirits are thinking...", font_family=Typography.BODY_FONT, italic=True), 
                                padding=Spacing.LG,
                                id="processing-indicator" # Optional: good for manual scrolling
                            ),
                        ),
                        width="100%",
                        padding_x="5%",
                        padding_y=Spacing.XL,
                        spacing="8",
                        align_items="stretch",
                    ),
                    height="100%", # Ensure it fills the parent box
                    width="100%",
                ),
                flex="1", 
                width="100%",
                overflow="hidden",
                bg=ThemeColors.BG_PAGE,
            ),
            chat_input(),
            height="100%", 
            width="100%",
            spacing="0",
        ),
    )