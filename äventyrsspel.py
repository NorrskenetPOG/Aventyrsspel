import random as rand,sys,time
from os import system

class Player():
    def __init__(self, lifes):
        """
        Funktionen initsierar klassen Player's atributer och startvärden
        """
        self.lifes = lifes
        self.max_level = 10
        self.current_level = 0
        self.max_xp = 5
        self.xp = 0
        self.strenght = 5
        self.inventory = []
        self.item_bonus = []

    def player_hit(self):
        """
        Funktion som minskar livet på avataren när hen blir träffad.
        """
        self.lifes -= 0.5
    
    def show_inventory(self):
        """
        Denna funktion tar två listor och med hjälp av funtionen Zip läggs dessa ihop. T.ex. [a, b, c] och [1, 2, 3] blir [1a, 2b, 3c].
        Sedan printer den listans index var för sig för att ge ett snyggt textbaserat gränssnitt.
        """
        self.inventory_layout = ""
        lists = zip(player.inventory[0:5], player.item_bonus[0:5])
        for index, list_content in enumerate(lists):
            self.inventory_layout += f"\n{index+1}. [{list_content[0]} +{list_content[1]} STR]" 
        return self.inventory_layout

    def player_level_up(self):
        """
        Funktion lägger till xp till karaktären och när karaktären når max xp för en nivå ökar nivån och gränsen för att ranka upp (xp_max).
        """
        self.xp += 5
        
        if self.xp >= player.max_xp:
            print(f"Du levlade upp, LVL.{player.current_level + 1}")
            self.current_level += 1
            self.xp = 0
            self.max_xp += 2
            return self.current_level and self.xp and self.max_xp

class Item():
    """
    Funktionen initsierar klassen Item's atributer och startvärden.
    """
    def __init__(self):
        self.item_names = ["Meme Blade", "Diamondsword", "Gravitygun", "Energisvärd", "Pizzaskärare", "BFG-9000", "Styrke-dryck", "Styrke-emblem", "Railgun", "Blades of kaos", "Matersword", "Köttbullsmacka", "Baguettespjut", "PP-svärd"]
        self.bonus_range = range(1, 6)

    def chest(self):
        """
        Funktion som lägger in ett vanligt item plus ett bonus item när avataren hittar en kista.
        """
        player.inventory.append(str(rand.choice(item.item_names)))
        player.item_bonus.append(int(rand.choice(item.bonus_range)))

class Monster():
    def __init__(self):
        """
        Funktionen initsierar klassen Monster's atributer och startvärden.
        """
        self.strenght_range = range(0, 23)

    def monster_types(self):
        """
        Denna funktion ska slumpmässigt välja ett monster. 
        Den gör det genom att först välja en också slumpmässad styrka.
        Alla monster är rangordnade efter styrka och baserat på den slumpade styrkan väljer den ett monster.
        """
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
    """
    Funktionen ska slumpmässigt välja en dörr, fast använder oss av weights för att få sannolikheter.
    Avataren kan antingen hitta en kista, ett monster eller en fälla.
    Chest() - öppnar chest funktionen och ger ett item. 
    Ifall avataren har fullt inventory så behövs det slänga eller bytas ut.
    """
    room_list = [1, 2, 3]
    room_randomizer = rand.choices(room_list, weights=(2, 2, 1), k=1)[0]

    while True:
        clear_screen()
        if room_randomizer == 1:
            print("\033[1;33;40m")
            delay_print(f"Bakom dörren fanns en kista med en skatt\n")
            while True:
                item.chest()
                if len(player.inventory) >= 6:
                    print("\033[1;37;40m")
                    print(f"\nDitt inventory är fullt\n\n--------------------------\n{player.show_inventory()}")
                    choice_inventory = input(f"\nVälj för [{player.inventory[5]} +{player.item_bonus[5]} STR] att [S] slänga eller [B] byta -> ").lower()
                    if choice_inventory == "b":
                        while True:
                            clear_screen()
                            print(f"Välj vilket vapen du vill byta ut mot [{player.inventory[5]} +{player.item_bonus[5]} STR]\n")
                            print(f"--------------------------\n{player.show_inventory()}")
                            change_inventory = str(input(delay_print(f"\n[1 - 5] -> ")))
                            if change_inventory in ['1','2','3','4','5']:
                                clear_screen()
                                inventory_index_to_pop = int(change_inventory) -1
                                print(f"Du bytte [{player.inventory[inventory_index_to_pop]} +{player.item_bonus[inventory_index_to_pop]} STR] mot [{player.inventory[5]} +{player.item_bonus[5]} STR]")
                                player.inventory.pop(inventory_index_to_pop)
                                player.item_bonus.pop(inventory_index_to_pop)
                                break
                            else:
                                clear_screen()
                                continue
                        break   
                    if choice_inventory == "s":
                        clear_screen()
                        delay_print(f"Du slängde [{player.inventory[5]} +{player.item_bonus[5]} STR]\n")
                        player.inventory.pop(5)
                        player.item_bonus.pop(5)
                        break
                    else:
                        clear_screen()
                        continue
                else:
                    break                  
            break

        elif room_randomizer == 2:
            delay_print(f"\nBakom dörren fanns {monster.monster_types()} som attackerar dig")
            while True:
                if monster.monster_strenght > player.strenght + sum(player.item_bonus):
                    print("\033[1;91;40m")
                    player.player_hit()
                    delay_print(f"Du förlorade mot {monster.monster_name}, -0.5 HP\n")
                    break
                else:
                    print("\033[1;92;40m")
                    delay_print(f"Du besegrade {monster.monster_name}, +5 XP\n")
                    player.player_level_up()
                    break
            break

        else:
            delay_print(f"\nBakom dörren fanns fälla")
            print("\033[1;91;40m")
            delay_print("Du tog skada av en fälla, -0.5 HP\n")
            player.player_hit()
            break

