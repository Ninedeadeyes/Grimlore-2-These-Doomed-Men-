from __future__ import annotations
import msvcrt
import random
import maps
import events
from typing import TYPE_CHECKING

# This block allows the code to "see" the definitions for the type hints 
# without causing the circular import crash at runtime.
if TYPE_CHECKING:
    from player import Player
    from enemy import Enemy 

def fight(player: Player, enemy: Enemy) -> None:
    """Run a full combat encounter between the player and an enemy."""
        
    print("\033c", end="")
    battle = True
    print("An enemy appears, ready to fight")

    
    while battle:
      
        print(f"{enemy.name} hp:{enemy.health} Power:{enemy.power}")
        print(" " * 100) # Simplified long empty strings
        print(f"Player hp:{player.health} Power:{player.power} Rage:{player.rage}")
        print(" " * 100) 
        print("What is your next action: Attack (A), Rage (R), Escape(E)")

        while True:
            choice = msvcrt.getch()

            # -------------------------
            # ATTACK
            # -------------------------
            if choice in {b'a', b'A'}:
                
                enemy_dice_roll = random.randint(1, 6)
                player_dice_roll = random.randint(1, 6)

                enemy_damage_total = max(0, enemy.power + enemy_dice_roll - player.armour.protection)
                player.health -= enemy_damage_total

                player_damage_total = player.power + player_dice_roll + player.weapon.damage
                enemy.health -= player_damage_total

                print(f"The {enemy.name} attacks you for {enemy_damage_total} damage. Your health is {player.health}")
                print(f"You attack the {enemy.name} and deal {player_damage_total} damage. The {enemy.name} health is {enemy.health}")                 

                if player.health <= 0:
                    events.death(player)

                if enemy.health <= 0:
                    print(f"You win the fight against the {enemy.name}")
                    player.exp += enemy.exp
                    player.gold += enemy.gold
                    print(f"You gain {enemy.gold} gold ")
                    events.check_level_up(player)
                    input("Press enter to continue")
                    battle = False
                    break
                if player.rage<20:
                    player.rage+=2    
                input("Press any key to continue")
                print("\033c", end="")
                break
            # -------------------------
            # Rage
            # -------------------------
            if choice in {b'r', b'R'}:
                
                while True:
                    while True:
                        print("Rage Attacks")
                        print("Power Blow(3 Rage):(P)")
                        print("Frenzy(6 Rage):(F)")
                        
                        choice = msvcrt.getch()

                        if choice in {b'p', b'P'}:
                            if player.rage>=3:
                                player_dice_roll = random.randint(10, 20)
                                print("You deliver a powerful blow")
                                player.rage-=3
                            else:
                                print("You do not have enough rage ")
                                player_dice_roll = 1
                            
                            break 

                        if choice in {b'f', b'F'}:
                            if player.rage>=6:
                                player_dice_roll = random.randint(20, 30)
                                print("You unleash a brutal flurry of attacks ")
                                player.rage-=6
                            else:
                                print("You do not have enough rage ")
                                player_dice_roll = 1
                            
                            break

                        else:
                            print("\033c", end="")
                            print(f"{enemy.name} hp:{enemy.health} Power:{enemy.power}")
                            print(" " * 100) # Simplified long empty strings
                            print(f"Player hp:{player.health} Power:{player.power} Rage:{player.rage}")
                            print(" " * 100) 


                    enemy_dice_roll = random.randint(1, 6)

                    enemy_damage_total = max(0, enemy.power + enemy_dice_roll - player.armour.protection)
                    player.health -= enemy_damage_total

                    player_damage_total = player.power + player_dice_roll + player.weapon.damage
                    enemy.health -= player_damage_total

                    print(f"The {enemy.name} attacks you for {enemy_damage_total} damage. Your health is {player.health}")
                    print(f"You attack the {enemy.name} and deal {player_damage_total} damage. The {enemy.name} health is {enemy.health}")                 

                    if player.health <= 0:
                        events.death(player)

                    if enemy.health <= 0:
                        print(f"You win the fight against the {enemy.name}")
                        player.exp += enemy.exp
                        player.gold += enemy.gold
                        print(f"You gain {enemy.gold} gold ")
                        events.check_level_up(player)
                        input("Press enter to continue")
                        battle = False
                        break
  
                    input("Press any key to continue")
                    print("\033c", end="")
                    break
                break
            # -------------------------
            # ESCAPE
            # -------------------------
            if choice in {b'e', b'E'}:
                
                escape_chance = random.random()

                if escape_chance < 0.40:
                    print("You manage to escape")
                    input("Press enter to continue")
                    battle = False
                    break
                     
                else:
                    print("You do not escape")
                    enemy_dice_roll = random.randint(1, 12)
                    enemy_damage_total = max(0, enemy.power + enemy_dice_roll)
                    player.health -= enemy_damage_total

                    print(f"The {enemy.name} attacks you for {enemy_damage_total} damage. Your health is {player.health}")
                    input("Press any key to continue")
                    print("\033c", end="")

                    if player.health <= 0:
                        events.death(player)
                     
                break
        
    print("\033c", end="")
    maps.display_map(maps.visual_map_choice)