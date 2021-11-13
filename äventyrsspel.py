#Äventyrsspel POGchamp

import random as rand

class Player():
    def __init__(self, lifes):
        self.lifes = lifes
        self.max_level = 10
        self.current_level = 0
        self.exp = 0
        self.strenght = 5

    def player_hit(self):
        self.lifes -= 1

    def player_level_up(self):
        self.exp += 1
        if self.exp >= 5:
            self.current_level += 1

class Item():
    def __init__(self):
        self.item_1 = "Diamantsvärd"
        self.item_2 = ""
        self.item_3 = ""
        self.item_4 = ""
        self.item_5 = ""

        bonus_list = range(1, 20)

        self.bonus_1 = rand.choice(bonus_list)
        self.bonus_2 = ""
        self.bonus_3 = ""
        self.bonus_4 = ""
        self.bonus_5 = ""


def rooms():
    room_list = [1, 2, 3]
    room_randomizer = rand.choice(room_list)

    while True:
        if room_randomizer == 1:
            print("Du hittade en kista med en värdefull skatt")
            break
        elif room_randomizer == 3:
            print("Du blir attackerad av ett månster")
            break
        else:
            print("Du gick i en fälla")
            player.player_hit()
            break





player = Player(10)
item = Item()

while True:
    print("""
----------------------------------
Du är i ett rum med tre dörrar...
    
    Se spelarinfo              [S]
    Öppna inventory            [I]

    Gå genom vänster dörr      [V]
    Gå genom mitten dörren     [M]
    Gå genom höger dörr        [H]
----------------------------------""")
    choice = input("Gör ett val -> ")
    
    if choice.strip() == "s" or choice == "S":
        print(f"""
--------------
    -HP:  [{player.lifes}]
    -STR: [{player.strenght}]
    -LVL: [{player.current_level}]
--------------
""")
        
    elif choice == "i" or choice == "I":
        print(f"""
--------------------------
    [{item.item_1}] +{item.bonus_1} STR
    [{item.item_2}] +{item.bonus_2} STR
    [{item.item_3}] +{item.bonus_3} STR
    [{item.item_4}] +{item.bonus_4} STR
    [{item.item_5}] +{item.bonus_5} STR
--------------------------
""")

    elif choice == "v" or choice == "V":
        rooms()

    elif choice == "m" or choice == "M":
        rooms()
        
    elif choice == "" or choice == "H":
        rooms()

    elif player.current_level == player.max_level:
        print("Du har vunnit spelet")
        break
