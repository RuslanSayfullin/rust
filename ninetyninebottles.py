"""Девяносто девять бутылок молока на стене, (c) Sayfullin Ruslan.
Выводит полный текст одной из самых длинных песен на свете!
Нажмите Ctrl-C для останова.
"""

import sys, time

print('Ninety-Nine Bottles, by Sayfullin Ruslan.')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(2)

bottles = 99    # Начальное количество бутылок.
PAUSE = 2       # (!) Замените на 0, чтобы сразу увидеть всю песню.

try:
    while bottles > 1:  # Отображаем текст песни в цикле.
        print(bottles, 'bottles of milk on the wall,')
        time.sleep(PAUSE)   # Приостанавливаем на PAUSE секунд.
        print(bottles, 'bottles of milk,')
        time.sleep(PAUSE)
        print('Take one down, pass it around,')
        time.sleep(PAUSE)
        bottles = bottles - 1   # Уменьшаем количество бутылок на 1.
        print(bottles, 'bottles of milk on the wall!')
        time.sleep(PAUSE)
        print()     # Выводим символ новой строки.

    # Выводим последний куплет:
    print('1 bottle of milk on the wall,')
    time.sleep(PAUSE)
    print('1 bottle of milk,')
    time.sleep(PAUSE)
    print('Take it down, pass it around,')
    time.sleep(PAUSE)
    print('No more bottles of milk on the wall!')
except KeyboardInterrupt:
    sys.exit()  # Если нажато сочетание клавиш Ctrl+C — завершаем программу.
