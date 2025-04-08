# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character(reader)
define o = Character("Odette")
define s = Character("Swan")

# The game starts here.

label start:
  $reader = renpy.input(" What is your name, my dearest?") #assign player's name 

  $reader = reader.strip()
  if $ reader == "":
  $ reader = "Rina"
    $ courage_points = 0 #pass odette's challenges 
    $ understand_self = 0 #understand non-dualism 
    $ manifest_points = 0 #summon magical objects upon request
    # Show a background
    play music "swanlake.mp3"
    scene forest at truecenter
    "After a short while, we reach the meadows just outside the neighborhood where we both live."
    "It's a scenic view I've grown used to. Autumn is especially beautiful here."
    "When we were children, we played in these meadows a lot, so they're full of memories."
    r "Where am I? "
    o "Pleased to meet you, %(player_name)s."

    # show Odette the first character sprite
    show odette at truecenter
    with dissolve 

    # display lines of dialogue

    o "Hi there!"
    r "Who are you? "
    o "I'm another version of your Ego, the magical one...I would say."
    r "I don't get it...where am I? How do I end up here?'"
    o  "You have entered the void. You're nothing but your consciousness now. Congrats!'"
    r  "What do you mean...oh no, my head hurts. This must be a dream." 
    o "Indeed! Everything about you  nothing but a long dream. Have you heard of this ancient phrase? "
    o "You are only the observer of your thoughts, that which is loved is always beautiful."
    r "What a beautiful phrase...My head is spinning...Who is Ego? What is the void?"
    o "Well..."
    
    show swan at truecenter
    with dissolve

    s "Hi, I am also your Ego."
    r "Huh? But you're a swan...I'm just a human. And you're an ethereal princess...you almost look like a swan yourself."
    s "Of course! I'm a swan, another version Ego of you.Right now you're nothing but your consciousness."
    r "What even is Ego and consciousness...also why can't I feel my hands?"
    s " Ego is your physical form, look around...is anything real to you?"
    r " No...everything here seems surreal. "
    o " Yes, you're correct! "
    dissolve swan 

    # using menu to enable reader to make choices & choose their own storyline.
    menu:
   r "What should I do then?"
   screen choice_button() :
   frame:
   xpos 100 ypos 100 
   imagebutton:
   idle "[button1.jpg]"
   hover "[ button1.jpg]"
   jump cross_trail
   o "Cross the lake and get to the meadow. ":
   $cross_lake = True 
   "I followed the trail alone & left Odette & her swan behind."
   $ courage_points = +2
   $ understand_self = -1
   jump cross_trail 
  r " I am staying here":
   $ stay = True 
   " Odette shook her head in disbelief, but she sighed & gave you a letter."
   scene letter at truecenter 
   r "What letter is this?"
   jump read_letter 
   r " I just want to know who is Ego, and who is my true Self..." :
   $ find_self = True 
   o "Of course you will, the key is already within you."
   r "How do I find the key?"
   o "Within the lake, as blue as the sky..."
   jump key
   
   label trail:
   scene lake at truecenter 
   r "What a magical view..."







    # This ends the game.

    return
