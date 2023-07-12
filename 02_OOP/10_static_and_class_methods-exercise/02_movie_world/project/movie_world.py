from typing import List, Optional

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = self.find_customer_by_id(customer_id)
        dvd = self.find_dvd_by_id(dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def find_customer_by_id(self, customer_id: int) -> Optional[Customer]:
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None

    def find_dvd_by_id(self, dvd_id: int) -> Optional[DVD]:
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                return dvd
        return None

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = self.find_customer_by_id(customer_id)
        dvd = self.find_dvd_by_id(dvd_id)

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self) -> str:
        customer_repr = "\n".join(repr(customer) for customer in self.customers)
        dvd_repr = "\n".join(repr(dvd) for dvd in self.dvds)
        return f"{customer_repr}\n{dvd_repr}"




