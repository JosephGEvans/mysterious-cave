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


    if "back" in mcinput.lower():
        exec(last_room + "(this_room)")
        return

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
            cave_entrance("cave_entrance")
            break
        elif mcp("no"):
            print("Great!  Let's get started.")
            cave_entrance("cave_entrance")
            break
        else:
            mcdu()
            print("Try typing 'yes' or 'no'")


def cave_entrance(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "cave_entrance"
    print(f"""
    Well, {player}, it looks like you've found yourself in the entrance to a cave!
    The light from outside shows paths leading EAST, WEST, and NORTH.
    Which way would you like to go?
    """)
    mci()
    # offer choices left, right, forwared, back out of the cave
    if mcp("east"):
        hobo_bedroom(this_room)
    elif mcp("west"):
        perfect_cube_room(this_room)
    elif mcp("north"):
        long_walk(this_room)
    elif mcp("south") or mcp("out") or mcp("exit") or mcp("leave"):
        print("""
        You decide it would be best to leave this cave.  It's probably dangerous.
        See ya!
        """)
        end()
    else:
        mcdu()
        cave_entrance(previous)


def hobo_bedroom(previous):
    this_room = "hobo_bedroom"
    last_room = previous
    #TEST>>
    print(f"this_room:  {this_room}")
    print(f"previous:  {previous}")
    print(f"last_room:  {last_room}")
    print(f"""
    You look around with your handy flashlight, and see some trash. Someone
    might live here.  One cave wall looks like it was arranged by human hands.
    You can EXAMINE the wall, or exit back to the WEST.
    """)

    while True:
        mci()

        if mcp("examine") and not mcp("wall"):
            print("Maybe you should consider examining SOMETHING. Like, the wall, for example.")
        elif mcp("examine", "wall"):
            print("Looks like someone carefully arranged these rocks to...")
            # This will get complicated.
        elif mcp("trash"):
            print("Ew.")
        elif mcp("west"):
            cave_entrance()


def hobo_cache():
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


this_room = ""
last_room = ""

os.system('cls')
start()
