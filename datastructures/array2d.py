from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type = object) -> None:
            self.__datatype = data_type
            self.__num_columns = num_columns
            self.__row_index = row_index
            self.__elements = array
            self.__offset = self.__num_columns * self.__row_index

        def __getitem__(self, column_index: int) -> T:
            if isinstance(column_index, int):
                if column_index > 0 and column_index >= self.__num_columns:
                    raise IndexError("Index out of bounds")
                elif column_index < 0 and column_index <= self.__num_columns:
                    raise IndexError("Index out of bounds")
                else:
                    return self.__elements[self.__offset + column_index]
            elif isinstance(column_index, slice):
                start = column_index.start
                stop = column_index.stop
                step = column_index.step
                if not (-num_columns < start and start < num_columns):
                    raise IndexError("Index out of bounds")
                elif not (-num_columns <= stop and stop <= num_columns):
                    raise IndexError("Index out of bounds")
                else:
                    return self.__elements[self.__offset + start:self.__offset + stop:step]
            else:
                type(column_index)
                raise TypeError
        
        def __setitem__(self, column_index: int, value: T) -> None:
                if column_index > 0 and column_index >= self.__num_columns:
                    raise IndexError("Index out of bounds")
                elif column_index < 0 and column_index <= self.__num_columns:
                    raise IndexError("Index out of bounds")
                else:
                    self.__elements[self.__num_columns * self.__row_index + column_index] = value
        
        def __iter__(self) -> Iterator[T]:
            return iter(self.__elements[self.__offset: self.__offset + self.__num_columns])
        
        def __reversed__(self) -> Iterator[T]:
            return self.__elements[self.__offset: self.__offset + self.__num_columns].reversed()

        def __len__(self) -> int:
            return self.__num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.__num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.__row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.__num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:

        if not isinstance(starting_sequence, Sequence):
            raise ValueError("must be a sequence of sequences")
        for row in starting_sequence:
            if not isinstance(row, Sequence):
                raise ValueError("must be a sequence of sequences")
        if isinstance(starting_sequence, str): #silly exception because a one letter string is a sequence apparently
            raise ValueError("must be a sequence of sequences")
        self.__data_type = data_type
        if self.__data_type == object:
            self.__data_type = starting_sequence[0][0]
        for row in starting_sequence:
            for item in row:
                if not isinstance(item, self.__data_type):
                    raise ValueError("All items must be of the same type")
        self.__num_columns = len(starting_sequence[0])
        for row in starting_sequence:
            if len(row) != self.__num_columns:
                raise ValueError("must be a sequence of sequences with the same length")
        self.__num_rows = len(starting_sequence)
        initial_sequence = ["" for i in range(self.__num_columns*self.__num_rows)]
        rowcount = 0
        for row in starting_sequence:
            itemcount = 0
            for item in row:
                initial_sequence[rowcount * self.__num_columns + itemcount] = item
                itemcount += 1
            rowcount += 1
        self.__elements = Array(starting_sequence=initial_sequence, data_type=self.__data_type)

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        start_empty = [[data_type() for i in range(cols)] for i in range(rows)]
        return Array(starting_sequence=start_empty)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        if row_index > 0 and row_index > self.__num_rows:
            raise IndexError("Row index out of bounds")
        elif row_index < 0 and row_index < -self.__num_rows:
            raise IndexError("Row index out of bounds")
        else:
            return Array2D.Row(row_index = row_index, array = self.__elements, num_columns = self.__num_columns, data_type = self.__data_type)
        
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        for i in range(self.__num_rows):
            yield self[i]
    
    def __reversed__(self):
        for i in range(self.__num_rows-1, -1, -1):
            yield self[i]
    
    def __len__(self): 
        return self.__num_rows
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.__num_rows} Rows x {self.__num_columns} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')