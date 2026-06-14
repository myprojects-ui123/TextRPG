from Choice_class import *
from saves import load_game


def prologue(main_hero):
    if main_hero.class_character == "Warrior":
        print("December 8:53, North Forest")
        time.sleep(3)
        print("""
              You, young Soldier, was born in village in northern part of the city Belmon 21 years ago. 
              In 18 years, after your parents died, you decided to join in army.
              You were learn fast and completed you education year.
              Over the next two years, you proved yourself as a disciplined and dependable soldier. 
              your actions on and off the battlefield earned you overwhelmingly positive recommendations 
              from officers of every rank

              Many believed that a promising military career awaited you in the years to come  
              """)
        time.sleep(3)
        print("""
                Now, while travelling to your new assignment,
                you find yourself escorting an important convoy through dangerous lands
              """)
        time.sleep(3)
        print("""
              You: So, you have been in the second company. 
              How did you end up working as a caravan guard?
                 
                 Mercenary: Better pay, less paperwork
                 
                 You: That's it?

                 Mercenary: Yeah
              
                 Merchant:Ha! Don't listen to him. He's just lazy to tell his true reasons
                 """)
        time.sleep(3)
        print("""
              Before the mercenary could answer, a guard screamed...
              
                Guard: Alarm, to arms!
              
                You: What happened?
                 
                Guard: Ogrs! We're under attack
              
                You leaved you're tent and saw dozens of Ogrs coming straight in your way

                In this time you got ready...
                """)


    if main_hero.class_character == "Mage":
        print("December 8:53, North Forest")
        time.sleep(2)
        print("You mage")

    if main_hero.class_character == "Assasin":
        print("December 8:53, North Forest")
        time.sleep(2)
        print("You Assasin")

    if main_hero.class_character == "Tank":
        print("December 8:53, North Forest")
        time.sleep(2)
        print("You Tank")


def start_story(main_hero):
        while True:
            try:
                skip = int(input("Do you want to skip Prologue:\n1.Skip\n2.No Skip\n"))
                if skip == 2:
                    prologue(main_hero)
                    break
                elif skip == 1:
                    break
                else:
                    print("Wrong\n")
            except ValueError:
                print("Try Again\n")    

class Game:
    def choice_hero(self):
        while True:
            fault = None
            try:
                self.start_game = int(input("1.Start Game\n2.Load Game\n3.Change the character(only in main menu)\n0.Exit\n"))
                if self.start_game == 0:
                    break
                if self.start_game == 1:
                    fault = int(input("Do you want to start a new game?\n1.Yes\n2.No\n"))
                    if fault == 1:
                        break
                if self.start_game == 2:
                    return load_game()
                
                if self.start_game == (3):
                    print("Developing\n")

                else:
                    print("Wrong\n")
            except ValueError:
                print("Try again:\n")
    
    

    

    def cicle(self):
       while True:
            try:
               self.start = int(input("1.Attack\n2.Heal\n3.Spells\n0.Main Menu\n"))
               break
            except ValueError:
                print("Try again:\n")