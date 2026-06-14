import random
import time
# a = int(input("Введите число: "))
# sum = 1
# for i in range(1,a + 1):
#     sum = sum * i
#     print(sum)



# a = int(input('Угадай загаданное мной число:'))
# secret = 15
# while a != secret:
#     if a < secret:
#         print('Слишком мало, попробуйте еще раз: ')
#     if a > secret:
#         print('Слишком много, попробуйте еще раз: ')
#     a = int(input("Попробуй еще раз: "))
# print('Поздравляю!!!')



# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# op = input("Какую операцию выполнить?: ")

# if op == '+':
#     print(a + b)
# elif op == '-':
#     print(a - b)
# elif op == '*':
#     print(a * b)
# elif op == "/":
#     print(a / b)



# password = "python"
# a = input("Введите пароль для доступа в систему: ")
# attempts = 2
# exit = 0
# while password != a:
#     print(f'Неверный пароль, осталось {attempts} попытки!')
#     a = input("Попробуйте еще раз: ")
#     if password != a:
#         attempts -= 1
#     if attempts == 0 and exit == 0:
#         print(f'Неверный пароль, осталось {attempts} попыток!')
#         print('Доступ запрещен на 30 секунд!!!')
#         time.sleep(30)
#         a = input("Теперь попробуйте еще раз: ")
#         attempts += 2
#         exit += 1
#     if attempts == 0 and exit == 1:
#         print(f'Неверный пароль, осталось {attempts} попыток!')
#         print('Доступ запрещен на 1 минуту!!!')
#         time.sleep(60)
#         a = input("Теперь попробуйте еще раз: ")
#         attempts += 2
#         exit += 1
#     if attempts == 0 and exit == 2:
#         print(f'Неверный пароль, осталось {attempts} попыток!')
#         print('Доступ запрещен ')
#         break
# if password == a:    
#     print('Доступ Разрешен')

# players = [1, 2, 3, 4, 5]
# for i in range(0,len(players)):
#     print(players[i])

# numbers = [10, 20, 30, 40 ,50]
# total = 0
# for i in range(0, len(numbers)):
#     total = total + numbers[i]
# print(total)

# names = ['Alex', 'Mecrury', 'Mask']
# name = input("Введите имя которое хотите найти: ")
# if name in names:
#     print('Да, это имя есть в списке')
#     for i in range(0, len(names)):
#         if names[i] == name:
#             print(f'Оно номер {i + 1} в списке')
# else:
#     print('Такого имени не существует в списке кандидатов')


# numbers = [5, 3, 19, 8, 32, 18]
# max = 0
# for i in range(0, len(numbers)):
#     if numbers[i] > max:
#         max = numbers[i]
# print(max)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# count = 0

# for i in range(0, len(numbers)):
#     if numbers[i] % 2 == 0:
#         count += 1
#         print(numbers[i])
# print(f'Количество четных чисел: {sum}')


# my_list = []
# avg_sum = 0
# for i in range(0, 5):
#     a = int(input("Введите 5 чисел, которые хотите занести в список: "))
#     my_list.append(a)
#     avg_sum = avg_sum + a
# avg_sum = avg_sum / len(my_list)
# print(my_list)
# print(avg_sum)

# names = ['Alex', 'John', 'Miles']

# for index, name in enumerate(names):
#     print(f'{index + 1}. {name}')

# def hello():
#     print("Hello")
# hello()


# def square(x):
#     x = x ** 2
#     return x

# a = int(input('Введите число для возведения в квадрат: '))
# print(square(a))


# def is_or_not(number):
#     return number % 2 == 0
        
# a = int(input("Введите число: "))
# print(is_or_not(a))


# def max_min(a, b):
#     if a > b:
#         return a
#     elif b > a:
#         return b
#     else:
#         return
# a = int(input())
# b = int(input())
# print(max_min(a, b))

