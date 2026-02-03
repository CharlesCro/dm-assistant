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


    return rx.container(
            navbar(),
            child,
            rx.logo(),
            rx.color_mode.button(position="bottom-right"),
    )