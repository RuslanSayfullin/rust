"""Головоломка судоку, (c) Sayfullin Ruslan.
Классическая головоломка на расстановку цифр на доске 9 × 9.
"""

import copy, random, sys

# Для этой игры необходим файл sudokupuzzle.txt с головоломками.
# Скачать его можно с https://inventwithpython.com/sudokupuzzles.txt
# Пример содержимого этого файла:
# ..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.
# 1.3..2...8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6
# ...4.1...3......9.7...42.18....7.5.261..9.4....5.....4....5.7..992.1.8....34
# .59...5.7.......3..5..4...8.1.5..46.....12.7.5.2.8....6.3....4.1.9.3.25.....
# 98..1.2.6...8..6..2.
# Задаем константы:
EMPTY_SPACE = '.'
GRID_LENGTH = 9
BOX_LENGTH = 3
FULL_GRID_SIZE = GRID_LENGTH * GRID_LENGTH

class SudokuGrid:
    def __init__(self, originalSetup):
        # originalSetup — строка из 81 символа для начального состояния
        # головоломки, содержащего числа и точки (на месте пустых клеток).
        self.originalSetup = originalSetup
        # Состояние поля судоку представлено в виде ассоциативного
        # массива с ключами (x, y) и значениями — числами (в виде
        # строковых значений) в соответствующей клетке.
        self.grid = {}
        self.resetGrid() # Устанавливаем поле в начальное состояние.
        self.moves = [] # Отслеживаем все ходы для возможности отката.

    def resetGrid(self):
        """Восстанавливаем состояние поля, отслеживаемое в self.grid,
        до состояния из self.originalSetup."""
        for x in range(1, GRID_LENGTH + 1):
            for y in range(1, GRID_LENGTH + 1):
                self.grid[(x, y)] = EMPTY_SPACE
        assert len(self.originalSetup) == FULL_GRID_SIZE
        i = 0 # i проходит значения от 0 до 80
        y = 0 # y проходит значения от 0 до 8
        while i < FULL_GRID_SIZE:
            for x in range(GRID_LENGTH):
                self.grid[(x, y)] = self.originalSetup[i]
                i += 1
            y += 1


    def makeMove(self, column, row, number):
        """Помещаем число в столбец column (буква от A до I) и строку
        row (число от 1 до 9) в поле."""
        x = 'ABCDEFGHI'.find(column) # Преобразуем в числовое значение.
        y = int(row) - 1

        # Проверяем, не производится ли ход над клеткой с "подсказкой":
        if self.originalSetup[y * GRID_LENGTH + x] != EMPTY_SPACE:
            return False

        self.grid[(x, y)] = number      # Помещаем данное число на сетку.
        # Необходимо сохранить отдельную копию объекта ассоциативного массива:
        self.moves.append(copy.copy(self.grid))
        return True

    def undo(self):
        """Устанавливаем текущее состояние поля равным предыдущему
        состоянию из списка self.moves."""
        if self.moves == []:
            return # В self.moves отсутствуют состояния, так что ничего не делаем.
        self.moves.pop() # Удаляем текущее состояние.

        if self.moves == []:
            self.resetGrid()
        else:
            # Задаем такое состояние поля, какое было ход назад.
            self.grid = copy.copy(self.moves[-1])

    def display(self):
        """Отображаем текущее состояние поля на экране."""
        print( 'A B C  D E F  G H I') # Отображаем метки столбцов.
        for y in range(GRID_LENGTH):
            for x in range(GRID_LENGTH):
                if x == 0:
                    # Отображаем метку строки:
                    print(str(y + 1) + ' ', end='')
                print(self.grid[(x, y)] + ' ', end='')
                if x == 2 or x == 5:
                    # Выводим на экран вертикальную линию:
                    print('| ', end='')
            print() # Выводим символ новой строки.

            if y == 2 or y == 5:
                # Выводим на экран горизонтальную линию:
                print('------+-------+------')

    def _isCompleteSetOfNumbers(self, numbers):
        """Возвращает True, если numbers содержит цифры от 1 до 9."""
        return sorted(numbers) == list('123456789')

    def isSolved(self):
        """Возвращает True, если текущее поле находится в решенном состоянии."""
        # Проверяем каждую из строк:
        for row in range(GRID_LENGTH):
            rowNumbers = []
            for x in range(GRID_LENGTH):
                number = self.grid[(x, row)]
                rowNumbers.append(number)
            if not self._isCompleteSetOfNumbers(rowNumbers):
                return False

        # Проверяем каждый из столбцов:
        for column in range(GRID_LENGTH):
            columnNumbers = []
            for y in range(GRID_LENGTH):
                number = self.grid[(column, y)]
                columnNumbers.append(number)
            if not self._isCompleteSetOfNumbers(columnNumbers):
                return False

        # Проверяем все субполя 3 × 3:
        for boxx in (0, 3, 6):
            for boxy in (0, 3, 6):
                boxNumbers = []
                for x in range(BOX_LENGTH):
                    for y in range(BOX_LENGTH):
                        number = self.grid[(boxx + x, boxy + y)]
                        boxNumbers.append(number)
                if not self._isCompleteSetOfNumbers(boxNumbers):
                    return False

        return True


