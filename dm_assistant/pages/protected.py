import reflex as rx
import reflex_local_auth

from ..ui.base import base_page

@reflex_local_auth.require_login
def protected_page() -> rx.Component:
    """About Page."""
    about_child = rx.vstack(
        rx.heading("Protected Page", weight="bold"),
        rx.text(
            "Dungeon Master Assistant is an AI-powered tool designed to help Dungeon Masters create and manage their Dungeons & Dragons campaigns with ease.",
            size="5",
        ),
        rx.text(
            "With features like automated story generation, NPC creation, and encounter balancing, Dungeon Master Assistant aims to streamline the campaign creation process and enhance the gaming experience for both DMs and players.",
            size="5",
        ),
        spacing="5",
        justify="center",
        text_align="center",
        align="center",
        min_height="85vh",
        id='about-child'
    )
    return base_page(
        about_child
    )