from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayerClass(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("John", 18, 100.5)

    def test_correct_initialization(self):
        self.assertEqual("John", self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(100.5, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_incorrect_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player1 = TennisPlayer("Al", 20, 0)

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_incorrect_age_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player1 = TennisPlayer("Alex", 17, 0)

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_correctly_expect_append_in_wins_list(self):
        self.assertEqual([], self.player.wins)

        result = self.player.add_new_win("Roland Gars")
        self.assertIsNone(result)
        self.assertEqual(["Roland Gars"], self.player.wins)

    def test_add_new_win_already_in_list_returns_message(self):
        self.player.add_new_win("Roland Gars")

        result = self.player.add_new_win("Roland Gars")

        self.assertEqual("Roland Gars has been already added to the list of wins!", result)


    def test_lt_method(self):
        self.player1 = TennisPlayer("Roger Federer", 39, 2000.0)
        self.player2 = TennisPlayer("Rafael Nadal", 35, 1800.0)
        self.player3 = TennisPlayer("Novak Djokovic", 34, 2200.0)
        result = self.player1 < self.player3
        self.assertEqual('Novak Djokovic is a top seeded player and he/she is better than Roger Federer', result)

        result2 = self.player1 < self.player2
        self.assertEqual('Roger Federer is a better player than Rafael Nadal', result2)

    def test_str_method_no_win(self):
        self.player1 = TennisPlayer("Roger Federer", 39, 2000.0)

        self.assertEqual(
            str(self.player1),
            "Tennis Player: Roger Federer\n"
            "Age: 39\n"
            "Points: 2000.0\n"
            "Tournaments won: "
        )

    def test_str_with_win(self):
        self.player1 = TennisPlayer("Roger Federer", 39, 2000.0)

        self.player1.add_new_win("Australian Open")
        self.player1.add_new_win("Wimbledon")
        self.assertEqual(
            str(self.player1),
            "Tennis Player: Roger Federer\n"
            "Age: 39\nPoints: 2000.0\n"
            "Tournaments won: Australian Open, Wimbledon")


if __name__ == '__main__':
    main()