"""Манкала, (c) Sayfullin Ruslan.
    Древняя игра в зерна
"""

import sys

# Кортежи лунок игроков:
PLAYER_1_PITS = ('A', 'B', 'C', 'D', 'E', 'F')
PLAYER_2_PITS = ('G', 'H', 'I', 'J', 'K', 'L')
# Ассоциативный массив, ключами которого служат лунки, а значениями —
# противоположные им лунки:
OPPOSITE_PIT = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K',
                'F': 'L', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D',
                'K': 'E', 'L': 'F'}
# Ассоциативный массив, ключами которого служат лунки, а значениями —
# следующие по порядку лунки:
NEXT_PIT = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': '1',
            '1': 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G',
            'G': '2', '2': 'A'}

# Метки всех лунок в порядке против часовой стрелки, начиная с A:
PIT_LABELS = 'ABCDEF1LKJIHG2'

# Количество зерен в каждой из лунок в начале новой игры:
STARTING_NUMBER_OF_SEEDS = 4    # (!) Попробуйте заменить это значение на 1 или 10


def main():
    print('''Mancala, by Sayfullin Ruslan
        The ancient two-player seed-sowing game. Grab the seeds from a pit on
        your side and place one in each following pit, going counterclockwise
        and skipping your opponent's store. If your last seed lands in an empty
        pit of yours, move the opposite pit's seeds into that pit. The
        goal is to get the most seeds in your store on the side of the board.
        If the last placed seed is in your store, you get a free turn.
        The game ends when all of one player's pits are empty. The other player
        claims the remaining seeds for their store, and the winner is the one
        with the most seeds.
        More info at https://en.wikipedia.org/wiki/Mancala
        ''')
    input('Press Enter to begin...')

    gameBoard = getNewBoard()
    playerTurn = '1'    # Сначала ходит игрок 1.

    while True:     # Обрабатываем ход одного из игроков.
        # Очищаем экран, выводя множество символов новой строки,
        # чтобы убрать с него старую доску.
        print('\n' * 60)
        # Отображаем доску и получаем ход игрока:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(playerTurn, gameBoard)

        # Осуществляем ход игрока:
        playerTurn = makeMove(gameBoard, playerTurn, playerMove)

        # Проверяем, не закончилась ли игра и не выиграл ли игрок:
        winner = checkForWinner(gameBoard)
        if winner == '1' or winner == '2':
            displayBoard(gameBoard)  # Отображаем доску последний раз.
            print('Player ' + winner + ' has won!')
            sys.exit()
        elif winner == 'tie':
            displayBoard(gameBoard)     # Отображаем доску последний раз.
            print('There is a tie!')
            sys.exit()


def getNewBoard():
    """Возвращает ассоциативный массив, соответствующий доске "Манкалы"
    в начальном состоянии: четыре зерна в каждой лунке и ноль в амбарах."""

    # Синтаксический сахар — используем сокращенное имя переменной:
    s = STARTING_NUMBER_OF_SEEDS

    # Создаем структуру данных для доски с 0 зерен в амбарах
    # и начальным количеством зерен в лунках:
    return {'1': 0, '2': 0, 'A': s, 'B': s, 'C': s, 'D': s, 'E': s,
            'F': s, 'G': s, 'H': s, 'I': s, 'J': s, 'K': s, 'L': s}


def displayBoard(board):
        """Отображает доску в виде ASCII-графики на основе
        ассоциативного массива board."""

        seedAmounts = []
        # Это строковое значение 'GHIJKL21ABCDEF' описывает порядок
        # лунок слева направо и сверху вниз:
        for pit in 'GHIJKL21ABCDEF':
            numSeedsInThisPit = str(board[pit]).rjust(2)
            seedAmounts.append(numSeedsInThisPit)
        print("""
        +------+------+--<<<<<-Player 2----+------+------+------+
        2      |G     |H     |I     |J     |K     |L     |      1
               | {}   | {}   | {}   | {}   | {}   | {}   |
        S      |      |      |      |      |      |      |      S
        T  {}  +------+------+------+------+------+------+  {}  T
        O      |A     |B     |C     |D     |E     |F     |      O
        R      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      R
        E      |      |      |      |      |      |      |      E
        +------+------+------+-Player 1->>>>>-----+------+------+   
           """.format(*seedAmounts))


