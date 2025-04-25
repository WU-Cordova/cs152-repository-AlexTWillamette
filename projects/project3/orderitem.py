from copy import deepcopy
from .drink import Drink

class OrderItem():

    def __init__(self, drink : Drink, customization : str) -> None:
        self._drink = deepcopy(drink)
        self._customization = customization

    def __str__(self) -> str:
        return f"{self._drink} \n {self._customization}"

    def drink(self) -> str:
        return self._drink.name

    def price(self) -> float:
        return self._drink.price
