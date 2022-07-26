"""Бега улиток, (c) Sayfullin Ruslan.
Бега быстроногих улиток!
"""

import random, time, sys

# Задаем константы:
MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40    # (!) Попробуйте изменить это число.

print('''Snail Race, by Sayfullin Ruslan

    @v <-- snail
    
''')


# Спрашиваем, сколько улиток должно участвовать в бегах:
while True: # Спрашиваем снова, пока игрок не введет число.
    print('How many snails will race? Max:', MAX_NUM_SNAILS)
    response = input('> ')
    if response.isdecimal():
        numSnailsRacing = int(response)
        if 1 < numSnailsRacing <= MAX_NUM_SNAILS:
            break
    print('Enter a number between 2 and', MAX_NUM_SNAILS)


# Ввод имен всех улиток:
snailNames = []     # Список имен улиток в виде строковых значений.
for i in range(1, numSnailsRacing + 1):
    while True:     # Продолжаем спрашивать, пока игрок не введет допустимое имя.
        print('Enter snail #' + str(i) + "'s name:")
        name = input('> ')
        if len(name) == 0:
            print('Please enter a name.')
        elif name in snailNames:
            print('Choose a name that has not already been used.')
        else:
            break    # Введено приемлемое имя.
    snailNames.append(name)


# Отображаем всех улиток на старте.
print('\n' * 40)
print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
print('|' + (' ' * (FINISH_LINE - len('|')) + '|'))
snailProgress = {}
for snailName in snailNames:
    print(snailName[:MAX_NAME_LENGTH])
    print('@v')
    snailProgress[snailName] = 0

time.sleep(1.5)     # Пауза перед началом гонок.

while True: # Основной цикл программы.
    # Выбираем случайным образом, каких улиток двигать вперед:
    for i in range(random.randint(1, numSnailsRacing // 2)):
        randomSnailName = random.choice(snailNames)
        snailProgress[randomSnailName] += 1

        # Проверяем, не достигла ли улитка финишной прямой:
        if snailProgress[randomSnailName] == FINISH_LINE:
            print(randomSnailName, 'has won!')
            sys.exit()

    # (!) Эксперимент: добавьте небольшой жульнический трюк:
    # увеличение скорости улитки, которую зовут так же, как вас.

    time.sleep(0.5)     # (!) Эксперимент: попробуйте изменить это значение.

    # (!) Эксперимент: что будет, если закомментировать эту строку?
    print('\n' * 40)

    # Отображает стартовую и финишную прямые:
    print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
    print('|' + (' ' * (FINISH_LINE - 1) + '|'))

    # Отображает улиток (с метками имен):
    for snailName in snailNames:
        spaces = snailProgress[snailName]
        print((' ' * spaces) + snailName[:MAX_NAME_LENGTH])
        print(('.' * snailProgress[snailName]) + '@v')
