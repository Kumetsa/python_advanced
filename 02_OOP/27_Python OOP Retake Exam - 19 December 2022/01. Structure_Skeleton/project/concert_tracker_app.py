from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = ["Guitarist", "Drummer", "Singer"]

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def _get_musician_by_name(self, name: str):
        try:
            musician = [m for m in self.musicians if m.name == name][0]
            return musician
        except IndexError:
            return None

    def _get_band_by_name(self, name):
        try:
            band = [b for b in self.bands if b.name == name][0]
            return band
        except IndexError:
            return None

    @staticmethod
    def _is_in_band(musician, band):
        for bm in band.members:
            if bm.name == musician.name:
                return True
        return False

    @staticmethod
    def all_members_to_play(band):
        has_singer = False
        has_drummer = False
        has_guitarist = False

        for member in band.members:
            if isinstance(member, Singer):
                has_singer = True
            elif isinstance(member, Drummer):
                has_drummer = True
            elif isinstance(member, Guitarist):
                has_guitarist = True

        if has_singer and has_drummer and has_guitarist:
            return True
        return False

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ConcertTrackerApp.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        musician_exist = self._get_musician_by_name(name)
        if musician_exist:
            raise Exception(f"{name} is already a musician!")

        if musician_type == "Singer":
            musician = Singer(name, age)
            self.musicians.append(musician)
        elif musician_type == "Drummer":
            musician = Drummer(name, age)
            self.musicians.append(musician)
        elif musician_type == "Guitarist":
            musician = Guitarist(name, age)
            self.musicians.append(musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for b in self.bands:
            if b.name == name:
                raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for c in self.concerts:
            if c.place == place:
                concert_genre = c.genre
                raise Exception(f"{place} is already registered for {concert_genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._get_musician_by_name(musician_name)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = self._get_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self._get_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = [bm for bm in band.members if bm.name == musician_name][0]
            band.members.remove(musician)
            return f"{musician_name} was removed from {band_name}."

        except IndexError:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

    def start_concert(self, concert_place: str, band_name: str):
        band = self._get_band_by_name(band_name)

        if not self.all_members_to_play(band):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = [c for c in self.concerts if c.place == concert_place][0]

        if concert.genre == "Rock":
            drummer_needed_skill = ["play the drums with drumsticks"]
            singer_needed_skill = ["sing high pitch notes"]
            guitarist_needed_skill = ["play rock"]
            for member in band.members:
                if isinstance(member, Drummer) and not set(drummer_needed_skill).issubset(set(member.skills)):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Singer) and not set(singer_needed_skill).issubset(set(member.skills)):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Guitarist) and not set(guitarist_needed_skill).issubset(set(member.skills)):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Metal":
            drummer_needed_skill = ["play the drums with drumsticks"]
            singer_needed_skill = ["sing low pitch notes"]
            guitarist_needed_skill = ["play metal"]

            for member in band.members:
                if isinstance(member, Drummer) and not set(drummer_needed_skill).issubset(set(member.skills)):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Singer) and not set(singer_needed_skill).issubset(set(member.skills)):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Guitarist) and not set(guitarist_needed_skill).issubset(set(member.skills)):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Jazz":
            drummer_needed_skill = ["play the drums with drum brushes"]
            singer_needed_skill = ["sing high pitch notes", "sing low pitch notes"]
            guitarist_needed_skill = ["play jazz"]

            for member in band.members:
                if isinstance(member, Drummer) and not set(drummer_needed_skill).issubset(set(member.skills)):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Singer) and not set(singer_needed_skill).issubset(set(member.skills)):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Guitarist) and not set(guitarist_needed_skill).issubset(set(member.skills)):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."