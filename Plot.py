from locations import location_s

def chapter_1_0(main_hero):
    if main_hero.chapter == 1.0:
        main_hero.story = "Find the Captian"
        if not location_s(main_hero):
            return False
        main_hero.story = "Completed"
        if main_hero.story == "Completed":
            main_hero.chapter = 1.1

def chapter_1_1(main_hero):
    if main_hero.chapter == 1.1:
        main_hero.story = "Find the captain"
        if not location_s(main_hero):
            return False
        main_hero.chapter = 1.2