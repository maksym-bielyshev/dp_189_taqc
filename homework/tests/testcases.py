"""Test cases for the two functions."""

import unittest
from unittest import TestCase
from homework.tests.calculation import add, subtract


class TestAdd(TestCase):
    """Test cases for the function 'add'."""

    def test_all_arguments_are_greater_than_zero(self):
        """Test function with arguments that are greater than zero.

        :return: True or AssertionError
        """
        result = add(2, 1)
        self.assertEqual(result, 3)

    def test_all_arguments_are_less_than_zero(self):
        """Test function with arguments that are less than zero.

        :return: True or AssertionError
        """
        result = add(-2, -3)
        self.assertEqual(result, -5)

    def test_at_least_one_argument_is_zero(self):
        """Test function with at least one argument is zero.

        :return: True or AssertionError
        """
        result = add(4, 0)
        self.assertEqual(result, 4)


class TestSubtract(TestCase):
    """Test cases for the function 'subtract'."""

    def test_all_arguments_are_greater_than_zero(self):
        """Test function with arguments that are greater than zero.

        :return: True or AssertionError
        """
        result = subtract(2, 1)
        self.assertEqual(result, 1)

    def test_all_arguments_are_less_than_zero(self):
        """Test function with arguments that are less than zero.

        :return: True or AssertionError
        """
        result = subtract(-2, -3)
        self.assertEqual(result, 1)

    def test_at_least_one_argument_is_zero(self):
        """Test function with at least one argument is zero.

        :return: True or AssertionError
        """
        result = subtract(4, 0)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
