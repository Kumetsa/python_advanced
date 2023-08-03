from project.toy_store import ToyStore
from unittest import TestCase
import unittest


class TestToyStore(TestCase):

    def test_correct_initializations(self):
        toy_store = ToyStore()
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, toy_store.toy_shelf)

    def test_add_toy_shelf_not_in_dict_raise_exception(self):
        toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            toy_store.add_toy("J", "Bear")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_given_is_already_on_the_shelf_raises_exception(self):
        toy_store = ToyStore()
        toy_store.add_toy("A", "Bear")

        with self.assertRaises(Exception) as ex:
            toy_store.add_toy("A", "Bear")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))
        self.assertEqual({
            "A": "Bear",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, toy_store.toy_shelf)

    def test_correct_add_toy_changes_dict_returns_message(self):
        toy_store = ToyStore()
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, toy_store.toy_shelf)
        toy_store.add_toy("A", "Bear")
        result = toy_store.add_toy("B", "Kitty")

        self.assertEqual({
            "A": "Bear",
            "B": "Kitty",
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, toy_store.toy_shelf)

        self.assertEqual("Toy:Kitty placed successfully!", result)

    def test_remove_toy_shelf_does_not_exist_raises_exception(self):
        toy_store = ToyStore()

        with self.assertRaises(Exception) as ex:
            toy_store.remove_toy("J", "Bear")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, toy_store.toy_shelf)

    def test_remove_toy_that_is_not_on_the_shelf_raises_exception(self):
        toy_store = ToyStore()
        toy_store.add_toy("A", "Bear")

        with self.assertRaises(Exception) as ex:
            toy_store.remove_toy("A", "Kitty")

        self.assertEqual("Toy in that shelf doesn't exists!",
                         str(ex.exception))
        self.assertEqual({
            "A": "Bear",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, toy_store.toy_shelf)

    def test_remove_toy_successfully_receive_message(self):
        toy_store = ToyStore()
        toy_store.add_toy("A", "Bear")

        result = toy_store.remove_toy("A", "Bear")

        self.assertEqual("Remove toy:Bear successfully!", result)
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, toy_store.toy_shelf)


if __name__ == "__main__":
    unittest.main()