import reflex as rx
from ..styles import ThemeColors, Spacing, Typography

import random

class DiceState(rx.State):
    roll_result: int = 0
    roll_history: list[str] = []

    def roll_dice(self, sides: int):
        result = random.randint(1, sides)
        self.roll_result = result
        # Add to the log: "Rolled a 14 (d20)"
        self.roll_history.insert(0, f"Rolled a {result} (d{sides})")
        # Keep only the last 5 rolls
        self.roll_history = self.roll_history[:5]



def dice_button(sides: int, color: str) -> rx.Component:
    return rx.button(
        f"d{sides}",
        on_click=lambda: DiceState.roll_dice(sides),
        variant="outline",
        size="2",
        # Custom OSRS/Fantasy style
        color_scheme=color,
        border=f"1px solid {ThemeColors.ANCIENT_GOLD}",
        _hover={"bg": ThemeColors.BG_OVERLAY}
    )

def dice_roller_panel() -> rx.Component:
    return rx.vstack(
        rx.heading("Dice Tray", size="4"),
        
        # The Result Display
        rx.center(
            rx.text(
                DiceState.roll_result,
                size="9",
                weight="bold",
                font_family=Typography.HEADING_FONT,
                color=ThemeColors.PRIMARY # Blood Red result
            ),
            width="100%",
            height="4em",
            border=f"2px double {ThemeColors.BORDER_SUBTLE}",
            bg=ThemeColors.BG_SURFACE
        ),
        
        # Grid of Dice
        rx.grid(
            dice_button(4, color = 'tomato'), dice_button(6, color = 'orange'), dice_button(8, color = 'amber'),
            dice_button(10, color = 'grass'), dice_button(12, color = 'indigo'), dice_button(20, color = 'crimson'),
            columns="3",
            spacing="2",
            width="100%",
        ),
        
        # Small Roll Log
        rx.vstack(
            rx.foreach(
                DiceState.roll_history,
                lambda log: rx.text(log, size="1", color=ThemeColors.TEXT_MUTED)
            ),
            align_items="start",
            width="100%",
            padding_top=Spacing.SM,
        ),
        text_align='center',
        padding=Spacing.MD,
        box_shadow = "3px 3px 0px rgba(0,0,0,0.3)",
        border=ThemeColors.BORDER_SUBTLE,
        bg=ThemeColors.BG_PAGE,
        width="15rem",
        padding_x='2rem'
    )