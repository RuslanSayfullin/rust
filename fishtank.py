"""Аквариум, Sayfullin Ruslan.
Безмятежное динамическое изображение аквариума. Нажмите Ctrl+C для останова.
Аналогична ASCIIQuarium и @EmojiAquarium, но программа основана на
более старой программе ASCII-аквариума под DOS.
"""

import random
import sys
import time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Задаем константы:
WIDTH, HEIGHT = bext.size()
# В Windows нельзя вывести что-либо в последнем столбце без добавления
# автоматически символа новой строки, поэтому уменьшаем ширину на 1:
WIDTH -= 1

NUM_KELP = 2 # (!) Попробуйте заменить это значение на 10.
NUM_FISH = 10 # (!) Попробуйте заменить это значение на 2 или 100.
NUM_BUBBLERS = 1 # (!) Попробуйте заменить это значение на 0 или 10.
FRAMES_PER_SECOND = 4 # (!) Попробуйте заменить это число на 1 или 60.
# (!) Попробуйте изменить константы, чтобы получился аквариум с одними
# только водорослями или пузырьками.
# Примечание: все строковые значения в ассоциативном массиве рыбок должны быть
# одинаковой длины.
FISH_TYPES = [
{'right': ['><>'],          'left': ['<><']},
{'right': ['>||>'],         'left': ['<||<']},
{'right': ['>))>'],         'left': ['<[[<']},
{'right': ['>||o', '>||.'], 'left': ['o||<', '.||<']},
{'right': ['>))o', '>)).'], 'left': ['o[[<', '.[[<']},
{'right': ['>-==>'],        'left': ['<==-<']},
{'right': [r'>\\>'],        'left': ['<//<']},
{'right': ['><)))*>'],      'left': ['<*(((><']},
{'right': ['}-[[[*>'],      'left': ['<*]]]-{']},
{'right': [']-<)))b>'],     'left': ['<d(((>-[']},
{'right': ['><XXX*>'],      'left': ['<*XXX><']},
{'right': ['_.-._.-^=>', '.-._.-.^=>',
           '-._.-._^=>', '._.-._.^=>'],
  'left': ['<=^-._.-._', '<=^.-._.-.',
           '<=^_.-._.-', '<=^._.-._.']},
] # (!) Попробуйте добавить в FISH_TYPES свои типы рыб.
LONGEST_FISH_LENGTH = 10 # Максимальная длина строкового значения в FISH_TYPES.

# Позиции по x и y, при которых рыбка наталкивается на край экрана:
LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 2

def main():
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP
    bext.bg('black')
    bext.clear()

    # Генерируем глобальные переменные:
    FISHES = []
    for i in range(NUM_FISH):
        FISHES.append(generateFish())

    # Примечание: мы нарисовали пузырьки, но не сами воздуховоды.
    BUBBLERS = []
    for i in range(NUM_BUBBLERS):
        # Все воздуховоды начинаются в разных местах.
        BUBBLERS.append(random.randint(LEFT_EDGE, RIGHT_EDGE))
    BUBBLES = []

    KELPS = []
    for i in range(NUM_KELP):
        kelpx = random.randint(LEFT_EDGE, RIGHT_EDGE)
        kelp = {'x': kelpx, 'segments': []}
        # Генерируем сегменты водорослей:
        for i in range(random.randint(6, HEIGHT - 1)):
            kelp['segments'].append(random.choice(['(', ')']))
        KELPS.append(kelp)

    # Запускаем моделирование:
    STEP = 1
    while True:
        simulateAquarium()
        drawAquarium()
        time.sleep(1 / FRAMES_PER_SECOND)
        clearAquarium()
        STEP += 1

def getRandomColor():
    """Возвращает строковое значение со случайным цветом."""
    return random.choice(('black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white'))

def generateFish():
    """Возвращает соответствующий рыбке ассоциативный массив."""
    fishType = random.choice(FISH_TYPES)

    # Задает цвета для каждого из символов рыбки:
    colorPattern = random.choice(('random', 'head-tail', 'single'))
    fishLength = len(fishType['right'][0])
    if colorPattern == 'random': # Все части окрашиваются случайным образом.
        colors = []
        for i in range(fishLength):
            colors.append(getRandomColor())
    if colorPattern == 'single' or colorPattern == 'head-tail':
        colors = [getRandomColor()] * fishLength # Все одного цвета.
    if colorPattern == 'head-tail': # Голова/хвост — отличного от тела цвета.
        headTailColor = getRandomColor()
        colors[0] = headTailColor # Задаем цвет головы.
        colors[-1] = headTailColor # Задаем цвет хвоста.

    # Задаем остальные части структуры данных для рыбки:
    fish = {'right':            fishType['right'],
            'left':             fishType['left'],
            'colors':           colors,
            'hSpeed':           random.randint(1, 6),
            'vSpeed':           random.randint(5, 15),
            'timeToHDirChange': random.randint(10, 60),
            'timeToVDirChange': random.randint(2, 20),
            'goingRight':       random.choice
            ([True, False]),
            'goingDown':        random.choice([True, False])}
    # 'x' - всегда крайняя слева сторона тела рыбки:
    fish['x'] = random.randint(0, WIDTH - 1 - LONGEST_FISH_LENGTH)
    fish['y'] = random.randint(0, HEIGHT - 2)
    return fish


