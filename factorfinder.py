"""Разложение на множители, Sayfullin Ruslan
Находит все множители заданного числа
"""
import math
import sys

print('''Factor Finder, by Sayfullin Ruslan
A number's factors are two numbers that, when multiplied with each
other, produce the number. For example, 2 x 13 = 26, so 2 and 13 are
factors of 26. 1 x 26 = 26, so 1 and 26 are also factors of 26. We
say that 26 has four factors: 1, 2, 13, and 26.

If a number only has two factors (1 and itself), we call that a prime
number. Otherwise, we call it a composite number.

Can you discover some prime numbers?
''')

while True:  # Основной цикл программы.
    print('Enter a positive whole number to factor (or QUIT):')
    response = input('> ')
    if response.upper() == 'QUIT':
        sys.exit()

    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)

    factors = []

    # Поиск множителей числа:
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:     # Если остатка нет, значит — множитель.
            factors.append(i)
            factors.append(number // i)

    # Преобразуем во множество, чтобы избавиться от повторов:
    factors = list(set(factors))
    factors.sort()

    # Выводим результаты:
    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(', '.join(factors))
