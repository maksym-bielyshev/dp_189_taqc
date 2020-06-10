"""Module 'num2words' testing."""

import unittest
from unittest import TestCase
from num_to_words_converter import num2words


class TestNum2Words(TestCase):
    """Test case for the function 'num2words'."""

    def test_positive(self):
        """Test function 'num2words' with argument that are greater than zero.

        :return: True or AssertionError
        """
        result = num2words('1')
        self.assertEqual(result, 'one')

    def test_negative(self):
        """Test function 'num2words' with argument that are less than zero.

        :return: True or AssertionError
        """
        result = num2words('-1')
        self.assertEqual(result, 'minus one')

    def test_positive_from_zero_to_one(self):
        """Test function with argument that between zero and one.

        :return: True or AssertionError
        """
        result = num2words('0.5')
        self.assertEqual(result, 'zero point five')

    def test_negative_from_zero_to_one(self):
        """Test function with argument that between zero and minus one.

        :return: True or AssertionError
        """
        result = num2words('-0.5')
        self.assertEqual(result, 'minus zero point five')


if __name__ == '__main__':
    unittest.main()
