import reflex as rx
from ..styles import ThemeColors, Typography, Spacing, components
from .state import CharSheetState

def stat_box(label: str, score_var: rx.Var, mod_var: rx.Var, on_change_handler: callable):
    """The vertical stat box. score_var is the value, mod_var is the calc'd modifier."""
    return rx.vstack(
        rx.text(label, font_family=Typography.HEADING_FONT, size="1", color=ThemeColors.TEXT_MUTED),
        rx.heading(
            rx.cond(mod_var >= 0, "+" + mod_var.to_string(), mod_var.to_string()), 
            size="7", 
            color=ThemeColors.TEXT_MAIN
        ),
        rx.box(
            rx.input(
                value=score_var.to_string(),
                on_change=on_change_handler,
                width="45px",
                variant="soft",
                size="1",
                text_align="center",
            ),
            border= f"1px solid {ThemeColors.TEXT_MAIN}",
            border_radius="50%",
            bg=ThemeColors.BG_PAGE,
            margin_top="-12px",
            z_index="1",
        ),
        border=f"2px solid {ThemeColors.TEXT_MAIN}",
        padding="10px",
        border_radius="8px",
        bg=ThemeColors.BG_SURFACE,
        align="center",
        width="100%",
    )

def character_sheet_content():
    return rx.vstack(
        # --- HEADER ---
        rx.grid(
            rx.vstack(
                rx.text("Character Name", font_family=Typography.HEADING_FONT, size="1"),
                rx.input(value=CharSheetState.char_name, on_change=CharSheetState.set_char_name, width="100%"),
                align_items="start",
            ),
            rx.grid(
                rx.vstack(rx.text("Class & Level", size="1"), rx.input(value=CharSheetState.level.to_string(), on_change=CharSheetState.set_level)),
                rx.vstack(rx.text("Race", size="1"), rx.input(value=CharSheetState.race, on_change=CharSheetState.set_race)),
                columns="2", spacing="2",
            ),
            columns="2", width="100%", spacing="4", padding_bottom=Spacing.MD,
            border_bottom=f"3px double {ThemeColors.TEXT_MAIN}",
        ),

        # --- BODY ---
        rx.grid(
            # Column 1: Stats
            rx.vstack(
                stat_box("STRENGTH", CharSheetState.strength, CharSheetState.str_mod, CharSheetState.set_strength),
                stat_box("DEXTERITY", CharSheetState.dexterity, CharSheetState.dex_mod, CharSheetState.set_dexterity),
                stat_box("CONSTITUTION", CharSheetState.constitution, CharSheetState.con_mod, CharSheetState.set_constitution),
                stat_box("INTELLIGENCE", CharSheetState.intelligence, CharSheetState.int_mod, CharSheetState.set_intelligence),
                stat_box("WISDOM", CharSheetState.wisdom, CharSheetState.wis_mod, CharSheetState.set_wisdom),
                stat_box("CHARISMA", CharSheetState.charisma, CharSheetState.cha_mod, CharSheetState.set_charisma),
                width="100%", spacing="3"
            ),
            # Column 2: Combat
            rx.vstack(
                rx.hstack(
                    rx.vstack(rx.text("AC", size="1"), rx.heading(CharSheetState.armor_class.to_string(), size="6"), border="2px solid black", padding="10px", align="center"),
                    rx.vstack(rx.text("INIT", size="1"), rx.heading(rx.cond(CharSheetState.dex_mod >= 0, "+" + CharSheetState.dex_mod.to_string(), CharSheetState.dex_mod.to_string()), size="6"), border="2px solid black", padding="10px", align="center"),
                    rx.vstack(rx.text("SPD", size="1"), rx.text(CharSheetState.speed), border="2px solid black", padding="10px", align="center"),
                    spacing="3", justify="center", width="100%"
                ),
                rx.box(
                    rx.text("Current HP", size="1", font_family=Typography.HEADING_FONT),
                    rx.input(value=CharSheetState.hp_current.to_string(), on_change=CharSheetState.set_hp_current, size="3", text_align="center"),
                    width="100%", border=f"1px solid {ThemeColors.TEXT_MAIN}", padding="10px"
                ),
                rx.text_area(placeholder="Attacks & Spellcasting", height="300px", width="100%"),
                width="100%", spacing="4"
            ),
            # Column 3: Features
            rx.vstack(
                rx.text_area(placeholder="Features & Traits", height="450px", width="100%"),
                width="100%", spacing="3"
            ),
            columns=rx.breakpoints(initial="1", md="3"),
            spacing="5", width="100%", padding_top=Spacing.LG,
        ),
        style=components.layout.CONTENT_AREA,
    )