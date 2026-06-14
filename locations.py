from fighting import *
from Story import Game
from saves import *
from menu import back_to_main_menu

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
        return 

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
            fight.damage_enemy(main_hero, small_ogr)
            if main_hero.zero_hp_start(small_ogr) == True:
                main_hero.location = "city"
                save_game(main_hero)
                input("Press Enter to continue:")
                main_hero.victory_text()
                break
            fight.damage_enemy(small_ogr, main_hero)
            if main_hero.zero_hp_start(main_hero) == True:
                break
            
            elif game.start == 2:
                # if main_hero.class_character == "Mage":

                Heal.heal_potion(heal, main_hero)
            elif game.start == 0:
                break
            print(f"{main_hero.name}\nHP:{main_hero.current_hp}\n")
            print(f"{small_ogr.name}\nHP:{small_ogr.current_hp}\n")

def location__current_fight(main_hero, enemy):
    fight = Fight()
    game = Game()
    heal = Heal()
    while True:
        game.cicle()
        if game.start == 1:        
            fight.damage_enemy(main_hero, enemy)
            if main_hero.zero_hp_start(enemy) == True:
                main_hero.location = "city"
                save_game(main_hero)
                input("Press Enter to continue:")
                main_hero.victory_text()
                break
            fight.stun(main_hero, enemy)
            if main_hero.zero_hp_start(main_hero) == True:
                break
            
        elif game.start == 2:
                # if main_hero.class_character == "Mage":

                heal.heal_potion(main_hero)
            
        elif game.start == 3 and main_hero.lvl < 2:
            print("Access denied\n")

        elif game.start == 3 and main_hero.lvl >= 2 and main_hero.lvl < 5 and main_hero.class_character == "Warrior":
            kicked = int(input("1.Kick\n0.Back"))
            if kicked == 1:
                fight.reduce_cooldown_fighter(main_hero)
                fight.fighter_kick(main_hero, enemy)
            elif kicked == 2:
                print("Back to game\n")
            

        elif game.start == 0:
            main_hero = back_to_main_menu(main_hero)
            break
        print(f"{main_hero.name}\nHP:{main_hero.current_hp}\n")
        print(f"{enemy.name}\nHP:{enemy.current_hp}\n")