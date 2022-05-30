"""Бейглз,
Дедуктивная логическая игра на угадывание числа по подсказкам."""

import random

NUM_DIGITS = 3   # (!) Попробуйте задать эту константу равной 1 или 10.
MAX_GUESSES = 10    # (!) Попробуйте задать эту константу равной 1 или 100.


def main():
    print('''Bagels, a deductive logic game.
          I am thinking of a {}-digit number with no repeated digits.
            Try to guess what it is. Here are some clues:
            When I say:
            That means:
            Pico
            One digit is correct but in the wrong position.
            Fermi
            One digit is correct and in the right position.
            Bagels
            No digit is correct.
            For example, if the secret number was 248 and your guess was 843, the
            clues would be Fermi Pico.'''.format(NUM_DIGITS)
          )

    while True: # Основной цикл игры.
        # Переменная, в которой хранится секретное число, которое
        secretNum = getSecretNum() # должен угадать игрок
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Продолжаем итерации до получения правильной догадки:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break   # Правильно, выходим из цикла.
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        # Спрашиваем игрока, хочет ли он сыграть еще раз.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretNum():
    """Возвращает строку из NUM_DIGITS уникальных случайных цифр."""
    numbers = list('0123456789')    # Создает список цифр от 0 до 9.
    random.shuffle(numbers)  # Перетасовываем их случайным образом.

    # Берем первые NUM_DIGITS цифр списка для нашего секретного числа:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Возвращает строку с подсказками pico, fermi и bagels
    для полученной на входе пары из догадки и секретного числа."""
    if guess == secretNum:
        return 'You got it!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Правильная цифра на правильном месте.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # Правильная цифра на неправильном месте.
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels' # Правильных цифр нет вообще.
    else:
        # Сортируем подсказки в алфавитном порядке, чтобы их исходный
        # порядок ничего не выдавал.
        clues.sort()
        # Склеиваем список подсказок в одно строковое значение.
        return ' '.join(clues)


# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    main()
