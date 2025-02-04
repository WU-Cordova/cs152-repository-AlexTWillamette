from datastructures.bag import Bag
from .card import Card, CardSuit, CardValue
from random import randint

class Multideck:
    """description or something"""

    def __init__(self):
        self.__numdecks__ = randint(1,4) * 2
        self.__bag__ = Bag()

        values = range(1, 11)
        for deck in range(self.__numdecks__):
            for suit in CardSuit:
                for value in CardValue:
                    self.__bag__.add(Card(value, suit))


                    

