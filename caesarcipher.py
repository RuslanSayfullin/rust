"""Шифр Цезаря
Шифр Цезаря — шифр сдвига, в котором шифрование и дешифровка букв
производятся путем сложения и вычитания соответствующих чисел.
"""

try:
    import pyperclip # pyperclip копирует текст в буфер обмена.
except ImportError:
    pass # Если библиотека pyperclip не установлена, ничего не делаем.

# Все возможные символы для шифрования/дешифровки:
# (!) Можете добавить также символы для цифр и знаков препинания,
# чтобы шифровать и их.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher, by Al Sweigart al@inventwithpython.com')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

# Спрашиваем у пользователя, хочет ли он шифровать или расшифровывать:
while True: # Повторяем вопрос, пока пользователь не введет e или d.
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

# Просим пользователя ввести ключ шифрования:
while True: # Повторяем вопрос, пока пользователь не введет допустимый ключ.
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# Просим пользователя ввести сообщение для шифрования/расшифровки:
print('Enter the message to {}.'.format(mode))
message = input('> ')
# Шифр Цезаря работает только с символами в верхнем регистре:
message = message.upper()

# Для хранения зашифрованного/расшифрованного варианта сообщения:
translated = ''

# Зашифровываем/расшифровываем каждый символ сообщения:
for symbol in message:
    if symbol in SYMBOLS:
        # Получаем зашифрованное (расшифрованное) числовое значение для символа.
        num = SYMBOLS.find(symbol) # Получаем числовое значение символа
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        # Производим переход по кругу, если число больше длины SYMBOLS
        # или меньше 0:
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
        # Добавляем соответствующий числу зашифрованный/расшифрованный символ
        # в translated:
        translated = translated + SYMBOLS[num]
    else:
        # Просто добавляем символ без шифрования/расшифровки:
        translated = translated + symbol

# Выводим зашифрованную/расшифрованную строку на экран:
print(translated)


try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass    # Если pyperclip не установлена, ничего не делаем.
