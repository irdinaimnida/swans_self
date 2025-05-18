# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("[name]")
define o = Character("Odette")
define s = Character("Swan")
define f = Character("Self")
define a = Character("Author")

# Declare points earned for the game. Different point leads to different endings.

$ Courage_Points = 0  # pass odette's challenges
default Courage = False
$ Manifest_Points = 0 #summon magical item to escape forest
default Manifest = False 
$ Law_Points = 0 # understand the basic concept of the law
default Law = False


# The game starts here.

label start:
    # Show a background
    scene forest at truecenter
    with fade 

    a "Note: This fantasy game is created based around the teachings & understandings of the law of assumption by Neville Goddard, the author of The Power of Awareness and Lester Levenson's theory of non-dualism, the author of Keys To The Ultimate Freedom."
    a "For people who are new to the concepts or has never heard of this before, the only key to this game is to believe in one's self!"
    a "Onto the game, stay limitless and may you become Self!"

    play music "swanlake.mp3"

    "I opened my eyes to find myself surrounded by the most ethereal meadow and lake the bare eyes could perceive."
    "It's so strange, I definitely saw this place somewhere in the movies when I was a child."
    "I mean, ever soon after I grow up, people told me life consists of never-ending mundane, probably until ones die."
    "It's strange that I don't entirely believe that. I always know there must be more of me, savouring the magical wonders of life."
    "My coworkers certainly laugh at me when I bring up about reality shifting abruptly. They think I got crazy from hours spent in the lab alone."
    
    $ name = renpy.input("What is your name?", length =32)
    o "Pleased to meet you, [name]."

    # Show Odette the first character sprite
    show odette at truecenter
    with dissolve

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
    s "Of course! I'm a swan, another version of your Ego. Right now you're nothing but your light and consciousness."
    s "The “LIGHT” is consciousness. Consciousness is one, manifesting in legions of forms or levels of consciousness."
    s "There is no one that is not all that is, for consciousness, though expressed in an infinite series of levels, is not divisional."
    s "There is no real separation or gap in consciousness. I AM cannot be divided. I may conceive myself to be a swan, a princess, a corporate slave as you think or a mermaid, but the center of my being remains the same, regardless of the concept I hold of myself."
    s "At the center of manifestation, there is only one I AM manifesting in legions of forms or concepts of itself and “I am that I am”."
    r "What even is Ego and consciousness...also why can't I feel my hands?"
    s "Ego is your physical form; look around...is anything real to you?"
    r "No...everything here seems surreal."
    o " Its because you are now only your own consciousness, you left the physical plane, your human body!"

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
        jump tomeadow
    else:
        show odette at left 
        with move
        pause(1.0)
        hide swan 
        with moveoutright
       
        "Odette sighed in disappointment."
        o "Seem like I have no choice but to directly send you to the Self. Do not fear, you are by your Self!"
        jump toself
    
label toself:
   play music "swanlake.mp3"
   scene selflake at truecenter
   with dissolve
   f "Fancy meeting you here, [name]. I have heard you rejected Odette's orders to follow the meadows."
   r "I am just too scared...I don't know what to do. And where are you?" 
   f "I am you, this is all you. Look in the lake, can't you see yourself? Go on, look."

   menu:
      "I followed the Self's voice & looked into the lake reflection.":
         $ Manifest = True 
      "I ran away from the voice, trembling in fear & agony.":
         pass
   if Manifest == True :
       r " I saw my own reflection in the water.I still look almost the same to the old [name] except there's something strange..."
       f "I admire your willingness to learn, soon you will no longer be separated from your desires. Here's a gift for you."
       show key at truecenter
       with dissolve
       pause (2.0)
       hide key
       with moveoutleft
       r "What do I use this key for? Are you tricking me again?"
       f "You have to let go of the fear of your Self! I am you, what is there to trick?"
       r "Well, for instance I was sent to this lake for no reason. I just want to escape whatever is going on in my reality right now."
       "I heard a faint laugh, almost mockery to what I said."
       f "Oh, you're so clueless...no one send you to this lake except you. Your so-called reality that you want to escape, it exists because you keep giving so much awareness to it."

       jump todoor 
   else:
        f "You cannot run forever from your own Self, [name]..."
        "I heard a faint laugh, almost similar to my voice, it's sickening..."
        jump tocave 
label tocave:
   play music "h2o.mp3"
   scene cave at truecenter 
   with dissolve
   "I saw the full moon shining so iridescently, as if it was a warning & the last light for me to escape."
   r "I have never seen a full moon this bright..."
   f "This is your last chance, young [name]...remember what I said? There's no separation from your Self."
   r "I still don't get all these woo-woo's. What even is non-dualism? Why am I not separate of everything?"
   f "I know the concept is too small for your mortal human mind to even take, but let me get this straight for you."
   f " All your desires, fears & the mirror of your so-called reality...it comes from you & your awareness."
   f " Your awareness can shift at any moment. You have millions of thoughts passing by, but only the thought you put awareness of is true."
   f " The facade of reality shifts every second according to your awareness. You are all that is. You are, therefore you are."
   f " Now think about the version of you now. The one you assume that lives a mundane life, that spends hours looking on your phone trying to escape the prison you created for yourself."
   f " Your reality now consists of all the time you spent assuming how it goes. Now tell me, what do you think the ideal [name] would be doing?"
   r " I don't know. I wish the ideal [name] is living the best life, whatever I am doing there."
   f " Now you almost got it. The version you think about yourself are already there. "
   " That voice was certainly mocking me. What do they even know? They get to live in a magical forest full of wonders hidden by the world while I was forced in the office cubicle for years of my life."
   f " I know what you're thinking. You would think you are this little victim, forced to a mundane office job and date burdening partner. I want to ask you a question though."
   " I hesitantly nodded. How was that even possible, my mind getting read so accurately?"
   f "Who told you what your life must consist of?"


