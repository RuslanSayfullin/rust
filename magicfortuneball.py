"""Магический хрустальный шар, (c) Sayfullin Ruslan.
Задавайте вопросы типа да/нет о своем будущем. Вдохновлено игрушкой Magic 8 Ball.
"""

import random
import time


def slowSpacePrint(text, interval=0.1):
    """Медленно выводит текст с пробелами между буквами и буквами i
    в нижнем регистре."""
    for character in text:
        if character == 'I':
            # Ради стильности I выводятся в нижнем регистре:
            print('i ', end='', flush=True)
        else:
            # Все прочие символы выводятся как обычно:
            print(character + ' ', end='', flush=True)
        time.sleep(interval)
    print()     # Выводим два символа новой строки.
    print()


# Запрашиваем у пользователя вопрос:
slowSpacePrint('MAGIC FORTUNE BALL, BY Sayfullin Ruslan.')
time.sleep(0.5)
slowSpacePrint('ASK ME YOUR YES/NO QUESTION.')
input('> ')

# Отображаем краткий ответ:
replies = [
    'LET ME THINK ON THIS...',
    'AN INTERESTING QUESTION...',
    'HMMM... ARE YOU SURE YOU WANT TO KNOW..?',
    'DO YOU THINK SOME THINGS ARE BEST LEFT UNKNOWN..?',
    'I MIGHT TELL YOU, BUT YOU MIGHT NOT LIKE THE ANSWER...',
    'YES... NO... MAYBE... I WILL THINK ON IT...',
    'AND WHAT WILL YOU DO WHEN YOU KNOW THE ANSWER? WE SHALL SEE...',
    'I SHALL CONSULT MY VISIONS...',
    'YOU MAY WANT TO SIT DOWN FOR THIS...',
    ]
slowSpacePrint(random.choice(replies))

# "Мхатовская" пауза:
slowSpacePrint('.' * random.randint(4, 12), 0.7)

# Выводим ответ:
slowSpacePrint('I HAVE AN ANSWER...', 0.2)
time.sleep(1)
answers = [
    'YES, FOR SURE',
    'MY ANSWER IS NO',
    'ASK ME LATER',
    'I AM PROGRAMMED TO SAY YES',
    'THE STARS SAY YES, BUT I SAY NO',
    'I DUNNO MAYBE',
    'FOCUS AND ASK ONCE MORE',
    'DOUBTFUL, VERY DOUBTFUL',
    'AFFIRMATIVE',
    'YES, THOUGH YOU MAY NOT LIKE IT',
    'NO, BUT YOU MAY WISH IT WAS SO',
]
slowSpacePrint(random.choice(answers), 0.05)
