"""Я обвиняю!, (c) Sayfullin Ruslan.
Детективная игра с обманом и пропавшей кошкой
"""

import time
import random
import sys

# Задаем константы:
SUSPECTS = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR',
            'MRS. FEATHERTOSS', 'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT', 'CECIL EDGAR VANDERTON']
ITEMS = ['FLASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'ANIME VHS TAPE', 'JAR OF PICKLES',
         'ONE COWBOY BOOT', 'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD']
PLACES = ['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE', 'BOWLING ALLEY', 'VIDEO GAME MUSEUM',
          'UNIVERSITY LIBRARY', 'ALBINO ALLIGATOR PIT']
TIME_TO_SOLVE = 300 # Длительность игры — 300 секунд (5 минут).
# Первые буквы и максимальная длина мест действия необходимы для отображения
# меню:
PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)

# Основные проверки корректности констант:
assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9
# Первые буквы не должны повторяться:
assert len(PLACE_FIRST_LETTERS.keys()) == len(PLACES)

knownSuspectsAndItems = []
# visitedPlaces: ключи — места действия, значения —строковые значения для находящихся там подозреваемых и предметов.
visitedPlaces = {}
currentLocation = 'TAXI'     # Начинаем игру в такси.
accusedSuspects = []     # Обвиненные подозреваемые никаких зацепок не дают.
liars = random.sample(SUSPECTS, random.randint(3, 4))
accusationsLeft = 3  # Вы можете обвинить не более трех человек.
culprit = random.choice(SUSPECTS)
# Ссылки на общие индексы; например, SUSPECTS[0] и ITEMS[0] находятся
# в PLACES[0].
random.shuffle(SUSPECTS)
random.shuffle(ITEMS)
random.shuffle(PLACES)

# Создаем структуры данных для зацепок, полученных от говорящих правду
# о каждом из предметов и подозреваемых.
# clues: ключи — подозреваемые, у которых попросили зацепку, значение — "ассоциативный массив зацепок".
clues = {}
for i, interviewee in enumerate(SUSPECTS):
    if interviewee in liars:
        continue # Пока пропускаем лжецов.

    # Ключи в этом "ассоциативном массиве зацепок" — предметы
    # и подозреваемые, значения — полученные зацепки.
    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = False     # Удобно для отладки.

    for item in ITEMS:   # Выбираем зацепки относительно всех предметов.
        if random.randint(0, 1) == 0:    # Говорит, где находится предмет:
            clues[interviewee][item] = PLACES[ITEMS.index(item)]
        else:    # Говорит, у кого предмет:
            clues[interviewee][item] = SUSPECTS[ITEMS.index(item)]
    for suspect in SUSPECTS:    # Выбираем зацепки относительно всех подозреваемых.
        if random.randint(0, 1) == 0:   # Говорит, где находится подозреваемый:
            clues[interviewee][suspect] = PLACES[SUSPECTS.index(suspect)]
        else: # Говорит, какой предмет есть у подозреваемого:
            clues[interviewee][suspect] = ITEMS[SUSPECTS.index(suspect)]

# Создаем структуры данных для получаемых от лжецов зацепок относительно всех предметов и подозреваемых:
for i, interviewee in enumerate(SUSPECTS):
    if interviewee not in liars:
        continue # Мы уже обработали тех, кто говорит правду.

    # Ключи в этом "ассоциативном массиве зацепок" — предметы
    # и подозреваемые, значения — полученные зацепки.
    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = True  # Удобно для отладки.

    # Этот опрашиваемый подозреваемый – лжец, и его зацепки ложны:
    for item in ITEMS:
        if random.randint(0, 1) == 0:
            while True: # Выбираем случайное (неправильное) место.
                # Лжет относительно местонахождения предмета.
                clues[interviewee][item] = random.choice(PLACES)
                if clues[interviewee][item] != PLACES[ITEMS.index(item)]:
                    # Выходим из цикла после выбора ложной зацепки.
                    break
        else:
            while True:  # Выбираем случайного (неправильного) подозреваемого.
                clues[interviewee][item] = random.choice(SUSPECTS)
                if clues[interviewee][item] != SUSPECTS[ITEMS.index(item)]:
                    # Выходим из цикла после выбора ложной зацепки.
                    break
    for suspect in SUSPECTS:
        if random.randint(0, 1) == 0:
            while True:  # Выбираем случайное (неправильное) место.
                clues[interviewee][suspect] = random.choice(PLACES)
                if clues[interviewee][suspect] != PLACES[ITEMS.index(item)]:
                    # Выходим из цикла после выбора ложной зацепки.
                    break
        else:
            while True: # Выбираем случайный (неправильный) предмет.
                clues[interviewee][suspect] = random.choice(ITEMS)
                if clues[interviewee][suspect] != ITEMS[SUSPECTS.index(suspect)]:
                    # Выходим из цикла после выбора ложной зацепки.
                    break

