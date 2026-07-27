class Weapon:
    def __init__(self, id, name, damage, price, rarity):
        self.id = id
        self.name = name
        self.damage = damage
        self.price = price
        self.rarity = rarity

class Enemy_Weapon(Weapon):
    pass

class Armor:
    def __init__(self, id, name, resistance, price, rarity):
        self.id = id
        self.name = name
        self.resistance = resistance
        self.prie = price
        self.rarity = rarity
        

def count_item(main_hero):

    print(f"\nGold: {main_hero.gold}\n")
    print(f"Heal Potion: {main_hero.heal_potion}\n")
    if not main_hero.inventory:
        print("No objects in Inventory\n")
        return
    

    menu_items = []
    number = 0
    print("Weapons:\n")
    for item, count in main_hero.inventory.items():
        number += 1 
        if item in Weapons:
            weapon = Weapons[item]
            menu_items.append(Weapons[item])
            print(f"{number}. {weapon.name}: {count}\n")
    

    print("Armors:\n")
    for item, count in main_hero.inventory.items():
        number += 1
        if item in Armors:
            armor = Armors[item]
            menu_items.append(Armors[item])
            print(f"{number} {armor.name}: {count}\n")

        else:
            print("No Armor\n")
            break
    print("What item do you want to equip?\n")

    choice = int(input("0 to go back\n> "))
    selected_item = menu_items[choice - 1]

    if choice == 0:
        return
    if isinstance(selected_item, Weapon):
        equip_weapon(main_hero, selected_item)
    
    elif isinstance(selected_item, Armor):
        equip_armor(main_hero, selected_item)


def add_item(hero, item):
    if item in hero.inventory:
        hero.inventory[item] += 1
    else:
        hero.inventory[item] = 1

# Equip
def equip_weapon(hero, weapon):
    for item in hero.inventory:
        if item == weapon.id:
            weapon = Weapons[item]
            old_weapon = hero.weapon.id
            hero.weapon.id = item
            hero.inventory[item] -= 1
            if hero.inventory[item]:
                del hero.inventory[item] 
            if not old_weapon == "fists" or old_weapon != None:
                add_item(hero, old_weapon)
            print(f"You equiped a {weapon.name}\n")
            return
        else:
            print("Not found\n")

def equip_armor(hero, armor):
    for item in hero.inventory:
        if item.id == armor.id:
            old_armor = hero.armor.id
            hero.armor.id = item.id
            hero.inventory[item.id] -= 1
            if not old_armor.id == "fists":
                add_item(hero, old_armor)
            print(f"You equiped a {hero.armor}\n")
            return
        else:
            print("Not found\n")


# Primitive weapon 1 star
fists = Weapon("fists", "Fists", 0, 0, "1 star")

old_staff = Weapon("old_staff", "Old Staff", 0, 0, "1 star")

steel_blade = Weapon("steel_blade", "Steel Blade", 5, 50, "1 star")

staff = Weapon("mage_staff", "Mage Staff", 5, 60, "1 star")

blades = Weapon("small_knives", "Small Knives", 5, 50, "1 star")

steel_gloves = Weapon("steel_gloves", "Steel Gloves", 20, 50, "1 star")


# Enemy Weapon

fists_enemy = Enemy_Weapon("fists_2", "Fists", 0, 0, "1 star")

strong_hands = Enemy_Weapon("strong_hands", "Strong Hands", 7, 0, "2 star")



# Armor 

Clothes = Armor("clothes", "Shirt", 0, 0, "1 star")

Mantle = Armor("mantle", "Mantle", 0, 0, "1 star")

Iron_Armor = Armor("iron_armor", "Iron Armor", 5, 75, "1 star")

Mage_Mantle = Armor("mage_mantle", "Mage Mantle", 6, 65, "1 star")

Mantle_of_Thief = Armor("mantle_of_thief", "Thief Mantle", 4, 70, "1 star")



Weapons = {
    fists.id: fists,
    old_staff.id: old_staff,
    steel_blade.id: steel_blade,
    staff.id: staff,
    blades.id: blades,
    steel_gloves.id: steel_gloves
}

Armors = {
    Clothes.id: Clothes,
    Mantle.id: Mantle,
    Iron_Armor.id: Iron_Armor,
    Mage_Mantle.id: Mage_Mantle,
    Mantle_of_Thief.id: Mantle_of_Thief 
}