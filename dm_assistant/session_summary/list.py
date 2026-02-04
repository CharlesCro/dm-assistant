import reflex as rx

from .. import navigation
from ..ui.base import base_page

from . import state, model

def session_summary_detail_link(child: rx.Component, summary: model.SessionSummaryModel) -> rx.Component:
    """Create a link to the session summary detail page."""
    if summary is None:
        return rx.fragment(child)
    summary_id = summary.id
    if summary_id is None:
        return rx.fragment(child)
    summary_detail_url = navigation.routes.SESSION_SUMMARIES_ROUTE + f"/{summary_id}"

    return rx.link(
        child,
        href=summary_detail_url
    )

def session_summary_list_item(summary: model.SessionSummaryModel) -> rx.Component:
    """Create a session summary list item."""
    return rx.box(
        session_summary_detail_link(
            rx.heading(summary.title),
            summary
            ),
        padding = '1em'
    )


def session_summary_list_page() -> rx.Component:

    return base_page(
        rx.vstack(
            rx.heading("Session Summaries", size = '5', weight="bold"),
            rx.link(
                rx.button('New Session Summary', color_scheme="teal"),
                href=navigation.routes.ADD_SESSION_SUMMARY_ROUTE,
                ),
            rx.foreach(state.SessionSummaryState.summaries, session_summary_list_item),
            spacing="5",
            align="center",
            min_height="85vh",
            id='session-summary-child'
        )
    )
