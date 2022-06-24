"""Цифровые часы, (c) Руслан Сайфуллин ruslansaifullin@gmail.com
Отображает показывающие текущее время цифровые часы с семисегментным
индикатором. Нажмите Ctrl+C для останова.
"""

import sys

import time

import sevseg    # Импорт программы sevseg.py.

try:
    while True:     # Основной цикл программы.
        # Очищаем экран, выводя несколько символов новой строки:
        print('\n' * 60)

        # Получаем текущее время из системных часов компьютера:
        currentTime = time.localtime()
        # % 12, поскольку мы используем 12-, а не 24-часовые часы:
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12'     # 12-часовые часы показывают 12:00, а не 00:00.
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        # Получаем из модуля sevseg строковые значения для цифр:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Отображаем цифры:
        print(hTopRow    + '   ' + mTopRow    + '   ' + sTopRow)
        print(hMiddleRow + ' * ' + mMiddleRow + ' * ' + sMiddleRow)
        print(hBottomRow + ' * ' + mBottomRow + ' * ' + sBottomRow)
        print()
        print('Press Ctrl-C to quit.')

        # Продолжаем выполнение цикла до перехода на новую секунду:
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    print('Digital Clock, by Al Sweigart al@inventwithpython.com')
    sys.exit() # Если нажато сочетание клавиш Ctrl+C — завершаем программу.