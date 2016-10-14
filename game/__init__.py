from collections import namedtuple
from random import shuffle

colors = ('WHITE', 'RED', 'GREEN', 'BLACK', 'BLUE')

Card = namedtuple('Card', ['bg','fg','txt'])

class Player:
    def __init__(self, index, hand):
        self.index = index
        self.hand = hand
        self.table = []

class BaseGame:
    def __init__(self):
        self.deck = [Card(bg, fg, txt) for bg in colors \
                for fg in colors \
                for txt in colors \
                if fg != bg]
        shuffle(self.deck)

class Game(BaseGame):
    DRAW = 0
    PLAY = 1
    
    def __init__(self):
        BaseGame.__init__(self)
        self.players = []
        self.table = self._deal(3)
        self.currentPlayer = 0
        self.state = Game.DRAW
        
    def _deal(self, cardCount):
        if cardCount > len(self.deck):
            cardCount = len(self.deck)
        cards = self.deck[:cardCount]
        self.deck = self.deck[cardCount:]
        return cards
        
    def newPlayer(self):
        player = Player(len(self.players), self._deal(3))
        self.players.append(player)
        return player
    
    def draw(self, playerIndex, tableIndex):
        assert playerIndex == self.currentPlayer
        assert self.state == Game.DRAW
        assert tableIndex >= -1 and tableIndex < len(self.table)
        if tableIndex == -1:
            self.players[playerIndex].hand.append(self._deal(1))
        else:
            self.players[playerIndex].hand.append(self.table[tableIndex])
            self.table = self.table[:tableIndex] + self._deal(1) + self.table[(tableIndex+1):]
        self.state = Game.PLAY
        
        
        