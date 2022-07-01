"""Мини-игра со взломом, (c) Sayfullin Ruslan.
Мини-игра со взломом из Fallout 3. Найдите семибуквенное слово-пароль
с помощью подсказок, возвращаемых при каждой попытке угадать его.
"""

# Примечание: для этой программы необходим файл sevenletterwords.txt.
# Скачать его можно на https://inventwithpython.com/sevenletterwords.txt

import random
import sys

# Задаем константы:
# Заполнитель мусорными символами для "памяти компьютера".
GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'

# Загружаем список WORDS из текстового файла с семибуквенными словами.
with open('sevenletterwords.txt') as wordListFile:
    WORDS = wordListFile.readlines()
for i in range(len(WORDS)):
    # Преобразуем каждое слово в верхний регистр и удаляем символ новой строки
    # в конце:

    WORDS[i] = WORDS[i].strip().upper()
def main():
    """Запуск одной игры со взломом."""
    print('''Hacking Minigame, by Sayfullin Ruslan
    Find the password in the computer's memory. You are given clues after
    each guess. For example, if the secret password is MONITOR but the
    player guessed CONTAIN, they are given the hint that 2 out of 7 letters
    were correct, because both MONITOR and CONTAIN have the letter O and N
    as their 2nd and 3rd letter. You get four guesses.\n''')
    input('Press Enter to begin...')
    gameWords = getWords()
    # "Память компьютера" — только для вида, но выглядит круто:
    computerMemory = getComputerMemoryString(gameWords)
    secretPassword = random.choice(gameWords)

    print(computerMemory)
    # Начинаем с четырех оставшихся попыток и постепенно уменьшаем
    # их количество:
    for triesRemaining in range(4, 0, -1):
        playerMove = askForPlayerGuess(gameWords, triesRemaining)
        if playerMove == secretPassword:
            print('A C C E S S G R A N T E D')
            return
        else:
            numMatches = numMatchingLetters(secretPassword, playerMove)
            print('Access Denied ({}/7 correct)'.format(numMatches))
    print('Out of tries. Secret password was {}.'.format(secretPassword))

def getWords():
    """Возвращает список из 12 слов — возможных паролей.

    Секретный пароль будет первым словом в списке.
    Ради честной игры мы попытаемся гарантировать наличие слов
    с различным количеством совпадающих с паролем букв."""
    secretPassword = random.choice(WORDS)
    words = [secretPassword]

    # Находим еще два слова; количество совпадающих букв — 0.
    # "< 3" потому, что секретный пароль уже входит в список слов.
    while len(words) < 3:
        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 0:
            words.append(randomWord)

    # Находим два слова, у которых совпадает три буквы
    # (но прекращаем поиск после 500 попыток, если не удалось найти).
    for i in range(500):
        if len(words) == 5:
            break    # Нашли пять слов, так что выходим из цикла.

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 3:
            words.append(randomWord)

    # Находим по крайней мере семь слов, у которых совпадает хотя бы одна
    # буква (но прекращаем поиск после 500 попыток, если не удалось найти).
    for i in range(500):
        if len(words) == 12:
            break    # Нашли 7 или более слов, так что выходим из цикла.

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) != 0:
            words.append(randomWord)

    # Добавляем любые случайные слова, чтобы всего их было 12.
    while len(words) < 12:
        randomWord = getOneWordExcept(words)
        words.append(randomWord)

    assert len(words) == 12
    return words


def getOneWordExcept(blocklist=None):
    """Возвращает случайное слово из списка WORDS, не входящее в blocklist."""
    if blocklist == None:
        blocklist = []

    while True:
        randomWord = random.choice(WORDS)
        if randomWord not in blocklist:
            return randomWord


def numMatchingLetters(word1, word2):
    """Возвращает число совпадающих букв в указанных двух словах."""
    matches = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            matches += 1
    return matches


def getComputerMemoryString(words):
    """Возвращает строковое значение, соответствующее "памяти компьютера"."""

    # Выбираем по одной содержащей слово строке. Всего строк 16,
    # но они разбиты на две половины.
    linesWithWords = random.sample(range(16 * 2), len(words))
    # Начальный адрес памяти (также только для вида).
    memoryAddress = 16 * random.randint(0, 4000)
    # Создаем строковое значение для "памяти компьютера".
    computerMemory = [] # Будет включать 16 строковых значений, по одному на строку.
    nextWord = 0 # Индекс в WORDS слова, помещаемого в строку.
    for lineNum in range(16): # "Память компьютера" содержит 16 строк.
        # Создаем половину строки мусорных символов:
        leftHalf = ''
        rightHalf = ''
        for j in range(16):     # Каждая половина содержит 16 символов.
            leftHalf += random.choice(GARBAGE_CHARS)
            rightHalf += random.choice(GARBAGE_CHARS)
        # Заполняем пароль из WORDS:
        if lineNum in linesWithWords:
            # Находим случайное место для вставки слова в половине строки:
            insertionIndex = random.randint(0, 9)
            # Вставляем слово:
            leftHalf = (leftHalf[:insertionIndex] + words[nextWord] + leftHalf[insertionIndex + 7:])
            nextWord += 1   # Обновляем слово для вставки в половину строки.
        if lineNum + 16 in linesWithWords:
            # Находим случайное место в половине строки для вставки слова:
            insertionIndex = random.randint(0, 9)
            # Вставляем слово:
            rightHalf = (rightHalf[:insertionIndex] + words[nextWord] + rightHalf[insertionIndex + 7:])
            nextWord += 1   # Обновляем слово для вставки в половину строки.

        computerMemory.append('0x' + hex(memoryAddress)[2:].zfill(4)
            + ' ' + leftHalf + ' '
            + '0x' + hex(memoryAddress + (16*16))[2:].zfill(4)
            + ' ' + rightHalf)
        memoryAddress += 16  # Перескакиваем, скажем, с 0xe680 на 0xe690.

    # Все строковые значения списка computerMemory для возвращения
    # объединяются в одно большое строковое значение:
    return '\n'.join(computerMemory)


def askForPlayerGuess(words, tries):
    """Ввод пользователем догадки."""
    while True:
        print('Enter password: ({} tries remaining)'.format(tries))
        guess = input('> ').upper()
        if guess in words:
            return guess
        print('That is not one of the possible passwords listed above.')
        print('Try entering "{}" or "{}".'.format(words[0], words[1]))


# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Если нажато Ctrl+C — завершаем программу.
