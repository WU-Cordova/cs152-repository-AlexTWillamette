from datastructures.linkedlist import LinkedList
from .orderitem import OrderItem
from typing import Iterator


class CustomerOrder():
    """
    Class to handle a customer's order.
    Contains a name (the customer's) as a string and a linkedlist of order items.
    """
    def __init__(self, name : str) -> None:
        """
        Initializes the CustomerOrder.
        Order is made with the name at first, while the items is an empty linkedlist,
        to be added to later as the order is made, for flexible order size.
        """
        self._name = name
        self._items = LinkedList(data_type = OrderItem)

    def add_item(self, item: OrderItem) -> None:
        """
        Adds an order item to the linkedlists of orders.
        """
        self._items.append(item)
    
    def repeat_order(self) -> None:
        """
        Prints information about the order.
        Starting with the name,
        then every item in the order sequentially.
        """
        print()
        print(self._name)
        for orderitem in self._items:
            print()
            print(orderitem)
        print()

    def drinks(self) -> Iterator[str]:
        """
        Returns an iterator over the names of all the drinks
        in the order.
        """
        for item in self._items:
            yield item.drink()

    def __len__(self) -> int:
        """
        Returns the number of items in the order.
        """
        return len(self._items)