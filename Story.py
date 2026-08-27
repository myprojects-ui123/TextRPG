from Choice_class import *
from saves import load_game
from Side_Quests import out_text

def prologue(main_hero):
    if main_hero.class_character == "Warrior":
        yield "December 13, 8:53, North Forest"
        
        yield """
        You, young Soldier, were born in village in northern part of the city Belmon 21 years ago. 
        In 18 years, after your parents died, you decided to join in army.
        You were learn fast and completed you education year.
        Over the next two years, you proved yourself as a disciplined and dependable soldier. 
        your actions on and off the battlefield earned you overwhelmingly positive recommendations 
        from officers of every rank
            """
        yield "Many believed that a promising military career awaited you in the years to come  "
              
        yield """
        Now, while travelling to your new assignment,
        you find yourself escorting an important convoy through dangerous lands
              """ 
        yield "You: So, you have been in the second company."
        yield "How did you end up working as a caravan guard?"
                 
        yield "Mercenary: Better pay, less paperwork"
                 
        yield "You: That's it?"

        yield "Mercenary: Yeah"
              
        yield "Merchant:Ha! Don't listen to him. He's just lazy to tell his true reasons"
        yield "Before the mercenary could answer, a guard screamed..."
              
        yield "Guard: Alarm, to arms!"
              
        yield "You: What happened?"
                 
        yield "Guard: Ogrs! We're under attack"
              
        yield "You leaved you're tent and saw dozens of Ogrs coming straight in your way"

        yield "In this time you got ready...\n"


    if main_hero.class_character == "Mage":
        yield "December 13, 8:53, North Forest"
        yield "You were born in capital of the Kingdom - Marol. You found magical talent when you were 4 yrs old." 
        yield "You were sent to the Academy to learn control you're power."
        yield "You were learning fast and became the best student in the entire Academy. "
        yield "When you turned 21, you and you're teacher was sent to neighboring city to give a lecture in their Academy."
        yield "That was the day you're destiny moved on...\n"
        yield "Teacher: You need some rest. There's enough training for today\n"
        yield "You: Okay, teacher, just give me a second\n"
        yield "Teacher: Everytime I give you 1 second turns into several hours\n"
        yield "I'm worring about you\n"
        yield "You: Don't worry, teacher. I promise, I won't be long\n"
        yield "Teacher: Good, because I...\n"
        yield "Guard: Alarm!!! Ogres attacking\n"
        yield "You saw dozens of Ogrs coming straight in your way\n"
        yield "You need to protect your friends!!!\n"

    if main_hero.class_character == "Assasin":
        yield "December 13, 8:53, North Forest"
        yield """You were born in the slums of the capital of kingdom - Marol. You're family was very poor
              and had to steal to survive. People around considered you as a trash. You were caught in 21 yrs and was sent
              prison in neighboring city. You thought your life ends here..."""
        yield "Security 1: And then this trash was trying to escape, but we caught pretty quick\n"
        yield "Security 2: I hope he will be executed\n"
        yield "Security 1: Yeah, me to...\n"
        yield "Silver Arrow pierced his throat. Security 2 didn't have time to turned around he was stabbed in he back by Ogr"
        yield "You had the chance to escape, but you saw Ogr was planning to attack Woman with baby. You conscience said you to help them...\n"
        

    if main_hero.class_character == "Tank":
        yield "December 13, 8:53, North Forest"
        yield "You Tank"


def start_story(main_hero):
        while True:
            while True:
                try:
                    skip = int(input("Do you want to skip Prologue:\n1.Skip\n2.No Skip\n"))
                    break
                except ValueError:
                    print("Try Again\n")
            if skip == 2:
                out_text(prologue(main_hero))
                return
            elif skip == 1:
                return
            else:
                print("Wrong\n")
                continue    