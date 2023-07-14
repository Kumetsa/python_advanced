from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food: Food):
        pass


class Bird(Animal):
    def __init__(self, name: str, weight: int, wing_size: float):
        self.name = name
        self.weight = weight
        self.wing_size = wing_size
        self.food_eaten = 0

    def make_sound(self):
        pass

    def feed(self, food: Food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    def __init__(self, name: str, weight: int, living_region: str):
        self.name = name
        self.weight = weight
        self.living_region = living_region
        self.food_eaten = 0

    def make_sound(self):
        pass

    def feed(self, food: Food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


