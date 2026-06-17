from locations import location_s

def chapter_1_1(main_hero):
    if main_hero.first_fight == True and main_hero.chapter == 1:
        main_hero.chapter = "Find the Captian"
        location_s(main_hero)
        main_hero.story = 2

def chapter_1_2(main_hero):
    if main_hero.first_fight == True and main_hero.chapter == 2:
        main_hero.chapter = "Find the captain"
        location_s(main_hero)
        main_hero.story = 3