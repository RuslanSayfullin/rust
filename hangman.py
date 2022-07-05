"""Виселица, (c) Sayfullin Ruslan.
Угадайте буквы загаданного слова, пока не будет нарисована виселица.
"""


import random
import sys
# Задаем константы:
# (!) Попробуйте добавить в HANGMAN_PICS новые строковые значения
# или изменить существующие, чтобы рисовать гильотину вместо виселицы.
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]
# (!) Попробуйте заменить константы CATEGORY и WORDS на другие строковые
# значения.
CATEGORY = 'Animals'
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()

def main():
    print('Hangman, by Sayfullin Ruslan.')

    # Переменные для новой игры:
    missedLetters = []      # Список неправильных попыток угадать буквы.
    correctLetters = []     # Список правильных попыток угадать буквы.
    secretWord = random.choice(WORDS)   # Загаданное слово.

    while True: # Основной цикл игры.
        drawHangman(missedLetters, correctLetters, secretWord)

        # Пусть пользователь введет свою букву:
        guess = getPlayerGuess(missedLetters + correctLetters)

        if guess in secretWord:
            # Добавляем правильную догадку в correctLetters:
            correctLetters.append(guess)
            # Проверяем, не выиграл ли игрок:
            foundAllLetters = True # Начинаем с предположения, что он выиграл.
            for secretWordLetter in secretWord:
                if secretWordLetter not in correctLetters:
                    # В загаданном слове есть буква, пока еще отсутствующая
                    # в correctLetters, так что игрок пока что не выиграл:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is:', secretWord)
                print('You have won!')
                break # Выходим из основного цикла игры.
        else:
            # Игрок не угадал:
            missedLetters.append(guess)

            # Проверяем, не превысил ли игрок допустимое количество попыток
            # и проиграл. ("- 1", поскольку пустая виселица в
            # HANGMAN_PICS не считается)
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                drawHangman(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!')
                print('The word was "{}"'.format(secretWord))
                break


def drawHangman(missedLetters, correctLetters, secretWord):
    """Рисуем текущее состояние виселицы вместе с неугаданными
    и правильно угаданными буквами загаданного слова."""
    print(HANGMAN_PICS[len(missedLetters)])
    print('The category is:', CATEGORY)
    print()

    # Отображаем неправильные попытки угадать букву:
    print('Missed letters: ', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    if len(missedLetters) == 0:
        print('No missed letters yet.')
    print()

    # Отображаем пропуски вместо загаданного слова (по одному на букву):
    blanks = ['_'] * len(secretWord)

    # Заменяем пропуски на угаданные буквы:
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]

    # Отображаем загаданное слово с пропусками между буквами:
    print(' '.join(blanks))


def getPlayerGuess(alreadyGuessed):
    """Возвращает введенную пользователем букву. Убеждается,
    что пользователь ввел одну букву, которую не вводил ранее."""
    while True:     # Запрашиваем, пока пользователь не введет допустимую букву.
        print('Guess a letter.')
        guess = input('> ').upper()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a LETTER.')
        else:
            return guess


# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()   # Если нажато Ctrl+C — завершаем программу.
