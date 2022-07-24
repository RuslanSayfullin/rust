"""Царская игра Ура, (c) Sayfullin Ruslan.
Игра 5000-летней давности из Месопотамии. Два игрока бьют фишки
друг друга, стремясь достичь финиша.
"""

import random, sys


X_PLAYER = 'X'
O_PLAYER = 'O'
EMPTY = ' '


# Задаем константы для меток клеток доски:
X_HOME = 'x_home'
O_HOME = 'o_home'
X_GOAL = 'x_goal'
O_GOAL = 'o_goal'


# Клетки доски слева направо, сверху вниз:
ALL_SPACES = 'hgfetsijklmnopdcbarq'
X_TRACK = 'HefghijklmnopstG' # (H означает Дом, G означает Финиш.)
O_TRACK = 'HabcdijklmnopqrG'

FLOWER_SPACES = ('h', 't', 'l', 'd', 'r')

BOARD_TEMPLATE = """
                   {}            {}
                   Home              Goal
                     v                 ^
+-----+-----+-----+--v--+           +--^--+-----+
|*****|     |     |     |           |*****|     |
|* {} *<   {}  < {}   < {}  |       |* {} *< {} |
|****h|    g|    f|    e|           |****t|    s|
+--v--+-----+-----+-----+-----+-----+-----+--^--+
|     |     |     |*****|     |     |     |     |
|   {} >  {}    > {} >* {} *> {} > {} > {} > {} |
|    i|    j|    k|****l|    m|    n|    o|    p|
+--^--+-----+-----+-----+-----+-----+-----+--v--+
|*****|     |     |     |           |*****|     |
|* {} *<  {} <  {} <     {} |       |* {} *< {} |
|****d|    c|    b|    a|           |****r|    q|
+-----+-----+-----+--^--+           +--v--+-----+
                     ^                 v
                   Home              Goal
                   {}             {}
"""


def main():
    print('''The Royal Game of Ur, by Sayfullin Ruslan
          This is a 5,000 year old game. Two players must move their tokens
    from their home to their goal. On your turn you flip four coins and can
    move one token a number of spaces equal to the heads you got.
    Ur is a racing game; the first player to move all seven of their tokens
    to their goal wins. To do this, tokens must travel from their home to
    their goal:
    
    
    X Home
    X Goal
                  v           ^
    +---+---+---+-v-+       +-^-+---+
    |v<<<<<<<<<<<<< |       | ^<|<< |
    |v  |   |   |   |       |   | ^ |
    +v--+---+---+---+---+---+---+-^-+
    |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>^ |
    |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>v |
    +^--+---+---+---+---+---+---+-v-+
    |^  |   |   |   |       |   | v |
    |^<<<<<<<<<<<<< |       | v<<<< |
    +---+---+---+-^-+       +-v-+---+
                  ^           v
                O Home      O Goal
                
                
    If you land on an opponent's token in the middle track, it gets sent
    back home. The **flower** spaces let you take another turn. Tokens in
    the middle flower space are safe and cannot be landed on.''')
    input('Press Enter to begin...')

    gameBoard = getNewBoard()
    turn = O_PLAYER
    while True: # Основной цикл игры.
        # Переменные для этого хода:
        if turn == X_PLAYER:
            opponent = O_PLAYER
            home = X_HOME
            track = X_TRACK
            goal = X_GOAL
            opponentHome = O_HOME
        elif turn == O_PLAYER:
            opponent = X_PLAYER
            home = O_HOME
            track = O_TRACK
            goal = O_GOAL
            opponentHome = X_HOME

        displayBoard(gameBoard)

        input('It is ' + turn + '\'s turn. Press Enter to flip...')

        flipTally = 0
        print('Flips: ', end='')
        for i in range(4):  # Подбрасываем четыре монеты.
            result = random.randint(0, 1)
            if result == 0:
                print('T', end='')  # Решка.
            else:
                print('H', end='')   # Орел.
            if i != 3:
                print('-', end='')   # Разделитель.
            flipTally += result
        print(' ', end='')

        if flipTally == 0:
            input('You lose a turn. Press Enter to continue...')
            turn = opponent # Переход хода к другому игроку.
            continue

        # Просим игрока сделать ход:
        validMoves = getValidMoves(gameBoard, turn, flipTally)

        if validMoves == []:
            print('There are no possible moves, so you lose a turn.')
            input('Press Enter to continue...')
            turn = opponent # Переход хода к другому игроку.
            continue

        while True:
            print('Select move', flipTally, 'spaces: ', end='')
            print(' '.join(validMoves) + ' quit')
            move = input('> ').lower()

            if move == 'quit':
                print('Thanks for playing!')
                sys.exit()
            if move in validMoves:
                break # Выход из цикла после выбора допустимого хода.

            print('That is not a valid move.')

        # Производим выбранный ход на доске:
        if move == 'home':
            # Если ход делается из дома, вычитаем соответствующее
            # количество фишек:
            gameBoard[home] -= 1
            nextTrackSpaceIndex = flipTally
        else:
            gameBoard[move] = EMPTY  # Очищаем клетку, из которой делался ход.
            nextTrackSpaceIndex = track.index(move) + flipTally

        movingOntoGoal = nextTrackSpaceIndex == len(track) - 1
        if movingOntoGoal:
            gameBoard[goal] += 1
            # Проверяем, не выиграл ли игрок:
            if gameBoard[goal] == 7:
                displayBoard(gameBoard)
                print(turn, 'has won the game!')
                print('Thanks for playing!')
                sys.exit()
        else:
            nextBoardSpace = track[nextTrackSpaceIndex]
            # Проверяем наличие в клетке фишки оппонента:
            if gameBoard[nextBoardSpace] == opponent:
                gameBoard[opponentHome] += 1

            # Заносим фишку игрока в клетку, в которую произведен ход:
            gameBoard[nextBoardSpace] = turn

        # Проверяем, попал ли игрок на розетку, а значит, может ходить снова:
        if nextBoardSpace in FLOWER_SPACES:
            print(turn, 'landed on a flower space and goes again.')
            input('Press Enter to continue...')
        else:
            turn = opponent  # Переход хода к другому игроку.


