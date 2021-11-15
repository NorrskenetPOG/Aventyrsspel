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
        self.item_1 = None
        self.item_2 = None
        self.item_3 = None
        self.item_4 = None
        self.item_5 = None

        self.bonus_list = range(1, 20)

        self.bonus_1 = None
        self.bonus_2 = None
        self.bonus_3 = None
        self.bonus_4 = None
        self.bonus_5 = None
    
        self.item_list = ["Diamantsvärd", "Gravitations pistol", "Energi svärd", "Skorpion spjut", "BFG-9000", "Styrke dryck", "Styrke emblem", "Railgun", "Blad av kaos", "Mästar svärd"]

    def pickup_items(self):
        self.random_item = rand.choice(item.item_list)
        print(self.random_item)
        while True:
            if item.item_1 == None:
                item.item_1 == item.random_item and item.bonus_1 == rand.choice(item.bonus_list)
                return item.item_1 and item.bonus_1
            elif item.item_2 == None:
                item.item_2 == item.random_item and item.bonus_2 == rand.choice(item.bonus_list)
                return item.item_2 and item.bonus_2
            elif item.item_3 == None:
                item.item_3 == item.random_item and item.bonus_3 == rand.choice(item.bonus_list)
                return item.item_3 and item.bonus_3
            elif item.item_4 == None:
                item.item_4 == item.random_item and item.bonus_4 == rand.choice(item.bonus_list)
                return item.item_4 and item.bonus_4
            elif item.item_5 == None:
                item.item_5 == item.random_item and item.bonus_5 == rand.choice(item.bonus_list)
                return item.item_5 and item.bonus_5
            else:
                print("Ditt inventory är fullt")
                item_choise = int(input("Vill du slänga bort [S] eller byta ut föremålet [B] -> "))
                if item_choise == "S" or item_choise == "s":
                    print(f"Du slägde bort {self.random_item} och fortsatte")
                elif item_choise == "B" or item_choise == "b":
                    replace_item = input(f"""
--------------------------
1.    [{item.item_1}] +{item.bonus_1} STR
2.    [{item.item_2}] +{item.bonus_2} STR
3.    [{item.item_3}] +{item.bonus_3} STR
4.    [{item.item_4}] +{item.bonus_4} STR
5.    [{item.item_5}] +{item.bonus_5} STR
--------------------------
Vilken vill du byta ut 1-5 -> """)
                    if replace_item == 1:
                        item.item_1 == item.random_item and item.bonus_1 == rand.choice(item.bonus_list)
                        return item.item_1 and item.bonus_1
                    elif replace_item == 2:
                        item.item_2 == item.random_item and item.bonus_2 == rand.choice(item.bonus_list)
                        return item.item_2 and item.bonus_2
                    elif replace_item == 3:
                        item.item_3 == item.random_item and item.bonus_3 == rand.choice(item.bonus_list)
                        return item.item_3 and item.bonus_3
                    elif replace_item == 4:
                        item.item_4 == item.random_item and item.bonus_4 == rand.choice(item.bonus_list)
                        return item.item_4 and item.bonus_4
                    elif replace_item == 5:
                        item.item_5 == item.random_item and item.bonus_5 == rand.choice(item.bonus_list)
                        return item.item_5 and item.bonus_5
                else:
                    print("Fel inmatning")
                    break
                break



#Osäker på den här klassen, går nog att göra poå ett annat sätt
class Monster():
    def __init__(self):
        strenghts = range(0, 20)
        self.monster_strenght = rand.choice(strenghts)
    
    def monster_types(self):
        self.monster_name = None

        if enemies.monster_strenght < 5:
            self.monster_name = "Slime"
            return self.monster_name
        elif enemies.monster_strenght < 10 and enemies.monster_strenght >= 5:
            self.monster_name = "Goblin"
            return self.monster_name
        elif enemies.monster_strenght < 15 and enemies.monster_strenght >= 10:
            self.monster_name = "Zombie"
            return self.monster_name
        elif enemies.monster_strenght < 20 and enemies.monster_strenght >= 15:
            self.monster_name = "Basilisk"
            return self.monster_name



def rooms():
    room_list = [1, 2, 3]
    room_randomizer = rand.choice(room_list)

    while True:
        if room_randomizer == 1:
            print(f"Bakom dörren fanns en kista med en skatt")
            item.pickup_items()
            break
        elif room_randomizer == 3:
            print(f"Bakom dörren fanns en {enemies.monster_types()} som attackerar dig")
            break
        else:
            print("Du tog skada av en fälla bakom dörren och förlorade ett HP")
            player.player_hit()
            break




enemies = Monster()
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
    HP:  [{player.lifes}]
    STR: [{player.strenght}]
    LVL: [{player.current_level}]
--------------
""")
        
    elif choice == "i" or choice == "I":
        print(f"""
--------------------------
1.    [{item.item_1}] +{item.bonus_1} STR
2.    [{item.item_2}] +{item.bonus_2} STR
3.    [{item.item_3}] +{item.bonus_3} STR
4.    [{item.item_4}] +{item.bonus_4} STR
5.    [{item.item_5}] +{item.bonus_5} STR
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

