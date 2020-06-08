import unittest
from unittest import TestCase
from homework.tests.calculation import add, subtract


class TestAdd(TestCase):
    def test_all_arguments_are_greater_than_zero(self):
        result = add(2, 1)
        self.assertEqual(result, 3)

    def test_all_arguments_are_less_than_zero(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

    def test_at_least_one_argument_is_zero(self):
        result = add(4, 0)
        self.assertEqual(result, 4)


class TestSubtract(TestCase):
    def test_all_arguments_are_greater_than_zero(self):
        result = subtract(2, 1)
        self.assertEqual(result, 1)

    def test_all_arguments_are_less_than_zero(self):
        result = subtract(-2, -3)
        self.assertEqual(result, 1)

    def test_at_least_one_argument_is_zero(self):
        result = subtract(4, 0)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
