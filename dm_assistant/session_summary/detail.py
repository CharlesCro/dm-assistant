import reflex as rx

from ..ui.base import base_page
from . import state

def session_summary_detail_page() -> rx.Component:
    """Session Summary Detail Page."""
    about_child = rx.vstack(
        rx.heading(state.SessionSummaryState.summary.title, weight="bold"),
        rx.text(state.SessionSummaryState.summary.summary_text, size="5"),
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