from collections import namedtuple
from random import shuffle

colors = ('WHITE', 'RED', 'GREEN', 'BLACK', 'BLUE')

Card = namedtuple('Card', ['bg','fg','txt'])

class Player:
    def __init__(self, index, hand):
        self.index = index
        self.hand = hand
        self.table = []

class Game:
    def __init__(self):
        self.deck = [Card(bg, fg, txt) for bg in colors \
                for fg in colors \
                for txt in colors \
                if fg != bg]
        shuffle(self.deck)
        
        self.players = []
        self.table = []
        
    def _deal(self, cardCount):
        cards = self.deck[:cardCount]
        self.deck = self.deck[cardCount:]
        return cards
        
    def start(self):
        self.table = self._deal(3)
        
    def newPlayer(self):
        player = Player(len(self.players), self._deal(3))
        self.players.append(player)
        return player