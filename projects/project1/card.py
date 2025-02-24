from dataclasses import dataclass
from .cardvalue import CardValue
from .cardsuit import CardSuit

@dataclass
class Card:
    value: CardValue
    suit: CardSuit

    def __str__(self):
        return self.value.value + self.suit.value

    def __hash__(self): #cole debois told me about this. 
        return hash(str(self)) #needed for a dictionary (my underlying bag structure) to function.