def askForPlayerMove(playerTurn, board):
    """Спрашиваем игрока, из какой лунки на его стороне доски
    он хочет сеять зерна. Возвращаем метку выбранной лунки в верхнем
    регистре в виде строкового значения."""

    while True:  # Продолжаем спрашивать игрока, пока он не введет допустимый ход.
        # Просим игрока ввести лунку на его стороне:
        if playerTurn == '1':
            print('Player 1, choose move: A-F (or QUIT)')
        elif playerTurn == '2':
            print('Player 2, choose move: G-L (or QUIT)')
        response = input('> ').upper().strip()

        # Проверяем, не хочет ли игрок выйти из игры:
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # Проверяем, выбрана ли допустимая лунка:
        if (playerTurn == '1' and response not in PLAYER_1_PITS) or (
            playerTurn == '2' and response not in PLAYER_2_PITS
        ):
            print('Please pick a letter on your side of the board.')
            continue # Снова просим игрока сделать ход.
        if board.get(response) == 0:
            print('Please pick a non-empty pit.')
            continue # Снова просим игрока сделать ход.
        return response


def makeMove(board, playerTurn, pit):
    """Модифицирует структуру данных board в соответствии с выбором
    игроком 1 или 2 при его ходе лунки — источника засеиваемых зерен.
    Возвращает '1' or '2' в зависимости от того, чей ход следующий."""

    seedsToSow = board[pit]     # Получаем количество зерен в выбранной лунке.
    board[pit] = 0   # Опустошаем выбранную лунку.

    while seedsToSow > 0:   # Сеем, пока зерна не закончатся.
        pit = NEXT_PIT[pit]     # Переходим к следующей лунке.
        if (playerTurn == '1' and pit == '2') or (
            playerTurn == '2' and pit == '1'
        ):
            continue    # Пропускаем амбар противника.
        board[pit] += 1
        seedsToSow -= 1

    # Если последнее зерно попало в амбар текущего игрока, он ходит снова.
    if (pit == playerTurn == '1') or (pit == playerTurn == '2'):
        # Последнее зерно попало в амбар текущего игрока; он ходит еще раз.
        return playerTurn
    # Проверяем, попало ли последнее зерно в пустую лунку; в этом случае
    # захватываем зерна из противоположной лунки.
    if playerTurn == '1' and pit in PLAYER_1_PITS and board[pit] == 1:
        oppositePit = OPPOSITE_PIT[pit]
        board['1'] += board[oppositePit]
        board[oppositePit] = 0
    elif playerTurn == '2' and pit in PLAYER_2_PITS and board[pit] == 1:
        oppositePit = OPPOSITE_PIT[pit]
        board['2'] += board[oppositePit]
        board[oppositePit] = 0

    # Возвращаем номер другого игрока как следующего:
    if playerTurn == '1':
        return '2'
    elif playerTurn == '2':
        return '1'


def checkForWinner(board):
    """Изучаем доску и возвращаем '1' или '2', если один из игроков
    победил, либо 'tie' или 'no winner', если нет. Игра заканчивается,
    когда все лунки одного игрока пусты; второй игрок забирает все
    оставшиеся зерна в свой амбар. Победитель — тот, у кого больше зерен."""

    player1Total = board['A'] + board['B'] + board['C']
    player1Total += board['D'] + board['E'] + board['F']
    player2Total = board['G'] + board['H'] + board['I']
    player2Total += board['J'] + board['K'] + board['L']

    if player1Total == 0:
        # Игрок 2 получает все оставшиеся зерна на стороне противника:
        board['2'] += player2Total
        for pit in PLAYER_2_PITS:
            board[pit] = 0  # Обнуляем все лунки.
    elif player2Total == 0:
        # Игрок 1 получает все оставшиеся зерна на стороне противника:
        board['1'] += player1Total
        for pit in PLAYER_1_PITS:
            board[pit] = 0  # Обнуляем все лунки.
    else:
        return 'no winner'   # Никто пока не выиграл.

    # Игра закончена, ищем игрока с максимальным счетом.
    if board['1'] > board['2']:
        return '1'
    elif board['2'] > board['1']:
        return '2'
    else:
        return 'tie'


# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    main()

