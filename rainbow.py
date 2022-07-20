"""Радуга, (c) Sayfullin Ruslan.
Отображает простое динамическое изображение радуги. Нажмите Ctrl-C для останова.
"""

import time, sys

try:
    import bext
except ImportError:
        print('This program requires the bext module, which you')
        print('can install by following the instructions at')
        print('https://pypi.org/project/Bext/')
        sys.exit()

print('Rainbow, by  Sayfullin Ruslan')
print('Press Ctrl-C to stop.')
time.sleep(3)

indent = 0 # Количество пробелов в полях.
indentIncreasing = True # Растут поля или уменьшаются.

try:
    while True: # Основной цикл программы.
        print(' ' * indent, end='')
        bext.fg('red')
        print('##', end='')
        bext.fg('yellow')
        print('##', end='')
        bext.fg('green')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('cyan')
        print('##', end='')
        bext.fg('purple')
        print('##')

        if indentIncreasing:
            # Увеличиваем количество пробелов:
            indent = indent + 1
            if indent == 60:    # (!) Попробуйте заменить это значение на 10 или 30.
                # Меняем направление:
                indentIncreasing = False
        else:
            # Уменьшаем количество пробелов:
            indent = indent - 1
            if indent == 0:
                # Меняем направление:
                indentIncreasing = True

        time.sleep(0.02)    # Небольшая пауза.
except KeyboardInterrupt:
    sys.exit()  # Если нажато сочетание клавиш Ctrl+C — завершаем программу.
