"""Блек-джек,
Классическая карточная игра, известная также как "двадцать одно".
(В этой версии нет страхования или разбиения.)
"""

import random, sys



# Задаем значения констант:
HEARTS = chr(9829)   # Символ 9829 — '♥'.
DIAMONDS = chr(9830) # Символ 9830 — '♦'.
SPADES = chr(9824)   # Символ 9824 — '♠'.
CLUBS = chr(9827)    # Символ 9827 — '♣'.
# (Список кодов chr можно найти в https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'


def main():
    print('''Blackjack
        Rules:
            Try to get as close to 21 without going over.
            Kings, Queens, and Jacks are worth 10 points.
            Aces are worth 1 or 11 points.
            Cards 2 through 10 are worth their face value.
            (H)it to take another card.
            (S)tand to stop taking cards.
            On your first play, you can (D)ouble down to increase your bet
            but must hit exactly one more time before standing.
            In case of a tie, the bet is returned to the player.
            The dealer stops hitting at 17.'''
          )

    money = 5000
    while True: # Основной цикл игры.
        # Проверяем, не закончились ли у игрока деньги:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

        # Даем возможность игроку сделать ставку на раунд:
        print('Money:', money)
        bet = getBet(money)

        # Сдаем дилеру и игроку по две карты из колоды:
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Обработка действий игрока:
        print('Bet:', bet)
        while True: # Выполняем цикл до тех пор, пока игрок не скажет "хватит" или у него не будет перебор.
            displayHands(playerHand, dealerHand, False)
            print()

            # Проверка на перебор у игрока:
            if getHandValue(playerHand) > 21:
                break

            # Получаем ход игрока: H, S или D:
            move = getMove(playerHand, money - bet)

            # Обработка действий игрока:
            if move == 'D':
                # Игрок удваивает, он может увеличить ставку:
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                # "Еще" или "удваиваю": игрок берет еще одну карту.
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)
                if getHandValue(playerHand) > 21:
                    # Перебор у игрока:
                    continue

            if move in ('S', 'D'):
                # "Хватит" или "удваиваю": переход хода к следующему игроку
                break


        # Обработка действий дилера:
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # Дилер берет еще карту:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
                if getHandValue(dealerHand) > 21:
                    break # Перебор у дилера.
                input('Press Enter to continue...')
                print('\n\n')

        # Отображает итоговые карты на руках:
        displayHands(playerHand, dealerHand, True)
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # Проверяем, игрок выиграл, проиграл или сыграл вничью:
        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you.')

        input('Press Enter to continue...')
        print('\n\n')



def getBet(maxBet):
    """Спрашиваем у игрока, сколько он ставит на этот раунд."""
    while True: # Продолжаем спрашивать, пока не будет введено допустимое значение.
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue # Если игрок не ответил — спрашиваем снова.

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet # Игрок ввел допустимое значение ставки.



def getDeck():
    """Возвращаем список кортежей (номинал, масть) для всех 52 карт."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) # Добавляем числовые карты.
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) # Добавляем фигурные карты и тузы.
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    """Отображаем карты игрока и дилера. Скрываем первую карту дилера, если showDealerHand равно False."""
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # Скрываем первую карту дилера:
        displayCards([BACKSIDE] + dealerHand[1:])


    # Отображаем карты игрока:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    """ Возвращаем стоимость карт. Фигурные карты стоят 10, тузы — 11
    или 1 очко (эта функция выбирает подходящую стоимость карты)."""
    value = 0
    numberOfAces = 0

    # Добавляем стоимость карты — не туза:
    for card in cards:
        rank = card[0] # карта представляет собой кортеж (номинал, масть)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'): # Фигурные карты стоят 10 очков.
            value += 10
        else:
            value += int(rank) # Стоимость числовых карт равна их номиналу.

    # Добавляем стоимость для тузов:
    value += numberOfAces # Добавляем 1 для каждого туза.
    for i in range(numberOfAces):
        # Если можно добавить еще 10 с перебором, добавляем:
        if value + 10 <= 21:
            value += 10
    return value


def displayCards(cards):
    """Отображаем все карты из списка карт."""
    rows = ['', '', '', '', ''] # Отображаемый в каждой строке текст.
    for i, card in enumerate(cards):
        rows[0] += ' ___ ' # Выводим верхнюю строку карты.
        if card == BACKSIDE:
        # Выводим рубашку карты:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Выводим лицевую сторону карты:
            rank, suit = card # Карта — структура данных типа кортеж.
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
    # Выводим все строки на экран:
    for row in rows:
        print(row)


def getMove(playerHand, money):
    """Спрашиваем, какой ход хочет сделать игрок, и возвращаем 'H', если он
    хочет взять еще карту, 'S', если ему хватит, и 'D', если он удваивает."""
    while True: # Продолжаем итерации цикла, пока игрок не сделает допустимый ход.
        # Определяем, какие ходы может сделать игрок:
        moves = ['(H)it', '(S)tand']
        # Игрок может удвоить при первом ходе, это ясно из того,
        # что у игрока ровно две карты:
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        # Получаем ход игрока:
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move # Игрок сделал допустимый ход.
        if move == 'D' and '(D)ouble down' in moves:
            return move # Игрок сделал допустимый ход.

# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    main()

