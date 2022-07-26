"""Игра в 15, (c) Sayfullin Ruslan.
Расставьте пронумерованные костяшки в правильном порядке
"""

import random, sys
BLANK = ' '     # Обратите внимание: это строковое значение состоит из двух пробелов.


def main():
    print('''Sliding Tile Puzzle, by Sayfullin Ruslan
    Use the WASD keys to move the tiles
    back into their original order:
        1 2 3 4
        5 6 7 8
        9 10 11 12
        13 14 15
    ''')
    input('Press Enter to begin...')

    gameBoard = getNewPuzzle()

    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(gameBoard)
        makeMove(gameBoard, playerMove)

        if gameBoard == getNewBoard():
            print('You won!')
            sys.exit()


def getNewBoard():
    """Возвращает список списков, соответствующий новой игре."""
    return [['1 ', '5 ', '9 ', '13'], ['2 ', '6 ', '10', '14'],
        ['3 ', '7 ', '11', '15'], ['4 ', '8 ', '12', BLANK]]


def displayBoard(board):
    """Отображает заданную доску на экране."""
    labels = [board[0][0], board[1][0], board[2][0], board[3][0],
        board[0][1], board[1][1], board[2][1], board[3][1],
        board[0][2], board[1][2], board[2][2], board[3][2],
        board[0][3], board[1][3], board[2][3], board[3][3]]
    boardToDraw = """
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
""".format(*labels)
    print(boardToDraw)


def findBlankSpace(board):
    """Возвращает кортеж (x, y) с местоположением пустой клетки."""
    for x in range(4):
        for y in range(4):
            if board[x][y] == ' ':
                return (x, y)


def askForPlayerMove(board):
    """Запрашивает у игрока, какую костяшку передвигать."""
    blankx, blanky = findBlankSpace(board)

    w = 'W' if blanky != 3 else ' '
    a = 'A' if blanky != 3 else ' '
    s = 'S' if blanky != 0 else ' '
    d = 'D' if blanky != 0 else ' '

    while True:
        print('      ({})'.format(w))
        print('Enter WASD (or QUIT): ({}) ({}) ({})'.format(a, s, d))
        response = input('> ').upper()

        if response == 'QUIT':
            sys.exit()
        if response in (w + a + s + d).replace(' ', ''):
            return response


def makeMove(board, move):
    """Производит заданный ход move на заданной доске board."""
    # Примечание: эта функция предполагает, что ход допустим.
    bx, by = findBlankSpace(board)

    if move == 'W':
        board[bx][by], board[bx][by+1] = board[bx][by+1], board[bx][by]
    elif move == 'A':
        board[bx][by], board[bx+1][by] = board[bx+1][by], board[bx][by]
    elif move == 'S':
        board[bx][by], board[bx][by-1] = board[bx][by-1], board[bx][by]
    elif move == 'D':
        board[bx][by], board[bx-1][by] = board[bx-1][by], board[bx][by]


def makeRandomMove(board):
    """Передвигает костяшку случайным образом."""
    blankx, blanky = findBlankSpace(board)
    validMoves = []
    if blanky != 3:
        validMoves.append('W')
    if blankx != 3:
        validMoves.append('A')
    if blanky != 0:
        validMoves.append('S')
    if blankx != 0:
        validMoves.append('D')

    makeMove(board, random.choice(validMoves))


def getNewPuzzle(moves=200):
    """Генерируем новую игру с помощью случайных ходов из упорядоченного
    состояния."""
    board = getNewBoard()

    for i in range(moves):
        makeRandomMove(board)
    return board


# Если программа не импортируется, а запускается, выполняем запуск:
if __name__ == '__main__':
    main()
