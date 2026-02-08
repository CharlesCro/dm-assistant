import reflex as rx
from ..ui.base import base_page
from ..styles import ThemeColors, Spacing, Typography
from .state import ChatState, ChatMessage

def message_bubble(message: ChatMessage) -> rx.Component:
    """Render a single chat message bubble."""
    is_user = message.role == "user"
    
    return rx.box(
        rx.hstack(
            # Avatar (only for assistant)
            rx.cond(
                ~is_user,
                rx.avatar(
                    fallback="🎲",
                    size="5",
                    radius="full",
                    color_scheme="gold",
                ),
                rx.box(),  # Empty spacer for user messages
            ),
            
            # Message content
            rx.box(
                rx.cond(
                    is_user,
                    # User message - plain text
                    rx.text(
                        message.content,
                        color=ThemeColors.TEXT_MAIN,
                        size="3",
                        white_space="pre-wrap",
                    ),
                    # Assistant message - with markdown support
                    rx.markdown(
                        message.content,
                        color=ThemeColors.TEXT_MAIN,
                    ),
                ),
                padding=Spacing.MD,
                border_radius="8px",
                max_width="600px",
                bg=rx.cond(
                    is_user,
                    ThemeColors.CHAT_USER_BUBBLE,
                    ThemeColors.CHAT_AI_BUBBLE,
                ),
                border=f"1px solid {ThemeColors.TEXT_MUTED}",
                box_shadow="2px 2px 4px rgba(0,0,0,0.1)",
            ),
            
            spacing="3",
            align="start",
            justify=rx.cond(is_user, "end", "start"),
            width="100%",
        ),
        width="100%",
        padding_y=Spacing.SM,
    )

def typing_indicator() -> rx.Component:
    """Animated typing indicator when AI is processing."""
    return rx.hstack(
        rx.avatar(
            fallback="🎲",
            size="5",
            radius="full",
            color_scheme="gold",
        ),
        rx.box(
            rx.hstack(
                rx.box(
                    width="8px",
                    height="8px",
                    border_radius="50%",
                    bg=ThemeColors.TEXT_MUTED,
                    animation="pulse 1.5s ease-in-out infinite",
                ),
                rx.box(
                    width="8px",
                    height="8px",
                    border_radius="50%",
                    bg=ThemeColors.TEXT_MUTED,
                    animation="pulse 1.5s ease-in-out 0.2s infinite",
                ),
                rx.box(
                    width="8px",
                    height="8px",
                    border_radius="50%",
                    bg=ThemeColors.TEXT_MUTED,
                    animation="pulse 1.5s ease-in-out 0.4s infinite",
                ),
                spacing="2",
                padding=Spacing.SM,
            ),
            padding=Spacing.MD,
            border_radius="8px",
            bg=ThemeColors.CHAT_AI_BUBBLE,
            border=f"1px solid {ThemeColors.TEXT_MUTED}",
        ),
        spacing="3",
        align="start",
        padding_y=Spacing.SM,
    )

def chat_input() -> rx.Component:
    """Input area with send button - fixed rx.cond return types."""
    return rx.box(
        rx.hstack(
            rx.text_area(
                id="chat_input_field",
                value=ChatState.current_input,
                on_change=ChatState.set_current_input,
                placeholder="Whisper your query... (Enter to send, Shift+Enter for newline)",
                resize="vertical",
                min_height="80px",
                max_height="200px",
                width="100%",
                disabled=ChatState.processing,
                font_family=Typography.BODY_FONT,
                size="3",
                border=f"2px solid {ThemeColors.TEXT_MUTED}",
                border_radius="8px",
                padding=Spacing.MD,
                # FIXED: The third argument must be an Event, not a Component.
                # We use rx.console_log as a safe "do-nothing" event for the browser.
                on_key_down=lambda k, e: rx.cond(
                    (k == "Enter") & (~e.shift_key),
                    ChatState.send_message(),
                    rx.console_log("Newline added"), 
                ),
                _focus={
                    "border_color": ThemeColors.ANCIENT_GOLD,
                    "box_shadow": f"0 0 0 2px {ThemeColors.ANCIENT_GOLD}",
                    "outline": "none",
                },
            ),
            
            rx.button(
                rx.icon("send", size=24),
                on_click=ChatState.send_message,
                disabled=ChatState.processing,
                size="4",
                color_scheme="gold",
                cursor="pointer",
                height="80px",
                padding_x=Spacing.LG,
            ),
            
            spacing="3",
            align="end",
            width="100%",
        ),
        padding=Spacing.LG,
        border_top=f"2px solid {ThemeColors.TEXT_MAIN}",
        bg=ThemeColors.BG_SURFACE,
        width="100%",
    )

def chat_page() -> rx.Component:
    """Main chat page component."""
    return base_page(
        rx.vstack(
            # Header
            rx.box(
                rx.hstack(
                    rx.vstack(
                        rx.heading(
                            "The Grand Ledger",
                            size="8",
                            font_family=Typography.HEADING_FONT,
                            color=ThemeColors.TEXT_MAIN,
                        ),
                        spacing="1",
                        align="start",
                    ),
                    rx.spacer(),
                    rx.button(
                        rx.icon("plus", size=20),
                        rx.text("New Chat", size="3", display=["none", "none", "block"]),
                        on_click=ChatState.new_chat,
                        variant="soft",
                        color_scheme="gold",
                        size="3",
                        spacing="2",
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                ),
                padding_y=Spacing.LG,
                padding_x=Spacing.LG,
                border_bottom=f"3px double {ThemeColors.TEXT_MAIN}",
                bg=ThemeColors.BG_SURFACE,
                width="100%",
            ),
            
            # Messages area
            rx.box(
                rx.scroll_area(
                    rx.box(
                        rx.cond(
                            ChatState.messages.length() == 0,
                            rx.center(
                                rx.vstack(
                                    rx.text(
                                        "🎲 Welcome to the Dungeon Master's Archive",
                                        size="5",
                                        weight="bold",
                                        color=ThemeColors.TEXT_MAIN,
                                        font_family=Typography.HEADING_FONT,
                                    ),
                                    rx.divider(width="200px", margin_y=Spacing.LG),
                                    rx.text(
                                        "Powered by Google ADK & Vertex AI RAG",
                                        size="3",
                                        color=ThemeColors.TEXT_MUTED,
                                    ),
                                    spacing="4",
                                    text_align="center",
                                ),
                                min_height="500px",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.foreach(
                                    ChatState.messages,
                                    message_bubble,
                                ),
                                rx.cond(
                                    ChatState.processing,
                                    typing_indicator(),
                                    rx.box(),
                                ),
                                spacing="6",
                                width="100%",
                                padding=Spacing.LG,
                            ),
                        ),
                        width="100%",
                        max_width="900px",
                        margin="0 auto",
                        id="chat-messages",
                    ),
                    height="100%",
                    width="100%",
                    type="auto",
                    scrollbars="vertical",
                    scroll_behavior='smooth'
                ),
                flex="1",
                overflow="hidden",
                bg=ThemeColors.BG_PAGE,
                width="100%",
                min_height="400px",
            ),
            
            # Input area
            rx.box(
                chat_input(),
                width="100%",
                max_width="900px",
                margin="0 auto",
            ),
            
            width="100%",
            height="calc(100vh - 100px)",
            spacing="0",
            overflow="hidden",
        ),
    )