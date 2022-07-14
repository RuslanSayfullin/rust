"""Таблица умножения, (c) Sayfullin Ruslan.
Выводит на экран таблицу умножения.
"""

print('Multiplication Table, by Al Sweigart al@inventwithpython.com')
# Выводим горизонтальные метки чисел:
print('  |  0  1  2  3   4   5   6   7   8   9   10   11   12')
print('--+---------------------------------------------------')

# Построчно выводим на экран произведения:
for number1 in range(0, 13):

    # Выводим вертикальные метки чисел:
    print(str(number1).rjust(2), end='')

    # Выводим разделитель:
    print('|', end='')

    for number2 in range(0, 13):
        # Выводит произведение и пробел:
        print(str(number1 * number2).rjust(3), end=' ')

    print() # Завершаем строку символом новой строки.