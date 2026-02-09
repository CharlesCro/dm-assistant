import reflex as rx
from .. import navigation
from ..styles import ThemeColors, Spacing, components, Typography
from .dice_roller import dice_roller_panel
from ..auth.state import GoogleState

def logout_confirmation_item() -> rx.Component:
    """A sidebar item that triggers a fantasy-styled confirmation dialog."""
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.box(
                rx.hstack(
                    rx.icon('log-out', color="inherit"),
                    rx.text('Log Out', size="4"),
                    width="100%",
                    align="center",
                ),
                style=components.navigation.NAV_ITEM_LOGOUT,
                width="100%",
            ),
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
                    rx.button("Stay", variant="soft", color_scheme="gray", cursor="pointer"),
                ),
                rx.alert_dialog.action(
                    rx.button("Logout", color_scheme="red", variant="solid", on_click=GoogleState.logout, cursor="pointer"),
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

def logout_item() -> rx.Component:
    """Sidebar logout item behaving like a normal nav entry."""
    return rx.hstack(
        rx.icon("log-out", color="inherit"),
        rx.text("Log Out", size="4"),
        align="center",
        width="100%",
        style=components.navigation.NAV_ITEM_LOGOUT,
        on_click=GoogleState.logout,
    )



def sibebar_user_item() -> rx.Component:
    """Displays user profile info if logged in."""
    return rx.cond(
        GoogleState.token_is_valid,
        rx.hstack(
            rx.avatar(
                src=GoogleState.user_picture,
                fallback=GoogleState.user_name[0],
                size="3",
                radius="full",
            ),
            rx.vstack(
                rx.box(
                    rx.text(GoogleState.user_name, size="3", weight="bold"),
                    rx.text(GoogleState.user_email, size="1", color=ThemeColors.TEXT_MUTED),
                ),
                spacing="0",
                align="start",
            ),
            padding_x=Spacing.SM,
            padding_y=Spacing.XS,
            align="center",
            width="100%",
        ),
        rx.fragment('')
    )

def sidebar_items() -> rx.Component:
    return rx.vstack(
        rx.link(
            rx.hstack(
                rx.icon('layout-dashboard', color="inherit"),
                rx.text('Home', size="4"),
                style=components.navigation.NAV_ITEM_HOME, 
                align="center",
            ),
            href=navigation.routes.HOME_ROUTE,
            underline="none",
            width="100%",
        ),
        rx.link(
            rx.hstack(
                rx.icon('message-circle', color="inherit"),
                rx.text('Chat', size="4"),
                style=components.navigation.NAV_ITEM_CHAT, 
                align="center",
            ),
            href=navigation.routes.CHAT_ROUTE,
            underline="none",
            width="100%",
        ),
        spacing="1",
        width="100%",
    )

def sidebar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                # Header Section
                rx.hstack(
                    rx.image(src="/logo_dnd.jpg", width="2.25em", height="auto", border=f"1px solid {ThemeColors.DARK_INK}"),
                    rx.heading("Fable.ai", size="8"),
                    align="center",
                    padding_x=Spacing.XS,
                    padding_y=Spacing.MD,
                    width="100%",
                ),
                rx.divider(),
                sidebar_items(),
                rx.spacer(),
                
                dice_roller_panel(),
                rx.spacer(),

                # Footer Section
                rx.vstack(
                    rx.link(
                        rx.hstack(
                            rx.icon('settings', color="inherit"),
                            rx.text('Settings', size="4"),
                            style=components.navigation.NAV_ITEM_SETTINGS, 
                            align="center",
                        ),
                        href=navigation.routes.HOME_ROUTE, 
                        underline="none",
                        width="100%",
                    ),
                    logout_confirmation_item(),
                    rx.divider(border_color=ThemeColors.BORDER_SUBTLE),
                    sibebar_user_item(),
                    width="100%",
                    spacing="4",
                ),
                style=components.navigation.SIDEBAR_CONTAINER,
            ),
        ),
        # Mobile Tablet View
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(rx.icon("align-justify", size=30, color=ThemeColors.TEXT_MAIN)),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(rx.drawer.close(rx.icon("x", size=30, color=ThemeColors.PRIMARY)), width="100%"),
                            sidebar_items(),
                            rx.spacer(),
                            rx.divider(border_color=ThemeColors.BORDER_SUBTLE),
                            sibebar_user_item(),
                            spacing="5",
                            width="100%",
                        ),
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