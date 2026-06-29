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
        print("""You was born in capital of the Kingdom - Marol. You found magical talent
              when you were 4 yrs old. You were sent to the Academy to learn control you're power.
              You were learning fast and became the best student in the entire Academy. When you turned 21,
              you and you're teacher was sent to neighboring city to give a lecture in their Academy.That was
              the day you're destiny moved on...\n""")
        time.sleep(8)
        print("Teacher: You need some rest. There's enough training for today\n")
        time.sleep(5)
        print("You: Okay, teacher, just give me a second\n")
        time.sleep(5)
        print("Teacher: Everytime I give you 1 second turns into several hours\n")
        time.sleep(5)
        print("I'm worring about you\n")
        time.sleep(5)
        print("You: Don't worry, teacher. I promise, I won't be long\n")
        time.sleep(5)
        print("Teacher: Good, because I...\n")
        time.sleep(5)
        print("Guard: Alarm!!! Ogres attacking\n")
        time.sleep(5)
        print("You saw dozens of Ogrs coming straight in your way\n")
        time.sleep(5)
        print("You need to protect your friends!!!\n")
        time.sleep(3)

    if main_hero.class_character == "Assasin":
        print("December 8:53, North Forest")
        time.sleep(2)
        print("""You was born in the slums of the capital of kingdom - Marol. You're family was very poor
              and had to steal to survive. People around considered you as a trash. You were caught in 21 yrs and was sent
              prison in neighboring city. You thought your life ends here...""")
        time.sleep(8)
        print("Security 1: And then this trash was trying to escape, but we caught pretty quick\n")
        time.sleep(5)
        print("Security 2: I hope he will be executed\n")
        time.sleep(5)
        print("Security 1: Yeah, me to...\n")
        time.sleep(5)
        print("Silver Arrow pierced his throat. Security 2 didn't have time to turned around he was stabbed in he back by Ogr")
        time.sleep(5)
        print("You had the chance to escape, but you saw Ogr was planning to attack Woman with baby. You conscience said you to help them...\n")
        

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
    
    def cicle(self):
       while True:
            try:
               self.start = int(input("1.Attack\n2.Heal\n3.Spells\n0.Main Menu\n"))
               break
            except ValueError:
                print("Try again:\n")