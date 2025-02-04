from enum import Enum
from dataclasses import dataclass

class CardSuit(Enum):
    HEART = "Heart"
    DIAMOND = "Diamond"
    CLUB = "Club"
    SPADE = "Spade"

class CardValue(Enum):
    TWO = "2"
    THREE = "3"
    FOUR = "4" 
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"

@dataclass
class Card:
    value: CardValue
    suit: CardSuit

    def __str__(self):
        return self.suit.value + self.suit.value

    def __hash__(self): #cole debois the boy told me about this
        return hash(str(self))