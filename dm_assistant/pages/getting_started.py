import reflex as rx

from ..ui.base import base_page



def getting_started_page() -> rx.Component:
    """Getting Started Page."""
    getting_started_child = rx.vstack(
        rx.heading("Getting Started with Dungeon Master Assistant", weight="bold"),
        rx.text(
            "To get started with Dungeon Master Assistant, follow these steps:",
            size="5",
        ),
        rx.ordered_list(
            rx.list_item("Sign up for an account."),
            rx.list_item("Create a new campaign."),
            rx.list_item("Use the AI tools to generate storylines, NPCs, and encounters."),
            rx.list_item("Manage your campaign files and notes."),
            rx.list_item("Invite players to join your campaign."),
            size="5",
        ),
        spacing="5",
        justify="center",
        align="center",
        min_height="85vh",
        id='getting-started-child'
    )
    return base_page(
        getting_started_child
    )