
import time


def out_text(dialog):
    from Side_Quests import slow_print
    for text in dialog:
        slow_print(text)
        input("")

# Side quests Warrior
# Side_1_01 choice Warrior
def side_1_01():
    yield "Stranger: Well, well , well, look, who is here...\n"
    yield "You turned around and saw your friend, Nathan\n"
    yield "You:Nathan, are you still alive?:)\n"
    yield "Nathan: Of course I am. I'm not as weak as you, ha ha!\n"
    yield "You: Glad to see you. What are you doing here?\n"
    yield "Nathan: The Championship of the Kingdom starting soon in this city.\n\nAs the one of the strongest soldiers, I must be here"
    yield "You: Wait, in this city?!\nToday?!\n"
    yield "Nathan: Yeah, if you wanna participate, I can put in a good word for you, so what do you think?\n"

def side_1_01_choice_1():
    yield "You: Yeah, sure\n"
    yield "Nathan: Good, go to the site later, see ya\n"
def side_1_01_choice_2():
    yield "You: No, thanks\n"
    yield "Nathan: Okay, but if you change your mind, meet me in the Site\n"

def side_1_01_version_2():
    from game import main_hero
    yield "You arrived to the Site and saw many soldiers around area. Then you saw Nathan and came straight to him\n"
    yield "Nathan: Oh, you here, I knew you would come\n"
    yield "You: Of Course I would come\n"
    yield "Nathan:There are 3 stages. Quarter-Final. Semi-Final. Final.\nYou need to win 3 opponents to win Tournament\n"
    yield "You:Okay, got it\n"
    yield "Nathan: Added you to the list of participants, show them, how to fight"
    yield "You: I will\n"
    yield f"Judge: First fight of Quarter Finals: {main_hero.name} against Blacksmith\n"

def side_1_01_version_2_short_1():
    from game import main_hero
    yield f"\nJudge: And the Winner is {main_hero.name}\n"
    yield f"Judge: Next fight: {main_hero.name} against The last year Champion\n"

def side_1_01_version_2_short_2():
    from game import main_hero
    yield f"\nJudge: And Final: {main_hero.name} against Nathan\n"
    yield "Nathan: Didn't expect it will be me in the Final?\n\nLet's finally found out, who is stronger\n"

# Side 2

# Side quest Mage
# Side 1
