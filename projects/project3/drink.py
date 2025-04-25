from dataclasses import dataclass

@dataclass
class Drink:
    name : str
    size : str # "Medium" always
    price: float

    def __str__(self) -> str:
        return f"{self.name}, {self.size}, ${self.price:.2f}."