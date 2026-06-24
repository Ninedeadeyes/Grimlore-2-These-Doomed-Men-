from __future__ import annotations
from typing import List, TYPE_CHECKING
import armour
import weapon
import msvcrt

if TYPE_CHECKING:
    from player import Player

def order(bag: List) -> None:
    """Print numbered list of items in the player's bag."""
    for x in range(len(bag)): 
        print(x + 1, str(bag[x]))


def play_instruction() -> None:
    """Display basic movement and inventory instructions."""
    print(" Instructions ")   
    print(" Movement: WASD, Inventory : I ")  


def commands(player: Player) -> None:
    """Handle player input for movement, inventory, and equipment."""
    print("                                   ")
    print("                                    ")
    print(f" Level:{player.level} Health: {player.health} Power: {player.power} Gold: {player.gold}")
    print(f" Armour: {player.armour.name} + {player.armour.protection} Protection    Weapon: {player.weapon.name} + {player.weapon.damage} Damage")

    while True:        # ignores all non instruction keypress 
        instruction = msvcrt.getch()

        # Movement
        if instruction in {b'w', b'W'}:  # Up
            player.y -= 1
            break
                
        if instruction in {b's', b'S'}:  # Down
            player.y += 1
            break
        
        if instruction in {b'd', b'D'}:  # Right
            player.x += 1
            break
                
        if instruction in {b'a', b'A'}:  # Left
            player.x -= 1
            break

        # Inventory
        if instruction in {b'i', b'I'}:
            print("Bag(B), Change(C), Exit(E)")

            while True:
                instruction = msvcrt.getch()

                # Bag
                if instruction in {b'b', b'B'}:
                    if player.inventory == [""]:
                        print("Your bag is empty")
                    else:
                        order(player.inventory)

                    print("Press E to Exit")

                # Change equipment
                if instruction in {b'c', b'C'}:
                    print("Weapon (W), Armour(A), Exit(E)")

                    while True:
                        instruction = msvcrt.getch()

                        # Equip weapon
                        if instruction in {b'w', b'W'}:
                            Weapons = [item for item in player.inventory if isinstance(item, weapon.Weapon)]
                                
                            if not Weapons:
                                print("You do not have any Weapon to equip")
                                print("Press E for Exit")
                                break

                            print(" Choose a Weapon to equip :")
                            for i, item in enumerate(Weapons, 1):
                                print(f"{i}. {item}")

                            valid = False
                            while not valid:
                                choice = input("")
                                try:
                                    old_weapon = player.weapon
                                    player.inventory.remove(Weapons[int(choice) - 1])
                                    player.weapon = Weapons[int(choice) - 1]
                                    player.inventory.append(old_weapon)
                                    print("You arm yourself with:", Weapons[int(choice) - 1])
                                    print("Press E for Exit")
                                    valid = True
                                    break

                                except (ValueError, IndexError):
                                    print("Invalid choice, try again")
                                        
                            break

                        # Equip armour
                        if instruction in {b'a', b'A'}:
                            Armours = [item for item in player.inventory if isinstance(item, armour.Armour)]
                                
                            if not Armours:
                                print("You do not have any Armour to equip")
                                print("Press E for Exit")
                                break

                            print(" Choose an Armour to equip :")
                            for i, item in enumerate(Armours, 1):
                                print(f"{i}. {item}")

                            valid = False
                            while not valid:
                                choice = input("")
                                try:
                                    old_armour = player.armour
                                    player.inventory.remove(Armours[int(choice) - 1])
                                    player.armour = Armours[int(choice) - 1]
                                    player.inventory.append(old_armour)
                                    print("You equip yourself with:", Armours[int(choice) - 1])
                                    print("Press E for Exit")
                                    valid = True
                                    break

                                except (ValueError, IndexError):
                                    print("Invalid choice, try again")
                                
                            break

                        # Exit equipment menu
                        if instruction in {b'e', b'E'}:
                            break

                # Exit inventory menu
                if instruction in {b'e', b'E'}:
                    break

            break
