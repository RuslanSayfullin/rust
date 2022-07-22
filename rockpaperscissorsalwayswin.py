""" Камень, ножницы, бумага (беспроигрышная версия), (c) Sayfullin Ruslan.
Классическая азартная игра на руках, в которой вы всегда выигрываете
"""

import time, sys

print('''Rock, Paper, Scissors, by Sayfullin Ruslan.
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
''')

# Переменная для отслеживания количества выигрышей.
wins = 0

while True:     # Основной цикл программы.
    while True: # Запрашиваем, пока игрок не введет R, P, S или Q.
        print('{} Wins, 0 Losses, 0 Ties'.format(wins))
        print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
            break
        else:
            print('Type one of R, P, S, or Q.')

    # Отображаем на экране выбранный игроком ход:
    if playerMove == 'R':
        print('ROCK versus...')
    elif playerMove == 'P':
        print('PAPER versus...')
    elif playerMove == 'S':
        print('SCISSORS versus...')

    # Считаем до трех с драматическими паузами:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # Отображаем на экране выбранный компьютером ход:
    if playerMove == 'R':
        print('SCISSORS')
    elif playerMove == 'P':
        print('ROCK')
    elif playerMove == 'S':
        print('PAPER')

    time.sleep(0.5)

    print('You win!')
    wins = wins + 1
