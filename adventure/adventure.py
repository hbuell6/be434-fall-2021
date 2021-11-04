#!/usr/bin/env python3
"""
Author : hbuell6 <hbuell6@localhost>
Date   : 2021-11-02
Purpose: Go on an Exciting Dungeon Adventure!
"""


def play_again():
    print("\n\tWould you like to play again? (Y/N)")

    answer = input("> ").lower()

    if "y" in answer:
        print("\033[H\033[J")
        print('\tYou awake in a dark cell.')
        print('\tWondering how you ended up in such a place,')
        print('\tyou look around to get your bearings.')
        cell_1()
    else:
        exit()


# --------------------------------------------------
def game_over(reason):
    print('\n' + '\t' + reason)
    play_again()


# --------------------------------------------------
def creeper():
    print('\t"Something big, I guess." you say, a little confused.')
    print('\t"Alrighty then," says the Dude reaching into the screen,')
    print('\t"Here you go." He pulls out an entire freaking creeper!')
    print('\t"Um, what?" you say, flustered. Before Dude can answer,')
    print(
        '\tthe creeper runs at you. Instinctively, you run in the opposite direction.'
    )
    print('\tUnfortunately for you, the opposite direction is a corner.')
    print('\tIt\'s all over for you now. You don\'t even have time to think')
    print('\tbefore the creeper explodes.')
    game_over('You have died')


# --------------------------------------------------
def diamond_sword():
    print('\t"Something shiny, I guess." you say, a little confused.')
    print('\t"Alrighty then," says the Dude reaching into the screen,')
    print('\t"Here you go." He hands you a four foot long diamond sword.')
    print(
        '\tAmazed, you take the sword from him and reflexivley hold it skyward'
    )
    print('\tas if you were in a videogame yourself.')
    print(
        '\tInstantly, you are surrounded by a bright light and teleported outside.'
    )
    print('\tYou look around and see a road in front of you.')
    print('\tYou are able to hitchhike all the way back home with an')
    print('\tincredible story to tell your friends and family.')
    game_over('Congratulations on clearing the dungeon!')


# --------------------------------------------------
def talk_dude():
    print('\tYou walk over to where Minecraft Dude is sitting.')
    print(
        '\t"Hello, sir," you say, "could you tell me how to get out of here?"')
    print('\t"Hang on, I\'m speedrunning here" he says,')
    print('\t"I might be able to get sub 11 minutes if I get good RNG')
    print(
        '\tYou look at the screen and the dude is definitely NOT speedrunning.'
    )
    print('\tHe is running from a creeper and soon dies from it')
    print(
        '\t"Okay, so I\'m not very good at the game, but this is actually a magic screen.'
    )
    print(
        '\tIf you want, I can pull something from out of the game into the real world.'
    )
    print(
        '\tThat might help you escape. Whaddaya say? You want something big,')
    print('\tor something shiny?" He asks proudly, gesturing to the screen.')
    print('\tWhat will you choose?')

    while True:
        if 'shiny' in answer:
            print("\033[H\033[J")
            diamond_sword()
        elif 'big' in answer:
            print("\033[H\033[J")
            creeper()
        elif answer == 'back':
            print("\033[H\033[J")
            print(
                '\tA magical screen? Sounds sketchy. Best leave Mr. Crazy alone.'
            )
            colosseum_from_stairs()
        elif answer == 'exit':
            exit()
        else:
            print('\n\tYou can\'t do that.')
            print('\tTry typing big or shiny')
            answer = input("> ").lower()


# --------------------------------------------------
def ladder():
    print("\033[H\033[J")
    print('\tYou ignore Minecraft Dude and head straight for the ladder.')
    print('\tYou take a look up the chimney and you see a light!')
    print('\tThis must be the way out!')
    print('\tExcited, you scramble up the ladder as fast as you can.')
    print(
        '\tOnce you get a ways up, you realize the light you see is steadily blinking.'
    )
    print(
        'You decide to investigate. Once you get close enough to tell what it is though,'
    )
    print(
        'it\'s already too late. It\'s a flashing time bomb! And it\'s out of time!'
    )
    game_over('You have died')


