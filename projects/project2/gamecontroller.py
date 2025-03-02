from .grid import Grid
from datastructures.array import Array
from datastructures.array2d import Array2D
import time
from .kbhit import KBHit
from copy import deepcopy

class GameController:
    """
    Manages the game of life logic.
    """
    def __init__(self) -> None:
        """
        Sets up some initial instance variables. 
        """
        self.__width  = 14  #setup width, config directly
        self.__height = 12  #setup height, config directly
        self.__kb = KBHit()
        
    def run(self) -> None:
        """
        Starts the game of life, handling both individual
        games and the overall application playing
        consecutive games if requested by user.
        """
        self.__big_running = True    #flags for whether the program as a whole is still running
        while self.__big_running == True:
            self.__generation = 0
            self.__history = Array(data_type=Grid)
            self.__stable = False
            self.__nonstable = False

            #setup before a game is being simulated

            self.__asking = True
            print("Press 'r' to start with a random start.")
            print("Press 'l' to start with the loaded config file.")
            while self.__asking == True:
                time.sleep(0.5)
                if self.__kb.kbhit():
                    c = (self.__kb.getch())
                    if c == "r": # creates a randomly generated game using preset config height and width
                        self.__current = Grid(start = "RANDOM", xwidth=self.__width, yheight=self.__height)
                        print("Random start generated")
                        self.__asking = False
                    elif c == "l": # uses a config file 
                        file = open("projects\project2\start.txt", "r")
                        rowcount = 0
                        for row in file:
                            if row[0] == "#":
                                pass
                            else:
                                if rowcount == 0:
                                    rowcount += 1
                                    rows = int(row)
                                elif rowcount == 1:
                                    rowcount += 1
                                    columns = int(row)
                                    start_seq = []
                                else:
                                    start_seq.append(row)
                        self.__current = Grid(start = start_seq, xwidth = columns, yheight = rows)
                        print("Start loaded from config file")
                        self.__asking = False

            #asks which mode to start the game in

            self.__mode = None
            print("Press 'm' for manual mode.")
            print("press 'a' for automatic mode.")
            self.__asking = True
            while self.__asking == True:
                time.sleep(0.5)
                if self.__kb.kbhit():
                    c = (self.__kb.getch())
                    if c == "m":
                        self.__mode = "m"
                        print("Manual mode selected")
                        self.__asking = False
                    elif c == "a":
                        self.__mode = "a"
                        print("Automatic mode selected")
                        self.__asking = False

            #starts running the game of life

            self.__running = True # flag for individual game of life
            self.__autointerval = 1 # handles speed of automatic mode
            print("Press 'm' to enter manual mode")
            print("Press 'a' to enter automatic mode")
            print("Press 's' to step to the next generation in manual mode")
            print("Press 'q' or 'e' to slow down or speed up simulation speed in automatic mode")
            print("Press 'l' to let go and quit running")

            print("".join(["-" for i in range(self.__current.get_width())]))
            print("Generation 0")
            print("".join(["-" for i in range(self.__current.get_width())]))
            self.__current.draw()
            print("".join(["-" for i in range(self.__current.get_width())]))

            while self.__running == True:
                if self.__mode == "m":
                    self.__asking = True
                    while self.__asking == True:
                        time.sleep(0.5)
                        if self.__kb.kbhit():
                            c = (self.__kb.getch())
                            if c == "s":
                                self.__asking = False
                                self.next_generation()
                            elif c == "a":
                                self.__asking = False
                                self.__mode = "a"
                            elif c == "l":
                                self.__asking = False
                                self.__running = False
                if self.__mode == "a":
                    self.__asking = True
                    while self.__asking == True:
                        time.sleep(0.1)
                        if self.__kb.kbhit():
                            c = (self.__kb.getch())
                            if c == "m":
                                self.__asking = False
                                self.__mode = "m"
                            elif c == "e":
                                if self.__autointerval > 0.25: #minimum allowed interval, maximum speed
                                    self.__autointerval -= 0.25
                            elif c == "q":
                                if self.__autointerval < 2:    #maximum allowed interval, minimum speed
                                    self.__autointerval += 0.25
                            elif c == "l":
                                self.__asking = False
                                self.__running = False
                        else:
                            time.sleep(self.__autointerval-0.1)
                            self.next_generation()

            #ends individual game of life and asks to continue or quit

            print("")
            if self.__stable == True:
                print("Game ended due to stability")
            elif self.__nonstable == True:
                print("Game ended due to non stability")
            else:
                print("Game ended due to manual exit.")
            print(f"Game ended after {self.__generation} generations.")

            print("")
            print("Press 's' to start a new game of life")
            print("press 'q' to end the application")
            self.__asking = True
            while self.__asking == True:
                time.sleep(0.5)
                if self.__kb.kbhit():
                    c = (self.__kb.getch())
                    if c == "s":
                        self.__asking = False
                    if c == "q":
                        self.__asking = False
                        self.__big_running = False


        
    def next_generation(self) -> None:
        """
        Helper function to step towards the next generation.
        Creates a new grid, populates it according to game rules and previous grid.
        Prints the new grid.
        Adds old grid to history, and makes the new grid the current grid.
        Checks afterwards if the there is stability or instability which should cause
        the current game to end.
        """
        next_grid = Grid(xwidth = self.__current.get_width(), yheight = self.__current.get_height())
        for i in range(self.__current.get_width()):
            for j in range(self.__current.get_height()):
                neighbors = self.__current.num_neighbors(xindex=i, yindex=j)
                this_cell = self.__current.get_cell_status(xindex=i, yindex=j)
                match [this_cell, neighbors]:
                    case [False, 3] | [True, 2] | [True, 3]:
                        next_grid.set_cell_status(xindex=i, yindex=j, status = True)
        self.__history.append(deepcopy(self.__current))
        self.__current = deepcopy(next_grid)
        if len(self.__history) > 5:     #only keeping track of last 5, can be adjusted
            self.__history.pop_front()  #keeps the history list at 5 long
        self.__generation += 1
        print("")
        print(f"Generation {self.__generation}:")
        print("".join(["-" for i in range(self.__current.get_width())]))
        self.__current.draw()
        print("".join(["-" for i in range(self.__current.get_width())]))

        if self.__current == self.__history[-1]:
            self.__stable = True
            self.__running = False
            self.__asking = False
        else:
            for i in range(len(self.__history)-1):
                if self.__current == self.__history[i]:
                    self.__nonstable = True
                    self.__running = False
                    self.__asking = False

        

