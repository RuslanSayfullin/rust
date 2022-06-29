"""Заливка, Sayfullin Ruslan.
Многоцветная игра, в которой нужно заполнить игральную доску одним цветом.
Включает специальный режим для игроков с дальтонизмом.
По мотивам игры Flood It!
"""

import random
import sys


try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Задаем константы:
BOARD_WIDTH = 16        # (!) Попробуйте заменить это значение на 4 или 40.
BOARD_HEIGHT = 14       # (!) Попробуйте заменить это значение на 4 или 20.
MOVES_PER_GAME = 20     # (!) Попробуйте заменить это значение на 3 или 300.

# Константы для различных фигур, используемых в режиме для дальтоников:
HEART        = chr(9829)    # Символ 9829 — '♥'.
DIAMOND     = chr(9830)     # Символ 9830 — '♦'.
SPADE       = chr(9824)     # Символ 9824 — '♠'.
CLUB        = chr(9827)     # Символ 9827 — '♣'.
BALL        = chr(9679)     # Символ 9679 — '•'.
TRIANGLE    = chr(9650)     # Символ 9650 — '▲'.

BLOCK       = chr(9608)     # Символ 9608 — '█'
LEFTRIGHT   = chr(9472)     # Символ 9472 — '─'
UPDOWN      = chr(9474)     # Символ 9474 — '│'
DOWNRIGHT   = chr(9484)     # Символ 9484 — '┌'
DOWNLEFT    = chr(9488)     # Символ 9488 — '┐'
UPRIGHT     = chr(9492)     # Символ 9492 — '└'
UPLEFT      = chr(9496)     # Символ 9496 — '┘'
# Список кодов chr() можно найти на https://inventwithpython.com/chr

# Все цвета/формы элементов, используемые на доске:
TILE_TYPES = (0, 1, 2, 3, 4, 5)
COLORS_MAP = {0: 'red', 1: 'green', 2:'blue',
                 3:'yellow', 4:'cyan', 5:'purple'}
COLOR_MODE = 'color mode'
SHAPES_MAP = {0: HEART, 1: TRIANGLE, 2: DIAMOND,
                3: BALL, 4: CLUB, 5: SPADE}
SHAPE_MODE = 'shape mode'


def main():
    bext.bg('black')
    bext.fg('white')
    bext.clear()
    print('''Flooder, by Sayfullin Ruslan.
        Set the upper left color/shape, which fills in all the
        adjacent squares of that color/shape. Try to make the
        entire board the same color/shape.''')

    print('Do you want to play in colorblind mode? Y/N')
    response = input('> ')
    if response.upper().startswith('Y'):
        displayMode = SHAPE_MODE
    else:
        displayMode = COLOR_MODE

    gameBoard = getNewBoard()
    movesLeft = MOVES_PER_GAME

    while True: # Основной цикл игры.
        displayBoard(gameBoard, displayMode)

        print('Moves left:', movesLeft)
        playerMove = askForPlayerMove(displayMode)
        changeTile(playerMove, gameBoard, 0, 0)
        movesLeft -= 1

        if hasWon(gameBoard):
            displayBoard(gameBoard, displayMode)
            print('You have won!')
            break
        elif movesLeft == 0:
            displayBoard(gameBoard, displayMode)
            print('You have run out of moves!')
            break


def getNewBoard():
    """Возвращает ассоциативный массив с новой доской "Заливки"."""

    # Роль ключей играют кортежи (x, y), а значений — клетки
    # на соответствующих позициях.
    board = {}

    # Генерируем случайные цвета для игральной доски.
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = random.choice(TILE_TYPES)

    # Делаем несколько элементов такими же, как соседний.
    # В результате получаются группы элементов одинакового цвета/формы.
    for i in range(BOARD_WIDTH * BOARD_HEIGHT):
        x = random.randint(0, BOARD_WIDTH - 2)
        y = random.randint(0, BOARD_HEIGHT - 1)
        board[(x + 1, y)] = board[(x, y)]
    return board


