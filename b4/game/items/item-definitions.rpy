##############################################################################
# InvItem class

init -2 python:
    class InvItem(store.object):
        def __init__(self, name, image, value, info, id, cost=[]): #if you add any properties, list them up here, too!
            self.name = name #item name (as seen by the player)
            self.image = image #item art
            self.value = int(value) #market price
            self.info = info #item description
            self.id = id #string to be used as a codename
        #!! IMPORTANT !! don't change the order of anything above this line!
            ## INSERT REQUIRED PROPERTIES HERE ##
            self.cost = cost #list of ingredients, only necessary for craftable items
            ## INSERT OPTIONAL PROPERTIES HERE ##

    ## INVITEM FUNCTIONS

        # add item to the list of seen items
        def see(self):
            if self.id not in seen_items:
                seen_items.append(self.id)

        # add crafting recipe to the list of seen recipes
        def see_recipe(self):
            if self.id not in seen_recipes:
                seen_recipes.append(self.id)

        # see the item and add it to your inventory
        def pickup(self, amount=1):
            self.see()
            while amount>0:
                inv.append(self.id)
                amount -= 1

        # discard the item from your inventory
        def toss(self, amount):
            while amount>0:
                inv.remove(self.id)
                amount -= 1

        # exchange gold for an item
        def buy(self, amount):
            global gold

            self.see()

            gold -= self.value*amount
            while amount>0:
                inv.append(self.id)
                amount -=1

        # exchange an item for gold
        def sell(self, amount):
            global gold

            gold += int(self.value*amount/2)
            self.toss(amount)

        # craft an item
        def make(self, amount):

            self.see()

            while amount>0:
                for i in self.cost:
                    inv.remove(i)
                inv.append(self.id)
                made_recipes.append(self.id)
                amount -=1

        #for shop screen--checks that you can afford to buy 1 of any item
        def check_price(self):
            if self.value <= gold:
                return True
            return False

##############################################################################
# more functions! (not part of InvItem)

    # turns the item tuple into the item object
    def set_item(self):

        for i in itemlist:
            if self==i[4]: #checks the id--this is why you can't change the order!!
                return i

    #inventory sorting
    def sortbyname(i):
        thisitem = InvItem(*set_item(i))
        return thisitem.name

    def sortbyprice(i):
        thisitem = InvItem(*set_item(i))
        return thisitem.value

    # for crafting-screens.rpy--checks that you are able to craft at least 1 of the item
    def check_ingredients(craftitem):

        check = 0
        for i in craftitem.cost:
            if inv.count(i) > 0:
                check += 1

        if check == len(craftitem.cost):
            return True

        return False

    # used to check if you have battle items in battle-screens.rpy--but you can make other lists to check for too!
    def check_inv_for(itemtype):
        for i in itemtype:
            if inv.count(i) > 0:
                return True

##############################################################################
# ITEM DEFINITIONS

# INGREDIENTS
# define item_water = (_("Plain Ol' Water"), "item water", 2,
    # _("A fundamental ingredient for alchemy and potion-making. It's clean enough to drink."), "item_water")

# define item_paper = (_("Paper"), "item paper", 3,
    # _("The support class of candymaking materials."), "item_paper")

# define item_beet = (_("Dat Beet"), "item beet", 8,
    # _("You can make sugar from these things. Sick!"), "item_beet")

define envelope_closed = (_("Suspicious Unopened Envelope"), "assetenv", 20,
    _("You can open this! Click Return in the bottom left to access the Crafting menu."), "envelope_closed")

define flosho_key = (_("Flower Shop Key"), "assetfloshokey", 30,
    _("The key to your new flower shop."), "flosho_key")

define flosho_photo = (_("Photograph of Flower Shop"), "assetfloshophoto", 31,
    _("A photograph of your new flower shop."), "flosho_photo")

define mojan_map = (_("Map of Mojan Town"), "assetmaps2item", 40,
    _("placeholder description here"), "mojan_map")

#revised map items
# define mojan_map_five = (_("Updated Map of Mojan Town"), "assetmaps5item", 41,
#     _("placeholder description here"), "mojan_map_five")

# define mojan_map_six = (_("Updated Map of Mojan Town"), "assetmaps6item", 42,
#     _("placeholder description here"), "mojan_map_six")
# 2032 wide 1143 short, cut 1280, move to top within 3px

define burnt_box = (_("Burnt Box"), "assetboxold", 50,
    _("Charred to perfection. Doesn't work anymore."), "burnt_box")

define dying_will = (_("Unfinished Will"), "assetwill", 51,
    _("Found in your new flower shop..."), "dying_will")



# CRAFTABLE
# define item_sugar = (_("Sweet Sweet Sugar"), "item sugar", 10,
    # _("Double sweet! Made from beets."), "item_sugar",
    # ["item_beet", "item_water"])

# define item_sucker = (_("Common Sucker"), "item sucker", 13,
    # _("Syrup's favorite. Use it to recover HP during battle!"), "item_sucker",
    # ["item_sugar", "item_paper"])

define envelope_open = (_("Opened Envelope"), "assetenvopen", 21,
    _("Opened letter. Intended to be read. Try clicking Continue in the Return menu after you make this."), "envelope_open", ["envelope_closed"])

define flosho_photo_front = (_("Front of Flower Shop Photo"), "assetfloshophotofront", 32,
    _("There were many vines and flowers growing on the walls when this was taken. How ironic."), "flosho_photo_front")

define flosho_photo_back = (_("Back of Flower Shop Photo"), "assetfloshophotoback", 33,
    _("This photo is dated July 7th, 20XX, just a week ago..."), "flosho_photo_back")

##############################################################################
# ITEM LISTS

# ALL ITEMS (every single one!!)
define itemlist = [
    # item_water,
    # item_paper,
    # item_beet,
    # item_sugar,
    # item_sucker,
    envelope_closed,
    envelope_open,
    flosho_key,
    flosho_photo,
    flosho_photo_front,
    flosho_photo_back,
    mojan_map,
    dying_will,
    ]

# all items that can be crafted
define allrecipes = [
    # "item_sugar",
    # "item_sucker",
    "envelope_open",
    "flosho_photo_front",
    "flosho_photo_back",
    ]

# all items that can be used in battle
define battle_items = [
    # "item_sucker"
    ]

## INSERT NEW RECIPE LISTS HERE ##

# for recipes screen
define recipelists = [ allrecipes, battle_items ]
define recipelist_names = [ _("All"), ]
