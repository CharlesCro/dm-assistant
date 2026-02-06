import reflex as rx

from .sidebar import sidebar

def base_dashboard_page(child: rx.Component, *args) -> rx.Component:

   

    if not isinstance(child, rx.Component):
        child = rx.heading('This is not a valid Reflex child component')



    return rx.fragment(
        rx.hstack(
            sidebar(),
            rx.box(
                child,
                rx.link(
                rx.button("Rules", size="3", color_scheme="teal"),
                href="/docs/rules",
                is_external=True,
                
            ),
            rx.logo(),
            # bg=rx.color("accent", 3),
            padding="1em",
            width="100%",
            id='my-content-area'
            )
        ),
        
        rx.color_mode.button(position="bottom-right", id="color-mode-button"),
        padding = '10em',
        id = 'my-base-container'
    )