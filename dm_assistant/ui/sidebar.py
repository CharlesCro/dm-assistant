import reflex as rx
from .. import navigation
# Import the design system
from ..styles import ThemeColors, Spacing, components, Typography
from .dice_roller import dice_roller_panel
from ..auth.state import GoogleState

def logout_confirmation_item() -> rx.Component:
    """A sidebar item that triggers a fantasy-styled confirmation dialog."""
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            # We use an hstack styled like a NAV_ITEM to match Settings perfectly
            rx.hstack(
                rx.icon("log-out", color=ThemeColors.DARK_INK),
                rx.text("Leave Tavern", size="4"),
                # Applying the exact same style spec as your other sidebar items
                style=components.navigation.NAV_ITEM, 
                width="100%",
                align="center",
                cursor="pointer",
            )
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title("Confirm Departure", font_family=Typography.HEADING_FONT),
            rx.alert_dialog.description(
                "Are you sure you wish to end your session? Any unsaved notes for your campaign may be lost to the void.",
                size="2",
                color=ThemeColors.TEXT_MUTED,
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button(
                        "Stay", 
                        variant="soft", 
                        color_scheme="gray",
                        cursor="pointer"
                    ),
                ),
                rx.alert_dialog.action(
                    rx.button(
                        "Logout", 
                        color_scheme="red", 
                        variant="solid",
                        on_click=GoogleState.logout,
                        cursor="pointer"
                    ),
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            style={
                "background_color": ThemeColors.BG_SURFACE,
                "border": f"1px solid {ThemeColors.TEXT_MAIN}",
                "box_shadow": "5px 5px 15px rgba(0,0,0,0.3)",
            },
        ),
    )

def sibebar_user_item() -> rx.Component:
    return rx.cond(
        GoogleState.token_is_valid,
        rx.hstack(
                rx.avatar(
                src=GoogleState.user_picture,
                fallback=GoogleState.user_name[0], # Shows first letter if image fails
                size="3",
                radius="full",
            ),
            rx.vstack(
                rx.box(
                    rx.text(GoogleState.user_name, size="3", weight="bold"),
                    rx.text(GoogleState.user_email, size="1"),
                ),
                spacing="0",
                align="start",
                justify="start",
                width="100%",
            ),
            padding_x=Spacing.XS,
            align="center",
            justify="start",
            width="100%",
        ),
        rx.fragment('')
    )

def sidebar_logout_item() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.icon('log-out', color=ThemeColors.DARK_INK),
            rx.text('Log Out', size="4"),
            # Applying the navigation component style spec
            style=components.navigation.NAV_ITEM, 
            width="100%",
            align="center",
        ),
        on_click=navigation.NavState.do_logout,
        cursor="pointer",
        width="100%",
    )

def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, color=ThemeColors.DARK_INK),
            rx.text(text, size="4"),
            # Centralized hover and transition logic
            style=components.navigation.NAV_ITEM, 
            width="100%",
            align="center",
        ),
        href=href,
        underline="none",
        width="100%",
    )

def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Dashboard", "layout-dashboard", navigation.routes.HOME_ROUTE),
        sidebar_item("Chat", "message-circle", navigation.routes.CHAT_ROUTE),
        sidebar_item("Files", "square-library", navigation.routes.SESSION_SUMMARIES_ROUTE),
        sidebar_item("New Session", "plus", navigation.routes.ADD_SESSION_SUMMARY_ROUTE),
        spacing="1",
        width="100%",
    )

def sidebar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                # Header Section
                rx.hstack(
                    rx.image(
                        src="/logo_dnd.jpg",
                        width="2.25em",
                        height="auto",
                        border=f"1px solid {ThemeColors.DARK_INK}", # Border around logo
                    ),
                    rx.heading("DM Assistant", size="7"),
                    align="center",
                    justify="start",
                    padding_x=Spacing.XS,
                    width="100%",
                ),
                sidebar_items(),
                rx.spacer(),
                
                # The New Dice Roller!
                dice_roller_panel(),
                rx.spacer(),
                # Footer Section
                rx.vstack(
                    rx.vstack(
                        sidebar_item("Settings", "settings", "/#"),
                        spacing="1",
                        width="100%",
                    ),
                    logout_confirmation_item(),
                    rx.divider(border_color=ThemeColors.BORDER_SUBTLE),
                    sibebar_user_item(),
                    width="100%",
                    spacing="5",
                ),
                # Applying the master Sidebar Container spec (Handles Parchment BG & Borders)
                
                style=components.navigation.SIDEBAR_CONTAINER,
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(rx.icon("align-justify", size=30, color=ThemeColors.TEXT_MAIN)),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(rx.icon("x", size=30, color=ThemeColors.PRIMARY)),
                                width="100%",
                            ),
                            sidebar_items(),
                            rx.spacer(),
                            rx.divider(border_color=ThemeColors.BORDER_SUBTLE),
                            sibebar_user_item(),
                            spacing="5",
                            width="100%",
                        ),
                        # Use the same surface color for the mobile drawer
                        bg=ThemeColors.BG_SURFACE,
                        padding=Spacing.LG,
                        height="100%",
                        width="20em",
                    ),
                ),
                direction="left",
            ),
            padding=Spacing.MD,
        ),
        
    )