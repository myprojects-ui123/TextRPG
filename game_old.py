# def start_story():
#         while True:
#             try:
#                 skip = int(input("Do you want to skip Prologue:\n1.Skip\n2.No Skip\n"))
#                 if skip == 2:
#                     main_hero.prologue()
#                     break
#                 elif skip == 1:
#                     break
#                 else:
#                     print("Wrong\n")
#             except ValueError:
#                 print("Try Again\n")    

# class Game:
#     def choice_hero(self):
#         while True:
#             try:
#                 self.start_game = int(input("1.Start Game\n2.Change the character(only in main menu)\n0.Exit\n"))
#                 if self.start_game in (1, 0):
#                     break
#                 if self.start_game == (2):
#                     print("Developing\n")
#                 if self.start_game not in (0, 1, 2):
#                     print("Wrong\n")
#             except ValueError:
#                 print("Try again:\n")
    
    

    

#     def cicle(self):
       
#        while True:
#             try:
#                self.start = int(input("1.Attack\n2.Heal\n3.Spells\n0.Main Menu\n"))
#                break
#             except ValueError:
#                 print("Try again:\n")
# class Character:
#     def __init__(self,
#                   name,
#                   max_hp,
#                     current_hp,
#                       attack,
#                         dodge,
#                           crit_chance,
#                           exp,
#                           gold
#                           ):
#         self.name = name
#         self.max_hp = max_hp
#         self.current_hp = current_hp
#         self.attack = attack
#         self.dodge = dodge
#         self.crit_chance = crit_chance
#         self.exp = exp
#         self.gold = gold

    

#     def cur_hp(self, enemy):
#         if enemy.current_hp < 0:
#             enemy.current_hp = 0

# class Hero(Character):
#     def __init__(self, 
#             name, 
#             strength,
#             dexterity,
#             magic,
#             will_power,
#             cunning,
#             physique,
#             lvl,
#             exp,
#             gold,
#             Species,
#             class_character):
#             self.name = name
#             self.strength = strength
#             self.dexterity = dexterity
#             self.magic = magic
#             self.will_power = will_power
#             self.cunning = cunning
#             self.physique = physique
#             self.lvl = lvl
#             self.exp = exp
#             self.gold = gold
#             self.class_character = class_character
#             self.Species = Species

#             self.update_stats()

#             super().__init__(
#                 self.name,
#                 self.max_hp,
#                 self.current_hp,
#                 self.attack,
#                 self.dodge,
#                 self.crit_chance,
#                 exp,
#                 gold
#             )


#     def saves(self):
#         with open("save_1.json", "w") as file:
#             json.dump(self.save(), file, indent=4)
        
#     def save(self):
#         return {
#         "name": self.name,
#         "Strength": self.strength, 
#         "Dexterity": self.dexterity, 
#         "Magic": self.magic, 
#         "WillPower": self.will_power, 
#         "Cunning": self.cunning, 
#         "Physique": self.physique, 
#         "Lvl": self.lvl,
#         "Species": self.Species,
#         "class": self.class_character,
#         "Current_hp": self.current_hp,
#         "Max_hp": self.max_hp,
#         "Experience": self.exp,
#         "Gold": self.gold

# }
    
#     def gets_hp(self, enemy):
#         print(enemy.name, "gets arrived")
#         if enemy.name == "Ogr":
#             self.exp += 1250
#             self.gold += 40
#             print("Exp:", self.exp)

#         if enemy.name == "Small_Ogr":
#             self.exp += 125
#             self.gold += 5

#     def zero_hp_start(self, enemy):
#         if enemy.current_hp == 0:
#             print("You win!\n")
#             self.gets_hp(enemy)
#             return True
#         elif self.current_hp == 0:
#             print("You died...\n")
#             return True

#     def update_stats(self):
#         self.max_hp = 50 + self.physique * 3
#         self.current_hp = self.max_hp
#         if self.class_character == "Warrior":
#             self.attack = int((int(self.strength * 1.5) + int(self.dexterity * 0.8)) * 0.7)
#             self.dodge = int(self.dexterity * 0.5)
#             self.crit_chance = int(self.cunning // 2)

