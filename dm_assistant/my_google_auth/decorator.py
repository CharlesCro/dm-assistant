import functools
from typing import Callable, overload

import reflex as rx

from . import google_auth
from .state import GoogleAuthState

ComponentCallable = Callable[[], rx.Component]


@overload
def require_google_login(
    page: ComponentCallable,
) -> ComponentCallable: ...


@overload
def require_google_login() -> Callable[[ComponentCallable], ComponentCallable]: ...


@overload
def require_google_login(
    *,
    button: rx.Component | None,
) -> Callable[[ComponentCallable], ComponentCallable]: ...


def require_google_login(
    page: ComponentCallable | None = None,
    *,
    button: rx.Component | None = None,
) -> ComponentCallable | Callable[[ComponentCallable], ComponentCallable]:
    """Decorator to require Google login before rendering a page.

    The login button should have on_click set to `reflex_google_auth.handle_google_login`.

    Args:
        page: Page to render after Google login.
        button: Button to render if Google login is required.

    Returns:
        A decorator function or the decorated page.
    """

    

    def navbar_link(text: str, url: str) -> rx.Component:
        return rx.link(
            rx.text(text, size="4", weight="medium"), 
            href=url,
            style={
        "width": "100%",
        "padding": f"0.75rem 1rem",
        "_hover": {
            "background_color": "var(--bg-overlay)" , # Dynamic hover
            "cursor": "pointer",
        },
    } # Use shared nav item style
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
                        navbar_link("About", '/about'),
                        navbar_link("Home", '/'),
                        spacing="5",
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
                            on_click=rx.redirect('/')),
                        rx.menu.item("About", 
                            on_click=rx.redirect('/about')),
                        rx.menu.item("Contact", 
                            on_click=rx.redirect('/contact')),
                        rx.menu.separator(),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
            # Use semantic background token
            bg="var(--bg-surface)" , 
            border_bottom=f"2px solid 1px solid var(--text-muted)",
            padding="1em",
            width="100%",
            align='left'
        )


    def base_layout_component(child: rx.Component, *args) -> rx.Component:
        """The public-facing layout (Landing/Login/About) with a fantasy tome vibe."""
        return rx.fragment(
            # 1. Top Navigation
            navbar(),
            
            # 2. Main Content Container
            rx.box(
                child,
                rx.link(
                    rx.button("Rules", size="3"),
                    href="/docs/rules",
                    is_external=True,
                ),
                # Styled via components.layout.CONTENT_AREA (Enterprise standard)
                style={
                    "padding": '1.5rem',
                    "width": "100%",
                    "max_width": "800px",  # Rulebooks are usually narrow for readability
                    "margin": "0 auto",    # Center the content like a book page
                    "display": "flex",
                    "flex_direction": "column",
                    "align_items": "center",
                    "text_align": "center",
                },
                id='my-content-area'
            ),
            
            # 3. Footer/Logo Branding
            rx.logo(),
            
            # 4. Utilities
            rx.color_mode.button(
                position="bottom-right", 
                id="color-mode-button",
                color_scheme="gold"
            ),
            
            # Root container style: Handles the aged paper background/texture globally
            style={
                "min_height": "100vh",
                "width": "100%",
            },
            id='my-base-container'
        )
    
  
    def login_page() -> rx.Component:

        return rx.vstack(

            rx.heading("The Ledger Awaits", size="9", weight="bold"),
            rx.text(
                "Welcome, Dungeon Master. Authenticate your scroll to access your campaigns and tools.",
                size="5",
                text_align="center",
                max_width="600px",
            ),
            # This is where the magic happens:
            rx.box(
                google_auth.google_login(),
                padding_top="1.5em",
            ),
            spacing="5",
            justify="center",
            align="center",

            min_height="85vh",

        )


    

    def _inner(page: Callable[[], rx.Component]) -> Callable[[], rx.Component]:
        @functools.wraps(page)
        def _auth_wrapper() -> rx.Component:
            return google_auth.google_oauth_provider(
                rx.cond(
                    rx.State.is_hydrated,  
                    rx.cond(
                        GoogleAuthState.token_is_valid,
                        page(),
                        base_layout_component(login_page()),
                    ),
                    # Loading state while hydrating
                    base_layout_component(
                        rx.center(
                            rx.vstack(
                                rx.spinner(size="3", color_scheme="gold"),
                                rx.text("Loading...", size="2"),
                                spacing="4",
                                align="center",
                            ),
                            min_height="85vh",
                        )
                    ),
                ),
            )
        _auth_wrapper.__name__ = page.__name__
        return _auth_wrapper

    if page is None:
        return _inner
    return _inner(page=page)
