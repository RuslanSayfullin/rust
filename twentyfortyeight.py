"""Игра «2048», (c) Sayfullin Ruslan aka CryptoLis.
Игра, в которой при сдвиге "плиток" объединяются числа, растущие
в геометрической прогрессии. На основе игры "2048" Габриэле Чирулли —
клона игры "1024" от Veewo Studios, которая является клоном игры Threes!
Подробнее — в статье https://ru.wikipedia.org/wiki/2048_(игра)
"""

import random, sys

# Задаем константы:
BLANK = ''  # Значение, соответствующее пустой клетке на доске.

def main():
    print('''Twenty Forty-Eight, by Sayfullin Ruslan
        Slide all the tiles on the board in one of four directions. Tiles with
        like numbers will combine into larger-numbered tiles. A new 2 tile is
        added to the board on each move. You win if you can create a 2048 tile.
        You lose if the board fills up the tiles before then.''')

    input('Press Enter to begin...')
    gameBoard = getNewBoard()

    while True:     # Основной цикл программы.
        drawBoard(gameBoard)
        print('Score:', getScore(gameBoard))
        playerMove = askForPlayerMove()
        gameBoard = makeMove(gameBoard, playerMove)
        addTwoToBoard(gameBoard)

        if isFull(gameBoard):
            drawBoard(gameBoard)
            print('Game Over - Thanks for playing!')
            sys.exit()


def getNewBoard():
    """Возвращает новую структуру данных для доски,
    которая представляет собой ассоциативный массив, ключи которого —
    кортежи (x, y), а значения находятся в соответствующих клетках.
    Эти значения равны либо числам — степеням двойки, либо BLANK.
    Система координат выглядит вот так:
    X0 1 2 3
        Y+-+-+-+-+
        0| | | | |
         +-+-+-+-+
        1| | | | |
         +-+-+-+-+
        2| | | | |
         +-+-+-+-+
        3| | | | |
         +-+-+-+-+"""


    newBoard = {} # Содержит возвращаемую структуру данных доски.
    # Проходим по всем клеткам доски, устанавливая "плиткам" значение BLANK:
    for x in range(4):
        for y in range(4):
            newBoard[(x, y)] = BLANK

    # Выбираем две случайные клетки для двух начальных двоек:
    startingTwosPlaced = 0          # Число выбранных изначально клеток.
    while startingTwosPlaced < 2:   # Повторяем, чтобы продублировать клетки.
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        # Проверяем, что случайно выбранная клетка еще не занята:
        if newBoard[randomSpace] == BLANK:
            newBoard[randomSpace] = 2
            startingTwosPlaced = startingTwosPlaced + 1
            return newBoard


def drawBoard(board):
    """Отрисовываем структуру данных для доски на экране."""

    # Проходим по всем возможным клеткам слева направо, сверху вниз
    # и создаем список меток всех клеток.
    labels = []     # Список строковых значений для числа/BLANK данной "плитки".
    for y in range(4):
        for x in range(4):
            tile = board[(x, y)]    # Получаем значение "плитки" в этой клетке.
            # Убеждаемся, что длина метки равна 5:
            labelForThisTile = str(tile).center(5)
            labels.append(labelForThisTile)

    # {} заменяются метками соответствующих "плиток":
    print("""
    +-----+-----+-----+-----+
    |     |     |     |     |
    |{}|{}|{}|{}|
    |     |     |     |     |
    +-----+-----+-----+-----+
    |     |     |     |     |
    |{}|{}|{}|{}|
    |     |     |     |     |
    +-----+-----+-----+-----+
    |     |     |     |     |
    |{}|{}|{}|{}|
    |     |     |     |     |
    +-----+-----+-----+-----+
    |     |     |     |     |
    |{}|{}|{}|{}|
    |     |     |     |     |
    +-----+-----+-----+-----+
    """.format(*labels))


def getScore(board):
    """Возвращает сумму всех "плиток" в структуре данных для доски."""
    score = 0
    # Проходим в цикле по всем клеткам, прибавляя "плитки" к score:
    for x in range(4):
        for y in range(4):
            # Прибавляем к score только непустые "плитки":
            if board[(x, y)] != BLANK:
                score = score + board[(x, y)]
    return score


def combineTilesInColumn(column):
    """column представляет собой список из четырех "плиток". Индекс 0
    соответствует низу столбца column, а сила тяжести тянет "плитки" вниз,
    в случае равных значений они объединяются. Например, combineTilesInCo
    lumn([2, BLANK, 2, BLANK]) возвращает [4, BLANK, BLANK, BLANK]."""

    # Копируем в combinedTiles только числа (не BLANK) из column
    combinedTiles = [] # Список непустых "плиток" в column.
    for i in range(4):
        if column[i] != BLANK:
            combinedTiles.append(column[i])
    # Продолжаем присоединять к списку значения BLANK, пока не получится
    # четыре "плитки":
    while len(combinedTiles) < 4:
        combinedTiles.append(BLANK)

    # Объединяем числа, если число сверху — такое же, и удваиваем.
    for i in range(3):  # Пропускаем индекс 3: это верхняя клетка.
        if combinedTiles[i] == combinedTiles[i + 1]:
            combinedTiles[i] *= 2   # Удваиваем число на "плитке".
            # Сдвигаем расположенные вверху "плитки" на одну клетку:
            for aboveIndex in range(i + 1, 3):
                combinedTiles[aboveIndex] = combinedTiles[aboveIndex + 1]
            combinedTiles[3] = BLANK    # Самая верхняя клетка — всегда пустая.
    return combinedTiles


