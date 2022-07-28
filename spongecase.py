"""гУбКоРеГиСтР, (c) Sayfullin Ruslan.
Преобразует сообщения на английском языке в гУбКоТеКсТ.
"""

import random

try:
    import pyperclip # pyperclip копирует текст в буфер обмена.
except ImportError:
    pass # Если pyperclip не установлена, ничего не делаем. Не проблема.


def main():
    """Запускаем программу "ГубкоТЕКСТ"."""
    print('''sPoNgEcAsE, bY aL sWeIGaRt Al@iNvEnTwItHpYtHoN.cOm
    eNtEr YoUr MeSsAgE:''')
    spongetext = englishToSpongecase(input('> '))
    print()
    print(spongetext)

    try:
        pyperclip.copy(spongetext)
        print('(cOpIed SpOnGeTexT to ClIpbOaRd.)')
    except:
        pass # Если pyperclip не установлена, ничего не делаем.


def englishToSpongecase(message):
    """Возвращаем заданную строку в губкорегистре."""
    spongetext = ''
    useUpper = False

    for character in message:
        if not character.isalpha():
            spongetext += character
            continue
        if useUpper:
            spongetext += character.upper()
        else:
            spongetext += character.lower()

        # Меняем регистр в 90 % случаев.
        if random.randint(1, 100) <= 90:
            useUpper = not useUpper     # Меняем регистр.
    return spongetext


# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    main()
