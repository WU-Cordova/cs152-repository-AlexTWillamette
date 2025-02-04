from enum import Enum
from dataclasses import dataclass

class CardSuit(Enum):
    HEART = "Heart"
    DIAMOND = "Diamond"
    CLUB = "Club"
    SPADE = "Spade"


@dataclass
class Card:
    face: str
    suit: CardSuit
    value: int