# --------------------------------------------------
def basement():
    print('\tYou follow the staircase downward and enter a basement')
    print('\tIt actually looks more like a recreation room.')
    print(
        '\tYou can see a dude in front of a large screen playing what looks like Minecraft'
    )
    print('\tAcross the room, there is a ladder leading up a wide chimney.')
    print('\tLooks like you could either talk to Minecraft Dude or')
    print('\tignore him and try for the ladder')
    print('\tWhat will you do?')

    answer = input("> ").lower()

    while True:
        if 'talk' in answer:
            print("\033[H\033[J")
            talk_dude()
        elif 'minecraft' in answer:
            print("\033[H\033[J")
            talk_dude()
        elif 'dude' in answer:
            print("\033[H\033[J")
            talk_dude()
        elif 'ladder' in answer:
            ladder()
        elif 'chimney' in answer:
            ladder()
        elif answer == 'back':
            print("\033[H\033[J")
            print(
                '\tYou decide to leave both the ladder and Minecraft Dude alone.'
            )
            colosseum_from_stairs()
        elif answer == 'exit':
            exit()
        else:
            print('\n\tYou can\'t do that.')
            print('\tTry typing the name of a location or object')
            answer = input("> ").lower()


# --------------------------------------------------
def trap_door():
    print("\033[H\033[J")
    print('\tIgnoring Dennis\'s advice, you turn left')
    print('\tNot too long after turning, you hit a wall.')
    print('\tYou feel around on the wall and you find a button!')
    print(
        '\tHoping for a secret room full of treasure, you hastily push the button.'
    )
    print(
        '\tImmediately, the floor opens beneath you and you fall into a bed of spikes.'
    )
    print('\tMaybe you should have just listened to Dennis. Poor guy.')
    game_over('You have died')


# --------------------------------------------------
def escape():
    print("\033[H\033[J")
    print('\tYou decide to listen to your cool new friend, Dennis')
    print(
        '\tYou continue straight through the passageway, and eventually reach a clearing'
    )
    print('\tA lovely meadow stands before you and you realize-')
    print('\tyou know exactly where you are! Your home isn\'t far from here!')
    print('\tYou run home as fast as you can eager to tell your friends and')
    print('\tfamily about your grand adventure!')
    game_over('Congratulations on escaping the dungeon!')


# --------------------------------------------------
def secret_passage():
    print("\033[H\033[J")
    print('\tYou enter the passage on your hands and knees.')
    print('\tIt\'s dark, but the passage is pretty straight,')
    print('\tso it\'s easy enough to keep going without being able to see.')
    print('\tYou stop to rest a bit a ways into the tunnel')
    print('\tand you feel a slight breeze coming from your left.')
    print('\tYou know Dennis told you to go straight until you get outside,')
    print('\tbut there\'s gotta be something interesting the other way!')
    print('\tWhich way will you go?')

    answer = input("> ").lower()

    while True:
        if 'straight' in answer:
            escape()
        elif 'left' in answer:
            trap_door()
        elif answer == 'back':
            print('\n\tNo going back now, it\'s too narrow to turn around')
            answer = input("> ").lower()
        elif answer == 'exit':
            exit()
        else:
            print('\n\tYou can\'t do that.')
            print('\tTry typing left or straight')
            answer = input("> ").lower()


# --------------------------------------------------
def talk_dennis():
    print('\tYou walk over to Dennis. "Excuse me, sir," you say,')
    print('\t"Are you Dennis?" The man slowly stops spinning in his chair.')
    print('\tHe turns to look at you. "What do you want?" he says, annoyed')
    print('\t"I had almost reached maximum velocity."')
    print(
        '\t"Sorry to disturb you," you begin, "but do you happen to know of a way out of here?"'
    )
    print(
        '\t"If I tell you, will you let me get back to my spinning?" He asks.')
    print(
        '\t"Indeed, sir." you say. "I don\'t usually tell people this, but,"')
    print(
        '\tDennis starts to get up from his beloved chair and moves to the corner of the room'
    )
    print('\t"I like you, so I\'ll let you in on a little secret"')
    print(
        '\tDennis moves a large board away from the wall to reveal a secret passage!'
    )
    print(
        '\t"Just go straight through this passage and you\'ll make it outside." Dennis says.'
    )
    print('\tWill you go through the passage?')

    answer = input("> ").lower()

    while True:
        if 'y' in answer:
            secret_passage()
        elif 'passage' in answer:
            secret_passage()
        elif answer == 'back':
            print("\033[H\033[J")
            print('\tYou leave the room and ignore Dennis. Poor guy.')
            colosseum_from_dennis()
        elif answer == 'exit':
            exit()
        else:
            print("\033[H\033[J")
            print('\tYou leave the room and ignore Dennis. Poor guy.')
            colosseum_from_dennis()


