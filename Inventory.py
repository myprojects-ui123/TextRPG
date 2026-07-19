class Weapon:
    def __init__(self, id, name, damage, price, rarity):
        self.id = id
        self.name = name
        self.damage = damage
        self.price = price
        self.rarity = rarity

class Enemy_Weapon(Weapon):
    pass

def count_item(main_hero):
    if not main_hero.inventory:
        print("No objects in Inventory")
        return
    
    print(f"Gold: {main_hero.gold}\n")
    print(f"Heal Potion: {main_hero.heal_potion}\n")

    for item, count in main_hero.inventory.items():
        weapon = Weapons[item]
        print(f"- {weapon.name}: {count}\n")

    

def add_item(hero, item):
    if item.id in hero.inventory:
        hero.inventory[item.id] += 1
    else:
        hero.inventory[item.id] = 1

def equip_weapon(hero, weapon):
    for item in hero.inventory:
        if item.id == weapon.id:
            old_weapon = hero.weapon.id
            hero.weapon.id = item.id
            hero.inventory[item.id] -= 1
            if not old_weapon.id == "fists":
                add_item(hero, old_weapon)
            print(f"You equiped a {hero.weapon}\n")
            return
        else:
            print("Not found\n")


# Primitive weapon 1 star
fists = Weapon("fists", "Fists", 0, 0, "1 star")

old_staff = Weapon("old_staff", "Old Staff", 0, 0, "1 star")

steel_blade = Weapon("steel_blade", "Steel Blade", 5, 50, "1 star")

staff = Weapon("mage_staff", "Mage Staff", 5, 60, "1 star")

blades = Weapon("small_knives", "Small Knives", 5, 50, "1 star")

armor = Weapon("steel_armor", "Steel Armor", 20, 50, "1 star")


# Enemy Weapon

fists_enemy = Enemy_Weapon("fists_2", "Fists", 0, 0, "1 star")

strong_hands = Enemy_Weapon("strong_hands", "Strong Hands", 7, 0, "2 star")






Weapons = {
    fists.id: fists,
    old_staff.id: old_staff,
    steel_blade.id: steel_blade,
    staff.id: staff,
    blades.id: blades,
    armor.id: armor 
}
