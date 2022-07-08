"""Муравей Лэнгтона, (c) Sayfullin Ruslan.
Динамическое изображение клеточного автомата. Нажмите Ctrl+C для останова.
"""

import copy, random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Задаем константы:
WIDTH, HEIGHT = bext.size()
# В Windows нельзя вывести что-либо в последнем столбце без добавления
# автоматически символа новой строки, поэтому уменьшаем ширину на 1:
WIDTH -= 1
HEIGHT -= 1 # Учет сообщения о возможности выхода в самом низу.

NUMBER_OF_ANTS = 10 # (!) Попробуйте заменить это значение на 1 или 50.
PAUSE_AMOUNT = 0.1 # (!) Попробуйте заменить это значение на 1.0 или 0.0.

# (!) Попробуйте поменять их, чтобы изменить внешний вид муравьев:
ANT_UP = '^'
ANT_DOWN = 'v'
ANT_LEFT = '<'
ANT_RIGHT = '>'

# (!) Попробуйте заменить эти цвета на что-то из 'black', 'red',
# 'green', 'yellow', 'blue', 'purple', 'cyan', or 'white'.
# (Все поддерживаемые модулем bext цвета.)
ANT_COLOR = 'red'
BLACK_TILE = 'black'
WHITE_TILE = 'white'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

def main():
    bext.fg(ANT_COLOR) # Цвет муравьев совпадает с цветом переднего плана.
    bext.bg(WHITE_TILE) # Задаем для начала белый цвет фона.
    bext.clear()

    # Создаем новую структуру данных для доски:
    board = {'width': WIDTH, 'height': HEIGHT}
    # Создаем структуры данных для муравьев:
    ants = []
    for i in range(NUMBER_OF_ANTS):
        ant = {
            'x': random.randint(0, WIDTH - 1),
            'y': random.randint(0, HEIGHT - 1),
            'direction': random.choice([NORTH, SOUTH, EAST, WEST]),
        }
        ants.append(ant)

    # Отслеживаем поменявшие цвет клетки, которые нужно перерисовать
    # на экране:
    changedTiles = []

    while True: # Основной цикл программы.
        displayBoard(board, ants, changedTiles)
        changedTiles = []

        # nextBoard — то, как доска будет выглядеть на следующем шаге
        # моделирования. Начинаем с копии доски для текущего шага:
        nextBoard = copy.copy(board)

        # Выполняем один шаг моделирования для каждого муравья:
        for ant in ants:
            if board.get((ant['x'], ant['y']), False) == True:
                nextBoard[(ant['x'], ant['y'])] = False
                # Поворот по часовой стрелке:
                if ant['direction'] == NORTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = NORTH
            else:
                nextBoard[(ant['x'], ant['y'])] = True
            # Поворот против часовой стрелки:
            if ant['direction'] == NORTH:
                ant['direction'] = WEST
            elif ant['direction'] == WEST:
                ant['direction'] = SOUTH
            elif ant['direction'] == SOUTH:
                ant['direction'] = EAST
            elif ant['direction'] == EAST:
                ant['direction'] = NORTH
        changedTiles.append((ant['x'], ant['y']))

        # Передвигаем муравья вперед в направлении, в котором он "смотрит":
        if ant['direction'] == NORTH:
            ant['y'] -= 1
        if ant['direction'] == SOUTH:
            ant['y'] += 1
        if ant['direction'] == WEST:
            ant['x'] -= 1
        if ant['direction'] == EAST:
            ant['x'] += 1

        # Если муравей пересекает край экрана, необходимо
        # перенести его на другую сторону.
        ant['x'] = ant['x'] % WIDTH
        ant['y'] = ant['y'] % HEIGHT

        changedTiles.append((ant['x'], ant['y']))

    board = nextBoard

def displayBoard(board, ants, changedTiles):
    """Отображает доску и муравьев на экране. Аргумент changedTiles
    представляет собой список кортежей (x, y) для поменявшихся клеток
    на экране, которые необходимо перерисовать."""

    # Выводим на экран структуру данных для доски:
    for x, y in changedTiles:
        bext.goto(x, y)
        if board.get((x, y), False):
            bext.bg(BLACK_TILE)
        else:
            bext.bg(WHITE_TILE)

        antIsHere = False
        for ant in ants:
            if (x, y) == (ant['x'], ant['y']):
                antIsHere = True
                if ant['direction'] == NORTH:
                    print(ANT_UP, end='')
                elif ant['direction'] == SOUTH:
                    print(ANT_DOWN, end='')
                elif ant['direction'] == EAST:
                    print(ANT_LEFT, end='')
                elif ant['direction'] == WEST:
                    print(ANT_RIGHT, end='')
                break
        if not antIsHere:
            print(' ', end='')

    # Отображаем внизу экрана сообщение о возможности выхода:
    bext.goto(0, HEIGHT)
    bext.bg(WHITE_TILE)
    print('Press Ctrl-C to quit.', end='')

    sys.stdout.flush() # (Необходимо для использующих модуль bext программ.)
    time.sleep(PAUSE_AMOUNT)

# Если программа не импортируется, а запускается, выполняем запуск:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Langton's Ant, by Al Sweigart al@inventwithpython.com")
        sys.exit() # Если нажато Ctrl+C — завершаем программу.