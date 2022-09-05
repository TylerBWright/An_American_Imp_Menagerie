# An American Imp Menagerie - A Text Adventure Game in Python
# By: Tyler Wright (2022)
#***************************************

print("AN AMERICAN IMP MENAGERIE\n")
print("A text adventure game by Tyler Wright (2002)\n")

print("""

ARRIVAL:

    A band of small creatures sit at a wooden table, eating slop.

    Large oaks are situated overhead, producing a menacing feel to the menagerie.

    You hope they don't notice your presence.
    """)
input("Press ENTER to continue.")

# The Menagerie (1)
def menagerie():
    print("""

    The small creatures are green and blue and red, and they frighten you with their high-pitched voices in tongues with which you are unfamiliar.

    Their porridge looks unappetizing, but you are starving. How can you reach it without detection?\n
    """)
    choice = input("Will you go North (N), South (S), or East (E)? ")

    if choice.lower() == "n":
        pond()

    elif choice.lower() == "s":
        grotto()

    elif choice.lower() == "e":
        forest()

    elif choice.lower() == "talk":
        redimp()

    else:
        print("I didn't understand. Please try again.")
        menagerie()
        
    print("\nYou entered " + choice)
    input("\nPress ENTER to continue")

# Pond (2)
def pond():
    print("""

    A pale man with darkened eyes stands before a pond, weeping softly to himself and analyzing a withering red rose within mere inches of one orbital.

    \"I am Edgar Allan Poe, author of failure at your service. Lenore! I have nothing to write about! I am feeling a bit melancholy for the moment. Please go.\"
    """)
    choice = input("\nWill you go South (S)? ")

    if choice.lower() == "s":
        menagerie()

    else:
        print("I didn't understand. Please try again.")
        pond()
    
    print("\nYou entered " + choice)
    input("\nPress ENTER to continue")

# Grotto (3)
def grotto():
    print("""

    A man who embodies the very image of one late President William McKinley stands before you, only with eccentric foreign attire and a fixed grin etched into his features.

    Behind him is an impassable grotto.

    \"Who am I? Why, I am the Wizard of Oz! Surely you have heard of the emerald-green kingdom of our great Princess Ozma? No? Say, do you happen to know where we are?\"
    \n""")
    choice = input("Will you go North (N), or East (E)? ")

    if choice.lower() == "n":
        menagerie()

    elif choice.lower() == "e":
        monolith()

    else:
        print("I didn't understand. Please try again.")
        grotto()
    
    print("\nYou entered " + choice)
    input("\nPress ENTER to continue")

# Forest (4)
def forest():
    print("""

    You enter a forest which gets darker with each step, until finally you are consumed in it. Curiously, a young girl about the age twelve lies illuminated by some unknown source. Her face is clasped in her hands and, while she does not look up at you, she clearly senses your presence.

    You feel a blue chill rise in your bones.

    \"I am Helen Keller, writer of 'The Frost-King.' They believe me a fraud! Now an impish fear clutches my hand. Will I be remembered as the blind-deaf girl that forged a fairy tale?\"
    \n""")
    choice = input("Will you go West (W), or South (S)? ")

    if choice.lower() == "w":
        menagerie()

    elif choice.lower() == "s":
        monolith()

    else:
        print("I didn't understand. Please try again.")
        forest()
    
    print("\nYou entered " + choice)
    input("\nPress ENTER to continue")

# Monolith (5)
def monolith():
    print("""

    You stumble upon an ancient monolith in a forest clearing, covered in brown and orange lichen.

    You read the inscription.

    \"The denizens of this lonely annex are consumed by American literary imps, conjured through the pen medium. These abhorrations, while far from benign, only have power when in the periphery of their host. Utter the full and correct name of the victim unto their impish gaoler to banish them from this realm.\"

    Below this inscription you can make out the word 'T-A-L-K.'
    \n""")
    choice = input("Will you go West (W), or North (N)? ")

    if choice.lower() == "w":
        grotto()

    elif choice.lower() == "n":
        forest()

    else:
        print("I didn't understand. Please try again.")
        monolith()
    
    print("\nYou entered " + choice)
    input("\nPress ENTER to continue")

# Red Imp (6)
def redimp():
    print("""

    Now you've done it! The three imps' heads spin from their axes and their eyes meet you where you stand. Moving is out of the question as you settle into a deep paralysis.

    The red imp steps before you with embers of flames emitting from its eyes.

    You still have the ability to talk, but you had better choose your words wisely!
    \n""")
    choice = input("What do you wish to say? ")

    if choice.lower() == "edgar allan poe":
        print('\nYou shout "' + choice + '!"' + " at the red imp.")
        blueimp()

    elif choice.lower() == "edgar allen poe":
        print('\nYou shout "' + choice + '!"' + " at the red imp. The imp has a more acute sense for the written language than you might guess, and was able to detect an 'e' in 'Allan' when you should have used an 'a.' This common mistake cost you your life as he was able to dodge your assault, albeit rattled by the experience.")
        gameover()

    elif choice.lower() == "edgar alan poe":
        print('\nYou shout "' + choice + '!"' + " at the red imp. The imp has a more acute sense for written language than you might guess, and was able to detect a missing 'l' in 'Allan.' This common mistake cost you your life as he was able to dodge your assault, albeit rattled by the experience.")
        gameover()

    elif choice.lower() == "edgar a poe":
        print('\nYou shout "' + choice + '!"' + " at the red imp. Your use of a middle initial rendered the spell useless, and your laziness cost you your life as he was able to dodge your assault, albeit rattled by the experience.")
        gameover()

    else:
        print('\nYou shout "' + choice + '!"' + " at the red imp.")
        gameover()

