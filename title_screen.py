from __future__ import annotations
import animations
import art


def title() -> None:
    print("                                           These Doomed Men                         ")
    print("                                                                                     ")
    print("                                                                                     ")


def press_enter()->None:
    print("                                                                 ")
    input("                                   press enter to continue")
    print("\033[H\033[J", end="")

def intro() -> None:
    animations.intro_animation()
    print("The castle has been breached, your home village is burning, and your King is dead. The kingdom has fallen...                 ")
    art.castle1()
    press_enter()
    print("Yet you stand with a heavy heart and unbridled rage.           ")
    print("                                 ")
    art.castle2()
    press_enter()
    print("You march toward the cries of comrades who have yet to fall, knowing you will always be too late   ")
    print("                                 ")
    art.castle3()
    press_enter()
    print("The nightmare continues....             ")
    print("                                 ")
    art.castle4()
    press_enter()
    animations.loading_animation()
    print("Loading Complete")
    input("Press enter to continue ")

