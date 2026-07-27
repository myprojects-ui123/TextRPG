import time


def out_text(dialog):
    from Side_Quests import slow_print
    for text in dialog:
        slow_print(text)
        input("")

# Side_1 choice Warrior
def side_1_01():
    yield "Stranger: Well, well , well, look, who is here...\n"
    yield "You turned around and saw your friend, Nathan\n"
    yield "You:Nathan, are you still alive?:)\n"
    yield "Nathan: Of course I am. I'm not as weak as you, ha ha!\n"
    yield "You: Glad to see you. What are you doing here?\n"
    yield "Nathan: The Championship of the Kingdom starting soon in this city.\n\nAs the one of the strongest soldiers, I must be here"
    yield "You: Wait, in this city?!\nToday?!\n"
    yield "Nathan: Yeah, if you wanna participate, I can put in a good word for you, so what do you think?\n\n1.Yeah\n2.No, thanks, mate\n"
def side_1_01_choice_1():
    yield "You: Yeah, sure\n"
    yield "Nathan: Good, go to the site later, see ya\n"
def side_1_01_choice_2():
    yield "You: No, thanks\n"
    yield "Nathan: Okay, but if you change your mind, meet me in the Site\n"