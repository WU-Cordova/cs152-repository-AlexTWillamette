import random
from character import Character

class Game:
    """Manages the Dice Battle game logic"""

    def __init__(self, player1: Character, player2: Character):
        """Initializes the game with two players."""
        self.__player1 = player1
        self.__player2 = player2

    def attack(self, attacker: Character, defender: Character):
        """Performs an attack where the attacker rolls a die to determine damage dealth."""
        # More sophisticated implementation using character type and attack power to be added
        diceroll = random.randint(1, 6)
        damage = diceroll * attacker.attack_power//6
        defender.health -= damage
        print(f"{attacker.name} rolled a {diceroll} and did {damage} damage to {defender.name}." )


    def start_battle(self):
        """Starts a turn based battle between two players."""
        turn = 1
        while self.__player1.health > 0 and self.__player2.health > 0: 
            if (turn % 2) == 0:
                self.attack(attacker = self.__player1, defender = self.__player2)
            else:
                self.attack(attacker = self.__player2, defender = self.__player1)
            turn += 1
        if self.__player1.health <= 0: 
            print(f"{self.__player2.name} won!")
        else:
            print(f"{self.__player1.name} won!")