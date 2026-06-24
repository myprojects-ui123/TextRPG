from characters import *
from Choice_class import *

import json
        
def save(main_hero):
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
        "Location": main_hero.location,
        "Prologue": main_hero.first_fight,
        "Chapter": main_hero.chapter,
        "Main_story": main_hero.story,
        "Side_quest": main_hero.side_quest
}
    else:
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
        "Location": main_hero.location,
        "Prologue": main_hero.first_fight,
        "Chapter": main_hero.chapter,
        "Main_story": main_hero.story,
        "Side_quest": main_hero.side_quest
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
        main_hero.location = save_data["Location"]
        main_hero.first_fight = save_data["Prologue"]
        main_hero.chapter = save_data["Chapter"]
        main_hero.story = save_data["Main_story"]
        main_hero.side_quest = save_data["Side_quest"]
        return main_hero

    else:
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
        main_hero.location = save_data["Location"]
        main_hero.first_fight = save_data["Prologue"]
        main_hero.chapter = save_data["Chapter"]
        main_hero.story = save_data["Main_story"]
        main_hero.side_quest = save_data["Side_quest"]
        return main_hero