import random as rand,sys,time,pygame
from os import system
from pygame.constants import K_0, K_1, K_2, K_3, K_4, K_RETURN, K_b, K_g, K_h, K_i, K_m, K_o, K_s, K_u, K_v, K_w, K_x

pygame.init()

class Player():
    def __init__(self, lifes):
        self.lifes = lifes
        self.max_level = 10
        self.current_level = 0
        self.exp = 0
        self.strenght = 5
        self.inventory = []
        self.item_bonus = []

    def show_stats(self):
        self.stat_text = ""
        while True:
            self.stat_text = f"{text}    LVL.{player.current_level}\n\nHP:  [{player.lifes}/{max_lifes}]\nSTR: [{player.strenght + sum(player.item_bonus)}]                                                  -ENTER"
            return self.stat_text

    def player_hit(self):
        self.lifes -= 1
        
    def chest(self):
        self.inventory.append(str(rand.choice(item.item_names)))
        self.item_bonus.append(int(rand.choice(item.bonus_range)))
    
    def show_inventory(self):
        self.inventory_layout = ""
        lists = zip(player.inventory[0:5], player.item_bonus[0:5])
        for index, list_content in enumerate(lists):
            self.inventory_layout += f"\n{index}. [{list_content[0]} +{list_content[1]} STR]"
        return self.inventory_layout

    def player_level_up(self):
        self.current_level += 1