# --------------------------------------------------
def colosseum_from_stairs():
    print('\tYou reenter the colosseum and see a small, low window across the')
    print('\troom to your right that looks big enough for you to fit through.')
    print('\tTo your left, you see a large sign painted with')
    print('\tblood-red capital letters that read “DENNIS”.')
    print('\tThere is a crimson door beneath the sign.')
    print('\tWhere will you go?')

    answer = input("> ").lower()

    while True:
        if 'door' in answer:
            print("\033[H\033[J")
            dennis()
        elif 'dennis' in answer:
            print("\033[H\033[J")
            dennis()
        elif 'window' in answer:
            print("\033[H\033[J")
            print('\tYou sqeeze yourself through the small window and')
            print('\thoist yourself down to the floor')
            print('\tYou realize you\'re right back where you started')
            cell_1()
        elif 'right' in answer:
            print("\033[H\033[J")
            print('\tYou sqeeze yourself through the small window and')
            print('\thoist yourself down to the floor')
            print('\tYou realize you\'re right back where you started')
            cell_1()
        elif answer == 'back':
            print("\033[H\033[J")
            print(
                '\tActually, that basement looked pretty interesting.'
            )
            basement()
        elif answer == 'exit':
            exit()
        else:
            print('\n\tYou can\'t do that.')
            print('\tTry typing the name of a location or object')
            answer = input("> ").lower()


# --------------------------------------------------
def colosseum_from_dennis():
    print('\tYou reenter the colosseum and see a small, low window across the')
    print(
        '\troom in front of you that looks big enough for you to fit through.')
    print('\tTo the right is flight of stairs leading downward.')
    print('\tWhere will you go?')

    answer = input("> ").lower()

    while True:
        if 'stairs' in answer:
            print("\033[H\033[J")
            basement()
        elif 'right' in answer:
            print("\033[H\033[J")
            basement()
        elif 'window' in answer:
            print("\033[H\033[J")
            print('\tYou sqeeze yourself through the small window and')
            print('\thoist yourself down to the floor')
            print('\tYou realize you\'re right back where you started')
            cell_1()
        elif answer == 'back':
            print("\033[H\033[J")
            print(
                '\tMaybe Dennis just wants a friend. You decide to give him another chance.'
            )
            dennis()
        elif answer == 'exit':
            exit()
        else:
            print('\n\tYou can\'t do that.')
            print('\tTry typing the name of a location or object')
            answer = input("> ").lower()


# --------------------------------------------------
def colo_from_dennis_1():
    print("\033[H\033[J")
    print('\tYou decide Dennis is best left alone.')
    print(
        '\tAnyone who can spin that fast in an office chair can’t be good news.'
    )
    colosseum_from_dennis()


# --------------------------------------------------
def dennis():
    print(
        '\tYou crack open the door to reveal a small office with a desk and computer.'
    )
    print(
        '\tThe room is otherwise empty besides a man spinning around in a small office chair.'
    )
    print('\tYou presume this must be Dennis.')
    print('\tShould you maybe strike up a friendly conversation?')
    print(
        '\tOr would you rather leave Dennis to his devices and head back to the colosseum?'
    )

    answer = input("> ").lower()

    while True:
        if 'leave' in answer:
            colo_from_dennis_1()
        elif 'colosseum' in answer:
            colo_from_dennis_1()
        elif 'talk' in answer:
            print("\033[H\033[J")
            talk_dennis()
        elif 'conversation' in answer:
            print("\033[H\033[J")
            talk_dennis()
        elif 'dennis' in answer:
            print("\033[H\033[J")
            talk_dennis()
        elif answer == 'back':
            colo_from_dennis_1()
        elif answer == 'exit':
            exit()
        else:
            print('\n\tYou can\'t do that.')
            print('\tTry typing the name of a location or object')
            answer = input("> ").lower()


