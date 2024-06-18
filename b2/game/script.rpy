﻿# title
define hop = "crash"

# define h = Character('[h_name]', color="#c8ffc8", who_outlines=[ (2, "#000000") ])
define p = Character('[p_name]', color="#000000")
define yw = Character('[yw_name]', color="#6b608e")
define jw = Character('[jw_name]', color="#feb3ff")
define jwt = Character('[jwt_name]', color="#5f55f1")
define yb = Character('[yb_name]', color="#c0ac02")
define jb = Character('[jb_name]', color="#6f18bc")
define yt = Character('[yt_name]', color="#7b0e73")
define jy = Character('[jy_name]', color="#de12cf")
define e = Character('[e_name]', color="#1be5c6")
define s = Character('[s_name]', color="#e99311")
define w = Character('[w_name]', color="#e3dd3d")
define n = Character('[n_name]', color="#aaaaaa")
define r = Character('[r_name]', color="#c12c09")
define g = Character('[g_name]', color="#2adf26")
define b = Character('[b_name]', color="#a8deef")

# $ h_name = "You"
$ p_name = "Bamboo"
$ yw_name = "Yi Wan"
# random stranger -> detective yi wan
$ jw_name = "Jiu Wan"
$ jwt_name = "Jiu Wan?"
$ yb_name = "Yi Bing"
$ jb_name = "Jiu Bing"
$ yt_name = "Yi Tiao"
$ jt_name = "Jiu Tiao"
$ e_name = "Dong"
$ s_name = "Nan"
$ w_name = "Xi"
$ n_name = "Bei"
$ r_name = "Hong Zhong"
$ g_name = "Fa Cai"
$ b_name = "Bai Ban"


###

image bg shop = Solid("#ffbedb")
image bg lab = Solid("#c3beff")

label start:

    ## copy this block into your own game
    python:
        gold = 0 #starting amount
        inv = []
        seen_items = []

        # crafting
        known_recipes = []
        seen_recipes = []
        made_recipes = []
        newitem = ""

        # shop inventory
        market = []

        # quests
        new_quests = []
        active_quests = []
        completed_quests = []

    ## CRAFT/SHOP SETUP
    $ known_recipes = [ "envelope_open", ]
    $ market = [ "envelope_closed", ]

    ## INVENTORY SETUP
    # $ InvItem(*item_sugar).pickup(3)
    # $ InvItem(*item_water).pickup(2)
    # $ InvItem(*item_sucker).pickup(1)
    # $ InvItem(*item_beet).pickup(200)

    jump s0p0

label process_quests:
    # add a quest with no unlock conditions
    $ add_new_quest("sucker3")

    # add a quest that only activates if you have money
    if new_quest("sugar1") and gold>0:
        $ new_quests.append("sugar1")

    # activate all new quests
    python:
        if len(new_quests) > 0: #if we have new quests
            for i in new_quests:
                active_quests.insert(0, i) #add to top of the quest list
            new_quests = [] #now reset the new quest list, since they all got added

label test_menu:
    scene bg shop
    menu:
        "Inventory":
            jump inventory
        "Crafting":
            jump start_crafting
        # "Quests":
            #jump view_quests
        # "Buy Items":
            #jump market_buy
        # "Sell Items":
            #jump market_sell
        "Continue":
            jump expression hop

##ITEMS
label inventory:
    scene bg lab
    call screen inventory(inv) with Dissolve(.2)
    jump test_menu

##CRAFTING
label start_crafting:
    scene bg lab
    call screen recipes() with Dissolve(.2)

label craft_success:
    show screen reward(newitem.image)
    "Made {color=#d48}[newitem.name!t]{/color}!"
    hide screen reward

    jump start_crafting

##QUESTS
label view_quests:
    scene bg lab
    call screen quests(page=0) with Dissolve(.2)

label activequest:
    call screen quests(page=0)
    jump test_menu

label completedquest:
    call screen quests(page=1)
    jump test_menu

## SHOP
label market_buy:
    scene bg shop
    call screen shop(market)
    jump test_menu

label market_sell:
    scene bg shop
    call screen inventory(inv, selling=True)
    jump test_menu


###
###
###

