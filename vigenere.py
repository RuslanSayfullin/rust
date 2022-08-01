"""Шифр Виженера, (c) Sayfullin Ruslan aka CryptoLis.
Шифр Виженера — многоалфавитный шифр подстановки, настолько
эффективный, что его не могли взломать многие столетия.
Подробнее — в статье https://ru.wikipedia.org/wiki/Шифр_Виженера
"""

try:
    import pyperclip # pyperclip копирует текст в буфер обмена.
except ImportError:
    pass    # Если pyperclip не установлена, ничего не делаем. Не проблема.

# Все возможные символы для шифрования/дешифровки:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print('''Vigenère Cipher, by Sayfullin Ruslan
    The Vigenère cipher is a polyalphabetic substitution cipher that was
    powerful enough to remain unbroken for centuries.''')

    # Спрашиваем у пользователя, хочет он шифровать или расшифровывать:
    while True:     # Повторяем вопрос, пока пользователь не введет e или d.
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()
        if response.startswith('e'):
            myMode = 'encrypt'
            break
        elif response.startswith('d'):
            myMode = 'decrypt'
            break
        print('Please enter the letter e or d.')

    # Просим пользователя ввести ключ шифрования:
    while True:     # Повторяем вопрос, пока пользователь не введет допустимый ключ
        print('Please specify the key to use.')
        print('It can be a word or any combination of letters:')
        response = input('> ').upper()
        if response.isalpha():
            myKey = response
            break

    # Просим пользователя ввести сообщение для шифрования/расшифровки:
    print('Enter the message to {}.'.format(myMode))
    myMessage = input('> ')

    # Производим шифрование/расшифровку:
    if myMode == 'encrypt':
        translated = encryptMessage(myMessage, myKey)
    elif myMode == 'decrypt':
        translated = decryptMessage(myMessage, myKey)

    print('%sed message:' % (myMode.title()))
    print(translated)

    try:
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard.' % (myMode))
    except:
        pass # Если pyperclip не установлена, ничего не делаем.


def encryptMessage(message, key):
    """Шифрует сообщение message в соответствии с ключом key."""
    return translateMessage(message, key, 'encrypt')


def decryptMessage(message, key):
    """Расшифровывает сообщение message в соответствии с ключом key."""
    return translateMessage(message, key, 'decrypt')


def translateMessage(message, key, mode):
    """Зашифровывает или расшифровывает сообщение в соответствии с ключом."""
    translated = []         # Для хранения строкового значения зашифрованного/расшифрованного сообщения.
    keyIndex = 0
    key = key.upper()

    for symbol in message:  # Проходим в цикле по всем символам сообщения.
        num = LETTERS.find(symbol.upper())
        if num != -1:       # -1 означает, что symbol.upper() не входит в LETTERS.
            if mode == 'encrypt':
                # Прибавляем при шифровании:
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                # Вычитаем при расшифровке:
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS)     # Учитываем возможный переход по кругу.

            # Добавляем зашифрованный/расшифрованный символ в translated.
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1   # Переходим к следующей букве ключа.
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # Просто добавляем символ без шифрования/расшифровки:
            translated.append(symbol)

    return ''.join(translated)


# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    main()
