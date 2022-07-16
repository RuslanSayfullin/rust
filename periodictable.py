"""Периодическая таблица элементов, (c) Sayfullin Ruslan.
Отображает информацию обо всех элементах
"""
# Данные из https://en.wikipedia.org/wiki/List_of_chemical_elements
# Выделите таблицу, скопируйте ее и вставьте в программу для работы
# с электронными таблицами, например Excel или Google-таблицы, как
# в https://invpy.com/elements. Сохраните файл как periodictable.csv.
# Или просто скачайте его по адресу https://invpy.com/periodictable.csv

import csv, sys, re

# Считываем все данные из periodictable.csv.
elementsFile = open('periodictable.csv', encoding='utf-8')
elementsCsvReader = csv.reader(elementsFile)
elements = list(elementsCsvReader)
elementsFile.close()

ALL_COLUMNS = ['Atomic Number', 'Symbol', 'Element', 'Origin of name',
                'Group', 'Period', 'Atomic weight', 'Density',
                'Melting point', 'Boiling point',
                'Specific heat capacity', 'Electronegativity',
                'Abundance in earth\'s crust']

# Для выравнивания текста по ширине нужно найти самую длинную строку
# в ALL_COLUMNS.
LONGEST_COLUMN = 0
for key in ALL_COLUMNS:
    if len(key) > LONGEST_COLUMN:
        LONGEST_COLUMN = len(key)
# Помещаем все данные об элементах в структуру данных:
ELEMENTS = {} # Структура данных со всеми данными об элементах.
for line in elements:
    element = {'Atomic Number':     line[0],
                'Symbol':           line[1],
                'Element':          line[2],
                'Origin of name':   line[3],
                'Group':            line[4],
                'Period':           line[5],
                'Atomic weight':    line[6] + ' u',         # атомная единица массы
                'Density':          line[7] + ' g/cm^3',    # граммов/куб. см
                'Melting point':    line[8] + ' K',         # градусов по Кельвину
                'Boiling point':    line[9] + ' K',         # градусов по Кельвину
                'Specific heat capacity':       line[10] + ' J/(g*K)',
                'Electronegativity':            line[11],
                'Abundance in earth\'s crust':  line[12] + ' mg/kg'}

    # Часть данных включает текст в квадратных скобках из "Википедии",
    # который необходимо удалить, например атомный вес бора:
    # вместо "10.81[III][IV][V][VI]" должно быть "10.81"
    for key, value in element.items():
        # Удаляем римские цифры в квадратных скобках:
        element[key] = re.sub(r'\[(I|V|X)+\]', '', value)

    ELEMENTS[line[0]] = element     # Сопоставляем атомный номер и элемент.
    ELEMENTS[line[1]] = element     # Сопоставляем символ и элемент.



print('Periodic Table of Elements')
print('By Al Sweigart al@inventwithpython.com')
print()

while True: # Основной цикл программы.
    # Выводим таблицу и позволяем пользователю выбрать элемент:
    print(''' Periodic Table of Elements
    1    2  3  4  5  6  7  8  9  10 11  12  13  14  15  16  17  18
    1 H                                                         He
    2 Li Be                                  B   C   N   O  F   Ne
    3 Na Mg                                  Al  Si  P   S  Cl  Ar
    4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu   Zn  Ga  Ge  As  Se Br  Kr
    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag   Cd  In  Sn  Sb  Te I   Xe
    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au   Hg  Tl  Pb  Bi  Po At  Rn
    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg   Cn  Nh  Fl  Mc  Lv Ts  Og

            Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
            Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')
    print('Enter a symbol or atomic number to examine, or QUIT to quit.')
    response = input('> ').title()

    if response == 'Quit':
        sys.exit()

    # Отображаем информацию о выбранном элементе:
    if response in ELEMENTS:
        for key in ALL_COLUMNS:
            keyJustified = key.rjust(LONGEST_COLUMN)
            print(keyJustified + ': ' + ELEMENTS[response][key])
        input('Press Enter to continue...')