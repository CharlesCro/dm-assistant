import reflex as rx

from .nav import navbar

def base_page(child: rx.Component, hide_navbar = False, *args) -> rx.Component:

    if not isinstance(child, rx.Component):
        child = rx.heading('This is not a valid Reflex child component')

    if hide_navbar:
        return rx.container(
            child,
            rx.logo(),
            rx.color_mode.button(position="bottom-right"),
    )


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