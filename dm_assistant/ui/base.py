import reflex as rx

from ..auth.state import SessionState
from .nav import navbar
from .dashboard import base_dashboard_page



def base_layout_component(child: rx.Component, *args) -> rx.Component:
    return rx.fragment(
            navbar(),
            rx.box(
                child,
                 rx.link(
                rx.button("Rules", size="3", color_scheme="teal"),
                href="/docs/rules",
                is_external=True,
            ),
                # bg=rx.color("accent", 3),
                padding="1em",
                width="100%",
                id='my-content-area'
            ),
            rx.logo(),
            rx.color_mode.button(position="bottom-right", id="color-mode-button"),
            padding = '10em',
            id = 'my-base-container'
    )

def base_page(child: rx.Component, *args) -> rx.Component:

    if not isinstance(child, rx.Component):
        child = rx.heading('This is not a valid Reflex child component')



    return rx.cond(
        SessionState.is_authenticated,
        base_dashboard_page(child, *args),
        base_layout_component(child, *args)
    )