# --------------------------------------------------
def colosseum():
    print(
        '\tYou find yourself in a large round room that looks like a sort of colosseum.'
    )
    print('\tAcross the room, you see a large sign painted with')
    print('\tblood-red capital letters that read “DENNIS”.')
    print('\tThere is a crimson door beneath the sign.')
    print('\tTo your left you see a flight of stairs leading downward.')
    print('\tWhere will you go?')

    answer = input("> ").lower()

    while True:
        if 'dennis' in answer:
            print("\033[H\033[J")
            dennis()
        elif 'door' in answer:
            print("\033[H\033[J")
            dennis()
        elif 'stairs' in answer:
            print("\033[H\033[J")
            basement()
        elif 'left' in answer:
            print("\033[H\033[J")
            basement()
        elif answer == 'back':
            print("\033[H\033[J")
            print('\tYou\'d rather try your luck back in the cell.')
            cell_1()
        elif answer == 'exit':
            exit()
        else:
            print('\n\tYou can\'t do that.')
            print('\tTry typing the name of a location or object')
            answer = input("> ").lower()


# --------------------------------------------------
def colosseum_window_2():
    print("\033[H\033[J")
    print('\tYou grab one of the chains and tug a few times.')
    print('\tIt seems pretty sturdy.')
    print('\tYou climb the chains and squeeze your way through the opening.')
    print(
        '\tYou find yourself in a large round room that looks like a sort of colosseum.'
    )
    print('\tAcross the room, you see a large sign painted with')
    print('\tblood-red capital letters that read “DENNIS”.')
    print('\tThere is a crimson door beneath the sign.')
    print('\tTo your left you see a flight of stairs leading downward.')
    print('\tWhere will you go?')

    answer = input("> ").lower()

    while True:
        if 'dennis' in answer:
            print("\033[H\033[J")
            dennis()
        elif 'door' in answer:
            print("\033[H\033[J")
            dennis()
        elif 'stairs' in answer:
            print("\033[H\033[J")
            basement()
        elif 'left' in answer:
            print("\033[H\033[J")
            basement()
        elif answer == 'back':
            print("\033[H\033[J")
            print('\tYou\'d rather try your luck back in the cell.')
            cell_2()
        elif answer == 'exit':
            exit()
        else:
            print('\n\tYou can\'t do that.')
            print('\tTry typing the name of a location or object')
            answer = input("> ").lower()


# --------------------------------------------------
def colosseum_window():
    print("\033[H\033[J")
    print('\tYou make your way to the window and tug on the rope.')
    print('\tIt feels like it is anchored to something outside the cell.')
    print('\tThe window looks just big enough for you to squeeze through.')
    print('\tYou slowly hoist yourself up the rope and through the opening.')
    colosseum()


# --------------------------------------------------
def colosseum_skeleton():
    print("\033[H\033[J")
    print('\tYou turn right down the tunnel.')
    print('\tShortly after taking the turn, the tunnel begins to flood with')
    print('\tan eerie yellowish light, making it difficult to see ahead.')
    print('\tSuddenly, you realize the floor beneath you is gone.')
    print('\tYou land with a thud on the dirt floor.')
    print('\tYou are a bit shocked, but unharmed.')
    colosseum()


# --------------------------------------------------
def hatch():
    print("\033[H\033[J")
    print(
        '\tYou crouch in front of the hatch, grab the handle, and pull up hard.'
    )
    print('\tClouds of red smoke billow from the open hole.')
    print(
        '\t"All those who summon the great and terrible demon Zelas must DIE!"'
    )
    print('\tbooms a deep voice from the hatch.')
    print(
        '\tBefore you can react, a horrifying winged creature emerges from the hole.'
    )
    print(
        '\tThe creature grabs you with its sharp claws and drags you into the abyss.'
    )
    game_over('You have died')


# --------------------------------------------------
def cliff():
    print("\033[H\033[J")
    print('\tYou turn left down the tunnel.')
    print(
        '\tAs you crawl on, you can feel water trickling beneath your hands.')
    print('\tIs this it? Could you be on the brink of escape?')
    print('\tThe tunnel slowly begins to illuminate with moonlight.')
    print(
        '\tYou can finally see the sky. Crawling as fast as you can, you race to the exit.'
    )
    print(
        '\tAlas, in your haste, you failed to observe that the tunnel lets out'
    )
    print('\tin a steep cliffside about 300 feet in the above a vast ocean.')
    print(
        '\tAs you fall, you imagine what might have been had you only turned right.'
    )
    game_over('You have died')