print('''Sudoku Puzzle, by Al Sweigart al@inventwithpython.com
Sudoku is a number placement logic puzzle game. A Sudoku grid is a 9x9
grid of numbers. Try to place numbers in the grid such that every row,
column, and 3x3 box has the numbers 1 through 9 once and only once.
For example, here is a starting Sudoku grid and its solved form:
5 3 . | . 7 . | . . .     5 3 4 | 6 7 8 | 9 1 2
6 . . | 1 9 5 | . . .     6 7 2 | 1 9 5 | 3 4 8
. 9 8 | . . . | . 6 .     1 9 8 | 3 4 2 | 5 6 7
------+-------+------     ------+-------+------
8 . . | . 6 . | . . 3     8 5 9 | 7 6 1 | 4 2 3
4 . . | 8 . 3 | . . 1 --> 4 2 6 | 8 5 3 | 7 9 1
7 . . | . 2 . | . . 6     7 1 3 | 9 2 4 | 8 5 6
------+-------+------     ------+-------+------
. 6 . | . . . | 2 8 .     9 6 1 | 5 3 7 | 2 8 4
. . . | 4 1 9 | . . 5     2 8 7 | 4 1 9 | 6 3 5
. . . | . 8 . | . 7 9     3 4 5 | 2 8 6 | 1 7 9
''')
input('Press Enter to begin...')

# Загружаем файл sudokupuzzles.txt:
with open('sudokupuzzles.txt') as puzzleFile:
    puzzles = puzzleFile.readlines()

# Удаляем символы новой строки в конце всех головоломок:
for i, puzzle in enumerate(puzzles):
    puzzles[i] = puzzle.strip()

grid = SudokuGrid(random.choice(puzzles))

while True: # Основной цикл программы.
    grid.display()

    # Проверяем, решена ли головоломка.
    if grid.isSolved():
        print('Congratulations! You solved the puzzle!')
        print('Thanks for playing!')
        sys.exit()
    # Запрашиваем действие пользователя:
    while True:
        # Продолжаем спрашивать, пока пользователь не введет допустимое действие.
        print() # Выводим символ новой строки.
        print('Enter a move, or RESET, NEW, UNDO, ORIGINAL, or QUIT:')
        print('(For example, a move looks like "B4 9".)')

        action = input('> ').upper().strip()

        if len(action) > 0 and action[0] in ('R', 'N', 'U', 'O', 'Q'):
            # Игрок ввел допустимое действие.
            break

        if len(action.split()) == 2:
            space, number = action.split()
            if len(space) != 2:
                continue

        column, row = space
        if column not in list('ABCDEFGHI'):
            print('There is no column', column)
            continue
        if not row.isdecimal() or not (1 <= int(row) <= 9):
            print('There is no row', row)
            continue
        if not (1 <= int(number) <= 9):
            print('Select a number from 1 to 9, not ', number)
            continue
        break # Игрок ввел допустимый ход.

    print() # Выводим символ новой строки.

    if action.startswith('R'):
        # Восстанавливаем поле:
        grid.resetGrid()
        continue

    if action.startswith('N'):
        # Создаем новую головоломку:
        grid = SudokuGrid(random.choice(puzzles))
        continue

    if action.startswith('U'):
        # Возвращаемся на ход назад:
        grid.undo()
        continue

    if action.startswith('O'):
        # Просмотр исходных чисел в поле:
        originalGrid = SudokuGrid(grid.originalSetup)
        print('The original grid looked like this:')
        originalGrid.display()
        input('Press Enter to continue...')

    if action.startswith('Q'):
        # Выходим из игры.
        print('Thanks for playing!')
        sys.exit()

    # Производим выбранный игроком ход.
    if grid.makeMove(column, row, number) == False:
        print('You cannot overwrite the original grid\'s numbers.')
        print('Enter ORIGINAL to view the original grid.')
        input('Press Enter to continue...')