import reflex as rx
from .nav import navbar
from .dashboard import base_dashboard_page
from ..styles import components, ThemeColors, Typography, Spacing
from ..auth.state import GoogleState


def base_layout_component(child: rx.Component, *args) -> rx.Component:
    """The public-facing layout (Landing/Login/About) with a fantasy tome vibe."""
    return rx.fragment(
        # 1. Top Navigation
        navbar(),
        
        # 2. Main Content Container
        rx.box(
            child,
            # The new Login Button
            
            # rx.link(
            #     rx.button("Rules", size="3"),
            #     href="/docs/rules",
            #     is_external=True,
                
            # ),
            # Styled via components.layout.CONTENT_AREA (Enterprise standard)
            style=components.layout.CONTENT_AREA,
            id='my-content-area'
        ),

        
        # 4. Utilities
        # rx.color_mode.button(
        #     position="bottom-right", 
        #     id="color-mode-button",
        #     color_scheme="gold"
        # ),
        
        # Root container style: Handles the aged paper background/texture globally
        style=components.layout.BASE_LAYOUT_CONTAINER,
        id='my-base-container'
    )

# base.py excerpt
def base_page(child: rx.Component,  *args) -> rx.Component:

    
    return rx.cond(
        GoogleState.token_is_valid,
        base_dashboard_page(child, *args), # This has your Sidebar
        base_layout_component(child, *args) # This has your Top Nav
    )