# --------------------------------------------------
def skeleton():
    print("\033[H\033[J")
    print('\tYou inch your way over to the skeleton until you can')
    print('\tclearly see a gaping hole in the wall behind it.')
    print('\tGathering all your courage, you push the old bones')
    print('\tout of the way and crawl into the hole.')
    print('\tThe tunnel is narrow and dark.')
    print('\tYou can barely see a foot in front of you.')
    print(
        '\tEventually, you reach a fork. Looks like you could go left or right.'
    )
    print('\tThere is no way to see what lies ahead down either path.')

    answer = input("> ").lower()

    while True:
        if 'left' in answer:
            cliff()
        elif 'right' in answer:
            colosseum_skeleton()
        elif answer == 'back':
            print("\033[H\033[J")
            print('\tYou\'d rather try your luck back in the cell.')
            cell_1()
        elif answer == 'exit':
            exit()
        else:
            print('\n\tYou can\'t do that.')
            print('\tTry typing left or right')
            answer = input("> ").lower()


# --------------------------------------------------
def cell_2():
    print("\033[H\033[J")
    print(
        '\tYou sneak past the guard and slip into the cell without being noticed.'
    )
    print('\tThis cell is similar in structure to the one you started in.')
    print(
        '\tThere is a small window high in the back wall with chains dangling down.'
    )
    print('\tMaybe you could climb them?')
    print('\tCuriously, there is also a wooden hatch in center of the floor')
    print('\tWhere could it lead?')
    print('\tWhat will you do?')

    answer = input("> ").lower()

    while True:
        if 'window' in answer:
            colosseum_window_2()
        elif 'chain' in answer:
            colosseum_window_2()
        elif 'hatch' in answer:
            hatch()
        elif answer == 'back':
            print("\033[H\033[J")
            print('\tYou\'d rather go back to the cell you started in.')
            cell_1()
        elif answer == 'exit':
            exit()
        else:
            print('\n\tYou can\'t do that.')
            print('\tTry typing the name of a location or object')
            answer = input("> ").lower()


# --------------------------------------------------
def talk_guard():
    print("\033[H\033[J")
    print(
        '\n\t"Hello there!" you yell, casually walking over to the bulky guard.'
    )
    print('\tHe turns to face you with a furrowed brow and a deep frown')
    print(
        '\t"In all my years guarding this dungeon, no one has EVER escaped!"')
    print('\the shouts, stomping over to your location, "You\'re the first."')
    print(
        '\the pauses and lets out a sigh, "Ya know, Prison Corp could really')
    print(
        '\tuse a fresh young mind like yours. What say you become our new CEO?"'
    )
    print(
        '\tShocked, but flattered, you agree. He shows you to your new office')
    print('\twhich looks surprisingly like the cell you just escaped from')
    print('\texcept it has a motivational kitten poster hanging on the wall')
    print(
        '\tYou spend the rest of your days trying to bring Prison Corp into the modern era'
    )
    game_over('You have won. Probably.')


# --------------------------------------------------
def guard():
    print("\033[H\033[J")
    print(
        '\tCarefully, you tip-toe down the hall so as not to alert the guard.')
    print('\tNow that you have a good view of him, you can see he is')
    print('\tmuch taller than you and a ton more built.')
    print('\tYou probably couldn’t take him in a fight.')
    print('\tYou see an open cell door in his blind spot.')
    print('\tIf you’re quiet enough, you might be able to sneak in.')
    print(
        '\tAlternatively, you could just walk up to the guard and talk to him.'
    )
    print('\tWho knows? Maybe you\'ll make a friend')
    print('\tWhat will you do?')

    answer = input("> ").lower()

    while True:
        if 'guard' in answer:
            talk_guard()
        elif 'talk' in answer:
            talk_guard()
        elif 'cell' in answer:
            cell_2()
        elif 'door' in answer:
            cell_2()
        elif 'sneak' in answer:
            cell_2()
        elif answer == 'back':
            print("\033[H\033[J")
            print(
                '\tYou decide it\'s too risky. You head back to the cell, closing the door behind you.'
            )
            cell_1()
        elif answer == 'exit':
            exit()
        else:
            print('\n\tYou can\'t do that.')
            print('\tTry typing an action or the name of a location or object')
            answer = input("> ").lower()


