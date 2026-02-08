import reflex as rx
from .sidebar import sidebar
from ..styles import ThemeColors, Spacing, components
def base_dashboard_page(child: rx.Component, *args) -> rx.Component:
    return rx.fragment(
        rx.hstack(
            sidebar(),
            rx.box(
                child,
                style=components.layout.CONTENT_AREA,
                id='my-content-area'
            ),
            style=components.layout.DASHBOARD_HSTACK,
            spacing=Spacing.ZERO,
            align_items="stretch", # Ensures sidebar stretches to bottom
        ),
        style=components.layout.BASE_LAYOUT_CONTAINER,
    )