label s0p0:
    
    scene ch0 with fade
    "(click to continue)"

    scene bg13blank with dissolve

    "It's a normal Sunday night for you and your family."
    "Gathered around a table, you've all lost track of how many games you've played."

    scene bg13inc with dissolve

    "It's quiet. You hear the Mahjong tiles clink softly against the table, and occasional calls from you and your family members as you draw, steal, or discard tiles."
    "You look at your tiles. You only need one more to win. You're waiting and waiting, until someone places the tile you need in the center."

    scene bg13com with dissolve

    "..."
    "You win! You've just assembled the ultimate Mahjong hand: the \"thirteen orphans\"! Statistics say that the probability of getting this hand is really really small! (~1/2464)"
    "You do a little dance in front of your family, because you are so cool."
    "That was the last game of the day."

    scene bg13blank with dissolve

    "It's getting pretty late, so you clean the Mahjong set up and put it away."
    
    scene bgletter with fade

    "Suddenly, one of your family members enters the room with an envelope in hand. They hand it to you."

    $ InvItem(*envelope_closed).pickup(1)

    show iconenv at truecenter
    "Received item: Suspicious Unopened Envelope"

    "Ah. Let's check that out!"

    $ hop = "lettercheck"
    jump inventory

label lettercheck:
    if "envelope_open" in made_recipes:
        jump s0p1
    else:
        jump noletter

label noletter:

    scene bgerror

    "Hey! No speedrunning shenanigans here. Go open that letter!"
    jump inventory

label s0p1:

    "Would you like to read the envelope?"
    $ hop = "s0p2"

    menu:

        "Yes":
            jump s0p2

        "Yes":
            jump s0p2

label s0p2:

    "Wait! Before you read this envelope..."

    $ p_name = renpy.input("What is your name? (Default: Bamboo)")
    $ p_name = p_name.strip()
    if p_name == "":
        $ p_name="Bamboo"    

    scene bgletter with fade
    
    "\"Dear %(p)s,"

    "I've been considering retirement for a while, but I still have my flower shop in Mojan to tend to."
    "I've heard from your parents that you are unemployed (lol), so if you would be so kind, could you take care of my shop for me?"
    "I think it would be a good learning experience for you, and the neighbors and customers are very sweet."

    "Sincerely, Aunt T\""

    "What do you do?"

    menu:

        "Accept":
            jump s0p3

        "Decline":
            jump s0p3o2

        "Ignore":
            jump s0p3o3

label s0p2a:

    scene bgletter with fade
    
    "\"Dear %(p)s,"

    "I've been considering retirement for a while, but I still have my flower shop in Mojan to tend to."
    "I've heard from your parents that you are unemployed (lol), so if you would be so kind, could you take care of my shop for me?"
    "I think it would be a good learning experience for you, and the neighbors and customers are very sweet."

    "Sincerely, Aunt T\""

    "What do you do?"

    menu:

        "Accept":
            jump s0p3

label s0p3:
    
    "This seems like an excellent offer. You used to help your aunt arrange flowers when she lived close by, so you already have some experience."
    "Running a shop in a small town shouldn't be too much of a problem."
    "You eagerly send her your reply:"

    scene bgletter with fade

    p "\"Dear Aunt T,"

    p "Yes, I will go. I shall be a basement dweller no longer."

    p "Sincerely, %(p)s\""

    "Yes, that should work."

    scene black with fade

    "A few days later, you receive a response:"

    scene bgletter with fade

    "\"Dear %(p)s,"

    "Thank you so much! I've attached some things that might be useful on the back."

    "Sincerely, Aunt T\""

    $ InvItem(*flosho_key).pickup(1)
    $ InvItem(*flosho_photo).pickup(1)

    scene bgletter
    show iconfloshokey at truecenter
    "Received item: Flower Shop Key"
    scene bgletter
    show iconfloshophoto at truecenter
    "Received item: Flower Shop Photograph"

    scene bgletter

    "Time to start packing!"

    scene black with fade

    jump s1p0
    

label s0p3o2:

    "You remember how stressful it was arranging flowers with your aunt on weekends."
    "You know that it's a family tradition to have someone run a flower shop, but you'd rather not. You send her a quick reply."

    scene bgletter with fade

    p "\"Dear Aunt T,"

    p "No."

    p "Sincerely, %(p)s\""

    jump s0end

label s0p3o3:

    "You're not even sure why your aunt sent you a letter instead of just emailing, texting, or calling you like a normal person, so you chose to ignore the letter. What if it was a scam?"

    scene bgtrash
    
    "You recycle the letter."

    jump s0end

label s0end:

    scene bgdeadfish

    "And so, you go about your life as always: being unemployed, having no purpose, and being the human embodiment of dead drifting fish."

    "GAME OVER"

    "..."

    "Come on now, are you sure you want to do it like this?"
    "Do you just hate taking risks or something?"
    "You know you made the wrong decision."

    scene bgclock

    "Let's do that again, but this time, accept her letter. Otherwise you'll spend your whole life struggling to find a job in the urban concrete jungle you live in."

    jump s0p2a

