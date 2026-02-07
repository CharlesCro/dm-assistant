import reflex as rx
import reflex_local_auth
from .. import navigation
from ..styles import ThemeColors, components # Import new styles

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), 
        href=url,
        style=components.navigation.NAV_ITEM # Use shared nav item style
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(src="logo_dnd.jpg", width="2.25em"),
                    rx.heading("DM Assistant", size="7"),
                    align_items="center",
                ),
                rx.hstack(
                    # Links now inherit the Fantasy Typography automatically
                    navbar_link("Home", navigation.routes.HOME_ROUTE),
                    navbar_link("About", navigation.routes.ABOUT_ROUTE),
                    spacing="5",
                ),
                rx.hstack(
                    rx.link(
                        rx.button("Sign Up", variant="outline"),
                        href=reflex_local_auth.routes.REGISTER_ROUTE,
                    ),
                    rx.link(
                        rx.button("Log In"),
                        href=reflex_local_auth.routes.LOGIN_ROUTE
                    ),
                    spacing="4",
                ),
                justify="between",
                align_items="center",
            ),
        ),
         rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo_dnd.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "DM Assistant", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home", 
                            on_click=navigation.NavState.to_home),
                        rx.menu.item("About", 
                            on_click=navigation.NavState.to_about),
                        rx.menu.item("Contact", 
                            on_click=navigation.NavState.to_contact),
                        rx.menu.separator(),
                        rx.menu.item("Log in", 
                            on_click=navigation.NavState.to_login),
                        rx.menu.item("Register", 
                            on_click=navigation.NavState.to_register),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        # Use semantic background token
        bg=ThemeColors.BG_SURFACE, 
        border_bottom=f"2px solid {ThemeColors.BORDER_SUBTLE}",
        padding="1em",
        width="100%",
    )