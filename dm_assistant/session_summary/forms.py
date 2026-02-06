import reflex as rx

from .state import (
    SessionEditSummaryFormState,
    SessionAddSummaryFormState
)

def session_summary_add_form() -> rx.Component:
    """Contact Page."""
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="Title",
                name="title",
                required=True,
                width="100%",
            ),
            rx.text_area(
                placeholder="Your Message",
                name="summary_text",
                required=True,
                width="100%",
                height="50vh",
            ),
            rx.button("Submit", type="submit", color_scheme="blue"),
            spacing="4",
            width="100%",
        ),
        on_submit= SessionAddSummaryFormState.handle_submit,
        reset_on_submit=True,
        width="400px",
    )


def session_summary_edit_form() -> rx.Component:
    """Contact Page."""
    summary = SessionEditSummaryFormState.summary
    title = summary.title
    publish_active = summary.publish_active
    summary_text = summary.summary_text

    return rx.form(
        rx.box(
             rx.input(
                type="hidden",
                name='session_id',
                value=summary.id
            ),
            display='none',
        ),
        rx.vstack(
            rx.input(
                default_value=title,
                placeholder="Title",
                name="title",
                required=True,
                width="100%",
            ),
            rx.text_area(
                default_value=summary_text,
                on_change = SessionEditSummaryFormState.set_summary_text,
                placeholder="Your Message",
                name="summary_text",
                required=True,
                width="100%",
                height="50vh",
            ),
            rx.flex(
                rx.switch(default_checked = SessionEditSummaryFormState.summary_publish_active,
                          name = 'publish_active',
                          on_change=SessionEditSummaryFormState.set_summary_publish_active),
                rx.text('Publish Active'),
                spacing='2'
            ),
            rx.cond(
                SessionEditSummaryFormState.summary_publish_active,
                rx.box(
                    rx.hstack(
                        rx.input(
                            default_value=SessionEditSummaryFormState.publish_display_date,
                            type='date',
                            name='publish_date',
                            width = '100%'
                        ),
                        rx.input(
                            default_value=SessionEditSummaryFormState.publish_display_time,
                            type='time',
                            name='publish_time',
                            width = '100%'
                        ),
                        width = '100%'
                    ),
                    width='100%'
                )
            ),
            rx.button("Submit", type="submit", color_scheme="blue"),
            spacing="4",
            width="100%",
        ),
        on_submit= SessionEditSummaryFormState.handle_submit,
        width="400px",
    )