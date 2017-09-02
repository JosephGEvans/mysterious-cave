from sys import exit
import os


def mci():
    "Mystery Cave Input"
    "Updates a global variable called 'mcinput' with input from the user."
    global mcinput
    mcinput = input("> ")
    os.system('cls')

def mcp(*certainWords):
    "Mystery Cave Parser"
    "Compares strings with input string and returns True or False"
    "[will accept] strings, variables, and boolean operators like NOT"
    thereOrNotThere = True
    for word in certainWords:

        if word.lower() in mcinput.lower():
            thereOrNotThere = thereOrNotThere and True
        else:
            thereOrNotThere = thereOrNotThere and False

    return thereOrNotThere


def mcdu():
    "Mystery Cave Don't Understand"
    "Generic way of saying you typed the wrong stuff."
    print(f"I don't know what you mean by {mcinput}")


def start():
    # get user's name
    print("Hello, there!  What is your name?")
    global player
    player = input("> ")
    os.system('cls')
    print(f"""
    Well, hello there, {player}.
    Tell me, {player}, how does this story sound:

    {player} is looking at a mysterious cave...
    A snake is slithering towards {player}!
    Oh! But then, the snake keeps on going.
    {player} is very relieved.

    If your name looks weird there, you can change it.
    """)

    while True:
        print("Would you like to change your name?")
        mci()

        if mcp("yes"):
            print("Ok, we can start again.")
            start()
            break
        elif mcp("no", "thank"):
            print("So polite!  Ok, here we go.")
            cave_entrance()
            break
        elif mcp("no"):
            print("Great!  Let's get started.")
            cave_entrance()
            break
        else:
            mcdu()
            print("Try typing 'yes' or 'no'")


def cave_entrance():
    # describe the environment
    print(f"""
    It looks like you've found yourslef in the entrance to a cave!
    The light from outside shows paths leading EAST, WEST, and NORTH.
    Which way would you like to go?
    """)
    mci()
    # offer choices left, right, forwared, back out of the cave
    if mcp("east"):
        hobo_bedroom()
    elif mcp("west"):
        perfect_cube_room()
    elif mcp("north"):
        long_walk()
    elif mcp("south") or mcp("back") or mcp("out") or mcp("exit") or mcp("leave"):
        print("""
        You decide it would be best to leave this cave.  It's probably dangerous.
        See ya!
        """)
        end()
    else:
        mcdu()
        cave_entrance()


def hobo_bedroom():
    pass


def perfect_cube_room():
    #secret entrance to finished path
    #cant find secret entrance unless exited through it once (no seams in room)
    pass


def long_walk():
    pass


def empty_cavern():
    pass


def longer_twisty_walk():
    #climb up
    #climb down
    pass


def vast_expanse():
    pass


def narrow_squeeze():
    #forward
    #back
    pass


def open_cavern():
    #pool
    #door?
    pass


def transition_hall():
    #leads to finished room
    #door requiring a key (found back in the cave somewhere...)
    #back
    pass


def finished_room():
    #back to transition hall
    #left door to bathroom
    #straight ahead to bedroom
    #right door to finished hall
    pass


def bath_room():
    #toilet
    #shower
    #med cabinet
    #finished room
    pass


def bed_room():
    #finished room
    pass


def finished_hallway():
    #kitchen
    #study
    #finished_room
    pass


def kitchen():
    #back_porch
    #hallway
    pass


def back_porch():
    # overlook pool in open cavern
    pass


def study():
    #library
    #desk
    #secret entrance
    pass


def secret_room():
    #confrontation?
    #exit to finished path
    pass


def finished_path():
    #leads back to cube room
    pass


def end():
    exit(0)


os.system('cls')
start()
