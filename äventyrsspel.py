import random as rand

class Player():
    def __init__(self, lifes):
        self.lifes = lifes
        self.max_level = 10
        self.current_level = 0
        self.exp = 0
        self.strenght = 5
        self.inventory = []
        self.item_bonus_list = []

    def player_hit(self):
        self.lifes -= 1
        
    def chest(self):
        self.inventory.append(str(rand.choice(item.item_names)))
        self.item_bonus_list.append(int(rand.choice(item.bonus_list)))
    
    def show_inventory(self):
        self.show_inventory1 = ""
        l = zip(player.inventory, player.item_bonus_list)
        for i, t in enumerate(l):
            self.show_inventory1 += f"{i}. {t[0]} +{t[1]} STR\n"
        return self.show_inventory1

    def show_inventory_for_switch(self):
        self.show_inventory2 = ""
        l = zip(player.inventory[0:5], player.item_bonus_list[0:5])
        for i, t in enumerate(l):
            self.show_inventory2 += f"{i}. {t[0]} +{t[1]} STR\n"
        return self.show_inventory2

    def pleayer_level_up(self):
        self.current_level += 1


class Item():
    def __init__(self):
        self.item_names = ["Diamantsvärd", "Gravitations pistol", "Energi svärd", "Skorpion spjut", "BFG-9000", "Styrke dryck", "Styrke emblem", "Railgun", "Blad av kaos", "Mästar svärd"]
        self.bonus_list = range(1, 10)


class Monster():
    def __init__(self):
        self.strenghts = range(0, 23)

    def monster_types(self):
        self.monster_strenght = rand.choice(enemies.strenghts)
        self.monster_name = None

        if enemies.monster_strenght < 5:
            self.monster_name = "en Slime"
            return self.monster_name
        elif enemies.monster_strenght < 8 and enemies.monster_strenght >= 5:
            self.monster_name = "en Goblin"
            return self.monster_name
        elif enemies.monster_strenght < 11 and enemies.monster_strenght >= 8:
            self.monster_name = "ett Skelett"
            return self.monster_name
        elif enemies.monster_strenght < 14 and enemies.monster_strenght >= 11:
            self.monster_name = "ett Troll"
            return self.monster_name
        elif enemies.monster_strenght < 17 and enemies.monster_strenght >= 14:
            self.monster_name = "en Minotaur"
            return self.monster_name
        elif enemies.monster_strenght < 20 and enemies.monster_strenght >= 17:
            self.monster_name = "en Basilisk"
            return self.monster_name
        elif enemies.monster_strenght < 22 and enemies.monster_strenght >= 20:
            self.monster_name = "en Golem"
            return self.monster_name
        elif enemies.monster_strenght <= 24 and enemies.monster_strenght >= 22:
            self.monster_name = "en Drake"
            return self.monster_name


def rooms():
    room_list = [1, 2, 3]
    room_randomizer = rand.choice(room_list)

    while True:
        if room_randomizer == 1:
            print(f"Bakom dörren fanns en kista med en skatt")
            player.chest()
            while True:
                if len(player.inventory) == 5:
                    print("Ditt inventory är fullt")
                    player.chest()
                    choice_inventory = input(f"Du måste slänga {player.inventory[5]} +{player.item_bonus_list[5]} STR som du hittade [S] eller byta ut det [B] -> ")
                    if choice_inventory == "B" or "b":
                        change_inventory = int(input(f"""
Välj vilket vapen du vill byta ut 
{player.show_inventory_for_switch()} 
[0 - 4] -> """))
                        player.inventory.pop(change_inventory)
                        player.item_bonus_list.pop(change_inventory)
                        break
                    if choice_inventory == "S" or "s":
                        player.inventory.pop(5)
                        player.item_bonus_list.pop(5) 
                        """verkar inte fungera"""
                        break
                    break
                else:
                    break
                            
                        
            break
        elif room_randomizer == 3:

            print(f"Bakom dörren fanns {enemies.monster_types()} som attackerar dig")
            while True:
                if enemies.monster_strenght > player.strenght + sum(player.item_bonus_list):
                    player.player_hit()
                    print(f"Du förlorade mot {enemies.monster_name}")
                    break
                else:
                    print(f"Du besegrade {enemies.monster_name}")
                    player.pleayer_level_up()
                    break
            break
                
        else:
            print("Du tog skada av en fälla bakom dörren och förlorade ett HP")
            player.player_hit()
            break


player = Player(10)
item = Item()
enemies = Monster()
max_lifes = 10

#inventory_list = ["%i: %s" % (index, value) for index, value in enumerate(player.inventory + player.item_bonus_list)]

character_name = str(input("""
------------------------------------------------------
    Vad heter din karaktär för att starta -> """))

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
----------------
{character_name}    LVL.{player.current_level}

    HP:  [{player.lifes}/{max_lifes}]
    STR: [{player.strenght + sum(player.item_bonus_list)}]
----------------
""")
        
    elif choice == "i" or choice == "I":
        print(f"""
--------------------------
Inventory

{player.show_inventory()}
--------------------------""")

    elif choice == "v" or choice == "V":
        rooms()

    elif choice == "m" or choice == "M":
        rooms()
        
    elif choice == "h" or choice == "H":
        rooms()

    if player.current_level == player.max_level:
        print("Du har vunnit spelet")

        break

    if player.lifes == 0:
        print(f"{player.lifes}/{max_lifes} HP kvar, spel slut, du förlorade")
        break
