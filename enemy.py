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

class Undead(Enemy):
    def __init__(self, name: str = "Undead", power: int = 5, health: int = 40, exp: int = 5, gold: int = 10) -> None:
        super().__init__(name, power, health, exp, gold)

class Cultist(Enemy):
    def __init__(self, name: str = "Cultist", power: int = 6, health: int = 60, exp: int = 7, gold: int = 15) -> None:
        super().__init__(name, power, health, exp, gold)

class DoomKnight(Enemy):
    def __init__(self, name: str = "Doom Knight", power: int = 7, health: int = 80, exp: int = 10, gold: int = 20) -> None:
        super().__init__(name, power, health, exp, gold)

class Abomination(Enemy):
    def __init__(self, name: str = "Abomination", power: int = 8, health: int = 120, exp: int =15, gold: int = 30) -> None:
        super().__init__(name, power, health, exp, gold)

class Troll(Enemy):
    def __init__(self, name: str = "Demon Troll", power: int = 14, health: int = 180, exp: int = 50, gold: int = 40) -> None:
        super().__init__(name, power, health, exp, gold)

class ShadowBeast(Enemy):
    def __init__(self, name: str = "Beast from the Shadows", power: int = 16, health: int = 80, exp: int = 40, gold: int = 35) -> None:
        super().__init__(name, power, health, exp, gold)

class MadKing(Enemy):
    def __init__(self, name: str = "Dead End King", power: int = 20, health: int = 666, exp: int = 100, gold: int = 100) -> None:
        super().__init__(name, power, health, exp, gold)
