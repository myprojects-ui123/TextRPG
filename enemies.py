from characters import Character

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
        self.attack = int((self.strength) + (self.dexterity) * 0.7)
        self.dodge = int(self.dexterity * 0.5)
        self.crit_chance = int(self.cunning // 2)
        self.max_hp = 50 + self.physique * 3
        self.current_hp = self.max_hp
