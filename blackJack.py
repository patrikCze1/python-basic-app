import random
import sys

class Game():
    cards = []
    playerCards = []
    croupierCards = []
    playerMoney = 100
    bet = 0

    win = 0
    draw = 0
    loose = 0

    def __init__(self):
        pass

    def startGame(self):
        self.cards = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        ]
        self.playerCards = []
        self.croupierCards = []
        self.bet = 0

        print(f'Your money: {self.playerMoney}')
        self.bet = int(input('Bet: '))
        self.playerMoney -= self.bet

        self.playerCards.append(self.drawCard())
        self.croupierCards.append(self.drawCard())
        self.playerCards.append(self.drawCard())

        print(f'Your cards: {self.playerCards}')
        self.playerRound()

    def drawCard(self):
        cardsCount = len(self.cards)
        randomNumber = random.randint(0, cardsCount - 1)

        card = self.cards[randomNumber]
        self.cards.pop(randomNumber)
        return card

    def countCards(self, list):
        sum = 0
        for l in list:
            sum += l

        return sum

    def result(self):
        if self.countCards(self.playerCards) > self.countCards(self.croupierCards):
            self.win += 1
            self.playerMoney += 2 * self.bet
            print('You win')
        elif self.countCards(self.playerCards) == self.countCards(self.croupierCards):
            self.draw += 1
            self.playerMoney += self.bet
            print('Draw')
        else:
            self.loose += 1
            print('Croupier win')
        self.endGame()

    def playerRound(self):
        while 1:
            playerMove = input('[H]it / [S]tand: ')

            if 'h' == playerMove.lower():
                self.playerCards.append(self.drawCard())
                print(f'Your cards: {self.playerCards}')
                if self.countCards(self.playerCards) > 21:
                    print('You loose')
                    self.loose += 1
                    self.endGame()
            else:
                break
        self.croupierRound()

    def croupierRound(self):
        while 1:
            if self.countCards(self.croupierCards) < 17:
                self.croupierCards.append(self.drawCard())
                print('Croupier take card')
                print(f'Croupier cards: {self.croupierCards}')
            elif self.countCards(self.croupierCards) > 21:
                print('Croupier loose')
                self.win += 1
                self.playerMoney = self.playerMoney + 2 * self.bet
                self.endGame()
            elif self.countCards(self.croupierCards) >= 17:
                print('Croupier stand')
                break
        self.result()

    def endGame(self):
        print(f'Wins: {self.win}')
        print(f'Draws: {self.draw}')
        print(f'Looses: {self.loose}')
        print(f'Your money: {self.playerMoney}')

        ans = input('New game? y/n ')
        if ans.lower() == 'y':
            self.startGame()
        else:
            sys.exit()

blackJack = Game()
blackJack.startGame()

