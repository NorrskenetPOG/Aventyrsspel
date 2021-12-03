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

    def player_level_up(self):
        self.current_level += 1


class Item():
    def __init__(self):
        self.item_names = ["Meme Blade", "Diamantsvärd", "Gravitationspistol", "Energisvärd", "Skorpionspjut", "BFG-9000", "Styrke-dryck", "Styrke-emblem", "Railgun", "Blad av kaos", "Mästar-svärd", "Köttbullsmacka", "Baguettespjut"]
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
        clear_screen()
        if room_randomizer == 1:
            delay_print(f"Bakom dörren fanns en kista med en skatt")
            while True:
                player.chest()
                if len(player.inventory) >= 6:
                    print(f"\nDitt inventory är fullt\n--------------------------\n{player.show_inventory_for_switch()}\n--------------------------")
                    choice_inventory = input(f"Du måste slänga [{player.inventory[5]} +{player.item_bonus_list[5]} STR] som du hittade [S] eller byta ut det [B] -> ")
                    if choice_inventory == "B" or choice_inventory == "b":
                        clear_screen()
                        change_inventory = int(input(delay_print(f"\nVälj vilket vapen du vill byta ut \n--------------------------\n{player.show_inventory_for_switch()} \n[0 - 4] -> ")))
                        clear_screen()
                        delay_print(f"Du bytte [{player.inventory[change_inventory]} +{player.item_bonus_list[change_inventory]}] mot [{player.inventory[5]} +{player.item_bonus_list[5]} ST]")
                        player.inventory.pop(change_inventory)
                        player.item_bonus_list.pop(change_inventory)
                        break
                    if choice_inventory == "S" or choice_inventory == "s":
                        clear_screen()
                        delay_print(f"Du slängde [{player.inventory[5]} +{player.item_bonus_list[5]} STR]")
                        player.inventory.pop(5)
                        player.item_bonus_list.pop(5)
                        break
                    else:
                        continue
                    break
                else:
                    break
                            
                        
            break
        elif room_randomizer == 3:

            delay_print(f"Bakom dörren fanns {enemies.monster_types()} som attackerar dig")
            while True:
                if enemies.monster_strenght > player.strenght + sum(player.item_bonus_list):
                    player.player_hit()
                    delay_print(f"\nDu förlorade mot {enemies.monster_name}, -1 HP")
                    break
                else:
                    delay_print(f"\nDu besegrade {enemies.monster_name}, +1 LVL")
                    player.player_level_up()
                    break
            break
                
        else:
            delay_print("Du tog skada av en fälla, -1 HP")
            player.player_hit()
            break

def clear_screen():
    system("cls || clear")

def delay_print(meningar):
    for tecken in meningar:
        sys.stdout.write(tecken)
        sys.stdout.flush()
        time.sleep(0.1)
    return ""

player = Player(10)
item = Item()
enemies = Monster()
max_lifes = 10

character_name = str(input(delay_print("\nVad heter din karaktär?\nSkriv in för att starta -> ")))
clear_screen()

while True:
    print("\n----------------------------------\nDu är i ett rum med tre dörrar...\n\n    Se spelarinfo              [S]\n    Öppna inventory            [I]\n    Gå genom vänster dörr      [V]\n    Gå genom mitten dörren     [M]\n    Gå genom höger dörr        [H]\n----------------------------------")
    choice = input(delay_print("Gör ett val -> "))
    
    if choice == "s" or choice == "S":
        clear_screen()
        print(f"\n----------------\n{character_name}    LVL.{player.current_level}\n\nHP:  [{player.lifes}/{max_lifes}]\nSTR: [{player.strenght + sum(player.item_bonus_list)}]\n----------------")
        
    elif choice == "i" or choice == "I":
        clear_screen()
        print(f"\n--------------------------\nInventory\n\n{player.show_inventory()}\n--------------------------")

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
        print(f"\n{player.lifes}/{max_lifes} HP kvar, spel slut, du förlorade")
        break
