"""Песочные часы, (c) Sayfullin Ruslan.
Динамическое изображение песочных часов. Нажмите Ctrl+C для останова.
"""

import random
import sys
import time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Задаем константы:
PAUSE_LENGTH = 0.2  # (!) Попробуйте заменить это значение на 0.0 или 1.0.
# (!) Попробуйте заменить это значение на любое число от 0 до 100:
WIDE_FALL_CHANCE = 50

SCREEN_WIDTH = 79
SCREEN_HEIGHT = 25
X = 0    # Индекс значений X в кортеже (x, y) – 0.
Y = 1   # Индекс значений Y в кортеже (x, y) – 1.
SAND = chr(9617)
WALL = chr(9608)
# Описываем стенки песочных часов:
HOURGLASS = set() # Кортежи (x, y) для стенок песочных часов.
# (!) Попробуйте закомментировать часть строк HOURGLASS.add(), чтобы стереть
# стенки песочных часов:
for i in range(18, 37):
    HOURGLASS.add((i, 1))           # Верхняя крышка песочных часов.
    HOURGLASS.add((i, 23))          # Нижняя крышка.
for i in range(1, 5):
    HOURGLASS.add((18, i))          # Верхняя левая прямая стенка.
    HOURGLASS.add((36, i))          # Верхняя правая прямая стенка.
    HOURGLASS.add((18, i + 19))     # Стенка внизу слева.
    HOURGLASS.add((36, i + 19))     # Стенка внизу справа.
for i in range(8):
    HOURGLASS.add((19 + i, 5 + i))  # Верхняя левая наклонная стенка.
    HOURGLASS.add((35 - i, 5 + i))  # Верхняя правая наклонная стенка.
    HOURGLASS.add((25 - i, 13 + i)) # Нижняя левая наклонная стенка.
    HOURGLASS.add((29 + i, 13 + i)) # Нижняя правая наклонная стенка.

# Начальная горка песка в верхней половине песочных часов:
INITIAL_SAND = set()
for y in range(8):
    for x in range(19 + y, 36 - y):
        INITIAL_SAND.add((x, y + 4))


def main():
    bext.fg('yellow')
    bext.clear()

    # Выводим сообщение о возможности выхода:
    bext.goto(0, 0)
    print('Ctrl-C to quit.', end='')
    # Отображаем стенки песочных часов:
    for wall in HOURGLASS:
        bext.goto(wall[X], wall[Y])
        print(WALL, end='')

    while True:     # Основной цикл программы.
        allSand = list(INITIAL_SAND)

        # Рисуем начальную горку песка:
        for sand in allSand:
            bext.goto(sand[X], sand[Y])
            print(SAND, end='')

        runHourglassSimulation(allSand)


