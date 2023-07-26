from project.mammal import Mammal
from unittest import TestCase
import unittest


class MammalTest(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Frankie", "Dog", "Woof")

    def test_initialize_mammal(self):
        self.assertEqual("Frankie", self.mammal.name)
        self.assertEqual("Dog", self.mammal.type)
        self.assertEqual("Woof", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound(self):
        expected_result = "Frankie makes Woof"
        result = self.mammal.make_sound()
        self.assertEqual(expected_result, result)

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_info(self):
        expected_result = "Frankie is of type Dog"
        result = self.mammal.info()

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()






