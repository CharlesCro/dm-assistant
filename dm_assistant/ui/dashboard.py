import reflex as rx
from .sidebar import sidebar
from ..styles import ThemeColors, Spacing, components

def base_dashboard_page(child: rx.Component, *args) -> rx.Component:
    """The master layout for authenticated users, resembling a fantasy tome."""
    
    if not isinstance(child, rx.Component):
        child = rx.heading('This is not a valid Reflex child component')

    return rx.fragment(
        rx.hstack(
            # 1. The Sidebar (Now inherits parchment background)
            sidebar(),
            
            # 2. The Main Content Area
            rx.box(
                child,
                
                # Floating 'Rules' Button - Styled via components.inputs
                rx.link(
                    rx.button(
                        "Rules", 
                        size="3",
                        # We no longer need color_scheme="teal" 
                        # as rx.button is globally styled in theme.py
                    ),
                    href="/docs/rules",
                    is_external=True,
                ),
                
                
                # Apply the centralized content area style spec
                style=components.layout.CONTENT_AREA,
                id='my-content-area'
            ),
            
            # Use the Dashboard Stack spec to ensure sidebar and content align perfectly
            style=components.layout.DASHBOARD_HSTACK,
            spacing=Spacing.ZERO,
            align_items="stretch",
        ),
        
        # Color mode toggle (Theme handling)
        rx.color_mode.button(
            position="bottom-right", 
            id="color-mode-button",
            # Optional: Tint the button to match the theme
            color_scheme="gold",
        ),
        
        # Applying the base layout container style (handles the paper texture)
        style=components.layout.BASE_LAYOUT_CONTAINER,
        id='my-base-container'
    )