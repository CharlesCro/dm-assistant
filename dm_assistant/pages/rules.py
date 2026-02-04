import reflex as rx

from ..ui.base import base_page


def rules_page() -> rx.Component:
    """Rules Page."""
    rules_child = rx.vstack(
        rx.heading("Dungeon Master Assistant Rules", weight="bold"),
        rx.text(
            "Here are some important rules and guidelines for using Dungeon Master Assistant:",
            size="5",
        ),
        rx.unordered_list(
            rx.list_item("Respect other users and their campaigns."),
            rx.list_item("Do not share personal information."),
            rx.list_item("Use the AI tools responsibly and ethically."),
            rx.list_item("Report any bugs or issues to the support team."),
            size="5",
        ),
        spacing="5",
        justify="center",
        align="center",
        min_height="85vh",
        id='rules-child'
    )
    return base_page(
        rules_child
    )