# --------------------------------------------------
def hallway_1():
    print("\033[H\033[J")
    print('\tYou put your full weight against the door')
    print('\tin an attempt to escape. It begins to budge!')
    print('\tYou can see the rust flaking off around your feet')
    print('\tas the door slowly creaks.')
    print('\tIn an instant, you are flung on the dungeon floor')
    print('\toutside the cell as the door swings open.')
    print('\tTo your left, you see a long, empty hallway,')
    print('\tbut you hear… humming? Could it be a guard?')
    print('\tTo your right, you see what looks like')
    print('\ta skeleton in shackles hanging on the wall.')
    print('\tIs there something behind it?')
    print('\tWhich way will you go?')

    answer = input("> ").lower()

    while True:
        if 'right' in answer:
            skeleton()
        elif 'skeleton' in answer:
            skeleton()
        elif 'left' in answer:
            guard()
        elif 'guard' in answer:
            guard()
        elif answer == 'back':
            print("\033[H\033[J")
            print('\tYou head back into the cell.')
            cell_1()
        elif answer == 'exit':
            exit()
        else:
            print('\n\tYou can\'t do that.')
            print('\tTry typing left or right')
            answer = input("> ").lower()


# --------------------------------------------------
def moss():
    print("\033[H\033[J")
    print('\tYou investigate the mossy corner.')
    print(
        '\tYou plunge your hand into the clump and retrieve a hefty handful.')
    print('\tIt feels cool and squishy against your skin.')
    print('\tAbruptly, you shove the whole wad in your mouth,')
    print('\tchew a few times, and then swallow.')
    print('\tTwo minutes in jail and you’ve already resorted to eating moss.')
    print('\tMaybe you could try the window or door?')
    print('\tWhat will you do?')

    answer = input("> ").lower()

    while True:
        if 'window' in answer:
            colosseum_window()
        elif 'door' in answer:
            hallway_1()
        elif 'rope' in answer:
            colosseum_window()
        elif answer == 'back':
            print("\033[H\033[J")
            print(
                '\tNo sense in eating any more moss. You turn back to the cell.'
            )
            cell_1()
        elif answer == 'exit':
            exit()
        else:
            print('\n\tYou can\'t do that.')
            print('\tTry typing the name of a location or object')
            answer = input("> ").lower()


# --------------------------------------------------


def cell_1():
    print('\tThree sides of the cell are worn stone walls')
    print('\twhile the fourth bears heavy iron bars.')
    print('\tA rusted iron door stands centered within the bars.')
    print('\tMaybe you could push it open?')
    print('\tA small window is carved high in the stone opposite the door.')
    print('\tis that a fragment of rope hanging from it?')
    print('\tYou turn to your left and see a damp corner encased')
    print('\tin a coat of moss. Can you use the moss in any way?')
    print('\tWhat will you do?')

    answer = input("> ").lower()

    while True:
        if 'moss' in answer:
            moss()
        elif 'door' in answer:
            hallway_1()
        elif 'window' in answer:
            colosseum_window()
        elif 'rope' in answer:
            colosseum_window()
        elif answer == 'exit':
            exit()
        else:
            print('\n\tYou can\'t do that.')
            print('\tTry typing the name of a location or object')
            answer = input("> ").lower()


# --------------------------------------------------
def start():
    print("\033[H\033[J")
    print('\tGreetings, young adventurer!')
    print('\tThis program sends you on a quest through a dungeon in a')
    print('\t‘choose your own adventure’ style format.')
    print(
        '\tThroughout this experience, you will make critical decisions that')
    print(
        '\twill help you escape from the dungeon or meet an untimely demise.')
    print('\tBased on the prompts for each room, you have the freedom')
    print('\tto choose where to go, with whom to interact or ignore,')
    print('\tand ultimately how to shape your own destiny.')
    print('\tIf at any time you feel lost or stuck, you can type "back"')
    print('\tto go to the previous room, or "exit" to quit the game')
    print('\tFare thee well on thy quest, adventurer!')
    print('\tMay this dungeon prove a worthy challenge! Shall we begin? (Y/N)')

    answer = input("> ").lower()

    if 'y' in answer:
        print("\033[H\033[J")
        print('\tYou awake in a dark cell.')
        print('\tWondering how you ended up in such a place,')
        print('\tyou look around to get your bearings.')
        cell_1()
    else:
        exit()


# --------------------------------------------------
start()
