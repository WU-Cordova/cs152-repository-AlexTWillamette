from .cell import Cell
from datastructures.array2d import Array2D
from random import choice

class Grid:
    """
    Class to handle grid logic. x indexes left to right, y index top to bottom.
    """
    def __init__(self, start=None, xwidth:int=None, yheight:int=None):
        """
        Creates the grid. Either uses a starting sequence or initial dimensions with all dead cells.
        If the starting sequence is "RANDOM", the grid will be initialized with each cell
        randomly either alive or dead. Otherwise, takes in an Array2D as read by the
        gamecontroller to make a grid according to a config file.
        """
        if start == None or start == "RANDOM":
            if xwidth == None or yheight == None:
                raise ValueError("Provide a starting sequence or size for the base grid")
            else:
                self.__grid = Array2D.empty(rows=yheight, cols=xwidth, data_type=Cell)
        else:
            self.__grid = Array2D.empty(rows=yheight, cols=xwidth, data_type=Cell)
        self.__width = xwidth
        self.__height = yheight
        if start == "RANDOM":
            for row in range(self.__height):
                for col in range(self.__width):
                    self.set_cell_status(xindex=col,yindex=row, status=choice([True, False]))
        elif start != None:
            for row in range(self.__height):
                for col in range(self.__width):
                    if start[row][col] == "X":
                        self.set_cell_status(xindex=col,yindex=row, status=True)


    def num_neighbors(self, xindex:int, yindex:int) -> int:
        """
        Returns the number of neighbors (alive cells) around a cell at a given index.
        """
        neighbors = 0
        for row in range(yindex-1, yindex+2, 1):
            for col in range(xindex-1, xindex+2):
                if row < 0 or row >= self.__height:
                    pass
                elif col < 0 or col >= self.__width:
                    pass
                elif row == yindex and col == xindex:
                    pass
                else:
                    if self.__grid[row][col].get_status() == True:
                        neighbors += 1
        return neighbors

    def get_width(self) -> int:
        """
        Getter function for grid width.
        """
        return self.__width

    def get_height(self) -> int:
        """
        Getter function for grid height.
        """
        return self.__height

    def get_cell_status(self, xindex, yindex) -> bool:
        """
        Getter function for the status of a cell within the grid.
        """
        if xindex < 0 or xindex >= self.__width:
            raise IndexError("Index out of bounds for finding a cell")
        elif yindex < 0 or yindex >= self.__height:
            raise IndexError("Index out of bounds for finding a cell")
        else:
            return self.__grid[yindex][xindex].get_status()

    def set_cell_status(self, xindex:int, yindex:int, status:bool) -> None:
        """
        Setter function for the status of a cell with a grid.
        """
        if xindex < 0 or xindex >= self.__width:
            raise IndexError("Index out of bounds for finding a cell")
        elif yindex < 0 or yindex >= self.__height:
            raise IndexError("Index out of bounds for finding a cell")
        else:
            return self.__grid[yindex][xindex].set_status(status)

    def __eq__(self, other) -> bool:
        """
        Dunder method override for equals. Equality determined
        by location of alive cells.
        """
        if self.__width == other.get_width():
            if self.__height == other.get_height():
                for i in range(self.__width):
                    for j in range(self.__height):
                        if self.get_cell_status(xindex = i, yindex = j) != other.get_cell_status(xindex = i, yindex = j):
                            return False
                return True
            else:
                return False
        else:
            return False

    def draw(self) -> None:
        """
        Prints the grid to the terminal with X's as live cells, and _'s as empty cells.
        """
        for row in range(self.__height):
            rowstr = ""
            for col in range(self.__width):
                cellstatus = self.get_cell_status(xindex=col, yindex=row)
                if cellstatus == True:
                    rowstr += "X"
                else:
                    rowstr += "_"
            print(rowstr)