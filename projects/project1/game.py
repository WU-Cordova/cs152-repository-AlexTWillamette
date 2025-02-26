from .multideck import Multideck

class Game():
    """Manages the blackjack game logic"""
    
    def __init__(self) -> None:
        pass # No execution needed upon initalization of a game object

    def play(self) -> None:
        """Starts the game of blackjack. Runs with helper functions."""
        print("Welcome to Blackjack!")
        print("")
        self.__playing = True   
        while self.__playing == True:
            self.initialize_round()
            self.playround()
        print("Game over! Thanks for playing!")

    def initialize_round(self) -> None:
        """
        Creates the initial multideck and hands to start a round of blackjack.
        Makes initial prints for the state of the start of each round.
        """
        self.__gamedeck = Multideck()
        self.__dealerhand = []
        self.__playerhand = []
        self.draw(self.__dealerhand)
        self.draw(self.__dealerhand)
        self.draw(self.__playerhand)
        self.draw(self.__playerhand)
        print("Initial Deal:")
        print(f"Player's Hand: {self.printhand(self.__playerhand)}", end="")
        print(f"| Score: {self.handvalue(self.__playerhand)}")
        print(f"Dealer's Hand: [{self.__dealerhand[0]}] ", end="")
        print(f"[Hidden] | Score: {self.handvalue(self.__dealerhand[0])}")
        print("")

    def playround(self) -> None:
        """
        Handles the playing of a game of blackjack after the initial draw.
        """
        has_stayed = False
        if self.handvalue(self.__playerhand) == 21: #stops hitting if the player starts with blackjack
            has_stayed = True
        while has_stayed == False:
            print(f"Player's Hand: {self.printhand(self.__playerhand)}", end="")
            print(f"| Score: {self.handvalue(self.__playerhand)}")
            call = input("Would you like to (H)it or (S)tay? ").upper()
            print("")
            if call == "H":
                self.draw(self.__playerhand)
                if self.handvalue(self.__playerhand) > 21: #stops hitting if the player busts
                    has_stayed = True
                    print(f"Player's Hand: {self.printhand(self.__playerhand)}", end="")
                    print(f"| Score: {self.handvalue(self.__playerhand)}")
                    print("Bust! You went over 21!")
                    print("")
                elif self.handvalue(self.__playerhand) == 21: #stops hitting if the player gets blackjack
                    has_stayed = True
                    print(f"Player's Hand: {self.printhand(self.__playerhand)}", end="")
                    print(f"| Score: {self.handvalue(self.__playerhand)}")
                    print("Player has Blackjack!")
                    print("")
            elif call == "S":
                has_stayed = True
            else:
                print("Input not recognized.")
        if self.handvalue(self.__playerhand) > 21: # player immediately loses if they bust
            print(f"Dealer's Hand: {self.printhand(self.__dealerhand)}", end="")
            print(f"| Score: {self.handvalue(self.__dealerhand)}")
            print("Dealer wins! Player busted.")
        else:
            while self.handvalue(self.__dealerhand) < 17: # dealer draws to at least 17
                self.draw(self.__dealerhand)
            print(f"Dealer's Hand: {self.printhand(self.__dealerhand)} ", end="")
            print(f"| Score: {self.handvalue(self.__dealerhand)}")
            if self.handvalue(self.__dealerhand) > 21:
                print("Player wins! Dealer busted.")
            elif self.handvalue(self.__playerhand) == 21 and self.handvalue(self.__dealerhand) == 21:
                print("Push! No winner.")
            elif self.handvalue(self.__playerhand) > self.handvalue(self.__dealerhand):
                print("Player wins!")
            else:
                print("Dealer wins!")
        play_again = ""
        while play_again not in ["Y", "N"]:
            print("")
            play_again = input("Would you like to play again? (Y)es or (N)o: ").upper()
            if play_again == "Y":
                print("")
            elif play_again == "N":
                self.__playing = False
            else:
                print("Input not recognized.")

    def printhand(self, hand) -> str:
        """
        Takes a hand list and returns the printable string of the hand.
        Hands are usually lists of objects, which can't be printed as expected
        when printed as usual.
        """
        cardstr = ""
        for card in hand:
            cardstr += f"[{card}] "
        return cardstr
    
    def handvalue(self, hand) -> int:
        """
        Takes a hand and returns the integer value of the hand
        as calculated by the rules of blackjack.
        Faces are 10s, 2-9 are their number, and aces are 1 or 11.
        """ 
        handval = 0
        num_ace = 0
        if type(hand) is not list:
            hand = [hand]
        for card in hand:
            if card.value.value in ["J", "K", "Q"]:
                handval += 10
            elif card.value.value == "A":
                handval += 1
                num_ace += 1
            else:
                handval += int(card.value.value)
        for ace in range(num_ace):
            if handval + 10 <= 21:
                handval += 10
        return handval

    def draw(self, hand) -> None:
        """Function to make a hand draw a card from the game's multideck."""
        hand.append(self.__gamedeck.draw())