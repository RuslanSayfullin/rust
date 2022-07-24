"""Ковер из "Сияния", (c) Sayfullin Ruslan.
Выводит на экран мозаичный узор ковра из фильма "Сияние"
"""

# Задаем константы:
X_REPEAT = 6    # Количество ячеек по горизонтали.
Y_REPEAT = 4     # Количество ячеек по вертикали.

for i in range(Y_REPEAT):
    print(r'_ \ \ \_/ __' * X_REPEAT)
    print(r' \ \ \___/ _' * X_REPEAT)
    print(r'\ \ \_____/ ' * X_REPEAT)
    print(r'/ / / ___ \_' * X_REPEAT)
    print(r'_/ / / _ \__' * X_REPEAT)
    print(r'__/ / / \___' * X_REPEAT)
