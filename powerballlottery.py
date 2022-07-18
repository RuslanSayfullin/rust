"""Лотерея Powerball, (c) Sayfullin Ruslan.
Моделирование лотереи, позволяющее почувствовать все удовольствие от
проигрыша в лотерее, не тратя понапрасну денег.
"""

import random

print('''Powerball Lottery, by Sayfullin Ruslan
Each powerball lottery ticket costs $2. The jackpot for this game
is $1.586 billion! It doesn't matter what the jackpot is, though,
because the odds are 1 in 292,201,338, so you won't win.
This simulation gives you the thrill of playing without wasting money.
''')

# Запрашиваем у игрока первые пять номеров, от 1 до 69:
while True:
    print('Enter 5 different numbers from 1 to 69, with spaces between')
    print('each number. (For example: 5 17 23 42 50)')
    response = input('> ')

    # Убеждаемся, что игрок ввел пять номеров:
    numbers = response.split()
    if len(numbers) != 5:
        print('Please enter 5 numbers, separated by spaces.')
        continue

    # Преобразуем строковые значения в числа:
    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print('Please enter numbers, like 27, 35, or 62.')
        continue

    # Проверяем, что номера — в диапазоне от 1 до 69:
    for i in range(5):
        if not (1 <= numbers[i] <= 69):
            print('The numbers must all be between 1 and 69.')
            continue

    # Убеждаемся, что номера не повторяются:
    # (Создаем из номеров множество, чтобы убрать дубликаты.)
    if len(set(numbers)) != 5:
        print('You must enter 5 different numbers.')
        continue

    break


# Просим игрока выбрать Powerball, от 1 до 26:
while True:
    print('Enter the powerball number from 1 to 26.')
    response = input('> ')
    # Преобразуем строковые значения в числа:
    try:
        powerball = int(response)
    except ValueError:
        print('Please enter a number, like 3, 15, or 22.')
        continue
    # Проверяем, что номер – в диапазоне от 1 до 26:
    if not (1 <= powerball <= 26):
        print('The powerball number must be between 1 and 26.')
        continue

    break


# Введите количество розыгрышей лотереи:
while True:
    print('How many times do you want to play? (Max: 1000000)')
    response = input('> ')
    # Преобразуем строковые значения в числа:
    try:
        numPlays = int(response)
    except ValueError:
        print('Please enter a number, like 3, 15, or 22000.')
        continue

    # Убеждаемся, что число – в диапазоне от 1 до 1 000 000:
    if not (1 <= numPlays <= 1000000):
        print('You can play between 1 and 1000000 times.')
        continue

    break


# Запускаем имитационное моделирование:
price = '$' + str(2 * numPlays)
print('It costs', price, 'to play', numPlays, 'times, but don\'t')
print('worry. I\'m sure you\'ll win it all back.')
input('Press Enter to start...')


possibleNumbers = list(range(1, 70))
for i in range(numPlays):
    # Выбираем выигравшие номера:
    random.shuffle(possibleNumbers)
    winningNumbers = possibleNumbers[0:5]
    winningPowerball = random.randint(1, 26)

    # Отображаем выигравшие номера:
    print('The winning numbers are: ', end='')
    allWinningNums = ''
    for i in range(5):
        allWinningNums += str(winningNumbers[i]) + ' '
    allWinningNums += 'and ' + str(winningPowerball)
    print(allWinningNums.ljust(21), end='')
    # Множества не упорядочены, так что порядок целочисленных
    # значений в set(numbers) и set(winningNumbers) неважен.
    if (set(numbers) == set(winningNumbers)
        and powerball == winningPowerball):
            print()
            print('You have won the Powerball Lottery! Congratulations,')
            print('you would be a billionaire if this was real!')
            break
    else:
        print(' You lost.')     # Пробел в начале фразы тут необходим.


print('You have wasted', price)
print('Thanks for playing!')
