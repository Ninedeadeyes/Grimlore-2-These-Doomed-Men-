from __future__ import annotations


class Enemy:
    """Base enemy class storing stats and rewards."""

    def __init__(self, name: str, power: int, health: int, exp: int, gold: int) -> None:
        self.name: str = name
        self.power: int = power
        self.health: int = health
        self.exp: int = exp
        self.gold: int = gold


# Random Event enemies 

class Ratling(Enemy):
    """Weak rat‑creature enemy."""
    def __init__(self, name: str = "Ratling", power: int = 4, health: int = 60, exp: int = 5, gold: int = 25) -> None:
        super().__init__(name, power, health, exp, gold)


class BogImp(Enemy):
    """Small swamp imp enemy."""
    def __init__(self, name: str = "Bog Imp", power: int = 5, health: int = 80, exp: int = 7, gold: int = 30) -> None:
        super().__init__(name, power, health, exp, gold)


class Hobgoblin(Enemy):
    """Stronger goblinoid enemy."""
    def __init__(self, name: str = "HobGoblin", power: int = 6, health: int = 100, exp: int = 10, gold: int = 35) -> None:
        super().__init__(name, power, health, exp, gold)