#         elif self.class_character == "Mage":
#             self.attack = int(self.magic * 1.5)
#             self.dodge = int(self.dexterity * 0.4)
#             self.crit_chance = 0
            
#         elif self.class_character == "Assasin":
#             self.attack = int((int(self.strength * 0.8) + int(self.dexterity * 1.5)) * 0.7)
#             self.dodge = int(self.dexterity * 0.7)
#             self.crit_chance = int(self.cunning // 2) + 10

#         elif self.class_character == "Tank":
#             self.attack = int(self.max_hp * 0.08 + self.strength * 0.8)
#             self.dodge = int(self.dexterity * 0.5)
#             self.crit_chance = int(self.cunning // 2)
        
#     def update_enemy(self):
#         self.attack = int((self.strength) + (self.dexterity) * 0.7)
#         self.dodge = int(self.dexterity * 0.5)
#         self.crit_chance = int(self.cunning // 2)
#         self.max_hp = 50 + self.physique * 3
#         self.current_hp = self.max_hp

    

# class Enemy(Character):
#     def __init__(self, 
#             name, 
#             strength,
#             dexterity,
#             magic,
#             will_power,
#             cunning,
#             physique,
#             Species,
#             class_character):
#             self.name = name
#             self.strength = strength
#             self.dexterity = dexterity
#             self.magic = magic
#             self.will_power = will_power
#             self.cunning = cunning
#             self.physique = physique
#             self.class_character = class_character
#             self.Species = Species

#             self.update_enemy()

#             super().__init__(
#                 name,
#                 self.max_hp,
#                 self.current_hp,
#                 self.attack,
#                 self.dodge,
#                 self.crit_chance,
#                 0,
#                 0
#                     )

#     def update_enemy(self):
#         self.attack = int((self.strength) + (self.dexterity) * 0.7)
#         self.dodge = int(self.dexterity * 0.5)
#         self.crit_chance = int(self.cunning // 2)
#         self.max_hp = 50 + self.physique * 3
#         self.current_hp = self.max_hp

    

# class loads_and_saves():

# class Warrior(Hero):
#     def __init__(self, name):
#         super().__init__(name, 13, 7, 3, 9, 5, 13, 1, 0, 0, "Human", "Warrior")
#         self.kick_stun = 2
#         self.kick_cd = 0
#         self.crit_damage = 1.5

#         self.update_stats()

    
#     def victory_text(self):
#         print("You took a sword from Hunter and calmly cut off the ogr's head.\n")

#     def prologue(self):
#         print("December 8:53, North Forest")
#         time.sleep(3)
#         print("""
#               You, young Soldier, was born in village in northern part of the city Belmon 21 years ago. 
#               In 18 years, after your parents died, you decided to join in army.
#               You were learn fast and completed you education year.
#               Over the next two years, you proved yourself as a disciplined and dependable soldier. 
#               your actions on and off the battlefield earned you overwhelmingly positive recommendations 
#               from officers of every rank

#               Many believed that a promising military career awaited you in the years to come  
#               """)
#         time.sleep(3)
#         print("""
#                 Now, while travelling to your new assignment,
#                 you find yourself escorting an important convoy through dangerous lands
#               """)
#         time.sleep(3)
#         print("""
#               You: So, you have been in the second company. 
#               How did you end up working as a caravan guard?
                 
#                  Mercenary: Better pay, less paperwork
                 
#                  You: That's it?

#                  Mercenary: Yeah
              
#                  Merchant:Ha! Don't listen to him. He's just lazy to tell his true reasons
#                  """)
#         time.sleep(3)
#         print("""
#               Before the mercenary could answer, a guard screamed...
              
#                 Guard: Alarm, to arms!
              
#                 You: What happened?
                 
#                 Guard: Ogrs! We're under attack
              
