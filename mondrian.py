"""Генератор картин в стиле Мондриана, (c) Sayfullin Ruslan.
Генерирует случайным образом картины в стиле Пита Мондриана.
"""

import sys, random

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Задаем константы:
MIN_X_INCREASE = 6
MAX_X_INCREASE = 16
MIN_Y_INCREASE = 3
MAX_Y_INCREASE = 6
WHITE = 'white'
BLACK = 'black'
RED = 'red'
YELLOW = 'yellow'
BLUE = 'blue'

# Настройки экрана:
width, height = bext.size()
# В Windows нельзя вывести что-либо в последнем столбце без добавления
# автоматически символа новой строки, поэтому уменьшаем ширину на 1:
width -= 1

height -= 3

while True: # Основной цикл приложения.
    # Заполняем сначала холст белым фоном:
    canvas = {}
    for x in range(width):
        for y in range(height):
            canvas[(x, y)] = WHITE

    # Генерируем вертикальные отрезки:
    numberOfSegmentsToDelete = 0
    x = random.randint(MIN_X_INCREASE, MAX_X_INCREASE)
    while x < width - MIN_X_INCREASE:
        numberOfSegmentsToDelete += 1
        for y in range(height):
            canvas[(x, y)] = BLACK
        x += random.randint(MIN_X_INCREASE, MAX_X_INCREASE)

    # Генерируем горизонтальные отрезки:
    y = random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)
    while y < height - MIN_Y_INCREASE:
        numberOfSegmentsToDelete += 1
        for x in range(width):
            canvas[(x, y)] = BLACK
        y += random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)

    numberOfRectanglesToPaint = numberOfSegmentsToDelete - 3
    numberOfSegmentsToDelete = int(numberOfSegmentsToDelete * 1.5)

    # Выбираем сегменты случайным образом и пытаемся их удалить.
    for i in range(numberOfSegmentsToDelete):
        while True: # Продолжаем выбирать сегменты для удаления.
            # Выбираем случайную начальную точку сегмента:
            startx = random.randint(1, width - 2)
            starty = random.randint(1, height - 2)
            if canvas[(startx, starty)] == WHITE:
                continue

            # Определяем, сегмент вертикальный или горизонтальный:
            if (canvas[(startx - 1, starty)] == WHITE and
                canvas[(startx + 1, starty)] == WHITE):
                orientation = 'vertical'
            elif (canvas[(startx, starty - 1)] == WHITE and
                canvas[(startx, starty + 1)] == WHITE):
                orientation = 'horizontal'
            else:
                # Начальная точка находится на пересечении,
                # так что нужно выбрать новую:
                continue

            pointsToDelete = [(startx, starty)]

            canDeleteSegment = True
            if orientation == 'vertical':
                # Поднимаемся на один участок от начальной точки
                # и смотрим, можно ли удалить этот сегмент:
                for changey in (-1, 1):
                    y = starty
                    while 0 < y < height - 1:
                        y += changey
                        if (canvas[(startx - 1, y)] == BLACK and
                            canvas[(startx + 1, y)] == BLACK):
                            # Наткнулись на четырехстороннее пересечение.
                            break
                        elif ((canvas[(startx - 1, y)] == WHITE and
                            canvas[(startx + 1, y)] == BLACK) or
                            (canvas[(startx - 1, y)] == BLACK and
                            canvas[(startx + 1, y)] == WHITE)):
                            # Наткнулись на T-образное пересечение;
                            # удалить этот сегмент нельзя:
                            canDeleteSegment = False
                            break
                        else:
                            pointsToDelete.append((startx, y))

            elif orientation == 'horizontal':
                # Поднимаемся на один участок от начальной точки
                # и смотрим, можно ли удалить этот сегмент:
                for changex in (-1, 1):
                    x = startx
                    while 0 < x < width - 1:
                        x += changex
                        if (canvas[(x, starty - 1)] == BLACK and
                            canvas[(x, starty + 1)] == BLACK):
                            # Наткнулись на четырехстороннее пересечение.
                            break
                        elif ((canvas[(x, starty - 1)] == WHITE and
                            canvas[(x, starty + 1)] == BLACK) or
                            (canvas[(x, starty - 1)] == BLACK and
                            canvas[(x, starty + 1)] == WHITE)):
                            # Наткнулись на T-образное пересечение;
                            # удалить этот сегмент нельзя:
                            canDeleteSegment = False
                            break
                        else:
                            pointsToDelete.append((x, starty))

            if not canDeleteSegment:
                continue # Выбираем новую случайную начальную точку.
            break # Переходим к удалению данного сегмента.

        # Если сегмент можно удалить, закрашиваем все точки белым:
        for x, y in pointsToDelete:
            canvas[(x, y)] = WHITE

    # Добавляем граничные линии:
    for x in range(width):
        canvas[(x, 0)] = BLACK # Верхняя граница.
        canvas[(x, height - 1)] = BLACK # Нижняя граница.
    for y in range(height):
        canvas[(0, y)] = BLACK # Левая граница.
        canvas[(width - 1, y)] = BLACK # Правая граница.

    # Рисуем прямоугольники:
    for i in range(numberOfRectanglesToPaint):
        while True:
            startx = random.randint(1, width - 2)
            starty = random.randint(1, height - 2)
            if canvas[(startx, starty)] != WHITE:
                continue # Выбираем новую случайную начальную точку.
            else:
                break

        # Алгоритм заливки:
        colorToPaint = random.choice([RED, YELLOW, BLUE, BLACK])
        pointsToPaint = set([(startx, starty)])
        while len(pointsToPaint) > 0:
            x, y = pointsToPaint.pop()
            canvas[(x, y)] = colorToPaint
            if canvas[(x - 1, y)] == WHITE:
                pointsToPaint.add((x - 1, y))
            if canvas[(x + 1, y)] == WHITE:
                pointsToPaint.add((x + 1, y))
            if canvas[(x, y - 1)] == WHITE:
                pointsToPaint.add((x, y - 1))
            if canvas[(x, y + 1)] == WHITE:
                pointsToPaint.add((x, y + 1))

    # Рисуем на экране структуру данных canvas:
    for y in range(height):
        for x in range(width):
            bext.bg(canvas[(x, y)])
            print(' ', end='')

        print()

    # Спрашиваем пользователя, нарисовать ли еще одну картину:
    try:
        input('Press Enter for another work of art, or Ctrl-C to quit.')
    except KeyboardInterrupt:
        sys.exit()