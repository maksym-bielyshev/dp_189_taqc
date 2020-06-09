"""Application testing."""

import unittest
from unittest import TestCase
from homework.pairs.app import search_pairs


class TestSearchPairs(TestCase):
    """Test case for the function 'search_pairs'."""

    def test_all_arguments_are_greater_than_zero(self):
        """Test function with arguments that are greater than zero.

        :return: True or AssertionError
        """
        result = search_pairs([1, 2, 3, 4, 5, 5, 6, 7], 10)
        self.assertEqual(result, ['5 + 5', '6 + 4', '7 + 3'])

    def test_all_arguments_are_less_than_zero(self):
        """Test function with arguments that are less than zero.

        :return: True or AssertionError
        """
        result = search_pairs([-1, -2, -3, -4, -5, -5, -6, -7], -10)
        self.assertEqual(result, ['-5 + -5', '-6 + -4', '-7 + -3'])

    def test_no_suitable_pairs(self):
        """Test function with arguments that are not suitable for displaying.

        :return: True or AssertionError
        """
        result = search_pairs([0, 0], 10)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
