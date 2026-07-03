class Weapon:
    def __init__(self, name, damage, price, rarity):
        self.name = name
        self.damage = damage
        self.price = price
        self.rarity = rarity

class Enemy_Weapon(Weapon):
    pass

def count_item(main_hero):
    for item, count in main_hero.inventory.items():
        print(f"- {item}: {count}")

def add_item(hero, item_name):
    if item_name in hero.inventory:
        hero.inventory[item_name] += 1
    else:
        hero.inventory[item_name] = 1

def equip_weapon(hero, weapon_name):
    for item in hero.inventory:
        if item.name == weapon_name:
            old_weapon = hero.weapon
            hero.weapon = item
            hero.inventory[item] -= 1
            add_item(hero, old_weapon)
            print(f"You equiped a {hero.weapon}\n")
            return
        else:
            print("Not found\n")

# Primitive weapon 1 star
fists = Weapon("Fists", 0, 0, "1 star")

old_staff = Weapon("Old Staff", 0, 0, "1 star")

steel_blade = Weapon("Steel Blade", 5, 50, "1 star")

staff = Weapon("Mage Staff", 5, 60, "1 star")

blades = Weapon("Small Knives", 5, 50, "1 star")

armor = Weapon("Steel Armor", 20, 50, "1 star")


# Enemy Weapon

fists_enemy = Enemy_Weapon("Fists", 0, 0, "1 star")

strong_hands = Enemy_Weapon("Strong Hands", 7, 0, "2 star")