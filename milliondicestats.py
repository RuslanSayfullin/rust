"""Моделирование статистики за миллион бросков костей, (c) Sayfullin Ruslan.
Моделирование миллиона бросков игральных костей.
"""

import random, time

print('''Million Dice Roll Statistics Simulator
By Sayfullin Ruslan.
Enter how many six-sided dice you want to roll:''')

numberOfDice = int(input('> '))
# Подготовка ассоциативного массива для хранения результатов бросков костей:
results = {}
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    results[i] = 0


# Моделирование бросков костей:
print('Simulating 1,000,000 rolls of {} dice...'.format(numberOfDice))
lastPrintTime = time.time()
for i in range(1000000):
    if time.time() > lastPrintTime + 1:
        print('{}% done...'.format(round(i / 10000, 1)))
        lastPrintTime = time.time()

    total = 0
    for j in range(numberOfDice):
        total = total + random.randint(1, 6)
    results[total] = results[total] + 1

# Выводим результаты:
print('TOTAL - ROLLS - PERCENTAGE')
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1)
    print(' {} - {} rolls - {}%'.format(i, roll, percentage))
