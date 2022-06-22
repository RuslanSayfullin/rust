"""Чо-хан,
Традиционная японская игра в кости типа чет-нечет.
"""

import random
import sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}
print('''Cho-Han,

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')

purse = 5000
while True:     # Основной цикл игры.
    # Делайте ставки, господа:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # Допустимая ставка.
            pot = int(pot)  # Преобразуем pot в тип integer.
            break   # Выходим из цикла после размещения допустимой ставки.

    # Бросаем кости.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print(' CHO (even) or HAN (odd)?')

    # Спрашиваем у игрока, на что он ставит: на чо или на хан:
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Открываем результаты броска костей:
    print('The dealer lifts the cup to reveal:')
    print(' ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print(' ', dice1, '-', dice2)
    # Определяем, выиграл ли игрок:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Отображаем результаты ставок:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot     # Прибавляем приз к кошельку.
        print('The house collects a', pot // 10, 'mon fee.')
        purse = purse - (pot // 10)  # Сбор игрального дома 10%.
    else:
        purse = purse - pot     # Вычитаем ставку из кошелька.
        print('You lost!')
    # Проверяем, не закончились ли у игрока деньги:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
