from copy import deepcopy
from .drink import Drink

class OrderItem():
    """
    Class to handle a single item on an order.
    Contains a drink and a customization.
    """

    def __init__(self, drink : Drink, customization : str) -> None:
        """
        Initializes an OrderItem.
        Assigns values to instance variables.
        """
        self._drink = deepcopy(drink)
        self._customization = customization

    def __str__(self) -> str:
        """
        Returns a 2 line representation of the OrderItem,
        for repeating back the order.
        """
        return f"{self._drink} \n {self._customization}"

    def drink(self) -> str:
        """ 
        Returns the name of the drink on the order item.
        """
        return self._drink.name

    def price(self) -> float:
        """
        Returns the price of the drink on the order item.
        """
        return self._drink.price
