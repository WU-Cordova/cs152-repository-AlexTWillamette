from datastructures.bag import Bag
from .card import Card, CardSuit, CardValue
from random import randint, shuffle

class Multideck:
    """Class to manage multideck storage logic"""

    def __init__(self) -> None:
        """
        Creates the multideck. Randomly picks a number of decks to shuffle together.
        Puts them in a bag, then takes them out of the bag into a list so it can be shuffled
        for the purpose of randomly selecting a card to draw.
        """ 
        
        numdecks = randint(1,4) * 2
        
        self.__bag = Bag()
        for deck in range(numdecks):
            for suit in CardSuit:
                for value in CardValue:
                    self.__bag.add(Card(value, suit))
        
        self.__order = []
        for card in self.__bag.distinct_items():
            for i in range(self.__bag.count(card)):
                self.__order.append(card)

        shuffle(self.__order)

    def draw(self) -> Card:
        """
        Returns the last card of the list, which is like the top of the deck.
        Removes that card from the deck/list afterwards.
        """

        if len(self.__order) != 0:
            card = self.__order[-1]
            self.__order.pop()
            return card
        else:
            return ValueError #deck should never be empty, but hey, I accounted for it




                    

