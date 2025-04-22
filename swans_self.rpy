# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("[name]")
define o = Character("Odette")
define s = Character("Swan")

$ Courage_Points = 0  # pass odette's challenges
default Courage = False

# The game starts here.

label start:
    # Show a background
    play music "swanlake.mp3"
    scene forest at truecenter
    with dissolve 
    "After a short while, we reach the meadows just outside the neighborhood where we both live."
    "It's a scenic view I've grown used to. Autumn is especially beautiful here."
    "When we were children, we played in these meadows a lot, so they're full of memories."
    
    $ name = renpy.input("What is your name?", length =32)
    o "Pleased to meet you, [name]."

    # Show Odette the first character sprite
    show odette at truecenter
    with fade 

    # Display lines of dialogue
    o "Hi there!"
    r "Who are you?"
    o "I'm another version of your Ego, the magical one...I would say."
    r "I don't get it...where am I? How do I end up here?"
    o "You have entered the void. You're nothing but your consciousness now. Congrats!"
    r "What do you mean...oh no, my head hurts. This must be a dream." 
    o "Indeed! Everything about you is nothing but a long dream. Have you heard of this ancient phrase?"
    o "You are only the observer of your thoughts; that which is loved is always beautiful."
    r "What a beautiful phrase...My head is spinning...Who is Ego? What is the void?"
    o "Well..."
    
    show swan at truecenter
    with dissolve

    s "Hi, I am also your Ego."
    r "Huh? But you're a swan...I'm just a human. And you're an ethereal princess...you almost look like a swan yourself."
    s "Of course! I'm a swan, another version of your Ego. Right now you're nothing but your consciousness."
    r "What even is Ego and consciousness...also why can't I feel my hands?"
    s "Ego is your physical form; look around...is anything real to you?"
    r "No...everything here seems surreal."
    o "Yes, you're correct!"
    o "Now you have to make a choice..."

    menu:
        "What will your choices be?"
        "Follow the meadows":
            $ Courage = True

        "Jump into the swan lake":
            pass 

        "Stay at the same place":
            pass  

    if Courage == True:
        "You followed the meadows, the path was flowery and ethereally magical."
    else:
        show odette at left 
        with move
        pause(1.0)
        hide swan 
        with moveoutright
       
        "Odette sighed in disappointment."
        o "Seem like I have no choice but to directly send you to the Self."
        jump toself

    return 
label toself:
   play music "swanlake.mp3"
   scene 