def runHourglassSimulation(allSand):
    """Моделируем падение песка, пока он не прекратит двигаться.
    """
    while True:                     # Проходим в цикле, пока песок не закончится.
        random.shuffle(allSand)     # Случайный порядок песчинок.

        sandMovedOnThisStep = False
        for i, sand in enumerate(allSand):
            if sand[Y] == SCREEN_HEIGHT - 1:
                # Песок на дне, а значит, больше не будет двигаться:
                continue

            # Если под песчинкой пусто, перемещаем ее вниз:
            noSandBelow = (sand[X], sand[Y] + 1) not in allSand
            noWallBelow = (sand[X], sand[Y] + 1) not in HOURGLASS
            canFallDown = noSandBelow and noWallBelow

            if canFallDown:
                # Отрисовываем песчинку ниже на одну строку:
                bext.goto(sand[X], sand[Y])
                print(' ', end='') # Очищаем старое место ее расположения.
                bext.goto(sand[X], sand[Y] + 1)
                print(SAND, end='')

                # Песчинка ниже на одну строку:
                allSand[i] = (sand[X], sand[Y] + 1)
                sandMovedOnThisStep = True
            else:
                # Проверяем, может ли песчинка упасть влево:
                belowLeft = (sand[X] - 1, sand[Y] + 1)
                noSandBelowLeft = belowLeft not in allSand
                noWallBelowLeft = belowLeft not in HOURGLASS
                left = (sand[X] - 1, sand[Y])
                noWallLeft = left not in HOURGLASS
                notOnLeftEdge = sand[X] > 0
                canFallLeft = (noSandBelowLeft and noWallBelowLeft
                    and noWallLeft and notOnLeftEdge)

                # Проверяем, может ли песчинка упасть вправо:
                belowRight = (sand[X] + 1, sand[Y] + 1)
                noSandBelowRight = belowRight not in allSand
                noWallBelowRight = belowRight not in HOURGLASS
                right = (sand[X] + 1, sand[Y])
                noWallRight = right not in HOURGLASS
                notOnRightEdge = sand[X] < SCREEN_WIDTH - 1
                canFallRight = (noSandBelowRight and noWallBelowRight
                    and noWallRight and notOnRightEdge)

                # Задаем направление падения:
                fallingDirection = None
                if canFallLeft and not canFallRight:
                    fallingDirection = -1 # Задаем падение песка влево.
                elif not canFallLeft and canFallRight:
                    fallingDirection = 1 # Задаем падение песка вправо.
                elif canFallLeft and canFallRight:
                    # Возможны оба направления, так что выбираем случайным образом:
                    fallingDirection = random.choice((-1, 1))
                # Проверяем, может ли песчинка упасть "далеко",
                # на две позиции влево или вправо, вместо одной:
                if random.random() * 100 <= WIDE_FALL_CHANCE:
                    belowTwoLeft = (sand[X] - 2, sand[Y] + 1)
                    noSandBelowTwoLeft = belowTwoLeft not in allSand
                    noWallBelowTwoLeft = belowTwoLeft not in HOURGLASS
                    notOnSecondToLeftEdge = sand[X] > 1
                    canFallTwoLeft = (canFallLeft and noSandBelowTwoLeft
                        and noWallBelowTwoLeft and notOnSecondToLeftEdge)

                    belowTwoRight = (sand[X] + 2, sand[Y] + 1)
                    noSandBelowTwoRight = belowTwoRight not in allSand
                    noWallBelowTwoRight = belowTwoRight not in HOURGLASS
                    notOnSecondToRightEdge = sand[X] < SCREEN_WIDTH - 2
                    canFallTwoRight = (canFallRight
                        and noSandBelowTwoRight and noWallBelowTwoRight
                        and notOnSecondToRightEdge)

                    if canFallTwoLeft and not canFallTwoRight:
                        fallingDirection = -2
                    elif not canFallTwoLeft and canFallTwoRight:
                        fallingDirection = 2
                    elif canFallTwoLeft and canFallTwoRight:
                        fallingDirection = random.choice((-2, 2))

                if fallingDirection == None:
                    # Эта песчинка никуда упасть не может, переходим к следующей.
                    continue
                # Отрисовываем песчинку на новом месте:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')  # Затираем старую песчинку.
                bext.goto(sand[X] + fallingDirection, sand[Y] + 1)
                print(SAND, end='')  # Отрисовываем новую песчинку.

                # Перемещаем песчинку на новое место:
                allSand[i] = (sand[X] + fallingDirection, sand[Y] + 1)
                sandMovedOnThisStep = True

        sys.stdout.flush()          # (Необходимо для использующих bext программ.)
        time.sleep(PAUSE_LENGTH)    # Пауза

        # Если на этом шаге песок вообще не двигался, обнуляем песочные часы:
        if not sandMovedOnThisStep:
            time.sleep(2)
            # Вытираем весь песок:
            for sand in allSand:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')
            break   # Выходим из основного цикла моделирования.


# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()   # Если нажато Ctrl+C — завершаем программу.
