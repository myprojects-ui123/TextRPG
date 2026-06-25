from characters import Character
import random
import time
import math

class Fight:

    def crit(self, attacker, damage):
        if random.randint(1, 100) <= attacker.crit_chance:
            print(f"Crit Damage X{attacker.crit_damage}!")
            old_damage = damage
            damage = math.ceil(damage * attacker.crit_damage)
            print(f"{old_damage} ->", end=" ")
            time.sleep(1)
            return damage
        return damage
    def damage_enemy(self, attacker, enemy):
        damage = self.dodge_enemy(attacker, enemy)
        if damage:
            print(f"{damage}\n")
        enemy.normalize_hp(enemy)
        time.sleep(1)
        print(f"{enemy.name}: {enemy.current_hp}\n")

    def fighter_kick(self, attacker, enemy):
        if attacker.kick_cd > 0:
            print(f"Kick on cooldown, {attacker.kick_cd} turns left\n")
            return False
        damage = math.ceil(attacker.strength * 1.25)

        enemy.current_hp -= damage
        enemy.stunned = 1
        
        print(f'{enemy.name} is stunned!\n')

        attacker.kick_cd = 2
        print(f"{enemy.name}: -{damage}\n")

        attacker.normalize_hp(enemy)

    def reduce_cooldown_fighter(self, main_hero, enemy):
        if main_hero.kick_cd > 0:
            main_hero.kick_cd -= 1
        
        if enemy.stunned > 0:
            enemy.stunned -= 1



    def stun(self, main_hero, enemy):
        if enemy.stunned > 0:
            print(f"{enemy.name} is stunned and skips the turn!\n")
            enemy.stunned -= 1
            
        else:
            fight = Fight()
            fight.damage_enemy(enemy, main_hero)
        
    def poisoning(self, attacker, enemy):
        if attacker.poison_cd > 0:
            print(f"Poison on cooldown, {attacker.poison.cd} turns left")
            return False

        damage = math.ceil(attacker.cunning * 1.5)
        enemy.current_hp -= damage
        enemy.bleeding = 2
        attacker.poison_cd = 3
        attacker.normalize_hp(enemy)
        print(f"You used a poison. {enemy.name} is bleeding!")

    def reduce_poison(self, attacker, enemy):
        if enemy.bleeding > 0:
            enemy.current_hp -= 5
            attacker.normalize_hp(enemy)
            print("Bleeding: -5\n")
            enemy.bleeding -= 1

        if attacker.poison_cd > 0:
            attacker.poison_cd -= 1

    def dimensions(self, attacker, enemy):
        if attacker.dimension_cd > 0:
            print(f"Dimension on cooldown, {attacker.dimension_cd} turns left")
            return False
        
        if attacker.current_mana < 30:
            print("Not enough Mana\n")
            return False

        damage = math.ceil(attacker.attack * 0.6)

        enemy.current_hp -= damage
        enemy.stunned = 2
        attacker.current_mana -= 30
        attacker.dimension_cd = 3
    
    def reduce_dimension(self, attacker, enemy):
        if attacker.dimension_cd > 0:
            attacker.dimension_cd -= 1
        if enemy.stunned > 0:
            enemy.stunned -= 1

    def armor(self, main_hero):
        if main_hero.armor_cd > 0:
            print(f"Armor on cooldown, {main_hero.armor_cd} turns left")
            return False
        print("Armor is activated!\n")
        main_hero.armor_cd = 3

    def reduce_armor(self, main_hero):
        if main_hero.armor_cd > 0:
            main_hero.armor_cd -= 1

    def dodge_enemy(self, attacker, enemy):
        print(f"{attacker.name} is attacking\n")
        damage = random.randint(int(attacker.attack * 0.5), attacker.attack)
        if attacker.class_character == "Mage":
            if enemy.stunned > 0:
                enemy.current_hp -= int(damage * 0.6)
                return damage
            else:
                enemy.current_hp -= damage
                return damage
        hit_roll = random.randint(1, attacker.attack + enemy.dodge)
        if hit_roll <= enemy.dodge:
            print(f"{enemy.name} dodged the hit!\n")
            time.sleep(1)
            return
        else: 
            damage = self.crit(attacker, damage)
            if enemy.class_character == "Tank":
                if enemy.armor_cd > 0:
                    enemy.current_hp -= int(damage * 0.85)
                    return damage
            enemy.current_hp -= damage
            return damage
class Heal:

    def heal_potion(self, hero):
        if hero.heal_potion > 0:
            self.limitation(hero)
            hero.heal_potion -= 1
        else: 
            print("You dont have Heal potions\n")

    def limitation(self, hero):
        if hero.current_hp < hero.max_hp:
            self.healer(hero)
        else:
            print("Your Current HP is too high\n")

    def healer(self, hero):
        amount = 20 + math.ceil(hero.magic * 0.15)
        hero.current_hp += amount
        print(f"You got heal +{amount}\n")
        if hero.current_hp > hero.max_hp:
            hero.current_hp = hero.max_hp
        print(f"Now your Current HP is: {hero.current_hp}")