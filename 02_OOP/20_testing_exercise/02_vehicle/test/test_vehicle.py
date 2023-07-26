from unittest import TestCase
import unittest

from project.vehicle import Vehicle


class VehicleTest(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(30.5, 110.5)

    def test_default_consumption_class_att_is_correct(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_initialization_of_vehicle(self):
        self.assertEqual(30.5, self.vehicle.fuel)
        self.assertEqual(30.5, self.vehicle.capacity)
        self.assertEqual(110.5, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_method_with_insufficient_fuel_raises(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_method_with_sufficient_fuel_expect_fuel_decrease(self):
        self.assertEqual(30.5, self.vehicle.fuel)

        self.vehicle.drive(1)

        self.assertEqual(29.25, self.vehicle.fuel)

    def test_refuel_if_too_much_fuel_raises(self):
        self.assertEqual(30.5, self.vehicle.fuel)
        self.assertEqual(30.5, self.vehicle.capacity)

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)

        self.assertEqual("Too much fuel", str(ex.exception))

        self.assertEqual(30.5, self.vehicle.fuel)
        self.assertEqual(30.5, self.vehicle.capacity)

    def test_refuel_successfully(self):
        self.vehicle.fuel = 0
        self.assertEqual(0, self.vehicle.fuel)
        self.assertEqual(30.5, self.vehicle.capacity)

        self.vehicle.refuel(5)
        self.assertEqual(5, self.vehicle.fuel)
        self.assertEqual(30.5, self.vehicle.capacity)

    def test_correct__str__method(self):
        expected_result = f"The vehicle has 110.5 " \
               f"horse power with 30.5 fuel left and 1.25 fuel consumption"

        expected_result_2 = str(self.vehicle)

        self.assertEqual(expected_result, self.vehicle.__str__())
        self.assertEqual(expected_result_2, self.vehicle.__str__())


if __name__ == "__main__":
    unittest.main()