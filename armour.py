from __future__ import annotations

class Armour:
    """Base armour class storing name and protection value."""

    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection

    def __str__(self) -> str:
        return self.name


class Rags(Armour):
    """Basic starter armour with minimal protection."""
    def __init__(self, name: str = "Rags", protection: int = 1) -> None:
        super().__init__(name, protection)


class LeatherTunic(Armour):
    """Light armour offering slightly better protection."""
    def __init__(self, name: str = "Leather Tunic", protection: int = 2) -> None:
        super().__init__(name, protection)