def clear_screen():
    """
    Winows cls kommando för att rensa skärmen.
    """
    system("cls || clear")

def delay_print(meningar):
    """
    Fördröjer printar så att det som inte printas ut, utan skrivs ut.
    """
    for tecken in meningar:
        sys.stdout.write(tecken)
        sys.stdout.flush()
        time.sleep(0.005)
    return ""

player = Player(10)
item = Item()
monster = Monster()
max_lifes = 10

print("\033[1;37;40m")
"""
ANSI escape-kod som sätter texten till en färg;
\033[ = Escape-kod, alltid samma
0 = Stil, 0 för normalt
36 = Text färg, 36 för mörk grått
40m = Bakgrundsfärg, 40 för svart

Förekomer flera gånger i koden för att ändra färger
"""

clear_screen()
character_name = str(input(delay_print("Vad heter din karaktär?\nSkriv in för att starta -> ")))
clear_screen()

while True:
    """
    Här är start menyn. Den loopar så länge avataren inte uppnår max level eller har noll liv. 
    Här kan spelaren välja ifall hen vill se information såsom namn, level, liv och styrka.
    Hen kan även öppna sitt inventory härifrån, och välja på tre dörrar som alla gör samma sak, öppnar rooms funtkionen.
    """
    print("\033[1;37;40m")
    print("\n--------------------------------------------\nDu har kommit till ett rum med tre dörrar...\n\n    Se spelarinfo                    [S]\n    Öppna inventory                  [I]\n    Gå genom vänster dörr            [V]\n    Gå genom mitten dörren           [M]\n    Gå genom höger dörr              [H]\n--------------------------------------------")
    choice = input(delay_print("Gör ett val -> ")).lower()
    
    if choice == "s":
        clear_screen()
        print(f"----------------------------\n{character_name}    LVL.{player.current_level} ({player.xp}/{player.max_xp} XP)\n\nHP:  [{player.lifes}/{max_lifes}]\nSTR: [{player.strenght + sum(player.item_bonus)}]\n----------------------------")
        
    elif choice == "i":
        clear_screen()
        print(f"--------------------------\nInventory\n{player.show_inventory()}\n--------------------------")

    elif choice == "v":
        rooms()

    elif choice == "m":
        rooms()
        
    elif choice == "h":
        rooms()
    
    else:
        clear_screen()
        continue

    if player.current_level == player.max_level:
        delay_print(f"\nGrattis, du har VUNNIT spelet\n\n")
        break

    if player.lifes == 0:
        print(f"\n{player.lifes: .0f}/{max_lifes} HP kvar, spel slut, du förlorade\n\n")
        break
