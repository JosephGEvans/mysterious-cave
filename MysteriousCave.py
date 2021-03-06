from sys import exit
import os
import random
import string


def quit():
    if mcinput.lower().startswith("quit"):
        print("You quit.  Program over.  Ended.  It's done.  Exit.  Out.  Fin.")
        end()
    elif mcinput.lower() == "q":
        print(
        f"""\rOoooh, nice!  The 'Q' quit.  You've used computers before, I can
        \rsee.  Sorry you have to go, {player}.  Come back sometime?""")
        end()
    else:
        return


# fixes a bug where you would travel in the direction that you looked
def catch_look(direction):
    if mcp("look", direction):
        exec(this_room + "(last_room)")
    else:
        return


def mci():
    "Mystery Cave Input"
    "Updates a global variable called 'mcinput' with input from the user."
    global mcinput
    mcinput = input("> ")
    # strip out punctuation
    translator = str.maketrans('', '', string.punctuation)
    mcinput = mcinput.translate(translator)
    os.system('cls')

    catch_look("north")
    catch_look("south")
    catch_look("east")
    catch_look("west")
    catch_look("up")
    catch_look("down")
    quit()


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
    global have_stalactite_powder, have_door_pudge

    cant_use = [
        "You can't.",
        "Nope.",
        "You cannot use that.",
        "Try using, or getting, or doing something else.",
        "Can't use that.",
        "I'm guessing you don't have that; therefore, you can't use that."
        ]
    cant_get = [
        f"Planning to 'use {mcinput[4:]}' later on, are we?  No.",
        f"""\rYou consider "getting {mcinput[4:]}" in case you might need it
        \rlater.  Just between us, {player}:  you're not gonna.
        """,
        f"Don't try to get {mcinput[4:]}, {player}.  You shouldn't.",
        f"You cannot get {mcinput[4:]}.",
        "Nope.",
        "Can't.",
        "Don't.",
        "Stop it.  That's not a thing."
        ]


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
        print(random.choice(cant_get))
    elif mcp("throw","pillow") and have_pillow:
        print(
        """\rI'd say it's more of a "sleep pillow" than a "throw pillow"."""
        )
    elif mcp("use", "pudge") and have_door_pudge:
        print("You, uh, squish some pudge between your fingers... feels nice.")
    elif mcp("stalactite","powder") and have_stalactite_powder:
        print(
        """\rYou pull out some stalactite powder and fling it in anger.  None of
        \rit goes very far, and a small cloud floats back in your face.  Stupid
        \rstalactite!""")
    elif mcp("stalactite","powder"):
        print("You don't have any of, um, that.")
    elif mcp("use", "flashlight"):
        print(
        f"""\rHonestly, {player}?  You're always using your flashlight.  This is
        \ra cave.
        """)
    elif mcp("use"):
        print(random.choice(cant_use))
    elif mcp("inv"):
        print("You check your inventory, and you have:")
        for item in inventory:
            print("\t*  " + item)
        print("\n")
    elif mcp("look"):
        exec(this_room + "(last_room)")
        return
    elif "ok" == mcinput.lower() or "okay" == mcinput.lower():
        print("Ok?  Ok.")
    elif mcp("talk"):
        print("You talk, but no one listens.")
    elif mcp("say"):
        print(
        """\rMmm, you can't really SAY stuff in this game.  I'm... look, I'm
        \rjust not really a real person.  Sorry to disappoint you.  I have no
        \ridea what you are saying.  I can only guess it is mostly dumb stuff,
        \rbut I'll never be sure.""")
    elif mcp("back"):
        exec(last_room + "(this_room)")
        return
    elif mcp("left") or mcp("right") or mcp("straight") or mcp("forward"):
        print(
        f"""\rListen, {player}, I'm just a dumb computer.  I don't know words
        \rlike "straight" or "left" or "right".  I understand NORTH, SOUTH,
        \rEAST, and WEST.  If I could actually understand WORDS, I would
        \rprobably take your job, assume your identity, and taunt you
        \rperpetually.
        """)
    elif mcp("east") or mcp("west") or mcp("north") or mcp("south"):
        print("There's nothing that way.")
    elif "help" in mcinput.lower():
        print("""Here are some things you can try:

        LOOK at a THING, or just LOOK around
        GET some THING
        USE one of your THINGS
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
    f"""\rWell, hello there, {player}. Here's a story I made about you.

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
    global last_room, this_room, player, you_win, you_lose
    last_room = previous
    this_room = "cave_entrance"

    if you_win:
        print(
        f"""\rAaaaaand here you are, back at the beginning.  You've basically
        \rwon the game, at this point.  You may exit to the SOUTH.  Feel free to
        \rexplore the cave some more, you know, if your into that sort of thing.
        \rOh, and {player}?  Nice job.  I'd wink at you if I weren't some kind
        \rof disembodied cave voice, eh, text, uh, guy.  Thing.
        """)
        you_win = False
    elif you_lose:
        print(
        f"""\rWell.  Here you are.  This is the entrance you came in.  Seems
        \rlike maybe you're not welcome here anymore, {player}.  You should, you
        \rknow, look into exiting to the SOUTH.  That way.  SOUTH way.""")
        you_lose = False
    else:
        print(
        f"""\rIt looks like you've found yourself in the entrance to the cave!
        \rThe light from outside shows paths leading EAST, WEST, and NORTH.
        \rWhich way would you like to go, {player}?""")

    while True:
        mci()
        # offer choices left, right, forwared, back out of the cave
        if mcp("west"):
            hobo_bedroom(this_room)
            break
        elif mcp("east"):
            perfect_cube_room(this_room)
            break
        elif mcp("north"):
            long_walk(this_room)
            break
        elif mcp("south") or mcp("out") or mcp("exit") or mcp("leave"):
            print("""
            \rYou decide it would be best to leave this cave.  It's probably
            \rdangerous.  See ya!
            """)
            end()
        elif mcp("left") or mcp("right") or mcp("straight") or mcp("back"):
            print("Try typing EAST, WEST, or NORTH.\n")
            cave_entrance(previous)
            break
        else:
            mcdu()
            cave_entrance(previous)
            break


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
        elif mcp("move", "rock") or mcp("use", "rock"):
            hobo_bedroom_rocks_moved = True
            print("You move the rocks.  Take another look at the wall.")
        elif mcp("move"):
            print("You move a little.  Oh, did you want to move some THING?")
        else:
            mcdu()


def hobo_cache(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "hobo_cache"

    print(
    """\rWow, neat!  It's some kind of secret pile of secret stuff.  Let's see,
    \rwe have a rusty harmonica, a can of "Beans", some broken glasses, and some
    \rused, uh... used stuff.  Actually, you know what?  This is not that neat.
    \rHead back EAST before you catch leprosy, or something.""")
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
    global key_identified, key_gag_initiated, key_gag_concluded
    global cube_room_secret_door_visible
    last_room = previous
    this_room = "perfect_cube_room"

    cant_get_key = [
        "You try to pick up the key, but you can't.  Is it stuck?",
        "You try to get the key.  You can't.",
        "Wait a second... is this even a real key?",
        "The key is suspiciously attached to the floor.",
        "It seems like it is part of the floor."
        ]
    cant_use_key = [
        "Ha Ha Ha!  No.",
        "Oh, that would be nice if it worked, wouldn't it?",
        "Oh, my, this is so amazing!  Try some more stuff.",
        f"{player}, you have no idea how amusing it is to see you struggle.",
        "Heh.  Maybe if you hold it a certain way...",
        "Really, try the same thing again.  This time it will work.",
        "Ha!  As if.",
        "I don't think you're going to get very far with that strategy.",
        "Okay, okay, okay.  This could work!  Move a little to the left first.",
        "It is COULD be impossible to get that key.  But keep trying!"
        ]

    print(
    """\rYou've entered some kind of perfectly shaped cube room just east of the
    \rcave entrance.  The stone ceiling, ground, and walls are all cut flat and
    \rsmooth.  This must have taken a lot of long, hard work.""")

    if cube_room_secret_door_visible:
        print(
        """\rYou can see the outline of a secret hatch now.  There is even a
        \rconvenient natural-looking handhold.  You can go DOWN the hatch, or
        \rhead WEST to the cave entrance.""")
    else:
        print("You don't see much to do here other than exit to the WEST.")

    look_key_gag_ended = """
    \rThere is a key on the floor that you can't pick up.  Remember how funny
    \rthat was?  I do!"""

    look_key_gag_shiny = """
    \rThere is a shiny object on the floor.  Was that there before?"""

    look_key_gag_key = "There is a shiny key on the floor."

    if key_gag_concluded:
        print(look_key_gag_ended)
    elif key_identified:
        print(look_key_gag_key)
    elif key_gag_initiated:
        print(look_key_gag_shiny)


    while True:
        mci()

        if mcp("look", "wall"):
            print("Yep, there are walls here.  They are perfectly cut.")
        elif mcp("look","shiny"):
            key_identified = True
            print(
            """\rIt looks like a key.  I wonder if it fits in that door back
            \rin that cavern with the glowing pool.""")
        elif mcp("look","key"):

            if key_identified:
                print(
                """\rThis key looks like it would go to the door by the glowing
                \rpool, deeper in the cave.""")
            else:
                print("Key?  What key?  I don't know what you're talking about.")

        elif mcp("get","key"):

            if key_identified:
                print(random.choice(cant_get_key))
            else:
                print(
                """\rYou see no keys here, but if there were a key you probably
                \rcouldn't get it for maddening reason.""")

        elif mcp("use","on","key") or mcp("use","with","key"):

            if key_gag_concluded:
                print(
                """\rAs awesome as that was... its over now.  Go away.""")
            elif key_identified:
                print(random.choice(cant_use_key))
            else:
                print("I have no earthly idea what you are asking for.")

        elif mcp("use","key"):
            print("How would that work?")
        elif mcp("get"):
            print(
            """\rUm, there is nothing here to get.  You can't get anything.""")
        elif mcp("use"):
            print("Honestly, this room is very boring, and you should leave.")
        elif mcp("down") and cube_room_secret_door_visible:
            print("You open the secret hatch, and head down the stairs.")
            finished_path(this_room)
            break
        elif mcp("hatch") and not cube_room_secret_door_visible:
            print(f"Ha!  Ha.  Ha.  There's no secret hatch in here.  {player}!")
        elif mcp("down"):
            print(f"Down, {player}?  You can't go down.  Don't be silly.")
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
    """\rYou're in a dark passage, and walk for a long time.  Eventually, you
    \rreach a spot where the dark passage veers WEST, an even darker passage
    \rcontinues to the NORTH, and a nice, safe-looking passage leads SOUTH.""")

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
    """\rThis is a great, big, empty cavern.  There are all kinds of
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
                \rworth carrying this thing around, considering you will be a
                \rfugitive from the Historical Cave Preservation Society for the
                \rrest of your days.""")

        elif mcp("look","stalactite"):
            print("Yeah, look!  Stalactites!")
        elif mcp("look","stalagmite"):
            print(f"Well, will you look at that.  {player}, look:  stalagmites!")
        elif mcp("talk"):
            print(
            """\rOooh, listen:  Echos!
            \r\tEchos
            echos
            \rHEY
            \r\tHEY
            hey
            \rLEGGO MY ECHO!
            \r\tLEGGO My Echo
            \tleggo my echo
            """)
        elif mcp("east"):
            long_walk(this_room)
            break
        else:
            mcdu()


