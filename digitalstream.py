"""Цифровой поток,
Экранная заставка в стиле визуальных эффектов фильма "Матрица".
"""
import random, shutil, sys, time
# Задаем константы:
MIN_STREAM_LENGTH = 6   # (!) Попробуйте заменить это значение на 1 или 50.
MAX_STREAM_LENGTH = 14   # (!) Попробуйте заменить это значение на 100.
PAUSE = 0.1     # (!) Попробуйте заменить это значение на 0.0 или 2.0.
STREAM_CHARS = ['0', '1']   # (!) Попробуйте заменить их на другие символы.

# Плотность может варьироваться от 0.0 до 1.0:
DENSITY = 0.02  # (!) Попробуйте заменить это значение на 0.10 или 0.30.

# Получаем размер окна терминала:
WIDTH = shutil.get_terminal_size()[0]
# В Windows нельзя вывести что-либо в последнем столбце без добавления
# автоматически символа новой строки, поэтому уменьшаем ширину на 1:
WIDTH -= 1

print('Digital Stream, by Ruslan Sayfullin')
print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    # Если для столбца счетчик равен 0, поток не отображается.
    # В противном случае он показывает, сколько раз должны отображаться
    # в этом столбце 1 или 0.
    columns = [0] * WIDTH
    while True:
        # Задаем счетчики для каждого из столбцов:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    # Перезапускаем поток для этого столбца.
                    columns[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)

            # Выводим пробел или символ 1/0.
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()         # Выводим символ новой строки в конце строки столбцов.
        sys.stdout.flush()  # Обеспечиваем появление текста на экране.
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()  # Если нажато сочетание клавиш Ctrl+C — завершаем программу.