menu:
    "The society. I was always told I should work hard, get a good job & follow all the rules in society to live a respectable life.":
        pass
    " My family. They have big expectations for me and I am scared, I don't want to disappoint them.":
        pass
    " Myself. I wanted to have everything but I fear of my circumstances & my what if's, how do I even get there?":
        pass
f "The only correct answer is yourself. I know you can get it by now."
r "But how do I get there? How am I going to just have everything? I am just a normal human. "
f "By acknowledging that you have it! Live as the reality of yo that you desire, just be."
f " You are, therefore you are."
r " I am, therefore I am? Is that right?"
f " That is correct! What you assume you are, you become. What you assume the reality is to you, it becomes. "
f " I AM is a feeling of permanent awareness. The very center of consciousness is the feeling of I AM. I may forget who I am, where I am, what I am, but I cannot forget that I AM. The awareness of being remains, regardless of the degree of forgetfulness of who, where and what I am."
r "Wow, you sure have your way with words, Self! Or I don't know what should I call you..."
r "But how do I assume something without proof? I mean, in my reality even to check money deposit you need to see it in your bank account. I mean, not like this enchanted forest has one..."
f "There is no such thing as a proof, the proof is only the reflection of your own assumptions."
f "I would give you another task, to make sure you understand that it is all you."
r " This is intriguing I can't lie,but sure..."



menu:
  "Choose correctly based on the basic concept of law of assumption, as told by Self." 
  "What do you need to do, in order to be the one who has it all?"
  "I think as the version of myself who has it, keep persisting in the thought & acknowledging I have it.":
       $ Law = True 
       
  " I don't know, I mean I want proof so I will keep checking for it in my reality. You are full of delusions, Self.":
       pass 

  " I am scared, Self...I just want to go back to my old reality." :
        pass
if  Law == True:
  show elina at left 
  with dissolve
  pause (3.0)
  f "Hi, [name]. I hope I don't startle you, now we look much alike aren't we? "
  " I gasped in awe, startled with the figure of a mermaid I only ever read in fairytale mythology when I was a child."
  r "Hi...Self? Or what should I call you...You are a beauty, unreal even..."
  f "You can call me Elina. And don't be silly with the compliment! I am your Self, you remember vividly who you wanted to be when you were a kid now?"
  r " Yes, a mermaid...you even have the same tail as I imagined mine would be, the same hair..."
  f "See? I told you, I am just a version of yourself in the reality you created. We are under the same consciousness, so nothing to be in awe about! Except maybe your amazing imagination at the age of 4."
  r "So the thing you told me about infinite realities, and that my assumption reflecting...It's true after all..."
  f "It's always been the only truth, only that the mere humans are so filled up with their Ego and their attachment to it that they fail to realise until they banish from existence."
  hide elina
  with moveoutright
  jump todoor
else:
  f "You still didn't get it don't you?"
  f "Let me rephrase it for you so your attachment to your mere physical could be broken."
  f " You are not separate from your desire, you are one with the reality you assume to be true."
  show elina at truecenter
  with fade 
  pause (3.0)
  r " So you are...Self?"
  " She laughed almost hysterically."
  f "I cannot do anything to save you..."
  hide elina 
  with moveoutright
  jump tocove

label todoor:
   show castle at truecenter
   with fade
   play music "swanlake.mp3"
   f "Congratulations, [name]... You have made it to the end of the enchanted land, without ever losing your Self."
   f " I have a gift for you, my dear..."
   show fairy at truecenter
   with fade
   f "Here, have a refreshment, my own brewed potion from my blooming garden..."
   f "You might think it's poison, but I have no intention in doing so. I am not polluting my garden with human's flesh."
   f "The potion I made are of pixie dusts,soon you wouldn't have any doubt in your heart... "
   r " Thank you, Elina. But what do you mean you brew it with potions? "
   hide fairy 
   with moveoutright
   $ renpy.pause()
   return 


label tocove:
   show cave at truecenter
   play music "h2o.mp3"
   with fade
   "I looked around, realising I am in the final danger."
   f " There is no use teaching a soul so rottenly attached to their own suffering..."
   r " Easy for you to say!"
   "The voice laughed even more hysterically."
   f "Here, [name]. I have a way for you to escape all this and return to your, most ordinary self."
   show poison at truecenter
   with dissolve  
   f "Drink this and you will return to your ordinary self."
   r "What would this potion do? Can I escape?"
   hide poison
   with moveoutright

   $ renpy.pause()

   return 



