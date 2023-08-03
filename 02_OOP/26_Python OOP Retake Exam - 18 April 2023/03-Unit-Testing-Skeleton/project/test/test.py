import unittest
from unittest import TestCase
from project.robot import Robot


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("404", "Military", 5, 1000)

    def test_correct_init(self):
        self.assertEqual("404", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(5, self.robot.available_capacity)
        self.assertEqual(1000, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_incorrect_category_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Toy"

        self.assertEqual(
            f"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'",
            str(ve.exception)
        )

    def test_negative_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -2

        self.assertEqual("Price cannot be negative!", str(ve.exception))
        self.assertEqual(1000, self.robot.price)

    def test_upgrade_component_already_added_return_message(self):
        self.robot.upgrade("RAM", 20)
        self.assertEqual(["RAM"], self.robot.hardware_upgrades)
        result = self.robot.upgrade("RAM", 20)

        self.assertEqual("Robot 404 was not upgraded.", result)

        self.assertEqual(["RAM"], self.robot.hardware_upgrades)

    def test_upgrade_robot_successfully_add_comp_increase_price_return_message(self):
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual(1000, self.robot.price)

        result = self.robot.upgrade("RAM", 20)

        self.assertEqual(["RAM"], self.robot.hardware_upgrades)
        self.assertEqual(1030, self.robot.price)
        self.assertEqual(
            'Robot 404 was upgraded with RAM.',
            result
        )

    def test_update_successful_decrease_capacity_add_soft_update_return_message(self):
        self.assertEqual([], self.robot.software_updates)
        self.assertEqual(5, self.robot.available_capacity)

        result = self.robot.update(3.14, 2)

        self.assertEqual([3.14], self.robot.software_updates)
        self.assertEqual(3, self.robot.available_capacity)
        self.assertEqual(f'Robot 404 was updated to version 3.14.', result)

    def test_update_not_needed_latest_version_return_msg(self):
        self.robot.update(3.14, 2)
        self.assertEqual([3.14], self.robot.software_updates)
        self.assertEqual(3, self.robot.available_capacity)

        result = self.robot.update(3.01, 2)

        self.assertEqual("Robot 404 was not updated.", result)

        self.assertEqual([3.14], self.robot.software_updates)
        self.assertEqual(3, self.robot.available_capacity)

    def test_update_not_enough_capacity_return_msg(self):
        self.robot.update(3.14, 2)
        self.assertEqual([3.14], self.robot.software_updates)
        self.assertEqual(3, self.robot.available_capacity)

        result = self.robot.update(3.15, 4)

        self.assertEqual("Robot 404 was not updated.", result)

        self.assertEqual([3.14], self.robot.software_updates)
        self.assertEqual(3, self.robot.available_capacity)

    def test_gt_method_when_self_robot_is_more_expensive(self):
        robot1 = Robot('001', 'Entertainment', 100, 1000.0)
        robot2 = Robot('002', 'Education', 120, 800.0)
        result = robot1 > robot2
        self.assertEqual(result, "Robot with ID 001 is more expensive than Robot with ID 002.")

    def test_gt_method_when_self_robot_is_equal_price(self):
        robot1 = Robot('001', 'Entertainment', 100, 1000.0)
        robot2 = Robot('002', 'Education', 120, 1000.0)
        result = robot1 > robot2
        self.assertEqual(result, "Robot with ID 001 costs equal to Robot with ID 002.")

    def test_gt_method_when_self_robot_is_cheaper(self):
        robot1 = Robot('001', 'Entertainment', 100, 800.0)
        robot2 = Robot('002', 'Education', 120, 1000.0)
        result = robot1 > robot2
        self.assertEqual(result, "Robot with ID 001 is cheaper than Robot with ID 002.")


if __name__ == "__main__":
    unittest.main()