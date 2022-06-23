"""Обратный отсчет,
Отображает динамическое изображение таймера обратного отсчета с помощью
семисегментного индикатора. Для останова нажмите Ctrl+C."""

import sys
import time
import sevseg   # Импорт программы sevseg.py.

# (!) Можете заменить это значение на любое количество секунд:
secondsLeft = 30

try:
    while True:  # Основной цикл программы.
        # Очищаем экран, выводя несколько символов новой строки:
        print('\n' * 60)

        # Берем часы/минуты/секунды из secondsLeft:
        # Например: 7265 равно 2 часам 1 минуте 5 секундам.
        # 7265 // 3600 равно 2 часам:
        hours = str(secondsLeft // 3600)
        # 7265 % 3600 равно 65, и 65 // 60 равно 1 минуте:
        minutes = str((secondsLeft % 3600) // 60)
        # А 7265 % 60 равно 5 секундам:
        seconds = str(secondsLeft % 60)

        # Получаем из модуля sevseg строковые значения для цифр:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Отображаем цифры:
        print(hTopRow       + '   '  + mTopRow    + '   ' + sTopRow)
        print(hMiddleRow    + ' * '  + mMiddleRow + ' * ' + sMiddleRow)
        print(hBottomRow    + ' * '  + mBottomRow + ' * ' + sBottomRow)

        if secondsLeft == 0:
            print()
            print('* * * * BOOM * * * *')
            break

        print()
        print('Press Ctrl-C to quit.')
        time.sleep(1)   # Вставляем паузу на 1 секунду.
        secondsLeft -= 1
except KeyboardInterrupt:
    print('Countdown, by Ruslan Sayfullin')
    sys.exit()  # Если нажато сочетание клавиш Ctrl+C — завершаем программу.
