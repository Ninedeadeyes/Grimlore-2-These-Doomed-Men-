
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
    hero = player.Player(1, 0, 100, 12, 0, 2, 2)   # x and y is also the starting position for map 1 

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

        if position == "C":
            maps.solid_interaction(hero, "C")
            events.goblin(hero) 

        if position == "G":
            maps.solid_interaction(hero, "G")
            events.goblin(hero) 

        if position == ">":
            maps.going_downstairs(hero)

        if position == "<":
            maps.going_upstairs(hero)

if __name__ == "__main__":
    main()
