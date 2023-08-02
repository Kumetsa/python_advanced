from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        if self.speed > Thoroughbred.MAX_SPEED:
            raise ValueError("Horse speed is too high!")

    def train(self) -> None:
        self.speed = min(self.speed + 3, self.MAX_SPEED)
