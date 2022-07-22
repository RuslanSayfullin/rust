"""Камень, ножницы, бумага, (c) Sayfullin Ruslan.
Классическая азартная игра на руках
"""

import random, time, sys

print('''Rock, Paper, Scissors, by , Sayfullin Ruslan.
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
''')

# Переменные для отслеживания количества выигрышей, проигрышей и ничьих.
wins = 0
losses = 0
ties = 0


while True:         # Основной цикл игры.
    while True:     # Запрашиваем, пока игрок не введет R, P, S или Q.
        print('{} Wins, {} Losses, {} Ties'.format(wins, losses, ties))
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
        playerMove = 'ROCK'
    elif playerMove == 'P':
        print('PAPER versus...')
        playerMove = 'PAPER'
    elif playerMove == 'S':
        print('SCISSORS versus...')
        playerMove = 'SCISSORS'

    # Считаем до трех с драматическими паузами:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # Отображаем на экране выбранный компьютером ход:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'ROCK'
    elif randomNumber == 2:
        computerMove = 'PAPER'
    elif randomNumber == 3:
        computerMove = 'SCISSORS'
    print(computerMove)
    time.sleep(0.5)

    # Отображаем и фиксируем победу/поражение/ничью:
    if playerMove == computerMove:
        print('It\'s a tie!')
        ties = ties + 1
    elif playerMove == 'ROCK' and computerMove == 'SCISSORS':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'PAPER' and computerMove == 'ROCK':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'SCISSORS' and computerMove == 'PAPER':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'ROCK' and computerMove == 'PAPER':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'PAPER' and computerMove == 'SCISSORS':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'SCISSORS' and computerMove == 'ROCK':
        print('You lose!')
        losses = losses + 1
