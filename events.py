from __future__ import annotations
from typing import List, TYPE_CHECKING
import random
import msvcrt
import battle
import weapon
import armour
import enemy
import sys
import animations
import sound
import time

if TYPE_CHECKING:
    from player import Player

nothing_list: List[str] = [
    "You look for deadly traps but find none",
    "You find nothing of interest here, maybe next time",
    "Wait..You hear something..It must be your imagination",
    "You find nothing of interest here"
]

def win() -> None:
    print("\033[H\033[J", end="")
    sound.play_background_music("Music/win_music")
    print("You have defeated the Mad King... Kingslayer.")
    print("Vengeance has been dealt, yet your heart remains cold.")
    print("You fight the endless horde, waiting for the darkness to consume all.")
    input("Press enter to continue your struggle")
    animations.ending()
    print("The darkness consumes... ")
    time.sleep(2)
    print("GAME OVER")
    input("Press enter to exit")
    sys.exit()

def death(player: Player) -> None:
    """End the game if the player's health reaches zero."""
    if player.health <= 0:
        sound.play_music_once("Music/death_music")
        animations.rip()
        print("Wounds upon wounds, you fall to your death")
        print("GAME OVER")
        input("Press enter to exit")
        sys.exit()

def check_level_up(player: Player) -> None:
    """Check if the player levels up and apply stat increases."""
    if player.exp > 15 * player.level:
        player.level += 1
        player.exp = 0
        print(f"You have gained a level. You are now level {player.level}")
        print("What would you like to increase: Power(P) or Health(H) ?")

        while True:
            level_up_choice = msvcrt.getch()

            if level_up_choice in {b'p', b'P'}:
                power_increase = random.randint(4, 6)
                player.full_power += power_increase
                player.power = player.full_power
                player.health = player.full_health
                print(f"Your power has increased by {power_increase}")
                print(f"Your power is now {player.power}")
                break
            
            if level_up_choice in {b'h', b'H'}:
                health_increase = random.randint(30, 40)
                player.full_health += health_increase
                player.health = player.full_health
                print(f"Your health has increased by {health_increase}")
                print(f"Your health is now {player.health}")
                break

        player.exp = 0

def random_event(player: Player) -> None:
    """Trigger a random event: nothing, battle, or loot."""
    r = random.random()
    
    if r < 0.92:
        nothing_happened()
    elif r < 0.96:
        random_battle(player)                    
    else:
        loot(player)

def random_battle(player: Player) -> None:
    r = random.random()

    if r < 0.50:
        battle.fight(player, enemy.Undead())
    elif r < 0.75:
        battle.fight(player, enemy.Cultist())
    else:
        battle.fight(player, enemy.DoomKnight())

def nothing_happened() -> None:
    noEvent = random.choice(nothing_list)
    print(noEvent)

def loot(player: Player) -> None:
    gold_pickup = random.randint(1, 5)
    player.gold += gold_pickup

    if gold_pickup == 1:
        print(f"You find a gold coin on the floor")
    else:
        print(f"You find {gold_pickup} gold coins on the floor")

# 1st floor 
def horde(player: Player) -> None:
    print("You stand against the endless horde.. How futile.. ")
    input("Press enter to continue")
    random_battle(player)

def jester(player: Player) -> None:
    jester_laughs = [
        "He giggles madly",
        "He laughs morbidly",
        "He shrieks absurdly",
    ]

    jester_tips = [
        "Some stones are stone, but some are air! Trust your feet, and not your stare!",
        "A blade in the bag cuts no foe to the bone; go into your pack or you’ll perish alone!",
        "Whispers in blackness, truths hidden from sight! The deepest of secrets require your own light!",
        "Let the beast loose, let your fury collide! Unleash your great 'rage' or you’ll die deep inside!",
    ]

    print(
        "High on the walls, a mad jester hangs in chains. There is no saving him."
    )

    chosen_laugh = random.choice(jester_laughs)
    chosen_tip = random.choice(jester_tips)


    print(f"{chosen_laugh}, '{chosen_tip}'")

def sword_found(player: Player) -> None:
    print("You see your dying Captain with a sword impaled through his belly")
    print("He chokes on his own blood, crying out for help.")
    print("Do you pull the blade out ? (Yes (Y) or No (N)) ")

    while True:
        decision = msvcrt.getch()

        if decision in {b'y', b'Y'}:
            print("You wrench the sword from his stomach. He grips the blade fighting to stay alive")
            print("...but it is already too late. With a final, pitiful gasp, he dies ")
            print("You gain an Iron Sword (+5 Damage) ")
            input("Press enter to continue")
            player.inventory.append(weapon.Sword())
            return True
            
        if decision in {b'n', b'N'}:
            print("You decide against it, as doing so would mean certain death for him ")
            input("Press enter to continue")
            return False

