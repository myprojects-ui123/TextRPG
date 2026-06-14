import random
import time

class Fight:

    def crit(self, attacker, damage):
        if random.randint(1, 100) <= attacker.crit_chance:
            print(f"Crit Damage X{attacker.crit_damage}!")
            old_damage = damage
            damage = int(damage * attacker.crit_damage)
            print(f"{old_damage} ->", end=" ")
            time.sleep(1)
            return damage
        return damage
    def damage_enemy(self, attacker, enemy):
        damage = self.dodge_enemy(attacker, enemy)
        if damage:
            print(f"{damage}\n")
        enemy.cur_hp(enemy)
        print(f"{enemy.name}: {enemy.current_hp}\n")

    def attack_enemy(self, attacker, enemy):
        self.damage_enemy(attacker, enemy)
        time.sleep(1)

       
    def dodge_enemy(self, attacker, enemy):
        print(f"{attacker.name} is attacking\n")
        damage = random.randint(int(attacker.attack * 0.5), attacker.attack)
        if attacker.class_character == "Mage":
            enemy.current_hp -= damage
            return damage
        hit_roll = random.randint(1, attacker.attack + enemy.dodge)
        if hit_roll <= enemy.dodge:
            print(f"{enemy.name} dodged the hit!\n")
            time.sleep(1)
            return
        else: 
            damage = self.crit(attacker, damage)
            enemy.current_hp -= damage
            return damage
class Heal:

    def heal_potion(self, hero):
        if hero.potion >= 1:
            self.limitation(hero)
            hero.potion -= 1
        else: 
            print("You dont have Heal potions\n")

    def limitation(self, hero):
        if hero.current_hp < hero.max_hp:
            self.healer(hero)
        else:
            print("Your Current HP is too high\n")

    def healer(self, hero):
        amount = 5
        hero.current_hp += amount
        print(f"You got heal +{amount}\n")
        if hero.current_hp > hero.max_hp:
            hero.current_hp = hero.max_hp
        print(f"Now your Current HP is: {hero.current_hp}")