from saves import save_game







def back_to_main_menu(main_hero):
    while True:
        save_point = int(input("Do you wanna save the game?\n1.Yes\n2.No\n3.Cancel\n"))
        if save_point == 1:
           return save_game(main_hero)

        elif save_point == 2:
            return 
        elif save_point > 3 and save_point <= 0:
            continue