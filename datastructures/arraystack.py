import os

from datastructures.array import Array, T
from datastructures.istack import IStack
from copy import deepcopy

class ArrayStack(IStack[T]):
    ''' ArrayStack class that implements the IStack interface. The ArrayStack is a 
        fixed-size stack that uses an Array to store the items.'''
    
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        ''' Constructor to initialize the stack 
        
            Arguments: 
                max_size: int -- The maximum size of the stack. 
                data_type: type -- The data type of the stack.       
        '''
        self.__dt = data_type
        self.__arr = Array(starting_sequence= [data_type() for i in range(max_size)])
        self.__top = -1
        self.__max_size = max_size - 1

    def push(self, item: T) -> None:
        if self.full:
            raise IndexError("Stack is full, cannot push")
        if not isinstance(item, self.__dt):
            raise TypeError("Pushed item type does not match stack data type")
        self.__top += 1
        self.__arr[self.__top] = item
        

    def pop(self) -> T:
        if self.empty:
            raise IndexError("Stack is empty, cannot pop")
        top_item = self.__arr[self.__top]
        self.__top -= 1
        return top_item

    def clear(self) -> None:
       self.__top = -1

    @property
    def peek(self) -> T:
       return self.__arr[self.__top]

    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the stack. 
        
            Returns:
                int: The maximum size of the stack.
        '''
        return self.__max_size + 1

    @property
    def full(self) -> bool:
        ''' Returns True if the stack is full, False otherwise. 
        
            Returns:
                bool: True if the stack is full, False otherwise.
        '''
        if self.__top == self.__max_size:
            return True
        return False

    @property
    def empty(self) -> bool:
        if self.__top == -1:
            return True
        return False

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ArrayStack):
            return False
        if len(other) != len(self):
            return False
        self_copy = deepcopy(self)
        other_copy = deepcopy(other)
        for i in range(len(self)):
            if self_copy.pop() != other_copy.pop():
                return False
        return True

    def __len__(self) -> int:
       return self.__top + 1
    
    def __contains__(self, item: T) -> bool:
        if not isinstance(item, self.__dt):
            return False
        for i in range(self.__top + 1):
            if item == self.__arr[i]:
                return True
        return False

    def __str__(self) -> str:
        return str([self.__arr[i] for i in range(self.__top + 1)])
    
    def __repr__(self) -> str:
        return f"ArrayStack({self.__max_size}): items: {str(self)}"
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')

