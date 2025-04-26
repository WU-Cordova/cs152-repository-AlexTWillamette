class Cell:
    """
    Class to handle cell logic.
    """
    def __init__(self, alive:bool = False) -> None:
        """
        Initializes the cell and its one instance variable to keep track of.
        """
        self.__alive_status = alive

    def get_status(self) -> bool:
        """
        Getter method for the cell's life status.
        """
        return self.__alive_status
    
    def set_status(self, status:bool) -> None:
        """
        Setter method for the cell's life status.
        """
        self.__alive_status = status
