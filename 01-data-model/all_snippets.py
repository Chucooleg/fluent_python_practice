"""
By implementing __len__ and __getitem__, our class FrenchDeck behaves like a python sequence. We can use
- len()
- FrenchDeck[5]
- list slicing
- iterate with for loops
- apply sorted() and reverse()

Problem: FrenchDeck cannot be shuffled because it is an immutable. Unless we access directly self._cards
Solution: use __setitem__ method
"""

#---------------------
# build the classes with special methods
import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


#---------------------
# basic usage
beer_card = Card('7', 'diamonds')
beer_card
# Card('rank'=7, 'suit'='diamonds')

deck = FrenchDeck()
len(deck)

deck[0]
# Card('rank'=2, 'suit'='spades')

deck[-1]
# Card('rank'='A', 'suit'='hearts')

#--------------------
# support random selection
from random import choice
choice(deck)
# Card('rank'='3', 'suit'='hearts')
choice(deck)
# Card('rank'='2', 'suit'='clubs')

#---------------------
# list slicing
deck[:3]
deck{12::13]  # get all the "A"s

#---------------------
# iterating through deck because __getitem__ is amazing
for card in deck:
    print (card)

for card in reversed(deck):
    print (card)

#---------------------
# sequential scan
Card('Q', 'hearts') in deck
# True

#---------------------
# rank sequence elements

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print (card)
#--------------------------------------------------------------------
"""
By implementing __repr__, __abs__, __add__, __mul__, our class can emulate numeric types like vectors

- v1 + v2
- abs(v)
- abs(v*3)


Notes:
    __repr__ should return the "source code" that is used to construct the object such as "Vector(3, 4)
    __str__ is called by str() method, if no __str__ is available, python calls __repr__ as a backup
    __bool__ calls bool(). And is useful to determine T/F object state when "if" or "while" are called.
    See https://docs.python.org/3/reference/datamodel.html

"""

from math import hypot

class Vector:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r,%r)'%(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    
    def __mul__(self, other):
        return Vector(self.x*scalar, self.y*scalar)


