import time
from characters import Hero


class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, 13, 7, 3, 9, 5, 13, 1, 0, 0, 0, "Start ", "Human", "Warrior", False, None, 0.0)
        self.kick_stun = 2
        self.kick_cd = 0
        self.crit_damage = 1.5
        self.exp_need = 1000
        self.max_stamina = 20 + self.will_power * 3
        self.current_stamina = self.max_stamina
        self.update_stats()
        self.update_stats_w()

    def lvl_up(self):
        if self.exp >= self.exp_need:
            self.lvl += 1
            self.exp = self.exp - self.exp_need
            self.exp_need = self.exp_need + 500
            print(f"Your lvl = {self.lvl}!!!\n")
            for i in range(3, 0, -1):
                level = int(input(f"You have {i} points, what are you want to upgrade:\n1.Strength\n2.Dexterity\n3.Magic\n4.Willpower\n5.Cunning\n6.Physique\n"))
                if level == 1:
                    self.strength += 1
                elif level == 2:
                    self.dexterity += 1
                elif level == 3:
                    self.magic += 1
                elif level == 4:
                    self.will_power += 1
                elif level == 5:
                    self.cunning += 1
                elif level == 6:
                    self.physique += 1
                self.update_stats()
                self.update_stats_w()
        
    def update_stats_w(self):
        self.max_stamina = 20 + self.will_power * 3
        self.current_stamina = self.max_stamina

        

    
    def victory_text(self):
        print("You calmly cut off the ogr's head.\n")
        time.sleep(3)
        print("You were under attack 1 hour.")
        time.sleep(1)
        print("""Killed many ogres and saved many merchants from death, 
              you proved yourself again as a good and talent soldier""")
        time.sleep(3)
        print("""You Reached City with on problems after this one.
              Then Captain Mave, one of the strongest soldier in the entire Kingdom came up to you:\n""")
        time.sleep(3)
        print("""Captain Mave: You fought very well, soldier.
               For a long time I didn't see such an ordinary and young soldier
               that can fight so discipline and good, What your Name?""")
        time.sleep(5)
        print(f"My name is {self.name}")

    def prologue(self):
        print("December 8:53, North Forest")
        time.sleep(3)
        print("""
              You, young Soldier, was born in village in northern part of the city Belmon 21 years ago. 
              In 18 years, after your parents died, you decided to join in army.
              You were learn fast and completed you education year.
              Over the next two years, you proved yourself as a disciplined and dependable soldier. 
              your actions on and off the battlefield earned you overwhelmingly positive recommendations 
              from officers of every rank

              Many believed that a promising military career awaited you in the years to come  
              """)
        time.sleep(3)
        print("""
                Now, while travelling to your new assignment,
                you find yourself escorting an important convoy through dangerous lands
              """)
        time.sleep(3)
        print("""
              You: So, you have been in the second company. 
              How did you end up working as a caravan guard?
                 
                 Mercenary: Better pay, less paperwork
                 
                 You: That's it?

                 Mercenary: Yeah
              
                 Merchant:Ha! Don't listen to him. He's just lazy to tell his true reasons
                 """)
        time.sleep(3)
        print("""
              Before the mercenary could answer, a guard screamed...
              
                Guard: Alarm, to arms!
              
                You: What happened?
                 
                Guard: Ogrs! We're under attack
              
                You leaved you're tent and saw dozens of Ogrs coming straight in your way

                In this time you got ready...
                """)