# def summa(a):
#     sum = 0
#     for i in range(0, len(a)):
#         sum = sum + a[i]
#     return sum
# num = [1, 2, 3, 4, 5]
# print(summa(num))


# def max_min(num):
#     max_num = 0
#     for i in range(0, len(num)):
#         if max_num < num[i]:
#             max_num = num[i]
#     return max_num

# numbers = []
# for i in range(0, 5):
#     a = int(input())
#     numbers.append(a)
# print(max_min(numbers))


# def calculate(number):
#     sum = 0
#     for i in range(1 , 11):
#         sum = number * i
#         print(f'{number} * {i} = {sum}')
#     return sum

# a = int(input())
# calculate(a)


# def square(numbers):
#     square = 0
#     for i in range(0, len(numbers)):
#         square = numbers[i] ** 2
#         print(square)
#     return square

# numbers = []
# a = int(input())
# for i in range(0, 5):
#     numbers.append(a)
# square(numbers)


# def searching():
#     secret = 15
#     attempt = 5
    
#     for i in range(1, 6):
#         numbers = int(input("Введите число: "))
#         attempt -= 1
#         if numbers == secret:
#             print('Поздравляю!')
#             return True
#         if attempt == 0:
#             print("Доступ заблокирован")
#             return False
#         print("Неверно")

# searching()


#Менеджер списка покупок

# def empty(manager):
#     for i in range(0, 5):
#         buys = input("Напишите 5 товаров: ")
#         manager.append(buys)
#     print("Вам нужно купить: ")
#     for i in range(0, len(manager)):
#         print(f'{i + 1}. {manager[i]}')
#     return manager
# a = []
# empty(a)

# person = {
#     "name": "Ruslan",
#     "age": 23,
#     "city": 'Tashkent'
# }
# print(person["name"])
# print(person["age"])
# print(person["city"]) 


# player = {
#     "nickname": "Spider",
#     "level": 15,
#     "gold": 500
# }


# player["gold"] = 1000
# print(player["nickname"])
# print(player["level"])
# print(player["gold"])


# person = {}
# a = int(input('Введите возраст: '))
# b = input("Введите возраст: ")
# person["name"] = b
# person["age"] = a

# print(person)


# hero = {
#     "name": "Knight",
#     "hp": 100,
#     "damage": 25,
#     "armor": 15
# }

# print(f'  Герой   \nИмя: {hero["name"]}\nЗдоровье: {hero["hp"]}\nУрон: {hero["damage"]}\nБроня: {hero["armor"]}')


# products = {
#     "Хлеб": 50,
#     "Молоко": 80,
#     "Яйцо": 15
# }

# product = input("Введите назавание продукта: ")

# if product in products:
#     print(f"Цена: {products[product]}")
# else:
#     print("Товара не существует")

# word = "programming"
# print(f'{word[0]} {word[-1]}')


# name = input("Введите свое имя: ")
# print(f'В вашем имени {len(name)} букв')


# word = input('Введите слово или текст с буквой а: ')
# print('а' in word)


# login = input("Введите логин: ")
# print(login.lower())
# print(login.upper())


# text = "Я люблю тебя"
# print(text)
# print(text.replace("тебя", "себя"))


# text = input()
# text = text.replace(",", ".")
# products = text.split('.')
# print(products)


# def parol(password):
#     if 'admin' in password or len(password) <= 6:
#         return False
#     return True

# while True:
#     password = input()
#     if parol(password):
#         print('Пароль принят')
#         break
#     else:
#         print("Слабый пароль")

# Первое задание
# def quantity(word):
#     a = print(f"Длина: {len(word)}")
#     return a 
# def first(word):
#     b = print(f'Первая буква: {word[0]}')
#     return b
# def last(word):
#     c = print(f'Последняя буква: {word[-1]}')
#     return c

# right = input("Введите слово: ")
# quantity(right)
# first(right)
# last(right)

# # 2 задание
# def bukva(word):
#     return "a" in word or "а" in word
# word = input("Введите слово: ")
# if bukva(word):
#     print("Есть буква а")
# else:
#     print('Нет буквы а')


