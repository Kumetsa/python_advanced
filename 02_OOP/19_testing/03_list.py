import unittest
from unittest import TestCase


#
#
# class IntegerList:
#     def __init__(self, *args):
#         self.__data = []
#         for x in args:
#             if type(x) == int:
#                 self.__data.append(x)
#
#     def get_data(self):
#         return self.__data
#
#     def add(self, element):
#         if not type(element) == int:
#             raise ValueError("Element is not Integer")
#         self.get_data().append(element)
#         return self.get_data()
#
#     def remove_index(self, index):
#         if index >= len(self.get_data()):
#             raise IndexError("Index is out of range")
#         a = self.get_data()[index]
#         del self.get_data()[index]
#         return a
#
#     def get(self, index):
#         if index >= len(self.get_data()):
#             raise IndexError("Index is out of range")
#         return self.get_data()[index]
#
#     def insert(self, index, el):
#         if index >= len(self.get_data()):
#             raise IndexError("Index is out of range")
#         elif not type(el) == int:
#             raise ValueError("Element is not Integer")
#
#         self.get_data().insert(index, el)
#
#     def get_biggest(self):
#         a = sorted(self.get_data(), reverse=True)
#         return a[0]
#
#     def get_index(self, el):
#         return self.get_data().index(el)


class IntegerListTest(TestCase):
    def test_init_list_all_int(self):
        integer = IntegerList(4, 5, 6)
        self.assertEqual(3, len(integer.get_data()))

    def test_init_list_not_integers_not_added(self):
        integer = IntegerList(4, 5, 6.5)
        self.assertEqual(2, len(integer.get_data()))
        self.assertEqual([4, 5], integer.get_data())

    def test_get_data_returns_list_elements(self):
        integer = IntegerList(4, 5, 6)
        self.assertEqual([4, 5, 6], integer.get_data())

    def test_add_method_not_int_raises(self):
        integer = IntegerList(4, 5, 6)
        self.assertEqual(3, len(integer.get_data()))

        test_data_values = [4.6, "asd", {}, [], True]
        for value in test_data_values:
            with self.assertRaises(ValueError) as ex:
                integer.add(value)
                self.assertEqual("Element is not Integer", str(ex.exception))

        self.assertEqual(3, len(integer.get_data()))

    def test_add_method_add_int_adds_element(self):
        integer = IntegerList(4, 5, 6)

        self.assertEqual(3, len(integer.get_data()))

        result = integer.add(7)
        self.assertEqual(4, len(integer.get_data()))
        self.assertIn(7, integer.get_data())
        self.assertEqual([4, 5, 6, 7], result)

    def test_remove_index_invalid_raises(self):
        integer = IntegerList(4, 5, 6)
        self.assertEqual(3, len(integer.get_data()))
        with self.assertRaises(IndexError) as ex:
            integer.remove_index(4)
        self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual(3, len(integer.get_data()))

    def test_remove_index_removes_element(self):
        integer = IntegerList(4, 5, 6)
        self.assertEqual(3, len(integer.get_data()))
        self.assertEqual(4, integer.get_data()[0])

        result = integer.remove_index(0)
        self.assertEqual(4, result)
        self.assertEqual(5, integer.get_data()[0])
        self.assertEqual(2, len(integer.get_data()))

    def test_get_invalid_index_raise(self):
        integer = IntegerList(4, 5, 6)
        self.assertEqual(3, len(integer.get_data()))

        with self.assertRaises(IndexError) as ex:
            integer.get(4)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_valid_index(self):
        integer = IntegerList(4, 5, 6)
        self.assertEqual(3, len(integer.get_data()))

        element = integer.get(2)
        self.assertEqual(6, element)

    def test_insert_invalid_index_raises(self):
        integer = IntegerList(4, 5, 6)
        self.assertEqual(3, len(integer.get_data()))

        with self.assertRaises(IndexError) as ex:
            integer.insert(4, 7)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(3, len(integer.get_data()))

    def test_insert_element_not_int(self):
        integer = IntegerList(4, 5, 6)
        self.assertEqual(3, len(integer.get_data()))

        with self.assertRaises(ValueError) as ex:
            integer.insert(0, 5.6)
        self.assertEqual("Element is not Integer", str(ex.exception))

        self.assertEqual(3, len(integer.get_data()))

    def test_insert(self):
        integer = IntegerList(4, 5, 6)
        self.assertEqual(3, len(integer.get_data()))

        self.assertEqual([4, 5, 6], integer.get_data())
        self.assertEqual([4, 5, 6], integer._IntegerList__data)

        integer.insert(0, 100)

        self.assertEqual(4, len(integer.get_data()))

        self.assertEqual([100, 4, 5, 6], integer.get_data())
        self.assertEqual([100, 4, 5, 6], integer._IntegerList__data)

    def test_get_biggest(self):
        integer = IntegerList(0, 12, -3)
        result = integer.get_biggest()

        self.assertEqual(12, result)

    def test_get_index(self):
        integer = IntegerList(4, 5, 6)

        self.assertEqual(4, integer.get_data()[0])

        result = integer.get_index(4)
        self.assertEqual(0, result)


if __name__ == "__main__":
    unittest.main()
