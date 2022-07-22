"""Шифр ROT13, (c) Sayfullin Ruslan.
Простейший шифр сдвига для шифрования и дешифровки текста.
"""

try:
    import pyperclip    # pyperclip копирует текст в буфер обмена.
except ImportError:
    pass                 # Если pyperclip не установлена, ничего не делаем. Не проблема.


# Задаем константы:
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

print('ROT13 Cipher, by Sayfullin Ruslan.')
print()

while True:  # Основной цикл программы.
    print('Enter a message to encrypt/decrypt (or QUIT):')
    message = input('> ')

    if message.upper() == 'QUIT':
        break   # Выходим из основного цикла программы.

    # Сдвигаем буквы в сообщении на 13 позиций.
    translated = ''
    for character in message:
        if character.isupper():
            # Выполняем конкатенацию символа в верхнем регистре.
            transCharIndex = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[transCharIndex]
        elif character.islower():
            # Выполняем конкатенацию символа в нижнем регистре.
            transCharIndex = (LOWER_LETTERS.find(character) + 13) % 26
            translated += LOWER_LETTERS[transCharIndex]
        else:
            # Выполняем конкатенацию символа в исходном виде.
            translated += character

    # Отображаем преобразованное сообщение:
    print('The translated message is:')
    print(translated)
    print()

    try:
        # Копируем преобразованное сообщение в буфер обмена:
        pyperclip.copy(translated)
        print('(Copied to clipboard.)')
    except:
        pass
