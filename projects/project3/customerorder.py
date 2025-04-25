from datastructures.linkedlist import LinkedList
from .orderitem import OrderItem
from typing import Iterator


class CustomerOrder():

    def __init__(self, name : str) -> None:
        self._name = name
        self._items = LinkedList(data_type = OrderItem)

    def add_item(self, item: OrderItem) -> None:
        self._items.append(item)
    
    def repeat_order(self) -> None:
        print()
        print(self._name)
        for orderitem in self._items:
            print()
            print(orderitem)
        print()

    def get_total_price(self) -> float:
        total = 0
        for item in self._items:
            total += item.price()
        return total

    def drinks(self) -> Iterator[str]:
        for item in self._items:
            yield item.drink()

    def __len__(self) -> int:
        return len(self._items)