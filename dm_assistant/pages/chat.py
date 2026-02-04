import reflex as rx

from ..ui.base import base_page
from . import style

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left",
        ),
        margin_y="1em",
        width="100%",
    )


def chat() -> rx.Component:
    qa_pairs = [
        (
            "What is Reflex?",
            "A way to build web apps in pure Python!",
        ),
        (
            "What can I make with it?",
            "Anything from a simple website to a complex web app!",
        ),
    ]
    return rx.box(
        *[
            qa(question, answer)
            for question, answer in qa_pairs
        ]
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            style=style.input_style,
        ),
        rx.button("Ask", style=style.button_style),
    )


def chat_page() -> rx.Component:
    """Chat Page."""
    chat_box = rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            align="center",
        )
    )

    chat_child = rx.vstack(
        rx.heading("Chat with Dungeon Master Assistant", weight="bold"),
        rx.text(
            "This is the chat page where users can interact with the AI assistant to generate storylines, NPCs, and encounters for their Dungeons & Dragons campaigns.",
            size="5",
        ),
        chat_box,
        spacing="5",
        justify="center",
        align="center",
        min_height="85vh",
        id='chat-child'
    )
    return base_page(
        chat_child
    )