from saves import *

import os

class Menu:
    def main_menu(self):
        while True:
                fault = None
                try:
                    self.start_game = int(input("1.Start Game\n2.Load Game\n3.Change the character(only in main menu)\n0.Exit\n"))
                    if self.start_game == 0:
                        break
                    elif self.start_game == 1:
                        fault = int(input("Do you want to start a new game?\n1.Yes\n2.No\n"))
                        if fault == 1:
                            break
                    elif self.start_game == 2:
                        if os.path.exists("save_1.json"):
                            return load_game()
                        else:
                            print("\nNo save file found\n")

                    elif self.start_game == (3):
                        print("Developing\n")

                    else:
                        print("Wrong\n")
                except ValueError:
                    print("Try again:\n")

    def back_to_main_menu(self, main_hero):
            try:
                save_point = int(input("Do you wanna save the game?\n1.Yes\n2.No\n3.Cancel\n"))
                if save_point == 1:
                    main_hero = save_game(main_hero)
                    return True
                elif save_point == 2:
                    return True
                elif save_point == 3:
                    return False
                else:
                    print("Incorrect choice\n")
            except ValueError:
                print("Error\n")