# 3 задание
# def up(name):
#     print(name.upper())
#     return name.upper()
# def low(name):
#     print(name.lower())
#     return name.lower
# name = input("Введите имя: ")
# up(name)
# low(name)


# Задача 4
# def probel(word):
#     pro = 0
#     for i in range(0, len(word)):
#         if " " in word[i]:
#             pro += 1
#     print(f'{pro} пробелов')
#     return pro
# sentence = input("Введите предложение:\n")
# probel(sentence)


#  5 task
# def stroka(word):
#     word = word.replace(".", ' ')
#     word = word.replace(",", ' ')
#     word = word.replace(":", ' ')
#     word = word.replace(";", ' ')
#     return word

# sentence = input()
# print(stroka(sentence))

# 6 task
# def raz(sentence):
#     sentence = sentence.replace('.', '.')
#     sentence = sentence.replace(':', '.')
#     sentence = sentence.replace(';', '.')
#     sentence = sentence.replace(' ', '.')
#     return sentence
# def raz_2(sentence):
#     sentence = sentence.split('.')
#     return sentence

# sentence = input("Список покупок:\n")
# print(f'Ваш Список покупок: {raz_2(raz(sentence))}')

# 7-8 task
# def silniy(parol):
#     return '1' in parol or '2' in parol or '3' in parol or '4' in parol or '5' in parol or '6' in parol or '7' in parol or '8' in parol or '9' in parol or '0' in parol
# def silniy_2(parol):
#     return len(parol) >= 8
# prinyatie = input('Write a password:\n')
# if silniy(prinyatie) and silniy_2(prinyatie) and 'admin' == False:
#     print("Password accepted")
# else:
#     print("Password not accepted")

# 9 task
# def slagayemie(sentence):
#     return 'a' in sentence or 'e' in sentence or 'y' in sentence or 'u' in sentence or 'i' in sentence or 'o' in sentence
# def slagayemie_2(sentence):
#     return 'A' in sentence or 'E' in sentence or 'Y' in sentence or 'U' in sentence or 'I' in sentence or 'O' in sentence

# glas = 0
# sentence = input('Write a sentence:\n')
# for i in range(0, len(sentence)):
#     if slagayemie(sentence[i]) or slagayemie_2(sentence[i]):
#         glas += 1
# print(f'{glas} vowels')

#  final boss task
# def login_1(login):
#     login = input("Write a login:\n")
#     while "mike123" in login or "Mike123" in login:
#         login = input("Login is taken, pls try again:\n")
#     print("Accepted")
#     return login
# def password_1(password):
#     return "admin" not in password and len(password) >= 8
# def password_3(password):
#     has_digit = False
#     for symbol in password:
#         symbol.isdigit()
#         if symbol.isdigit():
#             has_digit = True
#     return has_digit
# def password_4(password):
#     has_alpha = False
#     for symbol in password:
#         symbol.isalpha()
#         if symbol.isalpha():
#             has_alpha = True
#     return has_alpha

# login_0 = ""
# login = login_1(login_0)

# password = input("Write a password:\n")
# while not (password_1(password) and password_3(password) and password_4(password)):
#         password = input("Weak password, pls try again:\n")
#         if password_1(password) and password_3(password) and password_4(password):
#             break
# print("Accepted\n")
# print(f"Your Login: {login}\nYour Password: {password}")

# import random
# 1 task
# number = random.randint(1, 100)
# print(number)

# 2 task
# guess = int(input('Guess a number:\n'))

# while True:   
#     secret = random.randint(1, 5) 
#     if secret != guess:

#         guess = int(input("Try again:\n"))
#     else:
#         break
# print('Congratulations!!!')

# 3 task

# def rand(heroes):
#     hero = random.choice(heroes)
#     return hero
# heroes = ['Tank', 'Mage', 'Warrior']

# is_true = ''

# while True:
    
