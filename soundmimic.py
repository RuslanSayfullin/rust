"""Повторение музыки, (c) Sayfullin Ruslan.
Игра с подбором звуковых соответствий. Попробуйте запомнить все
возрастающую последовательность букв. Создана под впечатлением
от электронной игры "Саймон".
"""
import random, sys, time

# Скачайте звуковые файлы с этих URL (или воспользуйтесь своими):
# https://inventwithpython.com/soundA.wav
# https://inventwithpython.com/soundS.wav
# https://inventwithpython.com/soundD.wav
# https://inventwithpython.com/soundF.wav


try:
    import playsound
except ImportError:
    print('The playsound module needs to be installed to run this')
    print('program. On Windows, open a Command Prompt and run:')
    print('pip install playsound')
    print('On macOS and Linux, open a Terminal and run:')
    print('pip3 install playsound')
    sys.exit()

print('''Sound Mimic, by Sayfullin Ruslan
Try to memorize a pattern of A S D F letters (each with its own sound)
as it gets longer and longer.''')

input('Press Enter to begin...')

pattern = ''
while True:
    print('\n' * 60)    # Очищаем экран, выводя несколько символов новой строки.

    # Добавляем в pattern случайную букву:
    pattern = pattern + random.choice('ASDF')

    # Выводим pattern на экран (и проигрываем соответствующие звуки):
    print('Pattern: ', end='')
    for letter in pattern:
        print(letter, end=' ', flush=True)
        playsound.playsound('sound' + letter + '.wav')

    time.sleep(1)       # Добавляем в конце небольшую паузу.
    print('\n' * 60)    # Очищаем экран с помощью вывода нескольких символов новой строки.
    # Просим пользователя ввести последовательность:
    print('Enter the pattern:')
    response = input('> ').upper()

    if response != pattern:
        print('Incorrect!')
        print('The pattern was', pattern)
    else:
        print('Correct!')

    for letter in pattern:
        playsound.playsound('sound' + letter + '.wav')

    if response != pattern:
        print('You scored', len(pattern) - 1, 'points.')
        print('Thanks for playing!')
        break

    time.sleep(1)
