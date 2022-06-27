"""Гравировщик, Sayfullin Ruslan
Графическая программа, рисующая непрерывную линию на экране с помощью
клавиш WASD. Создана под влиянием игры "Волшебный экран".
Например, нарисовать фрактальную кривую Гильберта можно с помощью:
SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW

Или даже еще большую фрактальную кривую Гильберта с помощью:
DDSAASSDDWDDSDDWWAAWDDDDSDDWDDDDSAASDDSAAAAWAASSSDDWDDDDSAASDDSAAAAWA
ASAAAAWDDWWAASAAWAASSDDSAASSDDWDDDDSAASDDSAAAAWAASSDDSAASSDDWDDSDDWWA
AWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWAAWDDDDSDDWDDSDDWDDDDSAASDDS
AAAAWAASSDDSAASSDDWDDSDDWWAAWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWA
AWDDDDSDDWWAAWDDWWAASAAWAASSDDSAAAAWAASAAAAWDDWAAWDDDDSDDWWWAASAAAAWD
DWAAWDDDDSDDWDDDDSAASSDDWDDSDDWWAAWDD
Теги: большая, графика"""

import shutil, sys

# Задаем константы для символов линий:
UP_DOWN_CHAR = chr(9474) # Символ 9474 — '│'
LEFT_RIGHT_CHAR = chr(9472) # Символ 9472 — '─'
DOWN_RIGHT_CHAR = chr(9484) # Символ 9484 —'┌'
DOWN_LEFT_CHAR = chr(9488) # Символ 9488 — '┐'
UP_RIGHT_CHAR = chr(9492) # Символ 9492 — '└'
UP_LEFT_CHAR = chr(9496) # Символ 9496 — '┘'
UP_DOWN_RIGHT_CHAR = chr(9500) # Символ 9500 — '├'
UP_DOWN_LEFT_CHAR = chr(9508) # Символ 9508 — '┤'
DOWN_LEFT_RIGHT_CHAR = chr(9516) # Символ 9516 — '┬'
UP_LEFT_RIGHT_CHAR = chr(9524) # Символ 9524 — '┴'
CROSS_CHAR = chr(9532) # Символ 9532 — '┼'
# Список кодов chr() можно найти в https://inventwithpython.com/chr

# Получаем размер окна терминала:
CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
# В Windows нельзя вывести что-либо в последнем столбце без добавления
# автоматически символа новой строки, поэтому уменьшаем ширину на 1:
CANVAS_WIDTH -= 1
# Оставляем место в нескольких нижних строках для информации о команде.
CANVAS_HEIGHT -= 5

"""Ключи ассоциативного массива canvas представляют собой целочисленные
кортежи (x, y) координат, а значение — набор букв W, A, S, D,
описывающих тип отрисовываемой линии."""
canvas = {}
cursorX = 0
cursorY = 0

def getCanvasString(canvasData, cx, cy):
    """Возвращает многострочное значение рисуемой в canvasData линии."""
    canvasStr = ''

    """canvasData — ассоциативный массив с ключами (x, y) и значениями
    в виде множеств из строк символов 'W', 'A', 'S' и/или 'D',
    описывающих, в каком направлении идет линия в каждой точке xy."""
    for rowNum in range(CANVAS_HEIGHT):
        for columnNum in range(CANVAS_WIDTH):
            if columnNum == cx and rowNum == cy:
                canvasStr += '#'
                continue

            # Добавляем символ линии для данной точки в canvasStr.
            cell = canvasData.get((columnNum, rowNum))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvasStr += UP_DOWN_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasStr += LEFT_RIGHT_CHAR
            elif cell == set(['S', 'D']):
                canvasStr += DOWN_RIGHT_CHAR
            elif cell == set(['A', 'S']):
                canvasStr += DOWN_LEFT_CHAR
            elif cell == set(['W', 'D']):
                canvasStr += UP_RIGHT_CHAR
            elif cell == set(['W', 'A']):
                canvasStr += UP_LEFT_CHAR
            elif cell == set(['W', 'S', 'D']):
                canvasStr += UP_DOWN_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A']):
                canvasStr += UP_DOWN_LEFT_CHAR
            elif cell == set(['A', 'S', 'D']):
                canvasStr += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'D']):
                canvasStr += UP_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'S', 'D']):
                canvasStr += CROSS_CHAR
            elif cell == None:
                canvasStr += ' '
        canvasStr += '\n' # Добавляем в конце строк символ новой строки.
    return canvasStr


moves = []
while True: # Основной цикл программы.
    # Отрисовываем линии, исходя из содержащихся в canvas данных:
    print(getCanvasString(canvas, cursorX, cursorY))

    print('WASD keys to move, H for help, C to clear, '
        + 'F to save, or QUIT.')
    response = input('> ').upper()

    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit() # Выходим из программы.
    elif response == 'H':
        print('Enter W, A, S, and D characters to move the cursor and')
        print('draw a line behind it as it moves. For example, ddd')
        print('draws a line going right and sssdddwwwaaa draws a box.')
        print()
        print('You can save your drawing to a text file by entering F.')
        input('Press Enter to return to the program...')
        continue
    elif response == 'C':
        canvas = {} # Очищаем canvas.
        moves.append('C') # Записываем движение.
    elif response == 'F':
        # Сохраняем строковое значение с холстом в текстовый файл:
        try:
            print('Enter filename to save to:')
            filename = input('> ')

            # Проверяем, чтобы имя файла оканчивалось на .txt:
            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(getCanvasString(canvas, None, None))
        except:
            print('ERROR: Could not save file.')

    for command in response:
        if command not in ('W', 'A', 'S', 'D'):
            continue # Игнорируем букву и переходим к следующей.
        moves.append(command) # Фиксируем данное движение.

        # Первая добавляемая линия должна формировать полную строку:
        if canvas == {}:
            if command in ('W', 'S'):
                # Делаем первую линию горизонтальной:
                canvas[(cursorX, cursorY)] = set(['W', 'S'])
            elif command in ('A', 'D'):
                # Делаем первую линию вертикальной:
                canvas[(cursorX, cursorY)] = set(['A', 'D'])

        # Обновляем значения x и y:
        if command == 'W' and cursorY > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorY = cursorY - 1
        elif command == 'S' and cursorY < CANVAS_HEIGHT - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorY = cursorY + 1
        elif command == 'A' and cursorX > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorX = cursorX - 1
        elif command == 'D' and cursorX < CANVAS_WIDTH - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorX = cursorX + 1
        else:
            # Если курсор не двигается, чтобы не выйти за пределы холста,
            # то не меняем множество в canvas[(cursorX, cursorY)]
            # canvas[(cursorX, cursorY)].
            continue

        # Если не существует множества для (cursorX, cursorY), добавляем
        # пустое множество:
        if (cursorX, cursorY) not in canvas:
            canvas[(cursorX, cursorY)] = set()

        # Добавляем строку с направлением во множество для этой точки xy:
        if command == 'W':
            canvas[(cursorX, cursorY)].add('S')
        elif command == 'S':
            canvas[(cursorX, cursorY)].add('W')
        elif command == 'A':
            canvas[(cursorX, cursorY)].add('D')
        elif command == 'D':
            canvas[(cursorX, cursorY)].add('A')
