from Choice_class import Warrior, Mage, Assasin, Tank

def choose_name(name_Main):
    name_Main = input("Write your Name(6 letter or more):\n")
    if len(name_Main) < 6:
        while True:
            name_Main = input("\nTry again(6 letter or more):\n")
            if len(name_Main) >= 6:
                break
    return name_Main

def choice_start(name_Main, main_hero):
    name_class_Main = int(input("Choose your class:\n1.Warrior\n2.Mage\n3.Assasin\n4.Tank\n"))
    if name_class_Main == 1:
        print(f"""Characteristics:\n
Warrior:
    Strength: 13
    Dexterity: 7
    Magic: 3
    WillPower: 9
    Cunning: 5
    Physique: 13
              
Uniqueness from start:

    Speciality:
        - Berserk
        - Mage Hunter

    Advantages:

        - No Major Advantages
              
    Flaws:
        - No critical Flaws
              """)
        name_class_Main = int(input("Do you still want to choose this class:\n1.Yes\n2.No\n"))
        if name_class_Main == 1:
            main_hero = Warrior(name_Main)
            return main_hero
            
    
    elif name_class_Main == 2:
        print(f"""Characteristics:\n
Mage:
    Strength: 3
    Dexterity: 5
    Magic: 18
    WillPower: 13
    Cunning: 4
    Physique: 7
              
Uniqueness from start:

    Speciality:
        - Healer
        - Mage of blood

    Advantages:

        - Ignore Dodge
        - High Damage
              
    Flaws:

        - Low HP
        - Critical Chance = 0%

              """)
        name_class_Main = int(input("Do you still want to choose this class:\n1.Yes\n2.No\n"))
        if name_class_Main == 1:
            main_hero = Mage(name_Main)
            return main_hero
    elif name_class_Main == 3:
        print(f"""Characteristics:\n
Assasin:
    Strength: 8
    Dexterity: 17
    Magic: 4
    WillPower: 6
    Cunning: 10
    Physique: 5
Uniqueness from start:

    Speciality:
        - Duelist
        - Suicide

    Advantages:

        - Critical Chance: +10%
        - Critical Damage: X2
              
    Flaws:

        - Low HP  

              """)
        name_class_Main = int(input("Do you still want to choose this class:\n1.Yes\n2.No\n"))
        if name_class_Main == 1:
            main_hero = Assasin(name_Main)
            return main_hero
    elif name_class_Main == 4:
        print(f"""Characteristics:\n
Tank:
    Strength: 8
    Dexterity: 3
    Magic: 2
    WillPower: 9
    Cunning: 3
    Physique: 25

Uniqueness from start:

    Speciality:
        - Golem
        - Battle Tank

    Advantages:

        - High HP
        - Attack from HP
              
    Flaws:

        - Low Dodge  

              """)
        name_class_Main = int(input("Do you still want to choose this class:\n1.Yes\n2.No\n"))
        if name_class_Main == 1:
            main_hero = Tank(name_Main)
            return main_hero