import reflex as rx

from . import state

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
        on_submit= state.SessionAddSummaryFormState.handle_submit,
        reset_on_submit=True,
        width="400px",
    )
