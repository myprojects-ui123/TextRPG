from fighting import Fight


fight = Fight()

def spells(main_hero, enemy):
    assasin_spells(main_hero, enemy)
    warrior_spells(main_hero, enemy)
    mage_spells(main_hero, enemy)
    tank_spells(main_hero)

def assasin_spells(main_hero, enemy):
    if main_hero.class_character == "Assasin":
        while True:
            if main_hero.lvl < 5:
                try:
                    kill = int(input("1.Poison\n0.Back\n"))
                    if kill == 1:
                        fight.poisoning(main_hero, enemy)
                        return True
                    elif kill == 0:
                        return False
                    else:
                        print("Wrong spell\n")
                except ValueError:
                    print("Try again\n")

def warrior_spells(main_hero, enemy):
    if main_hero.class_character == "Warrior":
        while True:
            if main_hero.lvl < 5:
                try:
                    kick = int(input("1.Kick\n0.Back\n"))
                    if kick == 1:
                        fight.fighter_kick(main_hero, enemy)
                        return True
                    if kick == 0:
                        return False
                    else:
                        print("Wrong Spell\n")
                except ValueError:
                    print("Try Again\n")

def mage_spells(main_hero, enemy):
    if main_hero.class_character == "Mage":
        while True:
            if main_hero.lvl < 5:
                try:
                    banished = int(input("1.Dimenshion\n0.Back\n"))
                    if banished == 1:
                        fight.dimensions(main_hero, enemy)
                        return True
                    elif banished == 0:
                        return False
                    else:
                        print("Wrong spell\n")
                except ValueError:
                    print("Try again\n")

def tank_spells(main_hero):
    if main_hero.class_character == "Tank":
        while True:
            if main_hero.lvl < 5:
                try:
                    Armored = int(input("1.Armor\n0.Back\n"))
                    if Armored == 1:
                        fight.armor(main_hero)
                        return True
                    elif Armored == 0:
                        return False
                    else:
                        print("Wrong spell\n")
                except:
                    print("Try Again\n")