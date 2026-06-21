from fighting import *
from Story import Game
from saves import *
from menu import back_to_main_menu
from Spells import spells

fight = Fight()
game = Game()
heal = Heal()

def location_road(main_hero):
    if main_hero.location == "Road":
        a = int(input("1.City\n2.Forest\n3.Village\n4.Main_menu"))


def location_village(main_hero):
    if main_hero.location == "Village":
        a = int(input("1.Home\n2.Market\n3.Road\n4.Main_menu"))
        if a == 1:
            main_hero.location = "Home"
            return main_hero.location
        elif a == 2:
            main_hero.location = "Market"
            return main_hero.location
        elif a == 3:
            main_hero.locatiion = "Road"
            return main_hero.location
        elif a == 4:
            return False

def location_city(main_hero):
    a = int(input("1.Site\n2.Bar\n3.Road\n4.Main_menu"))
    if a == 1:
        main_hero.location = "Site"
        return main_hero.location

def location_North_Forest():
    return "North_Forest"

def location_brothel():
    return "Brothel"

def location_bar():
    return "Bar"

def location_s(main_hero):
    while True:
        if main_hero.location == "Village":
            if not location_village(main_hero):
                main_hero = back_to_main_menu(main_hero)
                break
        elif main_hero.location == "city":
            if not location_city(main_hero):
                main_hero = back_to_main_menu(main_hero)
                break
        elif main_hero.location == "Road":
            if not location_road(main_hero):
                main_hero = back_to_main_menu(main_hero)
                break
        elif main_hero.location == "bar":
            if not location_bar(main_hero):
                main_hero = back_to_main_menu(main_hero)
                break
        break
def location__first_fight(main_hero, small_ogr):
    fight = Fight()
    game = Game()
    heal = Heal()

    while True:
        game.cicle()
        if game.start == 1:        
            fight.damage_enemy(main_hero, small_ogr)
            if main_hero.zero_hp(small_ogr) == True:
                main_hero.lvl_up()
                main_hero.location = "city"
                main_hero.first_fight = True
                main_hero.chapter = 1
                save_game(main_hero)
                input("Press Enter to continue:")
                main_hero.victory_text()
                
                return main_hero
            fight.damage_enemy(small_ogr, main_hero)
            if main_hero.zero_hp(main_hero) == False:
                break
            print(f"{main_hero.name}\nHP:{main_hero.current_hp}\n")
            print(f"{small_ogr.name}\nHP:{small_ogr.current_hp}\n")
        elif game.start == 2:
            heal.heal_potion(main_hero)
        elif game.start == 3:
            print("Access denied\n")
        elif game.start == 0:
            return False
        



def location__current_fight(main_hero, enemy):
    fight = Fight()
    game = Game()
    heal = Heal()
    while True:
        if main_hero.zero_hp(enemy) == True:
            main_hero.lvl_up()
            save_game(main_hero)
            input("Press Enter to continue:")
            location_s(main_hero)
            break
        game.cicle()
        if game.start == 1:
            if main_hero.zero_hp(enemy) == True:
                main_hero.lvl_up()
                save_game(main_hero)
                input("Press Enter to continue:")
                break
            fight.stun(main_hero, enemy)

            if main_hero.zero_hp(main_hero) == True:
                break
            if main_hero.class_character == "Warrior":    
                fight.reduce_cooldown_fighter(main_hero)   
            fight.damage_enemy(main_hero, enemy)
            if main_hero.class_character == "Assasin":
                fight.reduce_poison(main_hero, enemy)
            if main_hero.class_character == "Mage":
                fight.reduce_dimension(main_hero, enemy)
            if main_hero.class_character == "Tank":
                fight.reduce_armor(main_hero)
        elif game.start == 2:

                heal.heal_potion(main_hero)

        elif game.start == 3:
            spells(main_hero, enemy)

        elif game.start == 0:
            main_hero = back_to_main_menu(main_hero)
            break
        print(f"{main_hero.name}\nHP:{main_hero.current_hp}\n")
        print(f"{enemy.name}\nHP:{enemy.current_hp}\n")