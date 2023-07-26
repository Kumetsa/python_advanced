from unittest import TestCase
import unittest

# from CarManager.car_manager import Car


class TestCar(TestCase):
    def setUp(self) -> None:
        self.lambo = Car("Lamborghini", "Gallardo", 10, 80)

    def test_correct_car_initialization(self):
        self.assertEqual("Lamborghini", self.lambo.make)
        self.assertEqual("Gallardo", self.lambo.model)
        self.assertEqual(10, self.lambo.fuel_consumption)
        self.assertEqual(80, self.lambo.fuel_capacity)
        self.assertEqual(0, self.lambo.fuel_amount)

    def test_no_make_raises_ex(self):
        with self.assertRaises(Exception) as ex:
            self.lambo.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raises_ex(self):
        with self.assertRaises(Exception) as ex:
            self.lambo.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_cannot_be_negative_or_zero(self):
        with self.assertRaises(Exception) as ex:
            self.lambo.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!",
                         str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.lambo.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!",
                         str(ex.exception))

    def test_fuel_capacity_cannot_be_negative_or_zero(self):
        with self.assertRaises(Exception) as ex:
            self.lambo.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!",
                         str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.lambo.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!",
                         str(ex.exception))

        def test_fuel_capacity_cannot_be_negative_or_zero(self):
            with self.assertRaises(Exception) as ex:
                self.lambo.fuel_capacity = -1

            self.assertEqual("Fuel capacity cannot be zero or negative!",
                             str(ex.exception))

            with self.assertRaises(Exception) as ex:
                self.lambo.fuel_capacity = 0

            self.assertEqual("Fuel capacity cannot be zero or negative!",
                             str(ex.exception))

    def test_fuel_amount_cannot_be_negative(self):
        with self.assertRaises(Exception) as ex:
            self.lambo.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!",
                         str(ex.exception))

    def test_cannot_refuel_with_zero_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.lambo.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!",
                         str(ex.exception))

    def test_refuel_not_full_tank(self):
        self.lambo.refuel(10)
        self.assertEqual(10, self.lambo.fuel_amount)

    def test_refuel_with_more_than_capacity_expect_fill_to_capacity(self):
        self.lambo.refuel(100)
        self.assertEqual(80, self.lambo.fuel_amount)

    def test_drive_if_not_enough_fuel_raises_exception(self):
        self.lambo.fuel_amount = 20

        with self.assertRaises(Exception) as ex:
            self.lambo.drive(1000)

        self.assertEqual("You don't have enough fuel to drive!",
                         str(ex.exception))

    def test_drive_with_enough_fuel_expect_fuel_amount_decrease(self):
        self.lambo.fuel_amount = 80

        self.lambo.drive(100)

        self.assertEqual(70, self.lambo.fuel_amount)





if __name__ == "__main__":
    unittest.main()
