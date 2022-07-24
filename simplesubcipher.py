"""Простой шифр подстановки, (c) Sayfullin Ruslan.
Простой шифр подстановки с взаимнооднозначным преобразованием всех
символов открытого и зашифрованного текста.
"""

import random

try:
    import pyperclip # pyperclip копирует текст в буфер обмена.
except ImportError:
    pass # Если pyperclip не установлена, ничего не делаем. Не проблема.


# Все возможные символы для шифрования/дешифровки:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print('''Simple Substitution Cipher, by Sayfullin Ruslan
    A simple substitution cipher has a one-to-one translation for each
    symbol in the plaintext and each symbol in the ciphertext.''')
    # Спрашиваем у пользователя, хочет ли он шифровать или расшифровывать:
    while True: # Повторяем вопрос, пока пользователь не введет e или d.
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
    while True: # Повторяем вопрос, пока пользователь не введет допустимый ключ.
        print('Please specify the key to use.')
        if myMode == 'encrypt':
            print('Or enter RANDOM to have one generated for you.')
        response = input('> ').upper()
        if response == 'RANDOM':
            myKey = generateRandomKey()
            print('The key is {}. KEEP THIS SECRET!'.format(myKey))
            break
        else:
            if checkKey(response):
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

    # Отображаем результат:
    print('The %sed message is:' % (myMode))
    print(translated)
    try:
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard.' % (myMode))
    except:
        pass # Если pyperclip не установлена, ничего не делаем.


def checkKey(key):
    """Возвращает True, если ключ допустимый. В противном случае
    возвращает False."""
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        print('There is an error in the key or symbol set.')
        return False
    return True


def encryptMessage(message, key):
    """Шифрует сообщение в соответствии с ключом key."""
    return translateMessage(message, key, 'encrypt')


def decryptMessage(message, key):
    """Расшифровывает сообщение в соответствии с ключом key."""
    return translateMessage(message, key, 'decrypt')


def translateMessage(message, key, mode):
    """Зашифровывает или расшифровывает сообщение в соответствии
    с ключом key."""
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # Для расшифровки можно использовать тот же код, что и для
        # шифрования. Нужно просто поменять местами key и LETTERS.
        charsA, charsB = charsB, charsA

    # Проходим в цикле по всем символам сообщения:
    for symbol in message:
        if symbol.upper() in charsA:
            # Зашифровываем/расшифровываем символ:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # Если символ не входит в LETTERS, добавляем его без изменения.
            translated += symbol

    return translated


def generateRandomKey():
    """Генерирует и возвращает случайный ключ шифрования."""
    key = list(LETTERS)     # Преобразуем строковое значение LETTERS в список.
    random.shuffle(key)     # Перетасовываем этот список случайным образом.
    return ''.join(key)     # Преобразуем список в строковое значение.


# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    main()
