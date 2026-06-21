import math

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
        self.current_hp = current_hp
        self.attack = attack
        self.dodge = dodge
        self.crit_chance = crit_chance
        self.exp = exp
        self.gold = gold
        self.heal_potion = heal_potion
        self.location = location
    

    def normalize_hp(self, enemy):
        if enemy.current_hp < 0:
            enemy.current_hp = 0

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
            chapter):
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
            print("You win!\n")
            self.gets_hp(enemy)
            return True
        elif self.current_hp == 0:
            print("You died...\n")
            return False

    def update_stats(self):
        self.max_hp = 50 + self.physique * 3
        self.current_hp = self.max_hp
        if self.class_character == "Warrior":
            self.attack = math.ceil((math.ceil(self.strength * 1.5) + math.ceil(self.dexterity * 0.6)) * 0.8)
            self.dodge = math.ceil(self.dexterity * 0.5)
            self.crit_chance = math.ceil(self.cunning // 2)

        elif self.class_character == "Mage":
            self.attack = math.ceil(self.magic * 1.5)
            self.dodge = math.ceil(self.dexterity * 0.4)
            self.crit_chance = 0
            
        elif self.class_character == "Assasin":
            self.attack = math.ceil((math.ceil(self.strength * 0.8) + math.ceil(self.dexterity * 1.5)) * 0.7)
            self.dodge = math.ceil(self.dexterity * 0.7)
            self.crit_chance = math.ceil(self.cunning // 2) + 12

        elif self.class_character == "Tank":
            self.attack = math.ceil(self.max_hp * 0.08 + self.strength * 0.8)
            self.dodge = math.ceil(self.dexterity * 0.5)
            self.crit_chance = math.ceil(self.cunning // 2)
