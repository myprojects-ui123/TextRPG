# from characters import *
from Choice_class import *
from Inventory import Weapons

import json
        
def save(main_hero):

    inventory_save = {}

    for item, count in main_hero.inventory.items():
        inventory_save[item] = count

    if main_hero.class_character == "Mage":
        return {
        "name": main_hero.name,
        "Strength": main_hero.strength, 
        "Dexterity": main_hero.dexterity, 
        "Magic": main_hero.magic, 
        "WillPower": main_hero.will_power, 
        "Cunning": main_hero.cunning, 
        "Physique": main_hero.physique, 
        "Lvl": main_hero.lvl,
        "Species": main_hero.Species,
        "class": main_hero.class_character,
        "Current_hp": main_hero.current_hp,
        "Max_hp": main_hero.max_hp,
        "Max_Mana": main_hero.max_mana,
        "Experience": main_hero.exp,
        "Exp Need": main_hero.exp_need,
        "Gold": main_hero.gold,
        "Heal_potion": main_hero.heal_potion,
        "Inventory": inventory_save,
        "Location": main_hero.location,
        "Prologue": main_hero.first_fight,
        "Chapter": main_hero.chapter,
        "Main_story": main_hero.story,
        "Side_quest": main_hero.side_quest,
        "Mage_side_quest": main_hero.mage_side
}
    elif main_hero.class_character == "Warrior":

        inventory_save = {}

        for item, count in main_hero.inventory.items():
            inventory_save[item] = count

        return {
        "name": main_hero.name,
        "Strength": main_hero.strength, 
        "Dexterity": main_hero.dexterity, 
        "Magic": main_hero.magic, 
        "WillPower": main_hero.will_power, 
        "Cunning": main_hero.cunning, 
        "Physique": main_hero.physique, 
        "Lvl": main_hero.lvl,
        "Species": main_hero.Species,
        "class": main_hero.class_character,
        "Current_hp": main_hero.current_hp,
        "Max_hp": main_hero.max_hp,
        "Max_Stamina": main_hero.max_stamina,
        "Experience": main_hero.exp,
        "Exp Need": main_hero.exp_need,
        "Gold": main_hero.gold,
        "Heal_potion": main_hero.heal_potion,
        "Inventory": main_hero.inventory,
        "Location": main_hero.location,
        "Prologue": main_hero.first_fight,
        "Chapter": main_hero.chapter,
        "Main_story": main_hero.story,
        "Side_quest": main_hero.side_quest,
        "Warrior_Side_quest": main_hero.tournament_site
        }
    
    elif main_hero.class_character == "Assasin":

        inventory_save = {}

        for item, count in main_hero.inventory.items():
            inventory_save[item] = count

        return {
        "name": main_hero.name,
        "Strength": main_hero.strength, 
        "Dexterity": main_hero.dexterity, 
        "Magic": main_hero.magic, 
        "WillPower": main_hero.will_power, 
        "Cunning": main_hero.cunning, 
        "Physique": main_hero.physique, 
        "Lvl": main_hero.lvl,
        "Species": main_hero.Species,
        "class": main_hero.class_character,
        "Current_hp": main_hero.current_hp,
        "Max_hp": main_hero.max_hp,
        "Max_Stamina": main_hero.max_stamina,
        "Experience": main_hero.exp,
        "Exp Need": main_hero.exp_need,
        "Gold": main_hero.gold,
        "Heal_potion": main_hero.heal_potion,
        "Inventory": main_hero.inventory,
        "Location": main_hero.location,
        "Prologue": main_hero.first_fight,
        "Chapter": main_hero.chapter,
        "Main_story": main_hero.story,
        "Side_quest": main_hero.side_quest,
        "Assasin_side_quest": main_hero.assasin_side
        }
    
    elif main_hero.class_character == "Tank":

        inventory_save = {}

        for item, count in main_hero.inventory.items():
            inventory_save[item] = count
        return {
        "name": main_hero.name,
        "Strength": main_hero.strength, 
        "Dexterity": main_hero.dexterity, 
        "Magic": main_hero.magic, 
        "WillPower": main_hero.will_power, 
        "Cunning": main_hero.cunning, 
        "Physique": main_hero.physique, 
        "Lvl": main_hero.lvl,
        "Species": main_hero.Species,
        "class": main_hero.class_character,
        "Current_hp": main_hero.current_hp,
        "Max_hp": main_hero.max_hp,
        "Max_Stamina": main_hero.max_stamina,
        "Experience": main_hero.exp,
        "Exp Need": main_hero.exp_need,
        "Gold": main_hero.gold,
        "Heal_potion": main_hero.heal_potion,
        "Inventory": main_hero.inventory,
        "Location": main_hero.location,
        "Prologue": main_hero.first_fight,
        "Chapter": main_hero.chapter,
        "Main_story": main_hero.story,
        "Side_quest": main_hero.side_quest,
        "Tank_side_quest": main_hero.tank_side
        }

def save_game(main_hero):
    with open("save_1.json", "w") as file:
        json.dump(save(main_hero), file, indent=4)



