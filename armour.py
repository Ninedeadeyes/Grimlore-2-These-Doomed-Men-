from __future__ import annotations

class Armour:
    """Base armour class storing name and protection value."""

    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection

    def __str__(self) -> str:
        return self.name


class LeatherTunic(Armour):
    """Basic starter armour with minimal protection."""
    def __init__(self, name: str = "Leather Tunic", protection: int = 1) -> None:
        super().__init__(name, protection)


class ChainMail(Armour):
    """Light armour offering slightly better protection."""
    def __init__(self, name: str = "Chain Mail", protection: int = 3) -> None:
        super().__init__(name, protection)

class HolyMail(Armour):
    """Light armour offering slightly better protection."""
    def __init__(self, name: str = "Holy Plate", protection: int = 8) -> None:
        super().__init__(name, protection)