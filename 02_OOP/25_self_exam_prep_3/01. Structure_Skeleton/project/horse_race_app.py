from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse_in_list = [h for h in self.horses if h.name == horse_name]
        if horse_in_list:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type not in ["Appaloosa", "Thoroughbred"]:
            return

        horse = None
        if horse_type == "Appaloosa":
            horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            horse = Thoroughbred(horse_name, horse_speed)

        self.horses.append(horse)

        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for j in self.jockeys:
            if j.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for hr in self.horse_races:
            if hr.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        horse_raise = HorseRace(race_type)
        self.horse_races.append(horse_raise)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = None
        for j in self.jockeys:
            if j.name == jockey_name:
                jockey = j

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = None
        for h in self.horses:
            if not h.is_taken and h.__class__.__name__ == horse_type:
                horse = h

        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if horse and jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = None
        for hr in self.horse_races:
            if hr.race_type == race_type:
                horse_race = hr

        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = None
        for j in self.jockeys:
            if j.name == jockey_name:
                jockey = j

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey and not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = None
        for hr in self.horse_races:
            if hr.race_type == race_type:
                horse_race = hr

        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner_jockey = None
        highest_speed = 0

        for jockey in horse_race.jockeys:
            if jockey.horse.speed > highest_speed:
                winner_jockey = jockey
                highest_speed = jockey.horse.speed

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {winner_jockey.name}! " \
               f"Winner's horse: {winner_jockey.horse.name}."
