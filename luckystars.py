"""Под счастливой звездой, (c) Sayfullin Ruslan.
Игра на везение, цель которой — набрать как можно больше "звезд" путем
выбрасывания костей. Можете бросать кости столько раз, сколько хотите,
но, если выбросите три "черепа", потеряете все набранные "звезды".
Создано под впечатлением от игры Zombie Dice от Steve Jackson Games.
Код размещен на https://nostarch.com/big-book-small-python-projects
Теги: большая, игра, многопользовательская"""



import random

# Задаем константы:
GOLD = 'GOLD'
SILVER = 'SILVER'
BRONZE = 'BRONZE'

STAR_FACE = ["+-----------+",
             "|     .     |",
             "|    ,O,    |",
             "| 'ooOOOoo' |",
             "|   `OOO`   |",
             "|   O' 'O   |",
             "+-----------+"]
SKULL_FACE = ['+-----------+',
              '|   ___     |',
              '|  /   \\   |',
              '| |() ()|   |',
              '| \\ ^ /    |',
              '|   VVV     |',
              '+-----------+']
QUESTION_FACE = ['+-----------+',
                 '|           |',
                 '|           |',
                 '|    ?      |',
                 '|           |',
                 '|           |',
                 '+-----------+']

FACE_WIDTH = 13
FACE_HEIGHT = 7

print("""Lucky Stars, (c) Sayfullin Ruslan.
    A "press your luck" game where you roll dice with Stars, Skulls, and
    Question Marks.
    On your turn, you pull three random dice from the dice cup and roll
    them. You can roll Stars, Skulls, and Question Marks. You can end your
    turn and get one point per Star. If you choose to roll again, you keep
    the Question Marks and pull new dice to replace the Stars and Skulls.
    If you collect three Skulls, you lose all your Stars and end your turn.
    
    When a player gets 13 points, everyone else gets one more turn before
    the game ends. Whoever has the most points wins.
    
    There are 6 Gold dice, 4 Silver dice, and 3 Bronze dice in the cup.
    Gold dice have more Stars, Bronze dice have more Skulls, and Silver is
      even.
""")

print('How many players are there?')
while True: # Выполняем цикл, пока пользователь не введет число.
    response = input('> ')
    if response.isdecimal() and int(response) > 1:
        numPlayers = int(response)
        break
    print('Please enter a number larger than 1.')
playerNames = [] # Список строковых значений с именами игроков.
playerScores = {} # Ключами служат имена игроков, значениями — счет в виде целых чисел.

for i in range(numPlayers):
    while True: # Выполняем цикл, пока пользователь не введет имя.
        print('What is player #' + str(i + 1) + '\'s name?')
        response = input('> ')
        if response != '' and response not in playerNames:
            playerNames.append(response)
            playerScores[response] = 0
            break
        print('Please enter a name.')
print()

