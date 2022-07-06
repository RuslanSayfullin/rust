"""Голодные роботы, (c) Sayfullin Ruslan.
Сбегите от голодных роботов, сталкивая их друг с другом.
"""

import random, sys

# Задаем константы:
WIDTH = 40          # (!) Попробуйте заменить это значение на 70 или 10.
HEIGHT = 20         # (!) Попробуйте заменить это значение на 10.
NUM_ROBOTS = 10     # (!) Попробуйте заменить это значение на 1 или 30.
NUM_TELEPORTS = 2   # (!) Попробуйте заменить это значение на 0 или 9999.
NUM_DEAD_ROBOTS = 2 # (!) Попробуйте заменить это значение на 0 или 20.
NUM_WALLS = 100     # (!) Попробуйте заменить это значение на 0 или 1000.


EMPTY_SPACE = ' '   # (!) Попробуйте заменить заменить это значение на '.'.
PLAYER = '@'        # (!) Попробуйте заменить заменить это значение на 'R'.
ROBOT = 'R'         # (!) Попробуйте заменить заменить это значение на '@'.
DEAD_ROBOT = 'X'    # (!) Попробуйте заменить заменить это значение на 'R'.


# (!) Попробуйте заменить это значение на '#', или 'O', или ' ':
WALL = chr(9617) # Символ 9617 соответствует '░'


def main():
    print('''Hungry Robots, by Sayfullin Ruslan
    You are trapped in a maze with hungry robots! You don't know why robots
    need to eat, but you don't want to find out. The robots are badly
    programmed and will move directly toward you, even if blocked by walls.
    You must trick the robots into crashing into each other (or dead robots)
    without being caught. You have a personal teleporter device, but it only
    has enough battery for {} trips. Keep in mind, you and robots can slip
    through the corners of two diagonal walls!
    '''.format(NUM_TELEPORTS))

    input('Press Enter to begin...')

    # Подготавливаем новую игру:
    board = getNewBoard()
    robots = addRobots(board)
    playerPosition = getRandomEmptySpace(board, robots)
    while True: # Основной цикл игры.
        displayBoard(board, robots, playerPosition)

        if len(robots) == 0: # Проверяем, не выиграл ли игрок.
            print('All the robots have crashed into each other and you')
            print('lived to tell the tale! Good job!')
            sys.exit()

    # Передвигаем игрока и роботов:
    playerPosition = askForPlayerMove(board, robots, playerPosition)
    robots = moveRobots(board, robots, playerPosition)

    for x, y in robots:     # Проверяем, не проиграл ли игрок.
        if (x, y) == playerPosition:
            displayBoard(board, robots, playerPosition)
            print('You have been caught by a robot!')
            sys.exit()


def getNewBoard():
    """Возвращает соответствующий доске ассоциативный массив. Роль ключей
    играют кортежи (x, y) целочисленных индексов позиций на доске,
    а значений — WALL, EMPTY_SPACE и DEAD_ROBOT. В ассоциативном массиве есть
    также ключ 'teleports' для числа оставшихся у игрока попыток телепортации.
    Живые роботы хранятся отдельно от ассоциативного массива board"""
    board = {'teleports': NUM_TELEPORTS}

    # Создаем пустую доску:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[(x, y)] = EMPTY_SPACE

    # Добавляем стенки на краях доски:
    for x in range(WIDTH):
        board[(x, 0)] = WALL # Верхняя стенка.
        board[(x, HEIGHT - 1)] = WALL # Нижняя стенка.
    for y in range(HEIGHT):
        board[(0, y)] = WALL # Левая стенка.
        board[(WIDTH - 1, y)] = WALL # Правая стенка.

    # Добавляем еще стенки случайным образом:
    for i in range(NUM_WALLS):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = WALL

    # Добавляем изначально мертвых роботов:
    for i in range(NUM_DEAD_ROBOTS):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = DEAD_ROBOT
    return board


def getRandomEmptySpace(board, robots):
    """Возвращает целочисленный кортеж (x, y) для пустого пространства
    на доске."""
    while True:
        randomX = random.randint(1, WIDTH - 2)
        randomY = random.randint(1, HEIGHT - 2)
        if isEmpty(randomX, randomY, board, robots):
            break
    return (randomX, randomY)


def isEmpty(x, y, board, robots):
    """Возвращает True, если клетка (x, y) на доске пуста
    и не содержит робота."""
    return board[(x, y)] == EMPTY_SPACE and (x, y) not in robots

def addRobots(board):
    """Добавляет NUM_ROBOTS роботов в пустые места на доске, а также возвращает
    список (x, y) этих пустых мест, в которых теперь находятся роботы."""
    robots = []
    for i in range(NUM_ROBOTS):
        x, y = getRandomEmptySpace(board, robots)
        robots.append((x, y))
    return robots