def simulateAquarium():
    """Моделирует один шаг движений в аквариуме."""
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP

    # Моделирует один шаг движения рыбки:
    for fish in FISHES:
        # Горизонтальное перемещение рыбки:
        if STEP % fish['hSpeed'] == 0:
            if fish['goingRight']:
                if fish['x'] != RIGHT_EDGE:
                    fish['x'] += 1 # Перемещение рыбки вправо.
                else:
                    fish['goingRight'] = False  # Поворот рыбки.
                    fish['colors'].reverse()    # Инверсия цветов.
            else:
                if fish['x'] != LEFT_EDGE:
                    fish['x'] -= 1 # Перемещение рыбки влево.
                else:
                    fish['goingRight'] = True # Поворот рыбки.
                    fish['colors'].reverse() # Инверсия цветов.
            # Рыбки могут случайным образом менять направление горизонтального
            # движения:
            fish['timeToHDirChange'] -= 1
            if fish['timeToHDirChange'] == 0:
                fish['timeToHDirChange'] = random.randint(10, 60)
                # Поворот рыбки:
                fish['goingRight'] = not fish['goingRight']

            # Вертикальное перемещение рыбки:
            if STEP % fish['vSpeed'] == 0:
                if fish['goingDown']:
                    if fish['y'] != BOTTOM_EDGE:
                        fish['y'] += 1 # Перемещение рыбки вниз.
                    else:
                        fish['goingDown'] = False # Поворот рыбки.
                else:
                    if fish['y'] != TOP_EDGE:
                        fish['y'] -= 1 # Перемещение рыбки вверх.
                    else:
                        fish['goingDown'] = True # Поворот рыбки.

        # Рыбки могут случайным образом менять направление вертикального движения:
        fish['timeToVDirChange'] -= 1
        if fish['timeToVDirChange'] == 0:
            fish['timeToVDirChange'] = random.randint(2, 20)
            # Поворот рыбки:
            fish['goingDown'] = not fish['goingDown']

    # Генерируем пузырьки из воздуховодов:
    for bubbler in BUBBLERS:
        # Вероятность создания пузырька: 1 из 5:
        if random.randint(1, 5) == 1:
            BUBBLES.append({'x': bubbler, 'y': HEIGHT - 2})

    # Перемещаем пузырьки:
    for bubble in BUBBLES:
        diceRoll = random.randint(1, 6)
        if (diceRoll == 1) and (bubble['x'] != LEFT_EDGE):
            bubble['x'] -= 1 # Пузырек воздуха перемещается влево.
        elif (diceRoll == 2) and (bubble['x'] != RIGHT_EDGE):
            bubble['x'] += 1    # Пузырек воздуха перемещается вправо.
            bubble['y'] -= 1    # Пузырек воздуха всегда поднимается вверх.

    # Проходим в цикле по BUBBLES в обратном порядке для удаления
    # из BUBBLES в цикле.
    for i in range(len(BUBBLES) - 1, -1, -1):
        if BUBBLES[i]['y'] == TOP_EDGE: # Удаляем достигшие верха пузырьки.
            del BUBBLES[i]

    # Моделирует один шаг колебания водоросли:
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            # Вероятность смены колебаний — 1 из 20:
            if random.randint(1, 20) == 1:
                if kelpSegment == '(':
                    kelp['segments'][i] = ')'
                elif kelpSegment == ')':
                    kelp['segments'][i] = '('


def drawAquarium():
    """Отрисовываем аквариум на экране."""
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP

    # Сообщение о возможности прервать отрисовку.
    bext.fg('white')
    bext.goto(0, 0)
    print('Fish Tank, by , Sayfullin Ruslan. Ctrl-C to quit.', end='')

    # Отрисовываем пузырьки воздуха:
    bext.fg('white')
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(random.choice(('o', 'O')), end='')

    # Отрисовываем рыбок:
    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])

        # Получаем правильный текст для рыбки, смотрящей влево или вправо.
        if fish['goingRight']:
            fishText = fish['right'][STEP % len(fish['right'])]
        else:
            fishText = fish['left'][STEP % len(fish['left'])]

        # Отрисовываем все символы рыбки правильными цветами.
        for i, fishPart in enumerate(fishText):
            bext.fg(fish['colors'][i])
            print(fishPart, end='')

    # Отрисовываем водоросли:
    bext.fg('green')
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            if kelpSegment == '(':
                bext.goto(kelp['x'], BOTTOM_EDGE - i)
            elif kelpSegment == ')':
                bext.goto(kelp['x'] + 1, BOTTOM_EDGE - i)
            print(kelpSegment, end='')

    # Отрисовываем песок на дне:
    bext.fg('yellow')
    bext.goto(0, HEIGHT - 1)
    print(chr(9617) * (WIDTH - 1), end='')   # Draws sand.

    sys.stdout.flush() # (Необходимо для использующих модуль bext программ.)


def clearAquarium():
    """Зарисовываем весь экран пробелами."""
    global FISHES, BUBBLERS, BUBBLES, KELP

    # Зарисовываем пузырьки воздуха:
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(' ', end='')

    # Зарисовываем рыбок:
    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])

        # Отрисовываем все символы текста рыбки правильными цветами.
        print(' ' * len(fish['left'][0]), end='')

    # Зарисовываем водоросли:
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            bext.goto(kelp['x'], HEIGHT - 2 - i)
            print(' ', end='')

    sys.stdout.flush()  # (Необходимо для использующих модуль bext программ.)


# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() # Если нажато Ctrl+C — завершаем программу.