#     choice = int(input('Press 1 to choice 1 random fighter or 0 to quit:\n'))
#     if choice == 1:
#         hero = rand(heroes)
#         while hero == is_true:
#             hero = rand(heroes)
#         is_true = hero
#         print(f'Your class:{hero}')
#     elif choice == 0:
#         break
#     else:
#         print('Pls try again!!!\n')

# 4 task
# def rubik(kubik_0):
#     kubik_0 = int(input("1 to start game and 0 to quit\n"))
#     return kubik_0
# def kubik(kubik_1, kubik_2):
#     print("My turn:")
#     time.sleep(1)
#     kubik_1 = random.randint(1, 6)
#     print(kubik_1)
#     choice = input("Your turn:\n")
#     kubik_2 = random.randint(1, 6)
#     print(kubik_2)
#     return kubik_1, kubik_2

# Pc = 0
# Me = 0
# while True:
#     choice = 0
#     choice = rubik(choice)
#     if choice == 1:
#         Pc, Me = kubik(Pc, Me)
#         if Pc > Me:
#             print("You lose\n")
#         elif Me > Pc:
#             print("You win, congratulations!!!\n")
#         else:
#             print("Tie\n")
#     if choice == 0:
#         for i in range(5, 0, -1):
#             print(f"Exit from aaplication in {i}")
#             time.sleep(1)
#         break

# 5 task
# def fight(hp_hero, hp_monster, hero_damage, monster_damage, win_or_lose):
#     hero_attack = input("\nPress Enter to attack or 0 to escape: ")
#     if '0' in hero_attack:
#         print("\nYou trying to escape...\n")
#         time.sleep(1)
#         print("Monster running behind you...\n")
#         win_or_lose = random.randint(1, 2)
#         if win_or_lose == 2:
#             hp_monster = 0
#             time.sleep(1)
#             return hp_hero, hp_monster, hero_damage, monster_damage, win_or_lose
#         if win_or_lose == 1:
#             hp_hero = 0
#             time.sleep(1)
#             return hp_hero, hp_monster, hero_damage, monster_damage, win_or_lose
#     hero_damage = random.randint(1, 10)
#     hp_monster = hp_monster - hero_damage
#     print(f"\nYou damaged -{hero_damage}\n")
#     print(f'Monster hp is {hp_monster}\n')
#     time.sleep(1)
#     print('Monster is attacking, watch out!!!\n')
#     time.sleep(1)
#     monster_damage = random.randint(1, 10)
#     hp_hero = hp_hero - monster_damage
#     print(f"Monster damaged you -{monster_damage}\n")
#     time.sleep(1)
#     print(f'You have {hp_hero}\n')
    
#     return hp_hero, hp_monster, hero_damage, monster_damage, win_or_lose


# hero_damage = 0
# monster_damage = 0
# win_or_lose = 0
# while True:
#     choice = int(input("Press 1 to start game or 0 to escape fight and left the application:\n"))
#     hp_hero = 50
#     hp_monster = 50
#     if choice == 1:
#         while True:
#             hp_hero, hp_monster, hero_damage, monster_damage, win_or_lose = fight(
#                 hp_hero, 
#                 hp_monster, 
#                 hero_damage, 
#                 monster_damage,
#                 win_or_lose)
#             while True:
#                 if hp_hero <= 0 and win_or_lose == 0:
#                     print("You died\n")
                    
#                 elif hp_monster <= 0 and win_or_lose == 0:
#                     print("You killed Monster\n")
                    
#                 elif hp_hero == 0 and win_or_lose == 1:
#                     print("Monster catches up...\n")
#                     time.sleep(1)
#                     print('Monster killed you:(\n')
#                     time.sleep(1)
                    
