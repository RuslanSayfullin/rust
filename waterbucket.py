"""Головоломка с ведрами воды, (c) Sayfullin Ruslan aka CryptoLis.
Головоломка с переливанием воды.
Подробнее — в статье https://en.wikipedia.org/wiki/Water_pouring_puzzle
"""


import sys

print('Water Bucket Puzzle, by Sayfullin Ruslan')
GOAL = 4 # Точный объем воды, необходимый для победы.
steps = 0 # Содержит количество ходов, выполненных игроком для решения головоломки.

# Объем воды в каждом из ведер:
waterInBucket = {'8': 0, '5': 0, '3': 0}

while True: # Основной цикл игры.
    # Отображаем текущее состояние ведер:
    print()
    print('Try to get ' + str(GOAL) + 'L of water into one of these')
    print('buckets:')
    waterDisplay = []   # Содержит строковые значения для воды и пустого места.

    # Получаем строковые значения для восьмилитрового ведра:
    for i in range(1, 9):
        if waterInBucket['8'] < i:
            waterDisplay.append(' ')        # Добавляем пустое место.
        else:
            waterDisplay.append('WWWWWW')   # Добавляем воду.

    # Получаем строковые значения для пятилитрового ведра:
    for i in range(1, 6):
        if waterInBucket['5'] < i:
            waterDisplay.append(' ')        # Добавляем пустое место.
        else:
            waterDisplay.append('WWWWWW')   # Добавляем воду.

    # Получаем строковые значения для трехлитрового ведра:
    for i in range(1, 4):
        if waterInBucket['3'] < i:
            waterDisplay.append(' ')        # Добавляем пустое место.
        else:
            waterDisplay.append('WWWWWW')   # Добавляем воду.

    # Отображаем на экране ведра, каждое со своим объемом воды:
    print('''
        8|{7}|
        7|{6}|
        6|{5}|
        5|{4}| 5|{12}|
        4|{3}| 4|{11}|
        3|{2}| 3|{10}| 3|{15}|
        2|{1}| 2|{9}| 2|{14}|
        1|{0}| 1|{8}| 1|{13}|
        +------+   +------+   +------+
        8L            5L         3L
        '''.format(*waterDisplay))

    # Проверяем, не содержится ли в каком-то из ведер нужное количество воды:
    for waterAmount in waterInBucket.values():
        if waterAmount == GOAL:
            print('Good job! You solved it in', steps, 'steps!')
            sys.exit()

    # Спрашиваем у игрока, какое действие он хочет произвести с ведром:
    print('You can:')
    print(' (F)ill the bucket')
    print(' (E)mpty the bucket')
    print(' (P)our one bucket into another')
    print(' (Q)uit')
    while True:     # Спрашиваем, пока пользователь не укажет допустимое действие.
        move = input('> ').upper()
        if move == 'QUIT' or move == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if move in ('F', 'E', 'P'):
            break   # Игрок выбрал допустимое действие.
        print('Enter F, E, P, or Q')

    # Предлагаем игроку выбрать ведро:
    while True: # Спрашиваем, пока не будет указано допустимое ведро.
        print('Select a bucket 8, 5, 3, or QUIT:')
        srcBucket = input('> ').upper()

        if srcBucket == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if srcBucket in ('8', '5', '3'):
            break   # Игрок выбрал допустимое ведро.

    # Производим выбранное действие:
    if move == 'F':
        # Устанавливаем количество воды в максимальное значение.
        srcBucketSize = int(srcBucket)
        waterInBucket[srcBucket] = srcBucketSize
        steps += 1

    elif move == 'E':
        waterInBucket[srcBucket] = 0    # Устанавливаем количество воды в нулевое значение.
        steps += 1

    elif move == 'P':
        # Предлагаем игроку выбрать ведро, в которое наливать воду:
        while True:     # Спрашиваем, пока не будет указано допустимое ведро.
            print('Select a bucket to pour into: 8, 5, or 3')
            dstBucket = input('> ').upper()
            if dstBucket in ('8', '5', '3'):
                break   # Игрок выбрал допустимое ведро.

        # Определяем наливаемый объем воды:
        dstBucketSize = int(dstBucket)
        emptySpaceInDstBucket = dstBucketSize - waterInBucket[dstBucket]
        waterInSrcBucket = waterInBucket[srcBucket]
        amountToPour = min(emptySpaceInDstBucket, waterInSrcBucket)

        # Выливаем воду из ведра:
        waterInBucket[srcBucket] -= amountToPour

        # Наливаем вылитую воду в другое ведро:
        waterInBucket[dstBucket] += amountToPour
        steps += 1

    elif move == 'C':
        pass    # Если игрок выбрал Cancel, ничего не делаем.
