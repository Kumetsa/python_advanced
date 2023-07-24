import unittest


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

import unittest


class WorkerTest(unittest.TestCase):
    def test_object_is_initialized_correctly(self):
        # Act
        worker = Worker("Test", 1000, 60)
        # Assert
        self.assertEqual("Test", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(60, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_works(self):
        worker = Worker("Test", 1000, 60)

        # Arrange
        self.assertEqual(0, worker.money)
        self.assertEqual(60, worker.energy)

        # Act
        worker.work()

        # Assert
        current_expected_money = 1000
        self.assertEqual(current_expected_money, worker.money)

        expected_energy = 60 - 1
        self.assertEqual(expected_energy, worker.energy)

        worker.work()
        # Worker works again
        current_expected_money = 1000 + 1000
        self.assertEqual(current_expected_money, worker.money)

        expected_energy = 60 - 2
        self.assertEqual(expected_energy, worker.energy)

    def test_worker_has_no_energy_can_not_work(self):
        worker = Worker("test2", 1000, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_cannot_work_if_negative_energy(self):
        worker = Worker("test2", 1000, -1)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_energy_is_increased_from_rest(self):
        worker = Worker("test2", 1000, 60)
        self.assertEqual(60, worker.energy)

        worker.rest()
        self.assertEqual(61, worker.energy)

        worker.rest()
        self.assertEqual(62, worker.energy)

    def test_get_info(self):
        worker = Worker("test2", 1000, 60)

        result = worker.get_info()

        expected_result = 'test2 has saved 0 money.'

        self.assertEqual(expected_result, result)

        worker.work()
        result = worker.get_info()
        expected_result = 'test2 has saved 1000 money.'
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
