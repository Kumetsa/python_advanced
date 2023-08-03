from abc import ABC, abstractmethod


class Delicacy(ABC):
    def __init__(self, name: str, portion: int, price: float):
        self.name = name
        self.portion = portion
        self.price = price
        
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value) -> None:
        if not value.strip():
            raise ValueError("Name cannot be null or whitespace!")
        self.__name = value

    @property
    def price(self) -> float:
        return self.__price
    
    @price.setter
    def price(self, value) -> None:
        if value <= 0.0:
            raise ValueError("Price cannot be less or equal to zero!")
        self.__price = value

    @abstractmethod
    def details(self):
        pass