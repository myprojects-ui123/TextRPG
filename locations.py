from fighting import *
from Story import Game
from saves import *
from enemies import Enemy

fight = Fight()
game = Game()
heal = Heal()

def location_village(main_hero):
    if main_hero.class_character == "village":
        a = int(input("1.Home\n2.Market\n3.Road\n4.Main_menu"))
        if a == 1:
            return "Home"

def location_city(main_hero):
    if main_hero.location == "city":
        print("You're going to the city")
        return 1

def location_North_Forest():
    return "North_Forest"

def location_brothel():
    return "Brothel"

def location_bar():
    return "Bar"

def location_s(main_hero):
    if main_hero.location == "village":
        location_village(main_hero)
    elif main_hero.location == "city":
        location_city(main_hero)

def location__first_fight(main_hero, small_ogr):
    fight = Fight()
    game = Game()
    heal = Heal()

    while True:
        game.cicle()
        if game.start == 1:        
            fight.attack_enemy(main_hero, small_ogr)
            if main_hero.zero_hp_start(small_ogr) == True:
                main_hero.location = "city"
                save_game(main_hero)
                main_hero.victory_text()
                break
            fight.attack_enemy(small_ogr, main_hero)
            if main_hero.zero_hp_start(main_hero) == True:
                break
            
            elif game.start == 2:
                # if main_hero.class_character == "Mage":

                Heal.heal_potion(heal, main_hero)
            elif game.start == 0:
                break
                # try:
                #     save_point = int(input("Do you wanna save the game?\n1.Yes\n2.No\n3.Cancel\n"))
                #     if save_point == 1:
                #         save_game(main_hero)
                #         break 
                #     elif save_point == 2:
                #         break
                #     elif save_point == 3:
                #         continue
                #     else:
            print(f"{main_hero.name}\nHP:{main_hero.current_hp}\n")
            print(f"{small_ogr.name}\nHP:{small_ogr.current_hp}\n")
