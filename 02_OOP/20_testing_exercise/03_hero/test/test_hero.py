from unittest import TestCase
import unittest

from project.hero import Hero


class TestHero(TestCase):

    def test_correct_hero1_initialization(self):
        hero = Hero("Frankie", 60, 80.5, 5.5)
        self.assertEqual("Frankie", hero.username)
        self.assertEqual(60, hero.level)
        self.assertEqual(80.5, hero.health)
        self.assertEqual(5.5, hero.damage)

    def test_battle_hero_with_same_name_raises(self):
        hero1 = Hero("Frankie", 60, 80.5, 5.5)
        hero2 = Hero("Frankie", 60, 80.5, 5.5)

        self.assertEqual(hero1.username, hero2.username)

        with self.assertRaises(Exception) as ex:
            hero1.battle(hero2)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_with_with_zero_or_less_health(self):
        hero1 = Hero("Frankie", 60, 0, 5.5)
        hero2 = Hero("Benji", 40, 50.5, 4.5)

        self.assertEqual(0, hero1.health)

        with self.assertRaises(ValueError) as ex:
            hero1.battle(hero2)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_hero_with_with_zero_or_less_health(self):
        hero1 = Hero("Frankie", 60, 80.5, 5.5)
        hero2 = Hero("Benji", 40, -1, 4.5)

        self.assertEqual(-1, hero2.health)

        with self.assertRaises(ValueError) as ex:
            hero1.battle(hero2)

        expected_result = "You cannot fight Benji. He needs to rest"
        self.assertEqual(expected_result, str(ex.exception))

    def test_battle_for_draw(self):
        hero1 = Hero("Frankie", 60, 1, 5.5)
        hero2 = Hero("Benji", 40, 1, 4.5)

        result = hero1.battle(hero2)
        self.assertEqual("Draw", result)

    def test_battle_for_win(self):
        hero1 = Hero("Frankie", 60, 500.5, 5.5)
        hero2 = Hero("Benji", 40, 1, 4.5)

        self.assertEqual(60, hero1.level)
        self.assertEqual(500.5, hero1.health)
        self.assertEqual(5.5, hero1.damage)

        result = hero1.battle(hero2)

        self.assertEqual(61, hero1.level)
        self.assertEqual(325.5, hero1.health)
        self.assertEqual(10.5, hero1.damage)

        self.assertEqual("You win", result)

    def test_battle_for_loss(self):
        hero1 = Hero("Frankie", 60, 1, 5.5)
        hero2 = Hero("Benji", 40, 500.5, 4.5)

        self.assertEqual(40, hero2.level)
        self.assertEqual(500.5, hero2.health)
        self.assertEqual(4.5, hero2.damage)

        result = hero1.battle(hero2)

        self.assertEqual(41, hero2.level)
        self.assertEqual(175.5, hero2.health)
        self.assertEqual(9.5, hero2.damage)

        self.assertEqual("You lose", result)

    def test_hero__str__method(self):
        hero1 = Hero("Frankie", 60, 1, 5.5)

        expected_result = f"Hero Frankie: 60 lvl\n" \
                          f"Health: 1\n" \
                          f"Damage: 5.5\n"

        self.assertEqual(expected_result, hero1.__str__())


if __name__ == "__main__":
    unittest.main()