#                 You leaved you're tent and saw dozens of Ogrs coming straight in your way

#                 In this time you got ready...
#                 """)

# class Mage(Hero):
#     def __init__(self, name):
#         super().__init__(name, 3, 5, 18, 13, 4, 7, 1, 0, 0, "Human", "Mage")
#         self.max_mana = 25 + self.will_power * 3
#         self.current_mana = self.max_mana
#         self.crit_damage = 0

#         self.update_stats()
#     def victory_text(self):
#         print("You banished the ogr to another dimension.\n")
    
    


# class Assasin(Hero):
#     def __init__(self, name):
#         super().__init__(name, 8, 17, 4, 6, 10, 5, 1, 0, 0, "Human", "Assasin")
#         self.crit_damage = 2
#         self.update_stats()

#     def victory_text(self):
#         print("The Ogr died from numerous wounds bcz of knife you took from him.\n")

# class Tank(Hero):
#     def __init__(self, name):
#         super().__init__(name, 8, 3, 2, 9, 3, 25, 1, 0, 0, "Human", "Tank")
#         self.crit_damage = 1.2
#         self.update_stats()

#     def victory_text(self):
#         print(".Ogr couldn't make any scratch on you and ran away\n")

# class Fight:

#     def crit(self, attacker, damage):
#         if random.randint(1, 100) <= attacker.crit_chance:
#             print(f"Crit Damage X{attacker.crit_damage}!")
#             old_damage = damage
#             damage = int(damage * attacker.crit_damage)
#             print(f"{old_damage} ->", end=" ")
#             time.sleep(1)
#             return damage
#         return damage
#     def damage_enemy(self, attacker, enemy):
#         damage = self.dodge_enemy(attacker, enemy)
#         if damage:
#             print(f"{damage}\n")
#         enemy.cur_hp(enemy)
#         print(f"{enemy.name}: {enemy.current_hp}\n")

#     def attack_enemy(self, attacker, enemy):
#         self.damage_enemy(attacker, enemy)
#         time.sleep(1)

       
#     def dodge_enemy(self, attacker, enemy):
#         print(f"{attacker.name} is attacking\n")
#         damage = random.randint(int(attacker.attack * 0.5), attacker.attack)
#         if attacker.class_character == "Mage":
#             enemy.current_hp -= damage
#             return damage
#         hit_roll = random.randint(1, attacker.attack + enemy.dodge)
#         if hit_roll <= enemy.dodge:
#             print(f"{enemy.name} dodged the hit!\n")
#             time.sleep(1)
#             return
#         else: 
#             damage = self.crit(attacker, damage)
#             enemy.current_hp -= damage
#             return damage
# class Heal:

#     def limitation(self, hero):
#         if hero.current_hp < 90:
#             self.healer(hero)
#         else:
#             print("Your Current HP is too high\n")

#     def healer(self, hero):
#         amount = 5
#         hero.current_hp += amount
#         print(f"You got heal +{amount}\n")
#         if hero.current_hp > hero.max_hp:
#             hero.current_hp = hero.max_hp
#         print(f"Now your Current HP is: {hero.current_hp}")

# name_Main = input("Write your Name(6 letter or more):\n")
# if len(name_Main) < 6:
#     while True:
#         name_Main = input("\nTry again(6 letter or more):\n")
#         if len(name_Main) >= 6:
#             break
        