#                 elif hp_monster == 0 and win_or_lose == 2:
#                     print("You escaped succesfully!!!\n")
#                     time.sleep(1)
#                 break
#             if hp_hero <= 0 or hp_monster <= 0:    
#                 break
#     elif choice == 0:
#         print("Exit in 5", end=", ", flush=True)
#         time.sleep(1)
#         for i in range(4, 1, -1):
#             print(i, end=", ", flush=True)
#             time.sleep(1)
#         print('1.\n')
#         break
# print('\nYou left the application.')
# 6 task
# def death(death_1, death_2):
#     if death_1 <= 0:
#         return death_1, death_2
#     if death_2 <=0:
#         return death_1, death_2
#     return None
# def upgrade(attack, hp):
#     while True:
#         lvl = int(input("Choose 1 to upgrade:\n1.Attack +5\n2.HP +10\n")) 
#         if lvl == 1:
#             attack += 5
#             print(f"Now your Attack = {attack}")
#             return attack, hp
#         elif lvl == 2:
#             hp += 10
#             print(f"Now your HP = {hp}")
#             return attack, hp
#         else:
#             print("Try Again\n")
#  def fight(attack_1, hp_1, attack_2, hp_2):
#      bonus_2 = attack_2 - 10
#      min_d_1 = 4 + bonus_2
#      max_d_1 = 6 + bonus_2 
#      bonus = attack_1 - 15
#      min_d = 5 + bonus
#      max_d = 10 + (bonus * 2)
#      hero_attack = input("\nPress Enter to attack:\n ")
#      attack_hero = random.randint(min_d, max_d)
#      hp_2 = hp_2 - attack_hero
#     print(f"-{attack_hero}\n")
#     time.sleep(1)
#     if death(hp_2, hp_1):
#         return attack_1, hp_1, attack_2, hp_2
#     print("Monster is attack\n")
#     attack_monster = random.randint(min_d_1, max_d_1)
#     hp_1 = hp_1 - attack_monster
#     time.sleep(1)
#     print(f"-{attack_monster}\n")
#     time.sleep(1)
#     if death(hp_2, hp_1):
#         return attack_1, hp_1, attack_2, hp_2
#     print(f"Monster hp {hp_2}")
#     print(f"Hero hp {hp_1}")
#     return attack_1, hp_1, attack_2, hp_2

# player = {
#     'lvl': 1,
#     'name': "Ruslan",
#     "attack": 15,
#     "hp": 100,
#     "max_hp": 100
# }

# # monster = {
#     'lvl': 1,
#     'name': "Monster",
#     "attack": 10,
#     "hp": 110,
#     "max_hp": 110
# }

# # while True:
#     player["attack"], player["hp"], monster["attack"], monster["hp"] = fight(
#         player["attack"],
#         player["hp"],
#         monster["attack"],
#         monster["hp"])
#     if monster["hp"] <= 0:
#         print("You killed Monster!\n")
#         print("You reached lvl 2!\n")
#         player["lvl"] += 1
#         break
#     if player["hp"] <= 0:
#         print("You died: ")
#         break
# # if player["lvl"] == 2:
#     while True:
#         player["attack"], player["max_hp"] = upgrade(player["attack"], player["max_hp"])
#         player["hp"] = player["max_hp"]
#         break
# # print(player)

# file
# 1 task
# write = input("Имя: ")
# with open("save.txt", "w") as file: 
#     file.write(write)

#  2 task
# with open("save.txt", "r") as file:
#     text = file.read()
# print(f"Hello, {text}!")

# 3 task
# with open("save.txt", "a") as file:
#     file.write("Programm Started\n")

# 4 task
# with open("save.txt", "r") as file:
#     scores = file.readlines()

# 5 task
# max = 0
# with open("save.txt", "a") as file:
#     for i in range(4):
#         write = input("Write:\n") 
#         file.write(f"{write}\n")

# with open("save.txt", "r") as file:
#     scores = file.readlines()
#     for i in scores:
#         max_2 = int(i)
#         if max < max_2:
#             max = max_2

# print(max)

# try/except

# # 1-2 task
# while True:
#     try:
#         number = int(input("Write a number: "))
#         break
#     except:
#         print("This in not number")

