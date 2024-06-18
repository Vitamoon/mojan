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

    "Suddenly, one of your family members enters the room with an envelope in hand. They hand it to you."

    $ InvItem(*envelope_closed).pickup(1)

    show iconenv at truecenter with dissolve
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
    show iconfloshokey at truecenter with dissolve
    "Received item: Flower Shop Key"
    scene bgletter
    show iconfloshophoto at truecenter with dissolve
    "Received item: Flower Shop Photograph"

    scene bgletter

    "Time to start packing!"

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
    scene black with fade
    scene ch1 with fade
    ""

    scene bgbus with dissolve
    
    "The bus ride to Mojan is lonely."
    "You are one of two people on the ride; a stranger joined you at the previous stop."
    "The deafening silence is about to end when you finally see the town limit sign over the next hill. Finally! No more boring, winding roads, boring, random buildings, or boring, rolling grasslands."
    "The other passenger follows your gaze out the window. He hasn't spoken to you this whole ride, but you can tell from the way he's closing his book this is his stop too."

    show charyi

    $ yw_name ="Random Stranger"

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

    scene bg13blank

    "INTERROGATION MODE!"
    "Interrogation allows you to ASK QUESTIONS and GET ANSWERS. But be careful! Ask the wrong questions and get the wrong answers."

    scene interrostart

    "INTERROGATION START!"

    scene bgbus
    show charyi

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
        show iconsunglas at truecenter with dissolve
        "This fellow has unusually dark sunglasses. Not the kind normally worn indoors."
        scene bgbus
        show charyi

    "WHAT HAS IT GOT IN ITS POCKETSES?" if not int1p2o2:
        $ int1p2o2 = True
        yw "That's just a part of the jacket. It's like a metallic pocket square."
        show iconbadgepocket at truecenter with dissolve
        "That doesn't seem right, but it's too hidden to see what it is."
        scene bgbus
        show charyi

label after_int1p2:

    if int1p2o1 and int1p2o2:
        jump s1p3

    else:
        jump int1p2



label s1p3:

    scene bgbus
    show charyi

    "If he won't give you straight answers, you'll just have to make some inferences about him later."
    "The bus comes to a halt, screeching as it stops at the stop. You can't read the other passenger's expressions due to the sunglasses, but it's easy to tell that he's in a hurry to leave."
    "He gives a quick thank you to the driver and hurries off the bus and down the beaten path into town."

    scene interrostop

    "INTERROGATION SUCCESS! (kinda?)"

    scene bgbus

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
        jump s1p4b

label s1p4b:
    
    "Nice try."
    jump s1p4c

label s1p4c:

    "Okay. Now it's time to get off and head into town."

menu:

    "Step off":
        jump s2p0

    "Sit and wait":
        jump s1p4d

label s1p4d:

    "Stop it!"
    
    "Okay. Now it's time to get off and head into town."

menu:

    "Step off":
        jump s2p0


label s2p0:
    scene black with fade
    scene ch2 with fade
    ""

    scene bgpath with dissolve
    "Ah, fresh air."
    "You realize that the walk to the flower shop may be more complicated than you thought. The path is hard to make out in the tall grass. You see some buildings in the distance."
    "Oh wait, there was a map attached in the letter too."

    $ InvItem(*mojan_map).pickup(1)

    show iconmap at truecenter with dissolve
    "Received item: Town Map"

    scene assetmaps2

    jump s2p1

label s2p1:

    scene bgpath

    "Oh, looks like there's a path that way."
    $ hop = "s2p1"

    "You take a leisurely stroll into town."

    scene bgshopextsus

    "As you approach the flower shop, there's a figure crouching down in front of the door. You already recognize the jacket... what is he doing?"

    p "Hey! What are you doing?"

    scene bgshopext
    show charyi

    "The stranger jolts and turns around, hiding something behind his back."

    yw "Um, I... I was..."

    scene interrostart

    "INTERROGATION START!"

    scene bgshopext
    show charyi
    
    $ int2p1o1 = False
    $ int2p1o2 = False
    $ int2p1o1p = False