label s1p0:

    scene ch1 with fade
    ""

    scene bgbus with dissolve
    
    "The bus ride to Mojan is lonely."
    "You are one of two people on the ride; a stranger joined you at the previous stop."
    "The deafening silence is about to end when you finally see the town limit sign over the next hill. Finally! No more boring, winding roads, boring, random buildings, or boring, rolling grasslands."
    "The other passenger follows your gaze out the window. He hasn't spoken to you this whole ride, but you can tell from the way he's closing his book this is his stop too."

    show charyi

    $ yw_name="Random Stranger"

    yw "What's brought you to this little town? I wouldn't say it's the more popular or interesting place to visit."
    
    "He's looking at your with an unreadable expression, and it's hard to tell because of the sunglasses."

menu:

    "Be vague":
        jump s1p1o1

    "Be honest":
        jump s1p1o2

label s1p1o1:

    p "A job opportunity opened up."

    jump s1p1

label s1p1o2:

    p "I'm inheriting my aunt's flower shop. She retired recently."

    jump s1p1

label s1p1:

    scene bgbus
    show charyi

    yw "I see..."

    "This guy's pretty weird. Let's find out what he's doing here and what his deal is."

    # scene change to interrogation mode popup or smthn

    "INTERROGATION MODE!"

    "Interrogation allows you to ASK QUESTIONS and GET ANSWERS. But be careful! Ask the wrong questions and get the wrong answers."

    "INTERROGATION START!"

    $ int1p1o1 = False
    $ int1p1o2 = False

menu int1p1:

    "WHO ARE YOU?" if not int1p1o1:
        $ int1p1o1 = True
        yw "Me? I'm just a nomad. I go from town to town."

    "WHY ARE YOU HERE?" if not int1p1o2:
        $ int1p1o2 = True
        yw "I've visited several smaller towns in this area. I haven't been to this one yet."

label after_int1p1:

    if int1p1o1 and int1p1o2:
        jump s1p2

    else:
        jump int1p1

label s1p2:

    "His answers are pretty vague. Perhaps asking more direct questions would be better."

    $ int1p2o1 = False
    $ int1p2o2 = False

menu int1p2:

    "WHAT'S WITH THOSE SHADES?" if not int1p2o1:
        $ int1p2o1 = True
        yw "I have... sensitive eyes. To light. Yes."
        "This fellow has unusually dark sunglasses. Not the kind normally worn indoors."

    "WHAT HAS IT GOT IN ITS POCKETSES?" if not int1p2o2:
        $ int1p2o2 = True
        yw "That's just a part of the jacket. It's like a metallic pocket square."
        "That doesn't seem right, but it's too hidden to see what it is."

label after_int1p2:

    if int1p2o1 and int1p2o2:
        jump s1p3

    else:
        jump int1p2



label s1p3:

    "If he won't give you straight answers, you'll just have to make some inferences about him later."
    "The bus comes to a halt, screeching as it stops at the stop. You can't read the other passenger's expressions due to the sunglasses, but it's easy to tell that he's in a hurry to leave."
    "He gives a quick thank you to the driver and hurries off the bus and down the beaten path into town."

    scene bgbus

    "INTERROGATION SUCCESS! (kinda?)"

    jump s1p4

label s1p4:

    "Okay. Now it's time to get off and head into town."

menu:

    "Step off":
        jump s2p0

    "Sit and wait":
        jump s1p5

label s1p5:

    "..."
    "You failed to leave the bus on time. The bus driver assumes you're getting off at the next stop, which is in another hour."
    "Because you're so afraid of social confrontation, you just sit in silence by yourself for the next hour, contemplating your actions. You're now stranded in a town you don't know."

    scene bgdeadfish

    "GAME OVER"
    "just kidding go back and make the right decision"

    jump s1p4a

label s1p4a:

    scene bgbus

    "Okay. Now it's time to get off and head into town."

menu:

    "Step off":
        jump s2p0

    "Sit and wait":
        jump s1p5a

label s1p5a:
    
    "Nice try."

menu:

    "Step off":
        jump s2p0


label s2p0:

    scene bgerror
    "Ah, fresh air."
    "You realize that the walk to the flower shop may be more complicated than you thought. The path is hard to make out in the tall grass. You see some buildings in the distance."
    "Oh wait, there was a map attached in the letter too."

    $ InvItem(*mojan_map).pickup(1)

    show iconmap at truecenter
    "Received item: Town Map"

    $ hop = "mapcheck"
    jump inventory

label mapcheck:

    jump s2p1

label s2p1:

    scene bgerror
    "Oh, looks like there's a path that way."
    $ hop = "s2p1"


    scene bgerror

    jump fin


# replace bgerror with grassy

label b:

    $ yw_name="Yi Wan"

    jump fin


###
###
###

label fin:

    "error code 1 we haven't programmed to here yet"

    return

label crash:

    "error code 0 something broke lmao game over"

    return