class Item():
    def __init__(self):
        self.item_names = ["Meme Blade", "Diamondsword", "Gravitygun", "Energisvärd", "Pizzaskärare", "BFG-9000", "Styrke-dryck", "Styrke-emblem", "Railgun", "Blades of kaos", "Matersword", "Köttbullsmacka", "Baguettespjut"]
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
        if room_randomizer == 1 or room_randomizer == 2:
            player.chest()
            if len(player.inventory) >= 6:
                input_rect = pygame.Rect(10,10,730,200)
                pygame.draw.rect(screen,color,input_rect,False ,10)
                pygame.draw.rect(screen,(95,158,160),input_rect,2 ,10)
                blitlines(screen, f"Du måste slänga [{player.inventory[5]} +{player.item_bonus[5]} STR] som du hittade [S] eller\nbyta ut det [B]\n\n{player.show_inventory()}", userfont, textcolor, 20, 850)
                pygame.display.update()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == K_b:
                                screen.blit(b1 , (0,0))
                                input_rect = pygame.Rect(10,10,730,180)
                                pygame.draw.rect(screen,color,input_rect,False ,10)
                                pygame.draw.rect(screen,(95,158,160),input_rect,2 ,10)
                                blitlines(screen, f"Välj vilket vapen du vill byta ut mot [{player.inventory[5]} +{player.item_bonus[5]} STR]\n\n{player.show_inventory()}", userfont, textcolor, 20, 850)
                                pygame.display.update()
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == K_0 or event.key == K_1 or event.key == K_2 or event.key == K_3 or event.key == K_4:
                                                print(player.inventory[5])
                                                inventory_index_to_pop = int(event.key)
                                                print("nummer har tryckts")
                                                screen.blit(b1 , (0,0))
                                                input_rect = pygame.Rect(10,10,730,160)
                                                pygame.draw.rect(screen,color,input_rect,False ,10)
                                                pygame.draw.rect(screen,(95,158,160),input_rect,2 ,10)
                                                blitlines(screen, f"\nDu bytte [{player.inventory[inventory_index_to_pop]} +{player.item_bonus[inventory_index_to_pop]} STR] mot [{player.inventory[5]} +{player.item_bonus[5]} STR]          -ENTER", userfont, textcolor, 20, 850)
                                                pygame.display.update()
                                                clear_screen()
                                                player.inventory.pop(inventory_index_to_pop)
                                                player.item_bonus.pop(inventory_index_to_pop)
                                                while True:
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.KEYDOWN:
                                                            if event.key == K_RETURN:
                                                                print("enter")
                                                                return              
                                        else:
                                            continue
         
                        if event.type == pygame.KEYDOWN:
                            if event.key == K_s:
                                print(f"\nDu slängde [{player.inventory[5]} +{player.item_bonus[5]} STR]\n")
                                clear_screen()
                                screen.blit(b1 , (0,0))
                                input_rect = pygame.Rect(10,10,730,40)
                                pygame.draw.rect(screen,color,input_rect,False ,10)
                                pygame.draw.rect(screen,(95,158,160),input_rect,2 ,10)
                                blitlines(screen, f"Du slängde [{player.inventory[5]} +{player.item_bonus[5]} STR]          -ENTER", userfont, textcolor, 20, 850)
                                pygame.display.update()
                                player.inventory.pop(5)
                                player.item_bonus.pop(5)
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == K_RETURN:
                                                print("enter")
                                                return

            else:
                print(f"\nBakom dörren fanns en kista med en skatt\n")
                while True:
                    screen.blit(b1 , (0,0))
                    input_rect = pygame.Rect(10,10,730,40)
                    pygame.draw.rect(screen,color,input_rect,False ,10)
                    pygame.draw.rect(screen,(95,158,160),input_rect,2 ,10)
                    blitlines(screen, f"Bakom dörren fanns en kista med en skatt                  -ENTER", userfont, textcolor, 20, 850)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == K_RETURN:
                                print("enter")
                                return
                        
                        


        elif room_randomizer == 3 or room_randomizer == 4:
            screen.blit(b1 , (0,0))
            input_rect = pygame.Rect(10,10,730,40)
            pygame.draw.rect(screen,color,input_rect,False ,10)
            pygame.draw.rect(screen,(95,158,160),input_rect,2 ,10)
            blitlines(screen, f"Bakom dörren fanns {monster.monster_types()} som attackerar dig", userfont, textcolor, 20, 850)
            pygame.display.update()
            while True:
                if monster.monster_strenght > player.strenght + sum(player.item_bonus):
                    player.player_hit()
                    screen.blit(b1 , (0,0))
                    input_rect = pygame.Rect(10,10,730,40)
                    pygame.draw.rect(screen,color,input_rect,False ,10)
                    pygame.draw.rect(screen,(95,158,160),input_rect,2 ,10)
                    blitlines(screen, f"Du förlorade mot {monster.monster_name}, -1 HP", userfont, textcolor, 20, 850)
                    blitlines_RETURN(screen, "-ENTER", userfont, textcolor, 20, 850)
                    pygame.display.update()
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == K_RETURN:
                                    print("enter")
                                    return
                else:
                    screen.blit(b1 , (0,0))
                    input_rect = pygame.Rect(10,10,730,40)
                    pygame.draw.rect(screen,color,input_rect,False ,10)
                    pygame.draw.rect(screen,(95,158,160),input_rect,2 ,10)
                    blitlines(screen, f"Du besegrade {monster.monster_name}, +1 LVL", userfont, textcolor, 20, 850)
                    blitlines_RETURN(screen, "-ENTER", userfont, textcolor, 20, 850)
                    pygame.display.update()
                    player.player_level_up()
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == K_RETURN:
                                    print("enter")
                                    return

        else:
            screen.blit(b1 , (0,0))
            input_rect = pygame.Rect(10,10,730,40)
            pygame.draw.rect(screen,color,input_rect,False ,10)
            pygame.draw.rect(screen,(95,158,160),input_rect,2 ,10)
            blitlines(screen, f"Du tog skada av en fälla, -1 HP                           -ENTER", userfont, textcolor, 20, 850)
            pygame.display.update()
            player.player_hit()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_RETURN:
                            print("enter")
                            return

def retun_input():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_RETURN:
                print("enter")
                return
                
def menu_text_appaering():
    screen.blit(b1 , (0,0))
    input_rect = pygame.Rect(10,10,730,160)
    pygame.draw.rect(screen,color,input_rect,False ,10)
    pygame.draw.rect(screen,(95,158,160),input_rect,2 ,10)
    blitlines(screen, "Du har kommit till ett rum med tre dörrar...\n\nSe spelarinfo                      [S]\nÖppna inventory                    [I]\nGå genom vänster dörr              [V]\nGå genom mitten dörren             [M]\nGå genom höger dörr                [H]", userfont, textcolor, 20, 850)
    pygame.display.update()

