from project.cat import Cat


class Kitten(Cat):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.gender = "Female"

    def make_sound(self):
        return "Meow"