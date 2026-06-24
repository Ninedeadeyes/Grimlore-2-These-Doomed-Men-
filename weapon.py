from __future__ import annotations

class Weapon:
    """Base weapon class storing name and damage."""

    def __init__(self, name: str, damage: int) -> None:
        self.name: str = name
        self.damage: int = damage

    def __str__(self) -> str:
        return self.name     # Needed so print() shows the weapon name instead of memory address


class Dagger(Weapon):
    """Basic starter dagger."""
    def __init__(self, name: str = "Dagger", damage: int = 2) -> None:
        super().__init__(name, damage)


class Sword(Weapon):
    """Stronger melee weapon."""
    def __init__(self, name: str = "Sword", damage: int = 4) -> None:
        super().__init__(name, damage)

    def __str__(self) -> str:
        return self.name
