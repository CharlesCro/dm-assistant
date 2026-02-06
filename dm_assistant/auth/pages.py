import reflex as rx

from reflex_local_auth.pages.login import LoginState, login_form
from reflex_local_auth.pages.registration import RegistrationState, register_form

from .. import navigation
from .forms import my_register_form
from ..ui.base import base_page
from .state import SessionState

def my_logout_page() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading("Are You Sure You Want To Log Out?", weight="bold"),
            rx.link(
                rx.button('No'),
                href = navigation.routes.HOME_ROUTE,
                color_scheme = 'gray'
                ),
            rx.link(
                rx.button('Yes'),
                on_click = SessionState.perform_logout
                ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id='my-child'
        )
    return base_page( 
        my_child
    )

def my_login_page() -> rx.Component:
    return base_page(
        rx.center(
            rx.cond(
                LoginState.is_hydrated,  # type: ignore
                rx.card(login_form()),
            ),
            min_height="85vh",
        ),
    )

def my_register_page() -> rx.Component:
    """Render the registration page.

    Returns:
        A reflex component.
    """

    return base_page(
            rx.center(
                rx.cond(
                    RegistrationState.success,
                    rx.vstack(
                        rx.text("Registration successful!"),
                    ),
                    rx.card(my_register_form()),
                ),
                min_height="85vh",
        )
    )