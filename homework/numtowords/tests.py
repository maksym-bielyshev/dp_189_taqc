"""Module 'num2words' testing."""

import unittest
from unittest import TestCase
from num_to_words_converter import num2words_fixed_minus_zero_one


class NumToWords(TestCase):
    """Test case for the function 'num2words_fixed_minus_zero_one'."""

    def test_positive(self):
        """Test function with arguments that are greater than zero.

        :return: True or AssertionError
        """
        result = num2words_fixed_minus_zero_one('1')
        self.assertEqual(result, 'one')

    def test_negative(self):
        """Test function with arguments that are less than zero.

        :return: True or AssertionError
        """
        result = num2words_fixed_minus_zero_one('-1')
        self.assertEqual(result, 'minus one')

    def test_negative_from_zero_to_one(self):
        """Test function with arguments that are not suitable for displaying.

        :return: True or AssertionError
        """
        result = num2words_fixed_minus_zero_one('-0.5')
        self.assertEqual(result, 'minus zero point five')


if __name__ == '__main__':
    unittest.main()