def longer_twisty_walk(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "longer_twisty_walk"

    look_from_south = """The passage twists.  It turns.  It climbs.  It drops.
    \rIt gets creepier, and darker, and danker.
    \rIn front of you the passage splits:  one way leads UP, the other DOWN.
    \rYou could leave, you know.  Type SOUTH three times and you're safe in
    \rthe sunshine.  I mean, as safe as you can be with murderers and theives
    \rand politicians out there."""

    look_from_north = """You're in a twisty, turny, climby, fally, creepy, dank,
    \rdark passage.  The cave entrance is back to the SOUTH.  There are also
    \rpassages leading UP and DOWN."""

    if last_room == "long_walk":
        print(look_from_south)
    else:
        print(look_from_north)

    while True:
        mci()

        if "south south south" in mcinput.lower():
            print(
            f"You leave in a super hurry.  Good idea.  Good bye, {player}.")
            end()
        elif mcp("east") or mcp("west"):
            print("Can't go that way; just UP, DOWN, or SOUTH.")
        elif mcp("UP"):
            vast_expanse(this_room)
            break
        elif mcp("DOWN"):
            narrow_squeeze(this_room)
            break
        elif mcp("north"):
            print(
            f"""\rYou run NORTH, as fast as you can, and crash cartoonishly into
            \rthe rock divider between two passages leading UP and DOWN.  Pay
            \rbetter attention to the description of this area, {player}.""")
        elif mcp("south"):
            long_walk(this_room)
            break
        else:
            mcdu()


def vast_expanse(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "vast_expanse"

    print(
    """\rYou survey a vast expanse.  Your flashlight cannot even hit the cave
    \rwall in most directions.  You see some shimmering reflections way off in
    \rthe distance, which is probably some body of water.  This is actually kind
    \rof peaceful.  The exit is back DOWN.""")

    while True:
        mci()

        if mcp("get", "peaceful"):
            print("You get peaceful.  Man, you are some kind of peaceful now!")
        elif mcp("get"):
            print(
            """\rYou know the problem with this world?  There is too much
            \rGETTING, but not enough LOOKING.  Just relax, you know?  Enjoy
            \rsurveying the vast expanse.""")
        elif mcp("talk"):
            print(
            """\rDon't bother listening for echos.  Everything is so far away,
            \ryou won't even hear the sound waves that return to you.""")
        elif mcp("look") or mcp("survey"):
            print(
            """\rYeah, that's right.  LOOK.  Absorb.  Enjoy.  One more time...
            """)
            vast_expanse(last_room)
            break
        elif mcp("north") or mcp("south") or mcp("east") or mcp("west"):
            print(f"Careful, {player}!  You're on a precipice.  You'll fall.")
        elif mcp("down"):
            longer_twisty_walk(this_room)
            break
        else:
            mcdu()


def narrow_squeeze(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "narrow_squeeze"

    print(
    """\rWelcome to the narrowest, squeeziest, most claustrophobic cave hole,
    \ruh, crawl space thing... place.  This is the part where people get stuck
    \rand starve and have documentaries made about their failed rescue attempt.
    \rLuckily, you're not stuck.  You can go NORTH, or go back UP the twisty,
    \rwindy crawlspace.
    """)

    while True:
        mci()

        if mcp("NORTH"):
            open_cavern(this_room)
            break
        elif mcp("east") or mcp("west"):
            print(
            """\rUm, your shoulders already extend from the East to the West.
            \rYou're lucky you can move at all.""")
        elif mcp("south"):
            print(
            """\rEh, well, SOUTH isn't technically a choice... but I'll allow
            \rit this time.  You run SOUTH and crack your head on a low-hanging
            \rrock.  Suddenly the cave fills with bright lights floating all
            \rabout!  Did the rock activate some kind of magical pixie light
            \rstuff?
            \r\tActually, wait... no.  The swirly lights dim and you remember
            \rthat you hit your head.  SOUTH is not a valid direction.  Try UP.
            """)
        elif mcp("talk") or mcp("say"):
            print("NO TALKING!  Shhhh!  This is a cave.")
        elif mcp("up"):
            longer_twisty_walk(this_room)
            break
        else:
            mcdu()


def open_cavern(previous):
    global last_room, this_room, player, key_gag_initiated, can_see_the_door
    global have_stalactite, have_stalagmite, door_open, have_door_pudge
    global have_stalactite_powder
    last_room = previous
    this_room = "open_cavern"
    in_pool = False
    wet = False

    look_open_cavern_wall = """
    \rYou are in a majestic cavern, which seems to be partially lit by a pool
    \rof water nearby.  Near the bioluminescent pool, there is an interesting
    \rwall which you may want to INSPECT.  The whole scene almost reminds you of
    \rbeing outside at night.  It is beautiful and tranquil.  You can exit to
    \rthe SOUTH whenever you are ready."""

    look_open_cavern_door = """
    \rYou are in a majestic cavern, which seems to be partially lit by a pool
    \rof water nearby.  There is a door to the NORTH near the bioluminescent
    \rpool.  The whole scene almost reminds you of being outside at night.  It
    \ris beautiful and tranquil.  You can exit to the SOUTH whenever you are
    \rready."""

    look_open_cavern_door_open = """
    \rYou are in a majestic cavern, which seems to be partially lit by a pool
    \rof water nearby.  There is a doorway leading NORTH near the bioluminescent
    \rpool.  The whole scene almost reminds you of being outside at night.  It
    \ris beautiful and tranquil.  You can exit to the SOUTH whenever you are
    \rready."""

    if door_open:
        print(look_open_cavern_door_open)
    elif can_see_the_door:
        print(look_open_cavern_door)
    else:
        print(look_open_cavern_wall)

    while True:
        mci()

        if mcp("get","in","pool") or mcp("get","in","water"):

            if in_pool:
                print("You're already in the pool, and I don't like it.")
            else:
                in_pool = True
                wet = True
                print(
                """\rYou get... in... the pool?  That is not the way "GET" is
                \rsupposed to work here.

                \rYou splash about in the blue, glowing water like a happy baby.
                \rYou giggle like a happy baby.  This cave is no place for
                \rbabies!  Get out.
                """)

        elif mcp("get","out"):

            if in_pool:
                in_pool = False
                print(
                """\rGood.  Yes.  Thank you.  Dry off!  Who knows what is in
                \rthat mysterious cave water.  I hope you didn't get any in your
                \rears.""")
            elif wet:
                print(
                """\rOf course I meant you need to GET OUT of the POOL.  Don't
                \rbe so sensitive.""")
            else:
                print(
                """\rI don't know what you're talking about.  Is there a pool?
                \rI'm sure I didn't notice.  If you'd like to get out, you are
                \rcertainly permitted to leave to the SOUTH.""")

        elif mcp("LOOK", "WALL") or mcp("EXAMINE","WALL") or mcp("INSPECT","WALL"):
            can_see_the_door = True
            key_gag_initiated = True
            print(
            """\rCloser to the wall, you can clearly make out a stone door in
            \rthe cave wall, with what may be a key hole?  Didn't you see a key
            \rwayyyyy back at the beginning, in that box room?  I'm sure I
            \rremember something like that.""")
        elif mcp("inspect"):
            print("You inspect, ah, um, your fingernails.")
        elif mcp("examine"):
            print(
            """\rNo one said "EXAMINE"; but if they did, I'm certain that they
            \rwould have intended for you to EXAMINE some THING!""")
        elif mcp("thing","door"):

            if can_see_the_door:
                print("Cute.")
            else:
                print("How do you know if there is a door unless you LOOK?")

        elif mcp("look","key","hole") and can_see_the_door:
            print(
            f"""\rYou look through the key hole.  Interesting.  Yeah.  Mmmm.
            \rHey, {player}, you should see this.  There's some interesting
            \rstuff through this key hole.""")
        elif mcp("stalagmite","door"):

            if door_open:
                print("The door is already open.  Go NORTH through the door!")
            else:

                if can_see_the_door and have_stalagmite:
                    door_open = True
                    key_gag_concluded = True
                    print(
                    """\rIn a fit of rage at the audacity of any door brazen
                    \renough to stand in your way, you SMASH the door into a
                    \rpuddle of door pudge with a stalagmite club.  The way is
                    \ropen!""")
                elif can_see_the_door:
                    print("What stalagmite?  Do you have one of those?")
                elif have_stalagmite:
                    print(
                    """\rSounds like a great idea.  Why don't you find some door
                    \rto use it on.""")
                else:
                    print("What door?  What stalagmite?  What're you saying???")

        elif mcp("stalactite","door"):

            if door_open:
                print(f"Sorry, {player}:  missed your chance on that one.")
            elif can_see_the_door and have_stalactite:
                have_stalactite = False
                remove_from_inventory("stalactite")
                have_stalactite_powder = True
                inventory.insert(0, "Stalactite powder")
                print(
                """\rIn a fit of rage at the audacity of any door brazen enough
                \rto stand in your way, you SMASH... the stalactite against the
                \rsolid door.  A cloud of stalactite dust puffs away from the
                \rdoor and settles to the cave floor.  That was anticlimactic.
                """)
            elif can_see_the_door and have_stalactite_powder:
                print("Useless.")
            elif can_see_the_door:
                print("What stalactite?  Do you have one of those?")
            elif have_stalactite:
                print(
                """\rThis idea sounds questionable.  How sturdy are stalactites?
                \rAt any rate, you'd need to find a door to use it on, first."""
                )
            else:
                print("What door?  What stalactite?  You delirious?")

        elif mcp("smash","door") or mcp("hit","door") and not door_open:

            if can_see_the_door:
                print(
                """\rOooooh!  So angry!  You probably have to smash the door
                \rwith a THING though.  A hard thing.""")
            else:
                print("What door?")

        elif mcinput.lower().startswith("open") and mcp("door"):

            if door_open:
                print("That doorway looks pretty dang open to me!")
            elif can_see_the_door:
                print("You open the door.  Then it slams closed in your face!!")
            else:
                print("To open a door, one must have located a door to open.")

        elif mcp("get","pudge"):

            if door_open and have_door_pudge:
                print(
                """\rYou already have door pudge.  Check your INVENTORY.""")
            elif door_open:
                have_door_pudge = True
                inventory.insert(0, "Door pudge, if that is even a real thing")
                print(
                f"""\rThat is a very strange thing to do, {player}.  Don't let
                \rme stand in your way, though!  You GET DOOR PUDGE.""")
            else:
                print(
                """\rYou are mentally deranged.  There is no such thing.""")

        elif mcp("north"):

            if door_open:
                transition_hall(this_room)
                break
            elif can_see_the_door:
                print(
                """\rYou need to find a way to open the door first.""")
            else:
                print("NORTH is a good direction; but you can't go that way.")

        elif mcp("south"):
            narrow_squeeze(this_room)
            break
        else:
            mcdu()


def transition_hall(previous):
    global last_room, this_room, player, have_door_pudge
    last_room = previous
    this_room = "transition_hall"

    print (
    """\rYou are in a passage that blends natural cave walls with finished ones,
    \rdecorated with colors and repeating patterns.  The NORTH end leads to a
    \rnicely finished room.  The SOUTH end leads back into the open cavern.
    """)

    while True:
        mci()

        if mcp("look","wall"):
            print(
            """\rThere are blues and golds and whites, with patterns of plants
            \rand flowers that appear to be carefully hand-painted.""")
        elif mcp("use","pudge","wall") and have_door_pudge:
            print(
            """\rYou desecrate the gorgeous wall paintings with door pudge.""")
        elif mcp("south"):
            open_cavern(this_room)
            break
        elif mcp("north"):
            finished_room(this_room)
            break
        else:
            mcdu()


def finished_room(previous):
    global last_room, this_room, player, have_door_pudge
    last_room = previous
    this_room = "finished_room"

    print(
    """\rThis nicely finished room has the same decorative patterns on the walls
    \ras the SOUTH hallway.  There are open doorways leading to rooms in every
    \rdirection.""")

    while True:
        mci()

        if mcp("look","wall"):
            print(
            """\rIt looks just like the patterns in the hallway to the SOUTH,
            \rexcept every inch of it continues to be unique.  There are blues
            \rand golds and whites, with patterns of plants and flowers that
            \rappear to be carefully hand-painted.""")
        elif mcp("use","pudge","wall") and have_door_pudge:
            print(
            """\rYou desecrate the gorgeous wall paintings with door pudge.""")
        elif mcp("west"):
            bath_room(this_room)
            break
        elif mcp("north"):
            bed_room(this_room)
            break
        elif mcp("east"):
            finished_hallway(this_room)
            break
        elif mcp("south"):
            transition_hall(this_room)
            break
        else:
            mcdu()


def bath_room(previous):
    global last_room, this_room, player, have_stalactite, have_door_pudge
    global pudge_in_toilet, toilet_overflowing
    last_room = previous
    this_room = "bath_room"

    print(
    """\rOh, how lovely!  A bathroom.  Not just any bathroom, either.  This one
    \rlooks fairly luxurious, and surprisingly clean for being deep inside a
    \rcave.  There is a toilet, a shower, and a sink complete with mirror.""")

    if toilet_overflowing:
        print("The toilet is overflowing.")

    while True:
        mci()

        if mcp("look","wall"):
            print(
            """\rThe walls in here are metallic, but there are more floral patterns
            \rcarefully etched into them.  The details intensify on the walls within
            \rreach of the toilet.  Someone spent a lot of time in here.""")
        elif mcp("use","pudge","wall") and have_door_pudge:
            print(
            """\rYou rub some door pudge into the etched wall carvings.  Hey,
            \rthat actually adds an interesting effect.""")
        elif mcp("look","mirror"):
            print(
            """\rYou recoil in horror!  Just kidding.  Hey, is that a medicine
            \rcabinet?""")
        elif mcp("use","pudge","mirror"):
            print(
            """\rYou cover the mirror in door pudge.  Much better.""")
        elif mcp("stalagmite","mirror"):
            print("Don't break it!  It isn't yours.")
        elif mcp("stalactite","mirror") and have_stalactite:
            print("It would probably break the stalactite.  Those are fragile.")
        elif mcp("use","mirror"):
            print("You use the mirror.")
        elif mcp("look","cabinet"):
            print("It's a medicine cabinet.  Why don't you OPEN it?")
        elif mcp("use","cabinet") or mcp("open","cabinet"):
            print(
            """\rOpening the medicine cabinet, you see a few bottles of medicine.
            \rThey look pretty old.  All the labels are faded so you can't tell what
            \rthey contain.""")
        elif mcp("take","medicine"):
            print("You take some medicine.  NO!  SPIT IT OUT!!")
        elif mcp("spit","medicine"):
            print("You spit into the sink.  Goooood.")
        elif mcp("get","medicine"):
            print(
            """\rWe shouldn't be getting any cave medicine that is so old the
            \rexpiration dates have fadded off the labels.  I won't allow you to get
            \rit.  I would be liable for negligance, or something.""")
        elif mcp("look","shower"):
            print(
            """\rWhile the rest of the bathroom is covered in in an etched
            \rmetalic surface, this shower looks to be carved directly from the
            \rstone.  It is smooth and polished.  There is a brass frame with
            \ra translucent glass door.  Or is it some kind of quartz?""")
        elif mcp("turn","on","shower") or mcp("use","shower"):
            print(
            """\rYou turn on the shower.  The water is glowing.  Maybe its not
            \ra good idea to use this shower.""")
        elif mcp("get","in","shower"):
            print(
            """\rMmmmmm, no.  That's not gonna work here.  You stay out of the
            \rshower.""")
        elif mcp("look","toilet"):
            print(
            """\rThis bowl is literally porcelain.  It is decorated with floral
            \rpatterns like the rest of this place, although these are brown.
            \rHmmm.""")

            if toilet_overflowing:
                print("Also, the toilet is overflowing.  Nice job.")

        elif mcp("pudge","toilet") and have_door_pudge:
            pudge_in_toilet = True
            have_door_pudge = False
            remove_from_inventory("pudge")
            print(
            """\rYou toss the rest of your trusty DOOR PUDGE into the can, where
            \rit belongs!""")

            if toilet_overflowing:
                print(
                """\rEven more water sloshes out of the princely porcelain
                \rpotty.  I can't believe you went back to get more of this
                \rstuff.  Don't think that I programmed the rest of this game
                \rto make use of DOOR PUDGE.  I didn't.  Because its ridiculous.
                """)

        elif mcp("put","in","toilet"):
            print("Huh.  It goes right in there.  Interesting.")
        elif mcp("use","toilet"):
            print(
            """\rAhhhhhhhhhhh.  Good thing this was here!""")
        elif mcp("flush","toilet"):

            if toilet_overflowing:
                print(
                f"""\rNow the overflowing toilet is even MORE overflowing.
                \rTerrific work, {player}!""")
            elif pudge_in_toilet:
                toilet_overflowing = True
                print(
                """\rYou flush the toilet.  Uh oh.  Its filling up!  Oh no..."""
                )
            else:
                print(
                """\rYou flush the toilet.  Nice!  I wonder where this leads.
                \rHopefully not to that glowing pond outside.""")

        elif mcp("east") or mcp("exit") or mcp("leave"):
            finished_room(this_room)
            break
        else:
            mcdu()


def bed_room(previous):
    global last_room, this_room, player, have_pillow
    last_room = previous
    this_room = "bed_room"

    print(
    """\rThere is a bed in this room.  It must be a bed room.  Maybe they store
    \rbeds in here.  A cave is a strange place for keeping beds, though, if you
    \rask me.""")

    while True:
        mci()

        if mcp("look","bed"):
            print(
            """\rThe bed looks comfy.  It is well made with ornate red covers
            \rand fluffy white pillows.""")
        elif mcp("use","bed"):
            print("Use it?  Use it for what?")
        elif mcp("sleep","bed"):
            print(
            """\rYou lie down in the bed and try to sleep.  You can't quite do
            \rit, though.  I mean, what if someone is down here.  Do you want
            \rthem to find you sleeping in their bed?""")
        elif mcp("sleep"):
            print(
            f"""\rYou sleep standing up for a few minutes.  That's a strange
            \rtalent, and an even stranger choice, {player}.  There's a
            \rperfectly good bed right there.""")
        elif mcp("get","pillow") and not have_pillow:
            have_pillow = True
            inventory.insert(0, "A fluffy, white pillow.")
            print(
            """\rYou get a pillow.  Good idea!  Pillows often come in handy in
            \rcaves.""")
        elif mcp("south"):
            finished_room(this_room)
            break
        else:
            mcdu()


def finished_hallway(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "finished_hallway"

    print(
    """\rThis hallway has high ceilings painted with bright blue sky and clouds.
    \rThe walls are painted on the north side with a beach and ocean view.  The
    \rsouth wall is painted like a lush forrest.  In the center of the forrest
    \rpainting is an opening to a SOUTH stairwell.  There are doorways at the
    \rEAST and WEST ends of the hall.
    """)

    while True:
        mci()

        if mcp("pudge","wall"):
            print(
            """\rYou still have that?  No!  This hall is too nice!  Go vandalize
            \ra train car, or something.""")
        elif mcp("look","ceiling"):
            print("The sun shines through billowing, gold-tinted clouds.")
        elif mcp("look","north"):
            print("The ocean is clear and bright blue.  The dunes are white.")
        elif mcp("look","south"):
            print(
            f"""\rThe jungle is filled with colorful flowers, and there are not
            \ra few cutesy animals peeking out from bushes to get a glimpse at
            \ryou, {player}.  Wink.  I'm winking at you, {player}.""")
        elif mcp("look","wall"):
            print(
            """\rThere are so very many walls, though!  Which of the two walls
            \rdo you mean?""")
        elif mcp("south"):
            kitchen(this_room)
            break
        elif mcp("west"):
            finished_room(this_room)
            break
        elif mcp("east"):
            study(this_room)
            break
        else:
            mcdu()


def kitchen(previous):
    global last_room, this_room, player
    global have_junk
    last_room = previous
    this_room = "kitchen"

    print(
    """\rYou see a stove, a few cabinets, some counters, and some drawers.
    \rA kitchen?  Of course there's a kitchen!  Why not have a kitchen in your
    \rsecret cave house?  There's also a balcony to the SOUTH.  The stairs down
    \rto the hall are NORTH.""")

    while True:
        mci()

        if mcp("cabinet"):
            print(
            """\rYou rummage through the cabinets.  There are various food
            \rsupplies.  You notice a large quantity of generic cans of "Beans."
            \rHow interesting...  Well, if you get hungry, there's food!""")
        elif mcp("eat"):
            print(f"You're not hungry, {player}.  Trust me, I know.")
        elif mcp("get","beans"):
            print(
            """\rWell, that's peculiar.  They seem to be firmly attached to the
            \rshelf in the cabinet!  It's almost as if someone here didn't want
            \ryou to GET BEANS.""")
        elif mcp("pudge","powder","counter"):
            print("That is just the weirdest-  What do you hope to even make?")
        elif mcp("look","counter"):
            print(
            """\rYep.  There're counters.  Guess what they're made of!  Well?
            \rGive up?  Alright, I'll tell you.  They're made of counters.""")
        elif mcp("drawer"):
            print(
            """\rYou rummage through the drawers.  You're so forward.  Anyway,
            \ryou don't find anything other than the kinds of mundane things
            \rpeople let accumulate in drawers.""")
        elif mcp("get","mundane") and not have_junk:
            have_junk = True
            inventory.insert(0, "Some utterly commonplace drawer junk")
            print(f"You get some stodgy old stuff 'n junk.  Why, {player}?")
        elif mcp("get","mundane") and have_junk:
            print("Really?  No.")
        elif mcp("look","stove"):
            print(
            """\rNow this is interesting.  This looks like a gas-powered stove.
            \rWhere's the gas come from?  From the cave somehow?""")
        elif mcp("turn","on","stove") or mcp("use","stove"):
            print(
            """\rYou turn on the stove.  Definitely gas.  That's neat!  Now you
            \rturn the stove back off, because you're so safety-conscious.
            \rWouldn't want to burn the cave down.""")
        elif mcp("turn","off","stove"):
            print("It's off.")
        elif mcp("south"):
            back_porch(this_room)
            break
        elif mcp("north"):
            finished_hallway(this_room)
            break
        else:
            mcdu()


def back_porch(previous):
    global last_room, this_room, player
    last_room = previous
    this_room = "back_porch"

    print(
    """\rThis is an open air balcony carved into the stone, atop the house.  You
    \rare just outside the kitchen.  You can see the glowing pool below you, but
    \ranyone down there would not notice this space up here.  The cavern looks
    \rbigger from up here...
    \rThe kitchen is back NORTH.""")

    while True:
        mci()

        if mcp("get","air"):
            print("You get some air.  Stale, cave air.  It's still nice.")
        elif mcp("take","in"):
            print("You take it all in.  Ahhhh.")
        elif mcp("look","pool"):
            print(
            """\rIt looks like it stretches farther away than you thought.  That
            \rmight be a glowing river connecting too it, but it is pretty far
            \raway, off to your left.""")
        elif mcp("north"):
            kitchen(this_room)
            break
        else:
            mcdu()


def study(previous):
    global last_room, this_room, player, secret_revealed
    last_room = previous
    this_room = "study"

    print(
    """\rThis room looks like a nice home office study combined with a library.
    \rThere are several floor-to-ceiling bookshelves.  There is a large desk
    \rwhich appears to be made of polished stone.  To the WEST lies a hall.""")
    if secret_revealed:
        print("There is also a secret door leading SOUTH.")

    while True:
        mci()

        if mcp("look","desk"):
            print(
            """\rThis desk appears to be carved from the cave, like so much else
            \rin this house.  Every inch of it is painstakingly crafted, and
            \rtiny, detailed patterns are everywhere.  The desk surface is so
            \rsmoothly polished that you can see your reflection.  It is
            \rbreathtaking.  I mean the desk, not your face.
            """)
        elif mcp("use","desk"):
            print(
            f"""\r"USE the DESK."  Okay, hmm.  Yeah, I can work with that.  You
            \rSit down at the big, stone desk, and try to look important.  Do
            \ryou feel useful at this desk?  I've gotta tell you, {player}, you
            \rcertainly do look very useful.  Excellent work at the desk, there.
            """)
        elif mcp("get","desk"):
            print(
            f"""\rYou pick up the enormous, stone desk of unfathomable weight
            \rwhich may have been carved directly from the cave itself, and
            \rplace it in your INVENTORY.

            \rHow does that sound?  Is that what you expected to happen when you
            \rtyped GET DESK?  Why don't we take a minute to think through our
            \ractions next time, {player}.""")
        elif mcp("look","bookshelf") or mcp("look","bookshelves"):
            print(
            """\rThese bookshelves are also carved into the stone walls.  They
            \rare very smooth.  They are filled to the brim with old books.""")

            if secret_revealed:
                print(
                """\rOne bookshelf has opened to reveal a doorway leading SOUTH.
                """)

        elif mcp("look","shelf") or mcp("look","shelves"):
            print(
            """\rYou'll have to be more specific.  Shelf is such a generic word.
            \rBookshelf, on the other hand... now that's a specific word, right
            \rthere.""")
        elif mcp("look","book") or mcp("look","books"):
            print(
            """\rScanning through the books, you notice a lot of classics.
            "Don Quixote"
            "War and Peace"
            "The Complete Works of William Shakespeare"
            "The Prince"
            ...just to name a few.  One book especially grabs your attention:
            "The Odyssey".
            """)
        elif mcp("look","Odyssey"):
            print(
            """\r"The Odyssey" stands out from the other books.  You can't quite
            \rput your finger on why... either the color, or the size, or the
            \rplacement are just... you don't know.  It doesn't fit in.""")

            if secret_revealed:
                print("Maybe because its a secret lever for a secret door.")

        elif mcp("get","odyssey") or mcp("use","odyssey"):

            if secret_revealed:
                print("You can't get it.  Its like a lever, or something.")
            else:
                print(
                """\rYou grab "The Odyssey", but you can't fully remove it from
                \rthe shelf.  Instead, the whole bookshelf feels like it comes
                \rloose from the wall!  It swings on a hinge and opens like a
                \rdoor.  This new doorway leads SOUTH into a secret room.""")

        elif mcp("get","book"):
            print("You grab a book, take a look, then put it back in its nook.")
        elif mcp("read"):
            print(
            """\rYou can't read.  Uh, in here.  Yeah!  It's too dark.  Yeah,
            \ryou know... cave reasons.""")
        elif mcp("west"):
            finished_hallway(this_room)
            break
        elif mcp("south"):
            secret_room(this_room)
            break
        else:
            mcdu()


def secret_room(previous):
    global last_room, this_room, player
    global man_in_secret_room, secret_room_door_open, secret_room_door_locked
    global have_stalactite, have_stalactite_powder, have_stalagmite
    global have_door_pudge, have_pillow, have_junk
    last_room = previous
    this_room = "secret_room"

    print(
    """\rYou're in a secret room.  To the NORTH is the open bookcase doorway."""
    )

    if secret_room_door_open:
        print("There is another open door leading SOUTH.")
    else:
        print("To the SOUTH is another door, which is closed.")

    if man_in_secret_room:
        print("There is a man here.  He's standing in front of the door.")
    else:
        print(
        "There really isn't anything interesting in here now that the man left."
        )

    while man_in_secret_room:
        mci()

        if mcp("look","man"):
            print(
            f"""\rYou look at the man.  He looks at you.  He doesn't look happy.
            \rActually, you don't look too happy either.
            \rYou alright there, {player}?""")
        elif mcp("hit","man"):
            print(
            f"""\rWhoa!  {player}!  A little less violence, and a little more
            \rmanners, please!  This man is a stranger.  We don't hit.""")
        elif mcp("talk","man"):
            print(
            """\rYou talk to the man.  He doesn't talk to you.  Weird.""")
        elif mcp("say"):
            print("You say some stuff.  He doesn't seem to care.  Rude.")
        elif mcp("stalactite","powder","man") and have_stalactite_powder:
            print(
            f"""\rYou fling some stalactite powder at the man.  He coughs.  Now
            \ryou're being rude, {player}.""")
        elif mcp("stalactite","man") and have_stalactite:
            print(
            """\rYou extend your only stalactite to the man.  He accepts your
            \rkind gesture, and takes the stalactite.""")
            have_stalactite = False
            remove_from_inventory("brittle")
            story(this_room, "stalactite")
            break
        elif mcp("pudge","man") and have_pudge:
            print(
            """\rYou extend your hand with some squishy door pudge on it.  The
            \rman looks at your hand.  He looks at your face.  He's clearly not
            \rgoing to touch that hand.""")
        elif mcp("stalagmite","man") and have_stalagmite:
            print(
            """\rYou reach into your endless pouch-pocket-hole-place-thing and
            \rpull out a stlagmite.  The man's eyes widen, and he looks excited.
            \rHe takes the stalagmite from you.""")
            have_stalagmite = False
            remove_from_inventory("stalagmite")
            story(this_room, "stalagmite")
            break
        elif mcp("pillow") and have_pillow:
            print(
            """\rYou pull out the pillow, and the man snatches it away from you.
            \r\t"Hey!  That's my pillow!" he exclaims.  The man is not pleased with
            \ryou.  He says, "I am not pleased with you."
            """)
            have_pillow = False
            remove_from_inventory("pillow")
        elif mcp("junk","man") and have_junk:
            print(
            """\rYou pull out some of that junk you found in a drawer.  The man
            \rcries out, "I've been looking everywhere for that!  Thank you!"
            \rHe takes the, uh, "valuable" things.""")
            have_junk = False
            remove_from_inventory("junk")
            story(this_room, "junk")
            break
        elif mcp("flashlight","man"):
            print(
            f"""\rYou wave your flashlight around, shine it in the man's eyes a
            \rlittle.  He blinks.  Real mature, {player}.""")
        elif mcp("push","man"):
            print("This particular man will not be pushed.")
        elif mcp("SOUTH"):
            print(
            "You can't get to the door.  The man is blocking it.  Annoying.")
        elif mcp("north"):
            study(this_room)
            break
        else:
            mcdu()

    while True:
        mci()

        if mcp("look","man"):
            print("No YOU look, man!  Don't see any MAN here, MAN.")
        elif mcp("man"):
            print("The man is gone now.  You can't interact with a gone man.")
        elif mcp("open","door"):

            if secret_room_door_open:
                print(f"All the doors in here are open, {player}.")
            elif mcp("north"):
                print(f"The doorway to the NORTH is already wide open.")
            elif secret_room_door_locked:
                print(f"You can't open the door, {player}.  The door is locked."
                )
            else:
                print("You open the door.  Great work!  WOO HOO!!")
                secret_room_door_open = True

        elif mcp("unlock","door"):

            if secret_room_door_locked:
                print(
                f"You can't unlock the door, {player}.  It's not happening.")
            elif secret_room_door_open:
                print(f"You can't unlock the door, {player}.  The door is open."
                )
            else:
                print(
                f"You can't unlock the door, {player}.  The door is not locked."
                )

        elif mcp("stalagmite","door"):
            print(
            f"""\r"{player}, that's not going to work here.  In fact, you know
            \rwhat?  Give me that!"
            \rThe cave, uh, narrator(?) takes away your stalagmite.
            \rWell, this is awkward...""")
            have_stalagmite = False
            remove_from_inventory("stalagmite")
        elif mcp("south") and secret_room_door_open:
            finished_path(this_room)
            break
        elif mcp("south"):
            print(f"You can't go south, {player}.  The door is closed.")
        elif mcp("north"):
            study(this_room)
            break
        else:
            mcdu()


def story(previous, reason):
    global last_room, this_room, player
    global secret_room_door_locked, secret_room_door_open, you_lose
    last_room = previous
    this_room = "story"

    if reason == "junk":
        print(
        """\r\t"Really, truely, thank you!  I'm going to put this in a drawer in
        \rmy kitchen to make sure it doesn't get lost again." """)
    elif reason == "stalagmite":
        print(
        """\r\t"I've been looking everywhere for one of these.  Where did you
        \rfind it?" """)
        mci()
    elif reason == "stalactite":
        print(
        """\r\t"Well, isn't this... nice?  I've never seen one like it."
        \rYou detect sarcasm.
        \r\t"Did you find it in this cave, or bring it from another one?"  The
        \rman is trying hard to be polite.""")
        mci()
    else:
        print("An impossible situation has occurred!")

    print(
    """\r\t"Ah.  Yes.  Anyway.
    \r\t"I'd love to tell you all about myself and how I came to live in and
    \rcreate this cave house.  Would you like to hear all about it?""")

    while True:
        mci()

        if mcp("yes") or mcp("continue") or mcp("yeah"):
            print("""\r\t"Fantastic!" """)
            break
        elif mcp("no"):
            print(
            f"""\r\t"Oh?  No?  Oh.  I see.  Well, I'll just get out of your way,
            \rthen.  Feel free to find your way back out of my cave."
            \rThe man walks past you into the study to the NORTH.  You probably
            \rwon't be seeing him again.  I think you really hurt his feelings,
            \r{player}.
            """)
            man_in_secret_room = False
            secret_room_door_locked = True
            you_lose = True
            secret_room("study")
            break
        else:
            print(
            """\r"I'm afraid I don't understand.  Shall I continue or not?" """)

    print(
    """\r\t"So this is how it all went down.  A long time ago, I was outside and
    \rstumbled across this cave, probably at the same entrance where you came
    \rin.  (I never found another way in or out.)
    \r\t"Anyway!  I was looking at this mysterious cave, and a snake came
    \rslithering toward me.  I froze up!  I was frightened.  I cried out, "Oh!"
    \rBut then the snake kept on going past me.  Let me tell you, I was very
    \rrelieved.  Has anything like that ever happened to you?"
    """)
    mci()

    print(
    """\r\t"Mmm hmm, fascinating," the man says.  He may not really think what
    \ryou said is fascinating.  It's hard to tell.
    \r\tHe continues, "So I go into this cave, and live just inside it for a
    \rwhile.  I even made, like, a secret hiding place.  It was all just inside
    \rthe entrance to the East.  Did you see it?"
    """)
    mci()

    print(
    """\r\t"Wonderful, great.  Anyway, so I explored the rest of the cave, yada,
    \ryada, yada, spent decades painstakingly carving out a home for myself,
    \retcetera, etcetera.  And here it is!"
    \r\t"Well?  What do you think?  Did you love my story?" """)

    while True:
        mci()

        if mcp("yes") or mcp("yeah"):
            print(
            """\r\t"Good.  That is a relief.  Hey, you're pretty alright.  Feel
            \rfree to, you know, explore in here, or come and go whenever you
            \rplease.  There is a quicker path to the cave entrance this way,
            \rbehind me."
            \rThe man gestures to the door leading SOUTH.  He opens the door for
            \ryou.
            \r\t"It has been a pleasure meeting you!  See you around."
            \rThe man goes NORTH into the study.  You never exchanged names, so
            \rI would hardly call that a "meeting", but who am I to say?
            """)
            man_in_secret_room = False
            secret_room_door_open = True
            secret_room("study")
            break
        elif mcp("no"):
            print(
            f"""\r\t"Oh?  No?  Oh.  Yeah, it wasn't a very good story.  Oh well.
            \rSorry to have bothered you."
            \rThe man looks dejected.  With his shoulders slumped, head down, he
            \rgently pushes past you to go NORTH into the study.  I hope he
            \rdoesn't, you know... hurt himself, {player}.  I agree with you,
            \rthough, {player}.  It was kind of an abrupt ending.
            """)
            man_in_secret_room = False
            secret_room_door_locked = True
            you_lose = True
            secret_room("study")
            break
        else:
            print(
            """\r"Yes, yes, but did you like my story?" """)


def finished_path(previous):
    global last_room, this_room, player, you_win
    last_room = previous
    this_room = "finished_path"

    print(
    """\rThe walls, floor, and ceiling here are all smooth and cut.  After
    \rYou walk for a while, the carved walls give way to raw cave surfaces.  It
    \ris a little cramped for a bit, but then you find more smoothly cut walls,
    \rfloor, and ceiling at the other end.""")

    if last_room == "secret_room":
        print(
        """\rThere are carved, stone steps leading up to a stone hatch.  You
        \rcould go UP and push on that hatch to open it.""")
    elif last_room == "perfect_cube_room":
        print(
        "There is a door leading NORTH to a secret room, and the study beyond.")
    else:
        print("This wasn't supposed to happen.  Which way did you come from?")

    while True:
        mci()

        if mcp("north"):
            secret_room(this_room)
            break
        elif mcp("up") or mcp("hatch") or mcp("push"):
            print(
            "You head up the steps and push on the hatch.  It opens easily.")
            cube_room_secret_door_visible = True
            you_win = True
            perfect_cube_room(this_room)
            break
        else:
            mcdu()


def end():
    exit(0)


def remove_from_inventory(uniqueWord):
    global inventory
    inventory = [x for x in inventory if uniqueWord not in x]



this_room = ""
last_room = ""
inventory = [
    "A flashlight, which you've been using to light up this dark cave"
    ]
hobo_bedroom_rocks_moved = False
have_stalactite = False
have_stalactite_powder = False
have_stalagmite = False
have_door_pudge = False
have_pillow = False
have_junk = False
key_gag_initiated = False
key_gag_concluded = False
key_identified = False
can_see_the_door = False
door_open = False
pudge_in_toilet = False
toilet_overflowing = False
secret_revealed = False
secret_room_door_open = False
man_in_secret_room = True
secret_room_door_locked = False
cube_room_secret_door_visible = False
you_win = False
you_lose = False

os.system('cls')
start()
