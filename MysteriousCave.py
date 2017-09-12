from sys import exit
import os
import random
import string


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
            print("\t" + item)
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
        elif mcp("move", "rock") or mcp("use", "rock"):
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
    global last_room, this_room, player, key_gag_initiated, key_gag_concluded
    global key_identified
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
    \rsmooth.  This must have taken a lot of long, hard work.  Who would do such
    \ra thing?  You can't see anything to do here other than exit to the WEST.
    """)

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
    """\rYou're in a dark passage heading north, and walk for a long time.
    \rEventually, you reach a spot where the dark passage veers WEST, and an
    \reven darker passage continues to the NORTH.  Really, though, you should
    \rhead back SOUTH and leave this scary cave."""
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
    \r\tYou could leave, you know.  Type SOUTH three times and you're safe in
    \rthe sunshine.  I mean, as safe as you can be with murderers and theives
    \rand politicians out there."""

    look_from_north = """Take this the twisty, turny, climby, fally, creepy,
    \rdank, dark passage all the way, and head SOUTH to keep on going.
    \rThere are also passages that go UP and DOWN."""

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
            """\rYeah!  That's right.  LOOK.  Absorb.  Enjoy.  One more time...
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
    \rYou enter a majestic cavern, which seems to be partially lit by a pool
    \rof water nearby.  There is an interesting wall near the bioluminescent
    \rpool which you may want to INSPECT.  The whole scene almost reminds you of
    \rbeing outside at night.  It is beautiful and tranquil.  You can exit to
    \rthe SOUTH whenever you are ready."""

    look_open_cavern_door = """
    \rYou enter a majestic cavern, which seems to be partially lit by a pool
    \rof water nearby.  There is a door near the bioluminescent pool to the
    \rNORTH.  The whole scene almost reminds you of being outside at night.  It
    \ris beautiful and tranquil.  You can exit to the SOUTH whenever you are
    \rready."""

    look_open_cavern_door_open = """
    \rYou enter a majestic cavern, which seems to be partially lit by a pool
    \rof water nearby.  There is a doorway near the bioluminescent pool to the
    \rNORTH.  The whole scene almost reminds you of being outside at night.  It
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

        if mcp("get","in","pool"):

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


        elif mcp("smash","door") or mcp("hit","door"):

            if can_see_the_door:
                print(
                """\rOooooh!  So angry!  You probably have to smash the door
                \rwith a THING though.""")
            else:
                print("What door?")

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
    direction.""")

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
        elif mcp("east"):
            bath_room(this_room)
            break
        elif mcp("north"):
            bed_room(this_room)
            break
        elif mcp("west"):
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
        elif mcp("get","medicine"):
            print(
            """\rWe shouldn't be getting any cave medicine that is so old the
            \rexpiration dates have fadded off the labels.  I won't allow you to get
            \rit.  I could probably be prosecuted for negligance, or something.""")
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
            shower.""")
        elif mcp("look","toilet"):
            print(
            """\rThis bowl is literally porcelain.  It is decorated with floral
            \rpatterns like the rest of this place, although these are brown.
            \rHmmm.""")

            if toilet_overflowing:
                print("Also, the toilet is overflowing.  Nice job.")

        elif mcp("pudge","toilet") and have_door_pudge:
            have_door_pudge = False
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

        elif mcp("west") or mcp("exit") or mcp("leave"):
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
        elif mcp("north"):
            kitchen(this_room)
            break
        elif mcp("east"):
            finished_room(this_room)
            break
        elif mcp("west"):
            study(this_room)
            break
        else:
            mcdu()


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

    #LOOK MAN
    #You look at the man.  He looks at you.  He doesn't look happy.  Actually,
    #you don't look too happy either.  You alright there, {player}?
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
have_door_pudge = False
have_pillow = False
key_gag_initiated = False
key_gag_concluded = False
key_identified = False
can_see_the_door = False
door_open = False
pudge_in_toilet = False
toilet_overflowing = False

os.system('cls')
start()
