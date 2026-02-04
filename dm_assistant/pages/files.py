import reflex as rx

from ..ui.base import base_page



def files_page() -> rx.Component:
    """Files Page."""
    files_child = rx.vstack(
        rx.heading("Files Page", weight="bold"),
        rx.text(
            "This is the files page where users can manage their campaign files such as:",
            size="5",
        ),
        rx.unordered_list(
            rx.list_item("Character Sheets"),
            rx.list_item("Campaign Notes"),
            rx.list_item("Maps and Visual Aids"),
            rx.list_item("NPC Profiles"),
            rx.list_item("Session Logs"),
            size="5",
        ),
        spacing="5",
        justify="center",
        align="center",
        min_height="85vh",
        id='files-child'
    )
    return base_page(
        files_child
    )   