def mad_king(player: Player) -> None:
    print("At last, you face your King—but something is.... wrong.")
    print("He sneers at you, 'Still alive, insect?'")
    print("'My kingdom for eternal life... a fair trade.'")
    print("'Now, to complete the trade... prepare to die!'")
    input("Press enter to continue")
    battle.fight(player, enemy.MadKing())

    if player.escaped==False:

        player.victory=True

        if player.victory==True:
            print("The King falls down to the ground, broken and defeated.. ")
            print("He mutters as his mortal coil ends, 'It was all for nothing..' ")
            input("Press enter to continue")
            win()


# Floor 2 
def warning (player: Player) -> None:  
    print("You see a sign on a door written in blood")
    print("DO NOT ENTER !! CERTAIN DEATH  ")

def abomination (player: Player) -> None:   
    print("You see a horrific monstrosity ahead of you.")
    print("It wants to make you his dead pet...")
    input("Press enter to continue")
    battle.fight(player, enemy.Abomination())  

    if player.escaped==False:
        print("You defeat the abomination")
        input("Press enter to continue")
        return True 
    
    else:
        return False


def ragman_found(player: Player) -> None:
    if player.holy_mail_got==True:
        print("The Ragman mutters 'I have nothing for you today'")
        input("Press enter to continue")

    else:
         
        if player.first_ragman_encounter==True:
            print("You see a Ragman prying a set of Holy Plate Mail from a dead paladin")
            print("He gleefully declares 'Just fresh in stock, Holy Plate Mail for a mere 500 gold ?' ")
            print("Do you want to buy holy Plate Mail ? (Yes (Y) or No (N)) ")

        else:
            print("The Ragman says 'Still in stock, Holy Plate Mail for 500 gold ?' ")
            print("Do you want to buy holy Plate Mail ? (Yes (Y) or No (N)) ")

        while True:
            decision = msvcrt.getch()

            if decision in {b'y', b'Y'}:
                if player.gold>=500:
                    player.gold=player.gold-500
                    player.inventory.append(armour.HolyMail())
                    print("You gain Holy Plate + 8 Protection ")
                    player.holy_mail_got=True
                    input("Press enter to continue")
                    break
            
                else:
                    print("You do not have enough gold")
                    player.first_ragman_encounter=False
                    input("Press enter to continue")
                    break

            if decision in {b'n', b'N'}:
                print("You decide against the idea")
                player.first_ragman_encounter=False
                input("Press enter to continue")
                break

def priest_found(player: Player) -> bool:
    print("You find a dead priest on the floor") 
    print( "He has some holy water left in his pouch. Do you drink it (Yes (Y) or No (N))?")

    while True:
        decision = msvcrt.getch()

        if decision in {b'y', b'Y'}:
            print("You drink the holy water, you feel fully recovered")
            player.health=player.full_health
            input("Press enter to continue")
            return True
            
        if decision in {b'n', b'N'}:
            print("You decide to leave it")
            input("Press enter to continue")
            return False
        
# Floor 3
def statue_found(player: Player) -> None:
    if player.claymore_got==True:
        print("You pray to the War God Krakus, for strength and glory")
        input("Press enter to continue")

    else:
        print("You see a statue of the War God Krakus, holding a Mithril War Hammer")
        print("The weapon sits loose in the statue's grasp")
        print("Do you take the War Hammer (Yes (Y) or No (N)) ?")

        while True:
            decision = msvcrt.getch()

            if decision in {b'y', b'Y'}:
                    player.inventory.append(weapon.WarHammer())
                    print("You gain a Mithril War Hammer + 15 ")
                    player.claymore_got=True
                    input("Press enter to continue")
                    break
        
            if decision in {b'n', b'N'}:
                print("You decide against the idea")
                input("Press enter to continue")
                break
            
def nursery_found(player: Player) -> None:
    if player.buried==False:
        print("You find the castle's nursery...")
        print("You bury their tiny bodies calmly and with care.")
        print("Profound rage overcomes you as you depart.")
        player.rage=100
        player.buried=True
        input("Press enter to continue")
    else:
        print("You pray at the mass grave of the innocent")
        input("Press enter to continue")

def chainmail_found(player: Player) -> bool:
    print("You find a decapitated guardsman on the floor but his chain mail armour looks brand new ") 
    print( "Do you take his chain mail armour ? (Yes (Y) or No (N))?")

    while True:
        decision = msvcrt.getch()

        if decision in {b'y', b'Y'}:
            print("You take the Chainmail armour, the dead do not fight")
            print("You gain Chain Mail + 3 Protection ")
            input("Press enter to continue")
            player.inventory.append(armour.ChainMail())
            return True
            
        if decision in {b'n', b'N'}:
            print("You decide against the idea ")
            input("Press enter to continue")
            return False

