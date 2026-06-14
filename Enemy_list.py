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
                  "Start",
                  "Ogr",
                  "Warrior")

Ogr = create_Ogr

small_ogr = Enemy("Small_Ogr", 
                  7, 
                  5, 
                  0, 
                  5,
                  3, 
                  5,
                  0,
                  "Start",
                  "Ogr",
                  "Warrior")