# classes = {
#    1: {
#        "name": name_Main,
#        "max_hp": 115,
#        "current_hp": 115,
#        "attack": 15,
#        "dodge": 15,
#        "ignore_dodge": False,
#        "crit_chance": 0,
#        "crit_damage": 1.5,
#        "Species": "Human",
#        "class": "Warrior"
#        },
#     2: {
#         "name": name_Main,
#         "max_hp": 70,
#         "current_hp": 70,
#         "attack": 30,
#         "dodge": 8,
#         "ignore_dodge": True,
#         "crit_chance": 0,
#         "crit_damage": 1,
#         "Species": "Human",
#         "class": "Mage"
#         },
#     3: {
#         "name": name_Main,
#         "max_hp": 80,
#         "current_hp": 80,
#         "attack": 20,
#         "dodge": 20,
#         "ignore_dodge": False,
#         "crit_chance": 10,
#         "crit_damage": 2,
#         "Species": "Human",
#         "class": "Assasin"
#         },
#     4: {
#         "name": name_Main,
#         "max_hp": 150,
#         "current_hp": 150,
#         "attack": 10,
#         "dodge": 5,
#         "ignore_dodge": False,
#         "crit_chance": 0,
#         "crit_damage": 1.2,
#         "Species": "Human",
#         "class": "Tank"
#         }
# }

# hero_data = classes[name_class_Main]

# while True:
#     name_class_Main = int(input("Choose your class:\n1.Warrior\n2.Mage\n3.Assasin\n4.Tank\n"))
#     if name_class_Main == 1:
#         print(f"""Characteristics:\n
# Warrior:
#     Strength: 13
#     Dexterity: 7
#     Magic: 3
#     WillPower: 9
#     Cunning: 5
#     Physique: 13
              
# Uniqueness from start:

#     Speciality:
#         - Berserk
#         - Mage Hunter

#     Advantages:

#         - No Major Advantages
              
#     Flaws:
#         - No critical Flaws
#               """)
#         name_class_Main = int(input("Do you still want to choose this class:\n1.Yes\n2.No\n"))
#         if name_class_Main == 1:
#             main_hero = Warrior(name_Main)
#             break
    
#     elif name_class_Main == 2:
#         print(f"""Characteristics:\n
# Mage:
#     Strength: 3
#     Dexterity: 5
#     Magic: 18
#     WillPower: 13
#     Cunning: 4
#     Physique: 7
              
# Uniqueness from start:

#     Speciality:
#         - Healer
#         - Mage of blood

#     Advantages:

#         - Ignore Dodge
#         - High Damage
              
#     Flaws:

#         - Low HP
#         - Critical Chance = 0%

#               """)
#         name_class_Main = int(input("Do you still want to choose this class:\n1.Yes\n2.No\n"))
#         if name_class_Main == 1:
#             main_hero = Mage(name_Main)
#             break
#     elif name_class_Main == 3:
#         print(f"""Characteristics:\n
# Assasin:
#     Strength: 8
#     Dexterity: 17
#     Magic: 4
#     WillPower: 6
#     Cunning: 10
#     Physique: 5
# Uniqueness from start:

#     Speciality:
#         - Duelist
#         - Suicide

#     Advantages:

#         - Critical Chance: +10%
#         - Critical Damage: X2
              
#     Flaws:

#         - Low HP  

#               """)
#         name_class_Main = int(input("Do you still want to choose this class:\n1.Yes\n2.No\n"))
#         if name_class_Main == 1:
#             main_hero = Assasin(name_Main)
#             break
#     elif name_class_Main == 4:
#         print(f"""Characteristics:\n
# Tank:
#     Strength: 8
#     Dexterity: 3
#     Magic: 2
#     WillPower: 9
#     Cunning: 3
#     Physique: 25

# Uniqueness from start:

#     Speciality:
#         - Golem
#         - Battle Tank

#     Advantages:

#         - High HP
#         - Attack from HP
              
#     Flaws:

#         - Low Dodge  

#               """)
#         name_class_Main = int(input("Do you still want to choose this class:\n1.Yes\n2.No\n"))
#         if name_class_Main == 1:
#             main_hero = Tank(name_Main)
#             break
    

# main_hero = Hero(
#     hero_data["name"],
#     hero_data["max_hp"],
#     hero_data["current_hp"],
#     hero_data["attack"],
#     hero_data["dodge"],
#     hero_data["ignore_dodge"],
#     hero_data["crit_chance"],
#     hero_data["crit_damage"],
#     hero_data["Species"],
#     hero_data["class"]
# )