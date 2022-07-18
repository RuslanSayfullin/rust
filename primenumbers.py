"""Простые числа, (c) Sayfullin Ruslan.
Вычисляет простые числа — числа, делящиеся нацело только на единицу
и на себя самое. Они применяются на практике во множестве сфер.
"""

import math, sys


def main():
    print('Prime Numbers, by Sayfullin Ruslan.')
    print('Prime numbers are numbers that are only evenly divisible by')
    print('one and themselves. They are used in a variety of practical')
    print('applications, but cannot be predicted. They must be')
    print('calculated one at a time.')
    print()
    while True:
        print('Enter a number to start searching for primes from:')
        print('(Try 0 or 1000000000000 (12 zeros) or another number.)')
        response = input('> ')
        if response.isdecimal():
            num = int(response)
            break

    input('Press Ctrl-C at any time to quit. Press Enter to begin...')
    while True:
        # Выводит все найденные простые числа:
        if isPrime(num):
            print(str(num) + ', ', end='', flush=True)
        num = num + 1   # Переходим к следующему числу.


def isPrime(number):
    """Возвращает True, если число простое, в противном случае — False."""
    # Обрабатываем частные случаи:
    if number < 2:
        return False
    elif number == 2:
        return True

    # Пытаемся разделить нацело данное число на все числа от 2
    # до квадратного корня из него.
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Если нажато сочетание клавиш Ctrl+C — завершаем программу.
