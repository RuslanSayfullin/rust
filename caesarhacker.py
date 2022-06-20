"""Взлом шифра Цезаря,
Данная программа взламывает сообщения, зашифрованные шифром Цезаря,
путем прямого перебора всех возможных ключей.
"""

print('Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com')

# Просим пользователя ввести сообщение для взлома:
print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ')

# Все возможные символы для шифрования/дешифровки:
# (должно совпадать с набором SYMBOLS, использовавшимся при шифровании)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated = ''
    # Проходим в цикле по всем возможным ключам.
    # Расшифровываем каждый символ в сообщении:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol) # Получаем числовое значение символа.
            num = num - key # Расшифровываем числовое значение.
            # Выполняем переход по кругу, если число меньше 0:
            if num < 0:
                num = num + len(SYMBOLS)
            # Добавляем соответствующий числу расшифрованный символ
            # в translated:
            translated = translated + SYMBOLS[num]
        else:
            # Просто добавляем символ без расшифровки:
            translated = translated + symbol

    # Выводим проверяемый ключ вместе с расшифрованным на его основе текстом:
    print('Key #{}: {}'.format(key, translated))
