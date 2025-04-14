import os
from datastructures.istack import IStack
from typing import Generic

from datastructures.linkedlist import LinkedList, T
from copy import deepcopy

class ListStack(Generic[T], IStack[T]):
    """
    ListStack (LinkedList-based Stack)

    """

    def __init__(self, data_type:object) -> None:
        """
        Initializes the ListStack.

        Args:
            data_type (type): The type of data the stack will hold.

        """
        self.ll = LinkedList(data_type=data_type)
        self.data_type = data_type

    def push(self, item: T):
        """
        Pushes an item onto the stack.

        Args:
            item (T): The item to push onto the stack.
        
        Raises:
            TypeError: If the item is not of the correct type.

        """
        self.ll.append(item)

    def pop(self) -> T:
        """
        Removes and returns the top item from the stack.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        return self.ll.pop()

    def peek(self) -> T:
        """
        Returns the top item from the stack without removing it.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        return self.ll.back

    @property
    def empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.ll.empty

    def clear(self):
        """
        Clears all items from the stack.
        """
        self.ll.clear()

    def __contains__(self, item: T) -> bool:
        """
        Checks if an item exists in the stack.

        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item exists in the stack, False otherwise.

        """
        return item in self.ll

    def __eq__(self, other) -> bool:
        """
        Compares two stacks for equality.

        Args:
            other (ListStack): The stack to compare with.

        Returns:
            bool: True if the stacks are equal, False otherwise.

        """
        if not isinstance(other, ListStack):
            return False
        if len(other) != len(self):
            return False
        
        copyself = deepcopy(self)
        copyother = deepcopy(other)
        selfarr = []
        otherarr = []
        for i in range(len(self)):
            selfarr.append(copyself.pop())
            otherarr.append(copyother.pop())
        if selfarr == otherarr:
            return True
        return False

    def __len__(self) -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return(len(self.ll))

    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
        selfcopy = deepcopy(self)
        selfarr = []
        for i in range(len(self)):
            selfarr.append(selfcopy.pop())
        return " ".join(selfarr)

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the stack.

        Returns:
            str: A detailed string representation of the stack.

        """
        return f"ListStack: [{str(self)}], Count: {len(self)}"
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
