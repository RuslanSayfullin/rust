"""Японский абак — соробан, (c) Sayfullin Ruslan.
Моделирование японского счетного инструмента типа абака.
"""

NUMBER_OF_DIGITS = 10

def main():
    print('Soroban - The Japanese Abacus')
    print('By Sayfullin Ruslan')
    print()

    abacusNumber = 0    # Число, отображаемое на абаке.
    while True:     # Основной цикл программы.
        displayAbacus(abacusNumber)
        displayControls()

        commands = input('> ')
        if commands == 'quit':
            # Выходим из программы:
            break
        elif commands.isdecimal():
            # Задаем число на абаке:
            abacusNumber = int(commands)
        else:
            # Обрабатываем команды увеличения/уменьшения:
            for letter in commands:
                if letter == 'q':
                    abacusNumber += 1000000000
                elif letter == 'a':
                    abacusNumber -= 1000000000
                elif letter == 'w':
                    abacusNumber += 100000000
                elif letter == 's':
                    abacusNumber -= 100000000
                elif letter == 'e':
                    abacusNumber += 10000000
                elif letter == 'd':
                    abacusNumber -= 10000000
                elif letter == 'r':
                    abacusNumber += 1000000
                elif letter == 'f':
                    abacusNumber -= 1000000
                elif letter == 't':
                    abacusNumber += 100000
                elif letter == 'g':
                    abacusNumber -= 100000
                elif letter == 'y':
                    abacusNumber += 10000
                elif letter == 'h':
                    abacusNumber -= 10000
                elif letter == 'u':
                    abacusNumber += 1000
                elif letter == 'j':
                    abacusNumber -= 1000
                elif letter == 'i':
                    abacusNumber += 100
                elif letter == 'k':
                    abacusNumber -= 100
                elif letter == 'o':
                    abacusNumber += 10
                elif letter == 'l':
                    abacusNumber -= 10
                elif letter == 'p':
                    abacusNumber += 1
                elif letter == ';':
                    abacusNumber -= 1

        # Абак не может отображать отрицательные числа:
        if abacusNumber < 0:
            abacusNumber = 0 # Заменяем все отрицательные числа на 0.

        # Абак не может отображать числа, превышающие 9 999 999 999:
        if abacusNumber > 9999999999:
            abacusNumber = 9999999999


def displayAbacus(number):
    numberList = list(str(number).zfill(NUMBER_OF_DIGITS))

    hasBead = [] # Содержит для каждой позиции костяшек True или False.

    # Костяшка в верхнем ряду "неба" соответствует цифрам 0, 1, 2, 3 или 4.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '01234')

    # Костяшка в верхнем ряду "неба" соответствует цифрам 5, 6, 7, 8 или 9.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '56789')

    # Костяшка в первом (верхнем) ряду "земли" выражает все цифры, кроме 0.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '12346789')

    # Костяшка в втором ряду "земли" выражает цифры 2, 3, 4, 7, 8 или 9.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '234789')

    # Костяшка в третьем ряду "земли" выражает цифры 0, 3, 4, 5, 8 или 9.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '034589')

    # Костяшка в четвертом ряду "земли" выражает цифры 0, 1, 2, 4, 5, 6 или 9.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '014569')

    # Костяшка в пятом ряду "земли" выражает цифры 0, 1, 2, 5, 6 или 7.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '012567')

    # Костяшка в шестом ряду "земли" выражает цифры 0, 1, 2, 3, 5, 6, 7 или 8.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '01235678')

    # Преобразуем эти значения True/False в символы O или |.
    abacusChar = []
    for i, beadPresent in enumerate(hasBead):
        if beadPresent:
            abacusChar.append('O')
        else:
            abacusChar.append('|')

    # Рисуем абак с символами O/|.
    chars = abacusChar + numberList
    print("""
+================================+
I {} {} {} {} {} {} {} {} {} {} I
I | | | | | | | | | | I
I {} {} {} {} {} {} {} {} {} {} I
+================================+
I {} {} {} {} {} {} {} {} {} {} I
I {} {} {} {} {} {} {} {} {} {} I
I {} {} {} {} {} {} {} {} {} {} I
I {} {} {} {} {} {} {} {} {} {} I
I {} {} {} {} {} {} {} {} {} {} I
I {} {} {} {} {} {} {} {} {} {} I
+=={}=={}=={}=={}=={}=={}=={}=={}=={}=={}==+""".format(*chars))


def displayControls():
    print(' +q w e r t y u i o p')
    print(' -a s d f g h j k l ;')
    print('(Enter a number, "quit", or a stream of up/down letters.)')


if __name__ == '__main__':
    main()