def clear_screen():
    system("cls || clear")

def show_inventory_text():
    print(player.show_inventory())
    screen.blit(b1 , (0,0))
    input_rect = pygame.Rect(10,10,730,160)
    pygame.draw.rect(screen,color,input_rect,False ,10)
    pygame.draw.rect(screen,(95,158,160),input_rect,2 ,10)
    blitlines(screen, f"Inventory\n{player.show_inventory()}", userfont, textcolor, 20, 850)
    blitlines(screen, "\n\n\n\n\n\n                                                          -ENTER", userfont, textcolor, 20, 850)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    print("enter")
                    return

def show_stat_text():
    print(player.show_stats())
    screen.blit(b1 , (0,0))
    input_rect = pygame.Rect(10,10,730,100)
    pygame.draw.rect(screen,color,input_rect,False ,10)
    pygame.draw.rect(screen,(95,158,160),input_rect,2 ,10)
    blitlines(screen, player.show_stats(), userfont, textcolor, 20, 850)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    print("enter")
                    return

def blitlines(surf, text, renderer, color, x, y):
    h = renderer.get_height()
    lines = text.split('\n')
    for i, ll in enumerate(lines):
        txt_surface = renderer.render(ll, True, color)
        surf.blit(txt_surface, (input_rect.x +15, input_rect.y +10 +(i*h)))
        
def blitlines_RETURN(surf, text, renderer, color, x, y):
    h = renderer.get_height()
    lines = text.split('\n')
    for i, ll in enumerate(lines):
        txt_surface = renderer.render(ll, True, color)
        surf.blit(txt_surface, (input_rect.x +655, input_rect.y +10 +(i*h)))

player = Player(10)
item = Item()
monster = Monster()
max_lifes = 10

#pygame.init()
background_colour = (192, 192, 192)
textcolor = (255, 255, 255)
screen = pygame.display.set_mode((750, 545))
userfont = pygame.font.SysFont("consolas", 20) #arialblack #consolas #cambria
input_rect = pygame.Rect(10,810,360,260)
color = (0,128,128)

screen.fill(background_colour)
b1 = pygame.image.load(r"C:\Users\Elev\Pictures\Saved Pictures\pixldungeon.png")
screen.blit(b1 , (0,0))

pygame.display.flip()

clock = pygame.time.Clock()
input_box = pygame.Rect(320, 35, 140, 750)
active = True
text = ""
done = False

while True:
    for event in pygame.event.get():
        screen.fill((30, 30, 30))
        input_rect = pygame.Rect(10,10,730,60)
        pygame.draw.rect(screen,color,input_rect,False ,10)
        pygame.draw.rect(screen,(95,158,160),input_rect,2 ,10)
        blitlines(screen, "Vad heter din karaktär?\nSkriv in för att starta ->                                -ENTER", userfont, textcolor, 20, 850)
        pygame.display.update()
        txt_surface = userfont.render(text, True, textcolor)
        # Resize the box if the text is too long.
        width = max(730, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.

        pygame.display.flip()
        clock.tick(100)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    menu_text_appaering()
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()

                            if event.type == pygame.KEYDOWN:
                                if event.key == K_o:
                                    print("hello")
                                    menu_text_appaering()

                                if event.key == K_s:
                                    show_stat_text()
                                    menu_text_appaering()

                                if event.key == K_i:
                                    print("enter har tryckts")
                                    show_inventory_text()
                                    menu_text_appaering()

                                if event.key == K_h:
                                    print("enter har tryckts")
                                    rooms()
                                    menu_text_appaering()

                                if event.key == K_m:
                                    print("enter har tryckts")
                                    rooms()
                                    menu_text_appaering()

                                if event.key == K_v:
                                    print("enter har tryckts")
                                    rooms()
                                    menu_text_appaering()
                                            

                                if player.current_level == player.max_level:
                                    print(f"\nGrattis, du har VUNNIT spelet\n\n")
                                    break

                                if player.lifes == 0:
                                    print(f"\n{player.lifes}/{max_lifes} HP kvar, spel slut, du förlorade\n\n")
                                    pygame.quit

                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