menu int2p1:

    "WHAT ARE YOU HOLDING?" if not int2p1o1:
        $ int2p1o1 = True
        $ int2p1o2 = True
        show iconlockpick at truecenter with dissolve
        "Upon closer inspection, it seems that he is holding a set of lockpicks."
        scene bgshopext
        show charyi

    "WHY ARE YOU TRYING TO ENTER MY FLOWER SHOP?" if int2p1o2:
        yw "I wasn't trying to enter! I was just seeing if it was open! I really want some flowers, haha."
        $ int2p1o1p = True



label after_int2p1:

    if int2p1o1p and int2p1o2:
        "After your questions, he turns around and... what's he doing?"
        scene bgshopextsus
        jump int2p2

    else:
        jump int2p1

menu int2p2:

    "WHY ARE YOU STILL TRYING TO ENTER MY SHOP?":
        scene bgshopext
        show charyi

        yw "Okay, okay, fine. I'll explain. First of all, my name is Yi."

        $ yw_name = "Yi"

        show iconyi at truecenter with dissolve
        yw "I'm a detective from the next town over, and there is a crime that happened on the grounds of this flower shop a while back; thirteen years ago to be precise, and I'm trying to solve it."

        scene bgshopext
        show charyi
        yw "Your flower shop may hold vital clues to solving this case."

        show iconbadge at truecenter
        yw "Here's my detective badge. Please, I need to search your place for clues."
        $ yw_name = "\"Detective\" Yi Wan"

        scene bgshopext
        show charyi
        p "Do you have a warrant?"

        yw "Well, no, but please trust me on this one."

        p "Hmmm, nah."
        "You unlock your shop with your key and slam the door shut, locking the door behind you."

        scene interrostop
        "INTERROGATION SUCCESS!"

        jump s2p2


label s2p2:
    scene black with fade
    scene ch3 with fade
    ""

    scene bgshopint

    "Now that that's done, you finally get to see the inside of the place you'll be staying for who knows how long."
    "The place is pretty empty, but you're excited to look around and begin planning what will go where."
    "There's already some old furniture in the room."

    $ s2p3o1 = False
    $ s2p3o2 = False
    $ s2p3o3 = False

menu s2p3:

    "Look at tables" if not s2p3o1:
        $ s2p3o1 = True
        "The tables are empty, save for some dirt left over from when there were flowers there."
        jump s2p3

    "Look at shelves" if not s2p3o2:
        $ s2p3o2 = True
        "There are a few half-empty seed packets left on the shelf along with a book on horticulture."
        jump s2p3

    "Look at door" if not s2p3o3:
        $ s2p3o3 = True
        "Locked. You notice a “OPEN” sign on the floor by the door. You'll need to hang that up later."
        jump s2p3

    "Done":
        jump s2p4


label s2p4:

    "There doesn't seem to be anything else of interest in the front of the shop, so you wander towards the back."
    "There's some junk on the ground."
    show iconboxold at truecenter with dissolve
    "Huh, what's in this box?"
    "The box is charred, slightly rusty, and has a broken lock."

menu:
    "Open suspicious box":
        scene bgshopint
        show iconenv at truecenter with dissolve
        "There’s a letter inside!"
        "It says \"To my beloved children\" on the outside."
        "That’s odd, your aunt never had any children. You could open it, but it feels wrong to open a letter not addressed to you."

menu:
    "Open it anyway":
        jump s2p5

