"""Угадай число, , (c) Sayfullin Ruslan.
Угадайте загаданное число по подсказкам.
"""

import random


def askForGuess():
    while True:
        guess = input('> ')  # Введите свое предположение.

        if guess.isdecimal():
            return int(guess)   # Преобразуем строковое представление предположения в число.
        print('Please enter a number between 1 and 100.')

print('Guess the Number, by (c) Sayfullin Ruslan.')
print()
secretNumber = random.randint(1, 100) # Выбираем случайное число.
print('I am thinking of a number between 1 and 100.')

for i in range(10):     # У игрока есть 10 попыток.
    print('You have {} guesses left. Take a guess.'.format(10 - i))

    guess = askForGuess()
    if guess == secretNumber:
        break   # Если число угадано — выходим из цикла.

    # Даем подсказку:
    if guess < secretNumber:
        print('Your guess is too low.')
    if guess > secretNumber:
        print('Your guess is too high.')

# Раскрываем результаты:
if guess == secretNumber:
    print('Yay! You guessed my number!')
else:
    print('Game over. The number I was thinking of was', secretNumber)