#Floor 4    
def shadow_beast (player: Player) -> None:   
    print("FROM THE SHADOWS A GREAT HORROR APPEARS")
    print("Prepare for combat")
    input("Press enter to continue")
    battle.fight(player, enemy.ShadowBeast())  

    if player.escaped==False:
        print("You defeat the Beast from the Shadows")
        print("You take its Paw as evidence")
        print("You gain a Beast Paw")
        player.inventory.append("Beast Paw")
        player.shadow_beast_found=True
        input("Press enter to continue")
        return True 
    
    else:
        return False


def alive_priest_found (player: Player) -> None:
    if player.shadow_beast_found==False:

        if player.first_alive_priest_encounter==False:
            print("You see a dying Battle Priest in the corner")
            print("He tells you a Shadow Beast slew his whole unit '")
            print("and asks you to take vengeance for his fallen brothers '")
            print("'The beast is hiding in the room southwest from here '")
            player.first_alive_priest_encounter=True
            input("Press enter to continue")

        else:
            print("The Battle Priest mutters 'The beast is hiding in the room south west from here '")
            print("'Please hurry, my time is coming to an end...'")
            input("Press enter to continue")

    else: 

        if player.paw_handed_in==False:
            print(" Weakly, the priest thanks you as he splutters blood onto the floor' ")
            print("He rewards you with his old battle axe")
            print("He will not need it where he is going... ")
            print("Lastly, with his final spark of life he fully heals your wounds")
            player.health=player.full_health
            player.inventory.remove("Beast Paw")
            player.inventory.append(weapon.Axe())
            player.paw_handed_in=True
            print("You gain a Steel Axe + 10 Damage")
            print("You lose a Beast Paw")
            input("Press enter to continue")

        else:
            print("The War Priest has died.. ")
            input("Press enter to continue")


def lantern_found(player: Player) -> bool:
    print("You see a broken soldier with only his lantern by his side")
    print("He grasps at his lantern and mumbles ' It's mine... go away...' ")
    print("Do you take the lantern from him ? (Yes (Y) or No (N)) ")
    while True:
        decision = msvcrt.getch()

        if decision in {b'y', b'Y'}:
            print("You kick the broken man, and his body falls as if he were already dead.")
            print("You pick up the lantern")
            player.got_lantern_for_quest = True
            player.inventory.append("lantern")
            input("Press enter to continue")
            return True
            
        if decision in {b'n', b'N'}:
            print("You decide against the idea. You leave the broken man alone.")
            input("Press enter to continue")
            return False
        
def noble_found(player: Player) -> bool:
    print("You find a dead noble on the floor") 
    print( "He has a purse full of gold. Do you take the purse (Yes (Y) or No (N))?")

    while True:
        decision = msvcrt.getch()

        if decision in {b'y', b'Y'}:
            print("You take the purse ")
            print("Gain 350 Gold ")
            player.gold=player.gold+350
            input("Press enter to continue")
            return True
            
        if decision in {b'n', b'N'}:
            print("You decide to leave it")
            input("Press enter to continue")
            return False
#Floor 5 
def  fountain (player: Player) -> None:
    print("You see the torn and tangled bodies of three dead witches")
    print("Their final moments were clearly spent tearing each other apart in savage rage.")
    print("Upon an altar you see a fountain of blood")
    print("You have a strong urge to violently drink the fountain dry")
    print("Do you drink from the fountain? (Yes (Y) or No (N)) ")

    while True:
        decision = msvcrt.getch()

        if decision in {b'y', b'Y'}:

            if player.rage<25:
                player.rage=25
                print("You are filled with rage")
                print("Your rage has increased to 25.")
                input("Press enter to continue")
                break

            else:
                print("You drink from the fountain but nothing happens")
                print("You go off to find something to kill with your overwhelming rage..")
                input("Press enter to continue")
                break

        if decision in {b'n', b'N'}:
            print("You decide against the idea")
            input("Press enter to continue")
            break     

def troll (player: Player) -> None:   
    print("You see a 7-foot demonic Troll standing in your way ")
    print("It bellows 'Fresh meat for the slaughter !! '")
    input("Press enter to continue")
    battle.fight(player, enemy.Troll())  

    if player.escaped==False:
        print("You defeat the Troll")
        input("Press enter to continue")
        return True 
    
    else:
        return False

def key_found(player: Player) -> bool:
    print("You find the King's Guard dead on the floor. He has the keys to the King's Chambers !!") 
    print("Do you take the keys ? (Yes (Y) or No (N))?")

    while True:
        decision = msvcrt.getch()

        if decision in {b'y', b'Y'}:
            print("You pick up the key")
            player.got_key_for_quest = True
            player.inventory.append("key")
            input("Press enter to continue")
            return True
            
        if decision in {b'n', b'N'}:
            print("You decide to leave it")
            input("Press enter to continue")
            return False

