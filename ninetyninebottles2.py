"""ДевяНосто деевяять буутылок млка На те не, (c) Sayfullin Ruslan.
Выводит полный текст одной из самых длинных песен на свете! С каждым
куплетом текст становится все более бессмысленным. Нажмите Ctrl+C для останова.
"""

import random, sys, time

# Задаем константы:
# (!) Замените обе эти константы на 0, чтобы сразу увидеть всю песню.
SPEED = 0.01        # Пауза между выводом отдельных букв.
LINE_PAUSE = 1.5    # Пауза в конце каждой строки.


def slowPrint(text, pauseAmount=0.1):
    """Медленно выводим символы текста по одному."""
    for character in text:
        # Укажите здесь flush=True, чтобы текст был выведен весь сразу:
        print(character, flush=True, end='')
        # end='' означает отсутствие перевода на новую строку.
        time.sleep(pauseAmount)     # Паузы между выводом символов.
    print()     # Выводим символ новой строки.


print('niNety-nniinE BoOttels, by Sayfullin Ruslan.')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(2)

bottles = 99

# Начальное количество бутылок.
# Список со строковыми значениями текста песни:
lines = [' bottles of milk on the wall,',
        ' bottles of milk,',
        'Take one down, pass it around,',
        ' bottles of milk on the wall!']

try:
    while bottles > 0:  # Отображаем текст песни в цикле.
        slowPrint(str(bottles) + lines[0], SPEED)
        time.sleep(LINE_PAUSE)
        slowPrint(str(bottles) + lines[1], SPEED)
        time.sleep(LINE_PAUSE)
        slowPrint(lines[2], SPEED)
        time.sleep(LINE_PAUSE)
        bottles = bottles - 1    # Уменьшаем количество бутылок на 1.

        if bottles > 0:     # Выводим последнюю строку текущего куплета.
            slowPrint(str(bottles) + lines[3], SPEED)
        else:   # Выводим последнюю строку всей песни.
            slowPrint('No more bottles of milk on the wall!', SPEED)

        time.sleep(LINE_PAUSE)
        print()     # Выводим символ новой строки.

        # Выбираем случайную строку, которую будем делать "смешной":
        lineNum = random.randint(0, 3)

        # Делаем список из символов строки текста, чтобы можно было
        # редактировать (строковые значения в Python — неизменяемые.)
        line = list(lines[lineNum])

        effect = random.randint(0, 3)
        if effect == 0:     # Заменяем символ пробелом.
            charIndex = random.randint(0, len(line) - 1)
            line[charIndex] = ' '
        elif effect == 1:   # Меняем регистр символа.
            charIndex = random.randint(0, len(line) - 1)
            if line[charIndex].isupper():
                line[charIndex] = line[charIndex].lower()
            elif line[charIndex].islower():
                line[charIndex] = line[charIndex].upper()
        elif effect == 2:   # Меняем два символа местами.
            charIndex = random.randint(0, len(line) - 2)
            firstChar = line[charIndex]
            secondChar = line[charIndex + 1]
            line[charIndex] = secondChar
            line[charIndex + 1] = firstChar
        elif effect == 3:   # Удваиваем символ.
            charIndex = random.randint(0, len(line) - 2)
            line.insert(charIndex, line[charIndex])

        # Преобразуем список обратно в строковое значение и вставляем в lines:
        lines[lineNum] = ''.join(line)
except KeyboardInterrupt:
    sys.exit()      # Если нажато сочетание клавиш Ctrl+C — завершаем программу.