def displayBoard(board, displayMode):
    """Выводит игральную доску на экран."""
    bext.fg('white')
    # Отображает верхний край доски:
    print(DOWNRIGHT + (LEFTRIGHT * BOARD_WIDTH) + DOWNLEFT)

    # Выводим отдельные строки:
    for y in range(BOARD_HEIGHT):
        bext.fg('white')
        if y == 0: # Первая строка начинается с '>'.
            print('>', end='')
        else: # Последующие строки начинаются с белой вертикальной линии.
            print(UPDOWN, end='')

        # Выводим все клетки данной строки:
        for x in range(BOARD_WIDTH):
            bext.fg(COLORS_MAP[board[(x, y)]])
            if displayMode == COLOR_MODE:
                print(BLOCK, end='')
            elif displayMode == SHAPE_MODE:
                print(SHAPES_MAP[board[(x, y)]], end='')

        bext.fg('white')
        print(UPDOWN) # Строки заканчиваются белой вертикальной линией.
    # Выводим нижний край игральной доски:
    print(UPRIGHT + (LEFTRIGHT * BOARD_WIDTH) + UPLEFT)


def askForPlayerMove(displayMode):
    """Даем возможность игроку выбрать цвет верхнего левого элемента."""
    while True:
        bext.fg('white')
        print('Choose one of ', end='')
        if displayMode == COLOR_MODE:
            bext.fg('red')
            print('(R)ed ', end='')
            bext.fg('green')
            print('(G)reen ', end='')
            bext.fg('blue')
            print('(B)lue ', end='')
            bext.fg('yellow')
            print('(Y)ellow ', end='')
            bext.fg('cyan')
            print('(C)yan ', end='')
            bext.fg('purple')
            print('(P)urple ', end='')
        elif displayMode == SHAPE_MODE:
            bext.fg('red')
            print('(H)eart, ', end='')
            bext.fg('green')
            print('(T)riangle, ', end='')
            bext.fg('blue')
            print('(D)iamond, ', end='')
            bext.fg('yellow')
            print('(B)all, ', end='')
            bext.fg('cyan')
            print('(C)lub, ', end='')
            bext.fg('purple')
            print('(S)pade, ', end='')
        bext.fg('white')
        print('or QUIT:')
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if displayMode == COLOR_MODE and response in tuple('RGBYCP'):
            # Возвращаем номер типа элемента в зависимости от response:
            return {'R': 0, 'G': 1, 'B': 2, 'Y': 3, 'C': 4, 'P': 5}[response]
        if displayMode == SHAPE_MODE and response in tuple('HTDBCS'):
            # Возвращаем номер типа элемента в зависимости от response:
            return {'H': 0, 'T': 1, 'D':2, 'B': 3, 'C': 4, 'S': 5}[response]


def changeTile(tileType, board, x, y, charToChange=None):
    """Меняем цвет/форму клетки с помощью алгоритма рекурсивной заливки."""
    if x == 0 and y == 0:
        charToChange = board[(x, y)]
        if tileType == charToChange:
            return # Простейший случай: тот же самый элемент.
    board[(x, y)] = tileType

    if x > 0 and board[(x - 1, y)] == charToChange:
        # Рекурсивно: меняем левый соседний элемент:
        changeTile(tileType, board, x - 1, y, charToChange)
    if y > 0 and board[(x, y - 1)] == charToChange:
        # Рекурсивно: меняем верхний соседний элемент:
        changeTile(tileType, board, x, y - 1, charToChange)
    if x < BOARD_WIDTH - 1 and board[(x + 1, y)] == charToChange:
        # Рекурсивно: меняем правый соседний элемент:
        changeTile(tileType, board, x + 1, y, charToChange)
    if y < BOARD_HEIGHT - 1 and board[(x, y + 1)] == charToChange:
        # Рекурсивно: меняем нижний соседний элемент:
        changeTile(tileType, board, x, y + 1, charToChange)


def hasWon(board):
    """Возвращает True, если вся доска — одного цвета/формы."""
    tile = board[(0, 0)]

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[(x, y)] != tile:
                return False
    return True


# Если программа не импортируется, а запускается, выполняем запуск:
if __name__ == '__main__':
    main()

