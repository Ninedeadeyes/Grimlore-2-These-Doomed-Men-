from __future__ import annotations

class Weapon:
    """Base weapon class storing name and damage."""

    def __init__(self, name: str, damage: int) -> None:
        self.name: str = name
        self.damage: int = damage

    def __str__(self) -> str:
        return self.name     # Needed so print() shows the weapon name instead of memory address

class GlassShank(Weapon):
    def __init__(self, name: str = "Glass Shank", damage: int = 2) -> None:
        super().__init__(name, damage)

    def __str__(self) -> str:
        return self.name

class Sword(Weapon):
    def __init__(self, name: str = "Iron Sword", damage: int = 5) -> None:
        super().__init__(name, damage)

    def __str__(self) -> str:
        return self.name

class Axe(Weapon):
    def __init__(self, name: str = "Steel Axe", damage: int = 10) -> None:
        super().__init__(name, damage)

    def __str__(self) -> str:
        return self.name

class WarHammer(Weapon):
    def __init__(self, name: str = "Mithril War Hammer", damage: int = 15) -> None:
        super().__init__(name, damage)

    def __str__(self) -> str:
        return self.name