label s2p5:
    scene bgshopint
    show iconwill at truecenter with dissolve
    "\"Dear my beloved children,"
    "I don’t have much time left. My old bones can’t keep up your active livelihoods and it is time for me to retire."
    "Some of you are old enough to leave on your own now, and I wish all of you the best of luck in life. Please take care of each other."
    "I apologize for any sort of disappointments I may have caused while running this place, but know that I do love all of you. I hope that you all can forgive me for\""

    "The sentence trails off, unfinished. There's no name anywhere on the letter."

    $ InvItem(*dying_will).pickup(1)
    "Received item: Unfinished Will"

    scene bgshopint
    show iconboxold at truecenter with dissolve
    $ InvItem(*burnt_box).pickup(1)
    "Received item: Burnt Box"

    scene bgshopint
    "You hear your front door rattling, a pause, and then a knock, alerting you to someone trying to enter. Good thing you locked the door!"

    scene bgshopextsus
    "You walk to the front and see Yi trying to get in again. You consider channeling your inner grandpa to tell him to get off your lawn, but think otherwise when you see how frantic he looks."

    scene bgshopext
    show charyi
    "You open the door, making sure to stand firmly in the doorway as to not allow him to slip inside."

    p "What do you want?"
    yw "Have you looked around the shop?"
    p "Yes, why?"
    yw "Have you, by chance, come across anything that looks burnt?"
    p "Yeah... a box."
    yw "Good, good, good. Anything in the box? Can I see the box?"
    p "A letter. And sure, but you can't touch it, or the box."

    "You pull out the box and show it to him, spinning it around in your hands to show all sides of it."
    "Then you show him the letter. It's hard to tell whether or not he's reading it because he still has those darn sunglasses on."
    "It must mean something to him, because he takes a small notebook out and starts scribbling into it."

    yw "I'll have to be honest with you; the case I'm working on is close to being dropped forever, but I feel the need to solve it because there circumstances surrounding it are just too strange."
    yw "An orphanage burnt down right where your flower shop stands thirteen years ago, but there doesn't seem to be an eye witnesses at all."
    yw "No one is able to remember what happened that day. Luckily all of the orphans survived. Only the orphanage owner died."
    yw "If you want to find out more, I would suggest checking out the newspaper archives. That's where I'll be heading."

    "The detective thanks you and heads off into the distance. It's getting late, too. You should head to bed."
    "As you close the door, you consider what Yi had said to you just a moment ago. It did sound a little interesting... Maybe you should figure out where those newspaper archives are tomorrow?"

    jump s4p1

label s4p1:
    scene black with fade
    scene ch4 with fade
    ""

    scene bgshopint

    "It’s the next day, you are well rested after sleeping for several hours to make up for the time difference. You remember what the detective said, and consider trying to go to the newspaper archives today. It’s not like your seeds are here yet and even if they were, they probably won't die if left alone for an hour or two."
    "The first thing you realize though, is that you have no idea where the archives are, and you're not sure how to start looking because there isn't any signal out here, so your phone is practically useless."
    "You're now just standing awkwardly in the front of your flower shop, looking around to plan what to do today? Where do you even start?"
    "Thankfully, you don't have to think, because you can see a man through the door, and he's holding a newspaper. How convenient! You quickly go to open the door and greet him before he goes away."
    
    scene bgshopext
    show chardan
    "He seems a little startled when you open the door."

label s4p2:
    scene bgshopext
    show chardan
    p "Hi. Are you the mail man?"
    $ b_name = "Mailman"
    b "Yes? Yes I am. Are you perhaps new here? I'm sure there used to be an older woman here."
    p "Yeah, that was my aunt. I'm running the flower shop for her now."
    b "Ah, glad to see you continuing family tradition. I did love to look at the flowers when I would drop the newspapers off every week."

menu s4p3:
    "Interrogate him":
        scene interrostart
        "INTERROGATION START!"
        scene bgshopext
        show chardan

        jump s4p4

    "Don't interrogate him":
        jump s4p6

menu s4p4:

    "WHO ARE YOU?":
        b "Me? I'm the mailman for the Zhen Post. I cover all of Mojan, mostly handing out the weekly news. Not many people send letters."
        "You're about to ask about the newspaper archives, but the man places the newspaper into your hands and walks away. Maybe you shouldn't have interrogated him."
        scene interrostop
        ""
        scene black
        "TIME REVERSAL"
        jump s4p2

    "Inspect his Outfit":
        jump s4p5

menu s4p5:
    "Ask about his Satchel":
        b "This is my my messenger bag. Why do you need to know about it?"
        "You're about to ask about the newspaper archives, but the man places the newspaper into your hands and walks away. Maybe you shouldn't have interrogated him."
        scene interrostop
        ""
        scene black
        "TIME REVERSAL"
        jump s4p2

    "Ask about his Hat":
        b "I'm wearing a hat because it's sunny outside. I fear my skin is sensitive to the sunlight."
        "You're about to ask about the newspaper archives, but the man places the newspaper into your hands and walks away. Maybe you shouldn't have interrogated him."
        scene interrostop
        ""
        scene black
        "TIME REVERSAL"
        jump s4p2

    "Ask about his Suit":
        b "Can a gentleman not wear nice clothes?"
        "You're about to ask about the newspaper archives, but the man places the newspaper into your hands and walks away. Maybe you shouldn't have interrogated him."
        scene interrostop
        ""
        scene black
        "TIME REVERSAL"
        jump s4p2

    "Ask about his Newspapers":
        b "I was going to place this at your door step..."
        "You're about to ask about the newspaper archives, but the man places the newspaper into your hands and walks away. Maybe you shouldn't have interrogated him."
        scene interrostop
        ""
        scene black
        "TIME REVERSAL"
        jump s4p2

    