def getNewBoard():
    """
    Возвращает ассоциативный массив, отражающий состояние доски.
    Ключами служат строковые значения меток клеток, значения —
    X_PLAYER, O_PLAYER или EMPTY. Также содержит счетчики количества
    фишек в доме и на финише для обоих игроков.
    """
    board = {X_HOME: 7, X_GOAL: 0, O_HOME: 7, O_GOAL: 0}
    # В начале игры все клетки пусты:
    for spaceLabel in ALL_SPACES:
        board[spaceLabel] = EMPTY
    return board


def displayBoard(board):
    """Отображает игральную доску на экране."""
    # Очищает экран путем вывода множества символов новой строки,
    # делая старую доску невидимой для пользователя.
    print('\n' * 60)

    xHomeTokens = ('X' * board[X_HOME]).ljust(7, '.')
    xGoalTokens = ('X' * board[X_GOAL]).ljust(7, '.')
    oHomeTokens = ('O' * board[O_HOME]).ljust(7, '.')
    oGoalTokens = ('O' * board[O_GOAL]).ljust(7, '.')

    # Добавляем строковые значения для заполнения BOARD_TEMPLATE
    # по порядку слева направо, сверху вниз.
    spaces = []
    spaces.append(xHomeTokens)
    spaces.append(xGoalTokens)
    for spaceLabel in ALL_SPACES:
        spaces.append(board[spaceLabel])
    spaces.append(oHomeTokens)
    spaces.append(oGoalTokens)

    print(BOARD_TEMPLATE.format(*spaces))


def getValidMoves(board, player, flipTally):
    validMoves = [] # Клетки с фишками, способными двигаться.
    if player == X_PLAYER:
        opponent = O_PLAYER
        track = X_TRACK
        home = X_HOME
    elif player == O_PLAYER:
        opponent = X_PLAYER
        track = O_TRACK
        home = O_HOME

    # Проверяем, может ли игрок пойти фишкой из дома:
    if board[home] > 0 and board[track[flipTally]] == EMPTY:
        validMoves.append('home')

    # Проверяем, в каких клетках есть фишки, которыми игрок может пойти:
    for trackSpaceIndex, space in enumerate(track):
        if space == 'H' or space == 'G' or board[space] != player:
            continue
        nextTrackSpaceIndex = trackSpaceIndex + flipTally
        if nextTrackSpaceIndex >= len(track):
            # Необходимо сделать ход так, чтобы не перескочить
            # финишную клетку, иначе ходить нельзя.
            continue
        else:
            nextBoardSpaceKey = track[nextTrackSpaceIndex]
            if nextBoardSpaceKey == 'G':
                # Эта фишка может уйти с доски:
                validMoves.append(space)
                continue
        if board[nextBoardSpaceKey] in (EMPTY, opponent):
            # Сделать ход в защищенную среднюю клетку можно,
            # только если она пуста:
            if nextBoardSpaceKey == 'l' and board['l'] == opponent:
                continue # Пропускаем ход, клетка защищена.
            validMoves.append(space)

    return validMoves


if __name__ == '__main__':
    main()
