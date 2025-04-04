from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence, Iterator
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.data_type = data_type
        self.count = 0
        self.head = self.tail = None
        
    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        
        if data_type == object:
            data_type = type(sequence[0])
        for item in sequence:
            if not isinstance(item, data_type):
                raise TypeError
        
        llist = LinkedList(data_type=data_type)
        for item in sequence:
            llist.append(item)

        return llist

    def append(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item is not a {self.data_type}")

        node = LinkedList.Node(item)

        if self.empty:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node

        self.count += 1

    def prepend(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item is not a {self.data_type}")

        node = LinkedList.Node(item)

        if self.empty:
            self.head = self.tail = node
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node

        self.count += 1


    def insert_before(self, target: T, item: T) -> None:
        if not isinstance(target, self.data_type):
            raise TypeError(f"Target is not a {self.data_type}")
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item is not a {self.data_type}")
        
        travel = self.head
        while travel:
            if travel.data == target:
                break
            travel = travel.next
        if travel == None:
            raise ValueError("Target does not exist in linked list.")

        node = LinkedList.Node(item)
        if travel is self.head:
            self.prepend(item)
        else:
            node.previous = travel.previous
            travel.previous.next = node
            node.next = travel
            travel.previous = node

        self.count += 1

    def insert_after(self, target: T, item: T) -> None:
        if not isinstance(target, self.data_type):
            raise TypeError(f"Target is not a {self.data_type}")
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item is not a {self.data_type}")

        travel = self.head
        while travel:
            if travel.data == target:
                break
            travel = travel.next
        if travel == None:
            raise ValueError("Target does not exist in linked list.")

        node = LinkedList.Node(item)
        if travel is self.tail:
            self.append(item)
        else:
            node.next = travel.next
            travel.next.previous = node
            node.previous = travel
            travel.next = node

        self.count += 1

    def remove(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item is not a {self.data_type}")

        travel = self.head
        while travel:
            if travel.data == item:
                break
            travel = travel.next
        if travel == None:
            raise ValueError("Item not in linked list.")

        if travel == self.head:
            self.pop_front()
        elif travel == self.tail:
            self.pop()
        else:
            travel.next.previous = travel.previous
            travel.previous.next = travel.next
            self.count -= 1

    def remove_all(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item is not a {self.data_type}")

        travel = self.head
        while travel:
            if travel.data == item:
                if travel == self.head:
                    self.pop_front()
                elif travel == self.tail:
                    self.pop()
                else:
                    travel.next.previous = travel.previous
                    travel.previous.next = travel.next
                    self.count -= 1
            travel = travel.next

    def pop(self) -> T:
        if self.empty:
            raise IndexError("Linked list is empty")

        item = self.tail.data

        self.tail = self.tail.previous
        if self.tail != None:
            self.tail.next = None
        
        self.count -= 1

        return item

    def pop_front(self) -> T:
        if self.empty:
            raise IndexError("Linked list is empty")

        item = self.head.data

        self.head = self.head.next
        if self.head != None:
            self.head.previous = None

        self.count -= 1

        return item

    @property
    def front(self) -> T:
        if self.empty:
            raise IndexError("Linked list is empty")
        return self.head.data

    @property
    def back(self) -> T:
        if self.empty:
            raise IndexError("Linked list is empty")
        return self.tail.data

    @property
    def empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def __contains__(self, item: T) -> bool:
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def __iter__(self) -> Iterator[T]:
        self.travel_node = self.head
        return self

    def __next__(self) -> T:
        if self.travel_node is None:
            raise StopIteration
        data = self.travel_node.data
        self.travel_node = self.travel_node.next
        return data
    
    def __reversed__(self) -> ILinkedList[T]:
        revlist = LinkedList(data_type=self.data_type)
        travel = self.tail
        while travel:
            revlist.append(travel.data)
            travel = travel.previous
        return revlist

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ILinkedList):
            return False
        if len(other) != self.count:
            return False
        if list(self) == list(other):
            return True
        return False

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
