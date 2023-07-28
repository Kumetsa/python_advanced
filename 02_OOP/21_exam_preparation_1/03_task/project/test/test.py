from unittest import TestCase
import unittest

from project.movie import Movie


class TestMovie(TestCase):

    def setUp(self) -> None:
        self.movie = Movie("Matrix", 1995, 9.5)
        self.movie2 = Movie("Titanic", 1999, 8.5)

    def test_correct_movie_initialization(self):
        self.assertEqual("Matrix", self.movie.name)
        self.assertEqual(1995, self.movie.year)
        self.assertEqual(9.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_empty_string_name_initialization_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.movie = Movie("", 1995, 9.5)

        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_year_less_than_1887_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.movie = Movie("Matrix", 1886, 9.5)

        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_successful_add_actor_if_actor_not_in_list(self):
        self.assertEqual([], self.movie.actors)

        self.movie.add_actor("Keanu Reeves")

        self.assertEqual(["Keanu Reeves"], self.movie.actors)

    def test_unsuccessful_add_actor_if_actor_in_list_expect_msg(self):
        self.movie.add_actor("Keanu Reeves")

        self.assertEqual(["Keanu Reeves"], self.movie.actors)

        result = self.movie.add_actor("Keanu Reeves")
        self.assertEqual(result, "Keanu Reeves is already added in the list of actors!")

        self.assertEqual(["Keanu Reeves"], self.movie.actors)
        self.assertEqual(1, len(self.movie.actors))

    def test__gt__method_movie_rating_greater_than_movie2_rating(self):
        self.assertTrue(self.movie.rating > self.movie2.rating)

        result = self.movie.__gt__(self.movie2)
        self.assertEqual('"Matrix" is better than "Titanic"', result)

    def test__gt_method_movie_rating_less_than_movie2_rating(self):
        self.movie.rating = 7.5
        self.assertTrue(self.movie.rating < self.movie2.rating)

        result = self.movie.__gt__(self.movie2)
        self.assertEqual('"Titanic" is better than "Matrix"', result)

    def test_correct__repr__method_no_actors(self):
        expected_result = f"Name: Matrix\n" \
                          f"Year of Release: 1995\n" \
                          f"Rating: 9.50\n" \
                          f"Cast: "

        result = self.movie.__repr__()

        self.assertEqual(expected_result, result)

    def test_correct__repr__method_with_actors(self):
        self.movie.add_actor("Keanu Reeves")
        self.movie.add_actor("Laurence Fishburn")

        expected_result = f"Name: Matrix\n" \
                          f"Year of Release: 1995\n" \
                          f"Rating: 9.50\n" \
                          f"Cast: Keanu Reeves, Laurence Fishburn"

        result = self.movie.__repr__()

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
