
from __future__ import annotations
import title_screen
import events
import maps
import player
import instructions
import sound

def main() -> None:
    """Main game loop: initializes the player, map, and handles all movement + events."""
    # This is the player (level, exp, health, power, gold, x, y):
    hero = player.Player(1, 0, 100, 10, 0, 4, 4)   # x and y is also the starting position for map 1 
    game_loop = True   # initiate game loop
    sound.play_background_music("Music/intro.wav")  # background music 
    title_screen.intro()  # Provide a description/setting/title screen of the game before it begins  
    sound.play_background_music("Music/background.wav") 
    # Clears the screen, prints the map, initializes backend + frontend, returns tile under player
    position = maps.clear_screen(hero)

    while game_loop:
        maps.recall_step(hero)  # Capture previous x,y for solid interaction  
        maps.flush(hero)        # Remove previous @ so the player doesn't leave a trail  
        instructions.commands(hero)  # Movement + inventory commands  
        position = maps.clear_screen(hero)  # Return backend tile at new position
        
        # TILE LOGIC
        if position == ".":           
            events.random_event(hero)  # Random encounter  

        if position == "#":
            maps.solid_interaction(hero, "#")
            print("You hit a wall..")

        if position == ">":
            maps.going_downstairs(hero)

        if position == "<":
            maps.going_upstairs(hero)

        if position == "B":
            if hero.got_lantern_for_quest==True:
                maps.data_map_choice[hero.y][hero.x] = "."
                print(" The lantern's warm glow pacifies even the darkest shadows. You move ahead")  
            else:
                maps.solid_interaction(hero, ".")
                print("The darkness here is much too great. You cannot move forward") 


        # Floor 1 

        if position == "K":
            maps.solid_interaction(hero, "K")
            events.mad_king(hero) 

        if position == "J":
            maps.solid_interaction(hero, "J")
            events.jester(hero) 
            
        if position == "H":
            maps.solid_interaction(hero, "H")
            events.horde(hero) 

        if position == "C":
            if events.sword_found(hero):
                maps.data_map_choice[hero.y][hero.x] = "."    
            else:
                maps.solid_interaction(hero, "C")

            position = maps.clear_screen(hero)

        if position == "D":
            if hero.got_key_for_quest:
                maps.data_map_choice[hero.y][hero.x] = "."
                print("You open the door")
            else:
                maps.solid_interaction(hero, "D")
                print("The King's door is locked, you must find a way in")           

        #Floor 2 

        if position == "A":
            if events.abomination(hero):
                maps.data_map_choice[hero.y][hero.x] = "."     
            else:
                maps.solid_interaction(hero, "A")

            position = maps.clear_screen(hero)

        if position == "W":
            maps.visual_map_choice[hero.y][hero.x] = "W"
            events.warning(hero) 

        if position == "P":
            if events.priest_found(hero):
                maps.data_map_choice[hero.y][hero.x] = "."     
            else:
                maps.solid_interaction(hero, "P")
            
            position = maps.clear_screen(hero)
            
        if position == "R":
            maps.solid_interaction(hero, "R")
            events.ragman_found(hero)
            position = maps.clear_screen(hero) 

        #Floor 3  

        if position == "n":
            events.nursery_found(hero) 
            maps.solid_interaction(hero, "t")
            position = maps.clear_screen(hero) 


        if position == "S":
            maps.solid_interaction(hero, "S")
            events.statue_found(hero)
            position = maps.clear_screen(hero)


        if position == "G":
            if events.chainmail_found(hero):
                maps.data_map_choice[hero.y][hero.x] = "."   
                
            else:
                maps.solid_interaction(hero, "G")
            
            position = maps.clear_screen(hero)  

        if position == "T":
            if events.troll(hero):
                maps.data_map_choice[hero.y][hero.x] = "."     
            else:
                maps.solid_interaction(hero, "T")

            position = maps.clear_screen(hero)

        # Floor 4 

        if position == "p":
            maps.solid_interaction(hero, "P")
            events.alive_priest_found(hero)
            position = maps.clear_screen(hero)     

        if position == "s":
            if events.shadow_beast(hero):
                maps.data_map_choice[hero.y][hero.x] = "."     
            else:
                maps.solid_interaction(hero, "B")

            position = maps.clear_screen(hero)

        if position == "N":
            if events.noble_found(hero):
                maps.data_map_choice[hero.y][hero.x] = "."     
            else:
                maps.solid_interaction(hero, "N")
            
            position = maps.clear_screen(hero)

        if position == "L":
            if events.lantern_found(hero):
                maps.data_map_choice[hero.y][hero.x] = "."     
            else:
                maps.solid_interaction(hero, "L")
            
            position = maps.clear_screen(hero)

     # Floor 5
   
        if position == "F":
            maps.solid_interaction(hero, "F")
            events.fountain(hero)
            position = maps.clear_screen(hero) 

        if position == "k":
            if events.key_found(hero):
                maps.data_map_choice[hero.y][hero.x] = "."     
            else:
                maps.solid_interaction(hero, "k")
            
            position = maps.clear_screen(hero)
            

    
if __name__ == "__main__":
    main()