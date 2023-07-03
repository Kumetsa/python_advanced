class Flower:
    def __init__(self, name: str, water_req: int):
        self.name = name
        self.water_requirements = water_req
        self.is_happy = False

    def water(self, water_received: int) -> None:
        if water_received >= self.water_requirements:
            self.is_happy = True

    def status(self) -> str:
        if self.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())