class Mage(Hero):
    def __init__(self, name):
        super().__init__(name, 3, 5, 18, 13, 4, 7, 1, 0, 0, 0, "Start", "Human", "Mage", False, None, 0.0)
        self.max_mana = 25 + self.will_power * 3
        self.current_mana = self.max_mana
        self.dimension_cd = 0
        self.crit_damage = 0
        self.exp_need = 1000
        
        self.update_stats()
        self.update_stats_m()

    def update_stats_m(self):
        self.max_mana = 25 + self.will_power * 3
        self.current_mana = self.max_mana
        
    def lvl_up(self):
        if self.exp >= self.exp_need:
            self.lvl += 1
            self.exp = self.exp - self.exp_need 
            self.exp_need = self.exp_need + 500
            print(f"Your lvl = {self.lvl}!!!\n")
            for i in range(3, 0, -1):
                level = int(input(f"You have {i} points, what are you want to upgrade:\n1.Strength\n2.Dexterity\n3.Magic\n4.Willpower\n5.Cunning\n6.Physique\n"))
                if level == 1:
                    self.strength += 1
                elif level == 2:
                    self.dexterity += 1
                elif level == 3:
                    self.magic += 1
                elif level == 4:
                    self.will_power += 1
                elif level == 5:
                    self.cunning += 1
                elif level == 6:
                    self.physique += 1
                self.update_stats()
                self.update_stats_m()

    def victory_text(self):
        print("You banished the ogr to another dimension.\n")
    
    


class Assasin(Hero):
    def __init__(self, name):
        super().__init__(name, 8, 17, 4, 6, 10, 5, 1, 0, 0, 0, "Start", "Human", "Assasin", False, None, 0.0)
        self.max_stamina = 20 + self.will_power * 3
        self.current_stamina = self.max_stamina
        self.exp_need = 1000
        self.poison_cd = 0
        self.crit_damage = 2

        self.update_stats()
        self.update_stats_a()

    def update_stats_a(self):
        self.max_stamina = 20 + self.will_power * 3
        self.current_stamina = self.max_stamina
    
    def lvl_up(self):
        if self.exp >= self.exp_need:
            self.lvl += 1
            self.exp = self.exp - self.exp_need
            self.exp_need = self.exp_need + 500
            print(f"Your lvl = {self.lvl}!!!\n")
            for i in range(3, 0, -1):
                level = int(input(f"You have {i} points, what are you want to upgrade:\n1.Strength\n2.Dexterity\n3.Magic\n4.Willpower\n5.Cunning\n6.Physique\n"))
                if level == 1:
                    self.strength += 1
                elif level == 2:
                    self.dexterity += 1
                elif level == 3:
                    self.magic += 1
                elif level == 4:
                    self.will_power += 1
                elif level == 5:
                    self.cunning += 1
                elif level == 6:
                    self.physique += 1
                self.update_stats()
                self.update_stats_a()
            
        

    def victory_text(self):
        print("The Ogr died from numerous wounds bcz of knife you took from him.\n")

class Tank(Hero):

    def __init__(self, name):
        super().__init__(name, 8, 3, 2, 9, 3, 25, 1, 0, 0, 0, "Start", "Human", "Tank", False, None, 0.0)
        self.crit_damage = 1.2
        self.exp_need = 1000
        self.armor_cd = 0
        self.max_stamina = 20 + self.will_power * 3
        self.current_stamina = self.max_stamina
        
        self.update_stats()
        self.update_stats_t()
        
    def update_stats_t(self):
        self.max_stamina = 20 + self.will_power * 3
        self.current_stamina = self.max_stamina

    def lvl_up(self):
        if self.exp >= self.exp_need:
            self.lvl += 1
            self.exp = self.exp - self.exp_need
            self.exp_need = self.exp_need + 500
            print(f"Your lvl = {self.lvl}!!!\n")
            for i in range(3, 0, -1):
                level = int(input(f"You have {i} points, what are you want to upgrade:\n1.Strength\n2.Dexterity\n3.Magic\n4.Willpower\n5.Cunning\n6.Physique\n"))
                if level == 1:
                    self.strength += 1
                elif level == 2:
                    self.dexterity += 1
                elif level == 3:
                    self.magic += 1
                elif level == 4:
                    self.will_power += 1
                elif level == 5:
                    self.cunning += 1
                elif level == 6:
                    self.physique += 1
                self.update_stats()
                self.update_stats_t()
            

    def victory_text(self):
        print(".Ogr couldn't make any scratch on you and ran away\n")