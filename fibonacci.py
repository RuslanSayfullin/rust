"""Последовательность Фибоначчи, Sayfullin Ruslan.
Вычисляет числа из последовательности Фибоначчи: 0, 1, 1, 2, 3, 5, 8, 13...
"""

import sys

print('''Fibonacci Sequence, by Sayfullin Ruslan.
The Fibonacci sequence begins with 0 and 1, and the next number is the
sum of the previous two numbers. The sequence continues forever:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...
''')

while True: # Основной цикл программы.
    while True: # Спрашиваем, пока пользователь не введет допустимое число.
        print('Enter the Nth Fibonacci number you wish to')
        print('calculate (such as 5, 50, 1000, 9999), or QUIT to quit:')
        response = input('> ').upper()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break # Когда пользователь ввел допустимое число — выходим из цикла

        print('Please enter a number greater than 0, or QUIT.')

    print()

    # Обработка частных случаев, если пользователь ввел 1 или 2:
    if nth == 1:
        print('0')
        print()
        print('The #1 Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('The #2 Fibonacci number is 1.')
        continue

    # Отображаем предупреждение, если пользователь ввел большое число:
    if nth >= 10000:
        print('WARNING: This will take a while to display on the')
        print('screen. If you want to quit this program before it is')
        print('done, press Ctrl-C.')
        input('Press Enter to begin...')

    # Вычисляем N-е число Фибоначчи:
    secondToLastNumber = 0
    lastNumber = 1
    fibNumbersCalculated = 2
    print('0, 1, ', end='') # Выводим первые два числа Фибоначчи.

    # Выводим все остальные числа Фибоначчи:
    while True:
        nextNumber = secondToLastNumber + lastNumber
        fibNumbersCalculated += 1

        # Выводим следующее число последовательности:
        print(nextNumber, end='')

        # Проверяем, нашли ли мы требуемое пользователем N-е число:
        if fibNumbersCalculated == nth:
            print()
            print()
            print('The #', fibNumbersCalculated, ' Fibonacci ', 'number is ', nextNumber, sep='')
            break

        # Выводим запятую между членами последовательности:
        print(', ', end='')

        # Заменяем последние два числа:
        secondToLastNumber = lastNumber
        lastNumber = nextNumber
