"""Вращающийся куб, (c) Sayfullin Ruslan.
Динамическое изображение вращающегося куба. Нажмите Ctrl+C для останова.
"""

# Эту программу следует запускать в окне терминала/командной оболочки.

import math, time, sys, os

# Задаем константы:
PAUSE_AMOUNT = 0.1   # Пауза на 1/10 секунды.
WIDTH, HEIGHT = 80, 24
SCALEX = (WIDTH - 4) // 8
SCALEY = (HEIGHT - 4) // 8
# Высота текстовых ячеек в два раза превышает ширину,
# так что задаем масштаб по оси y:
SCALEY *= 2
TRANSLATEX = (WIDTH - 4) // 2
TRANSLATEY = (HEIGHT - 4) // 2

# (!) Попробуйте заменить это значение на '#', или '*',
# или еще какой-либо символ:
LINE_CHAR = chr(9608)   # Символ 9608 — '█'

# (!) Попробуйте обнулить два из этих значений, чтобы вращать куб
# относительно только одной оси координат:
X_ROTATE_SPEED = 0.03
Y_ROTATE_SPEED = 0.08
Z_ROTATE_SPEED = 0.13

# Координаты XYZ данная программа хранит в списках, координату X —
# по индексу 0, Y — 1, а Z — 2. Эти константы повышают удобочитаемость
# кода при обращении к координатам в этих списках.
X = 0
Y = 1
Z = 2

def line(x1, y1, x2, y2):
    """Возвращает список точек, лежащих на прямой между заданными точками.
    Использует алгоритм Брезенхэма. Подробнее — в статье на
    https://ru.wikipedia.org/wiki/Алгоритм_Брезенхэма"""
    points = [] # Содержит точки прямой.
    # "Steep" означает, что уклон прямой больше 45 градусов
    # или меньше –45 градусов:

    # Проверяем на предмет частного случая, когда начальная и конечная точки
    # являются в определенном смысле соседними, что данная функция не умеет
    # хорошо обрабатывать, поэтому возвращаем заранее подготовленный список:
    if (x1 == x2 and y1 == y2 + 1) or (y1 == y2 and x1 == x2 + 1):
        return [(x1, y1), (x2, y2)]

    isSteep = abs(y2 - y1) > abs(x2 - x1)
    if isSteep:
        # Этот алгоритм умеет работать только с некрутыми прямыми,
        # так что делаем уклон не таким крутым, а потом возвращаем обратно.
        x1, y1 = y1, x1     # Меняем местами x1 и y1
        x2, y2 = y2, x2     # Меняем местами x2 и y2
    isReversed = x1 > x2    # True, если прямая идет справа налево.
    if isReversed:          # Получаем точки на прямой, идущей справа налево.
        x1, x2 = x2, x1     # Меняем местами x1 и x2
        y1, y2 = y2, y1     # Меняем местами y1 и y2

        deltax = x2 - x1
        deltay = abs(y2 - y1)
        extray = int(deltax / 2)
        currenty = y2
        if y1 < y2:
            ydirection = 1
        else:
            ydirection = -1
        # Вычисляем y для каждого x в этой прямой:
        for currentx in range(x2, x1 - 1, -1):
            if isSteep:
                points.append((currenty, currentx))
            else:
                points.append((currentx, currenty))
            extray -= deltay
            if extray <= 0:     # Меняем y, только если extray <= 0.
                currenty -= ydirection
                extray += deltax
    else: # Получаем точки на прямой, идущей слева направо.
        deltax = x2 - x1
        deltay = abs(y2 - y1)
        extray = int(deltax / 2)
        currenty = y1
        if y1 < y2:
            ydirection = 1
        else:
            ydirection = -1
        # Вычисляем y для каждого x в этой прямой:
        for currentx in range(x1, x2 + 1):
            if isSteep:
                points.append((currenty, currentx))
            else:
                points.append((currentx, currenty))
            extray -= deltay
            if extray < 0: # Меняем y, только если extray < 0.
                currenty += ydirection
                extray += deltax
        return points


