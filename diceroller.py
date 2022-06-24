"""Выбрасыватель игральных костей,
Моделирует выбрасывание костей, в нотации Dungeons & Dragons
"""

import random, sys

print('''Dice Roller, by Sayfullin Ruslan

Enter what kind and how many dice to roll. The format is the number of
dice, followed by "d", followed by the number of sides the dice have.
You can also add a plus or minus adjustment.


Examples:
    3d6 rolls three 6-sided dice
    1d10+2 rolls one 10-sided die, and adds 2
    2d38-1 rolls two 38-sided die, and subtracts 1
    QUIT quits the program
''')

while True:     # Основной цикл программы:
    try:
        diceStr = input('> ')   # Приглашение ввести описание игральных костей.
        if diceStr.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # Очищаем строку описания игральных костей:
        diceStr = diceStr.lower().replace(' ', '')

        # Ищем "d" в строке описания игральных костей:
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Missing the "d" character.')

        # Выясняем количество костей. ("3" в "3d6+1"):
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Missing the number of dice.')
        numberOfDice = int(numberOfDice)

        # Выясняем, присутствует ли модификатор в виде знака плюс или минус:
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')

        # Выясняем количество граней ("6" в "3d6+1"):
        if modIndex == -1:
            numberOfSides = diceStr[dIndex + 1:]
        else:
            numberOfSides = diceStr[dIndex + 1: modIndex]
        if not numberOfSides.isdecimal():
            raise Exception('Missing the number of sides.')
        numberOfSides = int(numberOfSides)

        # Выясняем числовое значение модификатора (The "1" in "3d6+1"):
        if modIndex == -1:
            modAmount = 0
        else:
            modAmount = int(diceStr[modIndex + 1:])
            if diceStr[modIndex] == '-':
                # Меняем числовое значение модификатора на отрицательное:
                modAmount = -modAmount

        # Моделируем бросок игральных костей:
        rolls = []
        for i in range(numberOfDice):
            rollResult = random.randint(1, numberOfSides)
            rolls.append(rollResult)

        # Отображаем итоговую сумму очков:
        print('Total:', sum(rolls) + modAmount, '(Each die:', end='')

        # Отображаем отдельные броски:
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        # Отображаем числовое значение модификатора:
        if modAmount != 0:
            modSign = diceStr[modIndex]
            print(', {}{}'.format(modSign, abs(modAmount)), end='')
        print(')')

    except Exception as exc:
        # Перехватываем все исключения и отображаем сообщение пользователю:
        print('Invalid input. Enter something like "3d6" or "1d10+2".')
        print('Input was invalid because: ' + str(exc))
        continue  # Возвращаемся к приглашению ввести описание игральных костей.
