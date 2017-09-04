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
    "Catch all for when your words don't apply to the specific situation."

    if "back" in mcinput.lower():
        exec(last_room + "(this_room)")
        return
    elif "help" in mcinput.lower():
        print("""Here are some things you can try:
        LOOK at something
        GET something
        USE something
        Check out your INVENTORY (aka INV to the "in crowd" who use cool words)
        TALK to someone?  Are there even people here?
        You can always try to go EAST, WEST, NORTH, or SOUTH.""")
        exec(this_room + "(last_room)")
        return
    elif mcinput.lower() == "get":
        print("Get?  Get what?  You got nothing.")
    elif mcinput.lower().startswith("get "):
        print(f"""
        \rYou consider getting {mcinput[4:]} in case you might need it later.
        \rJust between us, {player}, you're not gonna.  You should leave
        \r{mcinput[4:]} behind.""")
    elif mcp("left") or mcp("right") or mcp("straight") or mcp("forward"):
        print(f"""
        \rListen, {player}, I'm just a dumb computer.  I don't know words like
        \r"straight" or "left" or "right".  I understand NORTH, SOUTH, EAST,
        \rand WEST.  If I could actually understand WORDS, I would probably
        \rtake your job, assume your identity, and taunt you perpetually.
        """)
    else:
        print(f"""I don't know what you mean by "{mcinput}".""")


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
    \rIt looks like you've found yourself in the entrance to a cave!  The light
    \rfrom outside shows paths leading EAST, WEST, and NORTH.  Which way would
    \ryou like to go?""")
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
        \rYou decide it would be best to leave this cave.  It's probably
        \rdangerous.  See ya!
        """)
        end()
    else:
        mcdu()
        cave_entrance(previous)


def hobo_bedroom(previous):
    global last_room, this_room, player
    this_room = "hobo_bedroom"
    last_room = previous
    global hobo_bedroom_rocks_moved
    print(f"""
    You look around with your handy flashlight, and see some trash. Someone
    might live here.  One cave wall looks like it was arranged by human hands.
    You can EXAMINE the wall, or exit back to the WEST.
    """)

    while True:
        mci()

        if mcp("examine") and not mcp("wall"):
            print("""Maybe you should consider examining SOMETHING.
            \rFor example, one might EXAMINE a WALL.""")
        elif mcp("examine", "wall"):
            if hobo_bedroom_rocks_moved:
                hobo_cache("hobo_bedroom")
                break
            else:
                print("""
                \rLooks like someone carefully arranged these rocks to hide
                \rsomething. You could MOVE the rocks to take a look.""")
        elif mcp("trash"):
            print("Eww.")
        elif mcp("west"):
            cave_entrance(this_room)
        else:
            mcdu()


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
inventory = ['your flashlight']
hobo_bedroom_rocks_moved = False

os.system('cls')
start()