# Создаем структуры данных для ответов на вопросы о Зофи:
zophieClues = {}
for interviewee in random.sample(SUSPECTS, random.randint(3, 4)):
    kindOfClue = random.randint(1, 3)
    if kindOfClue == 1:
        if interviewee not in liars:
            # (Правдиво) отвечают, у кого Зофи.
            zophieClues[interviewee] = culprit
        elif interviewee in liars:
            while True:
                # Выбираем (неправильного) подозреваемого.
                zophieClues[interviewee] = random.choice(SUSPECTS)
                if zophieClues[interviewee] != culprit:
                    # Выходим из цикла после выбора ложной зацепки.
                    break

    elif kindOfClue == 2:
        if interviewee not in liars:
            # (Правдиво) отвечают, где Зофи.
            zophieClues[interviewee] = PLACES[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                # Выбираем случайное (неправильное) место.
                zophieClues[interviewee] = random.choice(PLACES)
                if zophieClues[interviewee] != PLACES[SUSPECTS.index(culprit)]:
                    # Выходим из цикла после выбора ложной зацепки.
                    break

    elif kindOfClue == 3:
        if interviewee not in liars:
            # (Правдиво) отвечают, близ какого предмета находится Зофи.
            zophieClues[interviewee] = ITEMS[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                # Выбираем случайный (неправильный) предмет.
                zophieClues[interviewee] = random.choice(ITEMS)
                if zophieClues[interviewee] != ITEMS[SUSPECTS.index(culprit)]:
                    # Выходим из цикла после выбора ложной зацепки.
                    break

# Эксперимент: раскомментируйте этот код, чтобы посмотреть на содержимое
# структур данных с зацепками:
#import pprint
#pprint.pprint(clues)
#pprint.pprint(zophieClues)
#print('culprit =', culprit)
# НАЧАЛО ИГРЫ
print("""J'ACCUSE! (a mystery game)")
By Sayfullin Ruslan
Inspired by Homestar Runner\'s "Where\'s an Egg?" game
You are the world-famous detective Mathilde Camus.
ZOPHIE THE CAT has gone missing, and you must sift through the clues.
Suspects either always tell lies, or always tell the truth. Ask them
about other people, places, and items to see if the details they give are
truthful and consistent with your observations. Then you will know if
their clue about ZOPHIE THE CAT is true or not. Will you find ZOPHIE THE
CAT in time and accuse the guilty party?
""")
input('Press Enter to begin...')

startTime = time.time()
endTime = startTime + TIME_TO_SOLVE

while True: # Основной цикл игры.
    if time.time() > endTime or accusationsLeft == 0:
        # Обрабатываем условие "игра окончена":
        if time.time() > endTime:
            print('You have run out of time!')
        elif accusationsLeft == 0:
            print('You have accused too many innocent people!')
        culpritIndex = SUSPECTS.index(culprit)
        print('It was {} at the {} with the {} who catnapped her!'.
        format(culprit, PLACES[culpritIndex], ITEMS[culpritIndex]))
        print('Better luck next time, Detective.')
        sys.exit()

    print()
    minutesLeft = int(endTime - time.time()) // 60
    secondsLeft = int(endTime - time.time()) % 60
    print('Time left: {} min, {} sec'.format(minutesLeft, secondsLeft))

    if currentLocation == 'TAXI':
        print(' You are in your TAXI. Where do you want to go?')
        for place in sorted(PLACES):
            placeInfo = ''
            if place in visitedPlaces:
                placeInfo = visitedPlaces[place]
            nameLabel = '(' + place[0] + ')' + place[1:]
            spacing = " " * (LONGEST_PLACE_NAME_LENGTH - len(place))
            print('{} {}{}'.format(nameLabel, spacing, placeInfo))
        print('(Q)UIT GAME')
        while True:  # Продолжаем спрашивать, пока не получим допустимый ответ.
            response = input('> ').upper()
            if response == '':
                continue # Спрашиваем снова.
            if response == 'Q':
                print('Thanks for playing!')
                sys.exit()
            if response in PLACE_FIRST_LETTERS.keys():
                break
        currentLocation = PLACE_FIRST_LETTERS[response]
        continue     # Возвращаемся к началу основного цикла игры.

    # Находимся в одном из мест; игрок может запрашивать зацепки.
    print(' You are at the {}.'.format(currentLocation))
    currentLocationIndex = PLACES.index(currentLocation)
    thePersonHere = SUSPECTS[currentLocationIndex]
    theItemHere = ITEMS[currentLocationIndex]
    print(' {} with the {} is here.'.format(thePersonHere, theItemHere))

    # Добавляем находящихся в этом месте подозреваемого и предмет
    # в наш список известных подозреваемых и предметов:
    if thePersonHere not in knownSuspectsAndItems:
        knownSuspectsAndItems.append(thePersonHere)
    if ITEMS[currentLocationIndex] not in knownSuspectsAndItems:
        knownSuspectsAndItems.append(ITEMS[currentLocationIndex])
    if currentLocation not in visitedPlaces.keys():
        visitedPlaces[currentLocation] = '({}, {})'.format(thePersonHere.lower(), theItemHere.lower())

    # Обвиненные ранее ошибочно подозреваемые не дают
    # игроку зацепок:
    if thePersonHere in accusedSuspects:
        print('They are offended that you accused them,')
        print('and will not help with your investigation.')
        print('You go back to your TAXI.')
        print()
        input('Press Enter to continue...')
        currentLocation = 'TAXI'
        continue # Возвращаемся к началу основного цикла игры.
    # Отображаем меню с известными подозреваемыми и предметами, о которых
    # можно спросить:
    print()
    print('(J) "J\'ACCUSE!" ({} accusations left)'.format(accusationsLeft))
    print('(Z) Ask if they know where ZOPHIE THE CAT is.')
    print('(T) Go back to the TAXI.')
    for i, suspectOrItem in enumerate(knownSuspectsAndItems):
        print('({}) Ask about {}'.format(i + 1, suspectOrItem))

    while True:     # Продолжаем спрашивать, пока не получим допустимый ответ.
        response = input('> ').upper()
        if response in 'JZT' or (response.isdecimal() and 0 < int(response) <=
        len(knownSuspectsAndItems)):
            break

    if response == 'J':     # Игрок обвиняет этого подозреваемого.
        accusationsLeft -= 1    # Учитываем использованное обвинение.
        if thePersonHere == culprit:
            # Вы обвинили того, кого нужно.
            print('You\'ve cracked the case, Detective!')
            print('It was {} who had catnapped ZOPHIE THE CAT.'.format(culprit))
            minutesTaken = int(time.time() - startTime) // 60
            secondsTaken = int(time.time() - startTime) % 60
            print('Good job! You solved it in {} min, {}sec.'.format(minutesTaken, secondsTaken))
            sys.exit()
        else:
            # Вы обвинили не того, кого нужно.
            accusedSuspects.append(thePersonHere)
            print('You have accused the wrong person, Detective!')
            print('They will not help you with anymore clues.')
            print('You go back to your TAXI.')
            currentLocation = 'TAXI'

    elif response == 'Z':    # Игрок спрашивает о Зофи.
        if thePersonHere not in zophieClues:
            print('"I don\'t know anything about ZOPHIE THE CAT."')
        elif thePersonHere in zophieClues:
            print(' They give you this clue:"{}"'.format(zophieClues[thePersonHere]))
            # Добавляем не относящиеся к местам зацепки в список известного:
            if zophieClues[thePersonHere] not in knownSuspectsAndItems and zophieClues[thePersonHere] not in PLACES:
                knownSuspectsAndItems.append(zophieClues[thePersonHere])

    elif response == 'T':   # Игрок возвращается в такси.
        currentLocation = 'TAXI'
        continue    # Возвращаемся к началу основного цикла игры.

    else:    # Игрок спрашивает о подозреваемом или предмете.
        thingBeingAskedAbout = knownSuspectsAndItems[int(response) - 1]
        if thingBeingAskedAbout in (thePersonHere, theItemHere):
            print(' They give you this clue: "No comment."')
        else:
            print(' They give you this clue:"{}"'.format(clues[thePersonHere][thingBeingAskedAbout]))
            # Добавляем не относящиеся к местам зацепки в список известного:
            if clues[thePersonHere][thingBeingAskedAbout] not in knownSuspectsAndItems and clues[thePersonHere][thingBeingAskedAbout] not in PLACES:
                knownSuspectsAndItems.append(clues[thePersonHere][thingBeingAskedAbout])

    input('Press Enter to continue...')
