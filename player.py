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
        self.armour: armour.Armour = armour.LeatherTunic()
        self.weapon: weapon.Weapon = weapon.GlassShank()

        # Stats
        self.level: int = level
        self.exp: int = exp
        self.health: int = health
        self.full_health: int = 100
        self.power: int = power
        self.full_power: int = 10
        self.gold: int = gold
        self.rage: int=0
        self.victory=False
        self.escaped=False

        # Position
        self.x: int = x
        self.y: int = y

        # Quests/Events 
        self.got_key_for_quest: bool = False
        self.got_lantern_for_quest: bool = False
        self.first_ragman_encounter: bool = True
        self.buried: bool = False
        self.holy_mail_got: bool = False
        self.claymore_got: bool= False
        self.shadow_beast_found: bool= False
        self.paw_handed_in: bool= False
        self.first_alive_priest_encounter : bool= False

    