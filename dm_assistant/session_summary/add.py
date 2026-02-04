import reflex as rx

from ..ui.base import base_page

from . import forms

def session_summary_add_page() -> rx.Component:
    """Session Summary Add Page."""
    my_form = forms.session_summary_add_form()

    contact_child = rx.vstack(
        rx.heading("Add Session Summary", weight="bold"),
        my_form,
        spacing="5",
        justify="center",
        align="center",
        min_height="95vh",
    )
    return base_page(
        contact_child
    )