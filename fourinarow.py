"""Четыре в ряд, (c) Sayfullin Ruslan.
Игра с отбрасыванием игровых элементов, требующая выстроить
четыре в ряд, аналогично игре Connect Four
"""

import sys

# Константы, необходимые для отображения доски:
EMPTY_SPACE = '.' # Точки считать проще, чем пробелы.
PLAYER_X = 'X'
PLAYER_O = 'O'

# Не забудьте поменять displayBoard() & COLUMN_LABELS, если меняете BOARD_WIDTH.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')
assert len(COLUMN_LABELS) == BOARD_WIDTH


def main():
    print("""Four in a Row, by Al Sayfullin Ruslan
        Two players take turns dropping tiles into one of seven columns, trying
        to make four in a row horizontally, vertically, or diagonally.
        """)

    # Начинаем новую игру:
    gameBoard = getNewBoard()
    playerTurn = PLAYER_X

    while True: # Очередь играть одного из игроков.
        # Отображаем доску и даем игроку возможность сделать ход:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn
        # Проверяем, выиграл ли игрок или не достигнута ли ничья:
        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard) # Отображаем доску один последний раз.
            print('Player ' + playerTurn + ' has won!')
            sys.exit()
        elif isFull(gameBoard):
            displayBoard(gameBoard) # Отображаем доску один последний раз.
            print('There is a tie!')
            sys.exit()

        # Переход хода к другому игроку:
        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O
        elif playerTurn == PLAYER_O:
            playerTurn = PLAYER_X


def getNewBoard():
    """Возвращает ассоциативный массив, соответствующий игральной доске
    для Connect Four.
    Ключами служат кортежи (columnIndex, rowIndex) из двух целых чисел,
    а значениями — одно из строковых значений 'X', 'O' или '.' (пустое
    место)."""

    board = {}
    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT):
            board[(columnIndex, rowIndex)] = EMPTY_SPACE
    return board


def displayBoard(board):
    """Отображает доску и все клетки на экране."""

    '''Подготовка списка для передачи в строковый метод format()
    для шаблона доски. В этом списке хранятся все клетки доски
    (и пустые участки) слева направо, сверху вниз:'''
    tileChars = []
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            tileChars.append(board[(columnIndex, rowIndex)])

    # Отображаем доску:
    print("""
    1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+""".format(*tileChars))


def askForPlayerMove(playerTile, board):
    """Даем возможность игроку выбрать столбец на доске
    для размещения элемента.
    Возвращает кортеж (столбец, строка), в который попадет элемент."""
    while True: # Запрашиваем игрока, пока не будет сделан допустимый ход.
        print('Player {}, enter a column or QUIT:'.format(playerTile))
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response not in COLUMN_LABELS:
            print('Enter a number from 1 to {}.'.format(BOARD_WIDTH))
            continue # Снова спрашиваем у игрока ход.

        columnIndex = int(response) - 1 # -1 for 0-based the index.

        # Если столбец заполнен, снова запрашиваем ход:
        if board[(columnIndex, 0)] != EMPTY_SPACE:
            print('That column is full, select another one.')
            continue # Снова спрашиваем у игрока ход.

        # Начиная снизу, ищем первый пустой участок.
        for rowIndex in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return (columnIndex, rowIndex)


def isFull(board):
    """Возвращает True, если в `board` нет пустых участков,
    в противном случае возвращает False."""
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return False # Нашли пустой участок и возвращаем False.
    return True # Все участки заполнены.


def isWinner(playerTile, board):
    """Возвращает True, если `playerTile` содержит в одной строке
    на `board` четыре элемента в ряд, иначе возвращает False."""

    # Проходим по всей доске в поисках четырех в ряд:
    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT):
            # Ищем горизонтальные четыре в ряд, двигаясь вправо:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex)]
            tile3 = board[(columnIndex + 2, rowIndex)]
            tile4 = board[(columnIndex + 3, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # Ищем вертикальные четыре в ряд, двигаясь вниз:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex + 1)]
            tile3 = board[(columnIndex, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # Ищем четыре в ряд, двигаясь вправо вниз по диагонали:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex + 1)]
            tile3 = board[(columnIndex + 2, rowIndex + 2)]
            tile4 = board[(columnIndex + 3, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

            # Ищем четыре в ряд, двигаясь влево вниз по диагонали:
            tile1 = board[(columnIndex + 3, rowIndex)]
            tile2 = board[(columnIndex + 2, rowIndex + 1)]
            tile3 = board[(columnIndex + 1, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    return False


# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    main()
