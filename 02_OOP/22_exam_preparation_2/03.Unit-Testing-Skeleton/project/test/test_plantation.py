from project.plantation import Plantation

from unittest import TestCase
import unittest


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(5)

    def test_correct_initialization(self):
        self.assertEqual(5, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_incorrect_size_expect_value_error(self):
        self.assertEqual(5, self.plantation.size)

        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ve.exception))
        self.assertEqual(5, self.plantation.size)

    def test_hire_worker_who_is_hired_expect_value_error(self):
        self.plantation.workers.append("Miguel")
        self.assertEqual(["Miguel"], self.plantation.workers)

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Miguel")

        self.assertEqual("Worker already hired!", str(ve.exception))
        self.assertEqual(["Miguel"], self.plantation.workers)

    def test_hire_worker_receive_successful_message(self):
        self.assertEqual([], self.plantation.workers)

        result = self.plantation.hire_worker("Miguel")
        self.assertEqual("Miguel successfully hired.", result)
        self.assertEqual(["Miguel"], self.plantation.workers)

    def test__len__method(self):
        self.plantation.size = 3
        self.plantation.hire_worker("Miguel")
        self.plantation.planting("Miguel", "Rose")
        self.assertEqual(1, len(self.plantation))

        self.plantation.planting("Miguel", "Lilly")
        self.assertEqual(2, len(self.plantation))

        self.plantation.hire_worker("Jose")
        self.plantation.planting("Jose", "Rose")

        self.assertEqual({"Miguel": ["Rose", "Lilly"], "Jose": ["Rose"]},
                         self.plantation.plants)
        self.assertEqual(3, len(self.plantation))

    def test_planting_worker_not_in_list_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Miguel", "Lilly")

        self.assertEqual("Worker with name Miguel is not hired!",
                         str(ve.exception))

        self.assertEqual({}, self.plantation.plants)

    def test_planting_plantations_is_full_raises(self):
        self.plantation.size = 0
        self.plantation.hire_worker("Miguel")

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Miguel", "Rose")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_worker_exist(self):
        self.assertEqual({}, self.plantation.plants)
        self.plantation.hire_worker("Miguel")

        result = self.plantation.planting("Miguel", "Rose")
        self.assertEqual({"Miguel": ["Rose"]}, self.plantation.plants)

        self.assertEqual("Miguel planted it's first Rose.", result)

        result2 = self.plantation.planting("Miguel", "Lilly")
        self.assertEqual({"Miguel": ["Rose", "Lilly"]}, self.plantation.plants)
        self.assertEqual("Miguel planted Lilly.", result2)

    def test__str__method(self):
        self.plantation.hire_worker("Miguel")
        self.plantation.hire_worker("Jose")
        self.plantation.planting("Miguel", "Rose")
        self.plantation.planting("Miguel", "Lilly")
        self.plantation.planting("Jose", "Rose")

        result = str(self.plantation)

        expected_result = "Plantation size: 5\nMiguel, Jose\nMiguel planted: Rose, Lilly\nJose planted: Rose"

        self.assertEqual(expected_result, result)

    def test_represent_method(self):
        self.plantation.size = 2
        self.plantation.hire_worker("Miguel")
        self.plantation.hire_worker("Jose")

        result = repr(self.plantation)
        expected_result = f"Size: 2\nWorkers: Miguel, Jose"
        self.assertEqual(expected_result, result)










if __name__ == "__main__":
    unittest.main()