def rotatePoint(x, y, z, ax, ay, az):
    """Возвращает кортеж (x, y, z) из повернутых аргументов x, y, z.

    Вращение на углы ax, ay, az (в радианах) относительно начала
    координат 0, 0, 0.
        Направления осей координат:
        -y
        |
        +-- +x
        /
        +z
    """

    # Вращаем относительно оси x:
    rotatedX = x
    rotatedY = (y * math.cos(ax)) - (z * math.sin(ax))
    rotatedZ = (y * math.sin(ax)) + (z * math.cos(ax))
    x, y, z = rotatedX, rotatedY, rotatedZ

    # Вращаем относительно оси y:
    rotatedX = (z * math.sin(ay)) + (x * math.cos(ay))
    rotatedY = y
    rotatedZ = (z * math.cos(ay)) - (x * math.sin(ay))
    x, y, z = rotatedX, rotatedY, rotatedZ

    # Вращаем относительно оси z:
    rotatedX = (x * math.cos(az)) - (y * math.sin(az))
    rotatedY = (x * math.sin(az)) + (y * math.cos(az))
    rotatedZ = z
    return (rotatedX, rotatedY, rotatedZ)


def adjustPoint(point):
    """Преобразуем трехмерную точку XYZ в двумерную точку XY, подходящую для
    отображения на экране. Для этого масштабируем данную двумерную точку
    на SCALEX и SCALEY, а затем сдвигаем ее на TRANSLATEX и TRANSLATEY."""
    return (int(point[X] * SCALEX + TRANSLATEX),
        int(point[Y] * SCALEY + TRANSLATEY))

"""В CUBE_CORNERS хранятся координаты XYZ углов куба.
Индексы всех углов в CUBE_CORNERS отмечены на следующей схеме:
      0---1
     /|  /|
     2---3|
     |4- |-5
     |/  |/
     6---7"""

CUBE_CORNERS = [[-1, -1, -1], # Точка 0
                [ 1, -1, -1], # Точка 1
                [-1, -1, 1], # Точка 2
                [ 1, -1, 1], # Точка 3
                [-1, 1, -1], # Точка 4
                [ 1, 1, -1], # Точка 5
                [-1, 1, 1], # Точка 6
                [ 1, 1, 1]] # Точка 7
# В rotatedCorners хранятся координаты XYZ из CUBE_CORNERS
# после вращения на rx, ry и rz:
rotatedCorners = [None, None, None, None, None, None, None, None]
# Вращение для каждой оси:
xRotation = 0.0
yRotation = 0.0
zRotation = 0.0

try:
    while True: # Основной цикл программы.
        # Вращение куба относительно различных осей на различный угол:
        xRotation += X_ROTATE_SPEED
        yRotation += Y_ROTATE_SPEED
        zRotation += Z_ROTATE_SPEED
        for i in range(len(CUBE_CORNERS)):
            x = CUBE_CORNERS[i][X]
            y = CUBE_CORNERS[i][Y]
            z = CUBE_CORNERS[i][Z]
            rotatedCorners[i] = rotatePoint(x, y, z, xRotation,
            yRotation, zRotation)

        # Получаем точки линий куба:
        cubePoints = []
        for fromCornerIndex, toCornerIndex in ((0, 1), (1, 3), (3, 2),
        (2, 0), (0, 4), (1, 5), (2, 6), (3, 7), (4, 5), (5, 7), (7, 6),
        (6, 4)):
            fromX, fromY = adjustPoint(rotatedCorners[fromCornerIndex])
            toX, toY = adjustPoint(rotatedCorners[toCornerIndex])
            pointsOnLine = line(fromX, fromY, toX, toY)
            cubePoints.extend(pointsOnLine)

        # Избавляемся от дублирующихся точек:
        cubePoints = tuple(frozenset(cubePoints))

        # Отображаем куб на экране:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) in cubePoints:
                    # Отображаем полный блок:
                    print(LINE_CHAR, end='', flush=False)
                else:
                    # Отображаем пустое пространство:
                    print(' ', end='', flush=False)
            print(flush=False)
        print('Press Ctrl-C to quit.', end='', flush=True)

        time.sleep(PAUSE_AMOUNT)    # Небольшая пауза.

        # Очищаем экран:
        if sys.platform == 'win32':
            os.system('cls')    # В Windows для этого служит команда cls.
        else:
            os.system('clear')   # В macOS и Linux – команда clear.

except KeyboardInterrupt:
    print('Rotating Cube, by Sayfullin Ruslan.')
    sys.exit()   # Если нажато сочетание клавиш Ctrl+C — завершаем программу.
