from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACY = ["Gingerbread", "Stolen"]
    VALID_BOOTH = ["Open Booth", "Private Booth"]

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in ChristmasPastryShopApp.VALID_DELICACY:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        for d in self.delicacies:
            if d.name == name:
                raise Exception(f"{name} already exists!")

        if type_delicacy == "Gingerbread":
            delicacy = Gingerbread(name, price)
            self.delicacies.append(delicacy)
        elif type_delicacy == "Stolen":
            delicacy = Stolen(name, price)
            self.delicacies.append(delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int) -> str:
        if type_booth not in ChristmasPastryShopApp.VALID_BOOTH:
            raise Exception(f"{type_booth} is not a valid booth!")

        for b in self.booths:
            if b.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth == "Open Booth":
            booth = OpenBooth(booth_number, capacity)
            self.booths.append(booth)
        elif type_booth == "Private Booth":
            booth = PrivateBooth(booth_number, capacity)
            self.booths.append(booth)

        return f"Added booth number {booth_number} in the pastry shop."
        # TODO error here or in the below method ?

    def reserve_booth(self, number_of_people: int) -> str:
        for b in self.booths:
            if not b.is_reserved and b.capacity >= number_of_people:
                b.reserve(number_of_people)
                return f"Booth {b.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str) -> str:
        booth = self.get_booth_by_number(booth_number)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.get_delicacy_by_name(delicacy_name)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.get_booth_by_number(booth_number)
        bill = 0
        bill += booth.price_for_reservation
        for d in booth.delicacy_orders:
            bill += d.price

        self.income += bill
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    # ----------Helpers--------------

    def get_delicacy_by_name(self, delicacy_name: str):
        try:
            return [d for d in self.delicacies if d.name == delicacy_name][0]
        except:
            return None

    def get_booth_by_number(self, booth_number: int):
        try:
            return [b for b in self.booths if b.booth_number == booth_number][0]
        except:
            return None
