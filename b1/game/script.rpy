# title

define p = Character("Bamboo", color="#ffffff")
define hop = "crash"

define yw = Character("Yi Wan", color="#3b305e")
define jw = Character("Jiu Wan", color="#feb3ff")
define jwt = Character("Jiu Wan?", color="#5f55f1")
define yb= Character("Yi Bing", color="#c0ac02")
define jb = Character("Jiu Bing", color="#6f18bc")
define yt = Character("Yi Tiao", color="#7b0e73")
define jt = Character("Jiu Tiao", color="#de12cf")
define e = Character("Dong", color="#1be5c6")
define w = Character("Nan", color="#f3ed4d")
define s = Character("Xi", color="#e99311")
define n = Character("Bei", color="#aaaaaa")
define r = Character("Hong Zhong", color="#c12c09")
define g = Character("Fa Cai", color="#2adf26")
define b = Character("Bai Ban", color="#b8eeff")

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

    scene bg13blank

    "It's a normal Sunday night for you and your family."
    "Gathered around a table, you've all lost track of how many games you've played."

    scene bg13inc

    "It's quiet. You hear the Mahjong tiles clink softly against the table, and occasional calls from you and your family members as you draw, steal, or discard tiles."

    scene bg13com

    "You look at your tiles. You only need one more to win. You're waiting and waiting, until someone places the tile you need in the center."
    "..."
    "You win! You've just assembled the ultimate Mahjong hand: the \"thirteen orphans\"! Statistics say that the probability of getting this hand is something really really small!"
    "You do a dance in front of your family, because you are so cool."
    "That was the last game of the day."

    scene bg13blank

    "It's getting pretty late, so you clean the Mahjong set up and put it away."
    
    scene bgletter

    "Suddenly, one of your family members enters the room with an envelope in hand. They hand it to you."

    $ InvItem(*envelope_closed).pickup(1)

    "Received item: Suspicious Unopened Envelope"

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

    $ p = renpy.input("What is your name? (Default: Bamboo)")
    $ p = p.strip()
    if p == "":
        $ p="Bamboo"
    
    "Dear %(p)s,"

    "I've been considering retirement for a while, but I still have my flower shop in Mojan to tend to."
    "I've heard from your parents that you are unemployed (lol), so if you would be so kind, could you take care of my shop for me?"
    "I think it would be a good learning experience for you, and the neighbors and customers are very sweet."

    "Sincerely, Aunt T."

    #Evidence updated: Aunt's Letter

    # choices screen

    jump crash

label crash:
    ###
    ###
    ###

    "error code 0 game over"

    return