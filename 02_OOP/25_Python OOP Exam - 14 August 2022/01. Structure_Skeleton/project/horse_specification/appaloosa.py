from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        if self.speed > Appaloosa.MAX_SPEED:
            raise ValueError("Horse speed is too high!")

    def train(self) -> None:
        self.speed = min(self.speed + 2, self.MAX_SPEED)
