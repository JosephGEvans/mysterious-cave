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

    if mcinput.lower() == "get":
        print("Get?  Get what?  You got nothing.")
    elif mcp("get","flashlight"):
        print(
        """\rYou have a flashlight.  Check your INVENTORY.  Also, without a
        \rflashlight, how would you see any other FLASHLIGHTS you intend to GET?
        \rAre you hallucinating other flashlights?  Maybe you should consider
        \rtyping "GET out of this cave" where you can "GET back to reality".
        """)
    elif mcp("get", "out", "of", "this", "cave"):
        print(
        f"""\rA wise move.  You scramble all the way back out of the cave.
        \rBye, {player}.  Take it easy.  See somebody about that flashlight
        \rthing.""")
        end()
    elif mcp("get", "back", "to", "reality"):
        print("Ha!  No.  Reality continues to elude you.\n")
    elif mcinput.lower().startswith("get "):
        print(
        f"""\rYou consider "getting {mcinput[4:]}" in case you might need it
        \rlater.  Just between us, {player}:  you're not gonna.
        """)
    elif mcp("use", "flashlight"):
        print(
        f"""\rHonestly, {player}?  You're always using your flashlight.  This is
        \ra cave.
        """)
    elif mcp("use"):
        print(f"You cannot use that.")
    elif mcp("inv"):
        print("You check your inventory, and you have:")
        for item in inventory:
            print("\t" + item)
        print("\n")
    elif mcp("look"):
        exec(this_room + "(last_room)")
        return
    elif mcp("talk"):
        print("You talk, but no one listens.")
    elif mcp("back"):
        exec(last_room + "(this_room)")
        return
    elif mcp("left") or mcp("right") or mcp("straight") or mcp("forward"):
        print(f"""
        \rListen, {player}, I'm just a dumb computer.  I don't know words like
        \r"straight" or "left" or "right".  I understand NORTH, SOUTH, EAST,
        \rand WEST.  If I could actually understand WORDS, I would probably
        \rtake your job, assume your identity, and taunt you perpetually.
        """)
    elif mcp("east") or mcp("west") or mcp("north") or mcp("south"):
        print("There's nothing that way.")
    elif "help" in mcinput.lower():
        print("""Here are some things you can try:

        LOOK at something, or just LOOK around
        GET something
        USE something
        Check out your INVENTORY (aka INV to the "in crowd" who use cool words)
        TALK to someone?  Are there even people here?
        You can always try to go EAST, WEST, NORTH, or SOUTH.
        """)
        exec(this_room + "(last_room)")
        return
    else:
        print(
        f"""\rI don't know what you mean by "{mcinput}".
        \rType HELP if you need it.
        """)


def start():
    # get user's name
    print("Hello, there!  What is your name?")
    global player
    player = input("> ")
    os.system('cls')
    print(
    f"""\rWell, hello there, {player}. Tell me, how does this story sound?

    {player} is looking at a mysterious cave...
    A snake is slithering towards {player}.  Oh!
    But then, the snake keeps on going.  {player} is very relieved.

    \rIf your name looks weird there, you can change it.""")

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
            print("Great.  Let's get started!")
            cave_entrance("cave_entrance")
            break
        else:
            mcdu()
            print("Try typing 'yes' or 'no'")


