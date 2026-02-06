import reflex as rx

from ..ui.base import base_page
from . import state

def session_summary_detail_page() -> rx.Component:
    """Session Summary Detail Page."""
    can_edit = True
    edit_link = rx.link('Edit', href = f'{state.SessionSummaryState.session_summary_edit_url}') 

    edit_link_element = rx.cond(
        can_edit,
        edit_link,
        rx.fragment('')
    )
    about_child = rx.vstack(
        rx.hstack(
            rx.heading(state.SessionSummaryState.summary.title, size='9', weight="bold"),
            edit_link_element,
            align='end'
        ),
        rx.text(
            f"Published on: {state.SessionSummaryState.summary.publish_date}"
        ),
        rx.text(state.SessionSummaryState.summary.summary_text, white_space="pre-wrap"),
        spacing="5",
        align="center",
        min_height="85vh",
    )
    return base_page(
        about_child
    )