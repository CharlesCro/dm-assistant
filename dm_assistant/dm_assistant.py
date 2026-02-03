"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from .ui.base import base_page

class State(rx.State):
    """The app state."""


    label = 'Traveler'

    def handle_input_change(self, value: str):
        """Handle the input change event."""
        self.label = value

    def did_click(self):
        """Handle the click event."""
        print(f"Button clicked! Current label: {self.label}")



def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        
        rx.vstack(
            rx.text(
                "Dungeoon Master Assistant is an AI-powered tool designed to help Dungeon Masters create and manage their Dungeons & Dragons campaigns with ease.",
                size="5",
            ),
            rx.link(
                rx.button("Get Started", size="3", color_scheme="teal"),
                href="/docs/getting-started",
                is_external=True,
            ),
            rx.input(
                default_value=State.label,
                on_click=State.did_click(),
                on_change = State.handle_input_change,
                placeholder="Type your name here",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        )
    )


app = rx.App()
app.add_page(index)
