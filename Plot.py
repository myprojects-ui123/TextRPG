from locations import location_s

def chapter_1_0(main_hero):
    if main_hero.chapter == 1.0:
        main_hero.story = "Find the Captian"
        result_of_story = location_s(main_hero)
        print("Debug: ", result_of_story)
        if not result_of_story:
            return False
        elif result_of_story == "Prologue: Chapter 1 completed":
            main_hero.story = "Completed"

        if main_hero.story == "Completed":
            from saves import save_game
            print("Debug: Story")
            main_hero.chapter = 1.1
            main_hero.location = "Camp_Prologue"
            save_game(main_hero)
            return True

def chapter_1_1(main_hero):
    if main_hero.chapter == 1.1:
        main_hero.story = "Find the captain"
        if not location_s(main_hero):
            return False
        main_hero.chapter = 1.2
        