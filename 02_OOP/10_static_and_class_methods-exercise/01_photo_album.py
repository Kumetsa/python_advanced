from typing import List
import math


class PhotoAlbum:
    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos: List[List[str]] = self.__initialize_photos()
        self.__current_row_index = 0

    def __initialize_photos(self) -> List:
        matrix = []
        for _ in range(self.pages):
            matrix.append([])

        return matrix

    @classmethod
    def from_photos_count(cls, photos_count: int) -> object:
        pages = math.ceil(photos_count/4)

        return cls(pages)

    def add_photo(self, label: str) -> str:
        if len(self.photos[self.__current_row_index]) == 4:
            self.__current_row_index += 1

        try:
            self.photos[self.__current_row_index].append(label)
            return f"{label} photo added successfully on page " \
                   f"{self.__current_row_index + 1}" \
                   f" slot {len(self.photos[self.__current_row_index])}"
        except IndexError:
            return f"No more free slots"

    def display(self) -> str:
        res = "-" * 11 + "\n"
        for page in self.photos:
            res += " ".join(["[]" for photo_name in page]) + "\n"
            res += "-" * 11 + "\n"

        return res


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())