turn = 0 # Первый ход — игрока из playerNames[0].
# (!) Раскомментируйте, чтобы игрок 'Al' начал игру с тремя очками:
# playerScores['Al'] = 3
endGameWith = None
while True: # Основной цикл игры.
    # Отображаем счет всех игроков:
    print()
    print('SCORES: ', end='')
    for i, name in enumerate(playerNames):
        print(name + ' = ' + str(playerScores[name]), end='')
        if i != len(playerNames) - 1:
            # Имена всех игроков, кроме последнего, отделены запятыми.
            print(', ', end='')
    print('\n')

    # Изначально количество собранных "звезд" и "черепов" равно 0.
    stars = 0
    skulls = 0
    # В чашке — шесть золотых костей, четыре серебряные и три бронзовые:
    cup = ([GOLD] * 6) + ([SILVER] * 4) + ([BRONZE] * 3)
    hand = [] # Сначала у вас нет никаких костей.
    print('It is ' + playerNames[turn] + '\'s turn.')
    while True: # Каждая итерация цикла соответствует броску костей.
        print()

        # Убеждаемся, что в чашке осталось достаточно костей:
        if (3 - len(hand)) > len(cup):
            # Переход хода, поскольку костей в чашке недостаточно:
            print('There aren\'t enough dice left in the cup to ' + 'continue ' + playerNames[turn] + '\'s turn.')
            break

        # Берем кости из чашки, пока в руках у игрока не будет три:
        random.shuffle(cup) # Перемешиваем кости в чашке.
        while len(hand) < 3:
            hand.append(cup.pop())

        # Бросаем кости:
        rollResults = []
        for dice in hand:
            roll = random.randint(1, 6)
            if dice == GOLD:
            # Бросаем золотую кость (три "звезды", два "знака вопроса", один "череп"):
                if 1 <= roll <= 3:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 4 <= roll <= 5:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1
            if dice == SILVER:
            # Бросаем серебряную кость (две "звезды", два "знака вопроса", два "черепа"):
                if 1 <= roll <= 2:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 3 <= roll <= 4:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1
            if dice == BRONZE:
                # Бросаем бронзовую кость (одна "звезда", два "знака вопроса", три "черепа"):
                if roll == 1:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 2 <= roll <= 4:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1

        # Отображаем результаты броска:
        for lineNum in range(FACE_HEIGHT):
            for diceNum in range(3):
                print(rollResults[diceNum][lineNum] + ' ', end='')
            print() # Выводим символ новой строки.

        # Отображаем типы всех костей (золотая, серебряная, бронзовая):
        for diceType in hand:
            print(diceType.center(FACE_WIDTH) + ' ', end='')
        print() # Выводим символ новой строки.

        print('Stars collected:', stars, 'Skulls collected:', skulls)

        # Проверяем, не собрал ли игрок три и более "черепа":
        if skulls >= 3:
            print('3 or more skulls means you\'ve lost your stars!')
            input('Press Enter to continue...')
            break

        print(playerNames[turn] + ', do you want to roll again? Y/N')
        while True: # Продолжаем спрашивать игрока, пока он не введет Y или N:
            response = input('> ').upper()
            if response != '' and response[0] in ('Y', 'N'):
                break
            print('Please enter Yes or No.')

        if response.startswith('N'):
            print(playerNames[turn], 'got', stars, 'stars!')
            # Добавляем «звезды» к общему счету этого игрока:
            playerScores[playerNames[turn]] += stars

            # Check if they've reached 13 or more points:
            # (!) Попробуйте заменить это значение на 5 или 50 очков.
            if (endGameWith == None
                and playerScores[playerNames[turn]] >= 13):
                # Поскольку этот игрок набрал 13 очков, позволяем
                # остальным игрокам сыграть еще один раунд:
                print('\n\n' + ('!' * 60))
                print(playerNames[turn] + ' has reached 13 points!!!')
                print('Everyone else will get one more turn!')
                print(('!' * 60) + '\n\n')
                endGameWith = playerNames[turn]
            input('Press Enter to continue...')
            break

        # Игнорируем "звезды" и "черепа", но сохраняем "знаки вопроса":
        nextHand = []
        for i in range(3):
            if rollResults[i] == QUESTION_FACE:
                nextHand.append(hand[i])     # Сохраняем "знаки вопроса".
        hand = nextHand

    # Ход переходит к следующему игроку:
    turn = (turn + 1) % numPlayers

    # Если игра окончена, выходим из цикла:
    if endGameWith == playerNames[turn]:
        break    # Конец игры.

print('The game has ended...')

# Отображаем счет всех игроков:
print()
print('SCORES: ', end='')
for i, name in enumerate(playerNames):
    print(name + ' = ' + str(playerScores[name]), end='')
    if i != len(playerNames) - 1:
        # Имена всех игроков, кроме последнего, отделены запятыми.
        print(', ', end='')
print('\n')

# Определяем победителей:
highestScore = 0
winners = []
for name, score in playerScores.items():
    if score > highestScore:
        # Максимальный счет — у этого игрока:
        highestScore = score
        winners = [name]    # Перезаписываем всех предыдущих победителей.
    elif score == highestScore:
        # У этого игрока — ничья с максимальным счетом.
        winners.append(name)

if len(winners) == 1:
    # Победитель только один:
    print('The winner is ' + winners[0] + '!!!')
else:
    # Несколько победителей с одинаковым счетом:
    print('The winners are: ' + ', '.join(winners))

print('Thanks for playing!')
