from fighting import *
from Story import Game
from saves import *
from menu import Menu
from Spells import spells
from Enemy_list import *
from Choice_class import *

fight = Fight()
game = Game()
heal = Heal()
menu = Menu()

def location_road(main_hero):
    if main_hero.location == "Road":
        a = int(input("1.City\n2.North Forest\n3.Village\n4.Goal\n5.Main_menu\n"))
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
            return False
        else:
            print("Incorrect choice\n")
        return main_hero.location

def location_village(main_hero):
    if main_hero.location == "Village":
        a = int(input("1.Home\n2.Market\n3.Road\n4.Goal\n5.Main_menu\n"))
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
            return False
        return main_hero.location
    
def location_city(main_hero):
    if main_hero.location == "city":
        a = int(input("1.Site\n2.Bar\n3.Fortrest\n4.Road\n5.Goal\n6.Main_menu\n"))
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
            return False
        else:
            print("Try again\n")
        return main_hero.location

def location_Fortress(main_hero):
    if main_hero.location == "Fortrest":
        if main_hero.chapter == 1.0:
            print("")

def location_North_Forest(main_hero):
    if main_hero.location == "North Forest":
        while True:
            a = int(input("1.Hunt\n2.Pick Berries\n3.Road\n4.Goal\n5.Main_menu\n"))
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
                return False
            else:
                print("Try again\n")
            

def location_site(main_hero):
    if main_hero.location == "Site":
        if main_hero.class_character == "Warrior":
            if main_hero.side_quest == "Meet Nathan on the Site" and main_hero.tournament_site == None:
                print("You arrived to the Site and saw many soldiers around area. Then you saw Nathan and came straight to him\n")
                time.sleep(2)
                print("Nathan: Oh, you here, I knew you would come\n")
                time.sleep(2)
                print("You: Of Course I would come\n")
                time.sleep(2)
                print("Nathan:There are 3 stages. Quarter-Final. Semi-Final. Final.\nYou need to win 3 opponents to win Tournament\n")
                time.sleep(2)
                print("You:Okay, got it\n")
                time.sleep(2)
                print("Nathan: Added you to the list of participants, show them, how to fight")
                time.sleep(2)
                print("You: I will\n")
                time.sleep(2)
                print(f"Judge: First fight of Quarter Finals: {main_hero.name} against Blacksmith\n")
                input("Press Enter to start fight: ")
                enemy = Soldier_chapter_0
                if not location__current_fight(main_hero, enemy):
                    main_hero.tournament_site = "Lose_Quarter"
                    main_hero.side_quest == None
                    print("BlackSmith: You fought well, son, you're just lack of an experience.\nMaybe next year\n")
                    main_hero.exp += 100
                    main_hero.update_stats()
                    return
                main_hero.update_stats()
                print(f"Judge: And the Winner is {main_hero.name}\n")
                time.sleep(2)
                print(f"Judge: Next fight: {main_hero.name} against The last year Champion\n")
                time.sleep(2)
                input("Press Enter to start fight: ")
                enemy = Soldier_chapter_0_2
                if not location__current_fight(main_hero, enemy):
                    main_hero.tournament_site = "Lose_Semi"
                    main_hero.side_quest == None
                    print("Judge: And the last year Champion goes to his second award\n")
                    time.sleep(2)
                    print("Champion: You did well, man. Finaaly I was fighting seriosly for a long time.\nHope to see in the next year\n")
                    time.sleep(2)
                    print("You received 20 gold and 125 Exp\n")
                    main_hero.gold += 20
                    main_hero.exp += 125
                    return
                main_hero.update_stats()
                print(f"Judge: And Final: {main_hero.name} against Nathan")
                time.sleep(3)
                print("Nathan: Didn't expect it will be me in the Final?\nLet's finally found out, who is stronger\n")
                time.sleep(3)
                input("Press Enter to start fight: ")
                enemy = Champion_chapter
                if not location__current_fight(main_hero, enemy):
                    main_hero.tournament_site = "Lose_Final"
                    main_hero.side_quest == None
                    print("Judge: Nathan became the new Champion of the Tournament!!!\n")
                    time.sleep(2)
                    print("Nathan:That was so close, mate, you almost did it. I hope we meet again soon, but now I need to go with my commander. See ya\n")
                    time.sleep(2)
                    print("You received 30 gold and 150 Exp\n")
                    main_hero.gold += 30
                    main_hero.exp += 150
                    main_hero.update_stats()
                print("You became the champion!!!\n")
                time.sleep(3)
                main_hero.tournament_site = "Lose_Final"
                main_hero.side_quest == None
                print("You get 50 gold and 250 Exp!\n")
                main_hero.gold += 50
                main_hero.exp += 250

                main_hero.update_stats()
                return
            if main_hero.chapter == 1.0:
                while True:
                    try:
                        a = int(input("1.City\n2.Goal\n3.Main_menu\n"))
                        if a == 1:
                            main_hero.location = "city"
                        if a == 2:
                            print(main_hero.story)
                            print(main_hero.side_quest)
                        if a == 3:
                            return False
                    except ValueError:
                        print("Try again")
                    return main_hero.location
                

def location_brothel():
    return "Brothel"

def location_bar(main_hero):
    if main_hero.location == "Bar":
        if main_hero.chapter == 1.0 and main_hero.class_character == "Warrior" and main_hero.side_quest == None:
            print("Well, well , well, look, who is here...\n")
            time.sleep(2)
            print("You turned around and saw your friend, Nathan\nYou:Nathan, are you still alive?:)\n")
            time.sleep(2)
            print("Nathan: Of course I am. I'm not as weak as you, ha ha!\n")
            time.sleep(2)
            print("You: Glad to see you. What are you doing here?")
            time.sleep(2)
            print("Nathan: The Championship of the Kingdom starting soon in this city.\nAs the one of the strongest soldiers, I must be here")
            time.sleep(2)
            print("You: Wait, in this city?!\nToday?!")
            time.sleep(2)
            try:
                a = int(input(("Nathan: Yeah, if wanna participate, I can put in a good word for you, so what do you think?\n1.Yeah\n2.No, thanks, mate\n")))
                if a == 1:
                    print("You: Yeah, sure")
                    time.sleep(2)
                    print("Nathan: Good, go to the site later, see ya\n")
                    time.sleep(2)
                    main_hero.side_quest = "Meet Nathan on the Site"
                if a == 2:
                    print("You: No, thanks\n")
                    time.sleep(2)
                    print("Nathat: Okay, but if you change your mind, meet me in the Site\n")
                    main_hero.side_quest = "Meet Nathan on the Site"
            except ValueError:
                print("Try again\n")
        if main_hero.chapter == 1.0:
            while True:
                try:
                    a = int(input("1.City\n2.Goal\n3.Main_menu\n"))
                    if a == 1:
                        main_hero.location = "city"
                    if a == 2:
                        print(main_hero.story)
                        print(main_hero.side_quest)
                    if a == 3:
                        return False
                except ValueError:
                    print("Try again")
                return main_hero.location
        try:
            a = int(input("1.Drink\n2.Food\n3.City\n4.Goal\n5.Main_menu\n"))
            if a == 3:
                main_hero.location == "city"
                return main_hero.location
        except ValueError:
            print("Try again\n")
        return main_hero.location

def location_s(main_hero):
    while True:
        if main_hero.location == "Village":
            if not location_village(main_hero):
                if menu.back_to_main_menu(main_hero):
                    return False
        elif location_site(main_hero):
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
            break

        print(f"{main_hero.name}\nHP:{main_hero.current_hp}\n")
        print(f"{enemy.name}\nHP:{enemy.current_hp}\n")