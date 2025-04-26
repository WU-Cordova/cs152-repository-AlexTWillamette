from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.__bagdict__ = {}
        for item in items:
            if item is None:
                raise TypeError
            else:
                if item in self.__bagdict__.keys():
                    self.__bagdict__[item] += 1
                else:
                    self.__bagdict__[item] = 1 

    def add(self, item: T) -> None:
        if item is None:
            raise TypeError
        else:
            if item in self.__bagdict__.keys():
                    self.__bagdict__[item] += 1
            else:
                self.__bagdict__[item] = 1 

    def remove(self, item: T) -> None:
        if item in self.__bagdict__.keys():
                self.__bagdict__[item] -= 1
                if self.__bagdict__[item] == 0:
                    self.__bagdict__.pop(item)
        else:
            raise ValueError

    def count(self, item: T) -> int:
        if item in self.__bagdict__.keys():
            return self.__bagdict__[item]
        else:
            return 0

    def __len__(self) -> int:
        totalcount = 0
        for count in self.__bagdict__.values():
            totalcount += count
        return totalcount

    def distinct_items(self) -> int:
        return self.__bagdict__.keys()

    def __contains__(self, item) -> bool:
        if item in self.__bagdict__.keys():
            return True
        else:
            return False

    def clear(self) -> None:
        self.__bagdict__ = {}