from abc import ABC, abstractmethod


class BaseRobot(ABC):
    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value) -> None:
        if not value.strip():
            raise ValueError("Robot name cannot be empty!")
        self.__name = value
        
    @property
    def kind(self) -> str:
        return self.__kind
    
    @kind.setter
    def kind(self, value) -> None:
        if not value.strip():
            raise ValueError("Robot kind cannot be empty!")
        self.__kind = value

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value) -> None:
        if value <= 0.0:
            raise ValueError("Robot price cannot be less than or equal to 0.0!")
        self.__price = value

    @abstractmethod
    def eating(self) -> None:
        pass