# Blue Imp (7)
def blueimp():
    print("""

    Upon the utterance of his name, Edgar Allan Poe emerges from the thicket and the red imp cowers in fear. The two of them collide, spiraling into the heavens and finally dissipating into the moonlit sky with a final flash of light.

    You now have the attention of the blue imp who lowers the temperature of your immediate surroundings as it searches your soul.

    You still have the ability to talk, but you had better choose your words wisely!
    \n""")
    choice = input("What do you wish to say? ")

    if choice.lower() == "helen keller":
        print('\nYou shout "' + choice + '!"' + " at the blue imp.")
        greenimp()

    elif choice.lower() == "hellen keller":
        print('\nYou shout "' + choice + '!"' + " at the blue imp. The imp has a more acute sense for written language than you might guess, and was able to detect an extra 'l' in 'Helen.' This common mistake cost you your life as he was able to dodge your assault, albeit rattled by the experience.")
        gameover()

    elif choice.lower() == "helen keler":
        print('\nYou shout "' + choice + '!"' + " at the blue imp. The imp has a more acute sense for written language than you might guess, and was able to detect a missing 'l' in 'Keller.' This common mistake cost you your life as he was able to dodge your assault, albeit rattled by the experience.")
        gameover()

    elif choice.lower() == "hellen keler":
        print('\nYou shout "' + choice + '!"' + " at the blue imp. The imp has a more acute sense for written language than you might guess, and was able to detect and extra 'l' in 'Helen' and a missing 'l' in 'Keller.' This common mistake cost you your life as he was able to dodge your assault, albeit rattled by the experience.")
        gameover()

    else:
        print('\nYou shout "' + choice + '!"' + " at the blue imp.")
        gameover()

# Green Imp (8)
def greenimp():
    print("""

    You summon Helen Keller who leaps forward from the east, hands outstretched in the direction of the blue imp. Her hands affix to the creature's eyes and it screeches into oblivion whilst Helen returns through a portal into the great cosmic beyond.  

    The green imp stands in the center of the forest clearing, the trees and foliage bending in its general direction as a display of total dominion over the biological structures of this terrarium. 

    You still have the ability to talk, but you had better choose your words wisely!
    \n""")
    choice = input("What do you wish to say? ")

    if choice.lower() == "wizard of oz":
        print('\nYou shout "' + choice + '!"' + " at the green imp.")
        end()

    elif choice.lower() == "oscar zoroaster phadrig isaac norman henkle emmannuel ambroise diggs":
        print('\nYou shout "' + choice + '!"' + " at the green imp. WOW! Of all the infinite strings that you could type in the parser, you landed on the wizard's earthly name before he became 'The Wizard of Oz' that we all know and love! On behalf of the developers of this game, we'll give you an honorary pass. A friend of Oz is a friend of ours. ~ devs")
        end()

    elif choice.lower() == "oz":
        print('\nYou shout "' + choice + '!"' + " at the green imp. You only uttered part of the name, and your laziness cost you your life as he was able to dodge your assault, albeit rattled by the experience.")
        gameover()

    else:
        print('\nYou shout "' + choice + '!"' + " at the green imp.")
        gameover()

# Ending (9)
def end():
    print("""

    The short little Wizard of Oz shuffles from behind a tree and gives you a whimsical wink before pointing his wand at the green imp (who is now sufficiently concerned for its own well-being.) 

    Within seconds, your final adversary disapears. The tree canopy rattles, revealing a giant hot air balloon slowly looming down above the head of the great wizard. The little man, smiling throughout this experience ear-to-ear, pops up a salute and then grabs on and disappears beyond the horizon. 

    With the threat now eliminated, you sit down before the pot of slop and eat a sizeable helping of it in honor of the three literary warriors and their showmanship against impish assaults on American exceptionalism. That'll show them!

    For now, you find it wise not to entertain the notion of your own predicament in this 5-celled dimension. You are without an imp, and that's a rather dismal thought. If only you'd been a writer instead of an oneironaut.
    \nEND""")
    exit()

# Game Over (10)
def gameover():
    print("""
    You've only managed to anger the imp further. Try as you might, your mental fortitude was no match for the creature as it slowly grips your mind and you lose yourself utterly. Your shadow dissapears and in its stead is a yellow imp, your doppleganger and gaoler. The creature kindly escorts you to your cell before wiping away all of your precious memories.

    I wish we had a nicer ending for you, but what did you expect?
    """)
    print("END")
    exit()

# Start of the game
menagerie()
