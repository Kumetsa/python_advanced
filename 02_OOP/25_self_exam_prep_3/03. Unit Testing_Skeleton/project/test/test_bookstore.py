from unittest import TestCase
import unittest

from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(3)

    def test_correct_init(self):
        self.assertEqual(3, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_invalid_book_limit_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))
        self.assertEqual(3, self.bookstore.books_limit)

    def test_invalid_book_limit_negative(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -1

        self.assertEqual("Books limit of -1 is not valid", str(ve.exception))
        self.assertEqual(3, self.bookstore.books_limit)

    def test_len_method(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Math 101": 1,
            "Physics": 1
        }
        result = len(self.bookstore)
        self.assertEqual(result, len(self.bookstore))

    def test_len_method_no_books(self):
        result = len(self.bookstore)
        self.assertEqual(result, len(self.bookstore))

    def test_receive_book_book_limit_reached_raises_exception(self):
        self.bookstore.books_limit = 2
        self.bookstore.availability_in_store_by_book_titles = {
            "Math 101": 1,
            "Physics": 1
        }

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Ninjas", 2)

        self.assertEqual("Books limit is reached. Cannot receive more books!",
                         str(ex.exception))

        self.assertEqual({
            "Math 101": 1,
            "Physics": 1
        }, self.bookstore.availability_in_store_by_book_titles)

    def test_receive_book_successful_returns_message(self):
        self.bookstore.books_limit = 5
        self.bookstore.availability_in_store_by_book_titles = {
            "Math 101": 1,
            "Physics": 1
        }

        result = self.bookstore.receive_book("Ninjas", 2)

        self.assertEqual({
            "Math 101": 1,
            "Physics": 1,
            "Ninjas": 2,
        }, self.bookstore.availability_in_store_by_book_titles)

        new_books = self.bookstore.availability_in_store_by_book_titles["Ninjas"]
        self.assertEqual(2, new_books)

        self.assertEqual("2 copies of Ninjas are available in the bookstore.", result)

    def test_sell_book_not_existing_raises_exception(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Math 101": 1,
            "Physics": 1
        }

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Ninjas", 1)
        self.assertEqual("Book Ninjas doesn't exist!", str(ex.exception))

        self.assertEqual({
            "Math 101": 1,
            "Physics": 1,
        }, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_existing_not_enough_qty_raises_exception(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Math 101": 1,
            "Physics": 1
        }

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Math 101", 2)
        self.assertEqual("Math 101 has not enough copies to sell. Left: 1"
                         , str(ex.exception))

        self.assertEqual({
            "Math 101": 1,
            "Physics": 1,
        }, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_successfully_expect_decrease_in_book_return_message(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Math 101": 1,
            "Physics": 1
        }
        self.assertEqual(0, self.bookstore.total_sold_books)
        result = self.bookstore.sell_book("Math 101", 1)
        self.assertEqual({
            "Math 101": 0,
            "Physics": 1
        }, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(1, self.bookstore.total_sold_books)
        self.assertEqual("Sold 1 copies of Math 101", result)

    def test_bookstore_with_available_books_string_representation(self):
        self.bookstore.books_limit = 20
        self.bookstore.receive_book("Book A", 10)
        self.bookstore.receive_book("Book B", 5)

        expected_output = "Total sold books: 0\nCurrent availability: 15\n - Book A: 10 copies\n - Book B: 5 copies"
        self.assertEqual(str(self.bookstore), expected_output)

    def test_empty_bookstore_string_representation(self):
        expected_output = "Total sold books: 0\nCurrent availability: 0"
        self.assertEqual(str(self.bookstore), expected_output)


if __name__ == "__main__":
    unittest.main()