def load_game():
    with open("save_1.json", "r") as file:
        save_data = json.load(file)
    if save_data["class"] == "Warrior":
        main_hero = Warrior(save_data["name"])
    elif save_data["class"] == "Mage":
        main_hero = Mage(save_data["name"])
    elif save_data["class"] == "Assasin":
        main_hero = Assasin(save_data["name"])
    elif save_data["class"] == "Tank":
        main_hero = Tank(save_data["name"])

    if main_hero.class_character == "Mage":

        for item_id, count in save_data["Inventory"].items():
            weapon = Weapons[item_id]
            main_hero.inventory[weapon] = count

        main_hero.strength = save_data["Strength"]
        main_hero.dexterity = save_data["Dexterity"]
        main_hero.magic = save_data["Magic"]
        main_hero.will_power = save_data["WillPower"]
        main_hero.cunning = save_data["Cunning"]
        main_hero.physique = save_data["Physique"]
        main_hero.lvl = save_data["Lvl"] 
        main_hero.Species = ["Species"] 
        main_hero.class_character = save_data["class"] 
        main_hero.current_hp = save_data["Current_hp"] 
        main_hero.max_hp = save_data["Max_hp"]
        main_hero.max_mana = save_data["Max_Mana"]
        main_hero.exp = save_data["Experience"]
        main_hero.gold = save_data["Gold"]
        main_hero.heal_potion = save_data["Heal_potion"]
        main_hero.inventory = save_data["Inventory"]
        main_hero.location = save_data["Location"]
        main_hero.first_fight = save_data["Prologue"]
        main_hero.chapter = save_data["Chapter"]
        main_hero.story = save_data["Main_story"]
        main_hero.side_quest = save_data["Side_quest"]
        main_hero.mage_side = save_data["Mage_side_quest"]
        return main_hero

    elif main_hero.class_character == "Warrior":


        for item_id, count in save_data["Inventory"].items():
            weapon = Weapons[item_id]
            main_hero.inventory[weapon] = count

        main_hero.strength = save_data["Strength"]
        main_hero.dexterity = save_data["Dexterity"]
        main_hero.magic = save_data["Magic"]
        main_hero.will_power = save_data["WillPower"]
        main_hero.cunning = save_data["Cunning"]
        main_hero.physique = save_data["Physique"]
        main_hero.lvl = save_data["Lvl"] 
        main_hero.Species = ["Species"] 
        main_hero.class_character = save_data["class"] 
        main_hero.current_hp = save_data["Current_hp"] 
        main_hero.max_hp = save_data["Max_hp"]
        main_hero.max_stamina = save_data["Max_Stamina"]
        main_hero.exp = save_data["Experience"]
        main_hero.gold = save_data["Gold"]
        main_hero.heal_potion = save_data["Heal_potion"]
        main_hero.inventory = save_data["Inventory"]
        main_hero.location = save_data["Location"]
        main_hero.first_fight = save_data["Prologue"]
        main_hero.chapter = save_data["Chapter"]
        main_hero.story = save_data["Main_story"]
        main_hero.side_quest = save_data["Side_quest"]
        main_hero.tournament_site = save_data["Warrior_Side_quest"]
        return main_hero
    
    elif main_hero.class_character == "Assasin":

        for item_id, count in save_data["Inventory"].items():
            weapon = Weapons[item_id]
            main_hero.inventory[weapon] = count

        main_hero.strength = save_data["Strength"]
        main_hero.dexterity = save_data["Dexterity"]
        main_hero.magic = save_data["Magic"]
        main_hero.will_power = save_data["WillPower"]
        main_hero.cunning = save_data["Cunning"]
        main_hero.physique = save_data["Physique"]
        main_hero.lvl = save_data["Lvl"] 
        main_hero.Species = ["Species"] 
        main_hero.class_character = save_data["class"] 
        main_hero.current_hp = save_data["Current_hp"] 
        main_hero.max_hp = save_data["Max_hp"]
        main_hero.max_stamina = save_data["Max_Stamina"]
        main_hero.exp = save_data["Experience"]
        main_hero.gold = save_data["Gold"]
        main_hero.heal_potion = save_data["Heal_potion"]
        main_hero.inventory = save_data["Inventory"]
        main_hero.location = save_data["Location"]
        main_hero.first_fight = save_data["Prologue"]
        main_hero.chapter = save_data["Chapter"]
        main_hero.story = save_data["Main_story"]
        main_hero.side_quest = save_data["Side_quest"]
        main_hero.assasin_side = save_data["Assasin_side_quest"]
        return main_hero
    
    elif main_hero.class_character == "Tank":

        for item_id, count in save_data["Inventory"].items():
            weapon = Weapons[item_id]
            main_hero.inventory[weapon] = count

        main_hero.strength = save_data["Strength"]
        main_hero.dexterity = save_data["Dexterity"]
        main_hero.magic = save_data["Magic"]
        main_hero.will_power = save_data["WillPower"]
        main_hero.cunning = save_data["Cunning"]
        main_hero.physique = save_data["Physique"]
        main_hero.lvl = save_data["Lvl"] 
        main_hero.Species = ["Species"] 
        main_hero.class_character = save_data["class"] 
        main_hero.current_hp = save_data["Current_hp"] 
        main_hero.max_hp = save_data["Max_hp"]
        main_hero.max_stamina = save_data["Max_Stamina"]
        main_hero.exp = save_data["Experience"]
        main_hero.gold = save_data["Gold"]
        main_hero.heal_potion = save_data["Heal_potion"]
        main_hero.inventory = save_data["Inventory"]
        main_hero.location = save_data["Location"]
        main_hero.first_fight = save_data["Prologue"]
        main_hero.chapter = save_data["Chapter"]
        main_hero.story = save_data["Main_story"]
        main_hero.side_quest = save_data["Side_quest"]
        main_hero.tank_side = save_data["Tank_side_quest"]
        return main_hero