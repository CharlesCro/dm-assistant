import reflex as rx
from ..ui.base import base_page
from ..styles import ThemeColors, Spacing
from ..styles.components import inputs

def qa(question: str, answer: str) -> rx.Component:
    return rx.vstack(
        # User Question (Right aligned, standard ink)
        rx.box(
            rx.text(question, color=ThemeColors.TEXT_MAIN, font_style="italic"),
            style=inputs.CHAT_BUBBLE_BASE,
            bg=ThemeColors.CHAT_USER_BUBBLE,
            align_self="flex-end",
        ),
        # AI Answer (Left aligned, golden hue)
        rx.box(
            rx.text(answer, color=ThemeColors.TEXT_MAIN),
            style=inputs.CHAT_BUBBLE_BASE,
            bg=ThemeColors.CHAT_AI_BUBBLE,
            border=f"1px solid {ThemeColors.ANCIENT_GOLD}",
            align_self="flex-start",
        ),
        width="100%",
        spacing="4",
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Whisper your query to the scroll...",
            style=inputs.CHAT_INPUT_STYLE,
            width="100%",
        ),
        rx.button("Consult", style=inputs.PRIMARY_BUTTON),
        width="100%",
        padding_y=Spacing.MD,
    )

def chat_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("The Grand Ledger", size="8", margin_bottom=Spacing.LG),
            rx.box(
                rx.vstack(
                    qa("What is Reflex?", "A way to build web apps in pure Python!"),
                    qa("What can I make?", "Anything from a simple website to a complex web app!"),
                    width="100%",
                    spacing="6",
                ),
                height="60vh",
                align='center',
                overflow_y="auto",
                width="100%",
                padding=Spacing.MD,
                border=f"1px double {ThemeColors.TEXT_MUTED}",
            ),
            action_bar(),
            align='center',
            width="100%",
            max_width="800px",
            spacing="4",
        )
    )