def displayBoard(board, robots, playerPosition):
    """Отображает доску, роботов и игрока на экране."""
    # Проходим в цикле по всем позициям на доске:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # Рисуем соответствующий символ:
            if board[(x, y)] == WALL:
                print(WALL, end='')
            elif board[(x, y)] == DEAD_ROBOT:
                print(DEAD_ROBOT, end='')
            elif (x, y) == playerPosition:
                print(PLAYER, end='')
            elif (x, y) in robots:
                print(ROBOT, end='')
            else:
                print(EMPTY_SPACE, end='')
        print() # Выводим символ новой строки.

def askForPlayerMove(board, robots, playerPosition):
    """Возвращает целочисленный кортеж (x, y) места, куда далее идет
    игрок, с учетом текущего местоположения и краев доски."""
    playerX, playerY = playerPosition

    # Ищем, движение в каких направлениях не преграждает стенка:
    q = 'Q' if isEmpty(playerX - 1, playerY - 1, board, robots) else ' '
    w = 'W' if isEmpty(playerX + 0, playerY - 1, board, robots) else ' '
    e = 'E' if isEmpty(playerX + 1, playerY - 1, board, robots) else ' '
    d = 'D' if isEmpty(playerX + 1, playerY + 0, board, robots) else ' '
    c = 'C' if isEmpty(playerX + 1, playerY + 1, board, robots) else ' '
    x = 'X' if isEmpty(playerX + 0, playerY + 1, board, robots) else ' '
    z = 'Z' if isEmpty(playerX - 1, playerY + 1, board, robots) else ' '
    a = 'A' if isEmpty(playerX - 1, playerY + 0, board, robots) else ' '
    allMoves = (q + w + e + d + c + x + a + z + 'S')

    while True:
        # Определяем ход игрока:
        print('(T)eleports remaining: {}'.format(board["teleports"]))
        print('                     ({}) ({}) ({})'.format(q, w, e))
        print('                     ({}) (S) ({})'.format(a, d))
        print('Enter move or QUIT:  ({}) ({}) ({})'.format(z, x, c))

        move = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif move == 'T' and board['teleports'] > 0:
            # Телепортируем игрока на случайную новую позицию:
            board['teleports'] -= 1
            return getRandomEmptySpace(board, robots)
        elif move != '' and move in allMoves:
            # Возвращаем новую позицию игрока в соответствии со сделанным ходом:
            return {'Q': (playerX - 1, playerY - 1),
                    'W': (playerX + 0, playerY - 1),
                    'E': (playerX + 1, playerY - 1),
                    'D': (playerX + 1, playerY + 0),
                    'C': (playerX + 1, playerY + 1),
                    'X': (playerX + 0, playerY + 1),
                    'Z': (playerX - 1, playerY + 1),
                    'A': (playerX - 1, playerY + 0),
                    'S': (playerX, playerY)}[move]

def moveRobots(board, robotPositions, playerPosition):
    """Возвращаем список кортежей (x, y) новых позиций роботов,
    после их попыток переместиться в направлении игрока."""
    playerx, playery = playerPosition
    nextRobotPositions = []

    while len(robotPositions) > 0:
        robotx, roboty = robotPositions[0]

        # Определяем направление движения робота.
        if robotx < playerx:
            movex = 1 # Перемещаем вправо.
        elif robotx > playerx:
            movex = -1 # Перемещаем влево.
        elif robotx == playerx:
            movex = 0 # Не перемещаем по горизонтали.

        if roboty < playery:
            movey = 1 # Перемещаем вверх.
        elif roboty > playery:
            movey = -1 # Перемещаем вниз.
        elif roboty == playery:
            movey = 0 # Не перемещаем по вертикали.
        # Проверяем, не натыкается ли робот на стену, и корректируем
        # направление его движения:
        if board[(robotx + movex, roboty + movey)] == WALL:
            # Робот натолкнется на стену, так что выбираем другой ход:
            if board[(robotx + movex, roboty)] == EMPTY_SPACE:
                movey = 0 # Робот не может переместиться горизонтально.
            elif board[(robotx, roboty + movey)] == EMPTY_SPACE:
                movex = 0 # Робот не может переместиться вертикально.
            else:
                # Робот не может переместиться.
                movex = 0
                movey = 0
        newRobotx = robotx + movex
        newRoboty = roboty + movey

        if (board[(robotx, roboty)] == DEAD_ROBOT
            or board[(newRobotx, newRoboty)] == DEAD_ROBOT):
            # Робот попал на место столкновения, удаляем его.
            del robotPositions[0]
            continue
        # Проверяем, не наткнулся ли он на другого робота, и уничтожаем обоих
        # в этом случае:
        if (newRobotx, newRoboty) in nextRobotPositions:
            board[(newRobotx, newRoboty)] = DEAD_ROBOT
            nextRobotPositions.remove((newRobotx, newRoboty))
        else:
            nextRobotPositions.append((newRobotx, newRoboty))

        # Удаляем роботов из robotPositions по мере их перемещения.
        del robotPositions[0]
    return nextRobotPositions


# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    main()
