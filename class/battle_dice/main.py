from game import Game
from character import Character
from charactertype import CharacterType

if __name__ == '__main__':
    # Create characters
    alice = Character(name="Alice", character_type=CharacterType.WARRIOR, health=100, attack_power=10)
    bob = Character(name="Bob", character_type=CharacterType.MAGE, health=70, attack_power=15)

    # Start game
    game = Game(alice, bob)
    game.start_battle()
