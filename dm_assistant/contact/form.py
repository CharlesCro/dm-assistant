import reflex as rx

from .state import ContactState

def contact_form() -> rx.Component:
    """Contact Page."""
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="Your Name",
                name="name",
                required=True,
                width="100%",
            ),
            rx.input(
                placeholder="Your Email",
                name="email",
                type="email",
                required=True,
                width="100%",
            ),
            rx.text_area(
                placeholder="Your Message",
                name="message",
                required=True,
                width="100%",
                height="150px",
            ),
            rx.button("Submit", type="submit", color_scheme="blue"),
            spacing="4",
            width="100%",
        ),
        on_submit=ContactState.handle_submit,
        reset_on_submit=True,
        width="400px",
    )