def makeMove(board, move):
    """Производит ход на доске.
    Аргумент move — 'W', 'A', 'S' или 'D'. Функция возвращает
    получившуюся структуру данных для доски (board)."""
    # board разбивается на четыре столбца, различные
    # в зависимости от направления хода:
    if move == 'W':
        allColumnsSpaces = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                            [(1, 0), (1, 1), (1, 2), (1, 3)],
                            [(2, 0), (2, 1), (2, 2), (2, 3)],
                            [(3, 0), (3, 1), (3, 2), (3, 3)]]
    elif move == 'A':
        allColumnsSpaces = [[(0, 0), (1, 0), (2, 0), (3, 0)],
                            [(0, 1), (1, 1), (2, 1), (3, 1)],
                            [(0, 2), (1, 2), (2, 2), (3, 2)],
                            [(0, 3), (1, 3), (2, 3), (3, 3)]]
    elif move == 'S':
        allColumnsSpaces = [[(0, 3), (0, 2), (0, 1), (0, 0)],
                            [(1, 3), (1, 2), (1, 1), (1, 0)],
                            [(2, 3), (2, 2), (2, 1), (2, 0)],
                            [(3, 3), (3, 2), (3, 1), (3, 0)]]
    elif move == 'D':
        allColumnsSpaces = [[(3, 0), (2, 0), (1, 0), (0, 0)],
                            [(3, 1), (2, 1), (1, 1), (0, 1)],
                            [(3, 2), (2, 2), (1, 2), (0, 2)],
                            [(3, 3), (2, 3), (1, 3), (0, 3)]]
    # Структура данных board после выполнения хода:
    boardAfterMove = {}
    for columnSpaces in allColumnsSpaces:   # Проходим в цикле по всем четырем столбцам.
        # Получаем "плитки" для этого столбца (первая "плитка"
        # соответствует "низу" столбца):
        firstTileSpace = columnSpaces[0]
        secondTileSpace = columnSpaces[1]
        thirdTileSpace = columnSpaces[2]
        fourthTileSpace = columnSpaces[3]
        firstTile = board[firstTileSpace]
        secondTile = board[secondTileSpace]
        thirdTile = board[thirdTileSpace]
        fourthTile = board[fourthTileSpace]
        # Формируем столбец и объединяем "плитки" в нем:
        column = [firstTile, secondTile, thirdTile, fourthTile]
        combinedTilesColumn = combineTilesInColumn(column)
        # Формируем новую структуру данных для доски
        # с объединенными "плитками":
        boardAfterMove[firstTileSpace] = combinedTilesColumn[0]
        boardAfterMove[secondTileSpace] = combinedTilesColumn[1]
        boardAfterMove[thirdTileSpace] = combinedTilesColumn[2]
        boardAfterMove[fourthTileSpace] = combinedTilesColumn[3]

    return boardAfterMove


def askForPlayerMove():
    """Просим игрока указать направление следующего хода (или выйти).
    Проверяем ход на допустимость: 'W', 'A', 'S' или 'D'."""
    print('Enter move: (WASD or Q to quit)')
    while True:     # Выполняем цикл, пока не будет введен допустимый ход.
        move = input('> ').upper()
        if move == 'Q':
            # Завершаем программу:
            print('Thanks for playing!')
            sys.exit()

        # Возвращаем допустимый ход или выполняем еще итерацию и спрашиваем снова:
        if move in ('W', 'A', 'S', 'D'):
            return move
        else:
            print('Enter one of "W", "A", "S", "D", or "Q".')


def addTwoToBoard(board):
    """Добавляет на доску две случайные новые "плитки"."""
    while True:
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        if board[randomSpace] == BLANK:
            board[randomSpace] = 2
            return   # Выполняем возврат из функции после обнаружения непустой "плитки".


def isFull(board):
    """Возвращает True, если в структуре данных для доски нет пустых клеток."""
    # Проходим в цикле по всем клеткам доски:
    for x in range(4):
        for y in range(4):
            # Если клетка пуста, возвращаем False:
            if board[(x, y)] == BLANK:
                return False
    return True     # Пустых клеток нет, возвращаем True.


# Если программа не импортируется, а запускается, выполняем запуск игры:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Если нажато Ctrl+C — завершаем программу.




