import reflex as rx


from ..ui.base import base_page
from . import forms

from .state import SessionEditSummaryFormState


def session_summary_edit_page() -> rx.Component:
    """Session Summary Edit Page."""
    my_form = forms.session_summary_edit_form()

    summary = SessionEditSummaryFormState.summary

    contact_child = rx.vstack(
        rx.heading(f"Edit Mode |  {summary.title}", weight="bold"),
        my_form,
        spacing="5",
        justify="center",
        align="center",
        min_height="95vh",
    )
    return base_page(
        contact_child
    )