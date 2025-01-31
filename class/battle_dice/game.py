import random
from character import Character

class Game:
    """Manages the Dice Battle game logic"""

    def __init__(self, player1: Character, player2: Character):
        """Initializes the game with two players."""
        self.__player1 == player1
        self.__player2 == player2

    def attack(self, attacker: Character, defender: Character):
        """Performs an attack where the attacker rolls a die to determine damage dealth."""
        # More sophisticated implementation using character type and attack power to be added
        diceroll = random.randit(1, 6)
        self.__player2.health -= diceroll
        # add print statements describing the diceroll,damage dealt, remaining health


    def start_battle(self):
        """Starts a turn based battle between two players."""
        turn = 1
        while self.__player1.health > 0 and self.__player2.health > 0: #todo, add comments
            if (turn % 2) == 0:
                attack(attacker = self.__player1, defender = self.__player2)
            else:
                attack(attacker = self.__player2, defender = self.__player1)
            turn += 1
        if self.__player1.health <= 0: #to add, win statements
            #print(self.)
            pass