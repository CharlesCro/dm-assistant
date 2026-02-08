import reflex as rx
import math

class CharSheetState(rx.State):
    """Handles the reactive data and D&D mechanics with explicit type conversion."""
    # Header Info
    char_name: str = ""
    char_class: str = ""
    level: int = 1
    race: str = ""
    background: str = ""
    alignment: str = ""
    exp: str = "0"

    # Core Ability Scores
    strength: int = 10
    dexterity: int = 10
    constitution: int = 10
    intelligence: int = 10
    wisdom: int = 10
    charisma: int = 10

    # Combat & Health
    armor_class: int = 10
    initiative_misc: int = 0
    speed: str = "30ft"
    hp_max: int = 10
    hp_current: int = 10
    hp_temp: int = 0
    hit_dice_total: str = "1d8"
    
    # Trackers
    inspiration: bool = False

    # --- EXPLICIT SETTERS (Fixes ArgTypeMismatchError) ---
    def set_level(self, val: str):
        try: self.level = int(val) if val != "" else 0
        except ValueError: pass

    def set_strength(self, val: str):
        try: self.strength = int(val) if val != "" else 0
        except ValueError: pass

    def set_dexterity(self, val: str):
        try: self.dexterity = int(val) if val != "" else 0
        except ValueError: pass

    def set_constitution(self, val: str):
        try: self.constitution = int(val) if val != "" else 0
        except ValueError: pass

    def set_intelligence(self, val: str):
        try: self.intelligence = int(val) if val != "" else 0
        except ValueError: pass

    def set_wisdom(self, val: str):
        try: self.wisdom = int(val) if val != "" else 0
        except ValueError: pass

    def set_charisma(self, val: str):
        try: self.charisma = int(val) if val != "" else 0
        except ValueError: pass

    def set_hp_current(self, val: str):
        try: self.hp_current = int(val) if val != "" else 0
        except ValueError: pass

    def set_armor_class(self, val: str):
        try: self.armor_class = int(val) if val != "" else 0
        except ValueError: pass

    # --- CALCULATED VARS ---
    @rx.var
    def prof_bonus(self) -> int:
        return math.floor((self.level - 1) / 4) + 2

    @rx.var
    def str_mod(self) -> int: return math.floor((self.strength - 10) / 2)
    @rx.var
    def dex_mod(self) -> int: return math.floor((self.dexterity - 10) / 2)
    @rx.var
    def con_mod(self) -> int: return math.floor((self.constitution - 10) / 2)
    @rx.var
    def int_mod(self) -> int: return math.floor((self.intelligence - 10) / 2)
    @rx.var
    def wis_mod(self) -> int: return math.floor((self.wisdom - 10) / 2)
    @rx.var
    def cha_mod(self) -> int: return math.floor((self.charisma - 10) / 2)

    @rx.var
    def passive_perception(self) -> int:
        return 10 + self.wis_mod