from fighting import *
from Story import Game
from saves import *
from menu import Menu
from Spells import spells
from Enemy_list import *
from Choice_class import *
from Side_Quests import *
from Inventory import count_item

fight = Fight()
game = Game()
heal = Heal()
menu = Menu()

def location_road(main_hero):
    if main_hero.location == "Road":
        print("You're in the Road\n")
        while True:
            try:
                a = int(input("1.City\n2.North Forest\n3.Village\n4.Goal\n5.Equioment\n6.Main_menu\n"))
                break
            except ValueError:
                print("Incorrect choice\n")
        if a == 1:
            main_hero.location = "city"
        elif a == 2:
            main_hero.location = "North Forest"
        elif a == 3:
            main_hero.location = "Village"

        elif a == 4:
            print(main_hero.story)
            print(main_hero.side_quest)
        elif a == 5:
            count_item(main_hero)
        elif a == 6:
            return False
                
        return main_hero.location

def location_village(main_hero):
    if main_hero.location == "Village":
        print("You're in the Village\n")
        while True:
            try:
                a = int(input("1.Home\n2.Market\n3.Road\n4.Goal\n5.Equipment\n6.Main_menu\n"))
                break
            except ValueError:
                print("Incorrect choice\n")
        if a == 1:
            main_hero.location = "Home"
        elif a == 2:
            main_hero.location = "Market"
        elif a == 3:
            main_hero.locatiion = "Road"
            
        elif a == 4:
            print(main_hero.story)
            print(main_hero.side_quest)
        elif a == 5:
            count_item(main_hero)
        elif a == 6:
            return False
        
        return main_hero.location
    
def location_city(main_hero):
    if main_hero.location == "city":
        print("You're in the city\n")
        while True:
            try:
                a = int(input("1.Site\n2.Bar\n3.Fortrest\n4.Road\n5.Goal\n6.Equipment\n7.Main_menu\n"))
                break
            except ValueError:
                print("Incorrect Choice\n")
        if a == 1:
            main_hero.location = "Site"
        elif a == 2:
            main_hero.location = "Bar"
        elif a == 3:
            main_hero.location = "Fortrest"
        elif a == 4:
            if main_hero.chapter == 1.0:
                print("Access Denied\n")
            else:
                main_hero.location = "Road"
        elif a == 5:
            print(main_hero.story)
            print(main_hero.side_quest)
        elif a == 6:
            count_item(main_hero)
        elif a == 7:
            return False    
        return main_hero.location
            

def location_Fortress(main_hero):
    if main_hero.location == "Fortrest":
        if main_hero.chapter == 1.0:
            main_hero.location = "city"
        return main_hero.location

def location_North_Forest(main_hero):
    if main_hero.location == "North Forest":
        while True:
            try:
                a = int(input("1.Hunt\n2.Pick Berries\n3.Road\n4.Goal\n5.Equipment\n6.Main_menu\n"))
                break
            except ValueError:
                print("Incorrect choice\n")
        if a == 1:
            hunt = random.randint(1, 100)
            if hunt <= 30:
                print("You attacked Ogr!\n")
                enemy = Ogr
                if not location__current_fight(main_hero, enemy):
                    return "dead"
            elif hunt >= 31 and hunt <= 35:
                print("You found gold!\n")
                main_hero.gold += 5
        elif a == 2:
            main_hero.location = "Bar"
        elif a == 3:
            main_hero.location = "Road"
            return main_hero.location
        elif a == 4:
            print(main_hero.story)
            print(main_hero.side_quest)
        elif a == 5:
            count_item(main_hero)
        elif a == 6:
            return False
            

def location_site(main_hero):
    if main_hero.location == "Site":
        side_1_1_War(main_hero)
        if main_hero.chapter == 1.0:
            while True:
                try:
                    a = int(input("1.City\n2.Goal\n3.Equipment\n4.Main_menu\n"))
                    break
                except ValueError:
                    print("Try again")
            if a == 1:
                main_hero.location = "city"
            elif a == 2:
                print(main_hero.story)
                print(main_hero.side_quest)
            elif a == 3:
                count_item(main_hero)
            elif a == 4:
                return False
            return main_hero.location
                

def location_brothel():
    return "Brothel"

def location_bar(main_hero):
    if main_hero.location == "Bar":
        side_1_0_War(main_hero)
        if main_hero.chapter == 1.0:
            while True:
                while True:
                    try:
                        a = int(input("1.City\n2.Goal\n3.Main_menu\n"))
                        break
                    except ValueError:
                        print("Incorrect Choice\n")
                if a == 1:
                    main_hero.location = "city"
                elif a == 2:
                    print(main_hero.story)
                    print(main_hero.side_quest)
                elif a == 3:
                    return False
                
                return main_hero.location
        else:
            try:
                a = int(input("1.Drink\n2.Food\n3.City\n4.Goal\n5.Main_menu\n"))
            except ValueError:
                print("Try again\n")
            if a == 3:
                main_hero.location == "city"
                return main_hero.location
            
            return main_hero.location

def location_s(main_hero):
    while True:
        if main_hero.location == "Village":
            if not location_village(main_hero):
                if menu.back_to_main_menu(main_hero):
                    return False
        if main_hero.location == "Fortrest":
            if not location_Fortress(main_hero):
                if menu.back_to_main_menu(main_hero):
                    return False
        elif main_hero.location == "Site":
            if not location_site(main_hero):
                if menu.back_to_main_menu(main_hero):
                    return False
        elif main_hero.location == "city":
            if not location_city(main_hero):
                if menu.back_to_main_menu(main_hero):
                    return False
        elif main_hero.location == "Road":
            if not location_road(main_hero):
                if menu.back_to_main_menu(main_hero):
                    return False
        elif main_hero.location == "Bar":
            if not location_bar(main_hero):
                if menu.back_to_main_menu(main_hero):
                    return False
        elif main_hero.location == "North Forest":
            check_point = location_North_Forest(main_hero)
            if not check_point:
                if menu.back_to_main_menu(main_hero):
                    return False
            if check_point == "dead":
                return False
            
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
                main_hero.chapter = 1.0
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
            break
        game.cicle()
        if game.start == 1:
            fight.damage_enemy(main_hero, enemy)
            if main_hero.zero_hp(enemy) == True:
                main_hero.lvl_up()
                save_game(main_hero)
                input("Press Enter to continue:")
                return True
            
            fight.stun(main_hero, enemy)
            if main_hero.zero_hp(main_hero) == True:
                return False
            if main_hero.class_character == "Warrior":    
                fight.reduce_cooldown_fighter(main_hero, enemy)  
                fight.heal_stamina(main_hero) 
            if main_hero.class_character == "Assasin":
                fight.reduce_poison(main_hero, enemy)
                fight.heal_stamina(main_hero)
            if main_hero.class_character == "Mage":
                fight.reduce_dimension(main_hero, enemy)
                fight.heal_mana(main_hero)
            if main_hero.class_character == "Tank":
                fight.reduce_armor(main_hero)
                fight.heal_stamina(main_hero)
        elif game.start == 2:

                heal.heal_potion(main_hero)

        elif game.start == 3:
            spells(main_hero, enemy)

        elif game.start == 0:
            break

        print(f"{main_hero.name}\nHP:{main_hero.current_hp}\n")
        print(f"{enemy.name}\nHP:{enemy.current_hp}\n")