from Enemy_list import *
from Inventory import *
import time


def side_1_0_War(main_hero):
     if main_hero.chapter == 1.0 and main_hero.class_character == "Warrior" and main_hero.side_quest == None and main_hero.tournament_site == None:
            print("Stranger: Well, well , well, look, who is here...\n")
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
                a = int(input(("Nathan: Yeah, if you wanna participate, I can put in a good word for you, so what do you think?\n1.Yeah\n2.No, thanks, mate\n")))
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

def side_1_1_War(main_hero):
     from locations import location__current_fight
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
                        main_hero.side_quest = None
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
                        main_hero.side_quest = None
                        print("Judge: And the last year Champion goes to his second award\n")
                        time.sleep(2)
                        print("Champion: You did well, man. Finaaly I was fighting seriosly for a long time.\nHope to see in the next year\n")
                        time.sleep(2)
                        print("You received 20 gold and 125 Exp\n")
                        main_hero.gold += 20
                        main_hero.exp += 125
                        return
                    main_hero.update_stats()
                    print(f"Judge: And Final: {main_hero.name} against Nathan\n")
                    time.sleep(3)
                    print("Nathan: Didn't expect it will be me in the Final?\nLet's finally found out, who is stronger\n")
                    time.sleep(3)
                    input("Press Enter to start fight: ")
                    enemy = Champion_chapter
                    if not location__current_fight(main_hero, enemy):
                        main_hero.tournament_site = "Lose_Final"
                        main_hero.side_quest = None
                        print("Judge: Nathan became the new Champion of the Tournament!!!\n")
                        time.sleep(2)
                        print("Nathan:That was so close, mate, you almost did it. I hope we meet again soon, but now I need to go with my commander. See ya\n")
                        time.sleep(2)
                        print("You received 30 gold and 150 Exp\n")
                        main_hero.gold += 30
                        main_hero.exp += 150
                        main_hero.update_stats()
                    main_hero.update_stats()
                    print("You became the champion!!!\n")
                    time.sleep(3)
                    main_hero.tournament_site = "Winner"
                    main_hero.side_quest = None 
                    main_hero.exp += 250
                    main_hero.weapon = steel_blade
                    print(f"You get {main_hero.weapon.name} and 250 Exp!\n")
                    return True
     
def side_1_1_Mage(main_hero):
    print("")

def side_1_1_Assasin(main_hero):
     print("")

def side_1_1_Tank(main_hero):
     print("")

def main_plot_1_1(main_hero):
     print("")