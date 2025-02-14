# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray
import copy

from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("This should raise because starting_sequence is not a sequence")
        if not isinstance(data_type, type):
            raise ValueError("This should raise because data_type is not a type, it's a data value")
        for item in starting_sequence:
            if not isinstance(item, data_type):
                raise TypeError
        self.__data_type = data_type
        self.__element_count = len(starting_sequence)
        
        if self.__element_count == 0:
            self.__capacity = 0
        else:
            exp = 0
            while self.__element_count - 2**exp > 0:
                exp +=1 
            self.__capacity = 2**exp

        self.__elements = np.empty(self.__capacity, dtype=self.__data_type)
        for index in range(len(starting_sequence)):
            self.__elements[index] = copy.deepcopy(starting_sequence[index])

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, int):
            if not (-self.__element_count < index and index < self.__element_count):
                raise IndexError("Index out of bounds")
            item = self.__elements[index]
            return item.item() if isinstance(item, np.generic) else item
        elif isinstance(index, slice):
            start = index.start
            if index.stop == None:
                stop = self.__element_count
            else:
                stop = index.stop
            step = index.step

            if not (-self.__element_count < start and start < self.__element_count):
                raise IndexError("Index out of bounds")
            if not (-self.__element_count <= stop and stop <= self.__element_count):
                raise IndexError("Index out of bounds")

            sliced_items = self.__elements[start:stop:step]

            return Array(starting_sequence=sliced_items.tolist(), data_type=self.__data_type)
        else:
            raise TypeError
    
    def __setitem__(self, index: int, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError("Item is wrong type")
        elif not (-self.__element_count < index and index < self.__element_count):
            raise IndexError("Index out of bounds")
        else:
            self.__elements[index] = item

    def append(self, data: T) -> None:
        if not isinstance(data, self.__data_type):
            raise TypeError("Data type does not match array")
        self.__element_count += 1
        self.__grow(self.__element_count)
        self.__elements[self.__element_count] = data

    def append_front(self, data: T) -> None:
        if not isinstance(data, self.__data_type):
            raise TypeError("Data type does not match array")
        self.__element_count += 1
        self.__grow(self.__element_count)
        for index in range(self.__element_count - 1, 0, -1):   
            self.__elements[index] = self.__elements[index - 1]
        self.__elements[0] = data

    def pop(self) -> None:
        self.__delitem__(-1)
    
    def pop_front(self) -> None:
        self.__delitem__(0)

    def __len__(self) -> int: 
        return self.__element_count

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Array):
            return False
        if len(other) != len(self):
            return False
        for index in range(len(self)):
            if self[index] != other[index]:
                return False
        return True
    
    def __iter__(self) -> Iterator[T]:
        return iter(self.__elements[0: self.__element_count])

    def __reversed__(self) -> Iterator[T]:
        return iter(self[(self.__element_count-1):-1:-1])

    def __delitem__(self, index: int) -> None:
        if not (-self.__element_count < index and index < self.__element_count):
            raise IndexError("Index out of bounds")
        for i in range(index, self.__element_count - 1):
            self.__elements[i] = self.__elements[i + 1]
        self.__element_count -= 1
        self.__shrink(self.__element_count)

    def __contains__(self, item: Any) -> bool:
        return item == any(self)

    def clear(self) -> None:
        self.__elements = np.empty(0)
        self.__element_count = 0
        self.__capacity = 0

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__element_count}, Physical: {self.__capacity}, type: {self.__data_type}'
    
    def __grow(self, new_size: int) -> None:
        if self.__capacity >= new_size:
            pass
        else:
            self.__capacity *= 2  
            newarray = np.empty(self.__capacity)
            for i in range(self.__element_count):
                newarray[i] = self.__elements[i]
            self.__elements = newarray

    def __shrink(self, new_size: int) -> None:
        if new_size > (self.__capacity / 4):
            pass
        else:
            self.__capacity /= 2
            newarray = np.empty(self.__capacity)
            for i in range(self.__element_count):
                newarray[i] = self.__elements[i]
            self.__elements = newarray    


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')