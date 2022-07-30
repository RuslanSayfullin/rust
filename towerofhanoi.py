"""Ханойская башня, (c) Sayfullin Ruslan aka CryptoLis.
Головоломка с переносом столбиков
"""

import copy
import sys

TOTAL_DISKS = 5     # Чем больше дисков, тем сложнее головоломка.

# В начале все диски находятся на башне A:
COMPLETE_TOWER = list(range(TOTAL_DISKS, 0, -1))

def main():
    print("""The Tower of Hanoi, by Sayfullin Ruslan
    Move the tower of disks, one disk at a time, to another tower. Larger
    disks cannot rest on top of a smaller disk.
    More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi
    """)

    # Задаем башни. Конец списка соответствует верху башни.
    towers = {'A': copy.copy(COMPLETE_TOWER), 'B': [], 'C': []}
    while True:     # Выполняем один ход.
        # Отображаем башни и диски:
        displayTowers(towers)

        # Просим пользователя сделать ход:
        fromTower, toTower = askForPlayerMove(towers)

        # Переносим верхний диск с fromTower на toTower:
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # Проверяем, не решил ли уже головоломку пользователь:
        if COMPLETE_TOWER in (towers['B'], towers['C']):
            displayTowers(towers)   # Отображаем башни последний раз.
            print('You have solved the puzzle! Well done!')
            sys.exit()


def askForPlayerMove(towers):
    """Просит игрока сделать ход. Возвращает (fromTower, toTower)."""
    while True:      # Продолжаем спрашивать игрока, пока он не введет допустимый ход.
        print('Enter the letters of "from" and "to" towers, or QUIT.')
        print('(e.g. AB to moves a disk from tower A to tower B.)')
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # Убеждаемся, что игрок ввел корректные буквы башен:
        if response not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
            print('Enter one of AB, AC, BA, BC, CA, or CB.')
            continue    # Просим игрока ввести ход снова.

        # Синтаксический сахар — более наглядные названия переменных:
        fromTower, toTower = response[0], response[1]
        if len(towers[fromTower]) == 0:
            # Исходная башня не должна быть пустой:
            print('You selected a tower with no disks.')
            continue # Просим игрока ввести ход снова.
        elif len(towers[toTower]) == 0:
            # На пустую целевую башню можно перенести любой диск:
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print('Can\'t put larger disks on top of smaller ones.')
            continue    # Просим игрока ввести ход снова.
        else:
            # Ход допустим, возвращаем выбранные башни:
            return fromTower, toTower


def displayTowers(towers):
    """Отображаем текущее состояние."""

    # Отображаем три башни:
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers['A'], towers['B'], towers['C']):
            if level >= len(tower):
                displayDisk(0)              # Отображаем пустой стержень без дисков.
            else:
                displayDisk(tower[level])   # Отображаем диск.
        print()

    # Отображаем метки башен A, B и C.
    emptySpace = ' ' * (TOTAL_DISKS)
    print('{0} A{0}{0} B{0}{0} C\n'.format(emptySpace))


def displayDisk(width):
    """Отображаем диск заданной ширины. Ширина 0 означает отсутствие диска."""
    emptySpace = ' ' * (TOTAL_DISKS - width)

    if width == 0:
        # Отображаем сегмент стержня без диска:
        print(emptySpace + '||' + emptySpace, end='')
    else:
        # Отображаем диск:
        disk = '@' * width
        numLabel = str(width).rjust(2, '_')
        print(emptySpace + disk + numLabel + disk + emptySpace, end='')


# Если программа не импортируется, а запускается, производим запуск игры:
if __name__ == '__main__':
    main()
