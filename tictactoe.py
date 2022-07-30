"""Крестики-нолики, (c) Sayfullin Ruslan aka CryptoLis.
Классическая настольная игра.
"""

ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '     # Константы для строковых значений.

def main():
    print('Welcome to Tic-Tac-Toe!')
    gameBoard = getBlankBoard() # Создаем ассоциативный массив для доски крестиков-ноликов.
    currentPlayer, nextPlayer = X, O # Сначала ходит X, а затем O.

    while True: # Основной цикл программы.
        # Отображаем доску на экране:
        print(getBoardStr(gameBoard))

        # Спрашиваем игрока, пока он не введет число от 1 до 9:
        move = None
        while not isValidSpace(gameBoard, move):
            print('What is {}\'s move? (1-9)'.format(currentPlayer))
            move = input('> ')
        updateBoard(gameBoard, move, currentPlayer) # Делаем ход.

        # Проверяем, не закончилась ли игра:
        if isWinner(gameBoard, currentPlayer): # Проверяем, кто победил.
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' has won the game!')
            break
        elif isBoardFull(gameBoard): # Проверяем на ничью.
            print(getBoardStr(gameBoard))
            print('The game is a tie!')

            break
        # Переход хода к следующему игроку:
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Thanks for playing!')


def getBlankBoard():
    """Создаем новую пустую доску для крестиков-ноликов."""
    # Карта номеров клеток: 1|2|3
    #                       -+-+-
    #                       4|5|6
    #                       -+-+-
    #                       7|8|9
    # Ключи — числа от 1 до 9, значения — X, O и BLANK:
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK # Все клетки начинаются в пустом состоянии.
    return board


def getBoardStr(board):
    """Возвращает текстовое представление доски."""
    return '''
    {}|{}|{} 1 2 3
    -+-+-
    {}|{}|{} 4 5 6
    -+-+-
    {}|{}|{} 7 8 9'''.format(board['1'], board['2'], board['3'],
                                board['4'], board['5'], board['6'],
                                board['7'], board['8'], board['9'])


def isValidSpace(board, space):
    """Возвращает True, если space на board представляет собой
    допустимый номер клетки, причем эта клетка пуста."""
    return space in ALL_SPACES and board[space] == BLANK

def isWinner(board, player):
    """Возвращает True, если игрок player победил на этой доске."""
    # Для удобочитаемости используются более короткие названия переменных:
    b, p = board, player
    # Проверяем наличие трех отметок на одной из трех строк,
    # двух диагоналей или в одном из трех столбцов.
    return ((b['1'] == b['2'] == b['3'] == p) or # Верхняя строка
        (b['4'] == b['5'] == b['6'] == p) or # Средняя строка
        (b['7'] == b['8'] == b['9'] == p) or # Нижняя строка
        (b['1'] == b['4'] == b['7'] == p) or # Левый столбец
        (b['2'] == b['5'] == b['8'] == p) or # Средний столбец
        (b['3'] == b['6'] == b['9'] == p) or # Нижний столбец
        (b['3'] == b['5'] == b['7'] == p) or # Диагональ
        (b['1'] == b['5'] == b['9'] == p))          # Диагональ


def isBoardFull(board):
    """Возвращает True, если все клетки на доске заполнены."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False # Если хоть одна клетка пуста — возвращаем False.
        return True # Незаполненных клеток нет, возвращаем True.

def updateBoard(board, space, mark):
    """Присваиваем клетке (space) на доске (board) значение (mark)."""
    board[space] = mark


if __name__ == '__main__':
    main() # Вызываем main(), если этот модуль не импортируется, а запускается.