#  3 task
# while True:
#     try:
#         number_1 = int(input("First number:\n"))
#         number_2 = int(input("Second number:\n"))
#         solution = int(input("1. *\n2. /\n3. +\n4. -\n"))
#         if solution == 1:
#             number_3 = number_1 * number_2
#             print(number_3)
#         if solution == 2:
#             number_3 = number_1 / number_2
#             print(number_3)
#         if solution == 3:
#             number_3 = number_1 + number_2
#             print(number_3)
#         if solution == 4:
#             number_3 = number_1 - number_2
#             print(number_3) 
#         break
#     except ValueError:
#         print("Error")

#  Tuple

#  1 task
# stats = (100, 30, 10)
# for i in stats:
#     print(i)

# 2 task
# def player():
#     return 100, 15, 5
# hp, attack, armor = player()
# print(hp, attack, armor)

# 3 task
# skills = ("Fire", "Water", "Rock")

# if "Water" in skills:
#     print("Found")
        
#  set()
#  1 task

# items = {"Sword", "Shield", "Potion"}
# for item in items:
#     print(f"{item}\n")

# 2 task

# skills = {"Fire", "Heal"}
# print(skills)
# skills.add("Shield")
# for item in skills:
#     print(f"{item}\n")
# print(skills)

# 3 task

# skills = {"Fire", "Water", "Rock"}
# while True:
#     try:
#         skill = input()

#         if skill in skills:
#             print("Already Studied")
#         else:
#             skills.add(skill)
#             print("Ability added")
            
#         break    
#     except ValidError:
#         print("Error")
# print(skills)


# class Monster:
#     pass
# goblin = Monster()
# print(goblin)


# class Monster:

#     def __init__(self, hp, attack):
#         hp = 50
#         attack = 10
# goblin = Monster(55, 15)
# orc = Monster(100, 25)
# dragon = Monster(250, 50)

# 2 task

# def prologue():
#         print("December: 8:56, South Forest")
#         time.sleep(3)
#         print("A Hunter found you unconscious")
#         time.sleep(3)
#         print("Hey, who are you?\nHow did you end up here?")
#         time.sleep(3)
#         print("He didn't managed to finish it, an Ogr jumped out of the bushes and attacked!\n")

# def start_story():
#         while True:
#             try:
#                 skip = int(input("Do you want to skip Prologue:\n1.Skip\n2.No Skip\n"))
#                 if skip == 2:
#                     prologue()
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
#                self.start = int(input("1.Attack\n2.Heal\n0.Main Menu\n"))
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
#                           crit_chance
#                           ):
#         self.name = name
#         self.max_hp = max_hp
#         self.current_hp = current_hp
#         self.attack = attack
#         self.dodge = dodge
#         self.crit_chance = crit_chance
        

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


# class Enemy(Hero):
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

# class Warrior(Hero):
#     def __init__(self, name):
#         super().__init__(name, 13, 7, 3, 9, 5, 13, "Human", "Warrior")
#         self.kick_stun = 2
#         self.kick_cd = 0
#         self.crit_damage = 1.5

#         self.update_stats()
#     def victory_text(self):
#         print("You took a sword from Hunter and calmly cut off the ogr's head.\n")

# class Mage(Hero):
#     def __init__(self, name):
#         super().__init__(name, 3, 5, 18, 13, 4, 7, "Human", "Mage")
#         self.max_mana = 25 + self.will_power * 3
#         self.current_mana = self.max_mana
#         self.crit_damage = 0

#         self.update_stats()
#     def victory_text(self):
#         print("You banished the ogr to another dimension.\n")

# class Assasin(Hero):
#     def __init__(self, name):
#         super().__init__(name, 8, 17, 4, 6, 10, 5, "Human", "Assasin")
#         self.crit_damage = 2
#         self.update_stats()

#     def victory_text(self):
#         print("The Ogr died from numerous wounds bcz of knife you took from him.\n")

