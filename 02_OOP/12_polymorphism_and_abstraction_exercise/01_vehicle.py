from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        pass


class Car(Vehicle):
    CONDITIONER_ON = 0.9

    def drive(self, distance: float) -> None:
        fuel_needed = distance * (self.fuel_consumption + Car.CONDITIONER_ON)

        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITIONER_ON = 1.6
    HOLE_IN_TANK = 0.95

    def drive(self, distance: float) -> None:
        fuel_needed = distance * (self.fuel_consumption + Truck.CONDITIONER_ON)

        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * Truck.HOLE_IN_TANK
