from __future__ import annotations
from typing import List
import weapon
import armour


class Player:
    """Player entity storing stats, equipment, position, inventory and quest flags."""

    def __init__(self,level: int,exp: int,health: int,power: int,gold: int,x: int,y: int) -> None:
        
        self.alive: bool = True
        self.inventory: List[str] = ["Bone Flute"]

        # Equipment
        self.armour: armour.Armour = armour.Rags()
        self.weapon: weapon.Weapon = weapon.Dagger()

        # Stats
        self.level: int = level
        self.exp: int = exp
        self.health: int = health
        self.full_health: int = 100
        self.power: int = power
        self.full_power: int = 12
        self.gold: int = gold
        self.rage: int=0

        # Position
        self.x: int = x
        self.y: int = y

        # Quests
        self.spoon_quest: bool = False
        self.got_spoon_for_quest: bool = False