def cave_entrance(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "cave_entrance"
    print(
    f"""\rIt looks like you've found yourself in the entrance to a cave!  The
    \rlight from outside shows paths leading EAST, WEST, and NORTH.  Which way
    \rwould you like to go?""")
    mci()
    # offer choices left, right, forwared, back out of the cave
    if mcp("west"):
        hobo_bedroom(this_room)
    elif mcp("east"):
        perfect_cube_room(this_room)
    elif mcp("north"):
        long_walk(this_room)
    elif mcp("south") or mcp("out") or mcp("exit") or mcp("leave"):
        print("""
        \rYou decide it would be best to leave this cave.  It's probably
        \rdangerous.  See ya!
        """)
        end()
    elif mcp("left") or mcp("right") or mcp("straight"):
        print("Try typing EAST, WEST, or NORTH.\n")
        cave_entrance(previous)
    else:
        mcdu()
        cave_entrance(previous)


def hobo_bedroom(previous):
    global last_room, this_room, player
    this_room = "hobo_bedroom"
    last_room = previous
    global hobo_bedroom_rocks_moved

    print(
    f"""\rYou're at a dead end just west of the cave entrance.  You look around
    \rand see some trash.  Someone might live here.  One cave wall looks like it
    \rwas arranged by human hands.  You can LOOK at the WALL, or exit back to
    \rthe EAST."""
    )

    while True:
        mci()

        if mcp("examine", "wall") or mcp("look", "wall"):
            if hobo_bedroom_rocks_moved:
                hobo_cache(this_room)
                break
            else:
                print(
                """\rLooks like someone carefully arranged these rocks to hide
                \rsomething. You could MOVE the rocks to take a look.""")
        elif mcp("examine"):
            print("""Maybe you should consider examining SOMETHING.
            \rFor example, one might EXAMINE a WALL.""")
        elif mcp("trash"):
            print("Eww.")
        elif mcp("east") or mcp("exit"):
            cave_entrance(this_room)
            break
        elif mcp("move", "rock"):
            hobo_bedroom_rocks_moved = True
            print("You move the rocks.  Take another look at the wall.")
        elif mcp("move"):
            print("You move.")
        else:
            mcdu()


def hobo_cache(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "hobo_cache"

    print(
    """\rWow, neat!  It's some kind of secret pile of secret stuff.  Let's see,
    \rwe have a can of "Beans", some broken glasses, a rusty harmonica, and some
    \rused, uh... used stuff.  Actually, you know what?  This is not that neat.
    """
    )
    while True:
        mci()

        if mcp("look", "stuff"):
            print("Beans, harmonica, glasses, and gross used somethings.")
        elif mcp("get", "stuff"):
            print(f"Trust me, {player}.  You don't want any of this stuff.")
        elif mcp("beans"):
            print("""It's a can of "beans".  You don't want it.  Don't get it.
            """)
        elif mcp("bean"):
            print("""What, like a single bean?  It's in the can, which you CAN't
            \ropen.  Get it?  A can?  CAN't?  Anyway, no, you may not.""")
        elif mcp("glasses"):
            print("These glasses are broken.  They might cut you.")
        elif mcp("look","used"):
            print(
            """\rYou decide to take a closer look at the... never mind.  You
            \rchanged your mind.  It is terrible and aweful and gross.""")
        elif mcp("get",  "used"):
            print(
            f"""\rWow, {player}, that is messed up.  You should probably lose
            \rthis game right now!  Consider this a warning.""")
        elif mcp("used"):
            print(
            f"""\r{player}, step away from the soiled materials.""")
        elif mcp("what"):
            print("Here's what you should do.  Back away from this hobo stash.")
        elif mcp("east"):
            cave_entrance("hobo_bedroom")
            break
        else:
            mcdu()


def perfect_cube_room(previous):
    #secret entrance to finished path
    #cant find secret entrance unless exited through it once (no seams in room)
    global last_room, this_room, player
    last_room = previous
    this_room = "perfect_cube_room"

    print(
    """\rYou've entered some kind of perfectly shaped cube room just east of the
    \rcave entrance.  The stone ceiling, ground, and walls are all cut flat and
    \rsmooth.  This must have taken a lot of long, hard work.  Who would do such
    \ra thing?  You can't see anything to do here other than exit to the WEST.
    """
    )

    while True:
        mci()

        if mcp("look", "wall"):
            print("Yep, there are walls here.  They are perfectly cut.")
        elif mcp("get"):
            print(
            """\rUm, there is nothing here to get.  You can't get anything.""")
        elif mcp("use"):
            print("Honestly, this room is very boring, and you should leave.")
        elif mcp("west") or mcp("leave") or mcp("exit"):
            cave_entrance(this_room)
            break
        else:
            mcdu()


def long_walk(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "long_walk"

    print(
    """\rYou head north into a dark passage, and walk for a long time.
    \rEventually, you reach a spot where a dark passage veers WEST, and a darker
    \rpassage continues to the NORTH.  Really, though, you should head back
    \rSOUTH and leave this scary cave."""
    )

    while True:
        mci()

        if mcp("east"):
            print(
            f"""\rYou hastily slam your face into a sold rock wall to the EAST,
            \rbecause you weren't paying attention at all when I told you that
            \rthe paths lead WEST, NORTH, and SOUTH.  {player}!""")
        elif mcp("west"):
            empty_cavern(this_room)
            break
        elif mcp("north"):
            longer_twisty_walk(this_room)
            break
        elif mcp("south") or mcp("leave"):
            cave_entrance(this_room)
            break
        else:
            mcdu()


def empty_cavern(previous):
    global last_room, this_room, player, have_stalagmite, have_stalactite
    last_room = previous
    this_room = "empty_cavern"

    print(
    """\rYou arrive in a great, empty cavern.  There are all kinds of
    \rstalagmites, and stalactites, and drippy cave sounds.  The scary path is
    \rback to the EAST.""")

    while True:
        mci()

        if mcp("get", "stalactite"):
            if have_stalactite:
                print("You already have a stalactite.  Check your INVENTORY.")
            elif have_stalagmite:
                have_stalactite = True
                inventory.insert(0, "A pointy, yet brittle stalactite")
                print(
                """\rYou already took a stalagmite.  But, hey, you need to hold
                \ra stalactite in your hand to really be sure they're different.
                \rA dark force is awakened deep, deep down in the cavern by your
                \rreckless disregard for cave preservation.  And greed.""")
            else:
                have_stalactite = True
                inventory.insert(0, "A pointy, yet brittle stalactite")
                print(
                """\rYou reach for one of the small, pointy stalactites hanging
                \rfrom the ceiling nearby.  It breaks off surprisingly easily.
                \rThe Historical Cave Preservation Society puts a warrant out
                \rfor your arrest.""")
        elif mcp("get", "stalagmite"):
            if have_stalagmite:
                print(
                """\rHow many stalagmites can you really hope to use?  There's
                \rone in your INVENTORY already.""")
            elif have_stalactite:
                have_stalagmite = True
                inventory.insert(0, "Some stalagmite you stole from somewhere")
                print(
                f"""\rNice, {player}, take both kinds.  They are 100%, totally
                \rdifferent pointy cave things.  I mean, one comes from the
                \rground, and the other from the ceiling!  You're not greedy,
                \ror anything.  It's good to have different things that are
                \rnot the same as each other.""")
            else:
                have_stalagmite = True
                inventory.insert(0, "Some stalagmite you stole from somewhere")
                print(
                """\rYou push, and pull, and finally manage to snap off a
                \rstalagmite from the ground.  It's pretty heavy.  I hope its
                \rworth being a fugitive from the Historical Cave Preservation
                \rSociety for the rest of your days.  They'll definitely be
                \rtalking bad about you on the Internet.""")
        elif mcp("east"):
            long_walk(this_room)
            break
        else:
            mcdu()



def longer_twisty_walk(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "longer_twisty_walk"
    #climb up
    #climb down
    pass


def vast_expanse(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "vast_expanse"
    pass


def narrow_squeeze(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "narrow_squeeze"
    #forward
    #back
    pass


def open_cavern(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "open_cavern"
    #pool
    #door?
    pass


def transition_hall(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "transition_hall"
    #leads to finished room
    #door requiring a key (found back in the cave somewhere...)
    #back
    pass


def finished_room(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "finished_room"
    #back to transition hall
    #left door to bathroom
    #straight ahead to bedroom
    #right door to finished hall
    pass


def bath_room(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "bath_room"
    #toilet
    #shower
    #med cabinet
    #finished room
    pass


def bed_room(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "bed_room"
    #finished room
    pass


def finished_hallway(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "finished_hallway"
    #kitchen
    #study
    #finished_room
    pass


def kitchen(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "kitchen"
    #back_porch
    #hallway
    pass


def back_porch(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "back_porch"
    # overlook pool in open cavern
    pass


def study(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "study"
    #library
    #desk
    #secret entrance
    pass


def secret_room(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "secret_room"
    #confrontation?
    #exit to finished path
    pass


def finished_path(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "finished_path"
    #leads back to cube room
    pass


def end():
    exit(0)


this_room = ""
last_room = ""
inventory = [
    "A flashlight, which you've been using to light up this dark cave"
    ]
hobo_bedroom_rocks_moved = False
have_stalactite = False
have_stalagmite = False

os.system('cls')
start()
