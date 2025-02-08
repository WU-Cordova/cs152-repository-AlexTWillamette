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


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        if not isinstance(starting_sequence, Sequence): 
            raise ValueError('Sequence must be a valid sequence type.')
        
        if data_type and not all(isinstance(item, data_type) for item in starting_sequence):
            raise TypeError(f'All items in  {starting_sequence} must be of the same type: {data_type}')
        
        self.__item_count: int = len(starting_sequence)
        self.__data_type = data_type
        self.__items: NDArray[T] = np.empty(self.__item_count, dtype=self.__data_type)

        for i in range(self.__item_count):
            self.__items[i] = starting_sequence[i]

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
            if isinstance(index, slice):
                start = index.start if index.start is not None else 0
                stop = index.stop if index.stop is not None else self.__item_count
                step = index.step if index.step is not None else 1
                
                start = max(min(start, self.__item_count), -self.__item_count)
                stop = max(min(stop, self.__item_count), -self.__item_count)

                sliced_items = self.__items[start:stop:step]
                
                return Array(sliced_items.tolist())  

            if index < -self.__item_count or index >= self.__item_count:
                raise IndexError('Index must be in range of array.')
            
            item = self.__items[index]
            return item.item() if isinstance(item, np.generic) else item
    
    def __setitem__(self, index: int, item: T) -> None:
        if not isinstance(index, int): raise TypeError('Index must be an integer')
        if not isinstance(item, self.__data_type): raise TypeError(f'Type must be {(self.__data_type)}')

        if index >= self.__item_count or index < -self.__item_count:
            raise IndexError(f'{index} is out of bounds.')
            
        self.__items[index] = item

    def append(self, data: T) -> None:
        current_item_count = self.__item_count

        if self.__item_count == len(self.__items):
            size = len(self.__items) * 2 if len(self.__items) > 0 else 2
            self.__resize(size)

        self.__items[self.__item_count] = data
        self.__item_count = current_item_count + 1

    def append_front(self, data: T) -> None:
        if self.__item_count == len(self.__items):
            size = len(self.__items) * 2 if len(self.__items) > 0 else 1
            self.__resize(size)

        for i in range(self.__item_count - 1, 0, -1): 
            self[i] = self[i - 1]

        self[0] = data
        self.__item_count += 1

    def pop(self) -> None:
        if self.__item_count == 0: raise IndexError('Array is empty.')
        
        del self[self.__item_count - 1]
    
    def pop_front(self) -> None:
        if self.__item_count == 0: raise IndexError('Array is empty.')
        
        del self[0]

    def __len__(self) -> int: return self.__item_count

    def __resize(self, new_size: int) -> None:
        if new_size < 0: raise ValueError('New size must be a positive integer.')
        
        if new_size > len(self.__items):
            default_value = self.__data_type()
            new_items = np.array([default_value] * (new_size - len(self.__items)))
            self.__items = np.append(self.__items, new_items)
        else:
            self.__items = self.__items[:new_size]
            self.__item_count = new_size

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Array) and len(self) == len(other) and all(self[i] == other[i] for i in range(self.__item_count))

    def __iter__(self) -> Iterator[T]:
        for i in range(self.__item_count):
            item_at_i = self.__items[i]
            yield item_at_i.item() if isinstance(item_at_i, np.generic) else item_at_i

    def __reversed__(self) -> Iterator[T]:
        for i in range(self.__item_count - 1, -1, -1):
            item_at_i = self.__items[i]
            yield item_at_i.item() if isinstance(item_at_i, np.generic) else item_at_i

    def __delitem__(self, index: int) -> None:
        if index < 0 or index >= len(self.__items): raise IndexError('Must be in range of array.')

        for i in range(index, self.__item_count - 1):
            self.__items[i] = self.__items[i + 1]

        self.__item_count -= 1

        self._item_count_before_resize = self.__item_count
        if self.__item_count <= len(self.__items) // 4:
            self.__resize(len(self.__items) // 2)
            self.__item_count = self._item_count_before_resize

    def __contains__(self, item: Any) -> bool:
        return any(self[i] == item for i in range(self.__item_count))

    def clear(self) -> None:
        self.__items = np.array([], dtype=self.__data_type)
        self.__item_count = 0

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__item_count}, Physical: {len(self.__items)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')