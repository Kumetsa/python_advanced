from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"

    def __add__(self, other) -> str:
        return Person(self.name, other.surname)

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name: str, people: List[Person]) -> None:
        self.name = name
        self.people = people

    def __len__(self) -> int:
        return len(self.people)

    def __add__(self, other) -> object:
        new_name = f"{self.name} {other.name}"
        new_people = self.people + other.people
        return Group(new_name, new_people)

    def __str__(self) -> str:
        members = ", ".join(str(person) for person in self.people)
        return f"Group {self.name} with members {members}"

    def __getitem__(self, index) -> str:
        person = self.people[index]
        return f"Person {index}: {person.name} {person.surname}"

    def __iter__(self) -> str:
        for index, person in enumerate(self.people):
            yield f"Person {index}: {person.name} {person.surname}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3
first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group
print(len(first_group))
print(second_group)
print(third_group[0])
for person in third_group:
    print(person)
