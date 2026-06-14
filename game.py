from saves import save_game
from enemies import Enemy
from Classes import choose_name, choice_start
from fighting import *
from Story import *
from locations import location_s, location__first_fight
import os

main_hero = None
original_name = None

small_ogr = Enemy("Ogr", 
                  7, 
                  5, 
                  0, 
                  5,
                  3, 
                  5,
                  0,
                  "Start",
                  "Ogr",
                  "Warrior")
game = Game()
fight = Fight()
heal = Heal()
while True:
    game.choice_hero()
    
    if game.start_game == 2:
        if os.path.exists("save_1.json"):
            main_hero = load_game()
        else:
            print("No save")

            
    if game.start_game == 1:
        original_name = choose_name(original_name)
        main_hero = choice_start(original_name, main_hero)
        while True:
            start_story(main_hero)
            location__first_fight(main_hero, small_ogr)
            break
    
    if game.start_game == 0:
        break

    while True:     
        print(main_hero.location)
        location_s(main_hero) 
        break
    
    
