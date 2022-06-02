"""Отскакивающий от краев логотип DVD
Анимация отскакивающего логотипа DVD. Оценить ее по достоинству могут
только люди "определенного возраста". Для останова нажмите Ctrl+C.
Примечание: не меняйте размера окна терминала во время работы программы.
"""

import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()


# Задаем константы:
WIDTH, HEIGHT = bext.size()
# В Windows нельзя вывести символ в последний столбец без добавления
# автоматически символа новой строки, так что уменьшаем ширину на 1:
WIDTH -= 1
NUMBER_OF_LOGOS = 5 # (!) Попробуйте заменить на 1 или 100.
PAUSE_AMOUNT = 0.2 # (!) Попробуйте заменить на 1.0 или 0.0.
# (!) Попробуйте уменьшить количество цветов в этом списке:
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Названия ключей для ассоциативных массивов логотипов:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()

    # Генерация логотипов.
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
            X: random.randint(1, WIDTH - 4),
            Y: random.randint(1, HEIGHT - 4),
            DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            # Гарантируем, что X четное число, для столкновения с углом.
            logos[-1][X] -= 1

    cornerBounces = 0 # Считаем, сколько раз логотип столкнулся с углом.
    while True: # Основной цикл программы.
        for logo in logos: # Обрабатываем все логотипы в списке логотипов.
            # Очищаем место, где ранее находился логотип:
            bext.goto(logo[X], logo[Y])
            print(' ', end='') # (!) Попробуйте закомментировать строку.
            originalDirection = logo[DIR]

            # Проверяем, не отскакивает ли логотип от угла:
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            # Проверяем, не отскакивает ли логотип от левого края:
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # Проверяем, не отскакивает ли логотип от правого края:
            # (WIDTH - 3, поскольку 'DVD' состоит из трех букв.)
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT
            # Проверяем, не отскакивает ли логотип от верхнего края:
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # Проверяем, не отскакивает ли логотип от нижнего края:
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] =  UP_RIGHT

            if logo[DIR] != originalDirection:
                # Меняем цвет при отскакивании логотипа:
                logo[COLOR] = random.choice(COLORS)

            # Перемещаем логотип. (Координата X меняется на 2, поскольку
            # в терминале высота символов вдвое превышает ширину.)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # Отображает количество отскакиваний от углов:
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', cornerBounces, end='')
        for logo in logos:
            # Отрисовывает логотипы на новом месте:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')
        bext.goto(0, 0)
        sys.stdout.flush() # (Нужно для программ, использующих модуль bext.)
        time.sleep(PAUSE_AMOUNT)

# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo, by Al Sweigart')
        sys.exit() # При нажатии Ctrl+C завершаем выполнение программы.