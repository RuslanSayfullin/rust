"""Leet, (c) Sayfullin Ruslan.
Переводит сообщения на английском языке в l33t.
"""

import random

try:
    import pyperclip # pyperclip копирует текст в буфер обмена.
except ImportError:
    pass # Если pyperclip не установлена, ничего не делаем. Не проблема.

def main():
    print('''L3375P34]< (leetspeek)
    By (c) Sayfullin Ruslan.
    Enter your leet message:''')
    english = input('> ')
    print()
    leetspeak = englishToLeetspeak(english)
    print(leetspeak)

    try:
        # Попытка использования pyperclip, если библиотека
        # не импортирована, приведет к генерации исключения NameError:
        pyperclip.copy(leetspeak)
        print('(Copied leetspeak to clipboard.)')
    except NameError:
        pass # Если pyperclip не установлена, ничего не делаем.


def englishToLeetspeak(message):
    """Преобразует строковое значение на английском языке из message
    в leetspeak."""
    # Проверяем, что все ключи в `charMapping` — в нижнем регистре.
    charMapping = {
        'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
        'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
        'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
        'v': ['\\/']}
    leetspeak = ''
    for char in message: # Проверяем каждый символ:
        # Меняем символ на leetspeak с вероятностью 70 %.
        if char.lower() in charMapping and random.random() <= 0.70:
            possibleLeetReplacements = charMapping[char.lower()]
            leetReplacement = random.choice(possibleLeetReplacements)
            leetspeak = leetspeak + leetReplacement
        else:
            # Не преобразуем этот символ:
            leetspeak = leetspeak + char
    return leetspeak


# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    main()
