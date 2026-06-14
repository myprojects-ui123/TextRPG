from characters import Character
import math

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
            self.location = location
            self.stunned = stunned
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