# class Tank(Hero):
#     def __init__(self, name):
#         super().__init__(name, 8, 3, 2, 9, 3, 25, "Human", "Tank")
#         self.crit_damage = 1.2
#         self.update_stats()

#     def victory_text(self):
#         print(".Ogr couldn't make any scratch on you and ran away\n")

# class Fight:

#     def crit(self, attacker, damage):
#         if random.randint(1, 100) <= attacker.crit_chance:
#             print("Crit Damage X2!")
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
#             heal.healer(hero)
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
        



# # classes = {
# #    1: {
# #        "name": name_Main,
# #        "max_hp": 115,
# #        "current_hp": 115,
# #        "attack": 15,
# #        "dodge": 15,
# #        "ignore_dodge": False,
# #        "crit_chance": 0,
# #        "crit_damage": 1.5,
# #        "Species": "Human",
# #        "class": "Warrior"
# #        },
# #     2: {
# #         "name": name_Main,
# #         "max_hp": 70,
# #         "current_hp": 70,
# #         "attack": 30,
# #         "dodge": 8,
# #         "ignore_dodge": True,
# #         "crit_chance": 0,
# #         "crit_damage": 1,
# #         "Species": "Human",
# #         "class": "Mage"
# #         },
# #     3: {
# #         "name": name_Main,
# #         "max_hp": 80,
# #         "current_hp": 80,
# #         "attack": 20,
# #         "dodge": 20,
# #         "ignore_dodge": False,
# #         "crit_chance": 10,
# #         "crit_damage": 2,
# #         "Species": "Human",
# #         "class": "Assasin"
# #         },
# #     4: {
# #         "name": name_Main,
# #         "max_hp": 150,
# #         "current_hp": 150,
# #         "attack": 10,
# #         "dodge": 5,
# #         "ignore_dodge": False,
# #         "crit_chance": 0,
# #         "crit_damage": 1.2,
# #         "Species": "Human",
# #         "class": "Tank"
# #         }
# # }

# # hero_data = classes[name_class_Main]

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
    

# # main_hero = Hero(
# #     hero_data["name"],
# #     hero_data["max_hp"],
# #     hero_data["current_hp"],
# #     hero_data["attack"],
# #     hero_data["dodge"],
# #     hero_data["ignore_dodge"],
# #     hero_data["crit_chance"],
# #     hero_data["crit_damage"],
# #     hero_data["Species"],
# #     hero_data["class"]
# # )

# small_ogr = Enemy("Small Ogr", 
#                   7, 
#                   5, 
#                   0, 
#                   5,
#                   3, 
#                   5,
#                   "Ogr",
#                   "Warrior")
# game = Game()
# fight = Fight()
# heal = Heal()
# print(main_hero.__dict__)
# while True:
#     game.choice_hero()  
#     if game.start_game == 1:
#         main_hero.current_hp = main_hero.max_hp
#         small_ogr.current_hp = small_ogr.max_hp
#         start_story()
#         while True:
#             game.cicle()
#             if game.start == 1:        
#                 print(f"{main_hero.name} is attacking\n")
#                 fight.attack_enemy(main_hero, small_ogr)
#                 if small_ogr.current_hp <= 0:
#                     print("You win!\n")
#                     break
                    
#                 print(f"{small_ogr.name} is attacking\n")
#                 fight.attack_enemy(small_ogr, main_hero)
#                 if main_hero.current_hp <= 0:
#                     print("You died...\n")
#                     break
#             elif game.start == 2:
#                 heal.limitation(main_hero)
#             elif game.start == 0:
#                 break

#             print(f"{main_hero.name} HP:{main_hero.current_hp}\n")
#             print(f"{small_ogr.name} HP:{small_ogr.current_hp}\n")
        
#     if game.start_game == 0:
#         break


class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value


b = BankAccount(500)

print(b.balance)

b.balance = -50

print(b.balance)

class Hero:
    @classmethod