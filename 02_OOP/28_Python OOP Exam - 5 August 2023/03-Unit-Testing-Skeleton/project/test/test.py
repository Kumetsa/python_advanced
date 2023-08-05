from unittest import TestCase
import unittest

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.bmw = SecondHandCar("BWM", "320", 5000, 7000)

    def test_correct_init(self):
        self.assertEqual("BWM", self.bmw.model)
        self.assertEqual("320", self.bmw.car_type)
        self.assertEqual(5000, self.bmw.mileage)
        self.assertEqual(7000, self.bmw.price)
        self.assertEqual([], self.bmw.repairs)

    def test_invalid_price(self):
        self.assertEqual(7000, self.bmw.price)
        with self.assertRaises(ValueError) as ve:
            self.bmw.price = 0.5

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))
        self.assertEqual(7000, self.bmw.price)

    def test_invalid_mileage(self):
        self.assertEqual(5000, self.bmw.mileage)
        with self.assertRaises(ValueError) as ve:
            self.bmw.mileage = 50
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!',
                         str(ve.exception))
        self.assertEqual(5000, self.bmw.mileage)

    def test_set_promo_price_greater_raises_ve(self):
        self.assertEqual(7000, self.bmw.price)

        with self.assertRaises(ValueError) as ve:
            self.bmw.set_promotional_price(8000)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))
        self.assertEqual(7000, self.bmw.price)

    def test_set_promo_price_correctly_receive_message(self):
        self.assertEqual(7000, self.bmw.price)

        result = self.bmw.set_promotional_price(6000)

        self.assertEqual('The promotional price has been successfully set.', result)
        self.assertEqual(6000, self.bmw.price)

    def test_need_repair_repair_price_too_high_return_msg(self):
        result = self.bmw.need_repair(5000, "Glava")

        self.assertEqual('Repair is impossible!', result)

    def test_need_repair_price_low_add_repair_to_list_chage_price_return_msg(self):
        self.assertEqual(7000, self.bmw.price)
        self.assertEqual([], self.bmw.repairs)

        result = self.bmw.need_repair(500, "Tire")

        self.assertEqual(7500, self.bmw.price)
        self.assertEqual(["Tire"], self.bmw.repairs)
        self.assertEqual('Price has been increased due to repair charges.', result)

    # Test magic methods now

    def test_gt_method_same_car_type(self):
        car1 = SecondHandCar("Toyota Corolla", "Sedan", 50000, 10000.0)
        car2 = SecondHandCar("Honda Civic", "Sedan", 60000, 9000.0)

        self.assertTrue(car1 > car2)

    def test_gt_method_different_car_type(self):
        car1 = SecondHandCar("Toyota Corolla", "Sedan", 50000, 10000.0)
        car2 = SecondHandCar("Ford F-150", "Truck", 60000, 12000.0)

        self.assertEqual(car1 > car2, 'Cars cannot be compared. Type mismatch!')

    def test_str_method_no_repairs(self):
        car = SecondHandCar("Toyota Corolla", "Sedan", 50000, 10000.0)

        expected_output = "Model Toyota Corolla | Type Sedan | Milage 50000km\n" \
                          "Current price: 10000.00 | Number of Repairs: 0"
        self.assertEqual(str(car), expected_output)

    def test_str_method_with_repairs(self):
        car = SecondHandCar("Toyota Corolla", "Sedan", 50000, 10000.0)
        car.need_repair(500.0, "Replace brake pads")
        car.need_repair(800.0, "Fix AC")

        expected_output = "Model Toyota Corolla | Type Sedan | Milage 50000km\n" \
                          "Current price: 11300.00 | Number of Repairs: 2"
        self.assertEqual(str(car), expected_output)


if __name__ == "__main__":
    unittest.main()