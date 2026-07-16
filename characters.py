import math
from Choice_class import *
from Inventory import *
class Character:
    def __init__(self,
                  name,
                  max_hp,
                    current_hp,
                      attack,
                        dodge,
                          crit_chance,
                          exp,
                          gold,
                          heal_potion,
                          location,
                          ):
        self.name = name
        self.max_hp = max_hp
        self._current_hp = current_hp
        self.attack = attack
        self.dodge = dodge
        self.crit_chance = crit_chance
        self.exp = exp
        self.gold = gold
        self.heal_potion = heal_potion
        self.location = location
    

    # def normalize_hp(self, enemy):
    #     if enemy.current_hp < 0:
    #         enemy.current_hp = 0
    @property
    def current_hp(self):
        return self._current_hp

    @current_hp.setter
    def current_hp(self, value):
        self._current_hp = max(0, min(value, self.max_hp))
        

class Hero(Character):
    def __init__(self, 
            name, 
            strength,
            dexterity,
            magic,
            will_power,
            cunning,
            physique,
            lvl,
            exp,
            gold,
            heal_potion,
            location,
            Species,
            class_character,
            first_fight,
            story,
            chapter,
            side_quest):
            self.name = name
            self.strength = strength
            self.dexterity = dexterity
            self.magic = magic
            self.will_power = will_power
            self.cunning = cunning
            self.physique = physique
            self.lvl = lvl
            self.exp = exp
            self.gold = gold
            self.heal_potion = heal_potion
            self.location = location
            self.class_character = class_character
            self.Species = Species
            self.first_fight = first_fight
            self.story = story
            self.chapter = chapter
            self.side_quest = side_quest
            self.weapon = fists
            self.inventory = {}

            self.update_stats()

            super().__init__(
                self.name,
                self.max_hp,
                self.current_hp,
                self.attack,
                self.dodge,
                self.crit_chance,
                exp,
                gold,
                heal_potion,
                location
            )

    def gets_hp(self, enemy):
        if enemy.name == "Small_Ogr":
            self.exp += 1000
            self.gold += 40

        if enemy.name == "Ogr":
            self.exp += 125
            self.gold += 5

    def zero_hp(self, enemy):
        if enemy.current_hp == 0:
            print("You win!!!\n")
            self.gets_hp(enemy)
            return True
        elif self.current_hp == 0:
            print("You lost...\n")
            return False

    def update_stats(self):
        if self.class_character == "Warrior":
            self.max_hp = 50 + self.physique * 3
            self.attack = math.ceil((math.ceil(self.strength * 1.5) + math.ceil(self.dexterity * 0.6)) * 0.8) + self.weapon.damage
            self.dodge = math.ceil(self.dexterity * 0.5)
            self.crit_chance = math.ceil(self.cunning // 2)

        elif self.class_character == "Mage":
            self.max_hp = 50 + self.physique * 3
            self.attack = math.ceil(self.magic * 1.5) + self.weapon.damage
            self.dodge = math.ceil(self.dexterity * 0.4)
            self.crit_chance = 0
            
        elif self.class_character == "Assasin":
            self.max_hp = 50 + self.physique * 3
            self.attack = math.ceil((math.ceil(self.strength * 0.8) + math.ceil(self.dexterity * 1.5)) * 0.7) + self.weapon.damage
            self.dodge = math.ceil(self.dexterity * 0.7)
            self.crit_chance = math.ceil(self.cunning // 2) + 12

        elif self.class_character == "Tank":
            self.max_hp = (60 + self.physique * 3) + self.weapon.damage
            self.attack = math.ceil(self.max_hp * 0.08 + self.strength * 0.8)
            self.dodge = math.ceil(self.dexterity * 0.5)
            self.crit_chance = math.ceil(self.cunning // 2)
        self.current_hp = self.max_hp

class Enemy(Character):
    def __init__(self, 
            name, 
            strength,
            dexterity,
            magic,
            will_power,
            cunning,
            physique,
            heal_potion,
            stunned,
            crit_damage,
            bleeding,
            burn,
            weapon,
            location,
            Species,
            class_character):
            self.name = name
            self.strength = strength
            self.dexterity = dexterity
            self.magic = magic
            self.will_power = will_power
            self.cunning = cunning
            self.physique = physique
            self.class_character = class_character
            self.Species = Species
            self.heal_potion = heal_potion
            self.weapon = weapon
            self.location = location
            self.stunned = stunned
            self.bleeding = bleeding
            self.burn = burn
            self.crit_damage = crit_damage

            self.update_enemy()

            super().__init__(
                name,
                self.max_hp,
                self.current_hp,
                self.attack,
                self.dodge,
                self.crit_chance,
                0,
                0,
                0,
                None
                    )

    def update_enemy(self):
        self.attack = math.ceil((self.strength) + (self.dexterity) * 0.7)
        self.dodge = math.ceil(self.dexterity * 0.5)
        self.crit_chance = math.ceil(self.cunning // 2)
        self.max_hp = 50 + self.physique * 3
        self.current_hp = self.max_hp
