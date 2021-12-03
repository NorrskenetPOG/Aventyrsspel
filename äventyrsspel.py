import random as rand,sys,time
from os import system

class Player():
    def __init__(self, lifes):
        self.lifes = lifes
        self.max_level = 10
        self.current_level = 0
        self.exp = 0
        self.strenght = 5
        self.inventory = []
        self.item_bonus = []

    def player_hit(self):
        self.lifes -= 1
        
    def chest(self):
        self.inventory.append(str(rand.choice(item.item_names)))
        self.item_bonus.append(int(rand.choice(item.bonus_range)))
    
    def show_inventory(self):
        self.inevntory_layout = ""
        l = zip(player.inventory, player.item_bonus)
        for i, t in enumerate(l):
            self.inevntory_layout += f"{i}. {t[0]} +{t[1]} STR\n"
        return self.inevntory_layout

    def show_inventory_switch(self):
        self.inevntory_layout_switch = ""
        l = zip(player.inventory[0:5], player.item_bonus[0:5])
        for i, t in enumerate(l):
            self.inevntory_layout_switch += f"{i}. {t[0]} +{t[1]} STR\n"
        return self.inevntory_layout_switch

    def player_level_up(self):
        self.current_level += 1


class Item():
    def __init__(self):
        self.item_names = ["Meme Blade", "Diamantsvärd", "Gravitationspistol", "Energisvärd", "Skorpionspjut", "BFG-9000", "Styrke-dryck", "Styrke-emblem", "Railgun", "Blad av kaos", "Mästar-svärd", "Köttbullsmacka", "Baguettespjut"]
        self.bonus_range = range(1, 6)


class Monster():
    def __init__(self):
        self.strenght_range = range(0, 23)

    def monster_types(self):
        self.monster_strenght = rand.choice(monster.strenght_range)
        self.monster_name = None

        if monster.monster_strenght < 5:
            self.monster_name = "en Slime"
            return self.monster_name
        elif monster.monster_strenght < 8 and monster.monster_strenght >= 5:
            self.monster_name = "en Goblin"
            return self.monster_name
        elif monster.monster_strenght < 11 and monster.monster_strenght >= 8:
            self.monster_name = "ett Skelett"
            return self.monster_name
        elif monster.monster_strenght < 14 and monster.monster_strenght >= 11:
            self.monster_name = "ett Troll"
            return self.monster_name
        elif monster.monster_strenght < 17 and monster.monster_strenght >= 14:
            self.monster_name = "en Minotaur"
            return self.monster_name
        elif monster.monster_strenght < 20 and monster.monster_strenght >= 17:
            self.monster_name = "en Basilisk"
            return self.monster_name
        elif monster.monster_strenght < 22 and monster.monster_strenght >= 20:
            self.monster_name = "en Golem"
            return self.monster_name
        elif monster.monster_strenght <= 24 and monster.monster_strenght >= 22:
            self.monster_name = "en Drake"
            return self.monster_name


def rooms():
    room_list = [1, 2, 3, 4, 5]
    room_randomizer = rand.choice(room_list)

    while True:
        clear_screen()
        if room_randomizer == 1 or room_randomizer == 2:
            delay_print(f"Bakom dörren fanns en kista med en skatt\n")
            while True:
                player.chest()
                if len(player.inventory) >= 6:
                    print(f"\nDitt inventory är fullt\n--------------------------\n{player.show_inventory_switch()}\n--------------------------")
                    choice_inventory = input(f"Du måste slänga [{player.inventory[5]} +{player.item_bonus[5]} STR] som du hittade [S] eller byta ut det [B] -> ")
                    if choice_inventory == "B" or choice_inventory == "b":
                        clear_screen()
                        delay_print(f"\nVälj vilket vapen du vill byta ut")
                        print(f"\n--------------------------\n{player.show_inventory_switch()}")
                        change_inventory = int(input(delay_print(f"\n[0 - 4] -> ")))
                        if change_inventory >= 0 and change_inventory <= 4:
                            clear_screen()
                            delay_print(f"Du bytte [{player.inventory[change_inventory]} +{player.item_bonus[change_inventory]}] mot [{player.inventory[5]} +{player.item_bonus[5]} ST]")
                            player.inventory.pop(change_inventory)
                            player.item_bonus.pop(change_inventory)
                            break
                        else:
                            clear_screen()
                            continue
                    if choice_inventory == "S" or choice_inventory == "s":
                        clear_screen()
                        delay_print(f"Du slängde [{player.inventory[5]} +{player.item_bonus[5]} STR]")
                        player.inventory.pop(5)
                        player.item_bonus.pop(5)
                        break
                    else:
                        clear_screen()
                        continue
                    break
                else:
                    break
                            
                        
            break
        elif room_randomizer == 3 or room_randomizer == 4:

            delay_print(f"Bakom dörren fanns {monster.monster_types()} som attackerar dig")
            while True:
                if monster.monster_strenght > player.strenght + sum(player.item_bonus):
                    player.player_hit()
                    delay_print(f"\nDu förlorade mot {monster.monster_name}, -1 HP\n")
                    break
                else:
                    delay_print(f"\nDu besegrade {monster.monster_name}, +1 LVL\n")
                    player.player_level_up()
                    break
            break
                
        else:
            delay_print("Du tog skada av en fälla, -1 HP\n")
            player.player_hit()
            break

def clear_screen():
    system("cls || clear")

def delay_print(meningar):
    for tecken in meningar:
        sys.stdout.write(tecken)
        sys.stdout.flush()
        time.sleep(0.035)
    return ""

player = Player(10)
item = Item()
monster = Monster()
max_lifes = 10

print("\033[1;32;40m")
clear_screen()
character_name = str(input(delay_print("\nVad heter din karaktär?\nSkriv in för att starta -> ")))
clear_screen()

while True:
    print("\n--------------------------------------------\nDu har kommit till ett rum med tre dörrar...\n\n    Se spelarinfo                    [S]\n    Öppna inventory                  [I]\n    Gå genom vänster dörr            [V]\n    Gå genom mitten dörren           [M]\n    Gå genom höger dörr              [H]\n--------------------------------------------")
    choice = input(delay_print("Gör ett val -> "))
    
    if choice == "s" or choice == "S":
        clear_screen()
        print(f"\n----------------\n{character_name}    LVL.{player.current_level}\n\nHP:  [{player.lifes}/{max_lifes}]\nSTR: [{player.strenght + sum(player.item_bonus)}]\n----------------")
        
    elif choice == "i" or choice == "I":
        clear_screen()
        print(f"\n--------------------------\nInventory\n\n{player.show_inventory()}\n--------------------------")

    elif choice == "v" or choice == "V":
        rooms()

    elif choice == "m" or choice == "M":
        rooms()
        
    elif choice == "h" or choice == "H":
        rooms()
    
    else:
        clear_screen()
        continue

    if player.current_level == player.max_level:
        print("Du har vunnit spelet")
        break

    if player.lifes == 0:
        print(f"\n{player.lifes}/{max_lifes} HP kvar, spel slut, du förlorade")
        break
