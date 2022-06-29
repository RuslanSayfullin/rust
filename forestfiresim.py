"""Моделирование лесных пожаров, (c) Sayfullin Ruslan.
Имитационное моделирование распространения лесных пожаров. Нажмите Ctrl+C
для останова.
По мотивам программы Emoji Sim Ники Кейс http://ncase.me/simulating/model/
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
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = 'W'
EMPTY = ' '

# (!) Попробуйте заменить эти параметры на что-либо в диапазоне от 0.0 до 1.0:
INITIAL_TREE_DENSITY = 0.20 # Начальное заполнение леса деревьями.
GROW_CHANCE = 0.01 # Вероятность превращения пустого места в дерево.
FIRE_CHANCE = 0.01 # Вероятность попадания в дерево молнии и его сгорания.

# (!) Попробуйте задать длительность паузы равной 1.0 или 0.0:
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True: # Основной цикл программы.
        displayForest(forest)

        # Отдельный шаг моделирования:
        nextForest = {'width': forest['width'], 'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # Если значение nextForest[(x, y)] уже было задано
                    # на предыдущей итерации, ничего не делаем:
                    continue
                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Выращиваем дерево на данном пустом участке.
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Молния поджигает это дерево.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # Это дерево горит.
                    # Проходим в цикле по всем соседним участкам:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Огонь перекидывается на соседние деревья:
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # Дерево сгорело, стираем его:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Просто копируем существующий объект:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Возвращает ассоциативный массив в качестве новой структуры данных для леса."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE   # Начинается с дерева.
            else:
                forest[(x, y)] = EMPTY  # Начинается с пустого места.
    return forest


def displayForest(forest):
    """Отображает структуру данных для леса на экране."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset') # Используем цвет шрифта по умолчанию.
    print('Grow chance: {}% '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}% '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# Если программа не импортируется, а запускается, выполняем запуск:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Если нажато сочетание клавиш Ctrl+C — завершаем программу.
