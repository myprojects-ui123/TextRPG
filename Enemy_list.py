from enemies import Enemy

def create_Ogr():
    return Enemy("Ogr", 
                  7, 
                  5, 
                  0, 
                  5,
                  3, 
                  5,
                  0,
                  0,
                  1.5,
                  0,
                  0,
                  None,
                  "Ogr",
                  "Warrior")

def create_big_Ogr():
    return Enemy("Big Ogr",
                 10,
                 5,
                 2,
                 8,
                 3,
                 9,
                 0,
                 0,
                 1.5,
                 0,
                 0,
                 None,
                 "Ogr",
                 "Warrior")

Big_Ogr = create_big_Ogr()


Ogr = create_Ogr()

Soldier_chapter_0 = Enemy("Blacksmith",
                          7,
                          7,
                          1,
                          4,
                          5,
                          7,
                          0,
                          0,
                          1.5,
                          0,
                          0,
                          None,
                          "Human",
                          "Warrior")

Soldier_chapter_0_2 = Enemy("Soldier",
                            8,
                            7,
                            2,
                            6,
                            6,
                            9,
                            0,
                            0,
                            1.5,
                            0,
                            0,
                            None,
                            "Human",
                            "Warrior")

Champion_chapter = Enemy("Nathan",
                          10,
                           7,
                           2,
                           7,
                           7,
                           10,
                           0,
                           0,
                           1.5,
                           0,
                           0,
                           None,
                           "Human",
                           "Warrior")

small_ogr = Enemy("Small_Ogr", 
                  7, 
                  5, 
                  0, 
                  5,
                  3, 
                  5,
                  0,
                  0,
                  1.5,
                  0,
                  0,
                  "Start",
                  "Ogr",
                  "Warrior")