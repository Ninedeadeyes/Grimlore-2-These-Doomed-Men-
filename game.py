
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
    hero = player.Player(1, 0, 100, 10, 0, 2, 2)   # x and y is also the starting position for map 1 

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
  
        # -------------------------
        # TILE LOGIC
        # -------------------------

        if position == ".":           
            events.random_event(hero)  # Random encounter  

        if position == "#":
            maps.solid_interaction(hero, "#")
            print("You hit a wall..")

        if position == "M":
            maps.solid_interaction(hero, "M")
            events.mad_king(hero) 

        if position == "H":
            maps.solid_interaction(hero, "H")
            events.horde(hero) 
             
        if position == "K":
            taken = events.key_found(hero)

            if taken:
                # Remove the K from backend so event cannot trigger again
                maps.data_map_choice[hero.y][hero.x] = "."     
                
            else:
                # If player refuses key, push them back
                maps.solid_interaction(hero, "K")
            position = maps.clear_screen(hero) 
            
        if position == "C":
            taken = events.sword_found(hero)

            if taken:
                # Remove the K from backend so event cannot trigger again
                maps.data_map_choice[hero.y][hero.x] = "."
                      
            else:
                # If player refuses key, push them back
                maps.solid_interaction(hero, "C")
            position = maps.clear_screen(hero) 


        if position=="D":

            if hero.got_key_for_quest==True:
              maps.data_map_choice[hero.y][hero.x] = "."
              print("You open the door")

            else:
                maps.solid_interaction(hero, "D")
                print("The door is locked")


        if position == ">":
            maps.going_downstairs(hero)

        if position == "<":
            maps.going_upstairs(hero)

if __name__ == "__main__":
    main()
