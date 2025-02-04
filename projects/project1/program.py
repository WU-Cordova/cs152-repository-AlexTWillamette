from .game import Game
from .multideck import Multideck

def main():
    
    game = Game()
    game.play()
    test = Multideck()
    print(len((test.__bag__)))


if __name__ == '__main__':
    main()