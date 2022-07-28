"""Три карты Монте, (c) Sayfullin Ruslan aka CryptoLis.
Найдите даму червей после перемешивания карт.
(В реальной жизни мошенник обычно прячет даму червей в руке, так что вы никогда не выиграете.)
"""

import random, time

# Задаем константы:
NUM_SWAPS = 16          # (!) Попробуйте заменить это значение на 30 или 100.
DELAY = 0.8             # (!) Попробуйте заменить это значение на 2.0 или 0.0.

# Символы карточных мастей:
HEARTS = chr(9829)      # Символ 9829 – '♥'
DIAMONDS = chr(9830)    # Символ 9830 – '♦'
SPADES = chr(9824)      # Символ 9824 – '♠'
CLUBS = chr(9827)       # Символ 9827 – '♣'
# Список кодов chr можно найти на https://inventwithpython.com/chr

# Индексы списка из трех карт:
LEFT = 0
MIDDLE = 1
RIGHT = 2


def displayCards(cards):
    """Отображает карты из списка cards кортежей (достоинство, масть).
    """
    rows = ['', '', '', '', '']     # Содержит текст для вывода на экран.

    for i, card in enumerate(cards):
        rank, suit = card   # card представляет собой структуру данных — кортеж.
        rows[0] += ' ___ '  # Выводим верхнюю линию карты.
        rows[1] += '|{} | '.format(rank.ljust(2))
        rows[2] += '| {} | '.format(suit)
        rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # Построчно выводим на экран:
    for i in range(5):
        print(rows[i])


def getRandomCard():
    """Возвращает случайную карту — НЕ даму червей."""
    while True:     # Подбираем карты, пока не получим НЕ даму червей.
        rank = random.choice(list('23456789JQKA') + ['10'])
        suit = random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])
        # Возвращаем карту, если это не дама червей:
        if rank != 'Q' and suit != HEARTS:
            return (rank, suit)

print('Three-Card Monte, by Sayfullin Ruslan aka CryptoLis.')
print()
print('Find the red lady (the Queen of Hearts)! Keep an eye on how')
print('the cards move.')
print()

# Отображаем исходную раскладку карт:
cards = [('Q', HEARTS), getRandomCard(), getRandomCard()]
random.shuffle(cards) # Помещаем даму червей в случайное место.
print('Here are the cards:')
displayCards(cards)
input('Press Enter when you are ready to begin...')


# Отображаем на экране перетасовки карт:
for i in range(NUM_SWAPS):
    swap = random.choice(['l-m', 'm-r', 'l-r', 'm-l', 'r-m', 'r-l'])

    if swap == 'l-m':
        print('swapping left and middle...')
        cards[LEFT], cards[MIDDLE] = cards[MIDDLE], cards[LEFT]
    elif swap == 'm-r':
        print('swapping middle and right...')
        cards[MIDDLE], cards[RIGHT] = cards[RIGHT], cards[MIDDLE]
    elif swap == 'l-r':
        print('swapping left and right...')
        cards[LEFT], cards[RIGHT] = cards[RIGHT], cards[LEFT]
    elif swap == 'm-l':
        print('swapping middle and left...')
        cards[MIDDLE], cards[LEFT] = cards[LEFT], cards[MIDDLE]
    elif swap == 'r-m':
        print('swapping right and middle...')
        cards[RIGHT], cards[MIDDLE] = cards[MIDDLE], cards[RIGHT]
    elif swap == 'r-l':
        print('swapping right and left...')
        cards[RIGHT], cards[LEFT] = cards[LEFT], cards[RIGHT]

    time.sleep(DELAY)

# Выводим несколько символов новой строки, чтобы скрыть перетасовки.
print('\n' * 60)

# Просим пользователя найти даму червей:
while True: # Спрашиваем, пока не будет введено LEFT, MIDDLE или RIGHT.
    print('Which card has the Queen of Hearts? (LEFT MIDDLE RIGHT)')
    guess = input('> ').upper()

    # Находим индекс в cards введенной пользователем позиции:
    if guess in ['LEFT', 'MIDDLE', 'RIGHT']:
        if guess == 'LEFT':
            guessIndex = 0
        elif guess == 'MIDDLE':
            guessIndex = 1
        elif guess == 'RIGHT':
            guessIndex = 2
        break


# (!) Раскомментируйте этот код, чтобы игрок всегда проигрывал:
#if cards[guessIndex] == ('Q', HEARTS):
#   # Игрок выиграл, так что перемещаем даму.
#   possibleNewIndexes = [0, 1, 2]
#   possibleNewIndexes.remove(guessIndex) # Убираем индекс дамы.
#   newInd = random.choice(possibleNewIndexes) # Выбираем новый индекс.
#   # Помещаем даму червей на позицию, соответствующую новому индексу:
#   cards[guessIndex], cards[newInd] = cards[newInd], cards[guessIndex]

displayCards(cards)     # Отображаем все карты.

# Проверяем, выиграл ли игрок:
if cards[guessIndex] == ('Q', HEARTS):
    print('You won!')
    print('Thanks for playing!')
else:
    print('You lost!')
    print('Thanks for playing, sucker!')