label s4p6:

    p "Is there a way that I can read newspapers from previous weeks? I'd like to learn about this town and the latest news so I won't be as confused. It's a shame there's no service out here."
    b "Well... we do archive newspapers. Just go to the address written on today's paper and you can ask the front desk to let you read them. Just say that Dan sent you."
    $ b_name = "Dan the Mailman"
    p "Thanks so much. When I start making flower arrangements I can give you one for free."
    b "No need. Just looking at them in the store is enough."
    "Dan nods, handing you the newspaper with a polite smile, and then turns to go and deliver the newspapers to your neighbors."
    scene bgshopext

    "You look the address for the Zhen Post, so you decide to head over. It's about a 30 minute bus ride."

    jump s5p1


label s5p1:
    scene black with fade
    scene ch5 with fade
    ""

    scene bgarchives

    "You find the Zhen Post in the next town over, and surprisingly it just looked like a regular house from the outside. When you entered, there is a receptionist sitting at the desk. After telling them that Dan sent you, you're now standing in a dimly lit hallway."
    "It looks sort of like a warehouse, but each room down the hall is sorted by intervals of 5 years. You immediately book it to the room that would have newspapers from 13 years ago. From some reason, the door is already open."
    "You walk over to shelves and take a look at whats on them."
    "They are arranged in a way to allow the most storage space for discarded newspapers. You are able to see labels peeking out from between newspapers that indicate the general dates and years that the newspapers are from."

    
    "The shelf is dated 20XX" # what year

    "The shelf containing newspapers from 13 years ago is surprisingly dust free, these archives must be maintained regularly. You decide push around a few stacks and notice a stack of copies pushed to the very back. Incidentally, these are the of the issue that you need."
    "You grab one of the newspapers on top to read."
    
    "\"BREAKING NEWS! LOCAL ORPHANAGE BURNT DOWN! ONE CASUALTY REPORTED.\""
    
    "Huh, that means Yi and Dan were orphans this whole time. It explains why Yi is back to investigate, but why is Dan still around?"
    "You shuffle all the newspapers back in place and pocket the newspaper from 13 years ago. You hope that you haven’t left a trace here, and prepare any lie you would need in case you got caught."
    "Suddenly, the door to the room swings open and you freak out for a second before realizing it's Yi who's entered. He must have been the one who unlocked the door at first."
    show charyi
    yw "Oh, you're here. Have you found anything?"

    "You're not really in the mood to show him the paper so instead you INTERROGATE HIM!"

    scene interrostart

    "INTERROGATION START!"

    scene bgarchives
    show charyi

    p "So you're one of the orphans, huh?"
    yw "Erm, yes, I am. I swear I didn’t mean to hide it but it just never came up in conversation before."

menu s5p2:
    "Did you know Huo well?":
        yw "I wasn’t close with her but I knew her, she doesn’t seem like the kind of person to do this."

    "Do you know where the other orphans live now?":
        yw "I know where a few are, Huo is in Mojan in jail, and her friends are still there too. I believe the bird siblings are there as well, but quite a few have moved here, to Zhen. I've researched them all. They're all nearby, which is a little strange."

    "What is the meaning of life?":
        yw "What?"

# make so that all options have to be chosen

label s5p3:
    scene interrostop
    "Interrogation Finished!"

    "After you are satisfied with his responses, you decide to show him the newspaper that you found, as well as the strange circumstances that you found them in. He ponders that a bit, writes something down in his journal, and then puts it away and nods at you. Yi gives you the address of the local jail and you decide to head over as soon as you’re done looking around."
    yw "We should visit Huo. She might have something to say about all of this. I'll round up all of the orphans for you and bring them to the jail. Something is fishy here."





#dun dun dun dun-dun
#dun dun dun dun-dun
#dun dun dun dunnadunnadun dun 





#label after_s3p4:

#    if s3p4a and s3p4b:
#        jump s3p5

#    else:
#        jump s3p4








label b:

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