from project.animal import Animal
from project.worker import Worker
from typing import List


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal, price) -> str:
        if len(self.animals) < self.__animal_capacity:
            if self.__budget > price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

            return "Not enough budget"

        return "Not enough space for animals"

    def hire_worker(self, worker) -> str:
        if not len(self.workers) < self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name) -> str:
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries = 0
        for w in self.workers:
            total_salaries += w.salary

        if total_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        total_expenses = 0
        for a in self.animals:
            total_expenses += a.money_for_care

        if total_expenses > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= total_expenses
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetah = []

        for a in self.animals:
            if a.__class__.__name__ == "Lion":
                lions.append(a.__repr__())
            elif a.__class__.__name__ == "Tiger":
                tigers.append(a.__repr__())
            elif a.__class__.__name__ == "Cheetah":
                cheetah.append(a.__repr__())

        lion_string = '\n'.join(lions)
        tiger_string = '\n'.join(tigers)
        cheetah_string = '\n'.join(cheetah)

        return f"You have {len(self.animals)} animals\n----- {len(lions)} Lions:\n{lion_string}\n" \
               f"----- {len(tigers)} Tigers:\n{tiger_string}\n----- {len(cheetah)} Cheetahs:\n{cheetah_string}"

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []

        for w in self.workers:
            if w.__class__.__name__ == "Keeper":
                keepers.append(w.__repr__())
            elif w.__class__.__name__ == "Caretaker":
                caretakers.append(w.__repr__())
            elif w.__class__.__name__ == "Vet":
                vets.append(w.__repr__())

        keepers_string = '\n'.join(keepers)
        caretakers_string = '\n'.join(caretakers)
        vets_string = '\n'.join(vets)

        return f"You have {len(self.workers)} workers\n----- {len(keepers)} Keepers:\n{keepers_string}\n" \
               f"----- {len(caretakers)} Caretakers:\n{caretakers_string}\n----- {len(vets)} Vets:\n{vets_string}"




