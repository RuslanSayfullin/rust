"""Проблема Монти Холла, (c) Sayfullin Ruslan.
Моделирование задачи телевизионной игры Монти Холла
Подробнее — в статье https://ru.wikipedia.org/wiki/Парадокс_Монти_Холла
"""

import random, sys

ALL_CLOSED = """
+------+ +------+ +------+
|      | |      | |      |
|    1 | |    2 | |    3 |
|      | |      | |      |
|      | |      | |      |
|      | |      | |      |
+------+ +------+ +------+"""

FIRST_GOAT = """
+------+ +------+ +------+
|  ((  | |      | |      | 
|  oo  | |    2 | |    3 |
| /_/|_| |      | |      |  
|    | | |      | |      |
|GOAT||| |      | |      |
+------+ +------+ +------+"""

SECOND_GOAT = """
+------+ +------+ +------+
|      | |  ((  | |      |
|    1 | |  oo  | |  3   |
|      | | /_/|_| |      |
|      | |    | | |      |
|      | |GOAT||| |      |
+------+ +------+ +------+"""

THIRD_GOAT = """
+------+ +------+ +------+
|      | |      | |  ((  |
|    1 | |    2 | |  oo  |
|      | |      | | /_/|_|
|      | |      | |    | |
|      | |      | |GOAT|||
+------+ +------+ +------+"""

FIRST_CAR_OTHERS_GOAT = """
+------+ +------+ +------+
| CAR! | |  ((  | |  ((  |
|    __| |  oo  | |  oo  |
|  _/ || | /_/|_| | /_/|_|
| /_ __| |    | | |    | |
|   O  | |GOAT||| |GOAT|||
+------+ +------+ +------+"""

SECOND_CAR_OTHERS_GOAT = """
+------+ +------+ +------+
|  ((  | | CAR! | |  ((  |
|  oo  | |    __| |  oo  |
| /_/|_| | _/   | | /_/|_|
|    | | |/_ __ | |    | |
|GOAT||| | O    | |GOAT|||
+------+ +------+ +------+"""

THIRD_CAR_OTHERS_GOAT = """
+------+ +------+ +------+
|  ((  | |  ((  | | CAR! |
|  oo  | |  oo  | |    __|
| /_/|_| | /_/|_| |  _/  |
|    | | |    | | | /_ __|
|GOAT||| |GOAT||| |    O |
+------+ +------+ +------+"""

print('''The Monty Hall Problem, by , (c) Sayfullin Ruslan.
    In the Monty Hall game show, you can pick one of three doors. One door
    has a new car for a prize. The other two doors have worthless goats:
    {}
    Say you pick Door #1.
    Before the door you choose is opened, another door with a goat is opened:
    {}
    You can choose to either open the door you originally picked or swap
    to the other unopened door.
    It may seem like it doesn't matter if you swap or not, but your odds
    do improve if you swap doors! This program demonstrates the Monty Hall
    problem by letting you do repeated experiments.
    You can read an explanation of why swapping is better at
    https://en.wikipedia.org/wiki/Monty_Hall_problem
'''.format(ALL_CLOSED, THIRD_GOAT))

input('Press Enter to start...')

swapWins = 0
swapLosses = 0
stayWins = 0
stayLosses = 0
while True: # Основной цикл программы.
    # Компьютер выбирает, за какой дверью будет автомобиль:
    doorThatHasCar = random.randint(1, 3)
    # Просим игрока выбрать дверь:
    print(ALL_CLOSED)
    while True: # Продолжаем спрашивать, пока игрок не выберет допустимую дверь.
        print('Pick a door 1, 2, or 3 (or "quit" to stop):')
        response = input('> ').upper()
        if response == 'QUIT':
            # Завершаем игру.
            print('Thanks for playing!')
            sys.exit()

        if response == '1' or response == '2' or response == '3':
            break
    doorPick = int(response)

    # Выбираем, какую дверь с козой открыть:
    while True:
        # Выбираем одну из дверей с козой, не выбранную игроком:
        showGoatDoor = random.randint(1, 3)
        if showGoatDoor != doorPick and showGoatDoor != doorThatHasCar:
            break

    # Открываем эту дверь с козой:
    if showGoatDoor == 1:
        print(FIRST_GOAT)
    elif showGoatDoor == 2:
        print(SECOND_GOAT)
    elif showGoatDoor == 3:
        print(THIRD_GOAT)

    print('Door {} contains a goat!'.format(showGoatDoor))

    # Спрашиваем игрока, хочет ли он изменить свое решение:
    while True: # Продолжаем спрашивать, пока игрок не введет Y или N.
        print('Do you want to swap doors? Y/N')
        swap = input('> ').upper()
        if swap == 'Y' or swap == 'N':
            break

    # Меняем дверь, если игрок решил изменить свой выбор:
    if swap == 'Y':
        if doorPick == 1 and showGoatDoor == 2:
            doorPick = 3
        elif doorPick == 1 and showGoatDoor == 3:
            doorPick = 2
        elif doorPick == 2 and showGoatDoor == 1:
            doorPick = 3
        elif doorPick == 2 and showGoatDoor == 3:
            doorPick = 1
        elif doorPick == 3 and showGoatDoor == 1:
            doorPick = 2
        elif doorPick == 3 and showGoatDoor == 2:
            doorPick = 1

    # Открываем все двери:
    if doorThatHasCar == 1:
        print(FIRST_CAR_OTHERS_GOAT)
    elif doorThatHasCar == 2:
        print(SECOND_CAR_OTHERS_GOAT)
    elif doorThatHasCar == 3:
        print(THIRD_CAR_OTHERS_GOAT)

    print('Door {} has the car!'.format(doorThatHasCar))

    # Фиксируем количество побед и неудач при изменении и неизменении решения:
    if doorPick == doorThatHasCar:
        print('You won!')
        if swap == 'Y':
            swapWins += 1
        elif swap == 'N':
            stayWins += 1
    else:
        print('Sorry, you lost.')
        if swap == 'Y':
            swapLosses += 1
        elif swap == 'N':
            stayLosses += 1

    # Вычисляем частоту выигрыша при изменении и неизменении решения:
    totalSwaps = swapWins + swapLosses
    if totalSwaps != 0: # Защищаемся от деления на ноль.
        swapSuccess = round(swapWins / totalSwaps * 100, 1)
    else:
        swapSuccess = 0.0

    totalStays = stayWins + stayLosses
    if (stayWins + stayLosses) != 0:    # Защищаемся от деления на ноль.
        staySuccess = round(stayWins / totalStays * 100, 1)
    else:
        staySuccess = 0.0

    print()
    print('Swapping: ', end='')
    print('{} wins, {} losses, '.format(swapWins, swapLosses), end='')
    print('success rate {}%'.format(swapSuccess))
    print('Not swapping: ', end='')
    print('{} wins, {} losses, '.format(stayWins, stayLosses), end='')
    print('success rate {}%'.format(staySuccess))
    print()
    input('Press Enter to repeat the experiment...')
